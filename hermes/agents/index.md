# Hermes Agent Library

## Overview

The Hermes Agent Library is a curated collection of production-ready agent configurations for common business roles. Each agent is a complete configuration blueprint — not a demo or stub — that you can deploy in minutes and customize for your specific stack, workflows, and tools. Every agent includes the role description, recommended model, skills to load, MCP connectors to connect, a cron schedule for autonomous operation, and a quick-start command.

Agents in this library run on the Hermes Agent framework by Nous Research. They combine large language model reasoning with persistent memory, scheduled execution, and deep integration with your business tools through CorpusIQ connectors. An agent isn't just a prompt — it's an always-on teammate that monitors, analyzes, drafts, alerts, and reports on a schedule you define.

## Available Agents

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

## How to Use This Library

### 1. Pick Your Agent

Each agent file is a self-contained configuration. Read the role description to confirm it matches your needs, then follow the Quick-Start command at the bottom. The command creates the agent in your Hermes installation with the specified profile, skills, and connectors.

### 2. Connect Your Tools

Before an agent can work, its MCP connectors need to be authenticated. Run `hermes setup connectors` and follow the prompts to connect each service the agent requires. You only need to connect the services you actually use — skip connectors for platforms you don't have.

### 3. Customize the Cron Schedule

The sample cron schedules are sensible defaults but should be tuned to your timezone, working hours, and operational cadence. Edit them in your agent's profile configuration:

```bash
hermes config edit --profile sales
```

Adjust report timing, alert frequencies, and which channels receive notifications.

### 4. Add Your Business Context

Agents work best when they understand your business. Use canonical facts to store your key definitions:

```bash
hermes canonical set --profile sales \
  --key icp_criteria \
  --value "B2B SaaS, 50-500 employees, US/Canada, marketing or sales tech stack"
```

Store your competitor lists, SLA targets, expense policies, contract playbooks, and other domain-specific knowledge so agents can reference them during operation.

### 5. Test and Iterate

Start with one agent. Run it manually for a few days:

```bash
hermes agent run sales --skill pipeline-health
```

Review the output, refine thresholds, add missing context, then enable the cron schedule. Once you're confident, deploy the next agent.

## Model Selection Guide

| Model | Best For | Trade-offs |
|-------|----------|------------|
| **Claude Sonnet 4** | General-purpose agent work; strong at nuance, contracts, multi-source synthesis | Higher cost per token; slightly slower than smaller models |
| **DeepSeek V3 / V4 Pro** | Structured analysis, financial data, research synthesis | May need more explicit formatting instructions |
| **GPT-4o** | Natural language generation, creative briefs, customer-facing drafts | Cost comparable to Claude; strong all-rounder |
| **Claude Haiku** | Always-on monitoring, alert classification, simple Q&A | Less capable at multi-step reasoning; use for high-frequency, low-complexity tasks |
| **GPT-4o Mini** | Cost-sensitive deployments, high-volume ticket classification | Less nuanced than full-size models; pair with escalation to larger model |

**Recommendation:** Use Claude Sonnet 4 or GPT-4o for agents that draft communications or analyze complex multi-source data. Use DeepSeek V3/V4 for structured data analysis. Use Haiku or GPT-4o Mini for always-on monitoring skills that run frequently.

## Extending Agents

Every agent in this library is a starting point, not a ceiling. Common extensions:

- **Add a custom skill:** Write a new skill file in your profile's skills directory and load it with the agent
- **Chain agents:** Have the Sales Agent's pipeline report feed into the Executive Agent's daily briefing
- **Add web search:** Enable browser automation or web search tools for agents that need real-time external data
- **Custom connectors:** Build MCP connectors for your proprietary tools or industry-specific platforms
- **Multi-model routing:** Use Haiku for classification and Sonnet for drafting within the same agent to optimize cost and speed

## Community Contributions

This library is open-source and community-driven. If you've built an agent configuration that works well for your role or industry, consider contributing it back. Submit a pull request to the Hermes Agent Library repository with your agent file following the same template: role description, recommended model, skills, connectors, cron schedule, and quick-start command.

## Framework Compatibility

These agents are built for Hermes Agent by Nous Research. The configuration format is specific to Hermes Agent's profile and skill system. For the latest framework documentation, including skill authoring, cron configuration, and connector setup, visit [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs).

---

*The Hermes Agent Library is maintained by the community. All agent configurations are provided as starting points — customize them for your specific tools, workflows, and operational requirements.*
