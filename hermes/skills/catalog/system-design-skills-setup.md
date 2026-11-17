---
title: "System Design Skills - Reasoning-Driven Architecture"
description: "proyecto26/system-design-skills - 9.1K combined installs across 22 indexed listings: composable building blocks for reasoning about scalable systems."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/system-design-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "system design", "architecture", "scalability"]
---

# System Design Skills - Setup Guide

**Source:** [proyecto26/system-design-skills](https://www.skills.sh/proyecto26/system-design-skills) via skills.sh - 9.1K combined installs across 22 indexed listings; first seen Nov 16, 2026 (Nov 16 evening sweep)
**GitHub:** 134 stars, MIT license, `main` branch, last pushed 2026-10-27, skills under `skills/<name>/SKILL.md` with `references/` and per-provider files
**Category:** System design - divide-and-conquer building-block skills that reason instead of memorizing
**Quality Tier:** 🟢 Green - all 22 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk.

This repo packages system design as a divide-and-conquer skill set for Claude Code. An orchestrator skill runs a clarify, estimate, design, trade-offs, stress-test loop and routes into 20 building-block skills plus a diagram engine. Each block ships options, trade-offs, behavior under stress, and per-provider references for AWS, Azure, GCP, and Temporal. A `/design` command and a `system-design-orchestrator` agent drive the workflow, and the result lands as a scored design doc in `docs/design/`.

The set is arranged bottom-up into layers, from framing and edge traffic through services, state, async, correctness, ops, and growth. Every block follows one contract, and the repo ships an eval harness that measures whether the skills make a design measurably better.

## Installation

With the skills CLI:

```sh
npx skills add proyecto26/system-design-skills
```

Or as a Claude Code plugin:

```sh
/plugin marketplace add proyecto26/system-design-skills
/plugin install system-design-skills
```

By hand: clone the repo and copy `skills/<name>/` into your agent's skills directory, for example `.claude/skills/`.

```sh
git clone https://github.com/proyecto26/system-design-skills.git
cp -r system-design-skills/skills/* .claude/skills/
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| system-design | 470 | Orchestrator that runs the clarify, estimate, design, trade-offs, stress-test loop and routes to blocks. |
| architecture-diagram | 462 | Generate a self-contained dark-theme HTML and SVG diagram with PNG and PDF export. |
| service-decomposition | 452 | Split a system into services, or argue for a modular monolith, and wire discovery. |
| api-design | 448 | Design the interface: request and response shape, pagination, idempotency, versioning, REST vs gRPC vs GraphQL. |
| task-scheduling | 424 | Schedule, delay, and lease work to a worker pool, including distributed cron. |
| data-storage | 422 | Choose SQL or NoSQL and design the schema, keys, sharding, and replication. |
| resilience-failure | 421 | Circuit breakers, retries with backoff, failover, and graceful degradation. |
| caching | 420 | Read and write strategies, eviction, and thundering-herd or hot-key fixes. |
| requirements-scoping | 419 | Turn a vague prompt into functional, non-functional, and out-of-scope. |
| messaging-streaming | 414 | Queues, streams, pub/sub, delivery guarantees, dead letters, and backpressure. |
| observability | 410 | Metrics, logs, traces, SLOs, and alerting so failure is visible. |
| scaling-evolution | 407 | Diagnose the next bottleneck and the order-of-magnitude growth path. |
| consistency-coordination | 405 | CAP, quorums, consensus, distributed transactions, and consistency models. |
| dns | 403 | Steer traffic globally with health-checked failover and record choices. |
| load-balancing | 402 | L4 vs L7, balancing algorithms, health checks, and TLS termination. |

The remaining 7 indexed listings range from 314 to 399 installs.

## Why This Matters for Hermes Agents

This set turns system design from memorization into a repeatable reasoning loop, which is exactly what a Hermes agent needs when a user asks to design a service, a feed, or a rate limiter. The orchestrator forces the conversation through clarify, estimate, design, trade-offs, and stress-test, so a vague ask gets scoped and sized with numbers before any component is chosen. Each building block carries explicit options, trade-offs, and behavior under stress, so the agent can justify every decision instead of reciting a diagram. Provider references let the same skill answer for AWS, Azure, GCP, or Temporal by reading a managed-service mapping rather than inventing one. The diagram engine emits a self-contained HTML and SVG file, so the result is a deliverable, not just prose. A scored design doc lands in `docs/design/`, giving the run a concrete artifact to review. For a builder, each skill stays small and testable, and the eval harness shows the skills measurably improve design quality.

## Usage

| You say | What happens |
|---|---|
| `/design a URL shortener that handles billions of reads` | Runs the full loop: scope, size with numbers, compose blocks, weigh trade-offs, stress-test, and write the scored design doc. |
| `design WhatsApp-scale messaging` | Triggers the system-design orchestrator, which clarifies, estimates, and routes to the right blocks. |
| `SQL or NoSQL for a chat app, and how do I shard it?` | data-storage answers with the trade-off table, key design, and sharding strategy. |
| `How many servers and how much storage for 100M DAU?` | back-of-the-envelope returns QPS, storage, bandwidth, and server count. |
| `What caching strategy for a read-heavy feed?` | caching returns read and write strategies, eviction, and stampede fixes. |
| `Draw the architecture for what we just designed.` | architecture-diagram emits a self-contained dark-theme HTML and SVG diagram. |
| `We lost a region. What breaks and how do we degrade?` | resilience-failure and consistency-coordination cover SPOFs, failover, and degradation. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/proyecto26/system-design-skills/main/skills/system-design/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/proyecto26/system-design-skills/main/skills/api-design/SKILL.md | head -20
npx skills add proyecto26/system-design-skills
```

Each skill is one `SKILL.md` under `skills/<name>/`; confirm the path exists in the current tree before copying a specific skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| system-design | Pass | Pass | Pass |
| architecture-diagram | Pass | Pass | Pass |
| service-decomposition | Pass | Pass | Pass |
| api-design | Pass | Pass | Pass |
| task-scheduling | Pass | Pass | Pass |
| data-storage | Pass | Pass | Pass |
| resilience-failure | Pass | Pass | Pass |
| caching | Pass | Pass | Pass |
| requirements-scoping | Pass | Pass | Pass |
| messaging-streaming | Pass | Pass | Pass |
| observability | Pass | Pass | Pass |
| scaling-evolution | Pass | Pass | Pass |
| consistency-coordination | Pass | Pass | Pass |
| dns | Pass | Pass | Pass |
| load-balancing | Pass | Pass | Pass |
| distributed-search | Pass | Pass | Pass |
| content-delivery | Pass | Pass | Pass |
| distributed-logging | Pass | Pass | Pass |
| blob-store | Pass | Pass | Pass |
| sharded-counters | Pass | Pass | Pass |
| sequencer | Pass | Pass | Pass |
| back-of-the-envelope | Pass | Pass | Pass |

All 22 sampled skills pass all three scanners.

## Limitations

- Snapshot data, verified Nov 16, 2026: 9,078 combined installs across 22 indexed listings; 134 GitHub stars; MIT; last pushed 2026-10-27. Counts drift over time.
- Reasoning is subjective, not deterministic; only back-of-the-envelope ships a scriptable calculator with a golden fixture.
- Provider numbers drift; provider files mark quotas and limits to verify against current docs.
- Diagram PNG and PDF export loads two pinned CDN scripts; the rendering itself is fully offline.
- No live state: the plugin has no runtime, server, or API keys, only skills and one stdlib Python calculator.

## Related

- [C3SC0 Scaffold](/hermes/skills/catalog/c3sc0-scaffold-setup)
- [EventCatalog Skills](/hermes/skills/catalog/event-catalog-skills-setup)
- [Code Review Skill](/hermes/skills/catalog/code-review-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the orchestrator first and let it route; do not hand-pick building blocks for a full design.
- Pin numbers early with back-of-the-envelope so the arithmetic is checked, not done from memory.
- Run `python3 skills/back-of-the-envelope/scripts/test_botec.py` to confirm the calculator matches its golden fixture.
- Read docs/study-path.md to sequence the skills into a learn, drill, self-test path for interviews.
- Keep the whole set; the orchestrator and blocks reference each other by name.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
