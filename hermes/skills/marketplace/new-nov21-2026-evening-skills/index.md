---
title: "New Skills - November 21, 2026 Evening"
description: "Skills.sh sweep (Nov 21 evening): 12 guides, 130,498 combined installs across 291 listings, led by a go-to-market agent plugin and a PR review suite"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov21-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 21, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

The standing 20-query window returned 884 unique listings across 289 distinct sources with 76 uncovered rows and no failed queries. Its top row was 158 installs for `wwewtech/anti-slop-design`, followed by 150 for `danielteles/awesome-agent-skills` and 79 for `belsrc/skills`, so the window carried no convertible cluster and a fresh topic probe did the discovery work.

The probe ran 204 lanes across media production, finance and accounting, legal and compliance, clinical and lab work, security operations, data and platform engineering, testing, mobile, games, embedded and industrial systems, procurement, facilities, insurance, customer success, ecommerce, marketing operations, recruiting and developer tooling. Every shortlisted publisher was then sized through its own exact-source filter before ranking, because a probe row understates a large publisher by an order of magnitude.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 884 listings |
| Distinct sources in the standing window | 289 |
| Uncovered rows in the standing window | 76 |
| Top standing-window row | 158 (`wwewtech/anti-slop-design`) |
| Fresh topic lanes completed | 204 |
| Probe rows this fire | 14,936 rows |
| Distinct listings across both lanes | 14,419 |
| Distinct names across both lanes | 10,736 |
| Distinct sources across both lanes | 5,586 |
| Uncovered sources after cross-reference | 4,851 |
| Candidates sized by exact source | 45 |
| Publishers published | 12 |
| Indexed listings behind those guides | 291 |
| Combined installs behind those guides | 130,498 |

## Published Guides

| Publisher | Guides | Combined installs | Listings |
|---|---|---:|---:|
| [Revnu Plugin - Go-to-Market Agent Suite](/hermes/skills/catalog/revnu-plugin-setup) | 1 | 52,073 | 22 |
| [Kanon Repo - PR and Code Review Skills](/hermes/skills/catalog/kanon-repo-setup) | 1 | 26,320 | 10 |
| [Open Artifact - Agent-Native Artifacts Suite](/hermes/skills/catalog/open-artifact-setup) | 1 | 16,807 | 20 |
| [Claude Marketing - Full Marketing Department Skills](/hermes/skills/catalog/claude-marketing-setup) | 1 | 7,464 | 57 |
| [Boring Marketing Skills - Marketing Operator Suite](/hermes/skills/catalog/boring-marketing-skills-setup) | 1 | 6,406 | 32 |
| [VoiceStudio Skills - Local Voice Platform](/hermes/skills/catalog/voicestudio-setup) | 1 | 5,697 | 6 |
| [TinyFish Cookbook - Web Agent Recipe Suite](/hermes/skills/catalog/tinyfish-cookbook-setup) | 1 | 4,510 | 26 |
| [EthSkills - Ethereum Knowledge Base for Agents](/hermes/skills/catalog/ethskills-setup) | 1 | 3,304 | 26 |
| [MobileBuildMCP - iOS and macOS Build Suite](/hermes/skills/catalog/mobilebuildmcp-setup) | 1 | 2,777 | 24 |
| [KV0906 CC Skills - Design and Diagram Suite](/hermes/skills/catalog/kv0906-cc-skills-setup) | 1 | 2,271 | 32 |
| [SDK Generation Skills - Speakeasy Agent Suite](/hermes/skills/catalog/sdk-generation-skills-setup) | 1 | 1,482 | 26 |
| [Handsomestwei Patent Skills - Chinese Patent Suite](/hermes/skills/catalog/patent-disclosure-skill-setup) | 1 | 1,387 | 10 |

One publisher carries a Green tier with every sampled verdict passing, five carry Yellow with Warn cells and no Fails, and six carry Orange after a Fail cell in the sample: Boring Marketing (eight Fail cells, all Snyk), Revnu (five, all Snyk on the GEO and AEO audit skills), Open Artifact (four), EthSkills (three), Patent Skills (three) and KV0906 (one). Each guide states those cells in its own Security table, so a reader can see which skills failed before installing them.

Each guide also carries the exact install count for every skill above its threshold, the repository licence position, and the index-versus-tree drift where the two disagree. Revnu carries seven legacy `revnu-*` alias listings at six installs each; MobileBuildMCP is the renamed `xcodebuildmcp` project, so the older prefix still holds the higher counts and nine review skills exist twice; Claude Marketing lists 57 names against 56 directories because `gtm` is an index-only alias; TinyFish carries two index-only names; and VoiceStudio's OmniVoice engine ships a legacy file rather than a SKILL.md.

Held on evidence: three publishers that clear the exact-source filter have no reachable repository. `kimny1143/claude-code-template` (7,015 installs), `scientiacapital/skills` (5,998) and `shajith003/awesome-claude-skills` (4,820) all serve skills.sh pages while their GitHub URLs return 404 to both the REST API and the web, so no page was written for them. Single-listing publishers such as `heydamir/unslop` (4,304 installs on one listing) and `daniel-dan-conrad/ui-designer-skill` (3,670 on one listing) were held as thin rather than published as one-row guides.

## Related

- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)
- [November 21, 2026 Morning Sweep](/hermes/skills/marketplace/new-nov21-2026-morning-skills)
