---
title: "Profitelligence MCP - Financial Intelligence from First-Party SEC Data"
description: "Hosted remote MCP server for financial intelligence built on first-party SEC data: insider trades, 13F holdings, 8-K summaries, OHLC prices, and FRED indicators via seven read-only tools"
category: Financial Data
stars: n/a (new listing)
added: 2026-08-18
source: "mcp.so GitHub issue #3637"
relevance: ★★
tags: [financial-data, sec-filings, insider-trading, 13f, market-intelligence, remote-mcp, oauth]
---

# Profitelligence MCP

**Hosted remote MCP server for financial intelligence built on first-party SEC data.** Seven read-only tools answer complete questions in one call: market snapshots, company deep dives, opportunity screening, position health checks, 13F institutional holdings, and semantic search across filings. Stateless pass-through design means no conversation data is stored and there is no trade execution — the server is read-only by construction.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 or API key
Endpoint: https://mcp.profitelligence.com/mcp
Tools: 7 (pulse, investigate, screen, assess, institutional, search, account_status)
Pricing: Free tier available
Category: Financial Data
Registry: io.github.profitelligence/mcp-server
Built by: Profitelligence (profitelligence.com)
```

## Why This Matters for Operators

Investors, analysts, and finance operators spend hours assembling the same picture from EDGAR: what did insiders do this week, what did the 8-K actually change, and which institutions moved their 13F positions. Profitelligence compresses that into seven one-call tools. An agent can ask "screen for companies where insiders bought within the last 30 days and the last 8-K carried positive impact scoring" and get a ranked answer instead of a day of manual filing work.

The stateless design matters for compliance-minded teams: no conversation data stored means nothing to breach, and the read-only posture means an agent cannot accidentally place a trade through the server.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `pulse` | Market snapshot: current conditions in one call |
| `investigate` | Deep dive on a company or insider |
| `screen` | Multi-signal opportunity scanning |
| `assess` | Position health check |
| `institutional` | 13F holdings and manager activity |
| `search` | Semantic search across filings |
| `account_status` | Tier and usage state for the current key |

## Installation

```bash
claude mcp add --transport http profitelligence https://mcp.profitelligence.com/mcp
```

OAuth 2.1 flow or a simple API key; a free tier is available for evaluation.

## Configuration

```json
{
  "mcpServers": {
    "profitelligence": {
      "type": "http",
      "url": "https://mcp.profitelligence.com/mcp"
    }
  }
}
```

## Business Relevance

- **Fundamental analysts** replace manual EDGAR sessions with one-call insider and filing investigation
- **Portfolio managers** run position health checks and 13F manager-activity tracking in-chat
- **Deal and corporate development teams** screen opportunities against multi-signal criteria
- **Compliance teams** get read-only, stateless market data with no execution surface to police
- **Finance operators** pair OHLC and FRED indicators with their own accounting connectors in one session

## Integration with CorpusIQ

CorpusIQ answers the books questions (Stripe, QuickBooks, Shopify, banking) while Profitelligence answers the market questions (insider flows, institutional holdings, filing impact). A finance operator runs both in the same agent session: CorpusIQ for actual cash, revenue, and invoices, Profitelligence for the market context around a target, a position, or a sector. The two join naturally on ticker or company name.

## Limitations

- Brand new listing (Aug 18, 2026), zero track record
- US-market SEC data focus; no international filings coverage
- Hosted-only: no self-host option published
- Read-only by design, so no execution workflows possible (deliberate)
- Free tier limits undisclosed at listing time

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
