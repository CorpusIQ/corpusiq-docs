---
title: Raspberry Pi 5 Hermes Agent Setup — Ultra-Low-Cost 24/7 AI Agent
description: Run Hermes Agent on Raspberry Pi 5 for under $80 hardware and $5/month ongoing. Always-on email monitoring, cron jobs, and lightweight AI automation. Step-by-step Pi setup with cloud models and external storage.
category: setup
tags: [raspberry-pi, hermes-agent, setup-guide, low-cost, always-on, arm64, cron-automation, budget-ai]
last_updated: 2026-06-16
---

# Raspberry Pi 5 Hermes Agent Setup — Ultra-Low-Cost 24/7 AI Agent

Run Hermes Agent 24/7 on a Raspberry Pi 5 for less than $80 in hardware and pennies a month in electricity. This Raspberry Pi setup guide is perfect for email monitoring, lightweight cron jobs, and home automation agents that run silently and cost almost nothing.

## Overview

The Raspberry Pi 5 is the most cost-effective always-on Hermes Agent platform. At $50–80, it draws ~5W idle and costs ~$5/year in electricity. It pairs with cloud API models for AI capabilities and is ideal for lightweight, persistent automation tasks that don't require GPU acceleration.

## How It Works

| Feature | Raspberry Pi 5 |
|---|---|
| Cost | $50–80 (board only) |
| Power draw | ~5W idle, ~10W under load |
| Annual electricity | ~$5–10 (24/7 at $0.12/kWh) |
| RAM | 4GB or 8GB |
| Storage | microSD or NVMe (via HAT) |
| Noise | Silent (no fan needed for light loads) |

## Limitations

- **No GPU acceleration** for local LLMs — use [API-based cloud models](cloud-vps.md) or very small quantized models
- **8GB RAM max** — can't run large models locally
- **ARM64 architecture** — some packages may need workarounds

## Step-by-Step Installation

### Step 1: OS Setup

```bash
# Flash Raspberry Pi OS Lite (64-bit) with Pi Imager
# Enable SSH, set username/password, configure WiFi

# SSH in after first boot:
ssh pi@raspberrypi.local
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Dependencies

```bash
sudo apt install -y python3 python3-pip python3-venv nodejs npm git curl
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

### Step 3: Install Hermes Agent

```bash
pip install hermes-agent
hermes profile create pi-agent
hermes profile use pi-agent
```

### Step 4: Model Strategy

**Primary: Cloud Models (Recommended)**

```bash
hermes config set providers.openrouter.api_key "your-key"
hermes config set model.default openrouter/qwen/qwen3-235b-a22b:free
```

**Optional: Tiny Local Models**

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull tinyllama       # ~637MB, runs on 4GB Pi
ollama pull nomic-embed-text # Embeddings
# Expect 2–5 tokens/sec — slow but functional
```

### Step 5: External Storage (Recommended)

```bash
# NVMe via HAT or USB SSD
sudo mkdir -p /mnt/ssd
sudo mount /dev/sda1 /mnt/ssd
mkdir -p /mnt/ssd/hermes-data
export HERMES_HOME=/mnt/ssd/hermes-data
echo 'export HERMES_HOME=/mnt/ssd/hermes-data' >> ~/.bashrc
```

### Step 6: Headless Operation

```bash
sudo tee /etc/systemd/system/hermes-gateway.service << 'EOF'
[Unit]
Description=Hermes Agent Gateway
After=network-online.target

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

### Step 7: Lightweight Crons

```bash
# Email check — uses cloud model, no local compute
hermes cron create --name "email-watch" \
  --prompt "Check for new emails. Summarize in one sentence." \
  --schedule "*/30 * * * *"

# System health — light, local-only
hermes cron create --name "pi-health" \
  --prompt "Check temperature, disk, memory. Report if >80%." \
  --schedule "0 * * * *"
```

### Step 8: Cooling and Power

```bash
vcgencmd measure_temp
# If exceeding 70°C, add active cooler (~$5)
# Use 5V 5A power supply — undervoltage causes crashes
```

## Benefits

- **Lowest cost**: Under $100 hardware, ~$5/month ongoing
- **Silent 24/7**: No fan needed, ~5W power draw
- **Perfect for monitoring**: Email, cron jobs, system health checks
- **Zero maintenance**: Headless operation with systemd auto-restart
- **Privacy**: Runs entirely on your local network

## Cost Summary

| Item | Cost |
|---|---|
| Raspberry Pi 5 (4GB) | $50 |
| Power supply + case | $15 |
| microSD (32GB) | $8 |
| NVMe SSD (optional) | $25 |
| **Total hardware** | **~$75–100** |
| Electricity (annual) | ~$6 |
| OpenRouter API | $0–5/month |

## When Not to Use a Pi

- Heavy browser automation (Playwright struggles)
- Running models larger than 1–2B parameters locally
- Video processing or encoding
- Multi-agent fleets

For those workloads, use a [cloud VPS](cloud-vps.md) or [gaming PC](gaming-pc.md).

## FAQ

### Can a Raspberry Pi run local AI models?
Only very small models like TinyLlama (~1B parameters). Expect 2–5 tokens/second. For practical AI, use cloud API models via OpenRouter — free tier models cost $0/token.

### Why use external storage with Raspberry Pi?
microSD cards wear out under constant write operations from logs and memory systems. An NVMe SSD via HAT or USB SSD provides faster, more durable storage.

### What tasks is a Raspberry Pi best for with Hermes Agent?
Email monitoring, system health checks, lightweight cron jobs, IoT automation, and notification routing. Not suitable for browser automation, video processing, or heavy inference.

## Related Pages

- [Hermes Agent Setup Overview](/hermes/setup/) — Compare all platforms
- [Cloud VPS Setup](cloud-vps.md) — Alternative always-on option
- [Docker Setup](docker.md) — Containerized ARM deployment
- [Cron Design Best Practices](/hermes/best-practices/cron-design.md) — Lightweight automation
- [Troubleshooting Guide](/hermes/troubleshooting/) — Pi-specific issues

---

*Next: [Cloud VPS Setup](cloud-vps.md) · [Docker Setup](docker.md)*

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can a Raspberry Pi 5 run local AI models with Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only very small models like TinyLlama (~1B parameters) at 2-5 tokens/second. For practical AI assistance, use cloud API models via OpenRouter — free tier models cost $0/token and provide full model capabilities."
      }
    },
    {
      "@type": "Question",
      "name": "Why use external storage with Raspberry Pi for Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "microSD cards wear out under constant write operations from logs, memory systems, and session data. An NVMe SSD via HAT or USB SSD provides faster, more durable storage for 24/7 operation."
      }
    },
    {
      "@type": "Question",
      "name": "What tasks is a Raspberry Pi 5 best for with Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Email monitoring, system health checks, lightweight cron jobs, IoT automation, and notification routing. It's not suitable for browser automation, video processing, or heavy local model inference."
      }
    }
  ]
}
</script>


---
*From the [Hermes Setup Guides](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/setup) — deploy Hermes Agent on any hardware. Built by [CorpusIQ](https://www.corpusiq.io).*


---
*From the [Hermes Setup Guides](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/setup) — deploy Hermes Agent on any hardware. Built by [CorpusIQ](https://www.corpusiq.io).*
