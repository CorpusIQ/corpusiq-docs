# Windows 11 + WSL2 — Native Linux Experience

Run Hermes on Windows 11 with full Linux compatibility via WSL2. Get GPU acceleration for local models, native filesystem performance, and all the Linux tooling — without dual-booting.

## Why WSL2?

| Feature | WSL2 Benefit |
|---|---|
| Linux kernel | Real Linux, not emulation |
| GPU passthrough | NVIDIA CUDA works inside WSL2 |
| Filesystem | ext4 inside, accessible from Windows via `\\wsl$` |
| Networking | Shared with Windows — no VM networking hassle |
| Systemd | Supported — run Hermes as a service |

## Step 1: Install WSL2

Open **PowerShell as Administrator**:

```powershell
# Install WSL2 with Ubuntu 24.04
wsl --install -d Ubuntu-24.04

# Restart if prompted, then set up Linux username/password
```

Verify:

```powershell
wsl --list --verbose
# Should show: Ubuntu-24.04  Running  2
```

## Step 2: Configure WSL2 Resources

Create `%USERPROFILE%\.wslconfig`:

```ini
[wsl2]
memory=8GB          # Adjust based on your RAM
processors=4        # Adjust based on your CPU cores
swap=4GB
networkingMode=mirrored
```

Apply with `wsl --shutdown` in PowerShell, then reopen WSL.

## Step 3: GPU Passthrough (NVIDIA)

```powershell
# In PowerShell (Windows side):
# Install NVIDIA driver for WSL2 — NOT the standard Windows driver
# Download from: https://developer.nvidia.com/cuda/wsl
# Or winget:
winget install --id=Nvidia.CUDA -e
```

Inside WSL:

```bash
# Verify GPU is visible
nvidia-smi
# Should show your GPU with driver version and CUDA version

# If nvidia-smi not found:
sudo apt update
sudo apt install nvidia-utils-550
```

## Step 4: Install Dependencies (Inside WSL)

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nodejs npm git curl ffmpeg

# Node 20+ for MCP servers
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

## Step 5: Install Hermes

```bash
pip install hermes-agent

hermes profile create wsl-agent
hermes profile use wsl-agent

# Configure models
hermes config set providers.openrouter.api_key "your-key"
hermes config set model.default openrouter/anthropic/claude-sonnet-4
```

## Step 6: Local Models with Ollama (Optional)

With GPU passthrough, Ollama runs at full CUDA speed inside WSL2:

```bash
curl -fsSL https://ollama.com/install.sh | sh

# Pull models — they run on your NVIDIA GPU
ollama pull llama3.2
ollama pull nomic-embed-text
ollama pull qwen2.5:14b        # If you have 12GB+ VRAM

# Verify GPU acceleration
ollama run llama3.2 --verbose | grep -i cuda
```

## Step 7: Filesystem Strategy

WSL2 filesystem performance matters:

| Location | Speed | Best For |
|---|---|---|
| `/home/` (Linux ext4) | Fast | Hermes config, skills, crons |
| `/mnt/c/` (Windows NTFS) | Slower | Shared files, backups |

**Rule:** Keep Hermes data in `/home/` for speed. If you need to access files from Windows, use `\\wsl$\Ubuntu-24.04\home\` in File Explorer.

```bash
# Recommended: all Hermes data in Linux filesystem
export HERMES_HOME=~/.hermes

# Avoid: mounting Windows folders for active Hermes data
# /mnt/c/Users/... is slow for frequent read/write operations
```

## Step 8: Systemd Service

WSL2 supports systemd (enabled by default in Ubuntu 24.04):

```bash
sudo tee /etc/systemd/system/hermes-gateway.service << 'EOF'
[Unit]
Description=Hermes Agent Gateway
After=network-online.target
Wants=network-online.target

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

## Step 9: Keep WSL2 Running

WSL2 shuts down when no processes are active. Prevent this:

```powershell
# In PowerShell — keep WSL alive between reboots
# Create a scheduled task:
# Task Scheduler → Create Task → Trigger: At startup
# Action: Start a program → Program: wsl.exe → Arguments: -d Ubuntu-24.04 -e sleep infinity
```

Or inside WSL, ensure the systemd service has `Restart=always` and runs a long-lived process.

## Step 10: Browser Automation

```bash
# Playwright inside WSL2
pip install playwright
playwright install chromium
playwright install-deps chromium

# Test
python3 -c "from playwright.sync_api import sync_playwright; print('OK')"
```

Browser automation works inside WSL2 but is headless by default. For headed browsing, install a Windows X server (like VcXsrv) and set `export DISPLAY=:0`.

## Troubleshooting

```bash
# WSL2 can't reach internet?
# PowerShell: wsl --shutdown, then restart

# nvidia-smi not working?
# Ensure you installed NVIDIA WSL2 driver, not standard Windows driver
# Re-run: winget install --id=Nvidia.CUDA -e

# Performance issues?
# Move data from /mnt/c/ to /home/
# Check .wslconfig memory/processor limits
```

## Cost

| Item | Cost |
|---|---|
| Windows 11 license | Already own it |
| WSL2 | Free |
| Ollama models | Free |
| API fallback | ~$5–15/month (optional) |

**Total: Free if you already have a Windows PC.**

---

*Next: [Gaming PC Setup](gaming-pc.md) · [Docker Setup](docker.md) · [Troubleshooting](/hermes/troubleshooting/)*
