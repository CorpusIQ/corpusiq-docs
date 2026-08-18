---
title: "New Skills — July 30, 2026 - CorpusIQ Docs"
description: 11 newly discovered Hermes Agent skills from skills.sh marketplace sweep — including HTML/Cyber Terminal presentations, X/Twitter automation, agent dashboard, and Telegram setup guides.
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-july30-2026/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "skill marketplace", "skills.sh"]

---

# New Skills — July 30, 2026

**Source:** [skills.sh](https://skills.sh) via REST API multi-query sweep
**Date:** July 30, 2026
**Total new this batch:** 11 skills
**Total skills.sh in sweep:** 204 (across 5 queries)

Routine daily sweep of the skills.sh marketplace across 5 queries (`nousresearch/hermes-agent`, `aradotso/hermes-skills`, `hermes agent`, `hermes skill`, `hermes automation`). After cross-referencing against the existing 185 documented skills in `hermes/skills/`, 19 were flagged as new. 8 were filtered out as OpenClaw-specific (polymarket-openclaw-*, loader-openclaw, openclaw-windows-*, moontv-openclaw) — leaving 11 genuinely new Hermes Agent skills.

---

## Creative & Design (1 skill)

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 1 | `html-ppt-hermes-cyber-terminal` | 192 | Cyber-terminal themed HTML/PPT presentation skill from the 82.7K⭐ nexu-io/open-design repo. Generates slide decks and terminal-styled presentations via Hermes Agent. |

**Source:** `nexu-io/open-design` (82,734 ⭐) — the open-source Claude Design alternative. Local-first desktop app. Coding agents become the design engine for prototypes, landing pages, dashboards, slides.

---

## Social Media & Automation (2 skills)

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 2 | `twitter-gtm-find-skill` | 13 | End-to-end pipeline for scraping X/Twitter for GTM/DevRel tech startup jobs using Apify, or optionally TweetClaw for OpenClaw and Hermes Tweet for Hermes Agent. |
| 3 | `x-twitter-automation` | 10 | Design safe X/Twitter automation workflows for tweet search, reply reads, monitoring, posting, and agent-operated social media actions. |

**Sources:** `varnan-tech/opendirectory`, `cosmicstack-labs/mercury-agent-skills`

---

## Agent Infrastructure & Dashboards (2 skills)

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 4 | `hermes-studio-dashboard` | 38 | Web dashboard for Hermes Agent with multi-platform AI chat, session management, scheduled jobs, and usage analytics. |
| 5 | `agentiko-hermes` | 16 | Hermes Agent features guide — cron, delegation, memory, automation, YOLO mode, dual-agent hunting, and slash commands for the agentiko Telegram setup. |

**Sources:** `aradotso/hermes-skills`, `uphiago/recon-skills`

---

## Niche & Emerging (6 skills)

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 6 | `hermes-agent-v2` | 14 | Hermes Agent skill from skills.volces.com ecosystem. |
| 7 | `hermes-worker-qxun` | 5 | Hermes worker skill from `andy304yang/codex`. |
| 8 | `hermes-code-bridge` | 3 | Code bridging skill from `xuyang-liu16/hermes-code-bridge`. |
| 9 | `hermes-usage` | 1 | Hermes usage tracking from `abdwhb-png/agent-tools`. |
| 10 | `hermes-pr-workflow` | 1 | PR workflow skill from `powerfulmoves/pmoves.ai`. |
| 11 | `hermes-network` | 1 | Network skill from `schin-300/hermes-skills`. |

---

## Installation

```bash
npx skills add nousresearch/hermes-agent
# or for skills from other publishers:
npx skills add https://github.com/nexu-io/open-design --skill html-ppt-hermes-cyber-terminal
npx skills add https://github.com/cosmicstack-labs/mercury-agent-skills --skill x-twitter-automation
```

## Notable

- **html-ppt-hermes-cyber-terminal** is the standout this sweep — 192 installs from an 82.7K⭐ design repo. Great for Hermes agents that need to generate presentations or terminal-themed slide decks.
- **x-twitter-automation** and **twitter-gtm-find-skill** fill social media automation gaps — useful for CorpusIQ growth agents doing organic social mining.
- **hermes-studio-dashboard** provides a web-based Hermes management UI.
- **agentiko-hermes** documents Hermes Agent features for Telegram-based setups — directly relevant to our Telegram Topic 2 operations.

## Next Steps

- See the [full skills catalog](/hermes/skills/catalog/) for setup guides
- See [skill marketplaces](/hermes/skills/skill-marketplaces/) for discovery and publishing
