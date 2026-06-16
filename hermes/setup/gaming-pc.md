# Gaming PC / High-End Desktop Setup

Got a gaming rig with an NVIDIA GPU? It's a perfect Hermes host. Run models locally at full speed with CUDA acceleration — no per-token API costs, no latency, no rate limits.

## Why a Gaming PC?

| Feature | Gaming PC Advantage |
|---|---|
| GPU memory | 8–24GB VRAM (runs 7B–70B models) |
| Inference speed | 50–200 tokens/sec with CUDA |
| Cost per token | $0.00 (electricity only) |
| Multi-GPU | Possible with NVLink |
| Existing hardware | You already own it |

## Minimum Specs

- **GPU:** NVIDIA GTX 1060 (6GB) or better — RTX 3060+ recommended
- **RAM:** 16GB system memory minimum, 32GB+ ideal
- **Storage:** 50GB free for models and embeddings
- **OS:** Linux (Ubuntu 22.04/24.04) or Windows 11 + WSL2

## Linux Setup (Recommended)

### Step 1: NVIDIA Drivers + CUDA

```bash
# Ubuntu 24.04
sudo apt update
sudo apt install nvidia-driver-550 nvidia-cuda-toolkit

# Verify
nvidia-smi
# Should show GPU, driver version, CUDA version
```

### Step 2: Install Ollama with GPU Acceleration

```bash
curl -fsSL https://ollama.com/install.sh | sh

# Verify GPU is used
ollama run llama3.2 "say hello"
# Check: nvidia-smi should show ollama process using GPU memory
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

### Step 4: Install Hermes

```bash
pip install hermes-agent

hermes profile create gpu-agent
hermes profile use gpu-agent
hermes config set model.default ollama/qwen2.5:14b
hermes config set model.fallback openrouter/anthropic/claude-sonnet-4
```

### Step 5: Maximize GPU Performance

```bash
# Set GPU to persistence mode (keeps driver loaded)
sudo nvidia-smi -pm 1

# Set max clocks for inference (optional, more power draw)
sudo nvidia-smi -ac 5001,1590  # Memory, GPU clock

# Increase GPU memory allocation for Ollama
# Edit: ~/.ollama/config.toml (or set env var)
export OLLAMA_NUM_PARALLEL=1       # One model at a time
export OLLAMA_MAX_LOADED_MODELS=1  # Don't keep extras in VRAM
export OLLAMA_KEEP_ALIVE=10m       # Unload after 10 min idle
```

### Step 6: Persistent Operation

```bash
# Systemd service for Hermes gateway
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

# For headless GPU-accelerated rendering (optional)
sudo apt install libnvidia-gl-550
```

## Windows + WSL2 Alternative

If you game on Windows, [follow the WSL2 guide](windows-wsl.md). GPU passthrough works — Ollama inside WSL2 sees your NVIDIA GPU via `nvidia-smi`.

## Cost

| Item | Cost |
|---|---|
| Hardware | Already own it |
| Electricity | ~$10–30/month (24/7 operation) |
| Models | Free (Ollama) |
| API fallback | ~$2–10/month (optional) |

**Total: Essentially free if the PC is already running.**

## Troubleshooting

```bash
# Ollama not using GPU?
ollama run llama3.2 --verbose  # Check if "cuda" appears in output

# Out of VRAM?
nvidia-smi                     # Check used memory
ollama rm <model>              # Remove models you don't use

# Driver issues?
sudo ubuntu-drivers autoinstall
sudo reboot
```

---

*Next: [Troubleshooting Guide](/hermes/troubleshooting/) · [Skills Marketplace](/hermes/skills/)*
