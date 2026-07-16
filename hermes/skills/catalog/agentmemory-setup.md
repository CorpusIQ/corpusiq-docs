---
title: AgentMemory Setup — Persistent Memory for Hermes Agents
description: Install and configure rohitg00/agentmemory — #1 persistent memory for AI coding agents with Hermes support. No more re-explaining your codebase.
author: rohitg00
repo: https://github.com/rohitg00/agentmemory
stars: 25,207
license: MIT
---

# AgentMemory Setup Guide

**Source:** [rohitg00/agentmemory](https://skills.sh/rohitg00/agentmemory) (25,207 ⭐)
**Category:** Agent Infrastructure / Memory

AgentMemory is the #1 persistent memory system for AI coding agents based on real-world benchmarks. It gives your Hermes agent persistent memory across sessions — your agent remembers codebase structure, your preferences, past decisions, and learned patterns without re-explaining everything on every restart.

Supported agents: **Hermes**, Claude Code, GitHub Copilot CLI, Cursor, Gemini CLI, Codex CLI, OpenClaw, pi, OpenCode, and any MCP client.

---

## Quick Install

```bash
# Via skills.sh (recommended)
npx skills add rohitg00/agentmemory@agentmemory-agents

# Direct from GitHub
cd ~/.hermes/skills/
git clone https://github.com/rohitg00/agentmemory.git
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ (for npx install) |
| **Hermes Agent** | v0.16.0+ |
| **MCP support** | Required for MCP-based memory backends |

---

## How It Works

AgentMemory builds on the **iii engine** (https://github.com/iii-hq/iii) to provide:

1. **Session persistence** — Memory survives restarts, crashes, and model switches
2. **Codebase awareness** — Agent remembers file structure, key modules, and architectural decisions
3. **User preferences** — Stores your coding style, naming conventions, and tool preferences
4. **Pattern learning** — Identifies recurring workflows and optimizes over time
5. **Cross-agent compatibility** — Same memory works across Hermes, Claude Code, Cursor, and other agents

---

## Configuration

After installation, configure AgentMemory through your Hermes profile:

```yaml
# ~/.hermes/profiles/corpusiq/config.yaml
memory:
  provider: agentmemory
  agentmemory:
    storage_backend: sqlite  # or postgres, filesystem
    auto_save: true
    save_interval: 300  # seconds
```

### Memory Storage Backends

| Backend | Best For | Notes |
|---|---|---|
| **SQLite** (default) | Single-agent, local | Zero config, fastest setup |
| **PostgreSQL** | Multi-agent, team | Shared memory across agents |
| **Filesystem** | Git-tracked memory | Version-controlled agent knowledge |

---

## Key Capabilities

| Capability | Trigger | What It Does |
|---|---|---|
| **Auto-memory** | Automatic on file changes | Saves codebase structure changes without prompting |
| **Preference recall** | "remember I prefer X" | Stores user preferences for future sessions |
| **Decision log** | After major decisions | Records architectural decisions with rationale |
| **Pattern recording** | On repeated workflows | Identifies and stores recurring patterns |
| **Session handoff** | End of session | Exports memory state for next session recovery |

---

## Why This Matters for Hermes

Without persistent memory, every Hermes session starts fresh — the agent forgets:

- What files you modified last session
- Which crons are paused and why
- Token/auth status across services
- User corrections and preferences
- Pain points discovered during debugging

AgentMemory solves this by maintaining a persistent, structured knowledge base that survives across sessions, restarts, and model switches. Combined with Honcho + GBrain, it creates a three-tier memory architecture:

1. **AgentMemory** — Codebase and workflow memory (structural)
2. **Honcho** — Session context and channel state (operational)
3. **GBrain** — Semantic knowledge and long-term facts (semantic)

---

## Production Notes

- 25K+ GitHub stars, trending #1 on TrendShift
- Built on the iii engine — production-grade, benchmarked
- 12-language README (English, Chinese, Japanese, Korean, Spanish, Turkish, Russian, Hindi, Portuguese, French, German)
- Active development (updated daily as of July 2026)
- Hermes is explicitly listed as a supported agent

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Memory not persisting | `auto_save: false` | Set `auto_save: true` in config |
| Cross-agent conflicts | Different agents writing simultaneously | Use PostgreSQL backend for multi-agent |
| Memory bloat | No pruning configured | Set `max_entries` and `prune_older_than` |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [MCP Use Setup →](/hermes/skills/catalog/mcp-use-setup/)*
*Powered by CorpusIQ*
