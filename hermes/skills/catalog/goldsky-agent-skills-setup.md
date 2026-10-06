---
title: "Goldsky Agent Skills - Blockchain Data Pipeline Setup"
description: "Setup guide for goldsky-io/goldsky-agent: 19 official Goldsky skills for AI agents building, deploying, and debugging blockchain data pipelines."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/goldsky-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-05"
tags: ["hermes skill", "agent skill", "skill setup", "blockchain", "data pipeline", "goldsky"]
---

# Goldsky Agent Skills - Setup Guide

**Source:** [goldsky-io/goldsky-agent](https://github.com/goldsky-io/goldsky-agent) (12⭐, 1 fork, MIT LICENSE; very active - pushed Oct 5, 2026)
**Skill family:** `goldsky-io/goldsky-agent` (19 SKILL.md files in-repo; 29 indexed listings)
**Combined Installs:** ~19,805 across indexed listings (Oct 5, 2026 snapshot)
**Category:** Developer Platform / Blockchain Data
**Quality Tier:** 🟡 Beta (official Goldsky publisher, MIT LICENSE in-repo, active development; low community stars and sampled Socket/Snyk verdicts mixed - verified Oct 5, 2026)

The official Goldsky plugin for AI agents, covering the full product surface: skills, agents, commands, and hooks for building blockchain data pipelines from natural-language prompts. Coverage spans **Turbo** pipelines (real-time chain data into Postgres, ClickHouse, Kafka, S3, Pub/Sub and more), **Mirror** (legacy streaming; the only product with subgraph entity sources), **Subgraphs** (hosted GraphQL APIs over onchain data), **Compose** (offchain-to-onchain TypeScript apps: oracles, keepers, circuit breakers, compliance gates), **Edge** (managed EVM RPC) and **Boost** (free caching CDN in front of an RPC provider you already pay for), plus **Feeds** (one wallet's balances and transfers over REST), a 130+ chain dataset reference, pipeline sink secrets management, and CLI auth setup. Pairs builder and doctor skills per product, with a cross-product onchain-automation router that maps a detect-decide-execute goal onto the right product combination.

---

## Installation

```bash
# Full suite (all 19 skills)
npx skills add goldsky-io/goldsky-agent

# Or specify the agent host directly
npx skills add goldsky-io/goldsky-agent -a claude-code   # or cursor, codex, opencode
```

Claude Code users can install via the plugin marketplace instead:

```text
/plugin marketplace add goldsky-io/goldsky-agent
/plugin install goldsky@goldsky-agent
```

The family bootstraps itself: tell the agent "Set up Goldsky" and the `auth-setup` skill installs the Goldsky CLI, runs the browser login, and hands off to the `/get-started` command. Product docs: [docs.goldsky.com/ai-skills](https://docs.goldsky.com/ai-skills).

## Roster - All 19 Skills

| Skill | Domain | Installs | What It Does |
|---|---|---|---|
| turbo-builder | Turbo | 1,113 | Build and deploy new Turbo pipelines: requirements, dataset selection, YAML, validation, deployment |
| turbo-pipelines | Turbo | 1,113 | YAML configuration and architecture reference: sources, transforms, sinks, design patterns |
| turbo-transforms | Turbo | 1,106 | SQL, TypeScript, and dynamic-table transforms for pipelines |
| turbo-doctor | Turbo | 1,104 | Interactive troubleshooting for broken pipelines: error states, stuck starts, duplicates, slow backfills |
| secrets | Cross-cutting | 1,102 | Pipeline sink credentials: PostgreSQL, ClickHouse, Kafka, S3, Pub/Sub, webhooks and more |
| mirror | Mirror | 1,092 | Legacy streaming pipelines: sources, sinks, lifecycle, and Mirror vs Turbo guidance |
| turbo-operations | Turbo | 1,090 | Lifecycle commands, pipeline states, checkpoints, inspect/logs CLI syntax, error-pattern lookup |
| edge | RPC | 1,089 | Managed EVM RPC endpoints: capabilities, supported chains, error codes, hedged requests |
| mirror-doctor | Mirror | 1,088 | Diagnose and fix broken Mirror pipelines interactively |
| datasets | Cross-cutting | 1,067 | Dataset reference: chain prefixes, dataset types, 130+ chains |
| auth-setup | Cross-cutting | 1,063 | Install the Goldsky CLI, log in, and configure projects |
| subgraph-builder | Subgraphs | 1,036 | Author, build, and deploy subgraphs: schema design, AssemblyScript mappings, manifest, endpoints |
| subgraph-doctor | Subgraphs | 1,034 | Diagnose failing, stalled, or stuck subgraphs; runs CLI checks and applies fixes |
| subgraph-migrate | Subgraphs | 1,030 | Guided drop-in migration of a subgraph from The Graph |
| compose | Compose | 1,027 | Offchain-to-onchain TypeScript tasks: oracles, keepers, circuit breakers, cross-chain automation |
| compose-doctor | Compose | 1,024 | Diagnose Compose apps: crashloops, missed events, trigger failures, wallet/gas issues |
| onchain-automation | Cross-product | 1,003 | Detect-decide-execute loop: event detection plus onchain transaction submission |
| boost | RPC | 931 | Free caching CDN in front of an existing RPC provider; cuts bills without migrating |
| feeds | Feeds | 256 | REST API for one wallet's balances and transfers (GOLDSKY_FEEDS_API_KEY) |

Additional indexed listings not in the current repo tree: `compose-reference` (98), `cli-reference` (53), `subgraphs` (48), `compose-bitcoin-oracle` (52), `compose-vrf` (48), `compose-dividend-distribution` (47), `compose-compliance-oracle` (46), `turbo-monitor-debug` (15), `turbo-lifecycle` (15), `turbo-architecture` (15).

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent-operable platform pattern** | Goldsky exposes a full product surface as agent skills: one setup skill, builder + doctor pairs per product, and a cross-product router. A strong reference for skill and connector authoring on our side |
| **Onchain data for operators with crypto exposure** | Wallet history, stablecoin flows, and payment-reconciliation pipelines for operator businesses that touch crypto revenue or treasury |
| **Natural language to YAML to deploy** | turbo-builder and compose illustrate prompt-driven data-pipeline provisioning, useful when scoping agent-assisted data engineering |

## Limitations / Verification

- Verified Oct 5, 2026: 19 `SKILL.md` files under `skills/` via the GitHub trees API (branch `main`); 12⭐ / 1 fork; MIT LICENSE in-repo; repo created Feb 26, 2026; last pushed Oct 5, 2026; tree also ships `agents/`, `commands/`, `hooks/`, `.claude-plugin/`, `.cursor-plugin/`.
- Low community traction (12 stars) despite official vendor status. Authority is justified by publisher identity (the goldsky-io org, active since 2021, 43 public repos) rather than community traction, the same pattern as the documented redis/agent-skills.
- The skills operate a live platform: deployments, RPC endpoints, and secrets touch real infrastructure. Start with read-only surfaces (datasets, turbo-pipelines reference, feeds) before enabling deployment flows.
- The 10 auxiliary indexed listings carry low install counts and appear to be pre-skill index artifacts; the roster covers the 19 in-repo skills.
- No live install test was performed; install counts are the Oct 5, 2026 skills.sh sweep snapshot.

## Security

skills.sh per-skill verdicts (sampled 4 skills, verified Oct 5, 2026) - verdicts vary per skill; check the skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| turbo-builder | Pass | Pass | Pass |
| compose | Pass | Pass | Warn |
| edge | Pass | Pass | Warn |
| onchain-automation | Pass | Warn | Warn |

## Related

- [Hermes Agent Setup](/hermes/skills/catalog/hermes-agent-setup)
- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
