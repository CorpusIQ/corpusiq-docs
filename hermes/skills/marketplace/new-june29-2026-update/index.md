---
title: "June 29, 2026 (Update) — OpenClaw/Clawd Ecosystem"
description: "June 29, 2026 update: 25 new skills discovered across 9 OpenClaw/Clawd ecosystem repos — clawdis (14 skills), clawdirect (2), clawdstrike (1), plus security, backup, and integrations."
---

# 🆕 June 29, 2026 (Update) — 25 New OpenClaw/Clawd Ecosystem Skills

**Date:** June 29, 2026
**Source:** skills.sh API multi-term sweep (14 search queries, 205 skills scanned)
**New Repos:** 9 | **New Skills:** 25 | **Total Installs:** 43K+

A broad API sweep across the OpenClaw/Clawd ecosystem surfaced 25 previously uncatalogued skills. The biggest find: **steipete/clawdis** — 14 high-install terminal, media, monitoring, and productivity skills (2.4K–5K installs each). These complement the existing Hermes/OpenClaw ecosystem with specialized CLI wrappers, session management, and hardware integrations.

*See [June 29 primary discovery](/hermes/skills/marketplace/new-june29-2026/) for 7 independently sourced skills (coding-posture, ultimate-humanizer, etc.). This update covers the API sweep findings.*

---

## New Skills at a Glance

| # | Repo | Skills | Top Install | Category |
|---|------|--------|:-----------:|----------|
| 1 | **steipete/clawdis** | 14 | 4,964 | Terminal, Media, Monitoring, Productivity |
| 2 | **napoleond/clawdirect** | 2 | 4,617 | Agent Directing |
| 3 | **zackkorman/skills** | 1 | 357 | Security |
| 4 | **cantinaxyz/clawdstrike** | 1 | 486 | Red Team |
| 5 | **sundial-org/awesome-openclaw-skills** | 2 | 233 | Backup, Cost Tracking |
| 6 | **thesethrose/clawdbot-security-check** | 1 | 24 | Security Audit |
| 7 | **clawdbot-skills/task-decomposer** | 1 | 55 | Task Decomposition |
| 8 | **romanescu11/hermes-skill-factory** | 1 | 109 | Skill Authoring |
| 9 | **aradotso/hermes-skills** | 2 | 30 | Wallet, AI Integrations |

---

## Repo 1: steipete/clawdis — 14 Skills (37K+ Installs)

The largest single-repo discovery. Clawdis is a curated collection of Hermes/OpenClaw skills by [@steipete](https://github.com/steipete) that wrap popular CLI tools, media utilities, and monitoring systems as agent-callable skills.

**Total skills:** 14 | **Total installs:** ~37,000

| Skill | Installs | Description |
|-------|:--------:|-------------|
| **tmux** | 4,964 | Terminal multiplexer — agent controls tmux sessions, windows, and panes |
| **openai-whisper** | 3,781 | Speech-to-text — transcribe audio files via OpenAI Whisper |
| **ordercli** | 3,388 | Order/shopping CLI — agent can place orders via command line |
| **peekaboo** | 3,112 | Screen capture utility — take screenshots for visual context |
| **himalaya** | 2,907 | Email CLI — send/receive/manage emails from terminal |
| **clawhub** | 2,859 | Central skill hub — discover and install skills from the ecosystem |
| **video-frames** | 2,762 | Extract and analyze individual video frames |
| **session-logs** | 2,616 | Session logging and history search for agent conversations |
| **healthcheck** | 2,594 | System health monitoring — CPU, memory, disk, processes |
| **trello** | 2,578 | Trello board management — create cards, move lists, comment |
| **model-usage** | 2,458 | Track and report LLM model usage and token costs |
| **sonoscli** | 2,457 | Sonos speaker control — play, pause, volume, queue management |
| **blogwatcher** | 2,451 | RSS/Atom feed monitoring — watch blogs for new content |
| **spotify-player** | 2,438 | Spotify playback control — search, play, queue, playlists |

```bash
# Install individual skills from clawdis
npx skills add steipete/clawdis/tmux
npx skills add steipete/clawdis/openai-whisper
# ... or browse all: https://skills.sh/steipete/clawdis
```

---

## Repo 2: napoleond/clawdirect — 2 Skills (9,119 Installs)

A specialized agent-directing framework that gives Hermes agents the ability to self-direct work through a structured command interface.

| Skill | Installs | Description |
|-------|:--------:|-------------|
| **clawdirect** | 4,617 | Core agent directing — structured task execution, work trees, directives |
| **clawdirect-dev** | 4,502 | Development mode — extended directives for coding, testing, deployment |

```bash
npx skills add napoleond/clawdirect/clawdirect
npx skills add napoleond/clawdirect/clawdirect-dev
```

---

## Repo 3: zackkorman/skills — 1 Skill (357 Installs)

| Skill | Installs | Description |
|-------|:--------:|-------------|
| **openclaw-admin-security-breakglass** | 357 | Emergency admin access with audit trail — break-glass procedures for agent admin |

```bash
npx skills add zackkorman/skills/openclaw-admin-security-breakglass
```

---

## Repo 4: cantinaxyz/clawdstrike — 1 Skill (486 Installs)

| Skill | Installs | Description |
|-------|:--------:|-------------|
| **clawdstrike** | 486 | Red-team security testing — automated vulnerability scanning for agent deployments |

```bash
npx skills add cantinaxyz/clawdstrike/clawdstrike
```

---

## Repo 5: sundial-org/awesome-openclaw-skills — 2 Skills (269 Installs)

| Skill | Installs | Description |
|-------|:--------:|-------------|
| **clawdbot-backup** | 233 | Automated backup of agent configurations, skills, and session data |
| **clawdbot-cost-tracker** | 36 | Track and report agent operational costs across providers |

```bash
npx skills add sundial-org/awesome-openclaw-skills/clawdbot-backup
npx skills add sundial-org/awesome-openclaw-skills/clawdbot-cost-tracker
```

---

## Repo 6: thesethrose/clawdbot-security-check — 1 Skill (24 Installs)

| Skill | Installs | Description |
|-------|:--------:|-------------|
| **clawdbot-self-security-audit** | 24 | Agent self-audits its own security posture — permissions, tokens, access scope |

```bash
npx skills add thesethrose/clawdbot-security-check/clawdbot-self-security-audit
```

---

## Repo 7: clawdbot-skills/task-decomposer — 1 Skill (55 Installs)

| Skill | Installs | Description |
|-------|:--------:|-------------|
| **super-skills** | 55 | Hierarchical task decomposition — break complex goals into sub-tasks |

```bash
npx skills add clawdbot-skills/task-decomposer/super-skills
```

---

## Repo 8: romanescu11/hermes-skill-factory — 1 Skill (109 Installs)

| Skill | Installs | Description |
|-------|:--------:|-------------|
| **skill factory** | 109 | Programmatic skill generation — create new skills from templates with validation |

```bash
npx skills add romanescu11/hermes-skill-factory/skill-factory
```

---

## Repo 9: aradotso/hermes-skills — 2 Skills (58 Installs)

| Skill | Installs | Description |
|-------|:--------:|-------------|
| **metamask-openclaw-wallet-integration** | 30 | MetaMask wallet integration — agent can interact with Web3 wallets |
| **deepseek-openclaw-integration** | 28 | DeepSeek model integration for OpenClaw — use DeepSeek as agent backend |

```bash
npx skills add aradotso/hermes-skills/metamask-openclaw-wallet-integration
npx skills add aradotso/hermes-skills/deepseek-openclaw-integration
```

---

## Summary

| Category | Count | Top Install |
|----------|:-----:|:-----------:|
| Terminal & CLI | 4 | 4,964 (tmux) |
| Media & Audio | 4 | 3,781 (openai-whisper) |
| Monitoring & Logging | 4 | 2,616 (session-logs) |
| Productivity | 3 | 2,578 (trello) |
| Agent Infrastructure | 4 | 4,617 (clawdirect) |
| Security | 3 | 486 (clawdstrike) |
| Integrations | 3 | 30 (metamask) |

**Total new skills: 25 | Total installs: 43,057 | Repos: 9**

---

*← [June 29 Primary Discovery](/hermes/skills/marketplace/new-june29-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*

*↑ [Skills Overview](/hermes/skills/)*
