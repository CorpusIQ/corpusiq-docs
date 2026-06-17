---
title: Cloud VPS Hermes Agent Setup — 24/7 AI Agent for $5-20/month
description: Deploy Hermes Agent on a cloud VPS for always-on AI automation. Step-by-step setup for Hetzner, DigitalOcean, AWS, Vultr. API-based models, systemd persistence, security hardening. $5/month budget deployment.
category: setup
tags: [cloud-vps, hermes-agent, setup-guide, hetzner, digitalocean, openrouter, systemd, 24/7-automation]
last_updated: 2026-06-16
---

# Cloud VPS Hermes Agent Setup — 24/7 AI Agent for $5–20/Month

Run Hermes Agent 24/7 on a cloud VPS for always-on AI automation at minimal cost. No hardware to maintain, no electricity bill, and your agent stays online even when your laptop is off. This cloud VPS setup guide covers provisioning, model configuration, cron persistence, and security hardening.

## Overview

A cloud VPS is the best budget option for always-on Hermes Agent operation. For $5–20/month you get a Linux server that runs 24/7 with built-in uptime guarantees. Use API-based models (OpenRouter for 200+ models including free-tier options) since VPS instances don't have GPUs.

## How It Works

| Component | How It Runs on Cloud VPS |
|---|---|
| **Models** | OpenRouter API (200+ models) or direct provider APIs |
| **Persistence** | systemd service with `Restart=always` |
| **Crons** | [Hermes cron scheduler](/hermes/best-practices/cron-design.md) — 24/7 execution |
| **Memory** | [Honcho](/hermes/knowledge/) + GBrain + memcore-cloud |
| **Security** | UFW firewall, SSH key-only auth, unattended upgrades |

## Provider Comparison

| Provider | Cheapest Plan | RAM | CPU | Best For |
|---|---|---|---|---|
| **Hetzner** | €4.51/mo (CX22) | 4GB | 2 vCPU | Best value in Europe |
| **DigitalOcean** | $6/mo (Basic) | 1GB | 1 vCPU | Good docs, global regions |
| **AWS Lightsail** | $5/mo | 1GB | 1 vCPU | AWS ecosystem integration |
| **Vultr** | $6/mo | 1GB | 1 vCPU | Many regions, hourly billing |
| **Linode** | $5/mo | 1GB | 1 vCPU | Simple, reliable |

**Recommendation:** Hetzner CX22 (4GB RAM, €4.51/mo) gives enough memory for Hermes Agent + memory stack. For lightweight cron-only usage, a 1GB droplet works.

## Step-by-Step Installation

### Step 1: Provision the VPS

```bash
# SSH into your VPS
ssh root@your-server-ip

# Create non-root user
adduser hermes
usermod -aG sudo hermes
su - hermes
```

### Step 2: Install Dependencies

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nodejs npm git curl
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

### Step 3: Install Hermes Agent

```bash
pip install hermes-agent
hermes profile create cloud-agent
hermes profile use cloud-agent
```

### Step 4: Configure Cloud Models

```bash
# OpenRouter — free tier models available
hermes config set providers.openrouter.api_key "your-key"
hermes config set model.default openrouter/qwen/qwen3-235b-a22b:free
hermes config set model.fallback openrouter/anthropic/claude-sonnet-4
```

See our [model selection guide](/hermes/best-practices/model-selection.md) for tiered routing strategies.

### Step 5: Docker Option

For containerized deployment:

```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker hermes

docker run -d --name hermes-agent \
  -v ~/.hermes:/home/hermes/.hermes \
  -e OPENROUTER_API_KEY="your-key" \
  --restart unless-stopped \
  nousresearch/hermes-agent:latest
```

Full setup in the [Docker guide](docker.md).

### Step 6: Systemd Service

```bash
sudo tee /etc/systemd/system/hermes-gateway.service << 'EOF'
[Unit]
Description=Hermes Agent Gateway
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=hermes
ExecStart=/home/hermes/.local/bin/hermes gateway run
Restart=always
RestartSec=10
Environment=HOME=/home/hermes

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now hermes-gateway
```

### Step 7: Cron Persistence

```bash
# Email monitoring
hermes cron create \
  --name "email-watch" \
  --prompt "Check inbox for unread. Summarize. Silent if empty." \
  --schedule "*/15 * * * *"

# Daily health check
hermes cron create \
  --name "health-check" \
  --prompt "Verify services running. Check disk space. Report issues." \
  --schedule "0 8 * * *"
```

### Step 8: Security Hardening

```bash
sudo ufw allow 22/tcp
sudo ufw enable
ssh-copy-id hermes@your-server-ip
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart sshd
sudo apt install unattended-upgrades
```

## Benefits

- **Always-on**: 24/7 operation with cloud provider uptime guarantees
- **Budget-friendly**: $5–20/month total including models
- **Zero hardware maintenance**: No physical machine to manage
- **Instant scaling**: Upgrade RAM/CPU with a few clicks
- **Global regions**: Deploy close to your data sources
- **Free-tier models**: OpenRouter offers free models for light usage

## Cost Breakdown

| Item | Monthly Cost |
|---|---|
| Hetzner CX22 (4GB RAM) | €4.51 |
| OpenRouter API (free models) | $0 |
| Honcho (free tier) | $0 |
| **Total** | **~$5/month** |

For heavier usage with Claude-level models: ~$15–25/month.

## FAQ

### Can I run local models on a cloud VPS?
No — cloud VPS instances don't have GPUs. Use API-based models via OpenRouter or direct provider APIs. For local model inference, use a [gaming PC](gaming-pc.md) or [Mac Mini M4](mac-mini-standalone.md).

### Which cloud VPS provider is best for Hermes Agent?
Hetzner CX22 offers the best value at €4.51/month with 4GB RAM — enough for Hermes Agent + memory stack. DigitalOcean and Linode are good alternatives with simpler interfaces.

### How do I keep Hermes Agent running after reboot?
The systemd service with `Restart=always` ensures Hermes Agent restarts automatically. Combine with `WantedBy=multi-user.target` so it starts on boot.

## Related Pages

- [Hermes Agent Setup Overview](/hermes/setup/) — All platform options
- [Docker Setup](docker.md) — Containerized cloud deployment
- [Raspberry Pi Setup](raspberry-pi.md) — Alternative low-cost 24/7 option
- [Model Selection Guide](/hermes/best-practices/model-selection.md) — API model tiering
- [Cron Design Best Practices](/hermes/best-practices/cron-design.md) — 24/7 automation
- [Troubleshooting Guide](/hermes/troubleshooting/) — VPS-specific issues

---

*Next: [Docker Setup](docker.md) · [Cron Scheduler](/hermes/governance/scheduling/)*

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I run local AI models on a cloud VPS with Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — cloud VPS instances typically don't have GPUs. Use API-based models via OpenRouter or direct provider APIs. For local model inference, use a gaming PC with NVIDIA GPU or Mac Mini M4."
      }
    },
    {
      "@type": "Question",
      "name": "Which cloud VPS provider is best for running Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hetzner CX22 offers the best value at €4.51/month with 4GB RAM — enough for Hermes Agent plus the memory stack. DigitalOcean and Linode are good alternatives with simpler interfaces."
      }
    },
    {
      "@type": "Question",
      "name": "How do I keep Hermes Agent running 24/7 on a cloud VPS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Configure Hermes Agent as a systemd service with Restart=always and WantedBy=multi-user.target. This ensures automatic restart on boot and after crashes. The cloud provider handles hardware uptime."
      }
    }
  ]
}
</script>


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*
