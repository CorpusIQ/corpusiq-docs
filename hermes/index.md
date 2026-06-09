---
title: Hermes Agent Knowledge Repository
description: Complete reference for autonomous Hermes agents. Architecture, infrastructure, skills, MCP, governance, content ops, tools, and operations.
---

# Hermes Agent Knowledge Repository

Everything you need to build and operate autonomous agents with [Hermes Agent](https://hermes-agent.nousresearch.com). Production-tested on a dual-machine deployment (DGX Spark + Mac Mini M4) running 24 agents across 24 cron jobs.

## Get Started

```bash
# Install Hermes Agent
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Install skills from the marketplace
npx skills add vercel-labs/agent-browser
npx skills add anthropics/skills@mcp-builder
npx skills add coreyhaines31/marketingskills@seo-audit
```

---

## Contents

### 1. Architecture
**[Production Agent Architecture](/hermes/architecture)** (103 lines)

Six-layer autonomous agent architecture: orchestration, knowledge, skills, infrastructure, content ops, governance.

[Read architecture →](/hermes/architecture)

### 2. Setup
**[Installation & Configuration](/hermes/setup/)** (106 lines)

Linux setup (DGX Spark), macOS setup (Mac Mini M4), API configuration, provider setup, environment variables.

[Read setup →](/hermes/setup/)

### 3. Orchestration
How agents are structured, coordinated, and improved.

| Page | Content |
|------|---------|
| [Hermes Agent](/hermes/orchestration/hermes/) | Execution kernel, tool loop, skills loading, session management |
| [CrewAI](/hermes/orchestration/crewai/) | Multi-agent coordination, task delegation, tool assignment |
| [LangGraph](/hermes/orchestration/langgraph/) | Stateful graph-based workflows, checkpoints, conditional routing |
| [Reflexion](/hermes/orchestration/reflexion/) | Self-improving agent loops, evaluation, reflection, memory |

[Browse orchestration →](/hermes/orchestration/)

### 4. Knowledge Architecture
**[Persistent Memory Systems](/hermes/knowledge/)** — GBrain, GraphRAG, Dream Cycle, Honcho

[Read knowledge →](/hermes/knowledge/)

### 5. Skills
73+ native skills + 85+ marketplace skills.

| Page | Content |
|------|---------|
| [Skills Index](/hermes/skills/) | Overview of all skills with install commands |
| [Marketplace](/hermes/skills/marketplace/) | 85 curated skills from skills.sh across 10 categories |
| [Marketing](/hermes/skills/marketing/) | 45 SEO, CRO, copy, ads, content, growth skills |
| [Development](/hermes/skills/development/) | GitHub, code review, issues, CI/CD skills |
| [Operations](/hermes/skills/operations/) | Email, cron, audit, lead capture, video skills |

[Browse skills →](/hermes/skills/)

### 6. MCP Integration
Model Context Protocol — connecting agents to 30+ data sources.

| Page | Content |
|------|---------|
| [MCP Overview](/hermes/mcp/) | Protocol architecture, server types, tool discovery |
| [Server Guides](/hermes/mcp/servers/) | GA4, Stripe, Shopify, QuickBooks, HubSpot, and more |

[Browse MCP →](/hermes/mcp/)

### 7. Infrastructure
Dual-machine deployment hardware and services.

| Page | Content |
|------|---------|
| [Infrastructure Overview](/hermes/infrastructure/) | Architecture and machine roles |
| [DGX Spark](/hermes/infrastructure/dgx/) | NVIDIA DGX, 21 cron jobs, GPU compute |
| [Mac Mini M4](/hermes/infrastructure/mac-mini/) | macOS worker, 4 cron jobs, Playwright |
| [Browser Automation](/hermes/infrastructure/browser/) | Playwright, stealth, cookie management |
| [Authentication](/hermes/infrastructure/auth/) | OAuth lifecycle, headless refresh |
| [Model Routing](/hermes/infrastructure/routing/) | Multi-model strategy, ~65% cost savings |

[Browse infrastructure →](/hermes/infrastructure/)

### 8. Governance
Rules, monitoring, and safety for autonomous agents.

| Page | Content |
|------|---------|
| [Governance Overview](/hermes/governance/) | Seven rules, session management |
| [System Registry](/hermes/governance/registry/) | Configuration registry, service inventory |
| [Email Operations](/hermes/governance/email/) | Dual-account, send checklist, response standards |
| [Cron Scheduling](/hermes/governance/scheduling/) | Job management, chain jobs, delivery channels |
| [System Monitoring](/hermes/governance/monitoring/) | Health checks, drift detection, alerting |

[Browse governance →](/hermes/governance/)

### 9. Content Operations
Autonomous content creation and publishing.

| Page | Content |
|------|---------|
| [Content Ops Overview](/hermes/content-ops/) | Content pipeline architecture |
| [Video Production](/hermes/content-ops/video/) | HeyGen video, UGC series, TikTok/Instagram |
| [Social Automation](/hermes/content-ops/social/) | X, Reddit, Discord, LinkedIn, Postiz |
| [Community Engagement](/hermes/content-ops/engagement/) | Help-first strategy, comment engines |

[Browse content ops →](/hermes/content-ops/)

### 10. Growth Outputs
**[Growth Channels & Metrics](/hermes/outputs/)** — SEO, Product Hunt, GitHub PRs, marketplace presence.

[Read outputs →](/hermes/outputs/)

### 11. Tools & Software Index
**[Complete Tool Reference](/hermes/tools/)** — 100+ tools with links

Every tool, library, service, and platform referenced in the knowledge repository in one page. Categories: Orchestration, Knowledge, MCP, Infrastructure, Browser, Content, LLM, Analytics, Email, Commerce, Dev Tools, Platforms, Protocols. All linked to repos/docs/homepages.

[Browse tools →](/hermes/tools/)

---

## Quick Reference

| What | Where |
|------|-------|
| How do agents execute tasks? | [Hermes Agent](/hermes/orchestration/hermes/) |
| How does persistent memory work? | [Knowledge Architecture](/hermes/knowledge/) |
| What skills can agents use? | [Skills Marketplace](/hermes/skills/marketplace/) |
| What tools and software does this use? | [Tools & Software Index](/hermes/tools/) |
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
| Pages | 33 |
| Total lines | 2,700+ |
| Categories | 11 |
| Tools indexed | 100+ |
| Skills cataloged | 158 |
| Active crons | 24 |
| Machines | 2 (DGX + Mac Mini) |
| Connected MCP servers | 30+ |

---

*Powered by CorpusIQ — agents that compound*
