---
title: "Inngest Skills — Durable Workflow Orchestration Setup"
description: "inngest/inngest-skills — 14 skills, 19.3K installs: event design, durable functions, steps, middleware, and agent workflows from the Inngest team."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/inngest-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-16"
tags: ["hermes skill", "agent skill", "skill setup", "workflow", "orchestration", "inngest"]
---

# Inngest Skills — Setup Guide

**Source:** [inngest/inngest-skills](https://skills.sh/inngest/inngest-skills)
**GitHub:** [inngest/inngest-skills](https://github.com/inngest/inngest-skills)
**Skills:** 14 skills · 19.3K total installs
**Category:** Workflow Orchestration
**First Seen:** catalogued August 16, 2026 sweep (inngest-events on skills.sh since February 17, 2026)
**Quality Tier:** 🟡 Trusted — official Inngest org; top skill carries a Snyk Warn (see Limitations)

Inngest's official skills teach agents durable execution: event schemas, idempotency, fan-out patterns, step-based retries, middleware, and flow control. For a multi-cron operation like CorpusIQ, durable functions with automatic retry semantics are the pattern layer between a naive background job and a reliable one.

---

## Installation

```bash
npx skills add inngest/inngest-skills
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/inngest/inngest-skills --skill inngest-events
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Inngest SDK** | `npm install inngest` in the project |
| **Inngest Dev Server** | `npx inngest-cli dev` for local development |

Note: these skills are TypeScript-focused. For Python or Go, the suite points to the Inngest documentation via `inngest.com/llms.txt`; core concepts carry across languages.

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| inngest-events | 3.2K | Event design, schemas, idempotency, fan-out |
| inngest-durable-functions | 3.2K | Function patterns with automatic retries |
| inngest-steps | 3.2K | Step-based execution and checkpointing |
| inngest-setup | 3.2K | Project configuration |
| inngest-middleware | 3.1K | Middleware patterns |
| inngest-flow-control | 1.0K | Concurrency and throttling |
| inngest-cli / inngest-api / inngest-api-cli | 337-357 | CLI and API reference |
| inngest-agents | 265 | Agent workflow patterns |
| inngest-brownfield-audit | 264 | Adopting Inngest in existing systems |
| inngest-v3-v4-migration | 245 | Migration playbook |
| inngest-agent-evals | 174 | Evaluation hooks for agent workflows |

## Quick Start

1. Install: `npx skills add inngest/inngest-skills`
2. Start with `inngest-setup` to scaffold the project, then `inngest-events` for event design
3. Ask: "convert this cron job into an Inngest durable function with retries and idempotency"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Cron hardening** | Our monitoring crons are fire-and-forget today; durable functions add retry and checkpoint semantics |
| **Multi-step pipelines** | Step-based execution maps onto our sweep → diff → draft → push pipelines |
| **Agent workflows** | inngest-agents and inngest-agent-evals address orchestrated multi-agent runs with eval hooks |
| **Idempotency discipline** | Event design rules transfer directly to our internal queue handling |

## Limitations / Verification

- Security audits on inngest-events: Gen Agent Trust Hub Pass, Socket Pass, **Snyk Warn** — trusted with the audit named
- Publisher-page install counts verified (19.3K total); GitHub 28 stars on the repo
- TypeScript-only guidance; Python/Go users get documentation pointers, not skills
- Eight of fourteen skills are sub-1K installs — the core five carry the suite

```bash
npx skills add inngest/inngest-skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
