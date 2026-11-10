---
title: "New Skills - November 10, 2026 Morning"
description: "Skills.sh sweep (Nov 10 morning): 6 publisher guides for 38,584 combined installs across 101 indexed listings"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov10-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 10, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 885 unique skills across 0 failed queries: 81 NEW rows and 251 PARTIAL, with the top NEW row at 333 installs and nothing above the 1,000-install trigger. That is the forty-fifth consecutive silent window.

With the standing window silent, this fire drained the pre-sized candidate queue that the November 9 evening write-up left behind: eight sources named there as the obvious next batch, all re-tested against the current tree before drafting and all eight still undocumented. Six were documented; the two held back are recorded under Held below. A compact 50-query topic probe ran in parallel over domains the previous fire did not sweep, and its results are the queue for the next fire rather than a second batch here.

Every guide was built from a pre-verified pack holding the exact per-listing install figure for every indexed skill, the repository metadata, the real skill layout read from the GitHub tree and the frontmatter description of each skill. Each draft was then checked with three gates: the format gate, the pack cross-check at a per-guide threshold and the frontmatter audit. All 18 gate runs are green.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 885 (0 failed queries) |
| NEW (not in catalog) | 81 rows |
| PARTIAL (source known, skill not cataloged) | 251 |
| Above-floor finds in the standing window | 0 (top row 333) |
| Pre-sized queue drained | 6 of 8 |
| Fresh topic probe queries | 50 (0 failed) |
| Unique rows from the probe | 4,291 |
| Distinct sources from the probe | 1,471 |
| Uncovered sources above 3,000 combined | 12 |
| Guides published this fire | 6 |
| Combined installs documented | 38,584 |
| Indexed listings covered | 101 |
| Tier mix | 0 Green, 4 Yellow, 2 Orange |

## New Setup Guides

- [RevenueCat AI Toolkit](/hermes/skills/catalog/revenuecat-ai-toolkit-setup) - revenuecat/ai-toolkit, 17,555 combined, 20 listings, 79 stars, MIT, Mobile monetization: in-app purchases, paywalls, entitlements and subscription analytics through the RevenueCat MCP server
- [Alibaba Cloud Core Skills](/hermes/skills/catalog/alicloud-core-skills-setup) - cinience/alicloud-skills, 6,261 combined, 20 listings, 397 stars, MIT, Cloud platform: Model Studio and DashScope models, OSS, ECS, log service, key management and API discovery
- [CCXT Skills](/hermes/skills/catalog/ccxt-setup) - ccxt/ccxt, 4,794 combined, 12 listings, 44846 stars, MIT, Market data and trading: exchange APIs, WebSocket streams, order execution and the official CCXT MCP server
- [DDC Construction Skills](/hermes/skills/catalog/ddc-construction-skills-setup) - datadrivenconstruction/ddc_skills_for_ai_agents_in_construction, 4,538 combined, 20 listings, 402 stars, MIT, Construction operations: BIM analysis, CAD and IFC conversion, quantity takeoff, cost estimation and document control
- [Novu Skills](/hermes/skills/catalog/novu-skills-setup) - novuhq/skills, 3,299 combined, 9 listings, 4 stars, MIT, Notifications: workflow design, multi-channel delivery, in-app inbox, subscriber and preference management
- [Supply Chain Skills](/hermes/skills/catalog/awesome-supply-chain-skills-setup) - kishorkukreja/awesome-supply-chain, 2,137 combined, 20 listings, 96 stars, MIT, Supply chain and operations research: inventory, procurement, forecasting, routing, warehouse and vertical playbooks

## Held

- `streamlit/agent-skills` (3,604 combined across 19 listings) was held rather than published. The install base is one skill: `developing-with-streamlit` carries 3,452 of the 3,604, and the repository tree holds a single `SKILL.md` while the index lists 19 names, so a guide would have to describe eighteen skills that have no file in the current tree.
- `workos/skills` (4,732 combined across 20 listings) was held on the same class of drift. The tree carries three `SKILL.md` files against twenty indexed names, and four of the sampled listings carry a Snyk Fail or an Agent Trust Hub Fail, which is more remediation than a single guide can honestly cover.

## Probe Queue for the Next Fire

The 50-query probe covered recruiting, legal, compliance, healthcare, education, real estate, construction, manufacturing, logistics, hospitality, retail, security, mobile, game development, embedded, web3, analytics, agent infrastructure, documentation, support, project management and design. It returned 4,291 unique rows across 1,471 sources, 12 of which carry at least 3,000 combined installs and have no catalog page: `zhinkgit/embeddedskills` (8,205 across 12), `zhaoxuya520/reverse-skill` (7,382 across 6), `404kidwiz/claude-supercode-skills` (4,038 across 17), `dhruvanbhalara/skills` (3,735 across 14), `ctsstc/get-shit-done-skills` (3,656 across 1), `sanity-io/context` (3,448 across 3), `philschmid/self-learning-skill` (3,431 across 1), `jgraph/drawio-mcp` (3,412 across 1), `devmartinese/awwwards-animations-skill` (3,119 across 1), `evanca/flutter-ai-rules` (3,075 across 12), `content-designer/ux-writing-skill` (3,032 across 1) and the DDC construction set published here. Two of those carry standing exclusions from earlier fires and need re-checking rather than drafting.

## Verification

Every guide carries its exact per-listing install figures, a snapshot line with the verified date and the sampled skills.sh verdicts. Re-check the security pages on skills.sh before production use: install counts and verdicts drift.

## Related

- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)
- [November 9, 2026 Evening Sweep](/hermes/skills/marketplace/new-nov9-2026-evening-skills)
