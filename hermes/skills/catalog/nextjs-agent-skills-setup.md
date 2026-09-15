---
title: "Next.js Agent Skills - Official Vercel Skill Suite Setup"
description: "vercel/next.js - 5 first-party Agent Skills in the Next.js monorepo: next-dev-loop, cache-components adoption/optimizer, and partial-prefetching adoption/optimizer. 44.4K skills.sh installs. Setup guide for Hermes agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nextjs-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-11"
tags: ["hermes skill", "agent skill", "skill setup", "nextjs", "vercel", "web development", "react"]
---

# Next.js Agent Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/vercel/next.js) (5 skills, ~44.4K combined installs)
**GitHub:** [vercel/next.js](https://github.com/vercel/next.js) (142K⭐, 32K forks, MIT, canary default branch; skills live in the `skills/` directory of the monorepo)
**Category:** Web Development / Next.js
**First Seen:** May 22, 2026 on skills.sh (surfaced in the Sep 11, 2026 sweep)
**Quality Tier:** 🟢 Production (flagship skill all audits Pass; one skill carries a Socket Warn - see Limitations)

First-party agent skills shipped inside the Next.js repository itself. Vercel now publishes skills that let an agent perform Next.js migration and workflow tasks directly - adopt Cache Components, resolve the blocking routes they surface, run the `next dev` edit/verify loop, and adopt partial prefetching. This is the clearest signal to date that framework vendors are wiring agent skills into their flagship repositories, not sidecar repos.

---

## Installation

```bash
npx skills add vercel/next.js
```

The skills are also vendored in the monorepo at `skills/` (canary branch): `next-dev-loop`, `next-cache-components-adoption`, `next-cache-components-optimizer`, `next-partial-prefetching-adoption`, `next-partial-prefetching-optimizer` - copy any of them into an agent skills directory to use without the CLI:

```bash
git clone --depth 1 --branch canary https://github.com/vercel/next.js.git
cp -r next.js/skills/next-dev-loop ~/.hermes/skills/
```

## Skill Roster

| Skill | Installs | What It Does |
|---|---|---|
| `next-dev-loop` | 13.5K | The edit/verify rhythm during `next dev` - run the dev server, verify changes, iterate |
| `next-cache-components-adoption` | 13.1K | Turn on Cache Components in a Next.js app and resolve the blocking routes it surfaces |
| `next-cache-components-optimizer` | 12.4K | Optimize existing Cache Components usage after adoption |
| `next-partial-prefetching-adoption` | 5.4K | Enable partial prefetching and migrate routes to the new model |
| `next-partial-prefetching-optimizer` | 32 | Tune partial-prefetching configuration after adoption (newest, lowest installs) |

## Quick Start

1. Install the suite; no API keys or accounts required - skills operate on a local Next.js project
2. Ask for a migration - "adopt Cache Components in this app" - the agent reads the skill, walks the routes, and applies the changes
3. `next-dev-loop` guides the verify step: run the dev server and confirm the change before moving on

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs site maintenance** | The CorpusIQ docs and marketing site run on Next.js - cache-components adoption is directly actionable on our own stack |
| **Client web builds** | Agent-driven Next.js migrations and optimizations become repeatable deliverables for client work |
| **Reference architecture** | How a framework vendor structures official skills inside a 142K-star monorepo is a template for shipping skills with products |

## Limitations / Verification

- **Mixed audit picture:** `next-dev-loop` (top skill) renders Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass, but `next-cache-components-adoption` carries a Socket Warn. Tiered 🟢 on the flagship with the sibling Warn noted.
- **Monorepo skills, canary branch:** the skills live on the `canary` branch; skills.sh serves them from the repo directly, so installs track canary content.
- **Next.js-specific:** these skills are useless outside Next.js projects - they are framework migration tools, not general agent skills.

```bash
# Verify skill installed
ls ~/.hermes/skills/next-dev-loop/SKILL.md
```

## Security

| Audit | Verdict (next-dev-loop) | Verdict (next-cache-components-adoption) |
|---|---|---|
| Gen Agent Trust Hub | Pass | Pass |
| Socket | Pass | Warn |
| Snyk | Pass | Pass |

## Related

- [Vercel AI SDK Skills - TypeScript AI Development Setup](/docs/hermes/skills/catalog/vercel-ai-skills-setup)
- [Vercel Eve Agent Skills - Official Eve Agent Framework Skills Setup](/docs/hermes/skills/catalog/vercel-eve-agent-skills-setup)
- [Vercel Agent Skills - Official Vercel Collection Setup](/docs/hermes/skills/catalog/vercel-agent-skills-setup)
- [CorpusIQ - one MCP endpoint, all your business tools](https://corpusiq.io)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
