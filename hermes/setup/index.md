# Hermes Agent — Installation & Setup

Hermes Agent runs on everything from a $50 Raspberry Pi to a $20,000 DGX workstation. This guide helps you pick the right hardware and get running fast.

**Don't overthink it.** If you're just getting started, use whatever machine you already have — a MacBook, a Windows desktop, or even a $5/month VPS. Hermes is designed to be provider-agnostic and hardware-flexible. You can always migrate later.

## Choosing Your Setup

Three questions to decide:

1. **Do you have a GPU?** If yes, run models locally for free with Ollama. If no, use API-based cloud models via OpenRouter.
2. **Does it need to run 24/7?** If yes, pick a cloud VPS, Raspberry Pi, or always-on desktop. If no, your laptop or gaming PC works fine.
3. **What's your budget?** $0/month (existing hardware + Ollama), ~$5/month (cloud VPS + free-tier models), or $20+/month (cloud VPS + Claude-level models).

## Hardware Comparison

| Platform | Approx. Cost | Best For | Local Models? | 24/7 Uptime? |
|---|---|---|---|---|
| **Mac Mini M4** | $599+ | Solo founders, desktop agent with browser automation | Yes (Ollama / MLX) | Easy |
| **Gaming PC / Desktop** | $1,200+ | Power users, GPU-accelerated inference | Yes (CUDA, max perf) | Easy |
| **Cloud VPS** | $5–20/mo | Always-on budget deployment, no hardware | No (API models) | Built-in |
| **Raspberry Pi 5** | $50–80 | Ultra-low-cost always-on agent, lightweight tasks | Minimal (tiny models) | Easy |
| **Docker (any host)** | Free | Reproducible, portable, CI/CD | Depends on host | Depends on host |
| **Windows 11 + WSL2** | Free (existing PC) | Windows users wanting native Linux experience | Yes (GPU passthrough) | Easy |
| **DGX / Workstation** | $3,000–20,000 | Heavy inference, multi-agent fleets | Yes (native) | Easy |

## Quick Start (Any Machine)

This gets Hermes running on any system with Python 3.11+.

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

That's it. You can now use Hermes interactively. For persistent operation (crons, gateway, messaging), continue to the setup guide for your platform.

## Detailed Setup Guides

Choose your hardware:

- **[Mac Mini M4 (Standalone)](mac-mini-standalone.md)** — All-in-one: models, browser automation, crons. Best for solo founders.
- **[Gaming PC / Desktop](gaming-pc.md)** — Max GPU performance with CUDA. Best for developers with powerful rigs.
- **[Cloud VPS](cloud-vps.md)** — $5–20/month, always-on. Best for budget production use.
- **[Raspberry Pi 5](raspberry-pi.md)** — Ultra-low-cost 24/7 agent. Best for lightweight automation.
- **[Docker](docker.md)** — Containerized deployment. Best for reproducibility and CI/CD.
- **[Windows 11 + WSL2](windows-wsl.md)** — Windows users, Linux-native experience. Best for Windows desktops.

## After Setup

Once Hermes is running, add capabilities:

- **[MCP Servers](/hermes/mcp/)** — Connect to Gmail, Slack, databases, and 37+ platforms
- **[Production Crons](/hermes/governance/scheduling/)** — Schedule autonomous tasks
- **[Skills Marketplace](/hermes/skills/)** — Add community-built capabilities
- **[Memory Architecture](/hermes/knowledge/)** — Honcho, GBrain, memcore-cloud
- **[Outputs & Use Cases](/hermes/outputs/)** — What agents actually do in production

---

*Now go build something autonomous.*
