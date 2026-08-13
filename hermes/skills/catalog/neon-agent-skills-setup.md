---
title: Neon Agent Skills — Serverless Postgres Platform for Hermes Agents
description: Neon's official agent skills — Serverless Postgres, branching, AI Gateway, Functions, Object Storage. 75K+ combined installs across 8 skills for database-driven agent applications.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/neon-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Neon Agent Skills — Setup Guide

**Source:** [neondatabase/agent-skills](https://skills.sh/neondatabase/agent-skills) (75K+ combined installs)
**GitHub:** [neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) (81 ⭐)
**Category:** Database / Serverless Platform
**Quality Tier:** 🟢 Production

Neon Agent Skills is the official skills collection for building on Neon's serverless Postgres platform. It covers database setup, branching workflows, AI Gateway for LLM routing, serverless functions, and S3-compatible object storage — all branching with your database. These skills enable Hermes agents to provision, manage, and build on a modern serverless Postgres backend.

---

## Installation

```bash
# Core database skills (highest installs)
npx skills add neondatabase/agent-skills --skill neon-postgres
npx skills add neondatabase/agent-skills --skill neon

# Branching & cost optimization
npx skills add neondatabase/agent-skills --skill neon-postgres-branches
npx skills add neondatabase/agent-skills --skill neon-postgres-egress-optimizer

# Platform features
npx skills add neondatabase/agent-skills --skill neon-ai-gateway
npx skills add neondatabase/agent-skills --skill neon-functions
npx skills add neondatabase/agent-skills --skill neon-object-storage
npx skills add neondatabase/agent-skills --skill claimable-postgres
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **neon-postgres** | 56.8K | Serverless Postgres setup, connection methods, pooling, autoscaling, scale-to-zero |
| **neon** | 13.2K | Platform overview — routing to correct skill, CLI setup, MCP server, branch-first workflow |
| **claimable-postgres** | 1.7K | Instant temporary Postgres databases via neon.new — no login, signup, or credit card |
| **neon-postgres-egress-optimizer** | 1.7K | Diagnose and fix excessive Postgres egress (network data transfer) to reduce costs |
| **neon-postgres-branches** | 1.5K | Database branching for testing — schema-only branches, migration testing, CI/CD lifecycles |
| **neon-ai-gateway** | — | One API for all LLMs — route between OpenAI, Anthropic, Google, Meta, DeepSeek from your Neon branch |
| **neon-functions** | — | Long-running serverless Node.js functions with automatic DATABASE_URL injection |
| **neon-object-storage** | — | S3-compatible object storage that branches with your database |

---

## 🔑 Standout Features

### Database Branching (neon-postgres-branches)
Neon's branching is the killer feature for agent workflows. Create isolated database copies instantly for testing agent code, running migrations against production data, or spinning up per-PR environments. Schema-only branches protect sensitive data while still giving realistic test environments — critical for agents that need to verify database changes without touching PII.

### AI Gateway (neon-ai-gateway)
A single API endpoint proxy for all major LLM providers. Hermes agents can route between Claude, GPT, Gemini, and open-source models through one credential. Works with OpenAI SDK, Anthropic SDK, Vercel AI SDK, and Mastra by changing only the base URL. Built-in logging and rate limiting for cost control.

### Serverless Functions (neon-functions)
Long-running HTTP functions co-located with your database. Unlike Lambda-style short-lived functions, Neon Functions support streaming responses, WebSockets, SSE, and MCP servers — ideal for agent backends that need persistent connections.

---

## Hermes Agent Use Cases

- **Agent Database Layer**: Use neon-postgres as the persistent storage backend for Hermes agent memory and state
- **Branch-Per-Task**: Create isolated database branches for each agent task, merge on success, discard on failure
- **Multi-Model Routing**: Use neon-ai-gateway to route between Claude, GPT, and Gemini without managing multiple API keys
- **MCP Server Hosting**: Deploy MCP servers on neon-functions with automatic database connectivity
- **Cost Optimization**: Use egress-optimizer to keep agent database costs minimal at scale

---

## Discovery Method

Publisher sweep via `npx skills find "database" --owner "neondatabase"`. Neon was not previously catalogued in any sweep. Confirmed 8 skills across the agent-skills repo. The neon-postgres skill at 56.8K installs is the highest-install serverless database skill on skills.sh.

---

## Notes

- **neon-postgres** (56.8K) is the most-installed database platform skill on skills.sh, surpassing even Supabase's individual skills
- Neon's branching model is uniquely suited to agent workflows — each agent task can get its own database branch
- The AI Gateway skill directly complements CorpusIQ's multi-model routing strategy
- Functions + Object Storage make Neon a viable all-in-one backend platform for agent applications
