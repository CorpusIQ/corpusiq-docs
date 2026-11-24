---
title: "New Skills - November 23, 2026 Evening"
description: "Skills.sh sweep (Nov 23 evening): 14 guides, 107,539 combined installs across 545 listings, led by Three.js Skills and Philtz JP Skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov23-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 23, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

The standing 20-query window returned 887 unique listings across 292 distinct sources with 75 uncovered rows, 206 partial rows and no failed queries. Its top row was 170 installs for `wwewtech/anti-slop-design`, the same name the three previous fires reported and declined, so the window carried no convertible cluster and a fresh topic probe did the discovery work again.

The probe ran 249 lanes organized by shape rather than by industry: agent workflow patterns (review, migration, refactor, debugging, spec to code), data and AI engineering (RAG, evaluation, vector search, fine-tuning, forecasting), platform ecosystems (Shopify, Salesforce, Notion, Slack, Kubernetes, database and warehouse tooling), locales and content languages, media production, and back-office process work. Every shortlisted publisher was then sized through its own exact-source filter before ranking, because a probe row understates a large publisher by an order of magnitude, and 77 exact sizes were used to order the batch.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 887 listings |
| Distinct sources in the standing window | 292 |
| Uncovered rows in the standing window | 75 |
| Partial rows in the standing window | 206 |
| Top standing-window row | 170 (`wwewtech/anti-slop-design`) |
| Fresh topic lanes completed | 249 |
| Probe rows this fire | 14,119 rows |
| Distinct names in the probe | 10,047 |
| Distinct sources in the probe | 5,992 |
| Merged unique rows (window plus probe) | 14,933 |
| Distinct sources after the merge | 6,137 |
| Uncovered sources after cross-reference | 5,467 |
| Candidates checked on GitHub | 80 |
| Candidates sized by exact source | 77 |
| Publishers published | 14 |
| Indexed listings behind those guides | 545 |
| Combined installs behind those guides | 107,539 |

## Published Guides

| Publisher | Guides | Combined installs | Listings |
|---|---|---:|---:|
| [Three.js Skills (Cesartevisual) - 3D Web Suite Setup](/hermes/skills/catalog/threejs-cesartevisual-setup) | 1 | 18,597 | 24 |
| [Philtz JP Skills - Japanese Business Dev Suite Setup](/hermes/skills/catalog/philtzjp-skills-setup) | 1 | 12,225 | 23 |
| [AI Design Skills - Agentic Product Design Suite Setup](/hermes/skills/catalog/owl-listener-ai-design-setup) | 1 | 10,890 | 44 |
| [Skill MCP Claude - Frontend Skills and Manager Setup](/hermes/skills/catalog/skill-mcp-claude-setup) | 1 | 7,637 | 77 |
| [Qinyan Academic Skills - Research Library Setup](/hermes/skills/catalog/qinyan-academic-setup) | 1 | 7,528 | 96 |
| [Meitu Skills - AI Image and Video Suite Setup](/hermes/skills/catalog/meitu-skills-setup) | 1 | 7,200 | 56 |
| [PlayCanvas Skills - 3D Web Engine Setup](/hermes/skills/catalog/playcanvas-skills-setup) | 1 | 6,550 | 18 |
| [WeChat Pay Skills - Chinese Payments Setup](/hermes/skills/catalog/wechatpay-skills-setup) | 1 | 6,262 | 7 |
| [OpenAI Plugins - Codex Plugin Examples Setup](/hermes/skills/catalog/openai-plugins-setup) | 1 | 6,211 | 52 |
| [Agentara Skills - AI Builder Skill Suite Setup](/hermes/skills/catalog/agentara-skills-setup) | 1 | 5,666 | 24 |
| [Yuyile Skills - AI Content Creator Skill Suite Setup](/hermes/skills/catalog/ttfake92-skills-setup) | 1 | 5,022 | 13 |
| [rar-skills (robsonrung) - Agent Engineering Skills Setup](/hermes/skills/catalog/rar-skills-setup) | 1 | 4,834 | 96 |
| [Tuist Agent Skills - Xcode Project Generation Suite Setup](/hermes/skills/catalog/tuist-agent-skills-setup) | 1 | 4,495 | 12 |
| [Supermemory Skills - Agent Memory API Suite Setup](/hermes/skills/catalog/supermemory-skills-setup) | 1 | 4,422 | 3 |

Three guides carry a Green tier with every sampled verdict passing: Three.js Skills (Cesartevisual), AI Design Skills (owl-listener) and Skill MCP Claude, each clean across its 20-skill sample. Seven carry Yellow with Warn cells and no Fails. Four carry Orange after at least one Fail cell: Qinyan Academic, Meitu, WeChat Pay and Yuyile.

Each guide states those cells in its own Security table, so a reader can see which skills failed before installing them. Each guide also carries the exact install count for every skill above its own threshold, the repository licence position, and the index-versus-tree drift where the two disagree.

Four guides carry a fact worth reading before installing. WeChat Pay moves money, so its Security section leads with that and names every Warn and Fail cell. Meitu's suite is a hosted Chinese AI media API, so its skills require a Meitu account rather than running locally. OpenAI Plugins is OpenAI's own examples repository with no LICENSE file, and the guide says so instead of guessing a licence. Supermemory ships no root README, so its guide sources the publisher description from the package README inside the repository.

Three publishers index far more names than their trees hold directories. Qinyan Academic catalogues 187 skills while skills.sh indexes 96 and the tree carries the installable subset; rar-skills indexes 96 listings against a much smaller current tree; Skill MCP Claude's 77 indexed listings are frontend and animation skill files even though its repository description advertises a Flask management interface for MCP skills, and its guide states that mismatch in the intro and the Limitations section. rar-skills does not ship a repository description at all, which its guide also states.

Held on evidence: three candidates returned 404 to the GitHub REST API and were dropped before any sizing spend. One further publisher, `obra/superpowers-skills` at 18,113 exact installs across 31 listings, was held because its repository has been archived since October 2025, skills.sh publishes no verdict cells for it, and every listing name carries spaces that the catalog's row format cannot represent. `docs.fish.audio` appeared again at 3,863 probe installs and remains a documentation host rather than a repository. Publishers at the 96-listing API cap carry counts that are floors, not totals.

## Related

- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)
- [November 23, 2026 Morning Sweep](/hermes/skills/marketplace/new-nov23-2026-morning-skills)
