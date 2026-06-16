# Mac Mini M4 — Standalone Setup

The Mac Mini M4 is the ideal single-machine Hermes host. Everything runs on one box: LLM inference, browser automation, cron scheduling, and messaging. No worker nodes, no SSH keys, no multi-machine complexity.

## Why Standalone?

| Feature | Mac Mini M4 |
|---|---|
| Unified memory | 16–32GB (shared CPU/GPU) |
| Local models | Ollama + MLX, up to ~13B params comfortably |
| Browser automation | Playwright runs natively on macOS |
| Power draw | ~20W idle, ~40W under load |
| Noise | Silent |
| Cost | $599+ (base model) |

## Step 1: macOS Prerequisites

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Dependencies
brew install python@3.12 ffmpeg node git
```

## Step 2: Install Hermes

```bash
pip install hermes-agent
hermes --version
```

## Step 3: Model Setup

Pick one or both:

### Local Models (Ollama — Free)

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

### Cloud Models (OpenRouter — Pay-per-use)

```bash
hermes config set providers.openrouter.api_key "your-key"
hermes config set model.default openrouter/anthropic/claude-sonnet-4
hermes config set model.fallback "openrouter/qwen/qwen3-235b-a22b:free"
```

**Strategy:** Use local models for cron tasks and embeddings (free), cloud models for complex reasoning (pay-as-you-go). Set Ollama as primary and OpenRouter as fallback, or vice versa depending on budget.

## Step 4: Browser Automation

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

## Step 5: Social Publishing (Postiz)

```bash
npm install -g postiz-cli
postiz auth
# → Opens browser: log in and authorize platform connectors
```

## Step 6: Persistent Operation

### Gateway (Background)

```bash
# Start as a launchd service for auto-restart
hermes gateway run --replace

# Verify
hermes gateway status
```

### Cron Jobs

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

### Keep Alive

Prevent macOS sleep during operation:

```bash
# Keep system awake while Hermes runs
caffeinate -dims &
```

Or go to **System Settings → Battery → Options → Prevent automatic sleeping on power adapter**.

## Step 7: Memory Stack

```bash
# Honcho — peer memory (2 min)
hermes mcp add honcho -- npx mcp-remote https://mcp.honcho.dev \
  --header "Authorization: Bearer your-honcho-token" \
  --header "X-Honcho-Workspace-ID: your-workspace"

# GBrain — project memory (10 min)
git clone https://github.com/garrytan/gbrain && cd gbrain && ./setup.sh

# memcore-cloud — cross-session context (5 min)
pip install memcore-cloud && memcore-cloud init
```

## Cost Summary

| Item | Cost |
|---|---|
| Mac Mini M4 hardware | $599 (one-time) |
| Ollama models | Free |
| OpenRouter API | ~$5–20/month |
| Honcho | Free tier available |
| Electricity | ~$3/month at $0.15/kWh |

**Total: ~$600 upfront, $10–25/month ongoing.**

---

*Next: [Production Cron Reference](/hermes/governance/scheduling/) · [MCP Integration](/hermes/mcp/)*
