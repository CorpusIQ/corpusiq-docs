---
title: Ultralayer MCP - Realtime Market Intelligence for Agents
description: Realtime financial context for AI agents - market news that separates new information from repeats, developments with impact scores, filing changes, sentiment and alerts, with evidence for every result.
category: Finance
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [market-intelligence, financial-news, sentiment, sec-filings, investor-research, alerts, evidence-linked, remote-mcp]
---

# Ultralayer MCP

**Remote MCP server (Streamable HTTP, OAuth or API key)** - realtime financial context for agents: what changed, who is affected, and what to watch next. News, events, guidance, filing changes, sentiment, stakeholder analysis and alerts, with evidence for every result and point-in-time safety for backtests.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in) or API key from console.ultralayer.ai
Endpoint: https://api.ultralayer.ai/v0/mcp
Tools: market intelligence suite (live tool list served from the endpoint)
Pricing: contact vendor; MIT plugin repo
Category: Finance
Built by: Ultralayer (ultralayer.ai), registry io.github.UltralayerHQ/ultralayer
```

## Why This Matters for Operators

Market research for agents usually means a web search plus a market-data API plus an afternoon of separating stale headlines from actual developments. **Ultralayer compresses that into one evidence-linked suite**: its news feed separates new information from repeats, developments carry company impact scores, and disclosure changes surface as filing diffs rather than "something changed somewhere".

For anyone running models against market history, the point-in-time discipline matters: backtests only see information that existed when it was published, so a strategy can't accidentally peek at the future.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Market news | Separates new information from repeats |
| Developments | Company events with impact scores |
| Guidance and outlooks | Company outlooks, disclosure changes, broader event timelines |
| Stakeholders and sentiment | Stakeholder analysis and sentiment signals |
| Alerts | Triggered alerts for watched companies |

Exact tool names are served from the live endpoint after auth; agent skills for effective use ship with the plugin.

## Installation

```bash
claude mcp add ultralayer-v0 --transport http https://api.ultralayer.ai/v0/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "ultralayer-v0": {
      "type": "http",
      "url": "https://api.ultralayer.ai/v0/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

OAuth sign-in in the browser is the alternative to a bearer key minted at console.ultralayer.ai.

## Business Relevance

- **Investor relations and strategy teams** get developments, guidance changes and stakeholder moves in one evidence-linked feed.
- **Analysts** replace headline scanning with impact-scored developments and filing diffs.
- **Quant teams** get point-in-time safety for backtests instead of hand-rolling a data freeze.
- **Operators watching competitors** get alerts on disclosure changes without reading raw filings.

## Integration with CorpusIQ

Ultralayer pairs with CorpusIQ's business-intelligence layer: market context from Ultralayer (news, filings, sentiment) sits next to internal context from CorpusIQ connectors (Stripe, HubSpot, GA4) so an operator can ask one assistant "what happened in our segment this week, and what did it do to our pipeline" and get internal and external evidence in the same answer. CorpusIQ watches the business; Ultralayer watches the market around it.

## Limitations

- Brand new listing - no track record yet.
- Pricing not published on the listing - expect to contact the vendor for plan details.
- OAuth or API key required; no anonymous read tier documented.
- Data is proprietary to Ultralayer - no public self-host option.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
