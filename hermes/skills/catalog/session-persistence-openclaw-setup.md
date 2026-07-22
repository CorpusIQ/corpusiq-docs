---
title: Session Persistence (OpenClaw) — SQLite message history for Hermes Agent memory
description: Import session transcripts into SQLite with FTS5 full-text search — agent never loses messages across compaction or rollover. 28+ installs from archieindian/openclaw-superpowers.
---

# Session Persistence (OpenClaw) — Setup Guide

**Source:** [archieindian/openclaw-superpowers](https://skills.sh/archieindian/openclaw-superpowers/session-persistence) (28+ installs)
**Category:** Engineering / Memory & Persistence
**Quality Tier:** 🔵 Community

Imports agent session transcripts into a local SQLite database with FTS5 full-text search, ensuring the agent never loses message history — even after context compaction or session rollover. Automatically runs every 15 minutes via cron for incremental import.

---

## Installation

```bash
npx skills add archieindian/openclaw-superpowers --skill session-persistence
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python 3** | Built-in `sqlite3` module — no external dependencies |
| **OpenClaw sessions** | JSONL session files to import from |
| **Disk space** | Varies with session volume — SQLite database at `~/.openclaw/lcm-db/messages.db` |

---

## Key Capabilities

### Automatic Incremental Import
Runs every 15 minutes via cron. Scans session directory for new JSONL files, tracks per-conversation sequence numbers to skip already-imported messages, and updates FTS5 index incrementally.

### FTS5 Full-Text Search
Search across all sessions, all channels, all time. Filter by role (user/assistant), date range, or conversation ID. Returns ranked results with conversation context.

### Conversation Dump & Export
Dump full conversations by ID, export back to JSONL format, or get database statistics (total messages, conversations, date ranges, activity patterns).

### Integration with Memory Systems
Feeds into `memory-dag-compactor`, `dag-recall`, and `context-assembly-scorer` for enhanced agent memory and recall.

---

## Quick Start

```bash
# Initial import of all existing sessions
python3 persist.py --import

# Search history
python3 persist.py --search "auth migration"

# Search only user messages
python3 persist.py --search "deploy" --role user

# Recent messages (last 24 hours)
python3 persist.py --recent --hours 24

# Database statistics
python3 persist.py --stats

# Export back to JSONL
python3 persist.py --export --format jsonl

# Last import summary
python3 persist.py --status
```

---

## Verification

```bash
# Check skill installed
npx skills list | grep session-persistence

# Verify database exists
ls ~/.openclaw/lcm-db/messages.db

# Check import status
python3 persist.py --status
```

---

## Notes

- Uses Python's built-in `sqlite3` — zero external dependencies
- FTS5 full-text search for ranked results across all time periods
- Idempotent: safe to re-run, tracks per-conversation sequence numbers
- Import lag: up to 15 minutes (cron interval)
- Database is local-only — never committed to repository
- Inspired by [lossless-claw](https://github.com/Martian-Engineering/lossless-claw)'s SQLite message persistence layer
- State file at `~/.openclaw/skill-state/session-persistence/state.yaml`
- Quality tier 🔵 Community: 28 installs, focused and well-implemented
