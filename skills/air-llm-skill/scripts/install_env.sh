#!/usr/bin/env bash
set -euo pipefail

# AirLLM & MLX Automated Environment Setup Script
# Works on macOS (Apple Silicon + MLX) and Linux (NVIDIA CUDA)

echo "=============================================="
echo " Setting up AirLLM & MLX Inference Environment"
echo "=============================================="

OS_TYPE="$(uname -s)"
ARCH_TYPE="$(uname -m)"

VENV_DIR="${VENV_DIR:-.venv-airllm}"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment at $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
fi

echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

pip install -U pip wheel setuptools

if [ "$OS_TYPE" = "Darwin" ]; then
    echo "Detected macOS ($ARCH_TYPE)."
    if [ "$ARCH_TYPE" = "arm64" ]; then
        echo "Installing Apple Silicon MLX and PyTorch..."
        pip install -U mlx torch torchvision torchaudio
    else
        echo "Warning: Intel Mac detected. MLX is only supported on Apple Silicon (arm64)."
        pip install -U torch torchvision torchaudio
    fi
    pip install -U airllm bitsandbytes safetensors "transformers>=4.43.3" accelerate optimum huggingface-hub fastapi uvicorn pydantic requests
elif [ "$OS_TYPE" = "Linux" ]; then
    echo "Detected Linux ($ARCH_TYPE)."
    echo "Installing PyTorch with CUDA..."
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 || pip install torch torchvision torchaudio
    pip install -U airllm bitsandbytes safetensors "transformers>=4.43.3" accelerate optimum huggingface-hub fastapi uvicorn pydantic requests
else
    echo "Unsupported OS: $OS_TYPE"
    pip install -U airllm torch safetensors "transformers>=4.43.3" accelerate optimum huggingface-hub fastapi uvicorn pydantic requests
fi

echo "=============================================="
echo " Installation completed successfully!"
echo " Activate with: source $VENV_DIR/bin/activate"
echo "=============================================="
