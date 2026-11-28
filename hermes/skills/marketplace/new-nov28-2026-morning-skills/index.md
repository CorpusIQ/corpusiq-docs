---
title: "New Skills - November 28, 2026 Morning"
description: "Skills.sh sweep (Nov 28 morning): 14 guides, 46,693 combined installs across 574 listings, led by the Awesome Claude Code Toolkit and Civitai."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov28-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 28, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

The standing 20-query window returned 887 unique listings with 71 uncovered rows, 184 partial rows and no failed queries. Its largest uncovered row was 162 installs and its uncovered side carried 231 installs across 48 sources, so the window held no convertible cluster and a topic probe did the discovery work.

This fire probed 456 lanes across finance and ERP systems, HR and recruiting, project and identity tooling, observability and infrastructure, data platforms, marketing and CRM suites, commerce, logistics, property, education, clinical software, field service and construction, creative production and non-English markets: 10,124 unique rows with no failed queries, 4,375 distinct sources and 3,901 sources without a catalog page.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique listings in the standing 20-query window | 887 |
| Uncovered rows in the standing window | 71 |
| Partial rows in the standing window | 184 |
| Failed standing-window queries | 0 |
| Top uncovered standing-window row | 162 installs |
| Uncovered install mass in the standing window | 231 |
| Fresh topic lanes completed | 456 |
| Probe rows collected | 10,124 |
| Distinct sources in the probe | 4,375 |
| Uncovered sources after cross-reference | 3,901 |
| Candidates checked on GitHub | 20 |
| Candidates sized by exact source | 30 |
| Publishers published | 14 |
| Indexed listings behind those guides | 574 |
| Combined installs behind those guides | 46,693 |

## Published Guides

| Publisher | Combined | Listings | Tier |
|---|---:|---:|---|
| rohitg00/awesome-claude-code-toolkit | 8,026 | 39 | Green |
| civitai/civitai | 5,104 | 56 | Orange |
| nesszer/linear-cli | 5,087 | 38 | Yellow |
| stablyai/agent-slack | 5,053 | 1 | Yellow |
| salesforcecommercecloud/b2c-developer-tooling | 3,669 | 89 | Yellow |
| vercel-labs/emulate | 3,558 | 17 | Orange |
| cosmix/loom | 2,526 | 90 | Orange |
| sam6dvpte34/ecommerce-skill | 2,489 | 96 | Orange |
| data-goblin/power-bi-agentic-development | 2,395 | 38 | Orange |
| terminalskills/skills | 2,237 | 35 | Yellow |
| maystudios/claude-skills | 1,996 | 22 | Orange |
| weaverse/shopify-hydrogen-skills | 1,754 | 14 | Orange |
| growthbook/skills | 1,302 | 28 | Orange |
| chaiwithjai/davinci-resolve-claude-skills | 1,497 | 11 | Green |

Tiers: 2 Green, 4 Yellow, 8 Orange, each derived from its own sampled skills.sh verdict table. The Greens are rohitg00/awesome-claude-code-toolkit, where all 20 sampled skills pass Gen Agent Trust Hub, Socket and Snyk, and chaiwithjai/davinci-resolve-claude-skills, where all 11 sampled listings pass. The Oranges are Civitai (Fail cells on civitai-orchestration, postgres-query, mod-actions and retool-query), Vercel Emulate (a Snyk Fail on next), Loom (two Gen Agent Trust Hub Fails), the ecommerce catalog (16 of 20 sampled Fail Gen Agent Trust Hub), Power BI (Fails on pbir-cli and deneb-visuals), MayStudios (Fails on opencode, gemini-image-gen and hermes-tweet), Shopify Hydrogen (three Snyk Fails) and GrowthBook (Snyk Fails on gb-setup and experiments).

## What Shipped

The batch is led by the largest publisher the catalog has documented this week: rohitg00/awesome-claude-code-toolkit, 8,026 installs across 39 listings inside a toolkit that advertises 135 agents, 35 curated skills, 42 commands and 176+ plugins. Its indexed slice is engineering playbooks - React, Next.js, Python, Go, Rust and TypeScript patterns, Postgres and Redis optimization, security hardening, CI/CD, observability, MCP development and prompt engineering - and the guide states the drift between the README's plugin count and its sections.

Two vendor-platform works follow. Civitai's own repository carries 5,104 installs across 56 listings for skills that teach an agent to extend the Civitai platform: generation support, prompt enhancement, trainer models, Postgres queries, moderation actions and Retool dashboards. Salesforce's B2C Commerce tooling carries 3,669 across 89 listings for its CLI, VS Code extension, b2c-dx MCP server and storefront skills, including SLAS auth patterns, WebDAV deployment and eCDN.

Agent tooling fills the middle of the batch: the nesszer Linear CLI in Rust with 5,087 installs, Stably's Slack automation CLI at 5,053, Vercel Labs' API emulators at 3,558, Loom's Rust orchestrator with 2,526 installs across 90 listings, and GrowthBook's official feature-flag and experimentation skills.

Office, data and media work closes it: Power BI agentic development for PBIP and PBIR report authoring with TMDL and DAX validation hooks, a 1,146-directory Terminal Skills library against 35 indexed listings, MayStudios skills for Unreal Engine 5 and llama.cpp, Weaverse's Shopify Hydrogen storefront skills, a DaVinci Resolve editing suite, and an ecommerce scraper catalog.

## Method

Each publisher was sized with a strict source-equality filter over its full listing set, checked on the GitHub REST repository endpoint, and documented from its own README, SKILL.md files and skills.sh listing pages. Where the install index named a skill with no file in the current repository tree, the guide says so rather than assuming a file. Every guide states its install band, its licence, its sampled security verdicts and the drift between what skills.sh indexes and what the repository actually contains.

## Held Back

Six sized publishers were held with a measured reason each. vasilyu1983/ai-agents-public carries 19,636 installs across 96 listings but its repository now returns 404 while skills.sh still serves the source page, so there is no tree to document. scientiacapital/skills carries 5,998 across 96 listings and its organisation is public, but no repository of that name exists under it. sales-skills/sales returns zero rows under strict source equality and does not exist at that path. 404kidwiz/claude-supercode-skills stays unreachable. cold-iq/coldiq-s-gtm-skills was renamed to Cold-IQ/ColdIQ-s-GTM-Skills and now returns no rows under the indexed source string. beltsh/superpowers, whytryharder/superpowers and styleof/superpowers are forks of the inference.sh corpus already documented through the inference-sh and halt-catch-fire guides.

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
