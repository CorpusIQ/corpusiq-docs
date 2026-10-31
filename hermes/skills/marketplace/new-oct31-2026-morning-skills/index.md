---
title: "New Skills - October 31, 2026 Morning"
description: "Skills.sh sweep (Oct 31 morning): 16 publisher guides for 536.1K combined installs across 835 indexed listings from the October 30 probe queue."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct31-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 31, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 885 unique skills with 0 failed queries: 85 NEW, 268 PARTIAL.

The standing window was silent above the 1,000-install trigger for the twenty-fifth consecutive fire, its top row reading 302 installs, and the October 30 evening probe left 73 undocumented above-floor sources, every one sized by publisher. This fire drained the sixteen largest, so no new probe was needed.

Every guide was built from a pre-verified pack holding the exact per-listing install figures, the cloned repository tree with its branch, licence and skill directories, and three-auditor verdicts sampled from skills.sh. Each draft was then checked with three gates: the format gate, the pack cross-check at a per-guide threshold, and the frontmatter audit. All 48 gate runs passed, and the orchestrator re-ran every one of them after an md5 comparison of the three canonical scripts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 885 (0 failed queries) |
| NEW (not in catalog) | 85 |
| PARTIAL (source known, skill not cataloged) | 268 |
| Above-floor finds in the standing window | 0 (top row 302) |
| Queue carried from the October 30 probe | 73 above-floor sources |
| Guides published this fire | 16 |
| Combined installs documented | 536,147 |
| Indexed listings covered | 835 |

## Publisher Guides

| Guide | Repository | Installs | Listings | Stars | License |
|---|---|---|---|---|---|
| [Jaganpro SF Skills - Salesforce Agent Suite](/hermes/skills/catalog/jaganpro-sf-skills-setup) | [jaganpro/sf-skills](https://github.com/jaganpro/sf-skills) | 43,852 | 46 | 424 | MIT |
| [Anti-Slop - AI Copywriting Quality Skill](/hermes/skills/catalog/anti-slop-setup) | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | 41,307 | 6 | 7,670 | MIT |
| [Browserbase Skills - Agent Browser Automation](/hermes/skills/catalog/browserbase-skills-setup) | [browserbase/skills](https://github.com/browserbase/skills) | 40,127 | 20 | 3,747 | no LICENSE file |
| [JEO Skills - Presentation and Document Suite](/hermes/skills/catalog/jeo-skills-setup) | [akillness/jeo-skills](https://github.com/akillness/jeo-skills) | 37,915 | 112 | 53 | no LICENSE file |
| [CCFA Skills - Academic Paper and Research Suite](/hermes/skills/catalog/ccfa-skills-setup) | [mikubaka88/ccfa-skills](https://github.com/mikubaka88/ccfa-skills) | 33,935 | 24 | 3,358 | MIT |
| [TanStack Agent Skills - Query and Router Setup](/hermes/skills/catalog/deckardger-tanstack-agent-skills-setup) | [deckardger/tanstack-agent-skills](https://github.com/deckardger/tanstack-agent-skills) | 32,849 | 4 | 228 | MIT |
| [Chris Banes Skills - Compose and Kotlin Suite](/hermes/skills/catalog/chrisbanes-skills-setup) | [chrisbanes/skills](https://github.com/chrisbanes/skills) | 32,776 | 35 | 1,133 | Apache-2.0 |
| [Paul Berg Agent Skills - Solidity and Foundry](/hermes/skills/catalog/paulrberg-agent-skills-setup) | [paulrberg/agent-skills](https://github.com/paulrberg/agent-skills) | 32,742 | 97 | 104 | MIT |
| [Maggy Skills - Android and Kotlin Agent Suite](/hermes/skills/catalog/maggy-skills-setup) | [alinaqi/maggy](https://github.com/alinaqi/maggy) | 32,037 | 73 | 710 | MIT |
| [SAP Skills - BTP, CAP and ABAP Agent Suite](/hermes/skills/catalog/sap-skills-setup) | [secondsky/sap-skills](https://github.com/secondsky/sap-skills) | 31,778 | 45 | 482 | GPL-3.0 |
| [Tencent CloudBase Agent Skills - WeChat Dev](/hermes/skills/catalog/tencent-cloudbase-agent-skills-setup) | [tencentcloudbase/skills](https://github.com/tencentcloudbase/skills) | 30,797 | 37 | 80 | MIT |
| [OrchestKit - Orchestration and DevOps Skills](/hermes/skills/catalog/orchestkit-skills-setup) | [yonatangross/orchestkit](https://github.com/yonatangross/orchestkit) | 30,386 | 151 | 300 | MIT |
| [Cypress AI Toolkit - E2E Testing Skills](/hermes/skills/catalog/cypress-ai-toolkit-setup) | [cypress-io/ai-toolkit](https://github.com/cypress-io/ai-toolkit) | 30,426 | 5 | 46 | MIT |
| [Asyraf Hussin Skills - Clean Code Suite](/hermes/skills/catalog/asyrafhussin-agent-skills-setup) | [asyrafhussin/agent-skills](https://github.com/asyrafhussin/agent-skills) | 29,010 | 24 | 95 | MIT |
| [Tigris Data Skills - Object Storage for Agents](/hermes/skills/catalog/tigrisdata-skills-setup) | [tigrisdata/skills](https://github.com/tigrisdata/skills) | 28,128 | 19 | 2 | MIT |
| [Xiaohongshu Skills - RED Content Operations](/hermes/skills/catalog/xiaohongshu-skills-setup) | [vivy-yi/xiaohongshu-skills](https://github.com/vivy-yi/xiaohongshu-skills) | 28,082 | 137 | 515 | no LICENSE file |

## What Changed

Four repositories in this batch carry a verdict that had to lead the page rather than sit in a footnote: `rtk` in akillness/jeo-skills fails Gen Agent Trust Hub, one sampled skill in browserbase/skills fails the same auditor while the repository ships no LICENSE file, and tencentcloudbase/skills has a Snyk Fail inside an otherwise clean sample. Three repositories are archived, idle or barely starred and say so plainly: jaganpro/sf-skills is archived with a published successor, tigrisdata/skills has two stars, and xiaohongshu-skills has no licence at all.

Index-versus-tree drift is the other recurring fact. paulrberg/agent-skills indexes 97 listings against 43 directories, chrisbanes/skills 35 against 20, and jaganpro/sf-skills 46 against 37; each guide names which rows have nothing to install rather than describing behaviour it cannot read.

## Related

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)
