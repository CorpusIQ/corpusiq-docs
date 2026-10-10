---
title: "Trigger.dev Skills - Background Jobs & Realtime Setup"
description: "Setup guide for triggerdotdev/skills - 14.6K combined installs. Official Trigger.dev skills for background jobs, tasks, realtime, and config."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/trigger-dev-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "background jobs", "durable execution", "realtime"]
---

# Trigger.dev Skills - Setup Guide

**Source:** [triggerdotdev/skills](https://www.skills.sh/triggerdotdev/skills) via skills.sh - 14.6K combined installs across 13 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [triggerdotdev/skills](https://github.com/triggerdotdev/skills) (33 stars, no LICENSE file; pushed 2026-09-01; branch `main`; skill directories at the repo root, e.g. `trigger-tasks/SKILL.md`)
**Category:** Background Jobs / Realtime Infrastructure
**Quality Tier:** 🟡 Beta - official Trigger.dev org; no LICENSE file in repo; small stars (33); all sampled verdicts Pass

Trigger.dev Skills is the official skills collection from Trigger.dev, a durable execution platform for AI agents, workflows, and background tasks. The skills cover the full arc of a Trigger.dev project: bootstrapping, backend task authoring, frontend realtime consumption, configuration and build extensions, AI agent patterns, and cost optimization.

The repo is an automatic mirror: the skills are maintained in the Trigger.dev monorepo and ship inside the `@trigger.dev/sdk` package, and a sync workflow republishes them here so they install through skills.sh. Start with `trigger-setup` to bootstrap a project, then move to `trigger-tasks` once the `/trigger` directory exists; `trigger-realtime` covers the consumer side for React and Next.js frontends.

---

## Installation

### skills.sh

```bash
# Install all skills
npx skills add triggerdotdev/skills

# Install a single skill
npx skills add triggerdotdev/skills --skill trigger-setup
```

### Already on Trigger.dev?

The same skills ship inside the SDK and can be installed straight into your coding agent:

```bash
npx trigger.dev@latest install-mcp
```

The repo is an automatic mirror - contribute skill changes in the Trigger.dev monorepo and they flow here automatically.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| trigger-tasks | 2,827 | Writing backend tasks with @trigger.dev/sdk: task() and schemaTask(), retries, waits, queues, concurrency, idempotency, and scheduled tasks |
| trigger-setup | 2,504 | Bootstrapping Trigger.dev into an existing project: CLI auth, SDK install, trigger.config.ts, a first task, and the dev server |
| trigger-realtime | 2,473 | Frontend realtime: subscribing to runs, React hooks, browser triggers, and scoped public tokens |
| trigger-config | 2,253 | trigger.config.ts configuration: build extensions for Prisma, Playwright, FFmpeg, and Python, plus deployment settings |
| trigger-agents | 2,218 | AI agent patterns: orchestration, parallelization, routing, evaluator-optimizer, and human-in-the-loop workflows |
| trigger-cost-savings | 1,957 | Cost optimization: static source analysis plus live run analysis via the Trigger.dev MCP tools |

The remaining 7 indexed listings range from 3 to 185 installs (trigger-authoring-chat-agent 185; trigger-chat-agent-advanced 181; tasks, setup, realtime, config, and agents at 3 each).

## Why This Matters for Hermes Agents

Background jobs and durable workflows are exactly the workloads agents get asked to build, and Trigger.dev's guarantees - retries with backoff, queues, long waits, realtime updates - are easy to use incorrectly without current SDK guidance. These skills put the platform's own best practices in front of the agent at the moment it writes task code, from `task()` and `schemaTask()` definitions to idempotency keys and scheduled tasks. The realtime skill covers the consumer half that agents routinely botch: subscribing to runs, streaming into React, and minting scoped public tokens instead of leaking secret keys. The agent-pattern skill packages orchestration, routing, evaluator-optimizer, and human-in-the-loop designs on top of durable execution, a cleaner substrate for multi-step agents than ad-hoc loops. The cost skill even audits spend with live run data through Trigger.dev's MCP tools. And because the skills ship inside the SDK, they track the version you actually deploy; the mirror here is just a distribution channel.

## Usage

| You say | What happens |
|---|---|
| Add Trigger.dev to my existing Next.js app | trigger-setup authenticates the CLI, installs the SDK, writes trigger.config.ts, and scaffolds /trigger with a first task |
| Write a durable task that retries with backoff | trigger-tasks covers task() and schemaTask(), retries, waits, queues, and idempotency keys |
| Show live run progress in my React UI | trigger-realtime wires useRealtimeRun and useRealtimeStream with scoped public tokens |
| Configure build extensions for Prisma and Playwright | trigger-config covers trigger.config.ts, build extensions, and deployment settings |
| Build a multi-step agent with approval gates | trigger-agents applies orchestration and human-in-the-loop patterns on durable execution |
| Reduce our Trigger.dev spend | trigger-cost-savings audits tasks, schedules, and runs with static analysis plus live run data |

## Verification

Confirm the install from the CLI or the skills directory:

```bash
npx skills list | grep trigger
```

The skills install as `trigger-*` directories at the repo root (`trigger-tasks/SKILL.md` layout). Before installing, review the exact instructions the agent will read: fetch the tasks skill file at `https://raw.githubusercontent.com/triggerdotdev/skills/main/trigger-tasks/SKILL.md` (verified reachable Oct 10, 2026).

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| trigger-tasks | Pass | Pass | Pass |
| trigger-setup | Pass | Pass | Pass |
| trigger-realtime | Pass | Pass | Pass |

## Limitations

- No LICENSE file in the repository; the skills ship inside the `@trigger.dev/sdk` package, but redistribution terms are not stated here - confirm with Trigger.dev before vendoring.
- The repo is an automatic mirror - edit changes in the Trigger.dev monorepo; content can change here without notice as the sync runs.
- The install index outruns the tree: trigger-config and trigger-agents carry install counts but have no matching directories in the current mirror, and five generic listings (tasks, setup, realtime, config, agents) sit at 3 installs each.
- Verdicts cover the three sampled skills only; the chat-agent skills and the cost skill are unaudited here.
- The small star count (33) reflects the mirror role rather than adoption - installs arrive through the SDK and skills.sh, not GitHub stars.

- Snapshot data, verified Oct 10, 2026: 14,613 combined installs across 13 indexed listings; 33 GitHub stars; no LICENSE file; last pushed 2026-09-01. Counts drift over time.

## Related

- [LangChain Agent Skills - Memory, RAG, Persistence & Middleware Setup](/hermes/skills/catalog/langchain-skills-setup) - agent-building counterparts for the LLM side
- [LaunchDarkly Agent Skills - Feature Flags & AgentControl Setup](/hermes/skills/catalog/launchdarkly-agent-skills-setup) - gate risky task rollouts behind flags
- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup) - observe the runs these skills produce
- [Netlify Agent Skills - Serverless Deployment for Hermes Setup](/hermes/skills/catalog/netlify-agent-skills-setup) - serverless deployment sibling
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Bootstrap first: run trigger-setup and get a dev server running before asking for task code, then switch to trigger-tasks.
- Verify against the live platform: tasks are easiest to test with the dev server, and the realtime hooks need a running run to observe.
- Keep secrets server-side; use auth.createPublicToken for frontend subscriptions instead of exposing the secret key.
- Ask for cost reviews periodically; trigger-cost-savings combines static analysis with live data from the Trigger.dev MCP tools.
- Remember the mirror rule: skill fixes belong in the Trigger.dev monorepo, and they flow back here automatically.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
