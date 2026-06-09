---
title: Agent Infrastructure
description: Production infrastructure for Hermes agents — DGX Spark, Mac Mini worker, browser automation, model routing
---

# Infrastructure

## Compute Architecture

| Node | Role | Specs |
|------|------|-------|
| NVIDIA DGX Spark | Primary: inference, orchestration, memory | Custom ARM64 |
| Apple Mac Mini M4 | Worker: browser, content, video | 16GB ARM64 |

Distributed to optimize cost and throughput.

## Browser Automation

Browser-use on dedicated worker node with Playwright stealth. Persistent contexts maintain session continuity, cookies, and auth states.

## Multi-Model Routing

| Task | Model | Cost |
|------|-------|------|
| Lightweight | Qwen | $0 |
| Local | Ollama/Llama3 | $0 |
| Advanced | DeepSeek V4 | $$ |
| Strategic | Claude Opus | $$$ |

~65% cost reduction vs premium-only routing.

## MCP Infrastructure

FastMCP + Pydantic validation. 53 operational tools. Type safety, schema enforcement, reliable invocation.

---

*Next: [Governance](/governance/) · [Setup Guide](/setup/)*
