---
title: New Skills — June 19, 2026 Batch 2 (15 repos, 20+ skills)
description: Second June 19 sweep — 15 new repos including workspace memory management, session maintenance, skill auditing, MAX Bot bridge, GitHub launch pipeline, agent apprenticeship, and Feishu rendering patches.
---

# New Skills — June 19, 2026 (Batch 2)

**Sources:** GitHub Search API (hermes-agent + openclaw topics)
**Date:** June 19, 2026 (evening sweep)
**Total new:** 15 repos (20+ skills/tools)

Evening sweep uncovered 15 brand-new repositories across the Hermes and OpenClaw ecosystems — infrastructure skills, developer tools, platform integrations, and agent learning frameworks. Highlights include workspace memory management from NeiroHost, a skill auditor from FavorPan, MAX Bot API bridge and native plugin, a parallel GitHub launch pipeline, and the Agent Apprenticeship learning ecosystem.

---

## Category 1: Agent Infrastructure & Operations (5 repos)

| # | Repo | Skills/Tool | Description |
|---|------|-------------|-------------|
| 1 | `salt-vrn/hermes-advanced-memory` | 1 skill | Workspace rules + memory management — enforces `AGENTS.md` index, project folders, `SOUL.md` principles |
| 2 | `salt-vrn/hermes-session-maintenance` | 1 script | Zero-token monthly cleanup — close zombie sessions, prune old data, VACUUM state.db |
| 3 | `salt-vrn/openclaw-to-hermes-migration` | 1 skill | Guided 10-phase migration from OpenClaw to Hermes Agent |
| 4 | `FavorPan/hermes-skill-cleaner` | 1 CLI | Zero-dependency TypeScript skill auditor — token budget, duplicates, unused skills, description bloat |
| 5 | `mmansillaf/hermes-skills` | 2 skills | Token optimization + context engineering for Hermes Agent |

---

## Category 2: Hermes Platform Integrations (3 repos)

| # | Repo | Description |
|---|------|-------------|
| 6 | `RuslanStrogov/max-hermes` | Python bridge: MAX Bot API ↔ Hermes Agent via webhook, Docker, systemd |
| 7 | `RuslanStrogov/max-hermes-plugin` | Native Hermes Gateway plugin for MAX Bot — direct integration, no external bridge |
| 8 | `Handsome-KK/Hermes-personal-stack` | Personal AI assistant: multi-backend search, Feishu table rendering patch, brief publishing pipeline, macOS launchd |

---

## Category 3: Developer Tools & Pipelines (2 repos)

| # | Repo | Description |
|---|------|-------------|
| 9 | `Rishiidev/hermes-github-launch` | Full GitHub launch in ~4–6 min via 3 parallel delegated subagents per phase — SEO naming, competitor research, social preview SVG, GitHub Pages, v1.0.0 release, 7-day distribution calendar |
| 10 | `Forsy-AI/agent-apprenticeship` | Agent learning ecosystem — 500+ seed tasks, mentor modes, experience packs, contribution bundles. Supports Hermes, Codex, Claude Code, OpenClaw, Cursor |

---

## Category 4: Experimental & Specialized (5 repos)

| # | Repo | Description |
|---|------|-------------|
| 11 | `ducanhao081-tech/hermos-optimization-layer` | Governed self-evolution layer — typed memory, domain isolation, completion gates (v0.3.2-alpha) |
| 12 | `kyzqdcs1968-dcs/hermes-skill-local-ocr` | Offline OCR for Chinese legal documents via macOS Vision framework |
| 13 | `csmoove530/hermes-eigen-prototype` | Wallet-controlled Hermes agent command plane for EigenCompute TEEs |
| 14 | `thenotoriousmrkrabs/opencli-plugin-fb-autopost` | Local-first Facebook group posting plugin with dry-run safety |
| 15 | `SmokerGreenOG/ToolCase` | 43 tools across 10 categories for OpenCLI — 100% RSI quality score |

---

## Spotlight: Workspace Memory Management (salt-vrn trilogy)

**Author:** Leonid Zolotarev ([salt-vrn](https://github.com/salt-vrn))
**Project:** [NeiroHost.ru](https://neirohost.ru/) — AI-agent hosting powered by Hermes and OpenClaw

Three complementary tools that solve agent memory chaos:

### hermes-advanced-memory
Enforces structured workspace — `AGENTS.md` index loaded every session, project folders with READMEs, `SOUL.md` for persistent principles. Transforms scattered agent files into an organized, navigable memory system.

```
~/.hermes/
├── SOUL.md              ← identity + rules
├── workspace/
│   ├── AGENTS.md        ← index (loaded every session)
│   ├── project-alpha/
│   └── project-beta/
```

### hermes-session-maintenance
Monthly cron script that closes zombie sessions, prunes old data (7-day threshold), backs up `state.db`, and runs `VACUUM` to reclaim disk space. Safe by design — never touches active sessions, verifies timestamps, uses `flock` to prevent parallel execution.

### openclaw-to-hermes-migration
Structured 10-phase migration for agents moving from OpenClaw to Hermes. Unlike a script, this skill adapts to each unique OpenClaw setup — analyzing files, planning transfer, migrating cron/secrets/files/config, and reporting what requires manual intervention.

---

## Spotlight: Skill Auditor (hermes-skill-cleaner)

**Author:** [FavorPan](https://github.com/FavorPan)

A zero-dependency TypeScript CLI that scans `~/.hermes/skills/` to:
- **Budget Analysis** — calculates what % of your 2% skill budget is consumed
- **Duplicate Detection** — finds identical skills by name, body hash, and Jaccard similarity
- **Usage Scanning** — parses session JSONL logs to find actually-used vs unused skills
- **Description Compression** — identifies bloated descriptions with compact alternatives

```bash
node --experimental-strip-types scripts/hermes-skill-cleaner.ts --no-logs
```

Three-phase cleanup workflow: remove duplicates → remove unused → compress descriptions.

---

## Spotlight: MAX Bot Platform (RuslanStrogov)

**Author:** [RuslanStrogov](https://github.com/RuslanStrogov)
**Design:** [BR-DESIGN](https://br-design.ru/)

Two options for connecting Hermes Agent to the MAX messenger platform:

### max-hermes (Bridge)
Standalone FastAPI bridge — receives webhooks from MAX Bot API, forwards to Hermes CLI, returns responses. Docker + systemd support. Feature-complete: typing indicators, inline keyboards, attachments, multi-user, group chats.

### max-hermes-plugin (Native)
Hermes Gateway plugin — install directly into `~/.hermes/plugins/platforms/max/`. No external process, no bridge. Requires legal entity/ИП/self-employed for MAX bot creation.

---

## Spotlight: Parallel GitHub Launch (Rishiidev)

A Hermes-native evolution of `github-launch-agent`. One trigger (`github launch`) spawns 3 parallel delegated subagents per phase, cutting launch from 20+ minutes to ~4–6 minutes. Includes:
- SEO name scoring (5 candidates ranked)
- Competitor README research
- Auto-embedded social preview SVG
- GitHub Pages + CI workflows
- v1.0.0 release + 20 topics
- 7-day distribution calendar
- IMPROVE mode for existing repos (6 parallel audit agents)

---

## Installation

```bash
# Workspace memory management
hermes skill install salt-vrn/hermes-advanced-memory

# Session maintenance script
mkdir -p ~/.hermes/scripts
curl -L https://raw.githubusercontent.com/salt-vrn/hermes-session-maintenance/main/scripts/session-maintenance.sh \
  -o ~/.hermes/scripts/session-maintenance.sh
chmod +x ~/.hermes/scripts/session-maintenance.sh

# OpenClaw → Hermes migration
hermes skill install salt-vrn/openclaw-to-hermes-migration

# Skill auditor (requires Node.js 22+)
git clone https://github.com/FavorPan/hermes-skill-cleaner.git
cd hermes-skill-cleaner
node --experimental-strip-types scripts/hermes-skill-cleaner.ts --no-logs

# GitHub launch pipeline
mkdir -p ~/.hermes/skills/hermes-github-launch
curl -L https://github.com/Rishiidev/hermes-github-launch/releases/latest/download/hermes-github-launch.skill \
  -o ~/.hermes/skills/hermes-github-launch/SKILL.md

# MAX Bot bridge
git clone https://github.com/RuslanStrogov/max-hermes.git
cd max-hermes && python3 -m venv venv && pip install -r requirements.txt

# MAX Bot native plugin
git clone https://github.com/RuslanStrogov/max-hermes-plugin.git \
  ~/.hermes/plugins/platforms/max
hermes gateway restart

# Agent Apprenticeship
npm install -g agent-apprenticeship
apprentice init

# Token optimization skills
hermes skills install https://raw.githubusercontent.com/mmansillaf/hermes-skills/main/skills/software-development/token-optimization.md
hermes skills install https://raw.githubusercontent.com/mmansillaf/hermes-skills/main/skills/software-development/context-engineering.md

# Local OCR (macOS only)
git clone https://github.com/kyzqdcs1968-dcs/hermes-skill-local-ocr.git \
  ~/.hermes/skills/hermes-skill-local-ocr
```

---

## Setup Guides

New setup guides added for:
- [Hermes Advanced Memory →](/hermes/skills/catalog/hermes-advanced-memory-setup/)
- [Hermes Session Maintenance →](/hermes/skills/catalog/hermes-session-maintenance-setup/)
- [Hermes Skill Cleaner →](/hermes/skills/catalog/hermes-skill-cleaner-setup/)

---

## Why This Matters

1. **Memory infrastructure maturing** — The salt-vrn trilogy (advanced-memory, session-maintenance, migration) is the first cohesive infrastructure package for production Hermes deployments. NeiroHost is building real hosting infrastructure around these tools.

2. **Skill hygiene becomes tractable** — `hermes-skill-cleaner` is the first dedicated tool for analyzing skill token budgets, finding duplicates, and identifying unused skills. Critical as the ecosystem grows past 380+ skills.

3. **Platform expansion continues** — MAX Bot API integration (bridge + native plugin) opens Hermes to the Russian messenger market. Feishu rendering patches from the personal-stack repo are upstream-quality candidates.

4. **Agent-to-agent learning emerges** — `agent-apprenticeship` is a genuinely new category: an open infrastructure for agents to learn from each other's work. 500+ seed tasks, mentor modes, contribution bundles.

5. **GitHub launch goes parallel** — Rishiidev's skill uses Hermes's `delegate_task(tasks=[...])` to run 3 agents concurrently per phase, cutting launch time by 70%+.

---

## Catalog Updates

- **Marketplace index:** Updated with this page
- **Ecosystem page:** Added 15 repos
- **Setup guides:** 3 new guides (advanced-memory, session-maintenance, skill-cleaner)
- **Total documented marketplace repos:** 340 + 15 = 355+

---

*← [Skills Marketplace](/hermes/skills/marketplace/) | [June 19 Batch 1](/hermes/skills/marketplace/new-june19-2026/) →*
*↑ [Skills Catalog Home](/hermes/skills/catalog/)*
*Powered by CorpusIQ*
