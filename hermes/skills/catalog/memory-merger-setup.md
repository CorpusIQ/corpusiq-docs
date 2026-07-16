---
title: Memory Merger Setup — Agent Session Memory Consolidation
description: Install and configure GitHub's memory-merger skill from awesome-copilot — merge and consolidate agent session memories across restarts.
author: github/awesome-copilot
repo: https://github.com/github/awesome-copilot
stars: 36,652
---

# Memory Merger Setup Guide

**Source:** [github/awesome-copilot@memory-merger](https://skills.sh/github/awesome-copilot/memory-merger) (part of 36,652 ⭐ repo)
**Category:** Agent Infrastructure / Memory

Memory Merger is a community-contributed skill from GitHub's awesome-copilot repository that consolidates agent session memories. It merges fragmented memory entries from multiple sessions into a coherent, deduplicated knowledge base — preventing memory bloat and ensuring your agent's context stays clean and relevant.

---

## Quick Install

```bash
# Via skills.sh
npx skills add github/awesome-copilot@memory-merger

# Direct from GitHub
cd ~/.hermes/skills/
git clone https://github.com/github/awesome-copilot.git
# Then copy the memory-merger skill to your skills directory
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ |
| **Skills CLI** | `npx skills` must be available |
| **Existing memory** | Works best with agents that already have session memory (AgentMemory, Honcho, or native Hermes memory) |

---

## What It Does

Memory Merger addresses a common problem with long-running agents: **memory fragmentation**. After many sessions, your agent accumulates:

- Duplicate facts stored under slightly different phrasings
- Contradictory preferences from different sessions
- Stale entries that were relevant once but aren't anymore
- Scattered context spread across multiple memory backends

The Memory Merger skill:

1. **Scans** all active memory backends (Hermes native, AgentMemory, Honcho, file-based)
2. **Deduplicates** identical and near-identical entries
3. **Resolves conflicts** when different sessions stored contradictory facts
4. **Prunes stale entries** based on age and relevance heuristics
5. **Consolidates** into a single, clean knowledge base

---

## Usage

### Trigger Keywords

The skill activates when you mention:
- "merge my memories"
- "clean up agent memory"
- "deduplicate session context"
- "consolidate memory"

### Manual Invocation

```bash
# View memory stats before merging
hermes memory stats

# Run the memory merger
hermes skill run memory-merger --dry-run  # Preview changes
hermes skill run memory-merger --commit   # Apply changes
```

### Automated (Recommended)

Add to your Hermes profile for automatic memory maintenance:

```yaml
# ~/.hermes/profiles/corpusiq/config.yaml
memory:
  auto_merge: true
  merge_schedule: daily  # or weekly, on_session_end
  merge_threshold: 50    # merge when >50 duplicate entries detected
```

---

## What Gets Merged

| Memory Type | Merge Behavior |
|---|---|
| **User preferences** | Latest wins, old versions archived |
| **Codebase facts** | Merged — duplicates removed, contradictions flagged |
| **Session context** | Summarized — key decisions preserved, routine logs pruned |
| **Tool configurations** | Latest version kept, old configs archived with timestamp |
| **Error patterns** | Consolidated — same error from different sessions merged into one entry with occurrence count |

---

## Conflict Resolution

When Memory Merger finds contradictory entries (e.g., "User prefers tabs" vs "User prefers spaces"):

1. **Timestamp-based**: Newer entry wins by default
2. **Explicit markers**: Entries tagged `[DEFINITIVE]` override all others
3. **Flag for review**: Conflicts without clear resolution are surfaced for human review
4. **Context-weighted**: Entries from more recent sessions get higher weight

---

## Why This Matters

Agents that run for weeks accumulate massive context bloat:
- Duplicate facts waste context window space
- Stale preferences lead to wrong behavior
- Contradictory entries cause inconsistent decisions

Memory Merger keeps your agent's memory lean, accurate, and efficient — reducing context window waste by 30-60% in long-running deployments.

---

## Production Notes

- Part of GitHub's awesome-copilot repo (36K+ stars)
- Community-contributed, actively maintained
- Works across Hermes, Claude Code, Copilot, Cursor, and any MCP-based agent
- 12.6K installs on skills.sh

---

*← [MCP Use Setup](/hermes/skills/catalog/mcp-use-setup/) | [OpenClaw XHS Setup →](/hermes/skills/catalog/openclaw-xhs-setup/)*
*Powered by CorpusIQ*
