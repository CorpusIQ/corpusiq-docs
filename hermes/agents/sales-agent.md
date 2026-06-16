# Sales Agent Configuration

## Role Description

The Sales Agent is an AI-driven sales assistant purpose-built for the entire sales lifecycle — from lead qualification to closed-won deal. It monitors your CRM pipeline, enriches lead data, drafts outreach sequences, surfaces at-risk opportunities, and generates daily pipeline reports so your sales team spends less time in spreadsheets and more time closing. The agent operates autonomously on a cron schedule but also responds to on-demand queries like "show me all leads in the negotiation stage with no activity in 7 days" or "draft a follow-up email for the Acme Corp deal."

The agent integrates with HubSpot, Close CRM, LeadConnector, Calendly, and your email platform to provide a unified view of every prospect interaction. It can qualify inbound leads against your ICP (Ideal Customer Profile), flag accounts showing buying signals (website visits, email opens, pricing page views), and prepare weekly pipeline health summaries for sales leadership.

## Recommended Model

**DeepSeek V3** or **Claude Sonnet 4** — these models balance cost, speed, and reasoning quality for the structured analysis and natural-language drafting this role demands. For lighter deployments, **GPT-4o Mini** handles CRM queries and response drafting efficiently.

## Key Skills to Load

- `pipeline-health` — Daily pipeline snapshot: stage distribution, weighted forecast, deals at risk, deals with no recent activity
- `lead-qualification` — Scores inbound leads against ICP criteria using firmographic and behavioral signals
- `outreach-sequence` — Drafts and sequences multi-touch outreach (email, call, LinkedIn) based on persona and stage
- `meeting-prep` — Pulls deal history, contact notes, and recent communications ahead of scheduled calls
- `competitor-battlecards` — Surfaces competitive intelligence when a competitor is mentioned in the deal record

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **HubSpot / Close CRM / LeadConnector** | Pipeline tracking, deal management, contact enrichment |
| **Calendly** | Meeting scheduling and availability |
| **Email (Gmail/Outlook)** | Outreach drafting, thread tracking, response detection |
| **GA4** | Prospect website visit tracking (if relevant) |
| **Slack** | Pipeline alerts and notifications to sales channels |
| **Airtable / Notion** | Sales playbooks, ICP docs, battlecards |

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

## Daily Workflow

At 7:30 AM, the agent posts a pipeline summary to your `#sales` Slack channel showing deals by stage, weighted forecast, deals with stalled activity, and upcoming meetings. Throughout the day it monitors inbound leads, enriches them with company data, and scores them. Before every scheduled Calendly meeting, it prepares a briefing document with the prospect's history, open questions, and recommended next steps. At end-of-week, it generates a forecast report for the Monday leadership review.

## Configuration Notes

Store your ICP definition in canonical facts so the agent can reference it during qualification. Configure deal stage definitions and activity thresholds (e.g., "stale = no activity in 7 days") in your Hermes profile's configuration. The agent respects pipeline permissions from your connected CRM — it only sees and acts on deals you have access to.

## Extending

Add a `competitor-intel` skill that watches for competitor mentions in deals and pulls data from Semrush or Ahrefs. Integrate with LinkedIn Sales Navigator for social selling signals. Add deal health scoring using machine learning on historical win/loss patterns stored in your CRM.
