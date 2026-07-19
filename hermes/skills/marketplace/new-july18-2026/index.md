---
title: "July 18, 2026 — Design Judge Skills, Loremaster PM, Agent Skill Stack"
description: "4 new Hermes-relevant skill repos discovered: SeanJ1ang design-judge-skills (25★, 5 skills for design award workflows), loremaster-ai PM skill pack (11 skills), agent-skill-stack (skill discovery tool), and MongrelDB-Hermes (hybrid memory backend)."
---

# 🆕 July 18, 2026 — 4 New Hermes-Agent Skill Repos

**Date:** July 18, 2026
**New Repos:** 4 | **New Skills:** 17+ | **Combined Stars:** 26

Evening discovery sweep across GitHub repos tagged `hermes-agent` and `agent-skills` created July 17-18, 2026. Cross-referenced against 324 existing catalog entries and all prior marketplace pages (June 9 — July 17, 2026). The headline find: **SeanJ1ang/design-judge-skills** (25★) — a production-grade skill pack that decomposes design award submissions into 5 boundary-clear, evidence-driven agent skills with bilingual (Chinese/English) documentation.

---

## New Repos at a Glance

| # | Repo | Stars | Skills | Category | Hermes-Ready |
|---|------|:-----:|:------:|----------|:------------:|
| 1 | **design-judge-skills** | 25 | 5 | Design / Awards | ✅ Tagged |
| 2 | **loremaster** | 1 | 11 | Project Management | ✅ Tagged |
| 3 | **agent-skill-stack** | 0 | 1+ | Meta / Skill Discovery | ✅ Tagged |
| 4 | **MongrelDB-Hermes** | 0 | — | Memory / Infrastructure | ✅ Tagged |

---

## Category Breakdown

### Design & Awards — design-judge-skills (25★, 6 forks) ⭐ Setup Guide Available

**Repo:** [SeanJ1ang/design-judge-skills](https://github.com/SeanJ1ang/design-judge-skills)
**Install:** `npx skills add SeanJ1ang/design-judge-skills`
**Language:** Python · **License:** Apache 2.0

The first comprehensive agent skill pack for the full design award lifecycle. Five modular skills cover research, evaluation, matching, entry preparation, and submission readiness — each with evidence-driven validation and transparent scoring. Configured for 11 major design awards: iF, Red Dot (Product + Concept), IDEA, DIA, K-Design, GOOD DESIGN Japan, Core77, James Dyson, and EPDA.

**The 5 skills:**

| Skill | What It Does |
|-------|-------------|
| **design-award-search** | Retrieve and verify winning entries in the same category from official sources |
| **design-evaluation** | Score design quality and presentation using evidence-based rubrics |
| **design-award-match** | Compare awards, tracks, and categories against project fit |
| **design-information-prep** | Prepare submission text constrained to source materials with word-count validation |
| **design-submission-check** | Final readiness check against current official rules — go / conditional go / no-go |

**Design principles:**
- Primary sources first — official award pages over third-party summaries
- Facts vs. inference separated — user materials, model inferences, and confirm-required items labeled distinctly
- Transparent scoring — fit scores aid decisions but don't simulate judging panels
- Modular — each skill operates independently with well-defined boundaries

**Why it matters for Hermes:** The design award submission process involves research, evaluation, writing, and compliance checking — all tasks where agent skills add leverage. These skills work across Claude Code, Codex, OpenClaw, OpenCode, and Hermes Agent. For CorpusIQ's content pipeline, the evaluation framework (evidence-based rubrics, source-first verification) is directly reusable for product review content.

**Setup Guide:** [Design Judge Skills — Full Setup Guide](/hermes/skills/catalog/design-judge-skills-setup/)

```bash
# Install all 5 skills + shared support package
npx skills add SeanJ1ang/design-judge-skills --skill design-award-search -g -y
npx skills add SeanJ1ang/design-judge-skills --skill design-evaluation -g -y
npx skills add SeanJ1ang/design-judge-skills --skill design-award-match -g -y
npx skills add SeanJ1ang/design-judge-skills --skill design-information-prep -g -y
npx skills add SeanJ1ang/design-judge-skills --skill design-submission-check -g -y
```

---

### Project Management — loremaster (1★)

**Repo:** [loremaster-ai/loremaster](https://github.com/loremaster-ai/loremaster)
**Install:** `npx skills add loremaster-ai/loremaster`

An AI scrum-master / PM skill pack purpose-built for Hermes Agent. Eleven skills that run a team's planning loop around a "lore vault" — a per-project wiki repo that stays the single source of truth. Extracted from a production system running Slack + Jira + GitHub.

**Core constraints (by design):**
- **Detect, don't decide** — AI surfaces conflicts and drift; humans own judgment
- **Approval gates** — Every write to external systems requires explicit per-item human approval
- **No invention** — Nothing enters the wiki without traceable sources; blanks flagged, never filled
- **One-way derivation** — raw/ → wiki/ → knowledge graph; humans never edit derived layers
- **Channel = project** — Memory, prompts, and graph isolated per project

**Architecture:** Slack planning loop → Lore vault (git repo with raw/, wiki/, graphify-out/) → Building loop (Claude Code, Cursor) → Jira. Obsidian for human browsing.

**Why it matters for Hermes:** For teams running Hermes Agent in production with multiple projects, loremaster provides governance structure — human-in-the-loop, source-traceable wiki, per-project isolation. Relevant for CorpusIQ's own multi-project management and potentially for operators managing their own Hermes deployments.

```bash
npx skills add loremaster-ai/loremaster -g -y
```

---

### Meta / Skill Discovery — agent-skill-stack (0★)

**Repo:** [neilchen2000-pixel/agent-skill-stack](https://github.com/neilchen2000-pixel/agent-skill-stack)
**Install:** `npx skills add neilchen2000-pixel/agent-skill-stack --skill agent-skill-stack -g -y`
**License:** MIT

A meta-tool that turns natural-language goals into minimal, audited AI agent skill stacks. Discovers, ranks, conflict-checks, and routes skills from GitHub, skills.sh, OpenCLI, and local environments. Derives a workflow from the outcome, reuses local capabilities, discovers direct and indirect helper skills, compares real-world adoption, checks safety and conflicts.

**Key features:**
- Goal → workflow derivation
- Multi-source skill discovery (GitHub, skills.sh, OpenCLI, local)
- Conflict detection between overlapping skills
- Adoption-based ranking
- Safety auditing

**Why it matters for Hermes:** As the skills ecosystem grows past 9,500+ skills, discovery becomes the bottleneck. agent-skill-stack is a discovery layer — useful for Hermes users who need to assemble skill stacks from the broader ecosystem without manually searching.

---

### Memory / Infrastructure — MongrelDB-Hermes (0★)

**Repo:** [visorcraft/MongrelDB-Hermes](https://github.com/visorcraft/MongrelDB-Hermes)
**Install:** Manual (Python package — not npx skills compatible)

A hybrid long-term memory backend for Hermes Agent using MongrelDB. Combines dense ANN (vector search), sparse retrieval, FM-index, bitmaps, learned ranges, and MinHash for multi-modal retrieval. An alternative to GBrain's PGLite backend for deployments that need stronger retrieval capabilities.

**Why it matters for Hermes:** For Hermes deployments needing production-grade memory beyond PGLite's single-connection limit. MongrelDB supports multi-process access, making it suitable for multi-agent setups. Early stage (0 stars, July 18 creation) — worth monitoring as an alternative memory backend.

---

## Setup Guides Added

This sweep produced one new setup guide:
- **[Design Judge Skills Setup Guide](/hermes/skills/catalog/design-judge-skills-setup/)** — 5 skills, design award workflow, evidence-driven evaluation framework

---

## Discovery Method

GitHub API search for repos tagged `hermes-agent` and `agent-skills` created July 17-18, 2026. 40 repos surfaced across two queries. Cross-referenced against all 324 existing catalog entries and 15 prior marketplace discovery pages (June 9 — July 17, 2026) via `grep -rl` across the full `hermes/skills/` directory. 4 new repos confirmed absent from prior sweeps.

Additional repos found (deployment/configuration tools, not skill repos — excluded):
- hermes-companion (Android voice, albertosena)
- hermes-search-survival-guide (SearXNG config, wu1chenghui)
- renz-launcher (Multi-agent launcher, BBRenxo)
- Various VPS/Cloudflare/Railway deployment templates

---

*← [July 17 Evening](/hermes/skills/marketplace/new-july17-2026-update/) | [Marketplace Home](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
