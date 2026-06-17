---
title: Hermes Agent Knowledge Repository — Production Autonomous Agent Reference
description: "Complete production reference for autonomous Hermes agents: 6-layer architecture, 133+ skills, 38 crons, 6 memory systems, and 37+ MCP business connectors. Real deployment on DGX Spark + Mac Mini M4."
category: Documentation
tags:
  - hermes-agent
  - autonomous-agents
  - production-reference
  - knowledge-repository
  - ai-infrastructure
last_updated: 2026-06-16
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

## FAQ

### What is the Hermes Agent Knowledge Repository?

The **Hermes Agent Knowledge Repository** is the most comprehensive production reference for autonomous Hermes agents. It documents a real 24/7 deployment running on DGX Spark + Mac Mini M4 with 38 crons, 133+ skills, 6 memory systems, and 37+ MCP connectors — everything the official docs don't cover.

### How do I get started with Hermes Agent?

Begin with the [Quick Start Guide](/hermes/setup/) for installation and configuration, then explore the [Architecture section](/hermes/architecture/) to understand the 6-layer production model. Deploy your first agent from the [Agent Library](/hermes/agents/) and browse the [Cron Scheduling Guide](/hermes/governance/scheduling/) for automation patterns.

### What hardware do I need to run Hermes Agent?

The documented production deployment runs on **NVIDIA DGX Spark** (primary compute, inference, 96+ skills) and **Apple Mac Mini M4** (worker node, browser automation). For lighter setups, a single machine with 16GB+ RAM and a modern GPU or cloud API access is sufficient. See the [Infrastructure guide](/hermes/infrastructure/) for full hardware specs.

### How does Hermes Agent handle memory and knowledge?

Hermes uses a **6-system memory stack**: Honcho (peer memory), GBrain (organizational knowledge), memcore-cloud (cross-session context), GraphRAG (relationship memory), Dream Cycle (nightly consolidation), and Session DB (conversation history). The [Knowledge Architecture guide](/hermes/knowledge/) covers the triple-stack pattern in depth.

### What tools and platforms does Hermes integrate with?

Through [CorpusIQ MCP connectors](/hermes/mcp/connectors/), Hermes connects to **37+ business platforms** including CRM (HubSpot, Close), analytics (GA4, PostHog), email (Gmail, Outlook), ads (Meta, Google, LinkedIn), ecommerce (Shopify, Stripe), finance (QuickBooks), SEO (Ahrefs, Semrush), and more — all through a single OAuth flow.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the Hermes Agent Knowledge Repository?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The most comprehensive production reference for autonomous Hermes agents, documenting a real 24/7 deployment with 38 crons, 133+ skills, 6 memory systems, and 37+ MCP connectors."
      }
    },
    {
      "@type": "Question",
      "name": "How do I get started with Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Begin with the Quick Start Guide for installation, explore Architecture for the 6-layer model, deploy your first agent from the Agent Library, and browse Cron Scheduling for automation patterns."
      }
    },
    {
      "@type": "Question",
      "name": "What hardware do I need to run Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Production runs on NVIDIA DGX Spark and Apple Mac Mini M4. For lighter setups, a single machine with 16GB+ RAM and GPU/cloud API access is sufficient."
      }
    },
    {
      "@type": "Question",
      "name": "How does Hermes Agent handle memory and knowledge?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hermes uses a 6-system memory stack: Honcho, GBrain, memcore-cloud, GraphRAG, Dream Cycle, and Session DB. The Knowledge Architecture guide covers the triple-stack pattern."
      }
    },
    {
      "@type": "Question",
      "name": "What tools and platforms does Hermes integrate with?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Through CorpusIQ MCP connectors, Hermes connects to 37+ platforms including CRM, analytics, email, ads, ecommerce, finance, SEO, and more via a single OAuth flow."
      }
    }
  ]
}
</script>

## Related Pages

- [Hermes Knowledge Hub — Production Deployment](/hermes/)
- [Architecture — 6-Layer Production Model](/hermes/architecture/)
- [Agent Library — 9 Role Configurations](/hermes/agents/)
- [Ecosystem Directory — 234+ Community Resources](/hermes/ecosystem.md)
- [Cron Scheduling — 38 Production Crons](/hermes/governance/scheduling/)
- [CorpusIQ MCP Connectors — 37+ Business Tools](/hermes/mcp/connectors/)
- [Best Practices — Production Operations](/hermes/best-practices/)

---

*Powered by CorpusIQ — agents that compound*
