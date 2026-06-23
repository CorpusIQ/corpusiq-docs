---
title: Hermes Agent Resources — Tools, Skills, MCP Servers & Deployment Knowledge
description: "A curated collection of Hermes Agent resources: MCP servers, skills, memory systems, deployment patterns, and community tools. Everything you need to build production autonomous AI agents."
category: Documentation
tags:
  - hermes-agent
  - autonomous-agents
  - production-deployment
  - ai-agent-architecture
  - mcp-ecosystem
last_updated: 2026-06-23
---

<p align="center">
  <img src="https://raw.githubusercontent.com/NousResearch/hermes-agent/main/assets/banner.png" alt="Hermes Agent" width="600">
</p>

<h1 align="center">Hermes Agent — Community Resources</h1>

<p align="center">
  <b>A curated directory of tools, skills, MCP servers, and deployment knowledge for building production AI agents with Hermes.</b>
</p>

<p align="center">
  <a href="https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml"><img src="https://img.shields.io/badge/Submit_a_Repo-Add_your_resource-brightgreen" alt="Submit"></a>
  <a href="https://github.com/CorpusIQ/corpusiq-docs/blob/main/hermes/ecosystem.md"><img src="https://img.shields.io/badge/Ecosystem-406_repos-blue" alt="Ecosystem"></a>
  <a href="https://github.com/CorpusIQ/corpusiq-docs"><img src="https://img.shields.io/badge/Star_us-Contribute-gold" alt="Star"></a>
</p>

---

## Why This Exists

The [official Hermes docs](https://hermes-agent.nousresearch.com/docs/) cover installation and configuration. They don't tell you what to actually build, how to wire memory systems together, or which MCP servers work in production.

This repository fills that gap:

- **406+ repos** indexed across 18 categories — MCP servers, agent personalities, skills, blueprints
- **Memory stack guides** — Honcho + GBrain + memcore-cloud triple stack for persistent agent memory
- **Deployment patterns** — single machine, multi-machine, Docker, systemd, model routing strategies
- **Skill directory** — find reusable agent workflows from agentskills.io, skills.sh, and the community
- **MCP server catalog** — 301+ servers discovered across 19 sweeps since June 2026

**This is the directory you wish existed when you started building.**

---

## Quick Start

```bash
# Install Hermes Agent
pip install hermes-agent

# Add an MCP server
hermes mcp add corpusiq --url https://mcp2.corpusiq.io/mcp
hermes mcp add honcho --url https://mcp.honcho.dev

# Install community skills
hermes skills install <skill-url>

# Clone this resource directory
git clone https://github.com/CorpusIQ/corpusiq-docs.git
```

**Next steps:** Setup Guides · Best Practices · Ecosystem Map

---

## Architecture

### The Production Stack

Most Hermes setups are single-machine chat loops. Production requires distinct layers:

| Layer | Purpose | Examples |
|-------|---------|----------|
| **Orchestration** | Agent runtime | Hermes Agent, CrewAI, LangGraph, Reflexion |
| **MCP Layer** | External tools | File systems, APIs, databases, browser automation |
| **Memory** | Persistent context | Honcho, GBrain, memcore-cloud, GraphRAG |
| **Skills** | Reusable workflows | Code review, deployment, content generation, monitoring |
| **Infrastructure** | Deployment | Multi-machine SSH, Docker containers, systemd services |
| **Governance** | Operations | System registry, cron scheduling, drift prevention, self-improvement |

### Multi-Machine Pattern

For production agents handling browser automation, video processing, or heavy workloads:

- **Primary node** — GPU compute for inference, orchestration, LLM routing
- **Worker node** — Apple Silicon or x86 for browser automation, social publishing, FFmpeg

Offloading noisy workloads keeps the primary agent stable.

---

## Memory

The biggest gap between a chat agent and an autonomous operator is persistent knowledge. Without memory, every session starts from zero.

### Stack Options

| System | Type | Use Case | Stars |
|--------|------|----------|-------|
| **[Honcho](https://mcp.honcho.dev)** | Peer memory | Identity, preferences, conversation history, decisions | — |
| **[GBrain](https://github.com/garrytan/gbrain)** | Knowledge base | File indexing, code understanding | 23K+ |
| **[memcore-cloud](https://github.com/memcore-cloud)** | Cross-session | Context injection, raw source tracking, FTS5 recall | — |
| **[EverOS](https://github.com/EverMind-AI/EverOS)** | Self-evolving | Long-term memory evolution | 7.5K+ |
| **[claude-mem](https://github.com/thedotmack/claude-mem)** | Session persistence | Persistent context across sessions | 82K+ |

### The Honcho + GBrain + memcore-cloud Pattern

Session Start loads peer context (Honcho), organizational knowledge (GBrain), and cross-session context (memcore-cloud). Agent operates with full context. Session End writes new observations and queues a 3 AM dream cycle for memory consolidation.

---

## Skills

Skills are reusable, self-contained agent workflows. Hermes loads them on demand.

| Source | Description |
|--------|-------------|
| **[agentskills.io](https://agentskills.io)** | Open standard skill hub — cross-agent compatible |
| **[skills.sh](https://skills.sh)** | Community marketplace — new skills daily |
| **[wondelai/skills](https://github.com/wondelai/skills)** | Cross-platform skills library (380+ stars) |
| **[agency-agents](https://github.com/msitarzewski/agency-agents)** | 232 specialized agent personalities (115K+ stars) |
| **[aawobdev/hermes-skills](https://github.com/aawobdev/hermes-skills)** | Blueprint orchestration patterns |

---

## MCP Servers

Model Context Protocol (MCP) servers extend Hermes with structured tools.

| Server | Description |
|--------|-------------|
| **[CorpusIQ MCP](https://corpusiq.io)** | 37+ business APIs — Shopify, Stripe, QuickBooks, HubSpot, GA4, Meta Ads, Gmail, Slack. Single OAuth. Read-only. CASA Tier 2 certified. |
| **[Stripe MCP](https://github.com/stripe/agent-toolkit)** | Payment processing, charges, customers, payouts |
| **[GitHub MCP](https://github.com/github/github-mcp-server)** | Repository management, issues, PRs, code review |
| **[Postgres MCP](https://github.com/modelcontextprotocol/servers)** | Direct database access with SQL |
| **[Browser MCP](https://github.com/modelcontextprotocol/servers)** | Web automation and scraping |
| **[Honcho MCP](https://mcp.honcho.dev)** | Peer memory and identity |
| **[EverOS](https://github.com/EverMind-AI/EverOS)** | Self-evolving memory across agents |

**301+ MCP servers catalogued** across 19 discovery sweeps.

---

## Deployment

### Patterns

| Pattern | When to Use |
|---------|-------------|
| **Single machine** | Local-only agents, development, small workloads |
| **Multi-machine** | Production agents with browser automation or heavy I/O |
| **Docker** | Containerized deployment with persistent volumes |
| **systemd** | Auto-restart on crash, log management, boot persistence |

### Model Routing

| Task Type | Model | Cost |
|-----------|-------|------|
| Lightweight ops | Qwen, local Ollama | ~free |
| Research, content, coding | DeepSeek V4, Claude Sonnet | $ |
| Strategy, architecture, contracts | Claude Opus, GPT-5 | $$ |

---

## Ecosystem

| Resource | Description |
|----------|-------------|
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Core project (195K+ stars) |
| [Official Docs](https://hermes-agent.nousresearch.com/docs/) | Installation, CLI, gateway, tools, skills |
| [Discord](https://discord.gg/NousResearch) | Community support |

### Community Projects

| Project | Stars | Description |
|---------|-------|-------------|
| [claude-mem](https://github.com/thedotmack/claude-mem) | 82K+ | Persistent context across sessions |
| [hermes-webui](https://github.com/nesquena/hermes-webui) | 14K+ | Web interface for Hermes |
| [hermes-desktop](https://github.com/fathah/hermes-desktop) | 12K+ | Desktop companion app |
| [PraisonAI](https://github.com/MervinPraison/PraisonAI) | 8K+ | 24/7 AI workforce orchestration |
| [mission-control](https://github.com/builderz-labs/mission-control) | 3.7K+ | Multi-agent fleet management |
| [Hermes Agency](https://github.com/DeployFaith/Hermes_Agency) | — | P2P agent collaboration |

**[Full ecosystem directory](ecosystem.md)** — 406+ repos indexed across 18 categories, updated daily. 301+ MCP servers catalogued.

---

## Contributing

[Submit a repo, skill, or MCP server](https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml). This is a community resource. If you built something useful for Hermes, add it here.

---

*Curated by [CorpusIQ](https://www.corpusiq.io) — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
