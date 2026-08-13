---
title: Hermes History Ingest — Setup Guide for Hermes Agents
description: Mine Hermes agent session history into Obsidian wiki. Extract insights from past conversations, import ~/.hermes memories, and track knowledge evolution. 2.1K+ installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hermes-history-ingest-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Hermes History Ingest — Setup Guide

**Source:** [ar9av/obsidian-wiki](https://github.com/ar9av/obsidian-wiki) (Community)
**Skill:** `hermes-history-ingest` · **Installs:** 2.1K+ · **Category:** Memory / Knowledge Management
**Platform:** Linux, macOS, Windows

Hermes History Ingest extracts knowledge from your Hermes agent history and distills it into an Obsidian wiki. It mines past sessions for durable knowledge, imports `~/.hermes/memories`, and tracks what's been ingested via a manifest file to avoid duplicates.

## Installation

```bash
npx skills add ar9av/obsidian-wiki@hermes-history-ingest
```

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Obsidian vault | Existing vault with `.obsidian-wiki` config or CWD-based setup |
| Hermes data | `~/.hermes/memories/` and optionally session transcripts |
| Python 3.7+ | For manifest and file processing |

## Configuration

The skill resolves configuration via a priority chain:

1. Inline `@name` override
2. Walk up CWD for `.env` file
3. `~/.obsidian-wiki/config`
4. Interactive prompt setup

Key config values:
- `OBSIDIAN_VAULT_PATH` — where the Obsidian wiki lives
- `HERMES_HISTORY_PATH` — defaults to `~/.hermes`

## Ingest Modes

### Append Mode (Default)

Checks `.manifest.json` at the vault root. Only processes:
- Files not in the manifest (new memories, new session logs)
- Files with modification time newer than `ingested_at`

Use for regular syncs.

### Full Mode

Processes everything regardless of manifest. Use after `wiki-rebuild` or for a fresh import.

## Data Sources

Ranked by knowledge value:

| Priority | Source | Content |
|:--------:|--------|---------|
| 1 (Highest) | `~/.hermes/memories/*.md` | Curated persistent agent knowledge |
| 2 | `~/.hermes/sessions/**/*.jsonl` | Structured turn-by-turn transcripts |
| 3 (Lowest) | `~/.hermes/config.yaml` | Metadata only (model prefs, paths) |

Skip: `.hub/` internals, `skills/` directory (source material, not user knowledge).

## Workflow

1. **Survey**: Scan `HERMES_HISTORY_PATH` and compare against `.manifest.json`
2. **Classify**: Mark each file as New, Modified, or Unchanged
3. **Extract**: Mine durable knowledge from new/modified files
4. **Distill**: Write to Obsidian wiki with proper links and tags
5. **Update**: Update `.manifest.json` with new `ingested_at` timestamps

## Verification

After running:
- Check `.manifest.json` for updated timestamps
- Verify new wiki pages in Obsidian vault
- Confirm no duplicate entries from previous runs

## Related Skills

- [Agent Memory Setup](/hermes/skills/catalog/agentmemory-setup/)
- [Memory Merger (GitHub Copilot)](/hermes/skills/catalog/awesome-copilot-setup/)
