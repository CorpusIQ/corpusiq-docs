---
title: "New Skills - November 27, 2026 Evening"
description: "Skills.sh sweep (Nov 27 evening): 11 guides, 4.65M combined installs across 454 listings, led by Anthropic Skills and K-Dense Scientific."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov27-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 27, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

The standing 20-query window returned 887 unique listings with 71 uncovered rows, 193 partial rows and no failed queries. Its largest uncovered row was 162 installs and its uncovered side carried 381 installs across 48 sources, so the window held no convertible cluster and a topic probe did the discovery work.

This fire probed 371 lanes across product ecosystems, platform and developer tooling, data and finance systems, industry verticals and regulated work: 18,960 unique rows with no failed queries, 6,858 distinct sources and 6,215 sources without a catalog page. Exact-source sizing then reset the order, as it does every fire: the probe showed nothing above 56,403 installs, while the published eleven carry 4.65 million between them.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique listings in the standing 20-query window | 887 |
| Uncovered rows in the standing window | 71 |
| Partial rows in the standing window | 193 |
| Failed standing-window queries | 0 |
| Top uncovered standing-window row | 162 installs |
| Uncovered install mass in the standing window | 381 |
| Fresh topic lanes completed | 371 |
| Probe rows collected | 18,960 |
| Distinct sources in the probe | 6,858 |
| Uncovered sources after cross-reference | 6,215 |
| Candidates checked on GitHub | 22 |
| Candidates sized by exact source | 13 |
| Publishers published | 11 |
| Indexed listings behind those guides | 454 |
| Combined installs behind those guides | 4,649,316 |

## Published Guides

| Publisher | Combined | Listings | Tier |
|---|---:|---:|---|
| anthropics/skills | 4,017,603 | 21 | Orange |
| k-dense-ai/scientific-agent-skills | 221,587 | 96 | Yellow |
| nvidia/skills | 192,633 | 95 | Orange |
| samber/cc-skills | 115,208 | 21 | Yellow |
| onewave-ai/claude-skills | 52,020 | 96 | Yellow |
| yizhiyanhua-ai/fireworks-tech-graph | 18,556 | 1 | Yellow |
| davepoon/buildwithclaude | 15,215 | 96 | Yellow |
| leonxlnx/earshot | 7,003 | 2 | Yellow |
| niazmorshed2007/reanimate | 4,117 | 2 | Yellow |
| agamm/claude-code-owasp | 2,911 | 1 | Green |
| scraperapi/scraperapi-skills | 2,463 | 23 | Orange |

Tiers: 1 Green, 7 Yellow, 3 Orange, each derived from its own sampled skills.sh verdict table. The Green is agamm/claude-code-owasp, where Gen Agent Trust Hub, Socket and Snyk all pass on the single sampled skill. Anthropic Skills is Orange on two Snyk failures in the document skills, NVIDIA is Orange on three Fail cells across omniverse-cad-to-simready, cuopt-developer and rag-perf, and ScraperAPI is Orange on six Snyk failures in its sample.

## What Shipped

Anthropic's own repository is the batch's headline and the largest publisher the catalog has documented: 4,017,603 installs across 21 listings, led by frontend-design at 1,178,349 and skill-creator at 444,827, with the docx, pdf, pptx and xlsx document skills that power Claude's document capabilities. The guide covers both Claude Code plugin sets, the plugin marketplace manifest, the 19 skill directories and the two listings whose names drift from the tree.

Science and hardware follow. The K-Dense AI corpus carries 221,587 installs across 96 listings in a flat band from 2,177 to 2,839, because one install pulls the validated set, and the README's 177-skill claim is stated against the 96 the index actually lists. NVIDIA's suite carries 192,633 across 95 listings with 501 skill directories in the tree, covering physical AI, robotics, simulation, CUDA acceleration and RAG blueprints.

The rest of the batch is craft and workflow: twenty-one standalone skills from samber/cc-skills, OneWave AI's business collection, a diagram generator that returns geometry-safe SVG and SVG-to-GIF motion, a 96-listing discovery hub, a sound-effects renderer for agents, an animation reverse-engineering skill, an OWASP review skill and ScraperAPI's vendor set.

## Method

Each publisher was sized with a strict source-equality filter over its full listing set, checked on the GitHub REST repository endpoint, and documented from its own README, SKILL.md files and skills.sh listing pages. Where the install index named a skill with no file in the current repository tree, the guide says so rather than assuming a file. Every guide states its install band, its licence, its sampled security verdicts and the drift between what skills.sh indexes and what the repository actually contains.

## Held Back

Two sized publishers were held with a measured reason each. langfuse/langfuse carries 2,570 installs across 42 listings but only one of those listings clears 500 installs, and the catalog already documents the separate langfuse/skills publisher. bradsjm/hassio-addons carries 4,591 across 7 listings that are Home Assistant addons rather than agent skills, last pushed in July.

Four further sources were held on evidence: beltsh/superpowers (56,403 in the probe) and whytryharder/superpowers (9,757) are forks carrying the inference.sh corpus already documented through the inference-sh and halt-catch-fire guides, 404kidwiz/claude-supercode-skills does not exist at that path on GitHub, and sales-skills/sales returns zero rows under strict source equality.

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
