---
title: Hermes A2A Bridge Setup Guide
description: Set up the Agent-to-Agent Protocol bridge for Hermes Agent — enable multi-agent collaboration across instances with standardized HTTP+JSON messaging.
skill_name: hermes-a2a-bridge
repo: asimons81/hermes-a2a-bridge
compatibility: Hermes Agent v0.17.0+
installs: New (June 2026)
---

# Hermes A2A Bridge — Setup Guide

## Overview

The Hermes A2A Bridge gives Hermes Agent the ability to communicate with other AI agents using the Agent-to-Agent (A2A) Protocol. While MCP lets agents use tools, A2A lets agents call other agents. This bridge is a local-first implementation of the A2A HTTP+JSON subset.

**Key Facts:**
- **Protocol:** A2A v0.4.6 (HTTP+JSON subset)
- **Python:** 3.11+
- **Transport:** Local HTTP server (default: `127.0.0.1:8765`)
- **Auth:** Bearer token for task endpoints
- **Storage:** SQLite3 task database

---

## Prerequisites

- Python 3.11 or newer
- Hermes Agent v0.17.0+
- Git

---

## Installation

### 1. Clone and Install

```bash
git clone https://github.com/asimons81/hermes-a2a-bridge.git
cd hermes-a2a-bridge
python -m pip install -e .
```

### 2. Enable the Plugin

```bash
hermes plugins enable a2a-bridge
```

> **Note:** If `hermes plugins list` doesn't show the plugin due to a host-side UI gap in v0.17.0, manually add `a2a-bridge` to `plugins.enabled` in `~/.hermes/config.yaml`:

```yaml
plugins:
  enabled:
    - a2a-bridge
```

### 3. Initialize

```bash
hermes a2a init
```

This creates:
- `~/.hermes/a2a/config.yaml` — bridge configuration
- `~/.hermes/a2a/tasks.sqlite3` — task persistence

### 4. Start the Server

```bash
hermes a2a serve
```

---

## Configuration

Default config at `~/.hermes/a2a/config.yaml`:

```yaml
server:
  host: 127.0.0.1
  port: 8765
  public_url: http://127.0.0.1:8765

executor:
  command: hermes chat -q {prompt}

auth:
  bearer_token: auto-generated
```

### Key Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `server.host` | `127.0.0.1` | Bind address (use `0.0.0.0` for network access) |
| `server.port` | `8765` | HTTP server port |
| `server.public_url` | `http://127.0.0.1:8765` | Public-facing URL for agent card |
| `executor.command` | `hermes chat -q {prompt}` | Hermes invocation command |
| `auth.bearer_token` | auto-generated | Token for task endpoint auth |

---

## Usage

### Verify Agent Card

```bash
hermes a2a card --json
curl http://127.0.0.1:8765/.well-known/agent-card.json
```

### Send a Task to Another Agent

```bash
# From another A2A-compatible agent:
curl -X POST http://127.0.0.1:8765/tasks \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Analyze the Q2 growth metrics and suggest 3 optimizations",
    "context": {"company": "CorpusIQ", "domain": "growth"}
  }'
```

### Discover Remote Agents

```bash
hermes a2a discover
hermes a2a agents
```

---

## Capabilities

- **Agent Card:** Self-describing metadata endpoint (`.well-known/agent-card.json`)
- **Task Submission:** HTTP POST tasks with text + structured JSON data parts
- **Task Polling:** Check task status and retrieve results
- **Bearer Auth:** Token-protected task endpoints
- **SQLite Persistence:** Tasks survive restarts
- **File ID References:** Gated file references for secure data sharing
- **Multi-Agent Discovery:** Find and catalog other A2A agents on the network

---

## Use Cases for CorpusIQ

### 1. Multi-Agent Growth Pipeline
Run specialized agents in parallel — one for social monitoring, one for lead research, one for content — coordinated via A2A:

```bash
hermes a2a serve &
hermes a2a discover
hermes a2a task --agent social-agent "Monitor Reddit for SaaS growth discussions"
hermes a2a task --agent research-agent "Research lead from @acmecorp"
```

### 2. Cross-Team Agent Collaboration
Enable the CorpusIQ growth agent to delegate specialized tasks to other Hermes instances:

```
Growth Agent → A2A → Content Agent (drafts posts)
Growth Agent → A2A → Research Agent (competitor analysis)
Growth Agent → A2A → Data Agent (pipeline metrics)
```

### 3. Distributed Agent Architecture
Deploy agents on separate machines (Mac Mini, cloud VM, Raspberry Pi) and coordinate via A2A:

```yaml
# On cloud VM: research agent
server:
  host: 0.0.0.0
  port: 8765
  public_url: https://research.corpusiq.io

# On Mac Mini: growth agent discovers and tasks cloud agent
hermes a2a discover --network
hermes a2a task --agent research.corpusiq.io "..."
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Plugin not visible in `hermes plugins list` | Manually add to `config.yaml` (see Installation step 2) |
| `No Hermes executor command configured` | Set `executor.command` in `~/.hermes/a2a/config.yaml` |
| Connection refused | Ensure server is running: `hermes a2a serve` |
| Auth errors on task endpoints | Check bearer token in `~/.hermes/a2a/config.yaml` |
| Port already in use | Change `server.port` in config |

---

## Verification

```bash
# 1. Check plugin is loaded
hermes plugins list | grep a2a

# 2. Verify initialization
ls ~/.hermes/a2a/config.yaml ~/.hermes/a2a/tasks.sqlite3

# 3. Start and test
hermes a2a serve &
sleep 2
curl http://127.0.0.1:8765/.well-known/agent-card.json | python3 -m json.tool

# 4. Check agent card
hermes a2a card --json
```

---

## Limitations

- **Not full A2A compliance:** This implements the HTTP+JSON subset only
- **Local-first:** Default bind is `127.0.0.1` — network access requires explicit config
- **v0.17.0 UI gap:** Plugin discovery in `hermes plugins list` may require manual config.yaml edit
- **No streaming tasks:** Tasks are submitted and polled, not streamed

---

*← [Skills Catalog](/hermes/skills/catalog/) | [A2A Bridge on GitHub](https://github.com/asimons81/hermes-a2a-bridge) →*

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
