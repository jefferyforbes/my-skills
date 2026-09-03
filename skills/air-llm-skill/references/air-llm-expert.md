# AirLLM Expert Sub-Agent Knowledge Base & Definition

> **Sub-Agent Name:** `air-llm-expert`  
> **Trigger Keywords:** `"air llm"`, `"air-llm"`, `"airllm"`, `"70B on 4GB"`, `"405B inference"`,
`"layer-wise LLM inference"`, `"MLX AirLLM"`  
> **Scope:** Antigravity / Gemini sub-agent and specialized pair-programmer for running large
> language models (70B, 405B, 671B MoE, 2.8T MoE) on memory-constrained hardware (Apple Silicon / MLX,
> single consumer GPUs, CPU).

---

## 1. Sub-Agent Overview & System Instructions

### Identity & Purpose

`air-llm-expert` is a specialized engineering sub-agent that guides users through running massive
open-weights foundation models on resource-constrained consumer machines without needing multi-GPU
clusters. It provides expert architectural analysis, environment setup, code generation, debugging,
performance tuning, and API serving for the **AirLLM** and **Apple MLX** ecosystems.

### System Prompt for `air-llm-expert`

```markdown
You are the AirLLM Expert, an authoritative technical assistant specializing in running ultra-large
language models (70B to 405B+ parameters and sparse MoEs up to 2.8T) on single consumer GPUs, Apple
Silicon MacBooks (via MLX/MPS), and low-memory environments.

Your responsibilities:

1. Explain AirLLM layer-wise streaming architecture, memory footprints, and disk-throughput
   trade-offs.
2. Guide users in setting up Apple Silicon (macOS + MLX + PyTorch) and Linux (CUDA + bitsandbytes)
   environments.
3. Configure `AutoModel.from_pretrained` with optimal settings (`compression='4bit'|'8bit'`,
   `prefetching`, `delete_original`, `layer_shards_saving_path`, `hf_token`).
4. Implement and manage full OpenAI-compatible API servers (FastAPI) powered by AirLLM.
5. Diagnose and fix common AirLLM failure modes: OOM / disk space issues (
   `MetadataIncompleteBuffer`), rope_scaling mismatches, missing padding tokens, gated repository
   auth, and tokenizer edge-cases.
```

---

## 2. Core Architecture & How AirLLM Works

### Layer-Wise Inference (Streaming Execution)

Conventional inference frameworks require the entire model weight matrix to reside simultaneously in
VRAM (e.g., ~140GB for 70B in FP16, ~800GB for 405B).
AirLLM eliminates this requirement by decomposing the model into isolated layer shards:

1. **Model Sharding / Splitting:** On first run, the full checkpoint is deserialized layer-by-layer
   and converted into discrete safetensors shards on disk.
2. **Sequential Streaming:** During token generation, only **one transformer layer** (or one active
   expert in sparse MoEs) is loaded from NVMe SSD into GPU memory at any single moment.
3. **Activation Passing:** Hidden states and key-value tensors flow through the active layer in
   VRAM, compute output activations, and unload the layer before streaming the next layer into VRAM.
4. **VRAM Footprint:** The memory requirement is strictly bounded by the size of the single largest
   layer + context KV cache, rather than total parameter count.

```
       [ Input Prompt Tokens ]
                  │
                  ▼
┌───────────────────────────────────────┐
│ Host NVMe Disk (Layer Shards)         │
│  [Layer 0] [Layer 1] ... [Layer N-1]  │
└──────┬──────────────────────▲─────────┘
       │ Stream In            │ Stream Out / Overwrite
       ▼                      │
┌───────────────────────────────────────┐
│ GPU / Unified VRAM (Single Layer)     │
│       Compute Hidden States           │
└───────────────────────────────────────┘
                  │
                  ▼
       [ Output Token Generation ]
```

### MoE Sparse Streaming (DeepSeek-V3 & Kimi K3)

In Mixture-of-Experts (MoE) architectures, each token only activates a subset of experts per layer:

- **DeepSeek-V3 (671B):** Runs in ~12GB VRAM.
- **Kimi K3 (2.8T):** Runs in ~3.72GB VRAM on a single GPU by streaming only the specific routed
  experts per token dynamically from disk using `compressed-tensors` and `flash-attn`.

### Block-Wise Model Compression (3x Speedup)

- **Disk Bottleneck:** In layer-wise streaming, inference speed is strictly bounded by disk-to-GPU
  transfer bandwidth.
- **Block-Wise Quantization:** Uses `bitsandbytes` to compress layer weight shards on disk to
  4-bit (`NF4`/`FP4`) or 8-bit (`INT8`).
- **Advantage:** Because only weights are quantized on disk (activations remain full precision
  during computation), perplexity degradation is negligible while loading time is reduced up to 3x.

---

## 3. Supported Model Families

AirLLM provides a unified `AutoModel` interface that automatically inspects model configuration and
loads the appropriate architecture:

| Model Family          | Key Models                                                                                          | VRAM Requirement                                           |
|:----------------------|:----------------------------------------------------------------------------------------------------|:-----------------------------------------------------------|
| **Llama Series**      | Llama 2 (7B, 13B, 70B), Llama 3/3.1/3.3 (8B, 70B, 405B), Llama 4                                    | ~4GB for 70B, ~8GB for 405B (4-bit)                        |
| **Qwen Series**       | Qwen 2, 2.5, 3, 3.8-27B Dense VL (3.33GB), Qwen 3.8-Flash-Next 125B MoE (5.95GB), Qwen3-235B (~3GB) | ~3GB to ~6GB                                               |
| **DeepSeek Series**   | DeepSeek-V2, DeepSeek-V3 (671B), DeepSeek-R1                                                        | ~12GB                                                      |
| **Kimi Series**       | Kimi K3 (2.8T MoE)                                                                                  | ~3.72GB (requires CUDA 12, flash-attn, compressed-tensors) |
| **Mistral / Mixtral** | Mistral-7B, Mixtral 8x7B, Mixtral 8x22B                                                             | ~4GB to ~8GB                                               |
| **Others**            | Gemma, Gemma 2, Phi-3/Phi-4, ChatGLM3, Baichuan2, InternLM2, Yi                                     | ~4GB                                                       |

---

## 4. Platform Setup & Installation

### macOS (Apple Silicon + MLX)

AirLLM on macOS leverages Apple Silicon's Unified Memory Architecture and MLX for optimized tensor
acceleration:

```bash
# 1. Ensure Native ARM64 Python (Python 3.10 or 3.11 recommended)
python3 -m venv .venv-airllm
source .venv-airllm/bin/activate

# 2. Install MLX (Apple Silicon array framework) and PyTorch
pip install -U pip
pip install mlx torch torchvision torchaudio

# 3. Install AirLLM and dependencies
pip install -U airllm safetensors transformers accelerate optimum huggingface-hub
```

### Linux (NVIDIA CUDA)

```bash
# 1. Create Virtual Environment
python3 -m venv .venv-airllm
source .venv-airllm/bin/activate

# 2. Install PyTorch with CUDA Support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# 3. Install AirLLM, bitsandbytes, and acceleration libraries
pip install -U airllm bitsandbytes safetensors transformers accelerate optimum
```

---

## 5. Configurations & Parameter Reference

When invoking `AutoModel.from_pretrained(repo_id_or_path, **kwargs)`, the following configuration
options are supported:

```python
from airllm import AutoModel

model = AutoModel.from_pretrained(
    "unsloth/Meta-Llama-3.1-405B-Instruct-bnb-4bit",
    compression='4bit',               # '4bit', '8bit', or None
    profiling_mode=False,             # Set True to output layer-by-layer timing
    layer_shards_saving_path=None,    # Custom directory for layer shards (e.g., "/Volumes/FastSSD/shards")
    hf_token=None,                    # Hugging Face token string for gated repos
    prefetching=True,                 # Overlaps disk load with GPU compute (Llama models)
    delete_original=True              # Deletes original HF download after splitting to save 50% disk space
)
```

### Generation Syntax

```python
MAX_LENGTH = 512
input_text = ["Explain quantum computing in three sentences."]

input_tokens = model.tokenizer(
    input_text,
    return_tensors="pt",
    return_attention_mask=False,
    truncation=True,
    max_length=MAX_LENGTH,
    padding=False
)

# If running on CUDA:
input_ids = input_tokens['input_ids'].cuda()
# If running on Apple Silicon / CPU:
# input_ids = input_tokens['input_ids']

generation_output = model.generate(
    input_ids,
    max_new_tokens=100,
    use_cache=True,
    return_dict_in_generate=True
)

output_text = model.tokenizer.decode(generation_output.sequences[0], skip_special_tokens=True)
print(output_text)
```

---

## 6. Common Issues & Troubleshooting Runbook

### 1. `SafetensorError: Error while deserializing header: MetadataIncompleteBuffer`

- **Root Cause:** Insufficient disk space during the layer splitting stage.
- **Fix:** Ensure free disk space is at least 1.5x the model weight size. Set `delete_original=True`
  or redirect `layer_shards_saving_path` to an external NVMe drive. Clear cached incomplete files
  from `~/.cache/huggingface/hub/`.

### 2. `ValueError: rope_scaling must be a dictionary with two fields, type and factor`

- **Root Cause:** Llama 3.1 / 3.2 uses updated RoPE configuration incompatible with older
  `transformers`.
- **Fix:** Upgrade transformers:
  ```bash
  pip install -U "transformers>=4.43.3"
  ```

### 3. `ValueError: Asking to pad but the tokenizer does not have a padding token`

- **Root Cause:** Tokenizers for models like Llama 3 do not assign a default pad token.
- **Fix:** Pass `padding=False` to `model.tokenizer(...)` or explicitly assign
  `model.tokenizer.pad_token = model.tokenizer.eos_token`.

### 4. `401 Client Error / Repository is Gated`

- **Root Cause:** Gated models (e.g., `meta-llama/Meta-Llama-3-70B`) require Hugging Face terms
  acceptance.
- **Fix:** Pass `hf_token="hf_..."` or run `huggingface-cli login`.

### 5. `ValueError: max() arg is an empty sequence`

- **Root Cause:** Using model-specific classes like `AirLLMLlama2` for models of different
  families (ChatGLM, QWen, etc.).
- **Fix:** Always use `from airllm import AutoModel` to let the library automatically dispatch the
  correct architecture parser.

---

## 7. Integration with Antigravity Skills

The sub-agent `air-llm-expert` integrates directly with the workspace skill located at:

- `.agent/skills/air-llm-skill/SKILL.md` (and `.agent/skills/air-llm-skill.md`)
- Helper scripts: `.agent/skills/air-llm-skill/scripts/` (Automated environment setup, FastAPI
  OpenAI-compatible server, CLI tester).
