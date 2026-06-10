---
title: Hermes Agent Knowledge Repository
description: Complete reference for autonomous Hermes agents. Architecture, infrastructure, skills, MCP, governance, content ops, tools, and operations.
---

# Hermes Agent Knowledge Repository

Everything you need to build and operate autonomous agents. Production-tested on a dual-machine deployment (DGX Spark + Mac Mini M4) running 24 agents across 24 cron jobs.

## Contents

### 1. Architecture
**[Production Agent Architecture](/hermes/architecture/)** 

Six-layer autonomous agent architecture: orchestration, knowledge, skills, infrastructure, content ops, governance.

[Read architecture →](/hermes/architecture/)

### 2. Setup
**[Installation & Configuration](/hermes/setup/)**

Linux setup (DGX Spark), macOS setup (Mac Mini M4), API configuration, provider setup, environment variables.

[Read setup →](/hermes/setup/)

### 3. Orchestration
**[Agent Orchestration Overview](/hermes/orchestration/)**

How agents are structured, coordinated, and improved.

| Framework | What It Does | Doc |
|-----------|-------------|-----|
| **Hermes Agent** | Execution kernel — tool loop, skills, sessions | [Read →](/hermes/orchestration/hermes/) |
| **CrewAI** | Multi-agent coordination, delegation, parallel work | [Read →](/hermes/orchestration/crewai/) |
| **LangGraph** | Stateful workflows, checkpoints, conditional routing | [Read →](/hermes/orchestration/langgraph/) |
| **Reflexion** | Self-improving loops, evaluation, reflection | [Read →](/hermes/orchestration/reflexion/) |

[Browse orchestration →](/hermes/orchestration/)

### 4. Knowledge Architecture
**[Persistent Memory Systems](/hermes/knowledge/)** — GBrain, GraphRAG, Dream Cycle, Honcho

[Read knowledge →](/hermes/knowledge/)

### 5. Skills
**[Skills Catalog](/hermes/skills/catalog/)** — 133+ skills, single source of truth

| Page | Content |
|------|---------|
| [Catalog](/hermes/skills/catalog/) | Every skill: 80 native + 217 marketplace, categorized |
| [Marketplace](/hermes/skills/marketplace/) | 85 curated skills from skills.sh with install counts |
| [Marketing](/hermes/skills/marketing/) | 45 SEO, CRO, ads, content, growth skills |
| [Development](/hermes/skills/development/) | GitHub, code review, issues, CI/CD skills |
| [Operations](/hermes/skills/operations/) | Email, cron, audit, lead capture, video skills |

[Browse skills →](/hermes/skills/)

### 6. MCP Integration
**[MCP Overview](/hermes/mcp/)** — Model Context Protocol for connecting agents to data

| Page | Content |
|------|---------|
| [MCP Overview](/hermes/mcp/) | Protocol architecture, server types, tool discovery |
| [Connector Catalog](/hermes/mcp/connectors/) | All 37+ CorpusIQ connectors across 11 categories |
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
**[Complete Tool Reference](/hermes/tools/)** — 233+ tools across 20 categories. All linked to repos/docs.

[Browse tools →](/hermes/tools/)

### 12. Troubleshooting
**[Common Issues & Fixes](/hermes/troubleshooting/)** — Browser, OAuth, cron, model routing, Playwright, SSH.

[Read troubleshooting →](/hermes/troubleshooting/)

### 13. Changelog
**[Version History](/hermes/changelog/)** — What changed and when.

[Read changelog →](/hermes/changelog/)

---

## Quick Reference

| What | Where |
|------|-------|
| How do agents execute tasks? | [Hermes Agent](/hermes/orchestration/hermes/) |
| How does persistent memory work? | [Knowledge Architecture](/hermes/knowledge/) |
| What skills can agents use? | [Skills Catalog](/hermes/skills/catalog/) |
| What tools and software does this use? | [Tools & Software Index](/hermes/tools/) |
| How do agents connect to SaaS tools? | [MCP Integration](/hermes/mcp/) |
| What hardware runs this? | [Infrastructure](/hermes/infrastructure/) |
| How is safety enforced? | [Governance](/hermes/governance/) |
| How do agents create content? | [Content Ops](/hermes/content-ops/) |
| Where is the architecture documented? | [Architecture](/hermes/architecture/) |
| How do I fix common problems? | [Troubleshooting](/hermes/troubleshooting/) |
| What growth outputs do agents produce? | [Growth Outputs](/hermes/outputs/) |

---

## Repo Stats

| Metric | Value |
|--------|-------|
| Pages | 36 |
| Total lines | 3,500+ |
| Categories | 13 |
| Tools indexed | 140+ |
| Skills cataloged | 142 |
| MCP connectors | 37+ |
| Active crons | 24 |
| Machines | 2 (DGX + Mac Mini) |

---

---

*Powered by CorpusIQ — agents that compound*
