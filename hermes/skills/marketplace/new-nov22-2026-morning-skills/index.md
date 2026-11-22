---
title: "New Skills - November 22, 2026 Morning"
description: "Skills.sh sweep (Nov 22 morning): 12 guides, 104,507 combined installs across 677 listings, led by Microsoft Power Platform and a .NET developer suite"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov22-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 22, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

The standing 20-query window returned 885 unique listings across 290 distinct sources with 77 uncovered rows and no failed queries. Its top row was 158 installs for `wwewtech/anti-slop-design`, followed by 150 for `danielteles/awesome-agent-skills` and 150 for `designrique/ai-graphic-design-skill`, so the window carried no convertible cluster and a fresh topic probe did the discovery work.

The probe ran 285 lanes across back-office and finance, legal and compliance, clinical and lab work, industry verticals from construction to agriculture, and developer platforms from mobile to data engineering. Every shortlisted publisher was then sized through its own exact-source filter before ranking, because a probe row understates a large publisher by an order of magnitude, and 63 of those sizes were used to order the batch.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 885 listings |
| Distinct sources in the standing window | 290 |
| Uncovered rows in the standing window | 77 |
| Top standing-window row | 158 (`wwewtech/anti-slop-design`) |
| Fresh topic lanes completed | 285 |
| Probe rows this fire | 15,970 rows |
| Distinct listings across both lanes | 14,949 |
| Distinct names across both lanes | 11,457 |
| Distinct sources across both lanes | 4,367 |
| Uncovered sources after cross-reference | 3,065 |
| Candidates sized by exact source | 63 |
| Publishers published | 12 |
| Indexed listings behind those guides | 677 |
| Combined installs behind those guides | 104,507 |

## Published Guides

| Publisher | Guides | Combined installs | Listings |
|---|---|---:|---:|
| [Microsoft Power Platform Skills - Setup Guide](/hermes/skills/catalog/microsoft-power-platform-skills-setup) | 1 | 19,053 | 96 |
| [Wshaddix .NET Skills - Developer Suite Setup](/hermes/skills/catalog/wshaddix-dotnet-skills-setup) | 1 | 13,465 | 96 |
| [Mysten Labs Skills - Sui Move Development Setup](/hermes/skills/catalog/mystenlabs-skills-setup) | 1 | 12,894 | 33 |
| [aiBTC Skills - Bitcoin, Stacks and DeFi Setup](/hermes/skills/catalog/aibtcdev-skills-setup) | 1 | 11,729 | 96 |
| [Syncfusion WinForms Skills - UI Component Suite Setup](/hermes/skills/catalog/syncfusion-winforms-skills-setup) | 1 | 8,354 | 96 |
| [NextStage Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/nextstage-brasil-skills-setup) | 1 | 7,843 | 96 |
| [Agents Inc Skills - Atomic Skills Marketplace Setup](/hermes/skills/catalog/agents-inc-skills-setup) | 1 | 6,735 | 96 |
| [CNKI Skills - Academic Search, Download & Zotero Setup](/hermes/skills/catalog/cookjohn-cnki-skills-setup) | 1 | 6,254 | 10 |
| [Scientific Skills - Literature Search Suite Setup](/hermes/skills/catalog/yorkeccak-scientific-skills-setup) | 1 | 5,059 | 13 |
| [Apifox CLI Skills - API Design and Test Automation Setup](/hermes/skills/catalog/apifox-cli-skills-setup) | 1 | 4,654 | 8 |
| [DefiLlama Skills - DeFi Analytics Setup](/hermes/skills/catalog/defillama-skills-setup) | 1 | 4,476 | 11 |
| [NocoBase Skills - No-Code Platform Suite Setup](/hermes/skills/catalog/nocobase-skills-setup) | 1 | 3,991 | 26 |

Two publishers carry a Green tier with every sampled verdict passing: Microsoft, whose Power Platform marketplace ships nothing worse than a Snyk Warn, and Agents Inc, which is MIT licensed and clean across the sample. Six carry Yellow with Warn cells and no Fails. Four carry Orange after a Fail cell in the sample: Mysten Labs (two Fail cells), NocoBase (three, all Snyk), Apifox (one Snyk Fail on the apifox-cli skill) and Scientific Skills, where all 13 sampled skills carry a Snyk Fail even though the other two scanners pass every one.

Each guide states those cells in its own Security table, so a reader can see which skills failed before installing them. Each guide also carries the exact install count for every skill above its own threshold, the repository licence position, and the index-versus-tree drift where the two disagree. Microsoft's marketplace spans five Power Platform app types plus Power Automate, and its telemetry is on by default for several plugins. Agents Inc indexes 96 listings against 238 skill directories in the tree. Syncfusion's 96 listings sit in a flat 84 to 103 band because one install pulls the whole control set, not because the controls are equally popular. CNKI needs an institutional subscription for most of the content it reaches.

Held on evidence: seven candidates that served skills.sh listings had GitHub repositories returning 404 to the REST API, so no page was written for them - `equinor/fusion-skills` (5,376 probe installs), `404kidwiz/claude-supercode-skills` (3,875), `sales-skills/sales` (2,693), `lvtd-llc/skills` (2,266), `scientiacapital/skills` (803), `danhvb/my-ba-skills` (725) and `hosmelq/skills`. Single-listing publishers were held as thin, and one AI-detection and text-humanizing suite was held because its README leads with defeating academic integrity scanners.

## Related

- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)
- [November 21, 2026 Evening Sweep](/hermes/skills/marketplace/new-nov21-2026-evening-skills)
