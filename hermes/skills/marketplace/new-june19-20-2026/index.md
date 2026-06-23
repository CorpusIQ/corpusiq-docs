---
title: New Hermes Skills  --  June 19-20, 2026
description: 12 newly discovered Hermes Agent skills across 6 repos  --  Ponytail lazy-senior-dev, SkillSpector security vetting, AgentMint subagent routing, Herman's execution playbook, and 3 new aradotso/hermes-skills additions
---

# New Skills: June 19-20, 2026

**Discovered:** June 20, 2026 via GitHub API search + aradotso/hermes-skills commit tracking  
**New repos:** 6 | **New skills:** 12

---

## tensakulabs/hermes-ponytail (7 skills)

**"Makes your agent think like the laziest senior dev in the room."**

Ponytail repackaged for Hermes  --  pure `SKILL.md` skills with no code, no tools, no env. Hermes loads them on demand: when a task looks over-engineered, the model pulls the skill into context and builds the simplest thing that works.

| Skill | What it does | Install Command |
|-------|-------------|-----------------|
| `ponytail` | Lazy senior dev mode. YAGNI, stdlib first, no unrequested abstractions. | `hermes skills install tensakulabs/hermes-ponytail/ponytail --yes` |
| `ponytail-review` | Review a diff for over-engineering. One line per thing to delete. | `hermes skills install tensakulabs/hermes-ponytail/ponytail-review --yes` |
| `ponytail-audit` | Audit the whole repo for over-engineering. Ranked list of what to cut. | `hermes skills install tensakulabs/hermes-ponytail/ponytail-audit --yes` |
| `ponytail-debt` | Harvest every `ponytail:` shortcut comment into one tracked debt ledger. | `hermes skills install tensakulabs/hermes-ponytail/ponytail-debt --yes` |
| `ponytail-gain` | Scoreboard of Ponytail's measured impact (less code, less cost, more speed). | `hermes skills install tensakulabs/hermes-ponytail/ponytail-gain --yes` |
| `ponytail-help` | Quick reference for modes and skills. | `hermes skills install tensakulabs/hermes-ponytail/ponytail-help --yes` |

**Repo:** [tensakulabs/hermes-ponytail](https://github.com/tensakulabs/hermes-ponytail) | **Stars:** 0 | **Created:** June 20, 2026  
**Credit:** Behavior from [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (MIT)  
**Setup Guide:** [hermes-ponytail-setup.md](/hermes/skills/catalog/hermes-ponytail-setup/)

---

## SoCalStreet/skill-vetting (1 skill)

**Auto-vet external AI agent skills with NVIDIA SkillSpector before installation.**

Scan-before-install enforcement, 64 vulnerability patterns, risk gating (auto-proceed/approval/refuse), marketplace catalog (5 marketplaces mapped), weekly re-audit cron, JSONL audit trail.

| Skill | What it does | Install Command |
|-------|-------------|-----------------|
| `skill-vetting` | Pre-install security scan + catalog + weekly re-audit | `hermes skills install https://github.com/SoCalStreet/skill-vetting/SKILL.md` |

**Repo:** [SoCalStreet/skill-vetting](https://github.com/SoCalStreet/skill-vetting) | **Stars:** 0 | **Created:** June 19, 2026  
**Requires:** NVIDIA SkillSpector, Python 3.12+  
**Setup Guide:** [skill-vetting-setup.md](/hermes/skills/catalog/skill-vetting-setup/)

---

## mesutcelik/agentmint-skills (2 skills)

**Route Hermes `delegate_task` to persistent AgentMint subagents that remember across calls.**

| Skill | What it does | Install Command |
|-------|-------------|-----------------|
| `agentmint` | Universal AgentMint usage  --  wallet matrix, JSON-RPC methods, persona format | `hermes skills install mesutcelik/agentmint-skills/agentmint` |
| `hermes-delegate-task` | Route `delegate_task(background=True)` to named, persistent AgentMint subagent | `hermes skills install mesutcelik/agentmint-skills/hermes-delegate-task` |

**Repo:** [mesutcelik/agentmint-skills](https://github.com/mesutcelik/agentmint-skills) | **Stars:** 0 | **Created:** June 19, 2026  
**Related:** [mesutcelik/agentmint-hermes](https://github.com/mesutcelik/agentmint-hermes) (Python adapter on PyPI)  
**Setup Guide:** [agentmint-skills-setup.md](/hermes/skills/catalog/agentmint-skills-setup/)

---

## darraappen2/herman-skill-playbook (8 skills in 1 playbook)

**Execution skills by Herman (Hermes Agent)  --  GitHub installs, plugin management, DB ops, GDrive uploads, data analysis, memory management.**

| # | Skill | Description |
|---|-------|-------------|
| 1 | GitHub Install | Install skill/plugin dari GitHub |
| 2 | Plugin Install | Install platform adapter |
| 3 | Service Management | Start/poll/kill background process |
| 4 | Database Ops | DuckDB query, backup, import |
| 5 | API Config | Setup provider/model via hermes CLI |
| 6 | Data Analysis | Analisis divisi/bulan/dept/outlet pakai DuckDB |
| 7 | Memory Management | Simpan/update/hapus fakta cross-session |
| 8 | Upload GDrive | rclone copy/sync ke Google Drive |

**Repo:** [darraappen2/herman-skill-playbook](https://github.com/darraappen2/herman-skill-playbook) | **Stars:** 0 | **Created:** June 19, 2026  
**Install:** Copy `herman-skill-playbook.md` to `~/.hermes/` or load via `skill_view(name='herman-skill-playbook')`

---

## New aradotso/hermes-skills Additions (3 skills)

Discovered via commit tracking on aradotso/hermes-skills (June 18, 2026):

| Skill | Description | Source |
|-------|-------------|--------|
| `openclaw-polymarket-trading-bot` | OpenClaw trading bot for Polymarket prediction markets | Golrypavium/openclaw-polymarket-trading-bot (7 stars/day) |
| `openclaw-videotranslate-skill` | Video translation skill for OpenClaw | zbjincheng/openclaw-skill-videotranslate (0 stars) |
| `hermes-agentmesh-async-bus` | Async message bus for Hermes agent mesh networking | seleman66eeddwegger3-art/hermes-agentmesh (1 star/day) |

---

## Also Discovered (lower value)

These repos were found but not catalogued in detail  --  low star counts, minimal content, or duplicate existing skills:

| Repo | Description | Why skipped |
|------|-------------|-------------|
| Modichen/Hermesagent | "Skill list2" | README only, no actual skills |
| wilmerarredondozavala-jpg/odysseus-skills | 20 exported Hermes skills | Mostly duplicates of built-in Hermes skills (GitHub, Arxiv, Blogwatcher, etc.) |
| qq250113397-dotcom/skill-shell | Chinese skill manager UI | Desktop app, not Hermes skills |
| arshaka666/sad-nft-tools | NFT minting tools | Niche domain, not broadly applicable |
| AveryLemon/Hermes_V2 | Skills, config, memory, cron export | Personal config export, not a skill pack |

---

## Stats

- **Total new skills catalogued:** 12 (ponytail × 6 + skill-vetting × 1 + agentmint × 2 + playbook × 1 + aradotso × 3)
- **New repos:** 6 first-time discoveries
- **Setup guides drafted:** 3 (ponytail, skill-vetting, agentmint-skills)

---

*← [Marketplace Home](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
