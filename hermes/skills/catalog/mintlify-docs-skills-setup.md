---
title: "Mintlify Docs Skills — Documentation Platform Setup"
description: "mintlify/docs — 5 skills, 9.2K installs: Mintlify documentation authoring, nav updates, and API references from the Mintlify team."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mintlify-docs-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "documentation", "mintlify"]
---

# Mintlify Docs Skills — Setup Guide

**Source:** [mintlify/docs](https://skills.sh/mintlify/docs)
**GitHub:** [mintlify/docs](https://github.com/mintlify/docs)
**Skills:** 5 skills · 9.2K total installs
**Category:** Documentation
**First Seen:** catalogued August 15, 2026 evening sweep
**Quality Tier:** 🟢 Production (official org — Mintlify, the docs platform vendor)

Mintlify's official skills teach agents to author documentation, update navigation, and build API references for Mintlify-based docs sites. Useful wherever teams maintain public docs — the exact class of work the CorpusIQ knowledge base represents.

---

## Installation

```bash
npx skills add mintlify/docs
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Mintlify project** | A Mintlify-based docs site |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| mintlify | 9.1K | Core Mintlify authoring and configuration |
| doc-reader | 36 | Read and parse existing docs |
| doc-author | 27 | Author new documentation pages |
| update-nav | 21 | Update site navigation |
| mintlify-api | 5 | Mintlify API reference workflows |

## Quick Start

1. Install: `npx skills add mintlify/docs`
2. Start with the core `mintlify` skill — it carries 99% of the suite's installs
3. Ask: "author this new page and wire it into the docs navigation"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Client docs projects** | Authoring skills for clients running Mintlify sites |
| **Migration reference** | doc-author patterns when moving content between docs platforms |
| **Agent docs authoring** | A reference for how a docs vendor structures agent-side documentation skills |
| **Nav management** | update-nav workflow pattern for any hierarchical docs site |

## Limitations / Verification

- Publisher-page install counts verified; individual skill audit pages were not fetched for this multi-skill suite
- The core skill dominates: doc-reader, doc-author, update-nav, and mintlify-api show sub-100 installs — early content
- Requires a Mintlify project; not a general-purpose docs tool

```bash
npx skills add mintlify/docs   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
