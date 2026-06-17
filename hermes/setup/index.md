---
title: Hermes Agent Setup & Installation Guide — Get Started Fast
description: Complete Hermes Agent setup guide for any hardware platform. Quick-start instructions, hardware comparison, and step-by-step installation for Mac Mini, gaming PC, cloud VPS, Raspberry Pi, Docker, and Windows WSL.
category: setup
tags: [hermes-agent, installation, setup-guide, getting-started, hardware, ollama, openrouter]
last_updated: 2026-06-16
---

# Hermes Agent Setup & Installation Guide — Get Started Fast

Hermes Agent runs on everything from a $50 Raspberry Pi to a $20,000 DGX workstation. This setup guide helps you pick the right hardware platform, install Hermes Agent in under 5 minutes, and choose the best model configuration for your needs.

## Overview

**Don't overthink it.** If you're just getting started, use whatever machine you already have — a MacBook, a Windows desktop, or even a $5/month VPS. Hermes Agent is designed to be provider-agnostic and hardware-flexible. You can always migrate later to a different [setup platform](index.md#hardware-comparison).

## How It Works

Hermes Agent installs via `pip install hermes-agent`, then connects to AI models through one of three paths:

| Path | How It Works | Cost |
|------|-------------|------|
| **Ollama (local)** | Run open-source models directly on your hardware via [Ollama](https://ollama.com) | Free |
| **OpenRouter** | Access 200+ models through a single API gateway — pay-per-token | $0–$20+/month |
| **Direct provider** | Connect directly to Anthropic, OpenAI, DeepSeek, or other model providers | Varies by provider |

After installation, Hermes Agent uses **skills** (reusable workflows), **crons** (scheduled automation), **MCP servers** (external tool connections), and **memory systems** to operate autonomously.

## Choosing Your Setup

Three questions to decide:

1. **Do you have a GPU?** If yes, run models locally for free with Ollama. If no, use API-based cloud models via OpenRouter.
2. **Does it need to run 24/7?** If yes, pick a [cloud VPS](cloud-vps.md), [Raspberry Pi](raspberry-pi.md), or always-on desktop. If no, your laptop or gaming PC works fine.
3. **What's your budget?** $0/month (existing hardware + Ollama), ~$5/month (cloud VPS + free-tier models), or $20+/month (cloud VPS + Claude-level models).

## Hardware Comparison

| Platform | Approx. Cost | Best For | Local Models? | 24/7 Uptime? |
|---|---|---|---|---|
| **[Mac Mini M4](mac-mini-standalone.md)** | $599+ | Solo founders, desktop agent with browser automation | Yes (Ollama / MLX) | Easy |
| **[Gaming PC / Desktop](gaming-pc.md)** | $1,200+ | Power users, GPU-accelerated inference | Yes (CUDA, max perf) | Easy |
| **[Cloud VPS](cloud-vps.md)** | $5–20/mo | Always-on budget deployment, no hardware | No (API models) | Built-in |
| **[Raspberry Pi 5](raspberry-pi.md)** | $50–80 | Ultra-low-cost always-on agent, lightweight tasks | Minimal (tiny models) | Easy |
| **[Docker](docker.md)** | Free | Reproducible, portable, CI/CD | Depends on host | Depends on host |
| **[Windows 11 + WSL2](windows-wsl.md)** | Free (existing PC) | Windows users wanting native Linux experience | Yes (GPU passthrough) | Easy |
| DGX / Workstation | $3,000–20,000 | Heavy inference, multi-agent fleets | Yes (native) | Easy |

## Quick Start (Any Machine)

This gets Hermes Agent running on any system with Python 3.11+.

```bash
# 1. Install
pip install hermes-agent

# 2. Create a profile
hermes profile create my-agent
hermes profile use my-agent

# 3. Configure a model provider (pick one)
# Option A: OpenRouter — instant access to 200+ models
hermes config set providers.openrouter.api_key "your-key"

# Option B: Direct provider
hermes config set providers.anthropic.api_key "your-key"

# Option C: Ollama — free, local, no API key needed
ollama pull llama3.2

# 4. Set your default model
hermes config set model.default openrouter/anthropic/claude-sonnet-4

# 5. Verify
hermes --version
hermes doctor
```

That's it. You can now use Hermes Agent interactively. For persistent operation (crons, gateway, messaging), continue to the setup guide for your platform.

## Benefits of Hermes Agent

- **Provider-agnostic**: Switch between Anthropic, OpenAI, DeepSeek, Ollama, and 200+ models without changing your code
- **Hardware-flexible**: Run on anything from a Raspberry Pi to a DGX workstation
- **Zero-friction migration**: Start on your laptop, move to a [cloud VPS](cloud-vps.md) later
- **Free tier available**: Use Ollama for local, free model inference
- **Autonomous operation**: [Cron scheduling](/hermes/governance/scheduling/) + [MCP tools](/hermes/mcp/) + [skills](/hermes/skills/) for 24/7 automation

## Detailed Setup Guides

Choose your hardware:

- **[Mac Mini M4 (Standalone)](mac-mini-standalone.md)** — All-in-one: models, browser automation, crons. Best for solo founders.
- **[Gaming PC / Desktop](gaming-pc.md)** — Max GPU performance with CUDA. Best for developers with powerful rigs.
- **[Cloud VPS](cloud-vps.md)** — $5–20/month, always-on. Best for budget production use.
- **[Raspberry Pi 5](raspberry-pi.md)** — Ultra-low-cost 24/7 agent. Best for lightweight automation.
- **[Docker](docker.md)** — Containerized deployment. Best for reproducibility and CI/CD.
- **[Windows 11 + WSL2](windows-wsl.md)** — Windows users, Linux-native experience. Best for Windows desktops.

## After Setup

Once Hermes Agent is running, add capabilities:

- **[MCP Integration](/hermes/mcp/)** — Connect to Gmail, Slack, databases, and 37+ platforms
- **[Cron Scheduling](/hermes/governance/scheduling/)** — Schedule autonomous tasks with [cron design best practices](/hermes/best-practices/cron-design.md)
- **[Skills Marketplace](/hermes/skills/)** — Add community-built capabilities and [create custom skills](/hermes/skills/creating-skills.md)
- **[Memory Architecture](/hermes/knowledge/)** — Honcho, GBrain, memcore-cloud triple stack
- **[Blueprints](/hermes/blueprints/)** — End-to-end automation workflows for business processes
- **[Prompt Library](/hermes/prompts/)** — Curated templates for code generation, analysis, content, and more

## FAQ

### What is Hermes Agent?
Hermes Agent is an open-source AI agent framework by Nous Research that connects to language models (local or cloud) and external tools through MCP (Model Context Protocol). It automates tasks through skills, scheduled crons, and multi-source data queries.

### Can I run Hermes Agent for free?
Yes. Install Hermes Agent on your existing hardware, pull free models from Ollama (like Llama 3.2), and you pay nothing. Cloud API usage is optional and pay-per-use.

### Which hardware is best for Hermes Agent?
The [Mac Mini M4](mac-mini-standalone.md) is the recommended all-in-one platform. For budget 24/7 operation, a [cloud VPS](cloud-vps.md) at $5–20/month works well. For maximum GPU performance, use a [gaming PC](gaming-pc.md) with CUDA.

### How do I connect Hermes Agent to business data?
Use the [MCP Integration Guide](/hermes/mcp/) to connect 37+ business platforms — CRM, email, analytics, databases, advertising, and more — through a single OAuth flow with CorpusIQ MCP.

### What's the difference between Ollama and OpenRouter?
Ollama runs models locally on your hardware (free, private, limited to smaller models). OpenRouter provides API access to 200+ models including frontier models like Claude and GPT-4o (pay-per-use, no hardware requirements).

### How do I keep Hermes Agent running 24/7?
Use a [cloud VPS](cloud-vps.md), [Raspberry Pi](raspberry-pi.md), or an always-on desktop with `caffeinate` (macOS) or power settings adjusted. Configure the Hermes gateway as a systemd or launchd service for automatic restart.

### How do I add new capabilities after setup?
Extend Hermes Agent through [MCP servers](/hermes/mcp/) for external tools, [skills](/hermes/skills/creating-skills.md) for reusable workflows, [crons](/hermes/best-practices/cron-design.md) for scheduled automation, and [memory systems](/hermes/knowledge/) for persistent context.

## Related Pages

- [Mac Mini M4 Setup](mac-mini-standalone.md) — Recommended standalone platform
- [Cloud VPS Setup](cloud-vps.md) — Budget always-on deployment
- [Model Selection Guide](/hermes/best-practices/model-selection.md) — Choose the right AI model
- [MCP Integration Guide](/hermes/mcp/) — Connect external tools and data
- [Cron Design Best Practices](/hermes/best-practices/cron-design.md) — Reliable scheduled automation
- [Troubleshooting Guide](/hermes/troubleshooting/) — Common issues and fixes

---

*Now go build something autonomous.*

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hermes Agent is an open-source AI agent framework by Nous Research that connects to language models (local or cloud) and external tools through MCP (Model Context Protocol). It automates tasks through skills, scheduled crons, and multi-source data queries."
      }
    },
    {
      "@type": "Question",
      "name": "Can I run Hermes Agent for free?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Install Hermes Agent on your existing hardware, pull free models from Ollama (like Llama 3.2), and you pay nothing. Cloud API usage is optional and pay-per-use."
      }
    },
    {
      "@type": "Question",
      "name": "Which hardware is best for Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Mac Mini M4 is the recommended all-in-one platform. For budget 24/7 operation, a cloud VPS at $5-20/month works well. For maximum GPU performance, use a gaming PC with CUDA."
      }
    },
    {
      "@type": "Question",
      "name": "How do I connect Hermes Agent to business data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use the MCP Integration Guide to connect 37+ business platforms — CRM, email, analytics, databases, advertising, and more — through a single OAuth flow with CorpusIQ MCP."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between Ollama and OpenRouter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ollama runs models locally on your hardware (free, private, limited to smaller models). OpenRouter provides API access to 200+ models including frontier models (pay-per-use, no hardware requirements)."
      }
    }
  ]
}
</script>
