---
title: "BitRouter — Self-Improving LLM Router for Agent Workflows"
description: "Install and configure BitRouter to optimize LLM routing for Hermes Agent, OpenClaw, Claude Code, and other agent harnesses."
---

# BitRouter Setup Guide

**Repo:** [bitrouter/bitrouter](https://github.com/bitrouter/bitrouter)
**Stars:** ⭐209 | **License:** Apache-2.0 | **Language:** Rust
**Install:** `cargo install bitrouter`

## Overview

BitRouter is a self-improving LLM router that optimizes agentic workflows with every run. It sits between your agent harness and LLM providers, routing each request to the optimal model based on cost, latency, and quality. Works with any harness (Hermes, OpenClaw, Claude Code, Codex) and any model.

**Key capabilities:**
- Self-improving routing — learns from every request
- Multi-model dispatch: DeepSeek, OpenAI, Anthropic, Ollama, and more
- Agent observability: token tracking, cost analysis, latency metrics
- Guardrails: rate limiting, content filtering, cost caps
- MCP-ready for agent integration
- OpenTelemetry-native for monitoring

## Prerequisites

- Rust toolchain (for building from source) OR Docker
- At least one LLM provider API key (OpenAI, Anthropic, DeepSeek, etc.)

## Installation

```bash
# Via cargo
cargo install bitrouter

# Via Docker
docker pull bitrouter/bitrouter:latest
docker run -d -p 8080:8080 \
  -e OPENAI_API_KEY=\$OPENAI_API_KEY \
  -e ANTHROPIC_API_KEY=\$ANTHROPIC_API_KEY \
  bitrouter/bitrouter
```

## Configuration

```yaml
# ~/.bitrouter/config.yaml
server:
  port: 8080
  host: "127.0.0.1"

providers:
  - name: deepseek
    base_url: https://api.deepseek.com/v1
    api_key_env: DEEPSEEK_API_KEY
    models:
      - deepseek-v4-pro
      - deepseek-chat
  - name: anthropic
    base_url: https://api.anthropic.com/v1
    api_key_env: ANTHROPIC_API_KEY
    models:
      - claude-sonnet-4-20250514
      - claude-opus-4-20250514

routing:
  strategy: cost_quality  # cost_only | latency_first | cost_quality | learning
  learning_window: 1000   # requests to analyze before self-improving
  cost_cap_daily: 50.00   # USD
```

## Integration with Hermes

Point Hermes to use BitRouter as its LLM provider:

```yaml
# ~/.hermes/config.yaml
model:
  default: bitrouter/auto        # Let BitRouter pick the model
  provider: bitrouter
  base_url: http://127.0.0.1:8080/v1
```

## Verification

```bash
# Health check
curl http://127.0.0.1:8080/health

# Test routing
curl -X POST http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"auto","messages":[{"role":"user","content":"Hello"}]}'

# Check routing stats
bitrouter stats
```

## Pitfalls

- Self-improving mode needs ~1000 requests before routing noticeably improves
- Docker image requires proper volume mounting for persistent learning data
- When API keys expire, BitRouter auto-routes to available providers
- Not a model aggregator — requires individual provider API keys
