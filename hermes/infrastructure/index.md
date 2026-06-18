# Multi-Machine Deployment — DGX Spark + Mac Mini Worker

Production agents need dedicated hardware. Here's the architecture we run.

## Why Two Machines?

| Problem | Single Machine | Two Machines |
|---------|---------------|--------------|
| Browser automation crashes | Takes down your agent | Isolated on worker — agent stays up |
| Video rendering pegs CPU | Blocks all other tasks | Offloaded to worker with FFmpeg |
| Social publishing failures | Can't post anywhere | Mac Mini runs Postiz independently |
| Memory pressure | LLM + browser + video = OOM | LLM on DGX, everything else on Mac Mini |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    DGX SPARK (Primary)                           │
│  OS: Linux (ARM64) · RAM: 128GB · GPU: NVIDIA                    │
│                                                                  │
│  Services:                                                       │
│  ├── Hermes Gateway (PID 35253 — running since Jun 12)           │
│  ├── 38 production crons                                         │
│  ├── Honcho MCP (peer memory)                                    │
│  ├── CorpusIQ MCP (53 business tools)                            │
│  ├── GBrain (729 indexed files, pglite, 768d vectors)            │
│  ├── memcore-cloud (cross-session context)                       │
│  ├── Ollama (local embeddings, lightweight inference)            │
│  └── DeepSeek V4 Pro (primary LLM via OpenRouter)                │
│                                                                  │
│  Model Routing:                                                  │
│  ├── Qwen: Lightweight ops ($0.001/task)                        │
│  ├── Ollama: Local embeddings (free)                             │
│  ├── DeepSeek V4: Research, content, coding ($0.01/task)        │
│  └── Claude Opus: Strategy, contracts ($0.05/task)              │
│                                                                  │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                    SSH (key-based auth)
                            │
┌───────────────────────────┴──────────────────────────────────────┐
│                  MAC MINI M4 (Worker)                             │
│  OS: macOS (ARM64) · RAM: 16GB                                   │
│                                                                  │
│  Services:                                                       │
│  ├── Postiz CLI (social publishing — X, LinkedIn, TikTok, IG)    │
│  ├── Playwright (browser automation, stealth)                    │
│  ├── FFmpeg (video post-production)                              │
│  ├── patchright (Cloudflare bypass)                              │
│  └── Instagram DM outreach (instagrapi)                          │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## DGX Spark Setup

### 1. Base Installation

```bash
# Hermes Agent
pip install hermes-agent

# Memory stack
pip install memcore-cloud
git clone https://github.com/garrytan/gbrain && cd gbrain && ./setup.sh

# MCP servers
hermes mcp add corpusiq -- url https://mcp2.corpusiq.io/mcp
hermes mcp add honcho -- npx mcp-remote https://mcp.honcho.dev

# Local inference (optional, for embeddings and lightweight tasks)
curl -fsSL https://ollama.com/install.sh | sh
ollama pull nomic-embed-text
```

### 2. Profile Setup

```bash
hermes profile create corpusiq
hermes config set model.default deepseek/deepseek-v4-pro
hermes config set model.fallback "openrouter/qwen/qwen3-235b-a22b:free,anthropic/claude-opus-4"
```

### 3. Gateway

```bash
# Start the gateway (background, auto-restart on crash)
hermes gateway run --replace

# Verify
hermes gateway status
```

---

## Mac Mini Worker Setup

### 1. Base

```bash
# Hermes Agent (same version)
pip install hermes-agent

# Postiz (social publishing)
npm install -g postiz-cli
postiz auth

# Playwright (browser automation)
pip install playwright
playwright install chromium

# FFmpeg (video)
brew install ffmpeg
```

### 2. SSH Key Setup

```bash
# On DGX Spark
ssh-keygen -t ed25519 -f ~/.ssh/mac-mini
ssh-copy-id -i ~/.ssh/mac-mini.pub user@worker-node.local

# Test
ssh user@worker-node.local "echo connected"
```

### 3. Worker Scripts

```bash
# Deploy video pipeline workers
scp ~/worker/videos/* user@worker-node.local:~/worker/videos/

# Deploy Postiz scripts
scp ~/worker/social/* user@worker-node.local:~/worker/social/
```

---

## Orchestration Patterns

### Pattern 1: Video Pipeline

```bash
# On DGX Spark:
# 1. Generate video with HeyGen API
python3 heygen-video-generator.py

# 2. Post-produce with FFmpeg
ffmpeg -i input.mp4 -vf "zoompan=..." -c:a copy output.mp4

# 3. Transfer to Mac Mini
scp output.mp4 user@worker-node.local:~/worker/videos/

# 4. Publish via Postiz (on Mac Mini)
ssh user@worker-node.local "postiz upload ~/worker/videos/output.mp4 && postiz posts:create --platform tiktok --video output.mp4"
```

### Pattern 2: Social Publishing

```bash
# On DGX Spark (or via cron):
ssh user@worker-node.local "postiz posts:create \
  --platform x \
  --connector cmpoar9y201icl70y7iof708s \
  --content 'Your post text here'"
```

### Pattern 3: Browser Automation

```bash
# On Mac Mini (via SSH from DGX):
ssh user@worker-node.local "python3 ~/worker/browser/task.py"
```

---

## Model Routing Strategy

Not every task needs Claude Opus. Here's how we route:

```python
# Intelligent model switching based on task complexity

def route_model(task):
    if task.type == "lightweight":
        return "openrouter/qwen/qwen3-235b-a22b:free"  # ~$0.001
    
    if task.type == "embedding":
        return "ollama/nomic-embed-text"  # Free, local
    
    if task.type in ("research", "content", "coding", "social"):
        return "deepseek/deepseek-v4-pro"  # ~$0.01/task
    
    if task.type in ("strategy", "architecture", "contracts"):
        return "anthropic/claude-opus-4"  # ~$0.05/task
```

**Cost savings:** ~65% vs running everything on Claude Opus.

---

## Monitoring

### Health Check (10 PM daily)

```bash
# On DGX Spark
hermes cron list | grep -c "active"
hermes mcp test corpusiq
hermes mcp test honcho

# On Mac Mini
ssh user@worker-node.local "postiz list"
ssh user@worker-node.local "pgrep -f playwright"
```

### Disk & Memory

```bash
# On both nodes
df -h /
free -h  # Linux
vm_stat  # macOS
```

---

## Recovery Procedures

### Gateway Crash

```bash
# Check if running
hermes gateway status

# Restart
hermes gateway run --replace

# Check logs
journalctl --user -u hermes-gateway -n 100
```

### Mac Mini Unreachable

```bash
# Ping test
ping worker-node.local

# If down: Postiz and browser automation will queue
# Crons will skip with error → retry on next tick
```

### OAuth Token Expired

```bash
# Gmail
python3 refresh_gmail_token.py

# GitHub (classic PAT — never expires)
# Verify: curl -H "Authorization: token $(cat secrets/github.token)" https://api.github.com/user
```

---

## Lessons Learned

1. **Browser automation is fragile** — offload it. Playwright crashes shouldn't take down your agent.
2. **Key-based SSH is mandatory** — password auth fails silently in cron environments.
3. **Postiz on Mac Mini is stable** — better than running social publishing directly from the agent.
4. **Model routing saves real money** — ~65% savings compounds at 24/7 operation.
5. **Monitor both machines** — the health check must verify the worker node too.
6. **Keep Hermes versions synced** — DGX and Mac Mini must run the same version.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
