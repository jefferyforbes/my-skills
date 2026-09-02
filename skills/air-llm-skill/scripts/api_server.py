#!/usr/bin/env python3
"""
AirLLM OpenAI-Compatible FastAPI Server
Provides /v1/chat/completions, /v1/completions, /v1/models, and /health endpoints.
Runs large models (70B, 405B, etc.) via AirLLM layer-wise streaming with serialized queueing.
"""

import argparse
import asyncio
import os
import sys
import time
import uuid
from typing import List, Optional, Dict, Any, Union

from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel, Field
import uvicorn

# Global state
app = FastAPI(
    title="AirLLM OpenAI-Compatible Inference API",
    description="Layer-wise streaming LLM server supporting 70B, 405B, and MoE models on consumer hardware.",
    version="1.0.0"
)

MODEL_HOLDER: Dict[str, Any] = {
    "model": None,
    "model_name": None,
    "lock": None,  # Async lock for thread-safe serialized layer streaming
    "loaded_at": None,
    "device": "cpu"
}


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: Optional[str] = None
    messages: List[ChatMessage]
    max_tokens: Optional[int] = Field(default=256, alias="max_new_tokens")
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 0.9
    stream: Optional[bool] = False


class CompletionRequest(BaseModel):
    model: Optional[str] = None
    prompt: Union[str, List[str]]
    max_tokens: Optional[int] = Field(default=256, alias="max_new_tokens")
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 0.9
    stream: Optional[bool] = False


def load_airllm_model(
    model_name: str,
    compression: Optional[str] = "4bit",
    hf_token: Optional[str] = None,
    shards_path: Optional[str] = None,
    delete_original: bool = True,
    prefetching: bool = True
):
    print(f"[AirLLM Server] Loading model '{model_name}' (compression={compression})...")
    import torch
    from airllm import AutoModel

    device = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")
    print(f"[AirLLM Server] Using target device: {device}")

    kwargs: Dict[str, Any] = {
        "delete_original": delete_original,
        "prefetching": prefetching,
    }
    if not torch.cuda.is_available() and compression in ["4bit", "8bit"]:
        print(f"[AirLLM Server] Note: CUDA is not available. Setting compression=None for native Apple Silicon MLX layer-wise streaming.")
        compression = None

    if compression in ["4bit", "8bit"]:
        kwargs["compression"] = compression
    if hf_token:
        kwargs["hf_token"] = hf_token
    if shards_path:
        kwargs["layer_shards_saving_path"] = shards_path

    model = AutoModel.from_pretrained(model_name, **kwargs)
    
    # Configure tokenizer padding safely
    if model.tokenizer.pad_token is None:
        if model.tokenizer.eos_token is not None:
            model.tokenizer.pad_token = model.tokenizer.eos_token
        else:
            model.tokenizer.add_special_tokens({'pad_token': '[PAD]'})

    MODEL_HOLDER["model"] = model
    MODEL_HOLDER["model_name"] = model_name
    MODEL_HOLDER["loaded_at"] = time.time()
    MODEL_HOLDER["device"] = device
    MODEL_HOLDER["lock"] = asyncio.Lock()
    print(f"[AirLLM Server] Successfully initialized {model_name}!")
    return model


def format_chat_messages(messages: List[ChatMessage], tokenizer) -> str:
    """Format chat messages using tokenizer chat template if available, else standard fallback."""
    try:
        if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template:
            dicts = [{"role": m.role, "content": m.content} for m in messages]
            return tokenizer.apply_chat_template(dicts, tokenize=False, add_generation_prompt=True)
    except Exception:
        pass

    # Fallback prompt format
    formatted = ""
    for msg in messages:
        formatted += f"<|im_start|>{msg.role}\n{msg.content}<|im_end|>\n"
    formatted += "<|im_start|>assistant\n"
    return formatted


def run_inference_sync(prompt: str, max_new_tokens: int) -> str:
    """Synchronously run AirLLM layer-wise inference supporting both PyTorch and MLX."""
    import torch
    model = MODEL_HOLDER["model"]
    tokenizer = model.tokenizer

    input_tokens = tokenizer(
        [prompt],
        return_tensors="pt",
        return_attention_mask=False,
        truncation=True,
        max_length=2048,
        padding=False
    )

    is_mlx = getattr(model, "__class__", None).__name__ == "AirLLMLlamaMlx"
    if is_mlx:
        import mlx.core as mx
        mlx_input = mx.array(input_tokens["input_ids"].numpy())
        generation_output = model.generate(mlx_input, max_new_tokens=max_new_tokens)
    else:
        if torch.cuda.is_available():
            input_ids = input_tokens["input_ids"].cuda()
        else:
            input_ids = input_tokens["input_ids"]

        generation_output = model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            use_cache=True,
            return_dict_in_generate=True
        )

    if isinstance(generation_output, str):
        full_output = generation_output
    elif hasattr(generation_output, "sequences"):
        full_output = tokenizer.decode(generation_output.sequences[0], skip_special_tokens=True)
    elif isinstance(generation_output, (list, tuple)):
        full_output = tokenizer.decode(generation_output[0], skip_special_tokens=True)
    else:
        full_output = tokenizer.decode(generation_output, skip_special_tokens=True)

    # Strip prompt prefix if echoed
    if full_output.startswith(prompt):
        generated_part = full_output[len(prompt):].strip()
    else:
        generated_part = full_output
    return generated_part


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model_loaded": MODEL_HOLDER["model"] is not None,
        "model_name": MODEL_HOLDER["model_name"],
        "device": MODEL_HOLDER["device"]
    }


@app.get("/v1/models")
async def list_models():
    model_id = MODEL_HOLDER["model_name"] or "airllm-model"
    return {
        "object": "list",
        "data": [
            {
                "id": model_id,
                "object": "model",
                "created": int(MODEL_HOLDER.get("loaded_at") or time.time()),
                "owned_by": "airllm"
            }
        ]
    }


@app.post("/v1/chat/completions")
async def chat_completions(req: ChatCompletionRequest):
    if MODEL_HOLDER["model"] is None:
        raise HTTPException(status_code=503, detail="AirLLM model not loaded yet.")

    tokenizer = MODEL_HOLDER["model"].tokenizer
    prompt_str = format_chat_messages(req.messages, tokenizer)
    max_tokens = req.max_tokens or 256
    req_id = f"chatcmpl-{uuid.uuid4().hex[:12]}"

    # Serialize generation via lock to avoid layer-swapping collisions
    async with MODEL_HOLDER["lock"]:
        loop = asyncio.get_event_loop()
        generated_text = await loop.run_in_executor(
            None, run_inference_sync, prompt_str, max_tokens
        )

    return {
        "id": req_id,
        "object": "chat.completion",
        "created": int(time.time()),
        "model": req.model or MODEL_HOLDER["model_name"],
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": generated_text
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": len(prompt_str.split()),
            "completion_tokens": len(generated_text.split()),
            "total_tokens": len(prompt_str.split()) + len(generated_text.split())
        }
    }


@app.post("/v1/completions")
async def text_completions(req: CompletionRequest):
    if MODEL_HOLDER["model"] is None:
        raise HTTPException(status_code=503, detail="AirLLM model not loaded yet.")

    prompt_str = req.prompt if isinstance(req.prompt, str) else req.prompt[0]
    max_tokens = req.max_tokens or 256
    req_id = f"cmpl-{uuid.uuid4().hex[:12]}"

    async with MODEL_HOLDER["lock"]:
        loop = asyncio.get_event_loop()
        generated_text = await loop.run_in_executor(
            None, run_inference_sync, prompt_str, max_tokens
        )

    return {
        "id": req_id,
        "object": "text_completion",
        "created": int(time.time()),
        "model": req.model or MODEL_HOLDER["model_name"],
        "choices": [
            {
                "text": generated_text,
                "index": 0,
                "logprobs": None,
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": len(prompt_str.split()),
            "completion_tokens": len(generated_text.split()),
            "total_tokens": len(prompt_str.split()) + len(generated_text.split())
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Start AirLLM OpenAI-Compatible API Server")
    parser.add_argument("--model", type=str, default="garage-bAInd/Platypus2-70B-instruct", help="HuggingFace model ID or local path")
    parser.add_argument("--compression", type=str, default="4bit", choices=["4bit", "8bit", "none"], help="Block-wise quantization")
    parser.add_argument("--hf-token", type=str, default=os.getenv("HF_TOKEN", None), help="Hugging Face API token")
    parser.add_argument("--shards-path", type=str, default=None, help="Custom folder for layer shards")
    parser.add_argument("--no-delete-original", action="store_true", help="Keep original checkpoint after splitting")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address to bind")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on")
    
    args = parser.parse_args()

    compression = None if args.compression == "none" else args.compression
    load_airllm_model(
        model_name=args.model,
        compression=compression,
        hf_token=args.hf_token,
        shards_path=args.shards_path,
        delete_original=not args.no_delete_original,
        prefetching=True
    )

    print(f"\n[AirLLM Server] Running on http://{args.host}:{args.port}")
    print(f"[AirLLM Server] OpenAI Chat Endpoint: http://{args.host}:{args.port}/v1/chat/completions\n")
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
