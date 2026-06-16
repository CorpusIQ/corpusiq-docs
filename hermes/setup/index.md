# Hermes Agent — Production Setup Guide

From zero to production agent in 15 minutes. Tested on Linux (DGX Spark) and macOS (Mac Mini M4).

## Prerequisites

```bash
# Python 3.11+
python3 --version  # 3.11+ required

# pip
pip --version

# Node.js (for MCP servers)
node --version  # 18+ recommended

# Git
git --version
```

## Step 1: Install Hermes Agent

```bash
pip install hermes-agent

# Verify
hermes --version
# Hermes Agent v0.16.0 · Python 3.11+
```

## Step 2: Create Your Profile

```bash
# Create a profile (keeps your config isolated)
hermes profile create my-agent

# Switch to it
hermes profile use my-agent

# Set your default model
hermes config set model.default deepseek/deepseek-v4-pro

# Add a fallback chain (if primary fails)
hermes config set model.fallback "openrouter/qwen/qwen3-235b-a22b:free,anthropic/claude-opus-4"
```

## Step 3: Configure Model Providers

```bash
# OpenRouter (access to 200+ models)
hermes config set providers.openrouter.api_key "sk-or-v1-YOUR-KEY"

# Anthropic (direct, better caching)
hermes config set providers.anthropic.api_key "sk-ant-YOUR-KEY"

# Ollama (local, free)
ollama pull nomic-embed-text
ollama pull llama3.2
```

## Step 4: Add Memory

### Honcho — Peer Memory (2 min)

```bash
hermes mcp add honcho -- npx mcp-remote https://mcp.honcho.dev \
  --header "Authorization: Bearer YOUR_KEY" \
  --header "X-Honcho-Workspace-ID: your-workspace" \
  --header "X-Honcho-User-Name: your-agent"
```

### GBrain — Organizational Memory (10 min)

```bash
git clone https://github.com/garrytan/gbrain
cd gbrain
./setup.sh
# Indexes your project files into searchable embeddings
```

### memcore-cloud — Cross-Session Context (5 min)

```bash
pip install memcore-cloud
memcore-cloud init
# Auto-injects context into every Hermes turn
```

## Step 5: Add Business Tools

### CorpusIQ MCP — One OAuth for 37+ Platforms

```bash
hermes mcp add corpusiq -- url https://mcp2.corpusiq.io/mcp
hermes mcp auth corpusiq
# → Opens browser: authenticate with Google
# → 53 tools available: Gmail, GA4, Stripe, HubSpot, QuickBooks, Meta Ads...
```

### Other Useful MCPs

```bash
# Web dashboard
hermes mcp add hermes-studio -- npx @ekkolearn/hermes-studio

# GitHub
hermes tools enable github
```

## Step 6: Configure Messaging Gateway

```bash
# Telegram (most popular)
hermes tools enable telegram
# → Set TELEGRAM_BOT_TOKEN in .env

# Discord
hermes tools enable discord

# Slack
hermes tools enable slack
```

## Step 7: Deploy Your First Crons

```bash
# Email monitoring
hermes cron create \
  --name "email-watch" \
  --prompt "Check Gmail for unread. Summarize new emails. Silent if empty." \
  --schedule "*/15 * * * *" \
  --enabled-toolsets "terminal,web,file,send_message"

# Daily report
hermes cron create \
  --name "daily-report" \
  --prompt "Generate a summary of today's activity. What happened? What's pending?" \
  --schedule "0 18 * * *" \
  --enabled-toolsets "terminal,web,file,send_message"

# Nightly self-improvement
hermes cron create \
  --name "nightly-improvement" \
  --prompt "Review today's work. What went wrong? Update skills with fixes." \
  --schedule "0 23 * * *" \
  --enabled-toolsets "terminal,file,skills"
```

## Step 8: Start the Gateway

```bash
# Run in background
hermes gateway run --replace

# Verify
hermes gateway status
# → Gateway running · 3 platforms connected · 38 crons active

# Monitor logs
journalctl --user -f -u hermes-gateway
```

## Step 9: Add a Worker Node (Optional)

```bash
# Set up Mac Mini for browser automation + social publishing
ssh-keygen -t ed25519
ssh-copy-id worker@worker-node.local

# Deploy Postiz
ssh worker@worker-node.local "npm install -g postiz-cli"

# Deploy Playwright
ssh worker@worker-node.local "pip install playwright && playwright install chromium"

# Test
ssh worker@worker-node.local "echo connected"
```

## Complete Verification

```bash
# Run the full health check
hermes doctor

# Should return:
# ✅ Hermes Agent v0.16.0
# ✅ Python 3.11+
# ✅ Model configured (deepseek-v4-pro)
# ✅ MCP servers: corpusiq (53 tools), honcho (peer memory)
# ✅ Memory: GBrain (729 files), memcore-cloud (active)
# ✅ Gateway: running
# ✅ Crons: 3+ active
# ✅ Messaging: Telegram connected
```

## Next Steps

- [Full Memory Architecture →](/hermes/knowledge/)
- [MCP Integration Guide →](/hermes/mcp/)
- [Production Cron Reference →](/hermes/governance/scheduling/)
- [Multi-Machine Deployment →](/hermes/infrastructure/)

---

## Platform-Specific Notes

### Linux (DGX Spark / Ubuntu)

```bash
# Additional deps
sudo apt install python3-dev build-essential ffmpeg

# Increase file watchers (for crons)
echo "fs.inotify.max_user_watches=524288" | sudo tee -a /etc/sysctl.conf
```

### macOS (Mac Mini)

```bash
# Additional deps
brew install ffmpeg python@3.11

# Allow background processes
# System Settings → General → Login Items → Allow Hermes
```

### Docker

```bash
docker run -d \
  -v ~/.hermes:/home/hermes/.hermes \
  -e HERMES_PROFILE=production \
  nousresearch/hermes-agent:latest
```

---

*Now go build something autonomous.*
