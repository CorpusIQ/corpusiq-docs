---
title: Gaming PC Hermes Agent Setup  --  CUDA-Accelerated AI Workstation
description: Run Hermes Agent on your gaming PC with NVIDIA CUDA acceleration. Local LLM inference at 50-200 tokens/sec, zero API costs. Step-by-step setup for Ubuntu Linux with Ollama, GPU optimization, and persistent operation.
category: setup
tags: [gaming-pc, hermes-agent, setup-guide, nvidia, cuda, ollama, gpu-acceleration, local-models]
last_updated: 2026-07-08
---

# Gaming PC Hermes Agent Setup  --  CUDA-Accelerated AI Workstation

Got a gaming rig with an NVIDIA GPU? It's a perfect Hermes Agent host for developers and power users. Run models locally at full speed with CUDA acceleration  --  no per-token API costs, no latency, no rate limits. This gaming PC setup guide covers everything from NVIDIA drivers to persistent operation.

## Overview

A gaming PC delivers the highest raw inference performance for local AI models. With 8–24GB of VRAM and CUDA acceleration, you can run models from 7B to 70B parameters locally at 50–200 tokens per second. Combined with Hermes Agent's [model selection](/docs/hermes/best-practices/model-selection.html) capabilities, you get a powerful AI workstation.

## How It Works

| Feature | Gaming PC Advantage |
|---|---|
| GPU memory | 8–24GB VRAM (runs 7B–70B models) |
| Inference speed | 50–200 tokens/sec with CUDA |
| Cost per token | $0.00 (electricity only) |
| Multi-GPU | Possible with NVLink |
| Existing hardware | You already own it |

## Minimum Specs

- **GPU:** NVIDIA GTX 1060 (6GB) or better  --  RTX 3060+ recommended
- **RAM:** 16GB system memory minimum, 32GB+ ideal
- **Storage:** 50GB free for models and embeddings
- **OS:** Linux (Ubuntu 22.04/24.04) or [Windows 11 + WSL2](windows-wsl.md)

## Step-by-Step Linux Setup (Recommended)

### Step 1: NVIDIA Drivers + CUDA

```bash
# Ubuntu 24.04
sudo apt update
sudo apt install nvidia-driver-550 nvidia-cuda-toolkit

# Verify
nvidia-smi
```

### Step 2: Install Ollama with GPU Acceleration

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3.2 "say hello"
# Check: nvidia-smi should show ollama using GPU memory
```

### Step 3: Pull Models That Fit Your VRAM

```bash
# 6–8GB VRAM: 7B–8B models
ollama pull llama3.2          # ~4.7GB
ollama pull mistral:7b         # ~4.1GB

# 12–16GB VRAM: 13B–14B models
ollama pull qwen2.5:14b        # ~8.5GB
ollama pull phi4:14b           # ~9.1GB

# 20–24GB VRAM: 32B–34B models
ollama pull qwen2.5:32b        # ~20GB
ollama pull codestral:22b      # ~13GB

# Embeddings (always pull)
ollama pull nomic-embed-text   # ~274MB
```

### Step 4: Install Hermes Agent

```bash
pip install hermes-agent

hermes profile create gpu-agent
hermes profile use gpu-agent
hermes config set model.default ollama/qwen2.5:14b
hermes config set model.fallback openrouter/anthropic/claude-sonnet-4
```

### Step 5: Maximize GPU Performance

```bash
# Set GPU to persistence mode
sudo nvidia-smi -pm 1

# Ollama optimization
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_MAX_LOADED_MODELS=1
export OLLAMA_KEEP_ALIVE=10m
```

### Step 6: Persistent Operation

```bash
sudo tee /etc/systemd/system/hermes-gateway.service << 'EOF'
[Unit]
Description=Hermes Agent Gateway
After=network.target

[Service]
Type=simple
User=your-username
ExecStart=/home/your-username/.local/bin/hermes gateway run
Restart=always
RestartSec=10
Environment=HOME=/home/your-username

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable --now hermes-gateway
```

### Step 7: Browser Automation

```bash
pip install playwright
playwright install chromium
sudo apt install libnvidia-gl-550  # For headless GPU rendering
```

## Benefits

- **Zero API costs**: All inference runs locally on your GPU
- **Maximum speed**: 50–200 tokens/sec with CUDA
- **Complete privacy**: Models and data never leave your machine
- **No rate limits**: Unlimited inference 24/7
- **Multi-GPU ready**: Scale with NVLink for larger models
- **Flexible fallback**: Add [cloud models via OpenRouter](cloud-vps.md) for frontier capabilities

## Windows + WSL2 Alternative

If you game on Windows, [follow the WSL2 guide](windows-wsl.md). GPU passthrough works  --  Ollama inside WSL2 sees your NVIDIA GPU via `nvidia-smi`.

## FAQ

### Can my gaming PC run Hermes Agent while I'm gaming?
Yes. Set `OLLAMA_KEEP_ALIVE=10m` so models unload from VRAM when idle. During gaming, Hermes Agent can use cloud fallback models or wait until you're done.

### What VRAM do I need for local LLMs?
6–8GB VRAM handles 7B models. 12–16GB handles 13–14B models. 24GB handles 32B models. See our [model selection guide](/docs/hermes/best-practices/model-selection.html) for detailed recommendations.

### Which GPU is best for Hermes Agent?
Any RTX 30-series or newer works well. The RTX 4090 (24GB VRAM) is ideal for running 32B+ models. Multiple GPUs can be combined with NVLink.

## Related Pages

- [Hermes Agent Setup Overview](/hermes/setup/)  --  Compare all platforms
- [Windows WSL2 Setup](windows-wsl.md)  --  GPU passthrough on Windows
- [Mac Mini M4 Setup](mac-mini-standalone.md)  --  Silent alternative
- [Model Selection Guide](/docs/hermes/best-practices/model-selection.html)  --  Choose the right model
- [Troubleshooting Guide](/hermes/troubleshooting/)  --  Common GPU issues
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
