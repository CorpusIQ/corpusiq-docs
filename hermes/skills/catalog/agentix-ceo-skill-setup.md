---
title: Agentix CEO Skill — AI Worker Team Orchestration Setup
description: "agentix-cloud/skills — agentix-ceo (52.0K installs): orchestrate a team of AI workers with roles, tasks, and ephemeral Modal agents in supervised or autopilot mode, via SaaS or self-hosted."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agentix-ceo-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "orchestration", "multi-agent"]
---

# Agentix CEO Skill — Setup Guide

**Source:** [agentix-cloud/skills](https://skills.sh/agentix-cloud/skills)
**GitHub:** [agentix-cloud/skills](https://github.com/agentix-cloud/skills)
**Skills:** 1 skill (`agentix-ceo`) · 52.0K installs
**Category:** Multi-Agent Orchestration
**First Seen:** March 20, 2026 (catalogued August 15, 2026 sweep)
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub pass, Socket pass; Snyk reports a warning)

agentix-ceo turns the agent into a CEO that orchestrates a team of AI workers through the Agentix platform. Workers are ephemeral agents spawned on Modal that complete their task and exit. The skill supports two operating modes: supervised (user approval for new work) and autopilot (full autonomous planning and execution). Roles carry custom system prompts, tasks carry priority and status, and GitHub integration covers git-based workflows. Worker execution requires an Anthropic API key.

---

## Installation

```bash
npx skills add agentix-cloud/skills --skill agentix-ceo
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Anthropic API key** | Required for worker execution |
| **Agentix endpoint** | SaaS (`https://agentix.cloud`, default) or self-hosted URL via `AGENTIX_API_URL` |
| **Node.js + npx** | For the installer |

```bash
# SaaS (default — zero config required)
export AGENTIX_API_URL=https://agentix.cloud

# Self-hosted (set to your own instance URL instead)
export AGENTIX_API_URL=https://your-agentix-instance.example.com
```

## What It Provides

| Capability | Notes |
|---|---|
| Role management | Create roles with custom system prompts |
| Task management | Create tasks with priority and status tracking |
| Ephemeral workers | Spawn workers on Modal that run and exit automatically |
| Operating modes | Supervised (approval gates) and autopilot (autonomous planning) |
| GitHub integration | Git-based workflows |
| Deployment options | SaaS (agentix.cloud with registration) or self-hosted (zero authentication) |

## Quick Start

1. `npx skills add agentix-cloud/skills --skill agentix-ceo`
2. Set `AGENTIX_API_URL` and the Anthropic key
3. Start supervised: "create a researcher role and assign it a task to summarize these three papers"
4. Graduate to autopilot only for tasks with reversible side effects

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Research parallelism** | Spawn ephemeral workers for multi-source market research sweeps |
| **Task fan-out** | Roles per workstream (research, drafting, review) with priority tracking |
| **Orchestration reference** | Supervised/autopilot mode design as a pattern for our own agent governance |
| **Git workflows** | Worker-driven git operations for docs and repo maintenance |

## Limitations / Verification

- Requires an Anthropic API key for workers; Snyk audit carries a warning (review before production use)
- Worker cost depends on Modal usage — budget per task

```bash
curl -s "$AGENTIX_API_URL" | head -c 200   # verify endpoint reachability
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Ruflo Agent Orchestration](/hermes/skills/marketplace/new-july24-2026/) — orchestration comparison

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
