---
title: wiki-history-ingest Setup Guide
description: Complete setup guide for wiki-history-ingest — unified agent history ingestion router for Hermes, OpenClaw, Claude, Codex, Copilot, and Pi agents into an Obsidian wiki vault.
---

# wiki-history-ingest Setup Guide

**Skill:** `wiki-history-ingest` · **Installs:** 2,744 · **Source:** [ar9av/obsidian-wiki](https://github.com/ar9av/obsidian-wiki)

Unified entrypoint for ingesting agent conversation history into an Obsidian wiki vault. Routes `/wiki-history-ingest hermes` and `/wiki-history-ingest openclaw` to their respective specialized history ingestion skills.

---

## Prerequisites

- **Obsidian** vault set up with the [obsidian-wiki](https://github.com/ar9av/obsidian-wiki) plugin structure
- **Python 3.10+** for the ingestion scripts
- **Agent history files** accessible at standard paths:
  - Hermes: `~/.hermes/` (memories, sessions)
  - OpenClaw: `~/.openclaw/` (MEMORY.md, session JSONL)
  - Claude: `~/.claude/` (memory/session JSONL)
  - Codex: `~/.codex/` (rollout/session index)
  - Copilot: `~/.copilot/` or `session-store.db`

---

## Installation

```bash
npx skills add ar9av/obsidian-wiki --skill wiki-history-ingest
```

The skill installs to your agent's skills directory. It works as a thin router — it dispatches to destination skills (`hermes-history-ingest`, `openclaw-history-ingest`, etc.) which must also be installed.

### Install destination skills

```bash
# For Hermes agent history
npx skills add ar9av/obsidian-wiki --skill hermes-history-ingest

# For OpenClaw agent history
npx skills add ar9av/obsidian-wiki --skill openclaw-history-ingest

# For Claude, Codex, Copilot, Pi (as needed)
npx skills add ar9av/obsidian-wiki --skill claude-history-ingest
npx skills add ar9av/obsidian-wiki --skill codex-history-ingest
npx skills add ar9av/obsidian-wiki --skill copilot-history-ingest
npx skills add ar9av/obsidian-wiki --skill pi-history-ingest
```

---

## Capabilities

| Subcommand | Routes To | Source Path Auto-Detection |
|---|---|---|
| `hermes` | `hermes-history-ingest` | `~/.hermes` memories/session artifacts |
| `openclaw` | `openclaw-history-ingest` | `~/.openclaw` MEMORY.md / session JSONL |
| `claude` | `claude-history-ingest` | `~/.claude` memory/session JSONL |
| `codex` | `codex-history-ingest` | `~/.codex` rollout/session index |
| `copilot` | `copilot-history-ingest` | `~/.copilot` session-store.db |
| `pi` | `pi-history-ingest` | `~/.pi/agent/sessions` |
| `auto` | Infers from context | Uses source path detection rules |

---

## Usage

### Basic: Ingest Hermes history

```
/wiki-history-ingest hermes
```

This routes to `hermes-history-ingest` which processes Hermes memories and session data into structured Obsidian notes.

### Auto-detect from path

```
/wiki-history-ingest auto ~/.hermes/profiles/corpusiq/
```

The router detects `~/.hermes` in the path and dispatches to `hermes-history-ingest`.

### Ingest all agent histories

```
/wiki-history-ingest claude
/wiki-history-ingest codex
/wiki-history-ingest hermes
/wiki-history-ingest openclaw
```

---

## CorpusIQ Use Cases

**Agent session archival:** After each Hermes session, ingest the conversation history into the CorpusIQ knowledge wiki for long-term search and retrieval.

**Cross-agent context synthesis:** Ingest history from Hermes, Claude Code, and Codex into a unified vault — then use `wiki-synthesize` to find patterns across agent sessions.

**Compliance and audit:** Maintain a searchable archive of all agent interactions for governance and audit requirements.

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `Skill not found: hermes-history-ingest` | Install the destination skill first: `npx skills add ar9av/obsidian-wiki --skill hermes-history-ingest` |
| `No such file: ~/.hermes` | Verify Hermes is installed and has generated session data at the standard path |
| Router dispatches to wrong skill | Use explicit subcommand instead of `auto` — e.g., `/wiki-history-ingest hermes` |
| Empty vault after ingest | Check that the destination skill's Python dependencies are installed (`pip install -r requirements.txt` in the obsidian-wiki repo) |

---

## Related Skills

- [hermes-history-ingest](/hermes/skills/catalog/hermes-history-ingest-setup/) — Hermes-specific history ingestion
- [openclaw-history-ingest](/hermes/skills/catalog/openclaw-history-ingest-setup/) — OpenClaw-specific history ingestion
- [wiki-synthesize](https://skills.sh/ar9av/obsidian-wiki) — Cross-session pattern synthesis
- [wiki-query](https://skills.sh/ar9av/obsidian-wiki) — Natural language vault queries

---

*← [Skills Marketplace](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
