---
title: Hermes Agent Knowledge Repository
description: Complete reference for autonomous Hermes agents. Architecture, infrastructure, skills, MCP, governance, content ops, tools, and operations.
---

# Hermes Agent Knowledge Repository

Everything you need to build and operate autonomous agents. Production-tested on a dual-machine deployment (DGX Spark + Mac Mini M4) running 24 agents across 34 cron jobs.

> **Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent)** by [Nous Research](https://nousresearch.com/). Hermes Agent is the open source autonomous agent framework — persistent memory, self-improving skills, multi-platform gateway, provider-agnostic. This knowledge repository documents our production deployment, skills, and patterns. [Star the official repo →](https://github.com/NousResearch/hermes-agent)

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
| [Catalog](/hermes/skills/catalog/) | Every skill: 89 native + 217 marketplace, categorized |
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

### 10. Case Studies & Examples
Real-world patterns across industries and company sizes.

| Page | Content |
|------|---------|
| [Outputs Overview](/hermes/outputs/) | Community-wide examples hub |
| [Workflow Templates](/hermes/outputs/workflows/templates.md) | 12 ready-to-deploy cron templates |

**By Industry:**
| [Compliance & Audit](/hermes/outputs/case-studies/compliance-audit.md) | [Healthcare](/hermes/outputs/case-studies/healthcare.md) | [Financial Services](/hermes/outputs/case-studies/financial-services.md) |
| [Manufacturing](/hermes/outputs/case-studies/manufacturing.md) | [Real Estate](/hermes/outputs/case-studies/real-estate.md) | [Professional Services](/hermes/outputs/case-studies/professional-services.md) |
| [Customer Support](/hermes/outputs/case-studies/customer-support.md) | [Revenue Operations](/hermes/outputs/case-studies/revenue-operations.md) |

**By Company Size:**
| [Startups](/hermes/outputs/by-company-size/startup.md) | [Mid-Market](/hermes/outputs/by-company-size/mid-market.md) | [Enterprise](/hermes/outputs/by-company-size/enterprise.md) |

[Browse all examples →](/hermes/outputs/)

### 11. Agent Library
Role-specific agent configurations ready to deploy.

| [Sales Agent](/hermes/agents/sales-agent.md) | [Marketing](/hermes/agents/marketing-agent.md) | [DevOps](/hermes/agents/devops-agent.md) |
| [Support](/hermes/agents/support-agent.md) | [Finance](/hermes/agents/finance-agent.md) | [HR](/hermes/agents/hr-agent.md) |
| [Research](/hermes/agents/research-agent.md) | [Legal](/hermes/agents/legal-agent.md) | [Executive](/hermes/agents/executive-agent.md) |

[Browse all agents →](/hermes/agents/)

### 12. Prompt Collections
Effective prompts for common Hermes tasks.

| [Code Generation](/hermes/prompts/code-generation.md) | [Content Creation](/hermes/prompts/content-creation.md) | [Data Analysis](/hermes/prompts/data-analysis.md) |
| [Business Ops](/hermes/prompts/business-operations.md) | [Research](/hermes/prompts/research.md) | [Creative](/hermes/prompts/creative.md) |

[Browse all prompts →](/hermes/prompts/)

### 13. Automation Blueprints
End-to-end workflow patterns with full cron schedules.

| [Daily Operations](/hermes/blueprints/daily-ops.md) | [Customer Lifecycle](/hermes/blueprints/customer-lifecycle.md) | [Content Pipeline](/hermes/blueprints/content-pipeline.md) |
| [Financial Close](/hermes/blueprints/financial-close.md) | [Incident Response](/hermes/blueprints/incident-response.md) |

[Browse blueprints →](/hermes/blueprints/)

### 14. Integration Examples
Connecting Hermes to your existing stack.

| [Slack + GitHub](/hermes/integrations/slack-github.md) | [Email + Calendar](/hermes/integrations/email-calendar.md) |
| [CRM + Analytics](/hermes/integrations/crm-analytics.md) | [Database + Reporting](/hermes/integrations/database-reporting.md) |

[Browse integrations →](/hermes/integrations/)

### 15. Best Practices
Operational wisdom from production deployments.

| [Cron Design](/hermes/best-practices/cron-design.md) | [Model Selection](/hermes/best-practices/model-selection.md) | [Memory](/hermes/best-practices/memory-management.md) |
| [Security](/hermes/best-practices/security.md) | [Skill Dev](/hermes/best-practices/skill-development.md) | [MCP Design](/hermes/best-practices/mcp-design.md) |

[Browse best practices →](/hermes/best-practices/)

### 16. Tools & Software Index
**[Complete Tool Reference](/hermes/tools/)** — 233+ tools across 20 categories. All linked to repos/docs.

[Browse tools →](/hermes/tools/)

### 12. Troubleshooting
**[Common Issues & Fixes](/hermes/troubleshooting/)** — Browser, OAuth, cron, model routing, Playwright, SSH.

[Read troubleshooting →](/hermes/troubleshooting/)

### 13. Ecosystem
**[Hermes Ecosystem](/hermes/ecosystem.md)** — Tools, libraries, research, dashboards, and community resources. Everything that extends Hermes.

[Browse ecosystem →](/hermes/ecosystem.md)

### 14. Changelog
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
| Pages | 37 |
| Total lines | 3,800+ |
| Categories | 14 |
| Tools indexed | 140+ |
| Skills cataloged | 142 |
| MCP connectors | 37+ |
| Active crons | 24 |
| Machines | 2 (DGX + Mac Mini) |

---

---

*Powered by CorpusIQ — agents that compound*
