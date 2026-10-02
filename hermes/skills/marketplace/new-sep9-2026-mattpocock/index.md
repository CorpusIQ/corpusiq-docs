---
title: "September 9, 2026 (Evening) - Matt Pocock Workflow Suite: 27"
description: "Evening skills.sh sweep found a major gap in Matt Pocock coverage: 27 uncatalogued skills with 12.2M+ combined installs (grill-me 1.1M, grill-with-docs 941K, tdd 873K, handoff 774K, triage 760K) plus nexu-io/open-design impeccable-design-polish. 4 setup guides drafted."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep9-2026-mattpocock/"
robots: "index,follow"
last_updated: "2026-09-09"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills", "matt pocock", "design polish"]
sweep_id: "2026-09-09-evening-mattpocock"
new_publishers: 1
new_skills: 28
guides_drafted: 4
---

# New Skills - September 9, 2026 (Evening)

Standard 14-query skills.sh API sweep (268 unique skills) plus publisher-page reconciliation caught a **major coverage gap in the Matt Pocock catalog**: the existing guides documented 24 of his skills (19-skill writing suite, 5-skill engineering suite, claude-handoff), but the publisher page shows **27 more with a combined 12.2M+ installs**. The morning sweep's cluster-level cross-reference had treated the zh-CN localization references as full coverage of the English originals. 4 setup guides drafted.

## New Skills at a Glance

| Skill | Source | Installs | Category | Setup Guide |
|---|---|---|---|---|
| grill-me | mattpocock/skills | 1,103,281 | Interrogation | ✅ suite guide |
| grill-with-docs | mattpocock/skills | 941,573 | Interrogation | ✅ suite guide |
| tdd | mattpocock/skills | 873,338 | Engineering | ✅ suite guide |
| handoff | mattpocock/skills | 774,587 | Session management | ✅ suite guide |
| triage | mattpocock/skills | 760,099 | Issue management | ✅ suite guide |
| teach | mattpocock/skills | 626,663 | Education | ✅ suite guide |
| domain-modeling | mattpocock/skills | 603,161 | Architecture | ✅ suite guide |
| codebase-design | mattpocock/skills | 584,794 | Architecture | ✅ dedicated guide |
| diagnosing-bugs | mattpocock/skills | 574,167 | Debugging | ✅ suite guide |
| code-review | mattpocock/skills | 521,103 | Code quality | ✅ suite guide |
| wayfinder | mattpocock/skills | 483,129 | Planning | ✅ suite guide |
| research | mattpocock/skills | 476,454 | Research | ✅ suite guide |
| to-spec | mattpocock/skills | 474,307 | Specs | ✅ suite guide |
| to-tickets | mattpocock/skills | 466,073 | Tickets | ✅ suite guide |
| resolving-merge-conflicts | mattpocock/skills | 457,159 | Git | ✅ dedicated guide |
| wizard | mattpocock/skills | 335,511 | Human steps | ✅ suite guide |
| to-questionnaire | mattpocock/skills | 282,849 | Decisions | ✅ suite guide |
| loop-me | mattpocock/skills | 277,934 | Interrogation | ✅ suite guide |
| writing-for-agents | mattpocock/skills | 233,014 | Skill authoring | ✅ suite guide |
| wait-what | mattpocock/skills | 224,639 | Clarity | ✅ suite guide |
| setup-ts-deep-modules | mattpocock/skills | 211,966 | TypeScript | ✅ suite guide |
| retro | mattpocock/skills | 72,735 | Retrospectives | ✅ suite guide |
| impeccable-design-polish | nexu-io/open-design | 2,072 | Design polish | ✅ dedicated guide |

**Marketplace-only (S3 - listed on skills.sh, no SKILL.md in repo main branch):** qa (205,424), diagnose (238,518), obsidian-vault (201,849), review (94,292), batch-grill-me (64,409).

## Category Breakdown

### Matt Pocock Interrogation Layer (4 skills, 2.5M installs)

The "grill" family is the flagship methodology: relentless interviews that sharpen plans before any code is written. `grill-me` (1.1M) dispatches to `grilling`; `grill-with-docs` (941K) produces ADRs and a glossary during the interview; `loop-me` (277K) grills workflow specs; `wait-what` (224K) catches messages that did not land.

### Matt Pocock Engineering Layer (7 skills, 4.3M installs)

`tdd` (873K) is the red-green-refactor reference. `code-review` (521K) reviews along Standards and Spec axes. `diagnosing-bugs` (574K) is the hard-bug diagnosis loop. `domain-modeling` (603K) builds the CONTEXT.md/ADR vocabulary. `codebase-design` (584K) supplies the deep-module design language. `research` (476K) captures findings as repo Markdown. `setup-ts-deep-modules` (211K) wires dependency-cruiser so every package is a deep module.

### Planning-to-Tickets (5 skills, 2M installs)

`to-spec` (474K) and `to-tickets` (466K) turn conversations into tracker-published specs and tracer-bullet tickets. `wayfinder` (483K) maps work too big for one session as decision tickets. `wizard` (335K) generates interactive bash wizards for human-only steps. `to-questionnaire` (282K) exports decisions you can't answer.

### Session and Collaboration (5 skills, 2.5M installs)

`handoff` (774K) compacts a session into a handoff document. `triage` (760K) runs issues/PRs through a triage state machine. `teach` (626K), `writing-for-agents` (233K), and `retro` (72K) round out the collaboration layer.

### Open Design (1 skill, 2K installs)

`impeccable-design-polish` from nexu-io/open-design - a follow-up polish pass for existing HTML artifacts (audit, critique, polish, animate, harden, live), with explicit anti-AI-slop rules and CN-market triggers. Distinct from pbakaus/impeccable (different publisher, follow-up scope vs full design brain).

## Setup Guides Created

1. [codebase-design - Deep Module Design Vocabulary](/hermes/skills/catalog/codebase-design-setup) - 584K installs, glossary of module/interface/seam/adapter terms
2. [resolving-merge-conflicts - 5-Step Merge Protocol](/hermes/skills/catalog/resolving-merge-conflicts-setup) - 457K installs, always resolve, never abort
3. [Matt Pocock Agent Workflow Suite - 20 Skills](/hermes/skills/catalog/mattpocock-agent-workflow-suite-setup) - 11.4M combined installs across interrogation, engineering, planning, and session layers
4. [impeccable-design-polish - Post-Generation Polish](/hermes/skills/catalog/impeccable-design-polish-setup) - 2K installs, anti-AI-slop follow-up pass

## Quick Install

```bash
# The interrogation core
npx skills add mattpocock/skills --skill grill-me
npx skills add mattpocock/skills --skill tdd
npx skills add mattpocock/skills --skill handoff

# Design polish
npx skills add nexu-io/open-design --skill impeccable-design-polish
```

## Why This Matters for Hermes

Matt Pocock's full methodology is a complete agent operating system: grill plans before building, build test-first, review on two axes, convert conversations to tracked specs and tickets, and hand off cleanly between sessions. The 24 previously documented skills covered writing and the engineering pipeline's edges; these 27 fill in the core execution loop that connects them. `handoff` (774K) is directly relevant to Hermes multi-session workflows, and `codebase-design` gives agents a precise vocabulary for AI-navigable architecture. At 12.2M+ combined installs this was the largest single-publisher coverage gap in the catalog.
