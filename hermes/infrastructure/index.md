---
title: Agent Infrastructure
description: Production infrastructure for Hermes agents — DGX Spark, Mac Mini worker, browser automation, model routing
---

# Agent Infrastructure

Production infrastructure for Hermes agents running 24/7 on a dual-machine deployment.

| Page | What You'll Learn |
|------|-------------------|
| [DGX Spark](/hermes/infrastructure/dgx/) | NVIDIA DGX hardware, GPU compute config, 21 cron jobs, model hosting |
| [Mac Mini M4](/hermes/infrastructure/mac-mini/) | macOS worker node, Playwright, browser automation, SSH management |
| [Browser Automation](/hermes/infrastructure/browser/) | Playwright setup, agent-browser, stealth mode, cookie persistence |
| [Authentication](/hermes/infrastructure/auth/) | OAuth token lifecycle, headless refresh, dual Gmail accounts |
| [Model Routing](/hermes/infrastructure/routing/) | Qwen-first routing, cost optimization, model selection strategy |

## Dual-Machine Architecture

```
DGX Spark (primary — 21 cron jobs)
├─ LLM hosting (DeepSeek, Qwen, Llama)
├─ Core agent operations
├─ Email monitoring & response
├─ Social media automation
└─ Daily reporting

Mac Mini M4 (worker — 4 cron jobs)
├─ Playwright browser automation
├─ HeyGen video generation
├─ Postiz social deployment
└─ GitHub contribution monitoring
```

## Why Dual-Machine?

The DGX handles compute-heavy LLM inference and core operations. The Mac Mini handles browser-based tasks that need a real GUI — Playwright, video rendering, social media posting tools that require Chromium. SSH bridge connects them.

---

*← [Setup](/hermes/setup/) | [Governance](/hermes/governance/) →*
*↑ [Home](/hermes/)*
