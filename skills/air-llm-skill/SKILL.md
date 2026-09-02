---
name: air-llm-skill
description: Comprehensive skill for installing Apple Silicon MLX and AirLLM, managing layer-wise inference for 70B/405B/MoE models, and deploying an OpenAI-compatible FastAPI server.
---

# AirLLM & MLX Inference Skill

This skill provides step-by-step instructions, runbooks, and automation scripts to install, configure, and operate **AirLLM** and **MLX** for massive LLM inference (70B, 405B, 671B DeepSeek-V3, 2.8T Kimi K3) on single consumer GPUs or Apple Silicon Macs, and serve them via a full OpenAI-compatible API.

## Core Capabilities

1. **Environment Installation**: Automated setup for Apple Silicon (MLX + PyTorch + AirLLM) and Linux (CUDA + bitsandbytes).
2. **Layer-Wise Inference**: Running 70B models in ~4GB VRAM and 405B models in ~8GB VRAM without quality-degrading quantization.
3. **Full OpenAI-Compatible API**: Deploying a local FastAPI server exposing `/v1/chat/completions`, `/v1/completions`, `/v1/models`, and `/health`.
4. **Performance Tuning & Storage Management**: Block-wise quantization (`4bit`/`8bit`), prefetching, and disk shard management.

---

## 1. Quick Setup & Installation

### Option A: Using the Automated Install Script
Run the bundled script to create a virtual environment and install all necessary dependencies (detects macOS vs Linux automatically):

```bash
chmod +x ~/.gemini/config/skills/air-llm-skill/scripts/install_env.sh
./~/.gemini/config/skills/air-llm-skill/scripts/install_env.sh
```

### Option B: Manual Installation

#### On macOS (Apple Silicon M1/M2/M3/M4):
```bash
python3 -m venv .venv-airllm
source .venv-airllm/bin/activate

pip install -U pip wheel setuptools
pip install -U mlx torch torchvision torchaudio
pip install -U airllm safetensors "transformers>=4.43.3" accelerate optimum huggingface-hub fastapi uvicorn pydantic requests
```

#### On Linux / Windows (NVIDIA CUDA):
```bash
python3 -m venv .venv-airllm
source .venv-airllm/bin/activate

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -U airllm bitsandbytes safetensors "transformers>=4.43.3" accelerate optimum huggingface-hub fastapi uvicorn pydantic requests
```

---

## 2. Running Standalone Inference in Python

```python
from airllm import AutoModel
import torch

# 1. Initialize AutoModel (auto-detects architecture: Llama, Qwen, DeepSeek, etc.)
model = AutoModel.from_pretrained(
    "garage-bAInd/Platypus2-70B-instruct",  # or "unsloth/Meta-Llama-3.1-405B-Instruct-bnb-4bit"
    compression='4bit',                     # '4bit' or '8bit' block-wise quantization for 3x disk speedup
    delete_original=True,                   # Deletes original raw download to save 50% disk space
    prefetching=True                        # Overlaps disk loading with GPU compute
)

# 2. Tokenize Input
prompt = "Explain quantum computing in simple terms."
inputs = model.tokenizer(
    [prompt],
    return_tensors="pt",
    return_attention_mask=False,
    truncation=True,
    max_length=512,
    padding=False
)

# 3. Target GPU if CUDA available
if torch.cuda.is_available():
    input_ids = inputs['input_ids'].cuda()
else:
    input_ids = inputs['input_ids']

# 4. Generate
output = model.generate(
    input_ids,
    max_new_tokens=100,
    use_cache=True,
    return_dict_in_generate=True
)

generated_text = model.tokenizer.decode(output.sequences[0], skip_special_tokens=True)
print(generated_text)
```

---

## 3. Serving AirLLM as a Full OpenAI-Compatible API Server

The skill includes a ready-to-run FastAPI server supporting standard OpenAI endpoints (`/v1/chat/completions`, `/v1/completions`, `/v1/models`, `/health`).

### Starting the Server:

```bash
source .venv-airllm/bin/activate

# Start server on port 8000
python3 ~/.gemini/config/skills/air-llm-skill/scripts/api_server.py \
    --model "garage-bAInd/Platypus2-70B-instruct" \
    --compression 4bit \
    --port 8000 \
    --host 0.0.0.0
```

### Supported API Arguments:
- `--model`: Hugging Face repo ID or local checkpoint path.
- `--compression`: `4bit`, `8bit`, or `none`.
- `--hf-token`: Hugging Face API token for gated repos (e.g., Llama-3-70B).
- `--shards-path`: Custom SSD directory for storing layer shards.
- `--no-delete-original`: Keep original download files.
- `--port`: Port number (default `8000`).
- `--host`: Host to bind (default `0.0.0.0`).

### Testing the API Server:

#### 1. Using curl (Chat Completions):
```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "garage-bAInd/Platypus2-70B-instruct",
    "messages": [
      {"role": "system", "content": "You are a helpful coding assistant."},
      {"role": "user", "content": "Write a Python script to sort a dictionary by value."}
    ],
    "max_tokens": 150
  }'
```

#### 2. Using Python OpenAI SDK:
```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="garage-bAInd/Platypus2-70B-instruct",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=64
)

print(response.choices[0].message.content)
```

#### 3. Using the Built-in Test Client:
```bash
python3 ~/.gemini/config/skills/air-llm-skill/scripts/client.py --prompt "Explain the theory of relativity briefly." --max-tokens 100
```

---

## 4. Key Troubleshooting Points

1. **Out of Disk Space during splitting (`SafetensorError: MetadataIncompleteBuffer`)**:
   - Model splitting stores shards locally. Ensure at least 1.5x model size free space, or specify `--shards-path /path/to/external/nvme`.
2. **RoPE scaling error (`rope_scaling must be a dictionary`)**:
   - Requires `transformers >= 4.43.3` for Llama 3.1 / 3.2.
3. **Missing padding token**:
   - Always initialize tokenizer with `padding=False` or assign `tokenizer.pad_token = tokenizer.eos_token`.
4. **Gated models (401 Client Error)**:
   - Provide `--hf-token <YOUR_TOKEN>` or set `export HF_TOKEN=...`.
