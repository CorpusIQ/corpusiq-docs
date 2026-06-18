---
title: Hermes Sales Agent Configuration — AI-Powered Pipeline & Outreach
description: Deploy an autonomous Hermes sales agent for lead qualification, pipeline management, outreach sequences, and daily CRM reporting. Complete configuration blueprint with cron schedules.
category: Agents
tags:
  - sales-agent
  - pipeline-management
  - lead-qualification
  - crm-automation
  - ai-sales-assistant
last_updated: 2026-06-16
---

# Hermes Sales Agent — Autonomous Pipeline Management & AI Outreach

The **Hermes Sales Agent** is a production-ready **AI sales assistant** that automates your entire sales lifecycle — from **lead qualification** to closed-won deal. Deploy in minutes to monitor your CRM pipeline, enrich lead data, draft outreach sequences, and surface at-risk opportunities so your team spends less time in spreadsheets and more time closing.

This agent runs on the [Hermes Agent framework](/hermes/) by Nous Research and integrates with your CRM, calendar, and communication tools through [CorpusIQ MCP connectors](/hermes/mcp/connectors/).

## Overview

**The Sales Agent replaces manual pipeline management** with autonomous monitoring, qualification, and reporting. Instead of checking dashboards and drafting follow-ups manually, your team receives pre-built pipeline summaries, lead scores, and outreach drafts delivered to Slack or email on schedule.

| Capability | What It Does |
|-----------|-------------|
| **Pipeline monitoring** | Daily snapshot of deals by stage, weighted forecast, at-risk flags |
| **Lead qualification** | Scores inbound leads against your ICP using firmographic + behavioral signals |
| **Outreach sequencing** | Drafts multi-touch sequences (email, call, LinkedIn) based on persona and stage |
| **Meeting preparation** | Pulls deal history, contact notes, and recent comms before every call |
| **Competitor intelligence** | Surfaces competitive insights when a competitor appears in a deal record |

> **See also:** [Agent Library Overview](/hermes/agents/) · [Marketing Agent](/hermes/agents/marketing-agent.md) · [Executive Agent](/hermes/agents/executive-agent.md)

## How It Works

1. **Connect your CRM** — HubSpot, Close CRM, or LeadConnector via [CorpusIQ connectors](/hermes/mcp/connectors/)
2. **Set your ICP** — Store ideal customer profile criteria in [canonical facts](/hermes/governance/)
3. **Load the skills** — Pipeline health, lead qualification, outreach sequencing, meeting prep
4. **Schedule the crons** — Daily reports, qualification checks, weekly forecasts
5. **Receive in Slack/Email** — Pipeline summaries, alerts for stalled deals, meeting briefs

## Key Features

- **Daily pipeline health reports** delivered to Slack every weekday at 7:30 AM
- **Lead scoring** against your ICP with firmographic and behavioral enrichment
- **Stale deal detection** — flags deals with no activity in 7+ days
- **Meeting prep briefs** auto-generated before every scheduled Calendly call
- **Weekly forecast reports** for Monday leadership reviews
- **Multi-touch outreach drafting** with persona-aware messaging

## Recommended Model

**DeepSeek V3** or **Claude Sonnet 4** — balanced cost, speed, and reasoning for structured CRM analysis and email drafting. Use **GPT-4o Mini** for lighter deployments.

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **HubSpot / Close CRM / LeadConnector** | Pipeline, deals, contacts |
| **Calendly** | Meeting scheduling |
| **Gmail / Outlook** | Outreach, thread tracking |
| **GA4** | Prospect website visits |
| **Slack** | Pipeline alerts, notifications |
| **Airtable / Notion** | Sales playbooks, ICP docs |

## Sample Cron Schedule

```cron
# Daily pipeline health report every weekday at 7:30 AM
30 7 * * 1-5 hermes skill pipeline-health --format slack

# Lead qualification check every 4 hours during business hours
0 9,13,17 * * 1-5 hermes skill lead-qualification --since 4h

# Weekly pipeline forecast every Monday at 8:00 AM
0 8 * * 1 hermes skill pipeline-health --weekly-forecast --format email

# Stale deal alert daily at 9:00 AM
0 9 * * 1-5 hermes skill pipeline-health --stale-only --period 7d
```

## Quick-Start Command

```bash
hermes agent create sales \
  --model deepseek-v4-pro \
  --skills pipeline-health,lead-qualification,outreach-sequence,meeting-prep \
  --connectors hubspot,calendly,gmail,slack \
  --profile sales \
  --description "Sales pipeline and outreach agent"
```

## Configuration Notes

- Store your **ICP definition** in canonical facts for qualification reference
- Define **deal stages and activity thresholds** (e.g., "stale = no activity in 7 days")
- The agent **respects CRM permissions** — only sees deals you have access to
- Set **alert routing** — which Slack channels receive pipeline alerts

## Extending

- Add `competitor-intel` skill for Semrush/Ahrefs competitor monitoring
- Integrate **LinkedIn Sales Navigator** for social selling signals
- Add **deal health scoring** using ML on historical win/loss patterns

## FAQ

### What does the Hermes Sales Agent do?

The Hermes Sales Agent is an autonomous AI assistant that monitors your CRM pipeline, qualifies inbound leads against your ICP, drafts outreach sequences, flags at-risk deals, and generates daily pipeline reports — all on a cron schedule without manual intervention.

### How does the sales agent qualify leads?

The agent scores inbound leads by comparing firmographic data (company size, industry, location) and behavioral signals (website visits, email opens, pricing page views) against your stored ICP criteria in canonical facts.

### Can the sales agent integrate with my existing CRM?

Yes. The agent connects to **HubSpot**, **Close CRM**, and **LeadConnector** through CorpusIQ MCP connectors. It reads deals, contacts, and activities from your CRM with full permission respect.

### How do I customize the sales agent for my pipeline stages?

Store your deal stage definitions, activity thresholds, and ICP criteria in [canonical facts](/hermes/governance/). The agent references these during all pipeline and qualification operations.

### What's the difference between the sales agent and the marketing agent?

The [Sales Agent](/hermes/agents/sales-agent.md) focuses on **pipeline management, lead qualification, and deal progression**. The [Marketing Agent](/hermes/agents/marketing-agent.md) focuses on **traffic analytics, SEO monitoring, campaign performance, and content operations**. They complement each other — marketing generates leads, sales converts them.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What does the Hermes Sales Agent do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Hermes Sales Agent is an autonomous AI assistant that monitors your CRM pipeline, qualifies inbound leads against your ICP, drafts outreach sequences, flags at-risk deals, and generates daily pipeline reports on a cron schedule."
      }
    },
    {
      "@type": "Question",
      "name": "How does the sales agent qualify leads?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The agent scores inbound leads by comparing firmographic data and behavioral signals against your stored ICP criteria in canonical facts."
      }
    },
    {
      "@type": "Question",
      "name": "Can the sales agent integrate with my existing CRM?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The agent connects to HubSpot, Close CRM, and LeadConnector through CorpusIQ MCP connectors with full permission respect."
      }
    },
    {
      "@type": "Question",
      "name": "How do I customize the sales agent for my pipeline stages?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Store your deal stage definitions, activity thresholds, and ICP criteria in canonical facts. The agent references these during all pipeline operations."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between the sales agent and the marketing agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Sales Agent focuses on pipeline management and deal progression. The Marketing Agent focuses on traffic analytics and campaign performance. They complement each other."
      }
    }
  ]
}
</script>

## Related Pages

- [Agent Library — All 9 Role Configurations](/hermes/agents/)
- [Marketing Agent — Campaign & SEO Automation](/hermes/agents/marketing-agent.md)
- [Executive Agent — Calendar & Inbox Management](/hermes/agents/executive-agent.md)
- [CorpusIQ MCP Connectors — 37+ Business Tools](/hermes/mcp/connectors/)
- [Cron Scheduling Guide](/hermes/governance/scheduling/)
- [Canonical Facts — Store Business Definitions](/hermes/governance/)


*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
