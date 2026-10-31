---
title: "New Skills - October 30, 2026 Evening"
description: "Skills.sh sweep (Oct 30 evening): a 68-query topic probe found 16 publisher guides for 1.10M combined installs across 1,717 indexed listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct30-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 30, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 885 unique skills with 0 failed queries: 85 NEW, 267 PARTIAL.

The standing window was silent above the 1,000-install trigger for the twenty-fourth consecutive fire, its top row reading 302 installs, and the trending board served 600 entries across 64 sources with all 64 already in the tree. The queue the previous fire drained was empty, so this fire ran a widened **68-query topic probe** across engineering, data, business, design and research topics instead.

That probe returned **5,276 unique skills across 68 queries with 0 failed queries**, and 2,025 of its listings sat in 1,004 sources the catalog did not cover. Every source with a window row of 1,500 installs or more was then sized by publisher, summing installs repo by repo rather than trusting a single window row: 99 sources cleared the 5,000-install floor, and the sixteen largest carry **1,101,389 combined installs across 1,717 indexed listings**.

Each guide was drafted against a pre-built pack holding the exact per-listing install figures, the cloned repository tree, branch and licence metadata and three-auditor verdicts sampled from skills.sh, then checked with three gates: the format gate, the pack cross-check at a per-guide threshold, and the frontmatter audit. All 48 gate runs passed on the first attempt, and the orchestrator re-ran every one of them after an md5 comparison of the three canonical scripts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 885 (0 failed queries) |
| NEW (not in catalog) | 85 |
| PARTIAL (source known, skill not cataloged) | 267 |
| Trending board | 600 entries / 64 sources, 0 uncovered |
| Above-floor finds in the standing window | 0 (top row 302) |
| Topic probe | 68 queries, 5,276 unique, 0 failed |
| Uncovered probe sources | 1,004 (2,025 listings) |
| Sources sized by publisher | 146 |
| Sources above the 5,000-install floor | 99 |
| Guides published this fire | 16 |

## Publisher Guides

| Guide | Repository | Installs | Listings | Stars | License |
|---|---|---|---|---|---|
| [Text to CAD Skills - 3D Model and URDF Setup](/hermes/skills/catalog/text-to-cad-skills-setup) | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | 124,096 | 18 | 24,377 | MIT |
| [Context Engineering Kit - Prompt and MCP Setup](/hermes/skills/catalog/context-engineering-kit-setup) | [neolabhq/context-engineering-kit](https://github.com/neolabhq/context-engineering-kit) | 110,374 | 138 | 1,795 | GPL-3.0 |
| [Science Skills - PubMed, arXiv and Lab Data Setup](/hermes/skills/catalog/science-skills-setup) | [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills) | 87,871 | 42 | 3,363 | Apache-2.0 |
| [SecondSky Claude Skills - Backend and API Suite Setup](/hermes/skills/catalog/secondsky-claude-skills-setup) | [secondsky/claude-skills](https://github.com/secondsky/claude-skills) | 85,061 | 200 | 240 | MIT |
| [Adobe Skills - PDF, Document and Creative Suite Setup](/hermes/skills/catalog/adobe-skills-setup) | [adobe/skills](https://github.com/adobe/skills) | 76,451 | 137 | 318 | Apache-2.0 |
| [Jwynia Agent Skills - Presentation and Writing Suite](/hermes/skills/catalog/jwynia-agent-skills-setup) | [jwynia/agent-skills](https://github.com/jwynia/agent-skills) | 65,356 | 119 | 180 | no LICENSE file at root |
| [ByteDance MediaKit CLI - Video Processing Setup](/hermes/skills/catalog/mediakit-cli-skills-setup) | [volcengine/mediakit-cli](https://github.com/volcengine/mediakit-cli) | 61,321 | 5 | 218 | MIT |
| [DeerFlow Skills - Deep Research Agent Setup](/hermes/skills/catalog/deer-flow-skills-setup) | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 60,292 | 26 | 84,743 | MIT |
| [LinkFox Skills - IP, Legal and Trade Data Setup](/hermes/skills/catalog/linkfox-skills-setup) | [linkfox-ai/linkfox-skills](https://github.com/linkfox-ai/linkfox-skills) | 58,424 | 200 | 115 | MIT |
| [Application Skills - SaaS Integration Suite Setup](/hermes/skills/catalog/application-skills-setup) | [membranedev/application-skills](https://github.com/membranedev/application-skills) | 57,985 | 200 | 270 | no LICENSE file at root |
| [Patricio Skills - Full Stack Engineering Suite Setup](/hermes/skills/catalog/patricio-skills-setup) | [patricio0312rev/skills](https://github.com/patricio0312rev/skills) | 56,693 | 153 | 63 | MIT |
| [Apollo GraphQL Skills - GraphQL and Rust Setup](/hermes/skills/catalog/apollographql-skills-setup) | [apollographql/skills](https://github.com/apollographql/skills) | 56,575 | 15 | 123 | MIT |
| [Patterns.dev Skills - UI and Rendering Patterns Setup](/hermes/skills/catalog/patterns-dev-skills-setup) | [patternsdev/skills](https://github.com/patternsdev/skills) | 53,715 | 58 | 258 | no LICENSE file at root |
| [Scenario Labs Skills - Custom Model Training Setup](/hermes/skills/catalog/scenario-labs-skills-setup) | [scenario-labs/skills](https://github.com/scenario-labs/skills) | 53,338 | 173 | 1,284 | MIT |
| [Android Skills - Play Policy and App Quality Setup](/hermes/skills/catalog/android-skills-setup) | [android/skills](https://github.com/android/skills) | 48,501 | 35 | 10,111 | Apache-2.0 |
| [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup) | [levnikolaevich/claude-code-skills](https://github.com/levnikolaevich/claude-code-skills) | 45,336 | 198 | 585 | MIT |

## What This Fire Found

The topic probe is what made this fire, and it is worth stating why plainly. The standing window watches Hermes-focused queries, so it cannot see a GraphQL vendor shipping skills for its own router, a camera-tracking CLI at ByteDance, or a 3,074-directory integration catalog from Membrane. Each of those carries far more installs than anything the standing window surfaced this week, and none of them mentions Hermes.

Three patterns ran through the batch. Vendor skill suites behave like documentation releases: Adobe ships 178 `SKILL.md` files across per-product plugins, Google ships 36 Android skills across 18 domain folders, and Apollo ships 15 GraphQL skills where the single largest install count belongs to a general Rust style guide. Single-author collections stay large and cheap to install: Patricio Marroquin publishes 155 markdown skills, SecondSky publishes 187 files across 145 plugin directories, and both are pure markdown with no scripts. And index-versus-tree drift is now the norm rather than the exception: 198 indexed listings against 41 skill directories for one publisher, 200 against 187 for another, and 138 against 68 distinct skills for a third.

Security verdicts were mixed. Four guides ship as Green on all-Pass samples: SecondSky, Patricio, Apollo and Patterns.dev. The other twelve carry a Snyk or Trust Hub Warn on at least one sampled skill, and every one of those guides states what the Warn means in the first sentence of its Security section rather than burying it in a table.

## Pitfalls Recorded This Fire

- A threshold ladder that only checks "at most 32 rows" can land above every row and produce an empty install table. The fix is to derive the threshold from the row distribution itself, at the twentieth largest row.
- A cross-reference sanity check that requires a Hermes name to appear in its own result set fails on a general-topic probe, because general queries never return Hermes repositories. The check must use a control literal already present in the tree.
- Trending-board sources must be matched against their own ripgrep pass. Reusing the topic-probe hit set marks every board source as uncovered, including repositories already documented.

## Related

- [Skills Catalog](/hermes/skills/catalog) - every setup guide in one index
- [Skills Marketplace](/hermes/skills/marketplace) - how the marketplace works

---

*← [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) →*
*Powered by CorpusIQ*
