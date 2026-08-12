---
title: Stratyfix MCP
description: Sales intelligence connector for MCP agents — 10 read-only tools over live pipeline, forecasts, pace-to-target, and coaching data, with per-user OAuth permissions
category: Sales
stars: n/a (commercial)
added: 2026-08-12
source: mcp.so
relevance: ★★★
tags: [sales, sales-intelligence, crm, forecasting, pipeline, b2b, remote-mcp]
---

# Stratyfix MCP

**Remote MCP server (Streamable HTTP, OAuth) for Stratyfix.** An AI-driven sales intelligence platform connector that lets managers and reps ask about their own Stratyfix data inside the chat they already use: "Are we going to make the quarter?" "Who needs my attention this week?" The answers come from the live platform — read only, with every person connecting as themselves under the same permissions as the app.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (per-user permissions)
Endpoint: https://app.stratyfix.com/api/mcp
Setup guide: https://app.stratyfix.com/connect
Category: Sales / Sales Intelligence
```

## Why This Matters for Operators

Forecast questions have an answer in your CRM — usually buried across ten screens. Stratyfix MCP collapses that: the quarter as the manager surfaces show it, in one tool call, with an honesty rule the category doesn't have. When Stratyfix withholds a number on purpose — odds not calibrated yet, target not set — the connector says exactly that instead of guessing. A null narrated as withheld is correct behavior, and it's the difference between a forecast you can act on and one you can't.

## Tools & Capabilities

- `my_deals` — your open deals, forecasts, and next moves
- `my_deal_risk` — one deal's forecast receipt, with honest uncertainty
- `my_pace` — your pace to target
- `coaching_queue` — who needs coaching next, with the evidence
- `team_target_odds`, `team_coverage`, `team_pace`, `team_gap_ledger` — the quarter as managers see it (managers/admins only)
- `triage_proposals` — deals proposed for dropping, decided in the app only
- `deal_brief` — one deal's strategy brief (managers/admins only)

## Installation

```bash
claude mcp add stratyfix --transport http https://app.stratyfix.com/api/mcp
```

Requires a Stratyfix workspace with the connector enabled by an administrator. Full guide: [app.stratyfix.com/connect](https://app.stratyfix.com/connect). Support: tejas@stratyfix.com.

## Configuration

```json
{
  "mcpServers": {
    "stratyfix": {
      "type": "http",
      "url": "https://app.stratyfix.com/api/mcp"
    }
  }
}
```

First connect opens a browser window for OAuth authorization; credentials are reused for future sessions.

## Business Relevance

- **Sales managers** get the quarter's coverage, pace, and gap ledger in chat — no dashboard exports
- **Reps** get their own deals, risks, and pace without pestering ops for pulls
- **Revenue leadership** gets coaching queues with evidence, not vibes
- **The honesty rule** means forecasts surface uncertainty instead of manufacturing false precision — exactly what board-level reporting needs

## Integration with CorpusIQ

Stratyfix composes with CorpusIQ's CRM and finance connectors as the "why" layer above the raw data: CorpusIQ pulls the books and pipeline state (HubSpot/CRM, QuickBooks, Stripe revenue), and Stratyfix supplies the forecast reasoning — odds, coverage, coaching evidence — that raw pipeline numbers can't produce. An agent can answer "how likely are we to hit the quarter, and where should we coach?" by joining the two, which is precisely the workflow a revenue team currently pays a rev-ops analyst to run manually.

## Limitations

- Requires a Stratyfix workspace with admin-enabled connector — not self-serve
- Read-only by design — updates and deal decisions stay in the app
- OAuth per-user permissions mean the agent sees only what the connected user sees
- Commercial platform; early-stage (listed on mcp.so Aug 12, 2026)
- No self-hosted option

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
