---
title: "Brian Lovin Agent Config — Design Engineering Suite Setup"
description: "brianlovin/agent-config — 19 skills, 33.6K installs: code simplification, UI slop removal (deslop), dependency cleanup (knip), and a full design-engineering workflow suite. 3/3 audit passes on the top skill."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/brianlovin-agent-config-setup/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "agent skill", "skill setup", "design engineering", "code quality", "deslop"]
---

# Brian Lovin Agent Config — Setup Guide

**Source:** [brianlovin/agent-config](https://skills.sh/brianlovin/agent-config)
**GitHub:** [brianlovin/agent-config](https://github.com/brianlovin/agent-config)
**Skills:** 19 skills · 33.6K total installs
**Category:** Design Engineering
**First Seen:** catalogued August 17, 2026 sweep (simplify on skills.sh since January 20, 2026)
**Quality Tier:** 🟢 Production — Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass (3/3 on top skill simplify)

Brian Lovin's agent-config is a design-engineering quality suite: simplification and deslopping of code and UI, dependency hygiene, and release workflow tooling. The flagship `simplify` preserves exact functionality while applying project-specific standards, and `deslop` targets UI slop — the visual-debt equivalent of text slop. Both map directly onto our code-quality and design-polish goals.

---

## Installation

```bash
npx skills add brianlovin/agent-config
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/brianlovin/agent-config --skill simplify
```

## Prerequisites

| Requirement | Details |
|---|---|
| **CLAUDE.md / project standards** | simplify reads project coding standards to apply refinements |
| **Node.js + npx** | For the skill installer |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| simplify | 13.5K | Code simplification preserving exact functionality; applies CLAUDE.md standards |
| deslop | 2.8K | UI slop removal — visual-debt cleanup |
| knip | 2.0K | Unused dependency and export detection |
| rams | 1.2K | — |
| find-skills | 1.1K | Skill discovery (separate implementation from vercel-labs' same-named skill) |
| agent-browser | 1.1K | Browser interaction (separate from vercel-labs/agent-browser) |
| favicon | 1.0K | Favicon generation |
| reclaude | 1.0K | Claude-session re-entry tooling |
| bun | 1.0K | Bun runtime guidance |
| react-doctor | 1.0K | React diagnostics |
| sentry | 990 | Sentry integration |
| skill-creator | 989 | Skill authoring scaffold |
| fix-sentry-issues | 985 | Sentry issue remediation |
| chrome-webstore-release-blueprint | 981 | Chrome Web Store release process |
| tdd | 975 | Test-driven development workflow |
| workflow | 965 | Task workflow management |
| playwriter | 916 | Playwright test authoring |
| grill-me | 884 | Self-interrogation before delivery |
| electron-wrapper | 110 | Electron app wrapper |

## Quick Start

1. Install: `npx skills add brianlovin/agent-config`
2. In a project, ask: "simplify the recently modified code per the project standards"
3. For UI debt: "run deslop on this component"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Code-quality pass** | simplify's preserve-function-refine-form doctrine matches our review standards |
| **UI polish** | deslop targets exactly the visual debt class we want removed before shipping |
| **Release hygiene** | chrome-webstore-release-blueprint and fix-sentry-issues cover the ship-and-monitor loop |

## Limitations / Verification

- Security audits on simplify: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass — clean on the flagship skill
- Publisher-page install counts verified (13.5K + 2.8K + 2.0K + 14 more = 33.6K); GitHub 360 stars on the repo
- Two skill names (find-skills, agent-browser) overlap vercel-labs' same-named skills — these are separate implementations from brianlovin
- Long-tail skills below 1K installs are early content; flagship value sits in simplify + deslop + knip

```bash
npx skills add brianlovin/agent-config   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
