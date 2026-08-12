---
title: "Multi-Machine Deployment Architecture"
description: "Production agent deployment pattern: a GPU primary node for inference and scheduling, plus a worker node for browser automation and content operations."
---

# Multi-Machine Deployment Architecture

Production agents need dedicated hardware. Here's the architecture pattern.

## Why Two Machines?

| Problem | Single Machine | Two Machines |
|---------|---------------|--------------|
| Browser automation crashes | Takes down your agent | Isolated on worker — agent stays up |
| Video rendering pegs CPU | Blocks all other tasks | Offloaded to worker with FFmpeg |
| Social publishing failures | Can't post anywhere | Worker node runs Postiz independently |
| Memory pressure | LLM + browser + video = OOM | LLM on primary, everything else on worker |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRIMARY COMPUTE NODE                          │
│  OS: Linux · GPU: NVIDIA                                         │
│                                                                  │
│  Services:                                                       │
│  ├── Hermes Gateway (production instance)                        │
│  ├── Production crons (multi-category scheduling)                │
│  ├── Session memory (peer context sharing)                       │
│  ├── Business tool connectors (MCP)                              │
│  ├── Knowledge graph (vector search)                             │
│  ├── Cross-session context store                                 │
│  ├── Ollama (local embeddings, lightweight inference)            │
│  └── LLM provider (primary inference via API)                    │
│                                                                  │
│  Model Routing:                                                  │
│  ├── Lightweight: daily ops, monitoring                          │
│  ├── Mid-tier: research, content, coding                        │
│  └── Heavy: strategy, complex analysis                          │
│                                                                  │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                    SSH (key-based auth)
                            │
┌───────────────────────────┴──────────────────────────────────────┐
│                  WORKER NODE (macOS, ARM64)                       │
│  OS: macOS (ARM64)                                                │
│                                                                  │
│  Services:                                                       │
│  ├── Postiz CLI (social publishing — X, LinkedIn, TikTok, IG)    │
│  ├── Playwright (browser automation, stealth)                    │
│  ├── FFmpeg (video post-production)                              │
│  ├── patchright (Cloudflare bypass)                              │
│  └── Content pipelines (video, docs, media)                      │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Node Pages

| Page | Purpose |
|------|---------|
| [Primary Compute (DGX Spark)](dgx/) | GPU workstation as inference + scheduling hub |
| [Worker Node (Mac Mini M4)](mac-mini/) | Dedicated worker for browser + content ops |
| [Authentication Management](auth/) | OAuth tokens, API keys, rotation patterns |
| [Browser Automation Architecture](browser/) | Playwright stealth + persistent contexts |
| [Multi-Model Routing](routing/) | Cost-optimized model selection |

## Key Decisions

1. **Two machines beat one big one.** Isolation between inference and browser/video workloads prevents cascade failures.
2. **Primary node never runs browsers.** Browsers leak memory and crash; keep them off the inference box.
3. **Worker node handles all external publishing.** Social APIs, browser automation, and media processing live on the worker.
4. **SSH key auth between nodes.** Agent-to-agent automation needs key-based SSH, never passwords.
