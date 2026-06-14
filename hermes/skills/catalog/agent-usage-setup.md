---
title: Agent Usage Monitor — Full Setup Guide for Hermes Agents
description: Install, configure, and use the agent-usage skill from briqt/agent-usage. Cross-agent spending and cost tracking across Hermes, Claude Code, Codex CLI, and more.
---

# Agent Usage Monitor — Setup Guide

**Source:** [briqt/agent-usage](https://skills.sh/briqt/agent-usage) (32 installs)
**Category:** Monitoring / Cost Tracking

Cross-agent usage and cost tracking. Query AI coding agent spending, token consumption, model costs, session history, and API call counts — all from within conversation. **Supports Hermes Agent, Claude Code, Codex CLI, OpenClaw, OpenCode, Kiro, and Pi.**

---

## Installation

```bash
npx skills add briqt/agent-usage
```

The skill auto-discovers supported agents on first run and configures data sources accordingly.

---

## Architecture

### Two Backends

| Backend | When Used | Accuracy |
|---|---|---|
| **REST API Server** | Preferred — start an API server backed by a shared SQLite database | High (live pricing data) |
| **Local JSONL Parser** | Fallback — parses log files directly | Approximate (heuristic pricing) |

### Hermes Agent Data Sources

Reads directly from Hermes SQLite databases:
- `~/.hermes/state.db` — default profile sessions
- `~/.hermes/profiles/*/state.db` — per-profile sessions

Supports **multiple profiles automatically** — all CorpusIQ profiles (corpusiq, dev, etc.) are tracked without extra configuration.

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version with SQLite session tracking |
| **REST API Server** (optional) | Node.js 18+ for the API backend; run `SKILL_DIR/scripts/start-api.sh` |
| **JSONL mode** | Zero dependencies — reads Hermes SQLite directly |

---

## Commands Reference

Once installed, the skill is triggered via natural language or CLI commands:

### Natural Language Triggers

- "How much did I spend on Hermes this month?"
- "Which model costs the most across all my agents?"
- "Show me token usage by day for the last week"
- "Compare Codex vs Hermes spending this month"
- "List all sessions from Friday"

### CLI Commands (via Skill Scripts)

```bash
# Summary: total cost, tokens, sessions
bash SKILL_DIR/scripts/query-api.sh stats --source hermes --from 2026-06-01

# Cost breakdown per model (GPT-4, Sonnet, Opus, etc.)
bash SKILL_DIR/scripts/query-api.sh cost-by-model --source hermes

# List all Hermes sessions with duration and cost
bash SKILL_DIR/scripts/query-api.sh sessions --source hermes

# Token usage trend (1h, 6h, 1d, 7d)
bash SKILL_DIR/scripts/query-api.sh tokens-over-time --source hermes --granularity 1d

# Compare across agents
bash SKILL_DIR/scripts/query-api.sh compare --sources hermes,codex,claude-code

# Session detail
bash SKILL_DIR/scripts/query-api.sh session-detail --source hermes --session-id <id>
```

### JSONL Mode (No API Server)

```bash
# Analyze Hermes state.db directly
bash SKILL_DIR/scripts/analyze-jsonl.sh --source hermes --method sqlite

# Parse all agent logs
bash SKILL_DIR/scripts/analyze-jsonl.sh --source all
```

---

## Setting Up the REST API Server (Recommended)

For accurate pricing with live model costs:

```bash
# Start the API server (background)
bash SKILL_DIR/scripts/start-api.sh &

# The server starts on localhost:4096 by default
# Verify it's running
curl http://localhost:4096/health
```

Without the API server, the skill falls back to JSONL/SQLite parsing with approximate pricing (still useful, just less precise for newer models).

---

## Example Output

```
📊 Agent Usage Report — Hermes (corpusiq)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Period: 2026-06-01 to 2026-06-14
Total cost: $18.42
Total tokens: 4,281,000
Sessions: 87

By model:
  deepseek-v4-pro    $8.21  (2.1M tokens)
  claude-sonnet-4    $7.33  (1.6M tokens)
  claude-opus-4       $2.88  (0.6M tokens)

Daily trend: ▂▃▅▃▂▄▆█▅▄▃▂▄▆
```

---

## CorpusIQ Use Cases

| Use Case | Command/NL Trigger |
|---|---|
| **Monthly spend audit** | "What did CorpusIQ agents spend this month?" |
| **Model cost optimization** | `cost-by-model --source hermes` → identify expensive model usage |
| **ROI tracking** | Compare agent spend vs. leads generated / features shipped |
| **Billing forensics** | "Why did Thursday cost 3x more than Wednesday?" |
| **Session efficiency** | Find sessions with high token burn, low output — optimize prompts |

---

## Cross-Agent Support

| Agent | Data Source | Notes |
|---|---|---|
| **Hermes Agent** | `~/.hermes/state.db`, `~/.hermes/profiles/*/state.db` | Multi-profile auto-discovery |
| **Claude Code** | `~/.claude/sessions/` | JSONL session logs |
| **Codex CLI** | `~/.codex/logs/` | JSONL logs |
| **OpenClaw** | `~/.openclaw/sessions/` | Session directory |
| **OpenCode** | `~/.opencode/logs/` | JSONL format |
| **Kiro** | `~/.kiro/sessions.db` | SQLite |
| **Pi** | `~/.pi/logs/` | JSONL format |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| "No Hermes data found" | Verify `~/.hermes/state.db` exists; ensure at least one session has completed |
| API server won't start | Check port 4096 is free: `lsof -i :4096` |
| Inaccurate pricing | Switch to API server mode for live pricing; JSONL mode uses heuristics |
| Missing sessions from a profile | Run `ls ~/.hermes/profiles/*/state.db` — the skill auto-discovers all profiles |
| Multi-agent compare blank | Each agent must have recorded at least one session |

---

## Verification

```bash
# Verify skill installed
hermes skills list | grep agent-usage

# Quick test — check Hermes data
bash SKILL_DIR/scripts/query-api.sh stats --source hermes --from 2026-06-01

# Or ask naturally in Hermes:
# "How many sessions did I run this week and what did they cost?"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 14 Discovery](/hermes/skills/marketplace/new-june14-2026/) →*
*Powered by CorpusIQ*
