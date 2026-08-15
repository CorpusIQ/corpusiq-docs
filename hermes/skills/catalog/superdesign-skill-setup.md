---
title: Superdesign Skill — Canvas Design & Inspiration Setup
description: "superdesigndev/superdesign-skill — superdesign (8.0K installs): find design inspirations and generate/iterate design drafts on an infinite canvas via the Superdesign CLI; repo analysis, live-site extraction, and graphic asset modes. Socket Warn, Snyk Fail."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/superdesign-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "design", "canvas", "ui design"]
---

# Superdesign Skill — Setup Guide

**Source:** [superdesigndev/superdesign-skill](https://skills.sh/superdesigndev/superdesign-skill)
**GitHub:** [superdesigndev/superdesign-skill](https://github.com/superdesigndev/superdesign-skill) (411 stars)
**Skills:** 1 skill (`superdesign`) · 8.0K installs
**Category:** UI Design & Creative Assets
**First Seen:** Jan 21, 2026 (catalogued August 15, 2026 midday sweep)
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub pass; Socket Warn and Snyk Fail on the skill page — named in Limitations)

Superdesign helps agents find design inspirations and styles, then generate and iterate design drafts on an infinite canvas. It runs through its own CLI and covers repo analysis (building .superdesign/init/ context), brand-new page design, design-system seeding, improvement requests, graphic assets (posters, covers, social creatives), and design from a live website via extract-website.

---

## Installation

```bash
npx skills add superdesigndev/superdesign-skill --skill superdesign
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Shell access** | The skill runs entirely through its CLI |

## What It Provides

| Capability | Notes |
|---|---|
| Design inspiration | Find inspirations and styles |
| Infinite canvas drafts | Generate and iterate drafts on-canvas |
| Repo analysis | Build UI context to .superdesign/init/ |
| Live-site extraction | extract-website pulls design DNA, tokens, and brand assets |
| Graphic mode | Posters, covers, social posts, thumbnails, ad creatives with platform dimensions |
| State resume | .superdesign/resume.json for durable work across sessions |

## Quick Start

1. Install: `npx skills add superdesigndev/superdesign-skill --skill superdesign`
2. Run the environment preflight, then ask: "help me design the onboarding page for our product"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Marketing assets** | Graphic mode for posters, covers, and social creatives |
| **Product UI drafts** | Design drafts for new pages and flows |
| **Design DNA extraction** | extract-website for competitor design reference |
| **Design system seeding** | Seed or refresh design systems from live sites |

## Limitations / Verification

- Socket Warn and Snyk Fail on the skill page — review flagged dependencies before production use
- Faithful pixel-recreation and editable on-canvas clones require the Superdesign app (superdesign.dev), not the CLI
- Install count verified on skill page: 8.0K

```bash
npx skills add superdesigndev/superdesign-skill   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
