---
title: Feature-Sliced Design Skill — Frontend Architecture Setup
description: "feature-sliced/skills — feature-sliced-design (16.6K installs): the official FSD v2.1 methodology skill for layer-based frontend architecture; start simple, extract when needed. All three security audits pass."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/feature-sliced-design-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "frontend architecture", "feature-sliced", "fsd"]
---

# Feature-Sliced Design Skill — Setup Guide

**Source:** [feature-sliced/skills](https://skills.sh/feature-sliced/skills)
**GitHub:** [feature-sliced/skills](https://github.com/feature-sliced/skills) (80 stars)
**Skills:** 1 skill (`feature-sliced-design`) · 16.6K installs
**Category:** Frontend Architecture
**First Seen:** Mar 9, 2026 (catalogued August 15, 2026 midday sweep)
**Quality Tier:** 🟢 Production (all three security audits pass — Gen Agent Trust Hub, Socket, Snyk)

This is the official agent skill for Feature-Sliced Design (FSD) v2.1, the frontend architecture methodology documented at fsd.how. Its core principle is "start simple, extract when needed": place code in pages/ first, accept duplication, and extract to shared/app/features/entities layers only when code is actually reused and boundaries are focused.

---

## Installation

```bash
npx skills add feature-sliced/skills --skill feature-sliced-design
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Frontend project** | Any JS/TS app where structure decisions are being made |

## What It Provides

| Capability | Notes |
|---|---|
| Layer system | pages/, shared/, app/, features/, entities/ with clear extraction rules |
| Pragmatic doctrine | Not all layers required; start with shared, pages, app |
| Extraction criteria | Extract only on actual reuse, stable boundaries, focused responsibility |
| Anti-overengineering guard | Empty layer folders "just in case" are explicitly discouraged |

## Quick Start

1. `npx skills add feature-sliced/skills --skill feature-sliced-design`
2. Ask: "restructure this frontend project following FSD v2.1, starting from pages/ and extracting only what is genuinely shared"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Frontend architecture standard** | A consistent structure doctrine for agent-built frontends |
| **Refactor guidance** | Rules for when to extract vs leave duplication |
| **Client project scaffolding** | Architecture decisions on new builds |
| **Review rubric** | Check structural drift against FSD principles |

## Limitations / Verification

- Single-skill cluster; all three security audits pass (verified on skill page)
- Methodology skill — no runtime dependencies, but also no tooling; it is pure procedural knowledge
- Strictness is adjustable per project scale and team context

```bash
npx skills add feature-sliced/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
