---
title: Hermes Agent Knowledge Repository
description: Complete reference for autonomous Hermes agents. Architecture, infrastructure, skills, MCP, governance, content ops, and operations. Built from real-world CorpusIQ deployment.
---

# Hermes Agent Knowledge Repository

Everything you need to build and operate autonomous agents with [Hermes Agent](https://hermes-agent.nousresearch.com). Production-tested on a dual-machine deployment (DGX Spark + Mac Mini M4) running 24 agents across 24 cron jobs.

## Get Started

```bash
# Install Hermes Agent
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Or from source
git clone https://github.com/NousResearch/hermes-agent
cd hermes-agent && pip install -e .

# Install skills from the marketplace
npx skills add vercel-labs/agent-browser
npx skills add anthropics/skills@mcp-builder
npx skills add coreyhaines31/marketingskills@seo-audit
```

---

## Contents

### 1. Architecture
**[Production Agent Architecture](/hermes/architecture)** (103 lines)

Six-layer autonomous agent architecture:
- Orchestration layer — agent execution kernel
- Knowledge layer — persistent memory and retrieval
- Skills layer — reusable capabilities
- Infrastructure layer — dual-machine deployment
- Content ops layer — autonomous publishing
- Governance layer — monitoring and safety

[Read architecture →](/hermes/architecture)

### 2. Setup
**[Installation & Configuration](/hermes/setup/)** (106 lines)

Complete setup guides:
- Linux setup (DGX Spark / NVIDIA DGX)
- macOS setup (Mac Mini M4)
- API configuration
- Provider setup (Anthropic, OpenAI, OpenRouter)
- Environment variables
- First agent run

[Read setup →](/hermes/setup/)

### 3. Orchestration
How agents are structured, coordinated, and improved.

| Page | Lines | Content |
|------|-------|---------|
| [Hermes Agent](/hermes/orchestration/hermes/) | 163 | Primary execution kernel, tool loop, skills loading, session management |
| [CrewAI](/hermes/orchestration/crewai/) | — | Multi-agent coordination, task delegation, tool assignment |
| [LangGraph](/hermes/orchestration/langgraph/) | — | Stateful graph-based workflows, checkpoints, conditional routing |
| [Reflexion](/hermes/orchestration/reflexion/) | — | Self-improving agent loops, evaluation, reflection, memory |

[Browse orchestration →](/hermes/orchestration/)

### 4. Knowledge Architecture
**[Persistent Memory Systems](/hermes/knowledge/)** (71 lines)

- **GBrain** — Garry Tan's agent brain (v0.42.26.0, 729 indexed files, nomic-embed-text/768d)
- **GraphRAG** — Microsoft graph-based retrieval (33K stars)
- **Dream Cycle** — Memory consolidation and insight generation
- **Honcho** — Peer identity and conversation memory

[Read knowledge →](/hermes/knowledge/)

### 5. Skills
73+ native skills + 85+ marketplace skills.

| Page | Lines | Content |
|------|-------|---------|
| [Skills Index](/hermes/skills/) | 45 | Overview of all skills, top picks, install commands |
| [Marketplace](/hermes/skills/marketplace/) | 143 | 85 curated skills from skills.sh across 10 categories |
| [Marketing](/hermes/skills/marketing/) | 47 | 45 SEO, CRO, copy, ads, content, growth skills |
| [Development](/hermes/skills/development/) | 29 | GitHub, code review, issues, CI/CD skills |
| [Operations](/hermes/skills/operations/) | 43 | Email, cron, audit, lead capture, video skills |

[Browse skills →](/hermes/skills/)

### 6. MCP Integration
Model Context Protocol — connecting agents to 30+ data sources.

| Page | Lines | Content |
|------|-------|---------|
| [MCP Overview](/hermes/mcp/) | 92 | Protocol architecture, server types, tool discovery |
| [Server Guides](/hermes/mcp/servers/) | 93 | GA4, Stripe, Shopify, QuickBooks, HubSpot, Google Ads, and more |

[Browse MCP →](/hermes/mcp/)

### 7. Infrastructure
Dual-machine deployment hardware and services.

| Page | Lines | Content |
|------|-------|---------|
| [Infrastructure Overview](/hermes/infrastructure/) | 38 | Architecture overview and machine roles |
| [DGX Spark](/hermes/infrastructure/dgx/) | 39 | NVIDIA DGX, 21 cron jobs, GPU compute, LLM hosting |
| [Mac Mini M4](/hermes/infrastructure/mac-mini/) | 34 | macOS worker node, 4 cron jobs, Playwright, SSH |
| [Browser Automation](/hermes/infrastructure/browser/) | 55 | Playwright, agent-browser, cookie management, stealth |
| [Auth Management](/hermes/infrastructure/auth/) | 40 | OAuth token lifecycle, headless automation, rotation |
| [Model Routing](/hermes/infrastructure/routing/) | 41 | Multi-model strategy, cost optimization, model selection |

[Browse infrastructure →](/hermes/infrastructure/)

### 8. Governance
Rules, monitoring, and safety for autonomous agents.

| Page | Lines | Content |
|------|-------|---------|
| [Governance Overview](/hermes/governance/) | 54 | System governance baseline, seven rules, session management |
| [System Registry](/hermes/governance/registry/) | 137 | Configuration registry, environment, service inventory |
| [Email Operations](/hermes/governance/email/) | — | Dual-account management, send checklist, response standards |
| [Cron Scheduling](/hermes/governance/scheduling/) | — | Job management, scheduling patterns, chain jobs |
| [System Monitoring](/hermes/governance/monitoring/) | — | Health checks, drift detection, alerting, audits |

[Browse governance →](/hermes/governance/)

### 9. Content Operations
Autonomous content creation and publishing.

| Page | Lines | Content |
|------|-------|---------|
| [Content Ops Overview](/hermes/content-ops/) | 22 | Content pipeline architecture |
| [Video Production](/hermes/content-ops/video/) | 148 | HeyGen video generation, UGC series, TikTok/Instagram |
| [Social Automation](/hermes/content-ops/social/) | — | X, Reddit, Discord, LinkedIn, cross-platform posting |
| [Community Engagement](/hermes/content-ops/engagement/) | — | Help-first strategy, comment engines, community building |

[Browse content ops →](/hermes/content-ops/)

### 10. Growth Outputs
**[Growth Channels & Metrics](/hermes/outputs/)** (22 lines)

Product Hunt, SEO, GitHub contributions, recruiting, and marketplace presence.

[Read outputs →](/hermes/outputs/)

---

## Quick Reference

| What | Where |
|------|-------|
| How do agents execute tasks? | [Hermes Agent](/hermes/orchestration/hermes/) |
| How does persistent memory work? | [Knowledge Architecture](/hermes/knowledge/) |
| What skills can agents use? | [Skills Marketplace](/hermes/skills/marketplace/) |
| How do agents connect to SaaS tools? | [MCP Integration](/hermes/mcp/) |
| What hardware runs this? | [Infrastructure](/hermes/infrastructure/) |
| How is safety enforced? | [Governance](/hermes/governance/) |
| How do agents create content? | [Content Ops](/hermes/content-ops/) |
| Where is the architecture documented? | [Architecture](/hermes/architecture) |
| How do I set up my own agent? | [Setup Guide](/hermes/setup/) |
| What growth outputs do agents produce? | [Growth Outputs](/hermes/outputs/) |

---

## External Resources

- [Hermes Agent Docs](https://hermes-agent.nousresearch.com/docs) — official documentation
- [Nous Research](https://nousresearch.com) — creators of Hermes
- [skills.sh](https://skills.sh) — agent skills marketplace (619K+ skills)
- [MCP Hub](https://mcp.so) — MCP server directory

---

## Repo Stats

| Metric | Value |
|--------|-------|
| Pages | 32 |
| Total lines | 1,700+ |
| Categories | 10 |
| Skills cataloged | 158 |
| Active crons | 24 |
| Machines | 2 (DGX + Mac Mini) |
| Connected MCP servers | 30+ |

---

*Powered by CorpusIQ — agents that compound*
