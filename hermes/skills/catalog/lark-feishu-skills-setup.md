---
title: Lark & Feishu Skills — Office Suite Automation Setup Guide for Hermes Agents
description: Install the official Lark/Feishu office suite skills — open.feishu.cn (28 skills, 14.8M installs) and larksuite/cli (32 skills, 10.2M installs). Docs, Base, Sheets, IM, Wiki, Calendar, Mail, Meetings, OKR and more, agent-native.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/lark-feishu-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Lark & Feishu Skills — Setup Guide

**Source:** [open.feishu.cn](https://www.skills.sh/site/open.feishu.cn) (28 skills · 14.8M combined installs) and [larksuite/cli](https://www.skills.sh/larksuite/cli) (32 skills · 10.2M combined installs)
**GitHub:** [github.com/larksuite/cli](https://github.com/larksuite/cli)
**Category:** Platform Integrations / Office Suite
**First Seen:** August 12, 2026
**Quality Tier:** 🟢 Production (official Feishu/Lark platform publishers)

Lark — Feishu's international brand — publishes two official listings on skills.sh covering the entire Lark office suite. Every surface is agent-native: Docs, Base (the database builder), Sheets, Drive, IM (messaging), Wiki, Calendar, Mail, Tasks, video Meetings, Approvals, Slides, Attendance, OKR, and Markdown rendering, plus open-platform API tooling. Together these two listings are the largest office-suite skill cluster on skills.sh (~25M listed installs).

---

## Installation

```bash
# Install the full official CLI repo (GitHub-backed, 32 skills)
npx skills add larksuite/cli

# Or install individual skills
npx skills add larksuite/cli --skill lark-doc
npx skills add larksuite/cli --skill lark-base
npx skills add larksuite/cli --skill lark-im
npx skills add larksuite/cli --skill lark-wiki
npx skills add larksuite/cli --skill lark-sheets
```

The `open.feishu.cn` listing mirrors the same skill set as a site registry (no GitHub repo required) — use it as a fallback when the CLI repo install is blocked.

---

## Core Skills

| Skill | Installs (cli repo) | Use For |
|---|---|---|
| `lark-doc` | 411.3K | Create, edit, and query Docs |
| `lark-base` | 409.7K | Database records, tables, views, automation |
| `lark-sheets` | 406.9K | Spreadsheet reads, writes, formulas |
| `lark-im` | 408.3K | Send/receive messages, group chats, bots |
| `lark-wiki` | 407.1K | Knowledge base pages and spaces |
| `lark-drive` | 408.4K | File storage, folders, sharing |
| `lark-calendar` | 405.7K | Events, scheduling, availability |
| `lark-mail` | 404.6K | Mailbox operations |
| `lark-task` | 406.2K | Task lists and assignments |
| `lark-vc` / `lark-vc-agent` | 404.4K / 292.5K | Meeting rooms and meeting agents |
| `lark-minutes` | 404.5K | Meeting minutes generation |
| `lark-approval` | 377.6K | Approval flows |
| `lark-okr` | 341.5K | OKR tracking |
| `lark-workflow-meeting-summary` | 403.5K | Automated meeting summaries |
| `lark-workflow-standup-report` | 402.9K | Automated standup reports |
| `lark-openapi-explorer` | 402.7K | Explore and call the open API |
| `lark-skill-maker` | 402.5K | Scaffold new Lark skills |

Also included: `lark-shared`, `lark-whiteboard`, `lark-event`, `lark-contact`, `lark-slides`, `lark-attendance`, `lark-markdown`, `lark-note`, `lark-apps`, `lark-whiteboard-cli`, plus test/dev utilities.

---

## Prerequisites

| Requirement | Details |
|---|---|
| Lark / Feishu account | Free tier works for most skills |
| Developer app credentials | `app_id` + `app_secret` from the [Feishu open platform](https://open.feishu.cn/) for API-backed skills |
| Bot permissions | Scope grants for the surfaces you use (docs, base, im, etc.) |
| Node.js + npx | For the skills.sh CLI install path |

API-backed skills read credentials from the environment (`LARK_APP_ID` / `LARK_APP_SECRET` or an equivalent config file); check each skill's SKILL.md for the exact variable names.

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Operator SOP automation** | `lark-base` + `lark-doc` to read/write runbooks and tracking tables |
| **Meeting ops** | `lark-workflow-meeting-summary` and `lark-workflow-standup-report` automate recurring team rituals |
| **IM-triggered agents** | `lark-im` as an inbound channel for agent workflows alongside Telegram/Discord |
| **OKR cadence** | `lark-okr` for quarterly tracking from an agent |
| **Feishu-first orgs** | Complements the existing Clawdbot Feishu setup for mixed-agent deployments |

---

## Limitations / Verification

- Two listings publish near-identical skill sets — the GitHub-backed `larksuite/cli` is the primary install path; the site listing is a mirror
- Verify install: `npx skills list | grep lark-` should show the installed skills
- API-backed skills require a developer app; IM/bot skills need scopes approved before first call

---

## Related

- [Clawdbot Feishu Setup](/hermes/skills/catalog/clawdbot-feishu-setup/)
- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
