---
title: "New Skills - November 19, 2026 Evening"
description: "Skills.sh sweep (Nov 19 evening): 14 guides for 101,600 combined installs across 586 listings, led by a Suno album pipeline and a 96-skill engineering library"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov19-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 19, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

The standing 20-query window returned 886 unique listings with 109 uncovered rows and no failed queries. Its top rows were 2,148 installs for `0xdesign/design-plugin` and 1,971 for `404kidwiz/claude-supercode-skills`, and both publishers are unreachable on GitHub, so the window itself produced no convertible cluster. A 210-lane topic probe across business verticals, industry service lines and developer platform work carried the discovery, and every shortlisted publisher was sized through its own exact-source filter before ranking.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 886 listings |
| Distinct sources in the standing window | 291 |
| Uncovered sources in the standing window | 73 |
| Top standing-window row | 2,148 (`0xdesign/design-plugin`, no reachable repository) |
| Fresh topic lanes completed | 210 |
| Probe rows this fire | 10,311 rows |
| Distinct names in the probe | 8,436 |
| Distinct sources in the probe | 3,322 |
| Uncovered sources after cross-reference | 2,229 |
| Candidates sized by exact source | 40 |
| Publishers published | 14 |
| Indexed listings behind those guides | 586 |
| Combined installs behind those guides | 101,600 |

## Published Guides

| Publisher | Guides | Combined installs | Listings |
|---|---|---:|---:|
| [Music Production Skills - Songwriting, Lyrics and Release](/hermes/skills/catalog/claude-ai-music-skills-setup) | 1 | 14,649 | 63 |
| [Engineering Agent Skills - Product, QA and Governance](/hermes/skills/catalog/magnus919-agent-skills-setup) | 1 | 13,218 | 96 |
| [Academic Research Skills - Citations, Reviews and Writing](/hermes/skills/catalog/kalarislabs-research-agent-skills-setup) | 1 | 12,160 | 93 |
| [MotherDuck Skills - Analytics Apps on DuckDB Data](/hermes/skills/catalog/motherduckdb-agent-skills-setup) | 1 | 9,095 | 39 |
| [iPhone Duo Skills - Foldable iOS Dev Setup Guide](/hermes/skills/catalog/iphone-duo-skills-setup) | 1 | 9,048 | 11 |
| [Research-Claw Research Plugins - Academic Skills Setup Guide](/hermes/skills/catalog/wentorai-research-plugins-setup) | 1 | 8,238 | 96 |
| [Flutter and Dart Skills - Architecture and Testing](/hermes/skills/catalog/dhruvanbhalara-skills-setup) | 1 | 6,607 | 63 |
| [Frontend Design Skills - UI Composition and UX Review](/hermes/skills/catalog/hueyexe-frontend-agent-skills-setup) | 1 | 6,111 | 9 |
| [Bagisto Agent Skills - Official Ecommerce Platform Setup](/hermes/skills/catalog/bagisto-agent-skills-setup) | 1 | 5,424 | 30 |
| [NestJS Skills - Seven Agent Skills for NestJS Setup](/hermes/skills/catalog/amirtaherkhani-nestjs-skills-setup) | 1 | 3,602 | 7 |
| [Valyu Search Skills - Web Search and Research APIs](/hermes/skills/catalog/valyuai-skills-setup) | 1 | 3,406 | 1 |
| [GoFrame Skills - Go Framework Development Setup](/hermes/skills/catalog/gogf-skills-setup) | 1 | 3,376 | 1 |
| [PMA Skills - Project Lifecycle and Code Review Setup](/hermes/skills/catalog/zzci-skills-setup) | 1 | 3,368 | 16 |
| [Agile Delivery Skills - Sprint Planning and Delivery Setup](/hermes/skills/catalog/djalmajr-skills-setup) | 1 | 3,298 | 61 |

## What Shipped

Music production arrives as a full pipeline rather than a prompt library: bitwize-music-studio's plugin runs a conversation into concept, lyrics with prosody and plagiarism checks, Suno style prompts, per-stem mastering, artwork and release preparation, with 72 genre directories and a source-verification gate for documentary albums.

Two engineering libraries anchor the middle of the batch. magnus919/agent-skills covers software design, product and UX review, QA and the governance questions multi-agent work raises, and kalarislabs/research-agent-skills gives a general agent the methods of a careful scientist, from literature search through citation verification to reviewer rebuttals. MotherDuck's own skills cover analytics apps on serverless DuckDB, and two academic libraries shipped side by side: Research-Claw's 400-plus-skill plugin set for scholarly databases and methods, and KalarisLabs' research suite.

Mobile and frontend work are covered by the iPhone Duo suite for Apple's first foldable, a 43-skill Flutter and Dart collection, and hueyexe's nine design skills that target the look agents usually ship. The platform guides are the official ones: Bagisto for its Laravel ecommerce platform, NestJS for architecture through audit, GoFrame v2 for accurate Go, Valyu for search and deep-research APIs, PMA for a complexity-tiered delivery lifecycle and djalmajr for agile ceremonies from intake to retrospective.

## Held On Evidence

| Source | Exact size | Reason |
|---|---:|---|
| equinor/fusion-skills | 40,671 across 38 listings | `github.com/equinor/fusion-skills` returns 404 and no fusion-skills repository exists under the equinor org, so the skill bodies cannot be read or verified |
| 404kidwiz/claude-supercode-skills | 20,036 across 96 listings | the publisher account is live with 26 public repositories and none of them is this one, so the listing survives on skills.sh with no repository behind it |
| sales-skills/sales | 0 from the exact-source filter | the search index carries the source in probe rows and returns nothing under strict source equality, and the repository is unreachable |
| developer.paddle.com | 2,678 across 1 listing | a documentation host, not a repository, so there is no tree or skill body to ground a guide in |

## Method

The standing window ran first, then the probe as three foreground slices of 70 lanes at 2.7 second pacing, writing per-lane JSONL so a kill loses nothing. Every candidate was then sized through its own exact-source filter, because the probe reads several times short at the top of the band: the week's largest exact sizes here sit an order of magnitude above their probe rows. Sixteen sampled security verdicts per publisher fed the quality tiers.

## Next Queue

Publishers already sized and still undocumented, led by peterhdd/agent-skills (2,885 across 19 listings), schwepps/skills (2,874, 8), nodeops-app/skills (2,688, 8), skills-il/localization (2,572, 16) and sergebulaev/instagram-skills (2,369, 10), then kv0906/cc-skills, imbad0202/academic-research-skills-codex, arpitg1304/robotics-agent-skills, 0xdesign/design-plugin (once a repository can be found), exploreomni/omni-agent-skills and branded-dropshipping/skills.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
