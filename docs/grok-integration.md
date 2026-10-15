---
title: "Grok Integration - CorpusIQ Docs"
description: "Connect CorpusIQ to Grok as a custom MCP server. Ask Grok about revenue, customers, orders, and marketing using live data from 40+ connected business tools."
canonical: "https://www.corpusiq.io/docs/grok-integration"
robots: "index,follow"
last_updated: "2026-10-14"
tags: ["grok", "grok mcp", "grok mcp server", "grok custom connector", "connect data to grok", "mcp", "business data", "ai business intelligence"]
---

# Connect CorpusIQ to Grok

Grok supports custom MCP connectors, so you can connect it to CorpusIQ and ask
questions about your business using live data from your own tools.

One endpoint. 40+ business connectors. No per-source API keys to collect.

## What you need

- A Grok account
- A CorpusIQ account with at least one data source connected
- About two minutes, one time

## Setup

1. Sign in to [CorpusIQ](https://www.corpusiq.io) and connect the tools you want
   to ask about (Shopify, QuickBooks, HubSpot, Stripe, GA4, and the rest). This
   happens on the CorpusIQ side, not in Grok.
2. Open [grok.com/connectors](https://grok.com/connectors).
3. Click **New Connector**, then select **Custom**.
4. Enter the CorpusIQ MCP server URL:

```
https://mcp2.corpusiq.io/mcp
```

5. Complete the CorpusIQ sign-in. Grok opens the CorpusIQ authorization page.
   Approve it once, and the connection persists.
6. Grok discovers the tools the server exposes. Open a new conversation and ask a
   question.

The first connection uses OAuth. You approve once in the browser and Grok keeps
the token from then on. It takes under a minute.

The server must be reachable over the public internet. The CorpusIQ endpoint is,
so no tunneling is needed.

## Questions that work well

- "What was our MRR last month?"
- "Which campaign had the best ROAS this quarter?"
- "How many orders shipped last week and what was the total value?"
- "Show me our top five customers by revenue this year."
- "Compare this month's revenue to last month."

Grok calls the CorpusIQ tools, pulls the numbers from your connected sources, and
answers with the data cited.

## How it is different from the ChatGPT integration

| | Grok (this guide) | ChatGPT integration |
|---|---|---|
| Where | grok.com connectors | ChatGPT app store |
| How | Custom MCP connector URL | One-click OAuth app |
| Auth | OAuth, approve once | OAuth, approve once |
| Best for | Grok users who want live business data in chat | Everyday chat with business data |

Both hit the same CorpusIQ endpoint and the same connected data sources.

## Troubleshooting

**Grok says the server failed to connect.**
Check the URL is exactly `https://mcp2.corpusiq.io/mcp` with no trailing slash
and no extra path.

**The authorization page does not open.**
Approve the connection manually at
`https://www.corpusiq.io/mcp-auth` and retry from Grok.

**The tools show up but answers say no data.**
The CorpusIQ account has no connectors linked yet. Sign in at
[corpusiq.io](https://www.corpusiq.io) and connect at least one source, then ask
again.

**Answers work, then stop after a while.**
The access token expired. Re-run the sign-in from the Grok connector settings to
refresh it.

**Selected tools are missing.**
CorpusIQ only exposes tools for the sources you have connected. Connect another
source in CorpusIQ and the matching tools appear.

## What CorpusIQ verifies

- The endpoint `https://mcp2.corpusiq.io/mcp` is reachable over the public
  internet and speaks the streamable HTTP MCP transport.
- Its OAuth discovery documents are published at
  `/.well-known/oauth-protected-resource` and
  `/.well-known/oauth-authorization-server`, with authorization code, refresh,
  and device grants, PKCE, and dynamic client registration.
- A standard MCP client handshake completes against it: session established and
  the full tool list discovered.

Access to your connected systems stays read-only. CorpusIQ reads from your tools
and never changes them. Grok would need separate tools and permissions of its own
to take actions on your behalf, and CorpusIQ does not grant them.

## Related

- [ChatGPT Integration](chatgpt-integration.md)
- [Perplexity Integration](perplexity-integration.md)
- [Google Gemini Integration](gemini-integration.md)
- [Supported AI Agents](supported-agents.md)
- [MCP Architecture](how-it-works/mcp-architecture.md)
