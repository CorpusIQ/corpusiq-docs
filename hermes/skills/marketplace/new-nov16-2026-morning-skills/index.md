---
title: "New Skills - November 16, 2026 Morning"
description: "Skills.sh sweep (Nov 16 morning): 14 publisher guides for 272,882 combined installs across 729 indexed listings, led by Blender, Basilic and Pedro Nauck"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov16-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 16, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. This is the largest batch in combined installs so far, and the probe is what produced it: three of the top five publishers read less than a sixth of their real size in probe rows.

The standing 20-query window stayed quiet, returning 884 listings, 80 NEW and 250 PARTIAL rows with a top NEW row of 355 installs. That window has been a poor guide in both directions, so the topic probe carried the fire: 313 lanes at 2.7-second pacing returned 20,392 rows across 4,904 distinct sources with zero failed queries. Cross-referencing against the docs tree left 3,247 uncovered sources, and the top 48 of them were sized through their own source filter before anything was ranked.

That sizing step is the whole story of this batch. `arjun988/blender-skills` read 7,716 from probe rows and 50,714 from its own source across 93 listings. `blockmatic-icebox/basilic-skills` read 3,716 and sized to 36,217. `pedronauck/skills` read 3,674 and sized to 32,017. `syncfusion/maui-ui-components-skills` read 2,785 and sized to 16,766. Ranking by the probe would have ordered this batch almost backwards.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 884 listings / 832 names / 290 sources |
| NEW (standing window) | 80 rows |
| PARTIAL (standing window) | 250 rows |
| Top NEW row in the standing window | 355 (`sjy051/music-composition` / `music-composition`) |
| Topic lanes completed | 313 |
| Probe rows / distinct sources | 20,392 / 4,904 |
| Failed queries | 0 |
| Uncovered sources after cross-reference | 3,247 |
| Candidates sized by exact source | 48 |
| Guides published this fire | 14 |
| Combined installs documented | 272,882 |
| Indexed listings covered | 729 |
| Tier mix | 5 Green, 7 Yellow, 2 Orange |

## Published guides

| Guide | Source | Combined | Listings | Tier |
|---|---|---|--:|--:|
| [Blender Skills - MCP Production Pipeline](/hermes/skills/catalog/blender-skills-setup) | arjun988/blender-skills | 50,725 | 93 | Green |
| [Basilic Skills - Slash Playbooks for Coding Agents](/hermes/skills/catalog/basilic-skills-setup) | blockmatic-icebox/basilic-skills | 36,217 | 96 | Yellow |
| [Pedro Nauck Skills - Curated Agent Skill Library](/hermes/skills/catalog/pedronauck-skills-setup) | pedronauck/skills | 32,017 | 96 | Yellow |
| [Tauri Skills - Desktop and Mobile App Development](/hermes/skills/catalog/tauri-skills-setup) | full-stack-skills/tauri-skills | 31,071 | 56 | Yellow |
| [Roblox Agent Skills - Production Roblox Skill Suite](/hermes/skills/catalog/roblox-agent-skills-setup) | el4cteo/roblox-skills | 25,473 | 23 | Yellow |
| [GrepAI Skills - Semantic Code Search and Call Graphs](/hermes/skills/catalog/grepai-skills-setup) | yoanbernabeu/grepai-skills | 19,366 | 27 | Green |
| [Syncfusion MAUI UI Skills - Component Suite Setup](/hermes/skills/catalog/syncfusion-maui-skills-setup) | syncfusion/maui-ui-components-skills | 16,766 | 81 | Yellow |
| [Spark CLI Skills - Email, Calendar and Meetings for Agents](/hermes/skills/catalog/spark-cli-skills-setup) | readdle/spark-cli-skills | 11,880 | 34 | Yellow |
| [Spree Agent Skills - Spree 6 Commerce Skill Suite](/hermes/skills/catalog/spree-agent-skills-setup) | spree/agent-skills | 10,079 | 42 | Orange |
| [Webhook Skills - Provider Webhook Receivers and Verification](/hermes/skills/catalog/webhook-skills-setup) | hookdeck/webhook-skills | 10,021 | 96 | Orange |
| [Three.js Skills - 3D Graphics Toolkit for Agents](/hermes/skills/catalog/threejs-skills-setup) | full-stack-skills/threejs-skills | 9,207 | 22 | Green |
| [Founder Skills - Validate Your Business Before Launch](/hermes/skills/catalog/founder-skill-setup) | jakeschincariol/founder-skill | 7,893 | 11 | Yellow |
| [Screenwriting Skills - Screenwriting and Dramaturgy Suite](/hermes/skills/catalog/screenwriting-skills-setup) | jtydhr88/screenwriting-skills | 7,716 | 26 | Green |
| [Koru Works Skills - Document-Driven Coding Workflow](/hermes/skills/catalog/koruworks-skills-setup) | koruworks/skills | 4,451 | 26 | Green |

## Why this batch is weighted toward developer workflow

Nine of the fourteen are engineering collections: coding playbooks, Tauri and Three.js, semantic code search, webhook receivers, a commerce suite and a document-driven feature loop. Three are business-facing (founder validation, screenwriting, email and calendar). Two are platform UI suites (Blender and Syncfusion MAUI). Nothing here duplicates an existing catalog page: every source was checked against the exact source string, the owner name and its distinctive skill names before drafting.

Three publishers carry a scanner Fail or a wide Warn spread and are tiered down accordingly. `spree/agent-skills` has one Snyk Fail (spree-payments) and two cells that returned no verdict, and `hookdeck/webhook-skills` has one Snyk Fail (webhook-handler-patterns); both pages lead with the Fail rather than burying it. `readdle/spark-cli-skills` carries Warns on eleven of twelve sampled skills with no Fail.

## Held, with reasons

- `ashexplained/roblox-skills` (7,504 / 40 listings): a fourth Roblox publisher with no name overlap against the three documented sets, held so one fire does not publish two Roblox pages.
- `okou-ai/okou-skills` (16,325 / 96 listings): the index still outruns the tree and most top rows do not ground to a directory.
- `senclaw-cdn.italent.cn` (33,735 / 14 listings): the source string is a CDN host, not a repository, so there is nothing to verify or install from.
- `sales-skills/sales` (2,836 probe rows): the exact-source filter returns zero rows and GitHub returns 404, so the publisher is dangling.

## Method note

The probe ran through a new `scripts/sweep_curl.py` runner, which shells out to `curl` and paces at 2.7 seconds. Python's own client against the same endpoint had averaged about a minute per query in an earlier fire; through `curl` the same 313 lanes finished in roughly twenty-two minutes. Packs were built by `scripts/build_skill_pack.py`, which dumps exact-source rows, the full repository tree, per-skill frontmatter descriptions and the skills.sh verdict cells for one source in a single call.

---
