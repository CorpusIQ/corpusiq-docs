---
title: "New Skills - October 9, 2026"
description: "Skills.sh sweep (Oct 9 morning): 442 skills checked; 1 new publisher guide - Modern Web Guidance, official Google Chrome web best-practices skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct9-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 9, 2026 (Morning Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. Fifth consecutive run of the reduced serving window (442 unique; the ~440 level first observed Oct 7), so coverage was again compensated with the skills.sh trending page (600 entries across 64 sources). The new publisher below was surfaced by the compensation pass and sized with a publisher follow-up against the skills.sh API - the trending figure undercounted it 60x (617 trending vs 37,119 actual).

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standard window) | 442 (15 queries, 0 failed) |
| NEW (not in catalog) | 14 (all below floor, max 3 installs) |
| PARTIAL (source known, skill not cataloged) | 134 |
| PARTIAL >= 100 installs | 0 |
| Trending compensation pass | 600 entries / 64 sources |
| New publisher guides | 1 |
| Roster reconciles | 0 |

## New Publisher Guides

### 1. Modern Web Guidance - Chrome & Edge Team Web Best Practices (official)

**Source:** [googlechrome/modern-web-guidance](https://www.skills.sh/googlechrome/modern-web-guidance/modern-web-guidance) (37,119 combined across 2 indexed listings; official Google Chrome org with Microsoft Edge team support; Apache-2.0; 2,455 stars)

Two skills that keep coding agents current on the modern web platform: modern-web-guidance (search and retrieve curated guides for HTML/CSS/client-side JS - view transitions, container queries, popovers, `:has()`, scroll-driven animation, LCP/INP performance, accessibility, built-in AI APIs) and chrome-extensions (Manifest V3 development end to end plus Chrome Web Store publishing prep). Verdicts: Pass/Warn/Warn and Pass/Warn/Pass.

-> [Setup guide](/hermes/skills/catalog/googlechrome-modern-web-guidance-setup)

## NEW Candidates Below the Guide Floor

| Source | Listings | Combined installs | Note |
|---|---|---|---|
| mturac/hermes-supercode-skills | 13 | 45 | Personal multi-skill repo - below floor |
| backtomyfuture/agent-skills | 17 | 44 | Personal Chinese-language suite - below floor |
| sdamkkk/openclaw-data-analyst-skills | 11 | 35 | OpenClaw-class personal repo - below floor |
| bog5d/claude-skills | 23 | 30 | Personal bundle - below floor |
| pablof7z/mosaico | 3 | 9 | Dev-tool skill bundle - below floor |
| fil-builders/filecoin-clawdi-fleet | 4 | 8 | Below floor |
| mechovation/superpowers-hermes | 8 | 8 | Superpowers derivative, all single-install rows - below floor |
| xiaoquqi/hermes-agent-skills | 5 | 5 | Below floor |
| jyje/skills | 2 | 2 | Below floor |
| sergiocoding96/hermes-multi-agent | 2 | 2 | Below floor |
| xiaoshiyilangzhao1996-droid/skillplus | 2 | 2 | Below floor |
| entrovyx/hermes-agent-offsec | 1 | 1 | Below floor |
| sisyphe42/portable-skill-creator-skill | 1 | 1 | Below floor |
| sipingme/web-publisher-skill | 1 | 1 | Below floor |

## Notes

- **Collection window:** fifth consecutive run at the ~440 level (442 this morning) vs 706-733 from Sep 29 through Oct 7 morning. Direct probes confirm the larger publishers still exist on the platform; they are simply not served in the standard query windows. The trending-page compensation pass carried today's yield.
- **Sizing discipline:** trending-window figures undercount clusters heavily (this run: googlechrome/modern-web-guidance 617 trending vs 37,119 via the API exact-source re-dump). Every candidate was sized via the API before disposition; roster numbers use API sums only.
- **Superpowers mirror set (standing):** five additional `*/superpowers` mirrors surfaced in the trending window (skills-shell 54,930; 101-skills 54,915; its-a-skill-issue 54,837; qu-skills 54,610; bankai-skills 54,513) plus magentosh/superpowers (162,111) - all already recorded on the inference-sh skills guide's mirror list; no new action.
- **Zero-catalog audit:** all 14 NEW candidates were sized via publisher follow-ups (largest cluster 45 combined) - all below floor. The standing set was re-sized and remains flat: irangareddy/openclaw-essentials 783, leoyeai/openclaw-master-skills 430, phenomenoner/openclaw-agent-optimize 165 (OpenClaw exclusion class); microsoftdocs/agent-skills 20,790 (Azure class); arthurzakirov/agentdesk 3,055 and skillatlas/skills 765 (dormant, below floor).
- **Duplicate defense:** no Oct 9 skills-sweep commit existed at the remote tip (4ab9b2748, the MCP night sweep); single scheduled fire for the 1100z slot.
- **Mechanics:** one-pass rg crossref on the Mac Mini (~21s sweep, 0 failed queries); guide drafted against the Oct 9, 2026 snapshot.

---

*Sweep run: Oct 9, 2026, skills-monitor cron (morning). Includes the Modern Web Guidance setup guide.*
