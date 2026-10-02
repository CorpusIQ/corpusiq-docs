---
title: "TanStack Skills - React Server State & Router Suite Setup"
description: "tanstack-skills/tanstack-skills - 14 skills, 36.6K combined installs. Community (unofficial) agent skills for the TanStack ecosystem: Query, Table, Router, Form, Start, Virtual, Store, and the new TanStack DB/AI tools."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tanstack-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "react"]
---

# TanStack Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/tanstack-skills/tanstack-skills) (36.6K combined installs)
**GitHub:** [tanstack-skills/tanstack-skills](https://github.com/tanstack-skills/tanstack-skills) (31⭐, MIT)
**Category:** Frontend Development (React)
**First Seen:** February 21, 2026 (skills.sh)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass) - note: community collection, NOT the official TanStack org

A community-maintained (explicitly UNOFFICIAL) skill cluster for the TanStack ecosystem, one of the most widely adopted React library families. Each skill encodes current v5-era API knowledge: `tanstack-query` covers server-state management (caching, background refetching, stale-while-revalidate, pagination, infinite scroll, optimistic updates), `tanstack-router` covers type-safe routing, `tanstack-table` covers headless data tables. Also covers the newer entries - Pacer, Store, DB, and TanStack AI - that official docs haven't fully codified for agents.

---

## Installation

```bash
npx skills add tanstack-skills/tanstack-skills --skill tanstack-query
npx skills add tanstack-skills/tanstack-skills --skill tanstack-router
npx skills add tanstack-skills/tanstack-skills --skill tanstack-table
npx skills add tanstack-skills/tanstack-skills --skill tanstack-form
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| tanstack-query | 7.2K | Server-state management: caching, refetching, SWR, optimistic updates |
| tanstack-table | 4.3K | Headless data-table construction (sorting, filtering, pagination) |
| tanstack-router | 3.8K | Type-safe file-based routing |
| tanstack-pacer | 3.5K | Rate-limiting and pacer utilities |
| tanstack-form | 3.5K | Form state and validation |
| tanstack-start | 3.1K | Full-stack React framework |
| tanstack-virtual | 2.0K | Virtualized lists for large datasets |
| tanstack-devtools | 1.8K | Debugging and devtools integration |
| tanstack-store | 1.4K | Framework-agnostic reactive store |
| tanstack-db | 1.3K | Client-side reactive database |
| tanstack-cli | 1.3K | Project scaffolding and CLI workflows |
| tanstack-ai | 1.2K | AI feature integration patterns |
| tanstack-config | 1.2K | Shared configuration patterns |
| tanstack-ranger | 1.0K | Slider/range components |

## Prerequisites

- React (or framework-agnostic for store/ranger) project
- Node.js; each skill assumes current v5 packages (`npm install @tanstack/react-query`, etc.)

## CorpusIQ Use Cases

- **Dashboard data layers** - tanstack-query's caching/SWR patterns are the reference model for CorpusIQ's data-heavy dashboard connectors
- **Large-result rendering** - tanstack-virtual + tanstack-table are the right toolkit for browsing big operator datasets (transactions, contacts, product catalogs)
- **Type-safe product surface** - tanstack-router's type-safe route contracts reduce the class of routing bugs in CorpusIQ's web app

## Limitations / Verification

- UNOFFICIAL community collection - skill content tracks upstream TanStack docs but lags breaking changes; cross-check against official docs for critical decisions
- 31⭐ repo vs 36.6K installs: adoption via skills.sh, not GitHub
- Verify install: `npx skills list | grep tanstack`

## Security

[Gen Agent Trust Hub: Pass](https://www.skills.sh/tanstack-skills/tanstack-skills/tanstack-query/security/agent-trust-hub) · [Socket: Pass](https://www.skills.sh/tanstack-skills/tanstack-skills/tanstack-query/security/socket) · [Snyk: Pass](https://www.skills.sh/tanstack-skills/tanstack-skills/tanstack-query/security/snyk)

## Related

- [VueJS AI Skills Setup](/hermes/skills/catalog/vuejs-ai-skills-setup)
- [Angular Skills Setup](/hermes/skills/catalog/angular-skills-setup)
- [Tailwind 4 Docs Setup](/hermes/skills/catalog/tailwind-4-docs-skill-setup)
