---
title: "New Skills - November 23, 2026 Morning"
description: "Skills.sh sweep (Nov 23 morning): 14 guides, 123,514 combined installs across 577 listings, led by Claude Code Thinking Skills and Okou Skills"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov23-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 23, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

The standing 20-query window returned 885 unique listings across 290 distinct sources with 77 uncovered rows, 206 partial rows and no failed queries. Its top row was 161 installs for `wwewtech/anti-slop-design`, followed by 153 for `danielteles/awesome-agent-skills` and 153 for `designrique/ai-graphic-design-skill`, the same three names the previous fire reported and declined, so the window carried no convertible cluster and a fresh topic probe did the discovery work.

The probe ran 251 lanes across finance and accounting, healthcare and clinical work, industrial and field trades, logistics and supply chain, legal and compliance, government, education, media production, developer platforms and data engineering. Every shortlisted publisher was then sized through its own exact-source filter before ranking, because a probe row understates a large publisher by an order of magnitude, and 190 of those sizes were used to order the batch.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 885 listings |
| Distinct sources in the standing window | 290 |
| Uncovered rows in the standing window | 77 |
| Partial rows in the standing window | 206 |
| Top standing-window row | 161 (`wwewtech/anti-slop-design`) |
| Fresh topic lanes completed | 251 |
| Probe rows this fire | 14,642 rows |
| Distinct names in the probe | 11,506 |
| Distinct sources in the probe | 4,583 |
| Uncovered sources after cross-reference | 3,233 |
| Candidates checked on GitHub | 200 |
| Candidates sized by exact source | 190 |
| Publishers published | 14 |
| Indexed listings behind those guides | 577 |
| Combined installs behind those guides | 123,514 |

## Published Guides

| Publisher | Guides | Combined installs | Listings |
|---|---|---:|---:|
| [Claude Code Thinking Skills - Mental Models Setup](/hermes/skills/catalog/cc-thinking-skills-setup) | 1 | 21,137 | 39 |
| [Okou Skills - API and SaaS Connector Skills Setup](/hermes/skills/catalog/okou-skills-setup) | 1 | 16,328 | 96 |
| [ADLC Team Skills - Agent Development Life Cycle Setup](/hermes/skills/catalog/adlc-team-skills-setup) | 1 | 13,914 | 65 |
| [Letta Agent Skills - Stateful Agent Setup](/hermes/skills/catalog/letta-agent-skills-setup) | 1 | 8,594 | 94 |
| [DFINITY ICP Skills - Internet Computer Development Setup](/hermes/skills/catalog/dfinity-icp-skills-setup) | 1 | 8,377 | 58 |
| [Runway Agent Skills - Generative Media API Setup](/hermes/skills/catalog/runway-agent-skills-setup) | 1 | 7,889 | 38 |
| [Elastic Integration Skills - Search and Observability Setup](/hermes/skills/catalog/elastic-integration-skills-setup) | 1 | 7,348 | 15 |
| [HumanizerAI Agent Skills - Text Humanizing Setup](/hermes/skills/catalog/humanizerai-agent-skills-setup) | 1 | 7,334 | 7 |
| [MedSci Skills - Medical Research Agent Skills Setup](/hermes/skills/catalog/medsci-skills-setup) | 1 | 6,888 | 62 |
| [SAP Open UX Tools - Fiori Tooling Setup](/hermes/skills/catalog/sap-open-ux-tools-setup) | 1 | 5,591 | 15 |
| [Automattic Agent Skills - WordPress Development Setup](/hermes/skills/catalog/automattic-agent-skills-setup) | 1 | 5,344 | 13 |
| [Sinch Agent Skills - Communications API Setup](/hermes/skills/catalog/sinch-agent-skills-setup) | 1 | 5,273 | 28 |
| [MapLibre Agent Skills - Mapping Code Guidance Setup](/hermes/skills/catalog/maplibre-agent-skills-setup) | 1 | 5,179 | 13 |
| [CockroachDB Agent Skills - Database Operations Setup](/hermes/skills/catalog/cockroachdb-agent-skills-setup) | 1 | 4,318 | 34 |

Two guides carry a Green tier with every sampled verdict passing: Claude Code Thinking Skills, whose only non-Pass cell is a Socket Warn on red-team, and Automattic, clean across all 13 sampled skills. Five carry Yellow with Warn cells and no Fails. Seven carry Orange after at least one Fail cell in the sample: ADLC, DFINITY, Elastic, Letta, Okou, Runway and SAP.

Each guide states those cells in its own Security table, so a reader can see which skills failed before installing them. Each guide also carries the exact install count for every skill above its own threshold, the repository licence position, and the index-versus-tree drift where the two disagree. Automattic's repository is archived after the move to WordPress/agent-skills, and the guide says so in its GitHub line, intro and Limitations. Okou indexes 96 listings against a tree where most connector skills live in a separate repository, so its Use For cells are name-level and the page says which two rows have in-repo descriptions. CockroachDB's 33 in-table skills sit in a flat 84 to 162 band, because one install pulls a family rather than a single skill. DFINITY and Letta both index more names than the current tree holds directories, and both pages carry the drift explicitly.

Held on evidence: ten candidates that served skills.sh listings had GitHub repositories returning 404 to the REST API, so no page was written for them: `astoeckli/agent-skills`, `letslego/insurance-agent-skills`, `alongor666/alongor666-skills`, `pandaallin/ubos_final`, `cleanexpo/ato`, `natuleadan/skills`, `endigo/claude-skills`, `scientiacapital/skills`, `danhvb/my-ba-skills` and `pointdotcom-marketing/marketing-skills`. One high probe row, `docs.fish.audio` at 1,778 installs, resolved to a documentation host rather than a repository, so it was not sized. Publishers at the 96-listing API cap carry counts that are floors, not totals.

## Related

- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)
- [November 22, 2026 Morning Sweep](/hermes/skills/marketplace/new-nov22-2026-morning-skills)
