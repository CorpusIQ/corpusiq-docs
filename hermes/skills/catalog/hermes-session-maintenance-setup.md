---
title: Hermes Session Maintenance — Setup Guide
description: Zero-token monthly cleanup for Hermes Agent — close zombie sessions, prune old data, VACUUM state.db. Safe, cron-scheduled, with dry-run mode.
author: salt-vrn (Leonid Zolotarev, NeiroHost.ru)
repo: https://github.com/salt-vrn/hermes-session-maintenance
license: MIT
---

# Hermes Session Maintenance Setup

**Monthly cleanup script for Hermes Agent's `state.db`.** Closes zombie sessions, prunes old data, backs up the database, and reclaims disk space — all with zero tokens consumed by the agent.

## The Problem It Solves

Hermes Agent stores all sessions and messages in `state.db` (SQLite). Over time:

- **Zombie sessions** (never closed) leak memory and confuse the gateway
- **FTS5 indexes** grow with every message sent
- **SQLite never releases pages** without `VACUUM`
- **RAM usage climbs** as the gateway loads accumulated session data

Without maintenance, a production Hermes instance degrades silently.

## Quick Install

```bash
# Copy the script
mkdir -p ~/.hermes/scripts
curl -L https://raw.githubusercontent.com/salt-vrn/hermes-session-maintenance/main/scripts/session-maintenance.sh \
  -o ~/.hermes/scripts/session-maintenance.sh
chmod +x ~/.hermes/scripts/session-maintenance.sh

# Preview what would happen (safe, no changes)
bash ~/.hermes/scripts/session-maintenance.sh --dry-run

# Run for real
bash ~/.hermes/scripts/session-maintenance.sh
```

## What It Does

| Step | Action | Threshold |
|------|--------|-----------|
| 1 | Sanity check | Verify `started_at` is unix seconds |
| 2 | Close zombie sessions | `ended_at IS NULL` and older than 1 day |
| 3 | Prune ended sessions | Older than 7 days (messages + FTS cascade) |
| 4 | Backup state.db | Timestamped copy in `~/.hermes/backups/` (30-day retention) |
| 5 | VACUUM state.db | Reclaim disk space |

## Scheduling

### Hermes Cron
Ask the agent:
> "Create a monthly cron job to run session-maintenance.sh on the 1st at 04:00"

Or use `/cron create` with:
- **Schedule:** `0 4 1 * *`
- **Script:** `session-maintenance.sh`
- **no_agent:** `true` (no tokens consumed)
- **deliver:** `origin`

### Manual crontab
```bash
0 4 1 * * /bin/bash ~/.hermes/scripts/session-maintenance.sh
```

## Configuration

Edit the top of `session-maintenance.sh`:

```bash
DAYS_ZOMBIE=1    # Close sessions older than N days with no ended_at
DAYS_PRUNE=7     # Delete ended sessions older than N days
```

## Output Example

```
=== Session Maintenance Start ===
10:00:01 default: zombies=3 pruned=12 freed=45MB remaining=150 sessions, 8420 messages
10:00:05 frame: zombies=0 pruned=2 freed=8MB remaining=45 sessions, 2100 messages
=== Session Maintenance Done ===
```

## Safety Design

- **Active sessions** (< 1 day old) are **never touched**
- **`started_at` format** is verified before modifications (rejects ms timestamps, ISO dates)
- **`ended_at = started_at`** for zombies — no fabricated durations
- **Backup before VACUUM** with 30-day retention
- **`flock`** prevents parallel execution
- **Each profile processed independently** — one failure doesn't affect others
- **Reports before/after stats** for audit trail

## ⚠️ VACUUM and the Gateway

VACUUM requires an **exclusive lock** on the database. If the Hermes gateway is writing to `state.db`, VACUUM fails with `database is locked`.

**Safe approaches:**
- Schedule at 04:00 (low activity)
- Use `--dry-run` first
- If VACUUM fails — backup is safe, retry next month

## Requirements

- **Linux** (GNU grep with PCRE, `flock`, `du -b`)
- Hermes Agent installed
- Bash 4+
- Python 3 (for SQLite operations — comes with Hermes)

---

*← [Advanced Memory Setup](/hermes/skills/catalog/hermes-advanced-memory-setup/) | [Skill Cleaner Setup →](/hermes/skills/catalog/hermes-skill-cleaner-setup/)*
*Powered by CorpusIQ*
