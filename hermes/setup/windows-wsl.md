---
title: Windows 11 WSL2 Hermes Agent Setup  --  Linux AI Agent on Windows
description: Run Hermes Agent on Windows 11 with full Linux compatibility via WSL2. GPU passthrough for NVIDIA CUDA, native Ollama models, systemd persistence, and browser automation. Free if you already own a Windows PC.
category: setup
tags: [windows, wsl2, hermes-agent, setup-guide, nvidia, gpu-passthrough, ollama, linux-on-windows]
last_updated: 2026-07-08
---

# Windows 11 WSL2 Hermes Agent Setup  --  Linux AI Agent on Windows

Run Hermes Agent on Windows 11 with full Linux compatibility via WSL2  --  no dual-booting required. Get NVIDIA GPU acceleration for local models through CUDA passthrough, native Linux filesystem performance, and all Hermes Agent features. This Windows WSL2 setup guide covers everything from installation to persistent 24/7 operation.

## Overview

WSL2 provides a real Linux kernel inside Windows, enabling Hermes Agent to run exactly as it would on a native Linux machine. GPU passthrough means your NVIDIA card accelerates Ollama models at full CUDA speed. The setup is free if you already own a Windows PC, making it the easiest entry point for Windows users who want the full [Hermes Agent setup](/hermes/setup/) experience.

## How It Works

| Feature | WSL2 Benefit |
|---|---|
| Linux kernel | Real Linux, not emulation |
| GPU passthrough | NVIDIA CUDA works inside WSL2 |
| Filesystem | ext4 inside, accessible from Windows via `\\wsl$` |
| Networking | Shared with Windows  --  no VM networking hassle |
| Systemd | Supported  --  run Hermes Agent as a service |

## Step-by-Step Installation

### Step 1: Install WSL2

Open **PowerShell as Administrator**:

```powershell
wsl --install -d Ubuntu-24.04
# Set up Linux username/password after reboot
wsl --list --verbose
```

### Step 2: Configure WSL2 Resources

Create `%USERPROFILE%\.wslconfig`:

```ini
[wsl2]
memory=8GB
processors=4
swap=4GB
networkingMode=mirrored
```

Apply: `wsl --shutdown` in PowerShell, then reopen WSL.

### Step 3: GPU Passthrough (NVIDIA)

```powershell
# In PowerShell  --  install NVIDIA WSL2 driver
winget install --id=Nvidia.CUDA -e
```

Inside WSL:

```bash
nvidia-smi  # Should show your GPU
sudo apt install nvidia-utils-550  # If not found
```

### Step 4: Install Dependencies

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nodejs npm git curl ffmpeg
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

### Step 5: Install Hermes Agent

```bash
pip install hermes-agent
hermes profile create wsl-agent
hermes profile use wsl-agent
hermes config set providers.openrouter.api_key ***
hermes config set model.default openrouter/anthropic/claude-sonnet-4
```

### Step 6: Local Models with Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2
ollama pull nomic-embed-text
ollama pull qwen2.5:14b  # If 12GB+ VRAM
ollama run llama3.2 --verbose | grep -i cuda  # Verify GPU
```

### Step 7: Filesystem Strategy

| Location | Speed | Best For |
|---|---|---|
| `/home/` (Linux ext4) | Fast | Hermes config, skills, crons |
| `/mnt/c/` (Windows NTFS) | Slower | Shared files, backups |

**Rule:** Keep active Hermes data in `/home/` for performance. For [model selection](/docs/hermes/best-practices/model-selection.html) and memory, WSL2's ext4 filesystem is significantly faster than NTFS.

### Step 8: Systemd Service

```bash
sudo tee /etc/systemd/system/hermes-gateway.service << 'EOF'
[Unit]
Description=Hermes Agent Gateway
After=network-online.target

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

sudo systemctl daemon-reload
sudo systemctl enable --now hermes-gateway
```

### Step 9: Keep WSL2 Running

WSL2 shuts down when idle. Prevent this:

```powershell
# Task Scheduler → Create Task → Trigger: At startup
# Action: wsl.exe -d Ubuntu-24.04 -e sleep infinity
```

### Step 10: Browser Automation

```bash
pip install playwright
playwright install chromium
playwright install-deps chromium
```

For headed browsing, install a Windows X server like VcXsrv and `export DISPLAY=:0`.

## Benefits

- **Free**: No additional hardware needed beyond your Windows PC
- **Full GPU acceleration**: NVIDIA CUDA works natively inside WSL2
- **No dual-boot**: Run Linux Hermes Agent alongside Windows apps
- **Local models**: Ollama at full speed via GPU passthrough
- **Persistent**: Systemd service with auto-restart keeps Hermes alive

## FAQ

### Does Ollama GPU acceleration work in WSL2?
Yes. NVIDIA's WSL2 driver enables full CUDA passthrough. Ollama detects the GPU automatically and uses it for inference  --  same speed as native Linux.

### Why not just use Windows native Hermes Agent?
WSL2 provides a real Linux environment with systemd, ext4 filesystem, and native package management. Many MCP servers and developer tools expect Linux. WSL2 delivers this without dual-booting.

### How do I prevent WSL2 from shutting down?
Create a Windows Task Scheduler task that runs `wsl.exe -d Ubuntu-24.04 -e sleep infinity` at startup, or ensure the Hermes systemd service has `Restart=always`.

## Related Pages

- [Hermes Agent Setup Overview](/hermes/setup/)  --  All platform options
- [Gaming PC Setup](gaming-pc.md)  --  Native Linux for max GPU performance
- [Docker Setup](docker.md)  --  Alternative Windows deployment
- [Model Selection Guide](/docs/hermes/best-practices/model-selection.html)  --  GPU model sizing
- [Troubleshooting Guide](/hermes/troubleshooting/)  --  WSL2-specific issues
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
