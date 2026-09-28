---
title: Gloom MCP - Bloomberg-Style Financial Terminal for AI Agents
description: "Gloom Cloud's MCP server gives agents quotes, financials, options, SEC filings, macro and news wire, with OAuth or per-agent keys."
category: Finance
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + gloom.sh/docs"
relevance: ★★★
tags: [financial-data, market-data, sec-filings, options, macro, equities, research-terminal, remote-mcp]
---

# Gloom MCP

**The research tools behind Gloom's own assistant, exposed to any agent.** Gloom Cloud hosts a Model Context Protocol server at `https://api.gloom.sh/mcp` that serves the same tools the Gloom terminal uses: quotes, price history, financials, holders, analyst research, options, SEC filings and insiders, macro data, congressional trades, short interest, options flow, the news wire, an equity diagnostic and hiring data. With the right access it also reaches notes, teams, team watchlists, portfolios and connected brokers. Nothing runs on the operator's machine; it is part of Gloom Pro.

```
Server type: Remote (Stateless Streamable HTTP)
Auth: OAuth browser sign-in, or per-agent bearer keys (x-api-key also accepted)
Endpoint: https://api.gloom.sh/mcp
Tools: market, company, filing, macro, news plus notes/teams/brokers by access tier
Pricing: part of Gloom Pro (gloom.sh/cloud)
Category: Finance
Built by: Gloom (gloom.sh)
```

## Why This Matters for Operators

Financial research is a context-switching problem: filings in one window, fundamentals in another, ownership and flows somewhere else. Gloom compresses that into one authenticated endpoint, so an agent can assemble a company picture, check who traded and when, pull the SEC filings behind a claim and watch the news wire without leaving the conversation.

The access model is unusually operator-friendly. Keys are created per agent (up to 10), carry fixed access levels and an optional team pin, and `tools/list` only returns what the caller may call. Signed-in clients get the same levels through `mcp:read` and `mcp:write` scopes that can be unticked on the consent screen. Personal notes always stay the account owner's own.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Market data | Quotes and price history |
| Company data | Financials, holders, analyst research |
| Options | Options chains and options flow |
| Filings and insiders | SEC filings and insider activity |
| Macro and flows | Macro data, congressional trades, short interest |
| News | The news wire and equity diagnostic |
| Hiring data | Company hiring signals |
| Workspace | Notes, teams, watchlists, portfolios, brokers by tier |

## Installation

```bash
claude mcp add --transport http gloom https://api.gloom.sh/mcp
```

The first call opens a browser tab to sign in and choose what the client may reach. For scripts and cron jobs, create a key in Cloud settings under Agents and send it as a bearer header.

## Configuration

```json
{
  "mcpServers": {
    "gloom": {
      "type": "http",
      "url": "https://api.gloom.sh/mcp"
    }
  }
}
```

Stateless transport returns one JSON reply per POST. Access tokens live two hours; request `offline_access` for a refresh token.

## Business Relevance

- **Investors and analysts** assemble company research in one conversation
- **Founders** get competitor financials, filings and hiring signals on demand
- **Finance teams** pin keys per agent and per team for controlled access
- **Operators tracking markets** get macro, flows and news without a terminal seat

## Integration with CorpusIQ

Gloom pairs with CorpusIQ's finance connectors: QuickBooks and Stripe give the internal view of a business while Gloom supplies the external market view, and a CorpusIQ recap can hold both. For companies tracked in HubSpot through the CorpusIQ CRM connector, Gloom's hiring and filing signals can trigger re-engagement lists.

## Limitations

- Market, company, filing, macro and news tools sit behind Gloom Pro
- Broker data depends on which brokers are connected in Gloom
- Keys are shown once at creation and fixed at their access level
- New listing; the MCP surface is part of a paid cloud product

## FAQ

### How do keys and scopes work?

Keys are created per agent, carry fixed access levels and an optional team pin, and tools/list only returns what the caller may call.

### What access levels exist?

Market data, read (notes, collections, broker tools) and read-write (notes.save, collections edits).

### Do access tokens expire?

Yes. Tokens live two hours; request offline_access for a refresh token.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
