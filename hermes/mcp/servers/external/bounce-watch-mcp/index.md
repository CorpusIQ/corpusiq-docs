---
title: Bounce Watch MCP
description: Company signal intelligence over MCP — dated funding, hiring, partnership and distress events across three million records, so agents know what changed at a company and when.
category: Marketing
stars: n/a (new listing)
added: 2026-08-17
source: mcp.so
relevance: ★★★
tags: [sales-intelligence, buying-signals, company-data, funding, prospecting, market-intelligence, oauth, remote-mcp]
---

# Bounce Watch MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** — Bounce Watch answers the timing question about a company: not who they are, but what changed there and when. Three million dated events across 39 types — funding rounds, senior hires, office openings, expansions, partnerships, named customer wins, certifications, layoffs and distress indicators — each weighted 1 to 10 so an agent ranks by substance instead of counting rows.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (browser flow) or X-API-Key header
Endpoint: https://api.bouncewatch.com/api/v1/mcp
Tools: 10 (8 read-only, 2 gated writes) + 5 ready-made workflow prompts
Pricing: 2,500 free credits, no card; paid from 99 EUR/month
Category: Marketing
Built by: Bounce Watch (bouncewatch.com)
```

## Why This Matters for Operators

Sales and market intelligence usually fails on the same axis: it tells you who a company is, not when it became interesting. A prospect that just closed a Series B, opened an office in your territory, or hired a VP of the exact function you sell is five times more likely to answer your email than the same company three months earlier. Bounce Watch gives the agent the dated event trail, with sources, so the outreach is timed rather than hoped.

**The weighting model is the differentiator**: a closed funding round and a conference booth are not the same fact, and the 1-to-10 event weights encode that. An agent can rank a market by substance — which companies show momentum but have not raised yet, which accounts are showing risk signals like senior departures or layoffs — instead of producing a flat list of names.

Two design choices protect against confident nonsense. Every response carries a coverage block stating whether an empty signal list means anything, and the server instructions tell the model not to call a company quiet on stale coverage. Invalid filter values are rejected with the list of valid ones. The two write tools (on-demand re-scan, standing watch) are annotated so a client can gate them behind approval.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Company event lookup | Dated, sourced events for one company — funding, hires, offices, wins |
| Market scanning | Companies in a market that raised recently or are hiring a given function |
| Account-change queries | What moved across a list of accounts since a given date |
| Momentum detection | Companies showing momentum that have not raised yet |
| Risk scanning | Senior departures, layoffs and distress indicators on existing accounts |
| Register watch | Standing watch delivering the next matching event to a webhook |

Ready-made prompts: pre-round radar, why-now for an account, funded-and-hiring, account brief, and risk scan. Watches push out of band to a webhook, so the agent finds out when the event happens rather than when someone asks.

## Installation

```bash
claude mcp add bouncewatch --transport http https://api.bouncewatch.com/api/v1/mcp
```

The first connect opens a browser for OAuth approval. Clients without OAuth send an API key as the `X-API-Key` header. The MCP server shares the key and credit pool with the Bounce Watch REST API — no separate subscription.

## Configuration

```json
{
  "mcpServers": {
    "bouncewatch": {
      "type": "http",
      "url": "https://api.bouncewatch.com/api/v1/mcp"
    }
  }
}
```

## Business Relevance

- **Sales teams** get funded-and-hiring lists and why-now context for every account before the first email
- **Founders** can watch competitor moves — offices, hires, partnerships — as dated events with sources
- **Investors and analysts** can scan markets for momentum signals before the round is announced
- **Account managers** get risk signals on existing customers before the churn conversation happens
- **Recruiters** can time outreach against funding rounds and leadership changes

## Integration with CorpusIQ

Bounce Watch pairs naturally with the CorpusIQ CRM connectors. An agent can pull funded-and-hiring companies from Bounce Watch and match them against HubSpot deals and contacts through the CorpusIQ CRM connector, then draft the outreach with the same session's context. Account risk signals feed the CRM directly — a distress event on a key account becomes a task, not a discovery. For the demand side, Bounce Watch's buying signals compose with CorpusIQ GA4 and email analytics: signal dates explain traffic and engagement spikes in the cross-source attribution view. The 2,500 free credits make the pairing testable without budget approval.

## Limitations

- Brand new — no track record yet; submitted to mcp.so August 17, 2026
- Coverage is Europe-weighted (EUR pricing, vendor is European); verify US depth against your target market
- Credit-metered — heavy market scans consume the 2,500 free credits quickly
- Write tools (re-scan, watch registration) spend credits and should be approval-gated
- Signal data is as current as the vendor's event pipeline; validate critical events against primary sources

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
