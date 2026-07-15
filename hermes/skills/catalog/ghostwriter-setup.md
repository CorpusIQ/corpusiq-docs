---
title: Ghostwriter — Full Setup Guide for Hermes Agents
description: Install and configure the Ghostwriter skill from okokelly/skill-ghostwriter. Autonomous email auto-reply pipeline with zero-token watchdog and voice-guided processor for VIP inboxes.
---

# Ghostwriter — Setup Guide

**Source:** [okokelly/skill-ghostwriter](#repo-unavailable)
**Category:** Email Automation

An autonomous email auto-reply pipeline for Hermes Agent. Two-job architecture: a zero-token Python watchdog checks Gmail, a processor agent drafts and sends replies in your voice. ~10x cheaper than single-job polling because the watchdog exits silently when there's nothing to process.

---

## Installation

```bash
# Clone the repo (preserves references)
git clone #repo-unavailable.git
mkdir -p ~/.hermes/skills/email
cp -a skill-ghostwriter/ghostwriter ~/.hermes/skills/email/
```

Then start a Hermes session and load:

```bash
hermes -s ghostwriter
```

Or inside Hermes:

```text
/skill ghostwriter
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Google Workspace Auth** | Gmail API access must be configured. Verify with: `GAPI="$HOME/.hermes/hermes-agent/venv/bin/python3 $HOME/.hermes/skills/productivity/google-workspace/scripts/gmail.py"` |
| **Hermes Agent** | v0.14.0+ for cron-based watchdog support |
| **Target Contact** | Email address of the VIP contact to auto-reply to |

---

## Key Capabilities

### Architecture

```
Watchdog (no_agent, script only)
  every 5min → checks Gmail for target emails
  ├─ Nothing found → exits silently (no stdout → no delivery → $0 cost)
  └─ Found → outputs email content → fed to Processor

Processor (agent, context_from=Watchdog)
  every 6min, offset by 1min → receives watchdog output as context
  ├─ No watchdog output → responds with "." (minimal tokens)
  └─ Email data present → reads, drafts reply, sends, archives
```

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| **VIP Inbox Monitoring** | "Set up auto-reply for [person]" | Watchdog polls Gmail every 5 minutes |
| **Voice-Guided Replies** | "Ghostwriter for [new contact]" | Processor drafts in your voice/style |
| **Silent Mode** | Automatic — no emails = zero tokens | Watchdog exits without output when nothing found |
| **Auto-Archive** | Built into processor | Sent replies are automatically archived |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **VIP Client Auto-Reply** | "Ghostwriter for client@example.com" — handles their emails autonomously |
| **Partner Communication** | Set up for integration partners who need quick responses |
| **Investor Updates** | Auto-respond to investor emails with status updates in your voice |
| **Support Triage** | Watchdog captures, processor drafts, human reviews before send |
| **After-Hours Coverage** | Run 24/7 — watchdog costs nothing when inbox is quiet |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| Watchdog not detecting emails | Verify Google Workspace auth: `GAPI=... gmail.py` |
| Processor sends no replies | Check cron offset — processor must run 1min after watchdog |
| High token usage | Verify watchdog exits silently on no-match (check cron output) |
| Wrong voice/style | Edit the voice prompt in `ghostwriter/SKILL.md` |

## Verification

```bash
# Verify skill loaded
hermes skills list | grep ghostwriter

# Test watchdog manually
cd ~/.hermes/skills/email/ghostwriter
python3 scripts/watchdog.py --dry-run
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-june23-2026/) →*
*Powered by CorpusIQ*
