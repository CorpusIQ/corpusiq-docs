# Raspberry Pi 5 — Ultra-Low-Cost Always-On Agent

Run Hermes 24/7 on a Raspberry Pi 5 for less than $80 in hardware and pennies a month in electricity. Perfect for email monitoring, lightweight cron jobs, and home automation agents.

## Why a Raspberry Pi?

| Feature | Raspberry Pi 5 |
|---|---|
| Cost | $50–80 (board only) |
| Power draw | ~5W idle, ~10W under load |
| Annual electricity | ~$5–10 (24/7 at $0.12/kWh) |
| RAM | 4GB or 8GB |
| Storage | microSD or NVMe (via HAT) |
| Noise | Silent (no fan needed for light loads) |

## Limitations

- **No GPU acceleration** for local LLMs — use API-based models or very small quantized models
- **8GB RAM max** — can't run large models locally
- **ARM64 architecture** — some packages may need workarounds

## Step 1: OS Setup

Use Raspberry Pi OS Lite (64-bit, no desktop) for minimal overhead.

```bash
# Flash with Raspberry Pi Imager:
#   Choose: Raspberry Pi OS Lite (64-bit)
#   Enable SSH, set username/password, configure WiFi

# After first boot, SSH in:
ssh pi@raspberrypi.local

# Update
sudo apt update && sudo apt upgrade -y
```

## Step 2: Install Dependencies

```bash
sudo apt install -y python3 python3-pip python3-venv nodejs npm git curl

# Node 20+ (ARM64 build)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

## Step 3: Install Hermes

```bash
pip install hermes-agent

hermes profile create pi-agent
hermes profile use pi-agent
```

## Step 4: Model Strategy

### Primary: Cloud Models (Recommended)

The Pi doesn't have the VRAM or CPU power for meaningful local inference. Use API-based models.

```bash
# OpenRouter — free tier models available
hermes config set providers.openrouter.api_key "your-key"
hermes config set model.default openrouter/qwen/qwen3-235b-a22b:free
```

### Optional: Tiny Local Models (Ollama)

For offline operation or tasks where latency doesn't matter:

```bash
curl -fsSL https://ollama.com/install.sh | sh

# Pull the smallest usable models
ollama pull tinyllama       # ~637MB, runs on 4GB Pi
ollama pull nomic-embed-text # Embeddings for GBrain

# Expect 2–5 tokens/sec on Pi 5 (slow but functional)
ollama run tinyllama "Hello"
```

Only pull tinyllama or similarly small models — anything above 1–2B parameters will overwhelm the Pi's CPU.

## Step 5: External Storage (Recommended)

microSD cards wear out under constant writes. Use NVMe or USB SSD.

```bash
# NVMe via HAT (best performance)
# Attach NVMe HAT, install NVMe SSD, then:
sudo mkdir -p /mnt/nvme
sudo mount /dev/nvme0n1p1 /mnt/nvme

# Or USB SSD (simpler)
sudo mkdir -p /mnt/ssd
sudo mount /dev/sda1 /mnt/ssd

# Move Hermes data to external storage
mkdir -p /mnt/ssd/hermes-data
export HERMES_HOME=/mnt/ssd/hermes-data

# Add to ~/.bashrc for persistence
echo 'export HERMES_HOME=/mnt/ssd/hermes-data' >> ~/.bashrc
```

## Step 6: Headless Operation

The Pi runs headless. Set up systemd and proper shutdown handling.

```bash
sudo tee /etc/systemd/system/hermes-gateway.service << 'EOF'
[Unit]
Description=Hermes Agent Gateway
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=pi
ExecStart=/home/pi/.local/bin/hermes gateway run
Restart=always
RestartSec=15
Environment=HOME=/home/pi
Environment=HERMES_HOME=/mnt/ssd/hermes-data

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now hermes-gateway
```

## Step 7: Lightweight Crons

Design crons for the Pi's constraints: use cloud models, keep prompts short, avoid heavy file operations.

```bash
# Email check — uses cloud model, no local compute
hermes cron create \
  --name "email-watch" \
  --prompt "Check for new emails. Summarize in one sentence. Silent if empty." \
  --schedule "*/30 * * * *"

# System health — light, local-only
hermes cron create \
  --name "pi-health" \
  --prompt "Check temperature, disk usage, and memory. Report if anything exceeds 80%." \
  --schedule "0 * * * *"
```

## Step 8: Cooling and Power

```bash
# Monitor temperature
vcgencmd measure_temp

# If exceeding 70°C regularly, add a small heatsink or fan
# The official Pi 5 active cooler is $5

# Use a quality power supply — 5V 5A recommended for Pi 5
# Undervoltage causes random crashes
```

## Cost Summary

| Item | Cost |
|---|---|
| Raspberry Pi 5 (4GB) | $50 |
| Power supply + case | $15 |
| microSD (32GB) | $8 |
| NVMe SSD (optional) | $25 |
| **Total hardware** | **~$75–100** |
| | |
| Electricity (annual) | ~$6 |
| OpenRouter API | $0–5/month |
| **Total ongoing** | **~$5/month** |

## When Not to Use a Pi

- Heavy browser automation (Playwright will struggle)
- Running models larger than 1–2B parameters
- Video processing or encoding
- Multi-agent fleets

For those workloads, use a [cloud VPS](cloud-vps.md) or [gaming PC](gaming-pc.md).

---

*Next: [Cloud VPS Setup](cloud-vps.md) · [Docker Setup](docker.md)*
