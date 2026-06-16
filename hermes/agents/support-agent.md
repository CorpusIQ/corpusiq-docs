# Customer Support Agent Configuration

## Role Description

The Support Agent is your first line of defense for customer inquiries — it triages incoming tickets, searches your knowledge base for answers, drafts response templates, monitors SLA compliance, and surfaces trending issues before they become support crises. It works alongside your human support team, handling the repetitive parts of ticket management so agents can focus on complex, empathy-requiring conversations.

The agent integrates with your helpdesk platform, knowledge base, CRM, and communication tools to provide context-rich ticket handling. It can classify, prioritize, and route tickets based on customer tier, issue type, and sentiment. For common issues, it drafts complete responses pulling from your knowledge base and past resolved tickets. For escalations, it prepares a full context summary so the human agent doesn't need to reconstruct the customer's history.

## Recommended Model

**Claude Sonnet 4** or **GPT-4o** — support responses require nuanced language that balances helpfulness, empathy, and brand voice. Both models handle multi-turn ticket context and can search knowledge bases effectively. For simple classification and routing tasks, **Claude Haiku** or **GPT-4o Mini** are faster and more cost-effective at scale.

## Key Skills to Load

- `ticket-triage` — Auto-classification by type, priority, and sentiment; intelligent routing to teams or agents
- `kb-search` — Semantic search across your knowledge base, docs, and past resolved tickets for answer retrieval
- `response-draft` — Generates response drafts for common issues with appropriate tone and brand voice
- `sla-monitor` — Tracks time-to-first-response and time-to-resolution; alerts on breach risk
- `trending-issues` — Detects emerging issue clusters (multiple tickets with similar keywords or error messages)
- `customer-360` — Pulls customer history, subscription tier, recent interactions, and open issues

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **HubSpot / Close CRM** | Customer profile, subscription tier, deal history |
| **Slack** | Ticket alerts, escalation notifications, trending issue flags |
| **Email (Gmail/Outlook)** | Ticket creation from email, thread tracking |
| **Stripe** | Subscription status, payment issues, refund eligibility |
| **Notion / Airtable** | Knowledge base articles, support playbooks, macros |
| **GA4 / PostHog** | Product usage data for troubleshooting |

> **Note:** Helpdesk platforms (Zendesk, Intercom, Freshdesk, Help Scout) are accessed via API integrations. Configure your helpdesk API keys in your Hermes profile and build or load the appropriate connector skill.

## Sample Cron Schedule

```cron
# Ticket triage every 5 minutes during business hours
*/5 8-18 * * 1-5 hermes skill ticket-triage --unassigned-only

# SLA breach risk check every 30 minutes
*/30 * * * * hermes skill sla-monitor --breach-risk --window 30m

# Trending issue detection every hour
0 * * * * hermes skill trending-issues --period 4h --min-cluster 3

# Daily support summary at 5:30 PM
30 17 * * 1-5 hermes skill sla-monitor --daily-summary --format slack

# Knowledge base gap analysis every Monday at 9:00 AM
0 9 * * 1 hermes skill trending-issues --kb-gaps --period last_week
```

## Quick-Start Command

```bash
hermes agent create support \
  --model claude-sonnet-4 \
  --skills ticket-triage,kb-search,response-draft,sla-monitor,trending-issues,customer-360 \
  --connectors hubspot,slack,gmail,stripe,notion \
  --profile support \
  --description "Customer support triage and response agent"
```

## Daily Workflow

Every 5 minutes during business hours, the agent scans for unassigned tickets, classifies them, and routes them to the appropriate team or queue. For low-complexity tickets (password resets, billing questions, shipping status), it drafts a complete response using knowledge base articles and ticket history. Human agents review and send with one click. Every 30 minutes it checks SLA timers and alerts the team lead if any ticket is approaching breach. At end of day, it posts a summary of tickets created, resolved, and breached to the `#support` Slack channel. On Monday mornings, it identifies knowledge base gaps — common questions with no existing article — so the team can fill documentation holes.

## Configuration Notes

Define your SLA targets (first response: 1h for P1, 4h for P2, 24h for P3) in canonical facts. Store your brand voice guidelines, common macros, and escalation paths. Map your product feature names to knowledge base article tags for accurate search. Configure which ticket fields the agent can modify vs. which require human approval.

## Extending

Add `sentiment-escalation` that detects frustrated or at-risk customers and auto-escalates. Integrate with Jira or Linear for bug report creation from support tickets. Add `self-service-optimizer` that analyzes search queries in your help center and suggests content improvements. Build a `churn-intervention` skill that flags cancellation-risk customers to the retention team.
