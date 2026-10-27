---
title: "New Skills - October 22, 2026"
description: "Skills.sh sweep (Oct 22): 887 skills checked, 103 new. Three publisher clusters join the catalog: GMGN Agent Skills (156.2K), Claude Trading Skills (233.5K), ASO Skills (106.5K)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct22-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 22, 2026 Sweep

Morning sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The same 20-query window (15 Hermes-focused plus the 5-query generic pass) served 887 unique skills with 0 failed queries: 103 NEW, 271 PARTIAL.

This fire converted three publisher clusters and every one of them came from a follow-up rather than from the sweep window. The window saw one row each from three repos and ranked all of them below the 5,000-install guide floor, which is the sixth consecutive fire in which the NEW lane alone would have produced nothing. Querying the publishers instead of the rows revealed 133 indexed listings and 496,216 combined installs across the three, roughly 99 times the largest single row the window displayed.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 887 (0 failed queries) |
| NEW (not in catalog) | 103 |
| PARTIAL (source known, skill not cataloged) | 271 |
| New publisher guides | 3 (133 indexed listings, 496,216 combined installs) |
| Above-floor finds rejected | 2 (1 standing security rejection, 1 deleted repository) |
| Zero-catalog audit | 169 sources at 100+; 0 uncovered in catalog/ recursive; 0 converts |
| Trending | 32 entries / 22 sources; 3 uncovered above floor, all three converted here |
| Marketplace count | 1,138+ to 1,141+ |

## New Publisher Guides

### 1. GMGN Agent Skills (156,181 combined)

**Source:** [gmgnai/gmgn-skills](https://www.skills.sh/gmgnai/gmgn-skills), 19 indexed listings, top skill `gmgn-market` at 17,412; 624 stars; MIT; pushed 2026-10-21.

The agent layer of the GMGN multi-chain trading terminal: 19 skills over Solana, BSC, Base and Ethereum, split cleanly into market reading, wallet forensics, three single-score verdict skills and three that can move money. The scoring skills are the notable design: `gmgn-contract-dd` returns one 0-100 due-diligence number where every deduction names the field it read, and `gmgn-wallet-analysis` returns four pass/fail gates plus a copy window in seconds.

The tier is Beta rather than Production on verdicts alone. Snyk fails `gmgn-market` with HIGH W007 because the skill has the agent collect an API key and pass it as a command-line argument, which puts the secret in the model context and the logs, and it adds MEDIUM W009 direct money access on `gmgn-swap`. The guide documents the vendored `.env` path instead.

-> [Setup guide](/hermes/skills/catalog/gmgn-skills-setup)

### 2. Claude Trading Skills (233,532 combined)

**Source:** [tradermonty/claude-trading-skills](https://www.skills.sh/tradermonty/claude-trading-skills), 74 indexed listings, top skill `us-stock-analysis` at 5,563; 3,166 stars; MIT; pushed 2026-10-20.

A process toolkit for individual investors across eight categories, from market regime and core portfolio to trade memory and strategy research. The structure is what makes it catalog-worthy: five workflow manifests under `workflows/` name the skills, gates and artifacts in order, `skillsets/` bundles the install sets, and `skills-index.yaml` describes every skill with inputs, outputs and integrations.

Two facts decided how the guide is written. First, the publisher marks every skill `not_verified` across all eight verification axes in its own index, and the README disclaims advisory status in explicit terms, so the guide frames the suite as a disciplined framework rather than validated alpha. Second, the same author ships a [Hermes Trading Research Agent work package](https://github.com/tradermonty/hermes-trading-research-agent-work-package) that packages these skills into a Hermes profile with slash-command routines, which is the first time a trading publisher has shipped a Hermes-native companion.

-> [Setup guide](/hermes/skills/catalog/claude-trading-skills-setup)

### 3. ASO Skills (106,503 combined)

**Source:** [appeeky/aso-skills](https://www.skills.sh/appeeky/aso-skills), 40 indexed listings, top skill `aso-audit` at 4,452; 2,199 stars; MIT; pushed 2026-10-06.

40 skills covering the App Store and Google Play lifecycle, each matching one directory in the tree one to one. The suite carries the stores' own hard limits in context (iOS title 30, subtitle 30, keyword field 100, description 4000 and not indexed; Play title 30, short description 80, full description 4000 and indexed), which is exactly the constraint class a language model fails silently, and it ships an `aso-router` entry point so a user does not need to memorise 40 names.

Live data comes from the Appeeky API over MCP. The skills work standalone on framework knowledge, and the guide states plainly where the paid line is: first-party App Store Connect data through Appeeky Connect needs the Indie plan at eight dollars a month.

-> [Setup guide](/hermes/skills/catalog/aso-skills-setup)

## Above-Floor Rejections

[cyxzdev/uncodixfy](https://www.skills.sh/cyxzdev/uncodixfy) remains the only NEW row above 5,000 installs in the window at 5,589, and remains excluded: Snyk rates it CRITICAL under E004 prompt injection. It has been published as a rejection since October 21 morning and was not re-evaluated here.

[404kidwiz/claude-supercode-skills](https://www.skills.sh/404kidwiz/claude-supercode-skills) now sizes at 20,036 combined installs across 96 indexed listings, which would clear the floor four times over. The repository does not exist: the GitHub API returns 404, and raw probes for `SKILL.md`, `skills/<name>/SKILL.md` and `README.md` on both `main` and `master` return 404 as well. The counts are unactionable, and no guide can cite an install path.

## Zero-Catalog Audit

169 PARTIAL sources sit at 100 or more combined installs, audited against `catalog/` recursively (718 markdown files, full `owner/repo` match then exact owner token). 0 carry no catalog page, so the conversion queue is empty and this audit produced no converts.

The carry list moved for the first time in a week. [gogf/skills](https://www.skills.sh/gogf/skills) sits at 3,246 combined, still below the floor at 65 percent of it, and has been carried since October 19. Everything else on the list is a flat below-floor single-skill repo.

## Trending

The trending board served 32 entries across 22 sources this fire, a much smaller window than the 600 entries prior fires received, so treat its coverage as a sample rather than a census. Three sources had no catalog page and all three cleared the floor: gmgnai/gmgn-skills (17,412), tradermonty/claude-trading-skills (7,034) and appeeky/aso-skills (5,488). All three are converted in this fire, which is the first time the trending board has produced converts.

The popular board (96 entries / 75 sources) added no above-floor candidates. Its largest uncovered sources are softaworks/agent-toolkit (4,010), mapbox/mapbox-agent-skills (2,577) and vikiboss/60s-skills (2,032), each on its own below the floor, and each worth a publisher follow-up if it keeps climbing.

## Cross-Reference Note

The coverage test excludes per-fire report pages (`!**/marketplace/new-*/**`), so names stay NEW until a guide exists. This fire is also the first since October 20 in which the two cross-ref passes agreed exactly, which suggests the masking repair is holding on this snapshot.
