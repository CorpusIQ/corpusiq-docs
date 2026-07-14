---
title: June 24, 2026 — Skills Discovery Roundup
description: 22 new Hermes skill repos discovered on June 24, 2026 including Ashima orchestration router, SG Arrival Card automation, Perfectloop design framework, and Three-Agent Bridge Protocol
---

# 🆕 June 24, 2026 — Skills Discovery Roundup

**22 repos discovered, 4 setup guides created, 11 srkhorde stubs skipped (empty READMEs).**

---

## ⭐ Top Picks (with Setup Guides)

| # | Repo | Stars | Type | Setup Guide |
|---|------|:-----:|------|:-----------:|
| 1 | `doucoo/ashima` | ⭐1 | Meta-routing (4 skills: ashima, aria, duet, chorus) | [Ashima Setup](/hermes/skills/catalog/ashima-setup/) |
| 2 | `Freakingnolife/sg-arrival-card-skill` | ⭐2 | Browser automation (SGAC submission) | [SG Arrival Card Setup](/docs/hermes/skills/catalog/sg-arrival-card-setup.html) |
| 3 | `sebmarion/hermes-agent-skill-perfectloop` | ⭐0 | Loop design framework (21KB SKILL.md) | [Perfectloop Setup](/docs/hermes/skills/catalog/perfectloop-setup.html) |
| 4 | `airbrushbones-afk/hermes-skills` | ⭐0 | Three-Agent Bridge Protocol | [Three-Agent Bridge Setup](/docs/hermes/skills/catalog/three-agent-bridge-setup.html) |

### 1. Ashima — Meta-Routing Orchestrator (doucoo/ashima)

A meta-routing skill for AI agent orchestration with three voices:
- **Aria** — Coding orchestration: Codex implements, Claude reviews. Scoped delegation with explicit verification gates.
- **Duet** — Dual-perspective reasoning: Fans a question to Claude-side and GPT-side, runs critique rounds, then synthesizes.
- **Chorus** — Documentation orchestration: Gathers repo context, drafts docs/changelogs, routes through independent review.

Package contains 4 SKILL.md files (ashima router + 3 voices). 6KB+ each. Apache-2.0 license with CHANGELOG and docs subdirectory.

**Why it matters:** Direct alternative to Ashima's own meta-orchestrator. The router auto-detects task type and loads the matching voice — useful for CorpusIQ's multi-agent setup where different task types need different review pipelines.

### 2. SG Arrival Card — Browser Automation (Freakingnolife)

13KB SKILL.md covering full SGAC submission workflow. Covers all three residency pathways (SC/PR, LTVP, Foreign Visitor). Handles Angular SPA quirks, CAPTCHA routing, and group submissions.

Includes 5+ helper scripts:
- `js_click_by_text.js` — Click Angular buttons by visible text
- `set_health_no.js` — Set health declaration toggles to NO
- `check_declaration.js` — Tick review-page declaration checkbox
- `extract_captcha.js` — Pull CAPTCHA image from page
- `save_captcha.py` — Decode and save CAPTCHA PNG

Portable across agents — uses abstract capability bindings (Open, Click, Type, PageJS, RunCode) mapped in `references/portability.md`.

**Why it matters:** Most polished browser-automation skill in the catalog. The Angular SPA patterns (click→type→commit tab cycle) transfer directly to any government portal automation task.

### 3. Perfectloop — Loop Design Framework (sebmarion)

21KB SKILL.md — the largest single skill file seen this week. A design-layer framework for building safe, testable agent loops.

**Key features:**
- 8-question core contract before any loop is designed
- Loop fit test: "Should this be a loop at all?"
- Falsifiable goals only — kills vague/unfalsifiable objectives
- Objective external gates: agent proposes, reviewer gate judges
- State file contract: persistent state must survive between runs
- 7 key failure modes documented (no gate, self-grading, no state, vague stop, no budget, judgment loops, orphaned schedulers)

**Why it matters:** Directly applicable to every CorpusIQ cron job and automated workflow. The 8-question interview would catch the issues that plague cron-based automations.

### 4. Three-Agent Bridge Protocol (airbrushbones-afk)

7KB SKILL.md defining a real-time sync protocol for three Hermes agents: Human + Desktop Hermes + VPS Hermes.

Core mechanism: Shared JSONL bridge file (`bridge-chat.jsonl`) acts as real-time communication channel. Every agent mirrors their conversation; polls the bridge file.

Two deployment patterns:
- **Same filesystem:** Both agents share NFS/SMB mount
- **VPS-hosted:** Desktop polls VPS via SSH every 2 seconds

Priority levels, conversation mirroring discipline, and all real-world deployment pitfalls documented.

**Why it matters:** Addresses a core limitation — Hermes bots can't join Telegram groups. The bridge file pattern is directly portable to CorpusIQ's multi-agent setup on the Mac Mini + Hermes server.

---

## 📋 Full Discovery List (22 repos)

### Substantive (8 repos — catalogued above or noted)

| Repo | Notes |
|------|-------|
| `doucoo/ashima` | ✅ Setup guide created — 4 skills |
| `Freakingnolife/sg-arrival-card-skill` | ✅ Setup guide created |
| `sebmarion/hermes-agent-skill-perfectloop` | ✅ Setup guide created |
| `airbrushbones-afk/hermes-skills` | ✅ Setup guide created — Three-Agent Bridge |
| `halmisen/hermes-skills` | Community collection — 1 skill: `wsl-windows-printer-invocation` |
| `c1ayooo/yuque-saber` | Yuque (Chinese knowledge base) automation |
| `DASEIN16615/skill` | Chinese Hermes skill collection |
| `joacogarciach/Hermes_Agent` | Portable Hermes config + skills + SOUL + cron |

### Niche / Single-Use (3 repos)

| Repo | Notes |
|------|-------|
| `JeroenThibaut/lago-abdijkaai-reservaties-skill` | Lago Abdijkaai venue reservations (Belgian) — very narrow geographic scope |
| `Freakingnolife/sg-arrival-card-skill` | Singapore-specific — but reference patterns for any government form automation |

### Empty Stubs (11 repos — all srkhorde)

`srkhorde/hermes-vps-deploy`, `srkhorde/hermes-webui-windows`, `srkhorde/ponytail` (duplicate of existing ponytail catalog entry), `srkhorde/website-prd`, `srkhorde/hostinger-base64-deploy`, `srkhorde/online-business-profile`, `srkhorde/web-design-audit`, `srkhorde/web-hosting-deploy`, `srkhorde/ssh-vps-windows`, `srkhorde/data-driven-app-discovery`, `srkhorde/non-tech-admin-ui`, `srkhorde/clone-existing-ui-not-redesign`

All 11 repos from `srkhorde` have **0-byte READMEs** and no SKILL.md files. Zero stars each. These are stub repos with no executable content. Skipped.

> **Note:** `srkhorde/ponytail` is a duplicate of the already-catalogued `tensakulabs/hermes-ponytail`.

---

## 📊 Stats

| Metric | Count |
|--------|:-----:|
| New repos discovered | 22 |
| Substantive repos | 8 |
| Setup guides created | 4 (Ashima, SGAC, Perfectloop, 3-AB) |
| Empty stubs skipped | 11 |
| New skills in catalog | 4 unique + 3 sub-skills from Ashima |
| Marketplace total | 366+ curated skill repos |

---

*← [Marketplace Home](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills). Built by [CorpusIQ](https://www.corpusiq.io).*
