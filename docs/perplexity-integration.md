---
title: "Perplexity Integration - CorpusIQ Docs"
description: "Connect CorpusIQ to Perplexity through the MCP server endpoint. Ask business questions about revenue, customers, orders, and marketing from live data inside Perplexity."
canonical: "https://www.corpusiq.io/docs/perplexity-integration"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["perplexity", "mcp", "perplexity mcp server", "connect data to perplexity", "business data", "ai business intelligence"]
---

# Connect CorpusIQ to Perplexity

Perplexity supports MCP servers, which means you can point it at CorpusIQ and ask real questions about your business data inside Perplexity threads.

One endpoint. 40+ business connectors. No per-source API keys to collect.

## What you need

- A Perplexity account (any plan with MCP support)
- A CorpusIQ account with at least one data source connected
- About two minutes, one time

## Setup

1. Sign in to [CorpusIQ](https://www.corpusiq.io) and connect the tools you want to ask about (Shopify, QuickBooks, HubSpot, Stripe, GA4, and the rest). This part happens on the CorpusIQ side, not in Perplexity.
2. In Perplexity, open Settings and find the MCP servers section.
3. Add a new custom MCP server.
4. Paste the CorpusIQ endpoint:

```
https://mcp2.corpusiq.io/mcp
```

5. Connect. Perplexity opens the CorpusIQ authorization page. Approve it once, and the connection persists.
6. Start a new Perplexity thread and ask a question.

The first connection uses OAuth. You approve once in the browser and Perplexity keeps the token from then on. It takes under a minute.

## Questions that work well

- "What was our MRR last month?"
- "Which campaign had the best ROAS this quarter?"
- "How many orders shipped last week and what was the total value?"
- "Show me our top five customers by revenue this year."
- "Compare this month's revenue to last month."

Perplexity calls the CorpusIQ tools, pulls the numbers from your connected sources, and answers with the data cited.

## How it is different from the ChatGPT integration

| | Perplexity (this guide) | ChatGPT integration |
|---|---|---|
| Where | Perplexity settings, MCP servers | ChatGPT app store |
| How | Custom MCP server URL | One-click OAuth app |
| Auth | OAuth, approve once | OAuth, approve once |
| Best for | Research-style threads with live business data | Everyday chat with business data |

Both hit the same CorpusIQ endpoint and the same connected data sources.

## Troubleshooting

**Perplexity says the server failed to connect.**
Check the URL is exactly `https://mcp2.corpusiq.io/mcp` with no trailing slash or extra path.

**The tools show up but answers say no data.**
The CorpusIQ account has no connectors linked yet. Sign in at [corpusiq.io](https://www.corpusiq.io) and connect at least one source, then ask again.

**The authorization page does not open.**
Approve the connection manually at `https://www.corpusiq.io/mcp-auth` and retry from Perplexity.

**Answers work, then stop after a while.**
The token is refreshed automatically. If a connection goes stale, remove the MCP server in Perplexity and add it again. It is a 60-second redo.

## Frequently Asked Questions

**Q: Do I need a paid Perplexity plan?**
A: You need a plan with MCP support. Check Perplexity's current plan details for MCP availability.

**Q: Does this give Perplexity access to my business tools directly?**
A: No. CorpusIQ sits between Perplexity and your data sources. Perplexity can only call the CorpusIQ tools you approved, and the connection is read-only by default.

**Q: Which data sources can I ask about?**
A: All 40+ CorpusIQ connectors. See the [connectors directory](connectors.md) for the full list.

**Q: Is this the same as the MCP direct connection for agents?**
A: Same endpoint, different client. This guide is for using Perplexity as the MCP client. Agents and developers use the same URL with the device flow described in [AI Agent Users](ai-agent-users.md).

## Per-connector Perplexity guides

- **[Connect Google Sheets to Perplexity](connect-google-sheets-to-perplexity.md)** - budgets, trackers and pipelines, cited to the tab
- **[Connect Google Drive to Perplexity](connect-google-drive-to-perplexity.md)** - clauses, versions and policies from your live files
- **[Connect Google Calendar to Perplexity](connect-google-calendar-to-perplexity.md)** - where the week went and which accounts went quiet
- **[Connect Airtable to Perplexity](connect-airtable-to-perplexity.md)** - roadmaps, hiring pipelines and operating trackers
- **[Connect Klaviyo to Perplexity](connect-klaviyo-to-perplexity.md)** - what email and SMS actually earned
- **[Connect Ahrefs to Perplexity](connect-ahrefs-to-perplexity.md)** - domain ratings, ranking keywords and referring domains
- **[Connect ActiveCampaign to Perplexity](connect-activecampaign-to-perplexity.md)** - campaign performance, automation health and pipeline age
- **[Connect Dropbox to Perplexity](connect-dropbox-to-perplexity.md)** - contracts, board decks and invoices read from your folders
- **[Connect Odoo to Perplexity](connect-odoo-to-perplexity.md)** - quotations, invoices, stock and pipeline across ERP modules
- **[Connect Semrush to Perplexity](connect-semrush-to-perplexity.md)** - competitor keywords, backlinks and demand sizing
- **[Connect TikTok to Perplexity](connect-tiktok-to-perplexity.md)** - per-video performance and channel trend

## Internal Links

- **[Gemini Integration](gemini-integration.md)** - the same connection, described for Gemini
- **[AI Agent Users Guide](/ai-agent-users)** - MCP direct connection for agents
- **[Supported Agents](/supported-agents)** - MCP config for Claude, Cursor, Hermes, Windsurf
- **[CorpusIQ Quick Start](/quick-start)** - get running in under 5 minutes
- **[CorpusIQ Connectors Directory](/connectors)** - all 40+ data source integrations
- **[MCP Connection Errors](/troubleshooting/mcp-connection-errors)** - fix common connection failures

*Powered by CorpusIQ - one MCP endpoint for all your business tools.*
