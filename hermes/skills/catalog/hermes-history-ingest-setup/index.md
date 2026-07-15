---
title: "hermes-history-ingest Setup Guide"
description: "Complete setup guide for hermes-history-ingest — ingest Hermes agent conversation history and session data into an Obsidian wiki vault."
---

# hermes-history-ingest Setup Guide

**Skill:** `hermes-history-ingest` · **Installs:** 2,700+ · **Source:** [ar9av/obsidian-wiki](https://github.com/ar9av/obsidian-wiki)

hermes-history-ingest extracts Hermes agent conversation history — memory snapshots, session data, and decision logs — and ingests them into an Obsidian wiki vault. Enables long-term knowledge retention, cross-session pattern discovery, and searchable agent memory.

---

## Capabilities

- Extract Hermes memory entries and session artifacts
- Convert to structured Obsidian markdown notes
- Link related sessions and decisions automatically
- Tag and categorize ingested content
- Support incremental ingestion (only new/changed data)

## Prerequisites

Hermes agent installed at ~/.hermes, Obsidian vault configured, Python 3.10+.

## Installation

```bash
npx skills add ar9av/obsidian-wiki --skill hermes-history-ingest
```

## Usage

Load the skill in your agent session:

```
/ hermes-history-ingest
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
- [openclaw-history-ingest](/hermes/skills/catalog/openclaw-history-ingest-setup/) — OpenClaw agent history ingestion
- [Skills Catalog](/hermes/skills/catalog/)
