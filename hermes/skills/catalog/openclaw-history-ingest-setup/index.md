---
title: "openclaw-history-ingest Setup Guide"
description: "Complete setup guide for openclaw-history-ingest — ingest OpenClaw agent conversation history into an Obsidian wiki vault."
---

# openclaw-history-ingest Setup Guide

**Skill:** `openclaw-history-ingest` · **Installs:** 2,700+ · **Source:** [ar9av/obsidian-wiki](https://github.com/ar9av/obsidian-wiki)

openclaw-history-ingest extracts OpenClaw agent conversation history — MEMORY.md entries, session JSONL logs, and decision artifacts — and ingests them into an Obsidian wiki vault. Enables unified knowledge management across Hermes and OpenClaw agents.

---

## Capabilities

- Extract OpenClaw MEMORY.md and session JSONL data
- Convert to structured Obsidian markdown notes
- Link related sessions and decisions automatically
- Tag and categorize ingested content
- Support incremental ingestion (only new/changed data)

## Prerequisites

OpenClaw installed at ~/.openclaw, Obsidian vault configured, Python 3.10+.

## Installation

```bash
npx skills add ar9av/obsidian-wiki --skill openclaw-history-ingest
```

## Usage

Load the skill in your agent session:

```
/ openclaw-history-ingest
```

The skill activates and provides browser automation tools accessible through natural language commands.

## Troubleshooting

| Issue | Fix |
|---|---|
| Skill not found | Verify `npx skills add` completed successfully and the skill appears in `npx skills list` |
| Browser not launching | Ensure Playwright/Puppeteer is installed system-wide |
| Permission errors on VPS | Check that the agent user has access to the browser binary |

## Related Skills

- [wiki-history-ingest](/hermes/skills/catalog/wiki-history-ingest-setup/) — Unified agent history ingestion router
- [hermes-history-ingest](/hermes/skills/catalog/hermes-history-ingest-setup/) — Hermes agent history ingestion
- [Skills Catalog](/hermes/skills/catalog/)
