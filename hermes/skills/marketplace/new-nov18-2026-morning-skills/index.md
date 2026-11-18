---
title: "New Skills - November 18, 2026 Morning"
description: "Skills.sh sweep (Nov 18 morning): 12 publisher guides for 98,166 combined installs across 651 indexed listings, led by Beagle, Han and the REA reverse-engineering suite"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov18-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 18, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

The standing 20-query window returned 884 unique listings with 78 NEW and 248 PARTIAL rows and no failed queries, and its top NEW row was 370 installs. The window has not carried a fire on install size for weeks, so a 216-lane topic probe across documents, data engineering, infrastructure, web frameworks, testing, security, marketing, sales, product, finance, HR, legal, operations, verticals, design and AI-platform lanes carried the discovery, and every shortlisted publisher was then sized through its own exact-source filter before ranking.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 884 listings |
| NEW (standing window) | 78 rows |
| PARTIAL (standing window) | 248 rows |
| Top NEW row in the standing window | 370 (`sjy051/music-composition`) |
| Fresh topic lanes completed | 216 |
| New probe rows this fire | 14,882 rows |
| Merged unique rows with the three previous fires | 41,183 rows |
| Distinct sources in the merged probe | 11,833 |
| Uncovered sources after cross-reference | 8,831 |
| Candidates sized by exact source | 63 |
| Publishers published | 12 |
| Indexed listings behind those guides | 651 |
| Combined installs behind those guides | 98,166 |

## Published Guides

| Publisher | Guides | Combined installs | Listings |
|---|---|---:|---:|
| [Beagle Skills - Agent Skill Marketplace Setup](/hermes/skills/catalog/beagle-setup) | 1 | 20,079 | 96 |
| [Han Skills - Claude Code Plugin Marketplace Setup](/hermes/skills/catalog/han-setup) | 1 | 15,036 | 96 |
| [REA Skill - Reverse Engineer Anything Suite Setup](/hermes/skills/catalog/rea-skill-setup) | 1 | 7,903 | 96 |
| [Roblox Game Dev Skills - Claude Code Suite Setup](/hermes/skills/catalog/roblox-game-skills-setup) | 1 | 7,791 | 40 |
| [Product Skills - UX Design & Product Management Setup](/hermes/skills/catalog/product-skills-setup) | 1 | 7,762 | 59 |
| [Rails Skills - Ruby on Rails Agent Suite Setup](/hermes/skills/catalog/rails-skills-setup) | 1 | 7,619 | 35 |
| [AgentKit Samples - Volcengine AgentKit Suite Setup](/hermes/skills/catalog/agentkit-samples-setup) | 1 | 6,363 | 96 |
| [Secure Agent Playbook - OWASP AI Agent Security Setup](/hermes/skills/catalog/secure-agent-playbook-setup) | 1 | 5,835 | 19 |
| [Craig Hewitt Skills - Founder, Sales and Creator Setup](/hermes/skills/catalog/craighewitt-skills-setup) | 1 | 5,765 | 64 |
| [SurrealDB Agent Skills - Official Database Skills Setup](/hermes/skills/catalog/surrealdb-skills-setup) | 1 | 4,947 | 10 |
| [Splunk Agent Skills - Splunk Operations Suite Setup](/hermes/skills/catalog/splunk-agent-skills-setup) | 1 | 4,650 | 32 |
| [Creative Strategy Skills - Paid Social Ads Suite Setup](/hermes/skills/catalog/creative-strategy-skills-setup) | 1 | 4,416 | 8 |

## Notes on this batch

- Exact-source sizing ran before ranking. The gap at the top of the band stayed wide: `thebushidocollective/han` read 2,041 installs from the probe and 15,036 across its 96 exact-source listings, `smartworldarafath/rea_skill` moved 1,837 to 7,903, and `ashexplained/roblox-skills` 2,088 to 7,791. Ranking on probe rows alone would have ordered the batch backwards.
- Two guides ship Green, five Yellow and five Orange. Two of the Orange guides carry a Fail on at least one auditor, and two are Orange because GitHub reports NOASSERTION rather than a standard licence. `thinkoodle/rails-skills` is Yellow for a missing LICENSE file rather than for any verdict.
- `bytedance/agentkit-samples` is ByteDance's own sample suite for the Volcengine AgentKit platform; most of its skills call Volcengine-hosted model endpoints for image, video, speech and music generation, and its guide says so rather than describing the skills as local.
- `splunk/splunk-agent-skills` installs as markdown, but almost every skill is only useful against a reachable Splunk instance or Splunk Cloud tenant, which its Limitations state.
- `ashexplained/roblox-skills` is the fourth independent Roblox publisher in this catalog, so its guide is titled and written to stay distinct from the existing pages, and its Related list leads with the closest neighbour.
- Held with the reason named: `jmsktm/claude-settings` (22,682 combined across 96 listings, the largest exact total sized this fire) because most of its listing names contain spaces or slashes that a table row cannot carry in the catalogue format; `dengineproblem/agents-monorepo` (8,633) and `eddiebe147/claude-settings` (5,395) and `mhagrelius/dotfiles` (2,618) all answer 404 on GitHub; `cold-iq/coldiq-s-gtm-skills` returns zero rows from its own exact-source filter. Sized and held on identity rather than size: `incept5/eve-skillpacks` (7,877) and `nextstage-brasil/skills` (7,733) publish no repository description and carry no stars, and `ascend/agent-skills` (7,646) last pushed in May 2026 under MulanPSL-2.0. `civitai/civitai` (4,948) is a platform monorepo of 21,482 files where the indexed skills are incidental, so it would need a tree-scoped guide rather than a publisher guide.

---
*<- [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) ->*
