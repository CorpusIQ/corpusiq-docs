---
title: New Hermes Skills — June 23, 2026
description: 15 new Hermes Agent repos discovered June 23, 2026 — Engineering Curation (104 skills, 10 profiles), Ghostwriter autonomous email, Cron Design Workflow, Machinations game economy, StepFun Chinese LLM, and 10 more
---

# New Skills: June 23, 2026

**Discovered:** June 23, 2026 via GitHub API + skills.sh API
**New repos:** 15 | **Net-new (uncatalogued):** 8 substantive
**Date range:** June 22-23, 2026

A productive Tuesday morning sweep. Two standout finds: a professionally-curated engineering workflow catalog (336 scanned, 104 selected, 10 profiles) and an autonomous email auto-reply system that's directly relevant to CorpusIQ operations. Also surfaced the first Chinese LLM provider skill for Hermes (StepFun/阶跃星辰) and a reusable cron design workflow.

---

## ⭐ Standout Finds (4)

| # | Repo | Stars | Description |
|---|------|:-----:|-------------|
| 1 | `Fahrnetic/hermes-engineering-skill-curation` | 1 ⭐ | Professional engineering workflow catalog — 336 skills scanned, 104 curated, 10 operator profiles, gate matrix, public readiness audit |
| 2 | `okokelly/skill-ghostwriter` | 0 ⭐ | Autonomous email auto-reply — Watchdog (no-LLM polling) + Processor (agent drafting). ~10x cheaper than single-job polling |
| 3 | `lovenps85/hermes-cron-design-workflow-skill` | 0 ⭐ | Reusable cron job design workflow — Context → Office Hour → Brainstorming → Grill Me → Docs → Execute |
| 4 | `adempus/machinations-skill` | 0 ⭐ | Game economy modeling with Machinations diagrams — 18 design patterns, verified syntax, references |

---

## 🔬 New Categories & Platforms (4)

| # | Repo | Stars | Description |
|---|------|:-----:|-------------|
| 5 | `fengjunlu618/stepfun-skills` | 0 ⭐ | First Chinese LLM provider skill for Hermes — StepFun (阶跃星辰) Chat/TTS/Image/ASR via Step Plan subscription |
| 6 | `aiedwardai/spcx-daily-report` | 1 ⭐ | SpaceX daily analysis report skill |
| 7 | `biscovery2015-collab/openclaw-news-skill` | 0 ⭐ | OpenClaw news aggregation with Traditional Chinese translation + WhatsApp |
| 8 | `SouthpawIN/nous-style-guide` | 0 ⭐ | Nous Research brand identity — monochrome design rules, image generation templates |

---

## 📦 Personal Collections & Stubs (7)

| # | Repo | Stars | Notes |
|---|------|:-----:|-------|
| 9 | `jamesbmour/Hermes-Skills` | 0 ⭐ | Personal skills collection |
| 10 | `superuser47/my-hermes-skills` | 0 ⭐ | Personal skills collection |
| 11 | `warmcrack2020/YAGENT_SKILLS` | 0 ⭐ | Personal skills — hermes-agent fork |
| 12 | `warmcrack2020/hermes-agent` | 0 ⭐ | Personal collection |
| 13 | `zhemed/hermes-skill-kit` | 0 ⭐ | 个人 Hermes Skill 仓库 |
| 14 | `lennney/hermes-skill-evolution` | 0 ⭐ | Skill self-evolution system — 被动存储到主动学习 |
| 15 | `overspread/hermes-skills` | 1 ⭐ | Productivity skills subdirectory |

---

## Spotlight: Fahrnetic Engineering Curation

**Source:** [Fahrnetic/hermes-engineering-skill-curation](https://github.com/Fahrnetic/hermes-engineering-skill-curation)
**Stars:** 1 ⭐ | **License:** MIT | **Created:** June 23, 2026

The most professionally-structured Hermes skill curation to date. Scanned 336 skills across the ecosystem and selected 104 based on quality, utility, and engineering rigor. Ships with 10 operator profiles covering different engineering roles.

### What's Inside

| Component | Content |
|-----------|---------|
| `CURATION.md` | Full curation methodology — scanning criteria, selection heuristics, quality tiers |
| `profiles/` | 10 operator profiles (role-specific skill loadouts) |
| `bundles/` | Pre-assembled skill bundles for common workflows |
| `reports/all-skills-inventory.json` | Machine-readable inventory of all 336 scanned skills |
| `PUBLIC_READINESS_AUDIT.md` | Public-facing audit documenting sanitization and readiness |
| `assets/` | SVG diagrams (workflow spine, gate matrix) |

### Engineering Spine

```
Route → Specify → Test → Build → Audit → Ship → Learn
```

Each phase has explicit gates, evidence loops, and role-separated review — moving from "make the change" to true engineering workflow.

### Installation

```bash
git clone https://github.com/Fahrnetic/hermes-engineering-skill-curation.git
cp -r hermes-engineering-skill-curation/profiles ~/.hermes/profiles/
cp -r hermes-engineering-skill-curation/bundles ~/.hermes/bundles/
```

**Setup guide:** [hermes-engineering-curation-setup.md](/hermes/skills/catalog/hermes-engineering-curation-setup/)

---

## Spotlight: Ghostwriter — Autonomous Email Auto-Reply

**Source:** [okokelly/skill-ghostwriter](https://github.com/okokelly/skill-ghostwriter)
**Stars:** 0 ⭐ | **License:** MIT | **Created:** June 23, 2026

A two-tier email auto-reply system designed for Hermes Agent. Splits the work: a lightweight Python **Watchdog** polls Gmail every 5 minutes (no LLM, zero token cost when idle), and hands off to the **Processor** agent only when a matching email is found.

### Architecture

```
Watchdog (script, no LLM)  →  Silent ($0) when no match
                           →  Processor (agent) when match:
                              1. Read email
                              2. Draft reply in your voice
                              3. Send
                              4. Archive
```

### Why It Matters

Polling Gmail with an LLM agent every 5 minutes burns ~$0.30/day in idle costs. Ghostwriter's Watchdog-first pattern eliminates this — the LLM only runs when there's actually an email to reply to. ~10x cost reduction.

### Quick Start

```bash
git clone https://github.com/okokelly/skill-ghostwriter.git
cp -r skill-ghostwriter ~/.hermes/skills/ghostwriter/
# Configure Gmail API credentials, VIP inbox, and voice profile
```

**Setup guide:** [ghostwriter-setup.md](/hermes/skills/catalog/ghostwriter-setup/)

---

## Spotlight: Cron Design Workflow

**Source:** [lovenps85/hermes-cron-design-workflow-skill](https://github.com/lovenps85/hermes-cron-design-workflow-skill)
**Stars:** 0 ⭐ | **License:** MIT | **Created:** June 23, 2026

A reusable Hermes Agent skill for designing cron jobs, scheduled automations, and recurring alerts. Adapts patterns from Superpowers (brainstorming, writing-plans), Matt Pocock (grill-me, domain-modeling), and GSTACK (office-hours) into a structured cron workflow.

### Workflow

```
Context → Office Hour → Brainstorming → Grill Me → Docs → Execute / Verify
```

### Installation

```bash
git clone https://github.com/lovenps85/hermes-cron-design-workflow-skill.git
mkdir -p ~/.hermes/skills/devops
cp -a hermes-cron-design-workflow-skill/cron-design-workflow ~/.hermes/skills/devops/
```

**Setup guide:** [cron-design-workflow-setup.md](/hermes/skills/catalog/cron-design-workflow-setup/)

---

## Cross-Reference

See also: [June 20-22 discovery](/hermes/skills/marketplace/new-june20-22-2026/) | [Full marketplace index](/hermes/skills/marketplace/)

---

*← [Previous: June 20-22, 2026](/hermes/skills/marketplace/new-june20-22-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*
