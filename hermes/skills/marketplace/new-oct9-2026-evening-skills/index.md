---
title: "New Skills - October 9, 2026 (Evening)"
description: "Skills.sh sweep (Oct 9 evening): 441 skills checked; 6 new publisher guides incl. Baoyu Skills (594.5K); extended-query probe queues 19 more publishers."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct9-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 9, 2026 (Evening Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. Sixth consecutive run of the reduced serving window (441 unique; the ~440 level first observed Oct 7), so coverage was again compensated with the skills.sh trending page (600 entries across 66 sources) - and the sixth-run revisit flag was executed: an extended-query probe of five general queries (agent skills, claude skills, design engineering skill, ui design skill, frontend skill) served 454 rows across 185 sources, of which 87 were absent from the catalog tree. Every candidate was sized with an exact-source re-dump against the skills.sh API before disposition; that pass produced tonight's guides and a sizable queue for upcoming fires.

Two structural notes. First, the trending pass surfaced the jakubkrehel family, but a family-level check showed the suite was already documented in the [Better UI Skills guide](/hermes/skills/catalog/better-ui-skills-setup) - so that find became a full roster reconcile instead of a new guide (51.3K to 310.6K combined installs; two sibling repositories added). Second, the extended-query probe confirmed the Hermes-focused query window structurally misses the general publisher space; the sweep plan now carries a generic-query pass so this space is scanned every fire, which is also the mechanism that will drain the queue below.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standard window) | 441 (15 queries, 0 failed) |
| NEW (not in catalog) | 0 |
| PARTIAL (source known, skill not cataloged) | 146 (>= 100 installs: 0) |
| Trending compensation pass | 600 entries / 66 sources |
| Extended-query probe (revisit flag) | 5 queries / 454 rows / 185 sources; 87 zero-hit in tree |
| New publisher guides | 6 |
| Roster reconciles | 1 |
| Queued for upcoming fires (exact-sized) | 19 sources, ~1.06M combined installs |

## New Publisher Guides

### 1. Baoyu Skills - Content Generation & Publishing Suite (594.5K)

**Source:** [jimliu/baoyu-skills](https://www.skills.sh/jimliu/baoyu-skills) (594.5K combined across 24 indexed listings; 26,498 stars, MIT; active through Sep 2026)

A 21-skill content suite covering draft to published post: article illustration, comics, infographics, cover images, provider-agnostic image generation, markdown formatting and conversion, and multi-platform publishing (WeChat, Weibo, X, Xiaohongshu), plus translation and YouTube transcripts. The WeChat Official Account line is the flagship. Mixed security verdicts on the browser/publishing automation skills (see guide).

-> [Setup guide](/hermes/skills/catalog/baoyu-skills-setup)

### 2. UI Skills - Design Engineer Skill Registry (99.1K)

**Source:** [ibelick/ui-skills](https://www.skills.sh/ibelick/ui-skills) (99,066 across 8 indexed listings; 9,564 stars, MIT; pushed Oct 9, 2026)

Seven design-engineering skills - baseline-ui, improve-ui, create-design-md, fixing-accessibility, fixing-metadata, fixing-motion-performance, ui-skills-root - plus a CLI (`npx ui-skills`) and an MCP endpoint at ui-skills.com/mcp with list/get tools. All sampled verdicts Pass/Pass/Pass.

-> [Setup guide](/hermes/skills/catalog/ibelick-ui-skills-setup)

### 3. Meticulous Agent Skills - Visual Regression Testing (66.5K)

**Source:** [alwaysmeticulous/skills](https://www.skills.sh/alwaysmeticulous/skills) (66,536 across 23 indexed listings; ISC; pushed Oct 9, 2026; official Meticulous org)

Ten skills that teach agents to drive the Meticulous visual regression platform: run tests, review diffs against the PR description, classify intended vs unintended changes, fix rejected diffs, zero-diff tasks for refactors and migrations, coverage increase, and session simulation. Claude Code and Codex plugins auto-connect the hosted MCP server.

-> [Setup guide](/hermes/skills/catalog/meticulous-agent-skills-setup)

### 4. Designer Skills - Design Process Suite (43.0K)

**Source:** [julianoczkowski/designer-skills](https://www.skills.sh/julianoczkowski/designer-skills) (43,011 across 8 indexed listings; 578 stars, Apache-2.0)

Eight skills that encode design process so AI follows a structured path: grill-me, design-brief, information-architecture, design-tokens, brief-to-tasks, frontend-design, design-review, and the /design-flow orchestrator. Every artifact persists to a `.design/` folder per feature. All sampled verdicts Pass/Pass/Pass.

-> [Setup guide](/hermes/skills/catalog/designer-skills-setup)

### 5. Medusa Agent Skills - Official Ecommerce Platform Skills (39.4K)

**Source:** [medusajs/medusa-agent-skills](https://www.skills.sh/medusajs/medusa-agent-skills) (39,377 across 19 indexed listings; official Medusa org; pushed Oct 5, 2026; no LICENSE file - noted in the guide)

18 skills across four Claude Code plugins: medusa-dev (building applications, storefronts, admin dashboard customizations, internal agents, db-generate/db-migrate), learn-medusa, ecommerce-storefront (storefront best practices), and medusa-cloud (the mcloud CLI family). All sampled verdicts Pass/Pass/Pass.

-> [Setup guide](/hermes/skills/catalog/medusa-agent-skills-setup)

### 6. Garden Skills - ConardLi's Web Video & Design Suite (26.3K)

**Source:** [conardli/garden-skills](https://www.skills.sh/conardli/garden-skills) (26,317 across 5 indexed listings; 12,796 stars, MIT)

Five production-ready skills: web-video-presentation (click-driven 16:9 web presentations recordable as cinematic videos; 23 themes; pluggable TTS), web-design-engineer, gpt-image-2, kb-retriever, and beautiful-article. Ships pinned release zips with SHA-256 checksums for CI and air-gapped installs.

-> [Setup guide](/hermes/skills/catalog/garden-skills-setup)

## Roster Reconciles

- **Better UI Skills (jakubkrehel family):** refreshed from the August snapshot (51.3K combined) to 310.6K combined installs across three repositories - the main 13-skill suite, make-interfaces-feel-better (62,520), and oklch-skill (4,228). Counts refreshed for all 15 skills, security verdicts table added, tier upgraded Beta to Production.
  -> [Refreshed guide](/hermes/skills/catalog/better-ui-skills-setup)

## Extended-Query Probe - Queued for Upcoming Fires

Exact-source sizes; these are above the guide floor and carry no catalog coverage yet. They will be dispositioned on upcoming sweeps (the queue drains fastest by combined installs):

| Source | Listings | Combined | Note |
|---|---|---|---|
| wondelai/skills | 65 | 275,610 | Cross-platform design and engineering knowledge collection (typography, UX heuristics, iOS HIG, DDD); noted in the ecosystem review set, no catalog coverage until now |
| starchild-ai-agent/official-skills | 96 | 179,684 | Official agent-platform library - agent infrastructure + Shopify + trading skills |
| getcargohq/cargo-skills | 28 | 142,328 | GTM engineering for agents: lead lists, email find/verify, enrichment, CRM sync |
| samber/developer-platform-skills | 32 | 92,506 | Platform and SDK developer-experience skills (samber family extension) |
| open-mercato/skills | 63 | 78,867 | Enterprise ERP engineering skills from Open Mercato |
| bencium/bencium-marketplace | 17 | 53,121 | Design, marketing, and productivity marketplace by bencium.io |
| minimax-ai/skills | 24 | 48,246 | Official MiniMax dev suite: frontend/fullstack/mobile scaffolds, pptx/docx/pdf/xlsx generators, music and multimodal tools |
| dimillian/skills | 18 | 33,824 | SwiftUI and iOS skills (Thomas Ricouard) |
| sanyuan0704/sanyuan-skills | 6 | 29,906 | Code review expertise suite |
| ghostsecurity/skills | 8 | 27,900 | AppSec skills from Ghost Security (Apache-2.0) |
| benjitaylor/agentation | 2 | 20,140 | Visual feedback tooling for agents |
| jamditis/claude-skills-journalism | 67 | 18,908 | Journalism, media, and academia skill collection |
| ehmo/platform-design-skills | 8 | 12,727 | 450+ platform design rules: Apple HIG, Material Design 3, WCAG 2.2 |
| tencentcloudbase/cloudbase-skills | 33 | 12,468 | Official Tencent CloudBase full-stack skills + companion MCP |
| deeflect/mies | 1 | 8,705 | Design-taste skill: remove what an interface does not need |
| appllama/appllama-skills | 3 | 7,566 | Mobile app design patterns for agents |
| magicpathai/agent-skills | 1 | 6,303 | MagicPath design skills (official org) |
| cyxzdev/uncodixfy | 1 | 5,537 | Anti-generic UI instructions |
| ant-design/antd-skill | 4 | 5,281 | Official Ant Design skill |

A further ~60 sources below 4K installs from the same probe are logged in the sweep working set for triage.

## Notes

- **Collection window:** sixth consecutive run at the ~440 level (441 tonight) vs 706-733 from Sep 29 through Oct 7 morning. The standard queries added nothing above floor; the trending pass and the extended-query probe carried all of tonight's yield.
- **Revisit flag resolved:** the sixth consecutive ~440 run triggered the planned review of the fixed 15-query plan. Outcome: the plan keeps its Hermes-focused queries as a canary and gains a generic-query pass (the five probe queries above), because the general publisher space is demonstrably not served by Hermes-specific terms alone.
- **Sizing discipline:** trending-window and probe figures undercount clusters heavily (tonight: baoyu 25.3K to 594.5K and up; ibelick 10.1K to 99.1K; starchild 5.7K to 179.7K). Every roster number on this page and in the guides is an exact-source API sum.
- **Family-level check matters:** a source string can read zero-hit while the family is already documented (jakubkrehel/make-interfaces-feel-better looked uncovered; the Better UI guide already covered the suite). Dispositions check the source, the owner, and distinctive skill names before a guide is created.
- **Duplicate defense:** no Oct 9 evening skills-sweep commit existed at the remote tip (b85b8bee8); single scheduled fire for the 0500z slot.
- **Mechanics:** one-pass rg crossref on the Mac Mini; 0 failed queries; all guides and this page drafted against Oct 9, 2026 snapshots.

---

*Sweep run: Oct 9, 2026, skills-monitor cron (evening). Includes the Baoyu Skills, UI Skills, Meticulous Agent Skills, Designer Skills, Medusa Agent Skills, and Garden Skills setup guides, plus the Better UI roster reconcile and the extended-query probe queue.*
