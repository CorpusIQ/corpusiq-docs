---
title: Convex Agent Skills — 46-Skill Backend Platform Setup Guide for Hermes Agents
description: "get-convex/agent-skills — 46 skills, 756.9K combined installs. Quickstart, components, auth, performance audits, migrations, and launch-readiness for the Convex TypeScript backend platform."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/convex-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup", "backend"]
---

# Convex Agent Skills — Setup Guide

**Source:** [skills.sh](https://www.skills.sh/get-convex/agent-skills) (756.9K combined installs)
**GitHub:** [get-convex/agent-skills](https://github.com/get-convex/agent-skills)
**Category:** Backend Platform (BaaS)
**First Seen:** August 13, 2026 sweep
**Quality Tier:** 🟢 Production

Convex is the TypeScript-first backend platform (realtime database, auth, crons, billing) backed by a16z. This is the official agent skill set — the largest single-platform developer-experience cluster outside Microsoft Azure. Agents can stand up a full backend (schema, auth, crons, domains, billing, deploys) end to end without leaving the skill system.

---

## Installation

```bash
npx skills add get-convex/agent-skills
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| convex-quickstart | 101.0K | New project scaffold — schema, functions, deploy |
| convex-create-component | 100.5K | Reusable component packages |
| convex-performance-audit | 94.4K | Query and function performance review |
| convex-setup-auth | 94.0K | Authentication wiring (Clerk, Auth.js, custom) |
| convex-migration-helper | 93.9K | Schema migration planning and execution |
| convex | 77.1K | Platform-wide expert knowledge |
| convex-expert / convex-docs / convex-migrate / convex-optimize / convex-reviewer / convex-auth / convex-authz / convex-deploy-guard / convex-advisor / convex-migrate-rehearse / convex-design / convex-env / convex-crons / convex-agent / convex-insights / convex-verify / convex-add / convex-explain-app / convex-monitor / convex-cost / convex-launch-readiness / convex-test / convex-backup / convex-domains / convex-seed / convex-billing / convex-self-heal / convex-suggest / convex-improve-convex-plugin / convex-sentinel | 6.3K each | 29 expert sub-skills — one per lifecycle stage |
| convex-ship / convex-check-updates / convex-acquire-domain | 1.2K each | Release, updates, domain acquisition |
| convex-helpers-guide / function-creator / components-guide / schema-builder / mike-convex-thumbnail / migration-helper / auth-setup | 0.5K each | Assistant utilities |

## Prerequisites

- A Convex account (free tier available)
- Node.js 20+ for the CLI (`npx convex dev`)

## CorpusIQ Use Cases

- **Fast internal tool backends** — agent builds a CRUD backend with auth in one session via `convex-quickstart` + `convex-setup-auth`
- **Cron-driven automations** — `convex-crons` schedules recurring functions as a lighter alternative to serverless for small tools
- **Launch readiness** — `convex-launch-readiness` + `convex-deploy-guard` as pre-release gates for customer-facing demos

## Limitations / Verification

- Convex-specific: skills assume the Convex platform, not a generic SQL/Postgres backend
- Verify: `npx convex dev` boots a project and the dashboard shows a new deployment

## Related

- [Neon Agent Skills — Serverless Postgres Setup](/hermes/skills/catalog/neon-agent-skills-setup/)
- [Supabase Agent Skills — Backend Platform Setup](/hermes/skills/catalog/supabase/)
- [Firebase Agent Skills — Google Backend Setup](/hermes/skills/catalog/google-skills-setup/)
