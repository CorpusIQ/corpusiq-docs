---
title: Ghostwriter Setup Guide
description: Deploy autonomous email auto-reply for Hermes Agent — Watchdog (no-LLM polling) + Processor (agent drafting). ~10x cheaper than single-job polling
---

# Ghostwriter — Autonomous Email Auto-Reply

**Source:** [okokelly/skill-ghostwriter](https://github.com/okokelly/skill-ghostwriter)
**Stars:** 0 ⭐ | **License:** MIT
**Created:** June 23, 2026

## Overview

A two-tier autonomous email auto-reply system for Hermes Agent. Splits the work between a lightweight Python **Watchdog** (polls Gmail, no LLM, zero cost when idle) and a **Processor** agent (drafts + sends replies in your voice only when there's a matching email).

The key insight: polling Gmail with an LLM agent every 5 minutes burns ~$0.30/day even when there's nothing to do. Ghostwriter eliminates this — the LLM only runs on actual matches.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  GHOSTWRITER                         │
│                                                      │
│  ┌──────────┐    every 5min     ┌────────────────┐  │
│  │ Watchdog │ ─── no match ───▶ │ Silent ($0)    │  │
│  │  (script)│                   └────────────────┘  │
│  │          │                                       │
│  │          │ ─── match ──────▶ ┌────────────────┐  │
│  └──────────┘                   │ Processor      │  │
│                                 │  (agent)       │  │
│                                 │                │  │
│                                 │ 1. Read email  │  │
│                                 │ 2. Draft reply │  │
│                                 │ 3. Send        │  │
│                                 │ 4. Archive     │  │
│                                 └────────────────┘  │
└─────────────────────────────────────────────────────┘
```

## Prerequisites

- Hermes Agent with Google Workspace configured (`gws` CLI or Gmail API)
- Python 3.10+
- Gmail API credentials with `gmail.readonly`, `gmail.send`, `gmail.modify` scopes
- A "voice profile" — writing samples for the agent to match your tone

## Installation

```bash
git clone https://github.com/okokelly/skill-ghostwriter.git
cp -r skill-ghostwriter ~/.hermes/skills/ghostwriter/

# Verify Gmail API access
python3 ~/.hermes/skills/ghostwriter/scripts/watchdog.py --dry-run
```

## Configuration

### 1. VIP Inbox

Edit `~/.hermes/skills/ghostwriter/config.yaml`:

```yaml
inbox: vip@yourdomain.com
poll_interval: 300  # seconds (5 min)
filters:
  from:
    - "investor@*.com"
    - "partner@*.com"
  subject_contains:
    - "urgent"
    - "proposal"
  exclude:
    - "newsletter"
    - "notification"
```

### 2. Voice Profile

Create `~/.hermes/skills/ghostwriter/voice.md` with writing samples:

```markdown
# My Email Voice

## Signature style
- Short paragraphs, 2-3 sentences max
- Direct: "Let's do X" not "I was thinking we might want to consider X"
- Sign-off: "- FirstName"

## Example replies

### To investors
Subject: Re: Quick check-in

Hey [Name],

Good timing — we just shipped [feature] on Tuesday. Early metrics: [number].

Full update coming Friday. Want to grab 15 min before then?

- Me

### To partners
...
```

### 3. Cron Schedule

Add to crontab (runs every 5 minutes):

```bash
*/5 * * * * cd ~/.hermes/skills/ghostwriter && python3 scripts/watchdog.py >> /tmp/ghostwriter.log 2>&1
```

Or as a Hermes cron:

```bash
hermes cron create \
  --name ghostwriter-watchdog \
  --schedule "*/5 * * * *" \
  --command "cd ~/.hermes/skills/ghostwriter && python3 scripts/watchdog.py" \
  --profile corpusiq
```

## Capabilities

| Feature | Description |
|---------|-------------|
| **Token-efficient polling** | Watchdog uses Gmail API's `messages.list` with `q=` filters — no LLM, ~0 tokens when idle |
| **Voice matching** | Processor agent reads `voice.md` before drafting — replies match your tone |
| **Archive-after-send** | Processor archives handled emails, preventing duplicate replies |
| **Multi-inbox** | Config supports multiple VIP inboxes with different voice profiles |
| **Dry-run mode** | `--dry-run` flag previews replies without sending |
| **Processing log** | All actions logged to `/tmp/ghostwriter.log` for audit |

## CorpusIQ Use Cases

| Use Case | Configuration | Benefit |
|----------|--------------|---------|
| **Benefit Reply** | Filter: `from:founder@example.com` | Instant replies to founder, no manual monitoring |
| **Lead Response** | Filter: subject contains "CorpusIQ" or "demo" | Auto-respond to qualified leads within 5 min |
| **Partner Comms** | Filter: from partner domains | Fast partner replies without constant inbox checking |
| **Support Triage** | Filter: subject "urgent" or "down" | Immediate acknowledgment before human escalation |

## Cost Comparison

| Approach | Idle Cost/Day | Active Cost/Reply | Monthly (100 replies) |
|----------|:------------:|:-----------------:|:---------------------:|
| LLM polling every 5 min | ~$0.30 | ~$0.02 | ~$11 |
| Ghostwriter | **$0.00** | ~$0.02 | **~$2** |

~5.5x cheaper monthly. The savings compound with more VIP inboxes.

## Troubleshooting

### Watchdog exits silently on every poll

```bash
# Check Gmail API access
python3 scripts/watchdog.py --dry-run --verbose

# Expected output when no matches:
#   [2026-06-23 14:30:00] Polling... 0 matches. Silent.
```

### Processor drafts but doesn't send

Verify `gmail.send` scope in your Gmail API token:

```bash
python3 -c "
import json
with open('~/.hermes/secrets/gmail.json') as f:
    creds = json.load(f)
print(creds.get('scope', 'no scope field'))
# Should include: https://www.googleapis.com/auth/gmail.send
"
```

### Duplicate replies

The Processor archives emails after sending. If duplicates occur, check that `gmail.modify` scope is present and the archive step is not failing silently.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace Home](/hermes/skills/marketplace/) →*
