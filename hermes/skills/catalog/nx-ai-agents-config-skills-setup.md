---
title: "Nx AI Agents Config — Monorepo Agent Skills Setup"
description: "nrwl/nx-ai-agents-config — 10 skills, 44.7K installs: official Nx workspace exploration, task running, and CI monitoring skills for agent coding assistants."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nx-ai-agents-config-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "agent skill", "skill setup", "monorepo", "nx", "devtooling"]
---

# Nx AI Agents Config — Setup Guide

**Source:** [nrwl/nx-ai-agents-config](https://skills.sh/nrwl/nx-ai-agents-config)
**GitHub:** [nrwl/nx-ai-agents-config](https://github.com/nrwl/nx-ai-agents-config)
**Skills:** 10 skills · 44.7K total installs
**Category:** Monorepo Tooling
**First Seen:** catalogued August 17, 2026 evening sweep (nx-workspace on skills.sh since January 27, 2026)
**Quality Tier:** 🟢 Production — official Nx org; flagship nx-workspace passes all three security audits (3/3 Pass)

The official Nx (nrwl) agent configuration gives coding agents read-only exploration of Nx monorepos, task orchestration, code generation, and CI monitoring. nx-workspace is the largest monorepo-navigation skill on the platform at 31.4K installs, and the read-only-by-design posture makes it safe to load in production workspaces.

---

## Installation

```bash
npx skills add nrwl/nx-ai-agents-config
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/nrwl/nx-ai-agents-config --skill nx-workspace
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Nx workspace** | An existing monorepo managed by Nx |
| **nx CLI** | Available globally or via `npx`/`pnpx`/`yarn` prefix |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| nx-workspace | 31.4K | Read-only workspace exploration: `nx show projects`, project filtering, dependency structure |
| nx-run-tasks | 2.6K | Task execution guidance across targets and projects |
| nx-generate | 2.5K | Code generation with generators and plugins |
| nx-plugins | 2.3K | Plugin configuration and extension patterns |
| link-workspace-packages | 2.2K | Local package linking within the workspace |
| nx-import | 2.0K | Importing external code and libraries |
| monitor-ci | 1.7K | CI pipeline monitoring and interpretation |
| polygraph / get-latest-ci / await-polygraph-ci | ≤3 | Nx Cloud Polygraph CI helpers (early content) |

The flagship skill's project-filtering syntax (explicit names, globs, `tag:` references, negation with `!project-name`) works across `nx run-many`, `nx release`, and `nx show projects` — one syntax for every workspace-scoped command.

## Quick Start

1. Install: `npx skills add nrwl/nx-ai-agents-config`
2. In the repo root, ask: "explore this Nx workspace and explain the project structure"
3. The skill runs `nx show projects` and walks the dependency graph read-only

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Monorepo navigation** | Read-only workspace maps reduce agent mistakes in multi-app repos |
| **CI diagnosis** | monitor-ci interprets Nx Cloud pipeline failures without manual log spelunking |
| **Task orchestration** | Filtering syntax carries over to `nx run-many` for targeted rebuilds |

## Limitations / Verification

- Security audits on nx-workspace: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass — all three clean
- Publisher-page total verified (44.7K across 10 skills); repo is young (27 GitHub stars as of the sweep)
- Read-only exploration only — the skill does not modify workspace configuration
- polygraph, get-latest-ci, and await-polygraph-ci are sub-5 installs — early content

```bash
npx skills add nrwl/nx-ai-agents-config   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
