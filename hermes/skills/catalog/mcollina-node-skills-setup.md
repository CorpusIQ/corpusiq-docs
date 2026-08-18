---
title: "M. Collina Node Skills — Fastify & Node.js Agent Suite Setup"
description: "mcollina/skills — 12 skills, 52.4K installs: Fastify best practices, Node.js core, and TypeScript guidance from the Fastify lead and Node.js TSC member."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mcollina-node-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "agent skill", "skill setup", "nodejs", "fastify", "backend"]
---

# M. Collina Node Skills — Setup Guide

**Source:** [mcollina/skills](https://skills.sh/mcollina/skills)
**GitHub:** [mcollina/skills](https://github.com/mcollina/skills)
**Skills:** 12 skills · 52.4K total installs
**Category:** Node.js / Backend
**First Seen:** catalogued August 17, 2026 evening sweep (fastify-best-practices on skills.sh since January 31, 2026)
**Quality Tier:** 🟢 Production — authored by Matteo Collina (Fastify lead, Node.js TSC member); flagship passes all three security audits (3/3 Pass)

Matteo Collina's personal skill pack encodes two decades of Node.js core expertise: Fastify architecture patterns, Node.js core internals, and TypeScript discipline. fastify-best-practices at 36.4K installs is the canonical Fastify reference for coding agents, straight from the framework's own author.

---

## Installation

```bash
npx skills add mcollina/skills
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/mcollina/skills --skill fastify-best-practices
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Fastify or Node.js project** | For backend guidance; TypeScript optional for typescript-magician |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| fastify-best-practices | 36.4K | Plugins, route handlers, TypeScript type stripping, `inject` testing, validation, serialization, error handling |
| node | 4.8K | Core Node.js patterns and runtime guidance |
| typescript-magician | 2.1K | TypeScript type-level patterns and tricks |
| nodejs-core | 1.5K | Node.js core module internals |
| documentation | 1.4K | API and project documentation workflows |
| oauth | 1.1K | OAuth flows and implementation patterns |
| skill-optimizer | 1.1K | Refining agent skills themselves |
| init / octocat / linting-neostandard-eslint9 / snipgrapher / node-best-practices | ≤1K | Project init, GitHub automation, ESLint 9 flat config, snippet extraction, Node guidance |

The flagship includes a runnable minimal Fastify server scaffold with `logger: true` and covers the testing path via Fastify's built-in `inject` method — the author's own preferred patterns.

## Quick Start

1. Install: `npx skills add mcollina/skills`
2. Ask: "scaffold a Fastify service following fastify-best-practices"
3. The skill walks plugins, validation, and inject-based tests

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Backend authoring** | The canonical Fastify reference for any agent-built Node service |
| **Skill authoring** | skill-optimizer improves our own skill drafts before they ship |
| **Node.js depth** | nodejs-core fills gaps when agents work below framework level |

## Limitations / Verification

- Security audits on fastify-best-practices: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass — all three clean
- Publisher-page total verified (52.4K across 12 skills); repo at 1.9K GitHub stars
- Fastify-focused — best for backend and API work, not frontend
- Six of twelve skills are sub-1.1K installs — the suite's weight sits in fastify-best-practices and node

```bash
npx skills add mcollina/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
