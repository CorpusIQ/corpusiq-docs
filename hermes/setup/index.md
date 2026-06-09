---
title: Hermes Setup Guide
description: Complete Hermes Agent installation and configuration for production deployments
---

# Hermes Setup Guide

Production installation guides covering single-machine, dual-machine (DGX + Mac Mini), and cloud deployments.

## Installation

### Prerequisites

- Linux (ARM64 or x86_64) or macOS
- Python 3.10+
- Node.js 18+ (for browser automation)

### Quick Install

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

### Production Deployment: DGX Spark + Mac Mini

The reference architecture splits compute across two machines:

**DGX Spark (Primary)**
- Hermes agent core
- LLM inference
- Orchestration scheduling
- Memory and knowledge systems

**Mac Mini M4 (Worker)**
- Browser automation
- Content generation
- Video processing
- Engagement engines

#### DGX Setup

```bash
hermes setup
hermes config set provider.default anthropic
hermes config set provider.fallback openai
```

#### Mac Mini Worker Setup

```bash
# SSH key exchange
ssh-copy-id media@medias-mac-mini.local

# Install Hermes on worker
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Configure as worker node
hermes config set role worker
hermes config set primary-node dgx-spark.local
```

### Configuration

#### Multi-Model Routing

Configure model routing by task complexity:

```yaml
models:
  lightweight: qwen3.6:27b
  local: ollama/llama3
  advanced: deepseek-v4
  strategic: anthropic/claude-opus-4
```

#### Browser Automation

```yaml
browser:
  engine: playwright
  stealth: true
  persistent_contexts: true
  worker_node: medias-mac-mini.local
```

#### MCP Server Registration

```yaml
mcp_servers:
  corpusiq:
    url: https://mcp.corpusiq.io
    tools: 53
    auth: oauth
```

## Verification

```bash
hermes status          # System health
hermes tools           # Available tools
hermes skills list     # Loaded skills
```

---

*Next: [Architecture Overview](/architecture/) · [MCP Integration](/mcp/)*
