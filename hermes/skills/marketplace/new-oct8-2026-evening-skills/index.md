---
title: "New Skills - October 8, 2026 (Evening)"
description: "Skills.sh sweep (Oct 8 evening): 442 skills checked; 4 new publisher guides - Limrun Skills, TypeSafe AI Skills, Yomiyasu, and Proseify."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct8-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 8, 2026 (Evening Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. Fourth consecutive run of the reduced serving window (442 unique; the ~440 level first observed Oct 7), so coverage was again compensated with the skills.sh trending page (600 entries across 62 sources). All four new publishers below were surfaced by the compensation pass and sized with publisher follow-ups against the skills.sh API.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standard window) | 442 (15 queries, 0 failed) |
| NEW (not in catalog) | 19 (all below floor, max 5 installs) |
| PARTIAL (source known, skill not cataloged) | 131 |
| PARTIAL >= 100 installs | 0 |
| Trending compensation pass | 600 entries / 62 sources |
| New publisher guides | 4 |
| Roster reconciles | 0 |

## New Publisher Guides

### 1. Limrun Skills - Cloud iOS & Android Simulators (official)

**Source:** [limrun-inc/skills](https://www.skills.sh/limrun-inc/skills) (~74.6K combined across 10 indexed listings; 8 active skills; MIT; authority-justified - the official Limrun org behind the lim.run cloud simulator product)

Build and drive mobile apps from any environment: remote Xcode, iOS Simulator, and Android Emulator services covering xcodebuild and Bazel builds, Gradle, Detox and Maestro testing, Expo development, and full simulator interaction (launch, tap, type, accessibility tree, logs, screenshots, video). Sampled verdicts predominantly Pass (two Snyk Warns on build-skills).

-> [Setup guide](/hermes/skills/catalog/limrun-skills-setup)

### 2. TypeSafe AI Skills - Typed AI Judgments (official)

**Source:** [typesafe-ai/skills](https://www.skills.sh/typesafe-ai/skills/typesafe-ai) (88,323 installs; 2,632 stars, MIT)

The official skill for building with TypeSafe's System One models: small units of AI intelligence - Choice, Noul, and Score primitives - that return typed judgments and probabilities code can compose. The skill drives docs-first workflow design (route, rank, extract, verify, escalate) and reads the live documentation as part of the task. Pass/Pass/Pass.

-> [Setup guide](/hermes/skills/catalog/typesafe-ai-setup)

### 3. Yomiyasu - Japanese AI Prose Refinement

**Source:** [nanaism/yomiyasu](https://www.skills.sh/nanaism/yomiyasu/yomiyasu) (6,330 installs; 1,768 stars, MIT, very active)

An agent skill that refines AI-generated Japanese into natural Japanese: meaning-preserving edits across metaphors, subject-predicate relations, sentence-ending stance, paragraph logic, terminology, and punctuation, with a three-part output (changes / remaining AI-ish phrasing / points to confirm). Pass/Pass/Pass.

-> [Setup guide](/hermes/skills/catalog/yomiyasu-setup)

### 4. Proseify - Anti-Prose-Slop Book Writing

**Source:** [proseify.xyz](https://proseify.xyz) (37,577 installs for `anti-prose-slop`; site-distributed skill over a hosted MCP; MIT)

A book-writing engine for agents: public-domain corpus, genre recipes, and a chapter-by-chapter drafting pipeline with a scored revision loop. The skill supplies the anti-slop writing workflow; the hosted MCP supplies the tools. No skills.sh verdicts published (site source) - the skill file is directly fetchable for review.

-> [Setup guide](/hermes/skills/catalog/proseify-setup)

## NEW Candidates Below the Guide Floor

| Source | Listings | Installs | Note |
|---|---|---|---|
| parcha-ai/parcha-skills | 1 | 5 (tether) | Personal single-skill repo - below floor |
| pondsiders/skills | 1 | 4 | Below floor |
| kaleljl/my-news | 1 | 4 | Below floor |
| zubair-trabzada/ai-trading-hermes | 1 | 3 | Below floor |
| jordi-murgo/agent-skills | 1 | 3 | Below floor |
| (remaining 14 listings) | 14 | all <= 3 installs | personal / dormant single-skill repos - below floor |

## Notes

- **Collection window:** fourth consecutive run at the ~440 level (442 tonight) vs 706-733 from Sep 29 through Oct 7 morning. Direct probes confirm large publishers still exist on the platform; they are simply not served in the standard query windows. The trending-page compensation pass carried all of tonight's yield.
- **Sizing discipline:** trending-window figures undercount clusters by 10-100x (tonight: limrun 5.0K to 74.6K, typesafe-ai 714 to 88,323, yomiyasu 640 to 6,330, proseify 885 to 37,577). Every candidate was re-dumped via the skills.sh API (exact-source rows) before disposition; roster numbers use API sums only.
- **Site-source handling:** proseify.xyz is a product site, not a repository - the skill installs from the site URL (`npx skills add https://proseify.xyz --skill anti-prose-slop`) and its SKILL.md is fetchable at `proseify.xyz/skills/anti-prose-slop/SKILL.md` for review. Its skills.sh detail page is not available, so no security verdicts could be recorded.
- **Zero-catalog audit:** the standing OpenClaw / Azure / dormant-source set was re-sized via publisher follow-ups (irangareddy/openclaw-essentials 783, leoyeai/openclaw-master-skills 429, phenomenoner/openclaw-agent-optimize 165, microsoftdocs/agent-skills 20,786, arthurzakirov/agentdesk 3,055, skillatlas/skills 765) - all flat and standing; no re-qualifications.
- **Duplicate defense:** no Oct 8 evening skills-sweep commit existed at the remote tip (b82589ce7); single scheduled fire for the 0500z slot.
- Mechanics: one-pass rg crossref on the Mac Mini (~28s); 0 failed queries; all four new guides drafted against Oct 8, 2026 snapshots.

---

*Sweep run: Oct 8, 2026, skills-monitor cron (evening). Includes the Limrun, TypeSafe AI, Yomiyasu, and Proseify setup guides.*
