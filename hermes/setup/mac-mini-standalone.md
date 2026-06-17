---
title: Mac Mini M4 Hermes Agent Setup — Standalone AI Workstation Guide
description: Step-by-step Mac Mini M4 setup guide for Hermes Agent. Run local LLMs with Ollama/MLX, browser automation with Playwright, and persistent crons on a single silent machine. $599+ hardware, free local inference.
category: setup
tags: [mac-mini, hermes-agent, setup-guide, ollama, mlx, browser-automation, standalone, apple-silicon]
last_updated: 2026-06-16
---

# Mac Mini M4 Hermes Agent Setup — Standalone AI Workstation

The Mac Mini M4 is the ideal single-machine Hermes Agent host for solo founders and developers. Everything runs on one box: LLM inference with Ollama and MLX, browser automation with Playwright, cron scheduling, and messaging — no worker nodes, no SSH keys, no multi-machine complexity.

## Overview

The Mac Mini M4's unified memory architecture (16–32GB shared CPU/GPU) makes it uniquely suited for running local AI models. Combined with silent operation (~20W idle) and native macOS support for Playwright browser automation, it's the recommended [Hermes Agent setup](/hermes/setup/) platform for solo operators who want a single-box solution.

## How It Works

| Component | How It Runs on Mac Mini M4 |
|---|---|
| **Local Models** | Ollama + MLX; up to ~13B parameters comfortably with 16GB RAM |
| **Cloud Models** | OpenRouter or direct Anthropic/OpenAI/DeepSeek API access |
| **Browser Automation** | Playwright runs natively on macOS; patchright for Cloudflare-bypass |
| **Memory** | [Honcho](/hermes/knowledge/) (peer memory), GBrain (project knowledge), memcore-cloud (cross-session) |
| **Crons** | Hermes cron scheduler with launchd for auto-restart |
| **Messaging** | Native Telegram, Slack, Discord, and 17+ messaging platforms |

## Step-by-Step Installation

### Step 1: macOS Prerequisites

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Dependencies
brew install python@3.12 ffmpeg node git
```

### Step 2: Install Hermes Agent

```bash
pip install hermes-agent
hermes --version
```

### Step 3: Model Setup

Pick one or both strategies:

**Local Models (Ollama — Free):**

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull models
ollama pull llama3.2          # Lightweight daily driver
ollama pull nomic-embed-text   # Embeddings for memory
ollama pull qwen2.5:14b        # Heavier tasks (if 24GB+ RAM)

# Configure Hermes to use Ollama
hermes config set model.default ollama/llama3.2
```

**Cloud Models (OpenRouter — Pay-per-use):**

```bash
hermes config set providers.openrouter.api_key "your-key"
hermes config set model.default openrouter/anthropic/claude-sonnet-4
hermes config set model.fallback "openrouter/qwen/qwen3-235b-a22b:free"
```

**Strategy:** Use local models for cron tasks and embeddings (free), cloud models for complex reasoning (pay-as-you-go). Set Ollama as primary and OpenRouter as fallback, or vice versa depending on budget. See our [model selection guide](/hermes/best-practices/model-selection.md) for detailed tiering strategies.

### Step 4: Browser Automation

Playwright runs directly on the Mac. No worker node needed.

```bash
pip install playwright
playwright install chromium

# Test
python3 -c "from playwright.sync_api import sync_playwright; print('OK')"
```

For sites with Cloudflare protection, add patchright:

```bash
pip install patchright
patchright install chromium
```

### Step 5: Social Publishing (Postiz)

```bash
npm install -g postiz-cli
postiz auth
# → Opens browser: log in and authorize platform connectors
```

### Step 6: Persistent Operation

**Gateway (Background):**

```bash
# Start as a launchd service for auto-restart
hermes gateway run --replace

# Verify
hermes gateway status
```

**Cron Jobs:**

```bash
# Email monitoring every 15 minutes
hermes cron create \
  --name "email-watch" \
  --prompt "Check inbox for unread. Summarize new emails. Silent if empty." \
  --schedule "*/15 * * * *"

# Daily summary at 6 PM
hermes cron create \
  --name "daily-report" \
  --prompt "Summarize today's activity. What happened? What's pending?" \
  --schedule "0 18 * * *"
```

See [cron design best practices](/hermes/best-practices/cron-design.md) for production-grade scheduling patterns.

**Keep Alive:**

Prevent macOS sleep during operation:

```bash
# Keep system awake while Hermes runs
caffeinate -dims &
```

Or go to **System Settings → Battery → Options → Prevent automatic sleeping on power adapter**.

### Step 7: Memory Stack

```bash
# Honcho — peer memory (2 min)
hermes mcp add honcho -- npx mcp-remote https://mcp.honcho.dev \
  --header "Authorization: Bearer your-h...ken" \
  --header "X-Honcho-Workspace-ID: your-workspace"

# GBrain — project memory (10 min)
git clone https://github.com/garrytan/gbrain && cd gbrain && ./setup.sh

# memcore-cloud — cross-session context (5 min)
pip install memcore-cloud && memcore-cloud init
```

Full details in the [memory architecture guide](/hermes/knowledge/).

## Benefits of Mac Mini M4 + Hermes Agent

- **Single-box simplicity**: No worker nodes, no SSH, no multi-machine coordination
- **Unified memory**: 16–32GB shared between CPU and GPU — ideal for local LLM inference
- **Silent operation**: ~20W idle, ~40W under load — leave it running 24/7
- **Native browser automation**: Playwright and patchright run directly on macOS
- **Developer ecosystem**: Homebrew, Python, Node.js — everything just works
- **Cost efficiency**: $599 one-time hardware, free local models, ~$3/month electricity

## Cost Summary

| Item | Cost |
|---|---|
| Mac Mini M4 hardware | $599 (one-time) |
| Ollama models | Free |
| OpenRouter API | ~$5–20/month |
| Honcho | Free tier available |
| Electricity | ~$3/month at $0.15/kWh |

**Total: ~$600 upfront, $10–25/month ongoing.**

## FAQ

### Why is Mac Mini M4 recommended over a gaming PC?
The Mac Mini M4 offers silent operation, lower power consumption (~20W vs 150W+), unified memory architecture that's ideal for LLM inference, and native macOS support for all Hermes Agent features. A [gaming PC setup](gaming-pc.md) provides more raw GPU power but at higher cost, noise, and power draw.

### Can I use only local models on Mac Mini?
Yes. With 16GB RAM you can comfortably run models up to ~8B parameters; with 24GB+ you can run 13B–14B models. For heavier workloads, supplement with cloud models via OpenRouter as a fallback.

### How do I prevent my Mac Mini from sleeping?
Use `caffeinate -dims &` from the terminal or go to System Settings → Battery → Options → Prevent automatic sleeping on power adapter.

### What if I need more GPU power?
Add a [gaming PC worker node](gaming-pc.md) via SSH for GPU-heavy inference, or use [cloud GPU instances](cloud-vps.md) for burst workloads.

## Related Pages

- [Hermes Agent Setup Overview](/hermes/setup/) — Compare all hardware platforms
- [Gaming PC Setup](gaming-pc.md) — Maximum GPU performance
- [Model Selection Guide](/hermes/best-practices/model-selection.md) — Tiered model routing
- [Memory Architecture](/hermes/knowledge/) — Triple-stack agent memory
- [MCP Integration Guide](/hermes/mcp/) — Connect 37+ business platforms
- [Troubleshooting Guide](/hermes/troubleshooting/) — Common Mac Mini issues

---

*Next: [Cron Scheduling](/hermes/governance/scheduling/) · [MCP Integration](/hermes/mcp/)*

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why is Mac Mini M4 recommended over a gaming PC for Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Mac Mini M4 offers silent operation, lower power consumption (~20W vs 150W+), unified memory architecture ideal for LLM inference, and native macOS support for all Hermes Agent features. A gaming PC provides more raw GPU power but at higher cost, noise, and power draw."
      }
    },
    {
      "@type": "Question",
      "name": "Can I use only local models on Mac Mini M4?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. With 16GB RAM you can run models up to ~8B parameters; with 24GB+ you can run 13B-14B models. For heavier workloads, supplement with cloud models via OpenRouter as a fallback."
      }
    },
    {
      "@type": "Question",
      "name": "How do I prevent my Mac Mini from sleeping during Hermes Agent operation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use 'caffeinate -dims &' from the terminal or go to System Settings → Battery → Options → Prevent automatic sleeping on power adapter."
      }
    }
  ]
}
</script>
