---
title: "Google Gemini Integration - CorpusIQ Docs"
description: "Connect CorpusIQ to Google Gemini as an MCP server. Ask Gemini about revenue, customers, orders, and marketing using live data from 40+ connected business tools."
canonical: "https://www.corpusiq.io/docs/gemini-integration"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["google gemini", "gemini mcp", "gemini mcp server", "connect data to gemini", "mcp", "business data", "ai business intelligence"]
---

# Connect CorpusIQ to Google Gemini

Gemini supports MCP servers, so you can connect it to CorpusIQ and ask questions about your business using live data from your own tools.

One endpoint. 40+ business connectors. No per-source API keys to collect.

## What you need

- A Gemini account with MCP support (the Gemini app or Google AI Studio)
- A CorpusIQ account with at least one data source connected
- About two minutes, one time

## Setup

1. Sign in to [CorpusIQ](https://www.corpusiq.io) and connect the tools you want to ask about (Shopify, QuickBooks, HubSpot, Stripe, GA4, and the rest). This happens on the CorpusIQ side, not in Gemini.
2. In the Gemini app, open Settings and find Extensions, then MCP servers. In Google AI Studio, use the MCP tools section instead.
3. Add a new custom MCP server.
4. Paste the CorpusIQ endpoint:

```
https://mcp2.corpusiq.io/mcp
```

5. Connect. Gemini opens the CorpusIQ authorization page. Approve it once, and the connection persists.
6. Open a new chat and ask a question.

The first connection uses OAuth. You approve once in the browser and Gemini keeps the token from then on. It takes under a minute.

## Questions that work well

- "What was our MRR last month?"
- "Which campaign had the best ROAS this quarter?"
- "How many orders shipped last week and what was the total value?"
- "Show me our top five customers by revenue this year."
- "Compare this month's revenue to last month."

Gemini calls the CorpusIQ tools, pulls the numbers from your connected sources, and answers with the data cited.

## How it is different from the ChatGPT integration

| | Gemini (this guide) | ChatGPT integration |
|---|---|---|
| Where | Gemini app or Google AI Studio | ChatGPT app store |
| How | Custom MCP server URL | One-click OAuth app |
| Auth | OAuth, approve once | OAuth, approve once |
| Best for | Gemini users who want live business data in chat | Everyday chat with business data |

Both hit the same CorpusIQ endpoint and the same connected data sources.

## Troubleshooting

**Gemini says the server failed to connect.**
Check the URL is exactly `https://mcp2.corpusiq.io/mcp` with no trailing slash or extra path.

**The tools show up but answers say no data.**
The CorpusIQ account has no connectors linked yet. Sign in at [corpusiq.io](https://www.corpusiq.io) and connect at least one source, then ask again.

**The authorization page does not open.**
Approve the connection manually at `https://www.corpusiq.io/mcp-auth` and retry from Gemini.

**Answers work, then stop after a while.**
The token is refreshed automatically. If a connection goes stale, remove the MCP server in Gemini and add it again. It is a 60-second redo.

## Frequently Asked Questions

**Q: Do I need a paid Gemini plan?**
A: You need a plan with MCP support. Check Google's current Gemini plan details for MCP availability.

**Q: Does this give Gemini access to my business tools directly?**
A: No. CorpusIQ sits between Gemini and your data sources. Gemini can only call the CorpusIQ tools you approved, and the connection is read-only by default.

**Q: Which data sources can I ask about?**
A: All 40+ CorpusIQ connectors. See the [connectors directory](connectors.md) for the full list.

**Q: Is this the same as the MCP direct connection for agents?**
A: Same endpoint, different client. This guide is for using Gemini as the MCP client. Agents and developers use the same URL with the device flow described in [AI Agent Users](ai-agent-users.md).

## Internal Links

- **[Gemini Integration](/gemini-integration)** - connect Gemini to your business data
- **[AI Agent Users Guide](/ai-agent-users)** - MCP direct connection for agents
- **[Supported Agents](/supported-agents)** - MCP config for Claude, Cursor, Hermes, Windsurf
- **[CorpusIQ Quick Start](/quick-start)** - get running in under 5 minutes
- **[CorpusIQ Connectors Directory](/connectors)** - all 40+ data source integrations
- **[MCP Connection Errors](/troubleshooting/mcp-connection-errors)** - fix common connection failures

*Powered by CorpusIQ - one MCP endpoint for all your business tools.*
