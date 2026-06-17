---
title: Hermes Agent Library — 9 Production-Ready AI Agent Blueprints
description: "Complete library of 9 role-specific Hermes agent configurations: sales, marketing, devops, support, finance, HR, research, legal, and executive. Deploy in minutes with cron schedules and MCP connectors."
category: Agents
tags:
  - agent-library
  - ai-agent-blueprints
  - hermes-agents
  - role-configurations
  - production-agents
last_updated: 2026-06-16
---

# Hermes Agent Library — 9 Production-Ready AI Agent Blueprints

The **Hermes Agent Library** is a curated collection of **production-ready agent configurations** for common business roles. Each agent is a complete configuration blueprint — not a demo or stub — that you can deploy in minutes and customize for your specific stack, workflows, and tools. Every agent includes role description, recommended model, skills to load, MCP connectors, cron schedule, and quick-start command.

Agents in this library run on the [Hermes Agent framework](/hermes/) by Nous Research. They combine **LLM reasoning with persistent memory, scheduled execution, and deep integration with your business tools** through [CorpusIQ MCP connectors](/hermes/mcp/connectors/). An agent isn't just a prompt — it's an **always-on teammate** that monitors, analyzes, drafts, alerts, and reports on a schedule you define.

## Overview

| # | Agent | Primary Use Case | Recommended Model | Connector Footprint |
|---|-------|-----------------|-------------------|---------------------|
| 1 | [Sales Agent](./sales-agent.md) | Lead qualification, pipeline management, outreach sequences | DeepSeek V3 / Claude Sonnet 4 | CRM, Calendly, Email, Slack |
| 2 | [Marketing Agent](./marketing-agent.md) | Content analytics, SEO monitoring, campaign performance | Claude Sonnet 4 / GPT-4o | GA4, Search Console, Ahrefs, Klaviyo, Meta Ads |
| 3 | [DevOps Agent](./devops-agent.md) | Infrastructure monitoring, incident response, deployment tracking | Claude Sonnet 4 / DeepSeek V3 | Database, Slack, Email, Observability APIs |
| 4 | [Support Agent](./support-agent.md) | Ticket triage, knowledge base search, SLA monitoring | Claude Sonnet 4 / GPT-4o | CRM, Slack, Email, Stripe, Notion |
| 5 | [Finance Agent](./finance-agent.md) | Invoice processing, reconciliation, financial reporting | Claude Sonnet 4 / DeepSeek V3 | QuickBooks, Stripe, Slack, Email, Drive |
| 6 | [HR Agent](./hr-agent.md) | Resume screening, onboarding, policy Q&A, compliance | Claude Sonnet 4 / GPT-4o | Calendly, Email, Slack, Notion, Drive |
| 7 | [Research Agent](./research-agent.md) | Competitive intel, market analysis, literature review | Claude Sonnet 4 / DeepSeek V3 | Ahrefs, Semrush, GA4, YouTube, Notion |
| 8 | [Legal Agent](./legal-agent.md) | Contract review, regulatory monitoring, audit prep | Claude Sonnet 4 / GPT-4o | Drive, OneDrive, Notion, Slack, Email |
| 9 | [Executive Agent](./executive-agent.md) | Calendar management, inbox triage, daily briefings | Claude Sonnet 4 / GPT-4o | Calendar, Calendly, Email, Slack, Notion |

## How It Works

### 1. Pick Your Agent

Each agent file is a **self-contained configuration**. Read the role description to confirm it matches your needs, then follow the Quick-Start command at the bottom. The command creates the agent in your Hermes installation with the specified profile, skills, and connectors.

### 2. Connect Your Tools

Before an agent can work, its MCP connectors need to be authenticated. Run `hermes setup connectors` and follow the prompts to connect each service the agent requires. You only need to connect the services you actually use — skip connectors for platforms you don't have.

### 3. Customize the Cron Schedule

The sample cron schedules are sensible defaults but should be tuned to your timezone, working hours, and operational cadence. Edit them in your agent's profile configuration:

```bash
hermes config edit --profile sales
```

### 4. Add Your Business Context

Agents work best when they understand your business. Use [canonical facts](/hermes/governance/) to store key definitions:

```bash
hermes canonical set --profile sales \
  --key icp_criteria \
  --value "B2B SaaS, 50-500 employees, US/Canada, marketing or sales tech stack"
```

### 5. Test and Iterate

Start with **one agent**. Run it manually for a few days, review the output, refine thresholds, then enable the cron schedule. Once confident, deploy the next agent.

## Model Selection Guide

| Model | Best For | Trade-offs |
|-------|----------|------------|
| **Claude Sonnet 4** | General-purpose agent work; nuance, contracts, multi-source synthesis | Higher cost per token |
| **DeepSeek V3 / V4 Pro** | Structured analysis, financial data, research synthesis | May need more explicit formatting |
| **GPT-4o** | Natural language generation, creative briefs, customer-facing drafts | Cost comparable to Claude |
| **Claude Haiku** | Always-on monitoring, alert classification, simple Q&A | Less capable at multi-step reasoning |
| **GPT-4o Mini** | Cost-sensitive deployments, high-volume classification | Less nuanced; pair with larger model |

**Recommendation:** Use Claude Sonnet 4 or GPT-4o for agents that draft communications or analyze complex multi-source data. Use DeepSeek V3/V4 for structured data analysis. Use Haiku or GPT-4o Mini for always-on monitoring skills.

## Extending Agents

Every agent in this library is a starting point. Common extensions:

- **Add a custom skill:** Write a new skill file in your profile's skills directory
- **Chain agents:** Have the Sales Agent's pipeline report feed into the Executive Agent's daily briefing
- **Add web search:** Enable browser automation or web search tools for real-time external data
- **Custom connectors:** Build MCP connectors for your proprietary tools
- **Multi-model routing:** Use Haiku for classification and Sonnet for drafting — same agent, optimized cost

## FAQ

### What is the Hermes Agent Library?

The **Hermes Agent Library** provides 9 production-ready, role-specific agent configurations for common business roles. Each includes skills, MCP connectors, cron schedules, model recommendations, and quick-start commands — ready to deploy in minutes on the Hermes Agent framework.

### How do I deploy a Hermes agent from this library?

1. Pick the agent matching your role from the table above 2. Run the Quick-Start command from the agent's page 3. Authenticate the required connectors with `hermes setup connectors` 4. Customize the cron schedule for your timezone 5. Test manually, then enable the cron.

### Which agent should I deploy first?

Start with the agent that solves your **most painful manual process**. For most businesses, that's the [Sales Agent](/hermes/agents/sales-agent.md) (pipeline management), [Marketing Agent](/hermes/agents/marketing-agent.md) (SEO monitoring), or [Executive Agent](/hermes/agents/executive-agent.md) (daily briefings).

### Can I run multiple agents simultaneously?

Yes. Deploy as many agents as you need. They run as separate Hermes profiles with isolated skills, crons, and configurations. Chain agents together for cross-role workflows (e.g., Sales Agent reports feed into Executive Agent briefings).

### How much does running these agents cost?

Cost varies by model and frequency. Lightweight monitoring with **Claude Haiku** costs pennies per day. Full-featured agents with **Claude Sonnet 4** may cost $1-5/day depending on frequency. See the [Model Selection Best Practices](/hermes/best-practices/model-selection.md) for optimization tips.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the Hermes Agent Library?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Hermes Agent Library provides 9 production-ready, role-specific agent configurations with skills, MCP connectors, cron schedules, and model recommendations — ready to deploy in minutes."
      }
    },
    {
      "@type": "Question",
      "name": "How do I deploy a Hermes agent from this library?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pick the agent matching your role, run the Quick-Start command, authenticate connectors, customize the cron schedule, test manually, then enable the cron."
      }
    },
    {
      "@type": "Question",
      "name": "Which agent should I deploy first?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Start with the agent that solves your most painful manual process — typically Sales Agent, Marketing Agent, or Executive Agent."
      }
    },
    {
      "@type": "Question",
      "name": "Can I run multiple agents simultaneously?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Agents run as separate Hermes profiles with isolated skills, crons, and configurations. Chain them for cross-role workflows."
      }
    },
    {
      "@type": "Question",
      "name": "How much does running these agents cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cost varies by model and frequency. Lightweight monitoring costs pennies per day. Full-featured agents may cost $1-5/day."
      }
    }
  ]
}
</script>

## Related Pages

- [Hermes Knowledge Hub — Architecture & Deployment](/hermes/)
- [Skills Catalog — 133+ Production Skills](/hermes/skills/catalog/)
- [CorpusIQ MCP Connectors — 37+ Business Tools](/hermes/mcp/connectors/)
- [Cron Scheduling Guide](/hermes/governance/scheduling/)
- [Canonical Facts — Store Business Definitions](/hermes/governance/)
- [Model Selection Best Practices](/hermes/best-practices/model-selection.md)


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
