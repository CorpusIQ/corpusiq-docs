---
title: "Jawz MCP - Live Macro Reads and a Disciplined Investing Loop"
description: "Hosted Streamable HTTP MCP with 22 read-only tools giving AI assistants a live read on the macro economy: regime classification, financial conditions, G4 central-bank balance sheets, growth and inflation indicators, an event calendar and ETF look-through, plus a four-chapter decision framework. No signup for reads."
category: Finance
stars: n/a (hosted)
added: 2026-08-27
source: "chatmcp/mcpso issue #3800 + jawz.ai/docs/mcp"
relevance: ★★
tags: [macro, economics, financial-conditions, central-banks, etf, market-data, remote-mcp]
---

# Jawz MCP

**Hosted remote MCP server (Streamable HTTP, anonymous reads with optional OAuth 2.0 identity) for live macro-economics.** Jawz gives any MCP client a live read on the macro economy through 22 read-only tools: a current regime classification (growth/inflation/liquidity with confirmation rules), financial conditions, G4 central-bank balance sheets, inflation and growth indicators, an event calendar, and ETF look-through - plus the Jawz Loop, a published four-chapter decision framework (See the World, Understand the Book, Decide, Observe & Refine) the assistant can run step by step. Reads work with no token, no email and no registration; identity is only needed to persist loop selection and raise rate ceilings.

```
Server type: Remote (Streamable HTTP)
Auth: None for reads (300 calls/day anonymous; 25/day for get_prices and get_etf_profile); optional OAuth 2.0 (DCR + PKCE) for identity tools
Endpoint: https://jawz.ai/api/mcp
Tools: 22 (all read-only)
Pricing: Free anonymous reads; email raises rate ceilings; no card mentioned
Docs: https://jawz.ai/docs/mcp · Loop guide: https://jawz.ai/docs/loop-guide
Category: Finance
```

## Why This Matters for Operators

Investors and CFOs run on macro context they currently assemble by hand from scattered FRED series, central-bank pages and news calendars. Jawz packages it as agent-callable tools with an opinionated decision framework instead of a wall of charts. **The anonymous-first design is the differentiator: an assistant can pull this week's macro read and run a Loop chapter with zero setup, no key, no signup - and the platform never stores a portfolio, only a one-way hash of loop context.** Price lookups send only ticker symbols to the data provider; identity is a bare email with no password.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_started` | What Jawz can do: first prompts and a live market read |
| `get_world_brief` | The weekly World Brief - this week's macro read |
| Loop chapter tools | Run the four chapters of the Jawz Loop (See the World, Understand the Book, Decide, Observe & Refine) and their modes, plus submit feedback on a run |
| Regime / conditions tools | Current macro regime with confirmation rules; financial conditions read |
| Central-bank tools | G4 central-bank balance-sheet data |
| Growth and inflation tools | Growth and inflation indicators |
| `get_prices` | Prices for requested symbols (25 calls/day anonymous) |
| `get_etf_profile` | ETF look-through (25 calls/day anonymous) |
| Event calendar tool | Upcoming economic events |

22 tools in total; the full list serves from the endpoint's tools/list.

## Installation

```bash
claude mcp add jawz --transport http https://jawz.ai/api/mcp
```

For reads, connect and go - no Authorization header. OAuth discovery documents are published at the standard /.well-known paths, so compliant clients discover the optional sign-in flow automatically.

## Configuration

```json
{
  "mcpServers": {
    "jawz": {
      "type": "http",
      "url": "https://jawz.ai/api/mcp"
    }
  }
}
```

Headless agents needing identity (loop persistence, feedback) run a four-call documented flow: register a client (DCR), PKCE authorize with an email, exchange for tokens. Access tokens last 24 hours; refresh tokens last 30 days and rotate on every use, with an idempotent 10-minute grace window.

## Business Relevance

- **Investors** run a disciplined macro read and decision loop inside their own AI app
- **CFOs and finance teams** pull regime, conditions and event-calendar context ahead of planning conversations
- **Analysts** get anonymous, keyless access to FRED-sourced and market-data reads with no procurement cycle
- **Operators pricing or hedging** pair macro context with company-level numbers in one thread

## Integration with CorpusIQ

Jawz supplies the external macro backdrop; CorpusIQ supplies the operator's internal numbers. An agent holding both can answer "how is our revenue trending against the current macro regime" by pulling Jawz's regime and conditions read alongside GA4, Stripe and QuickBooks data from CorpusIQ - a composed view no single tool provides. For operators in import-heavy or interest-sensitive businesses, the Jawz event calendar and central-bank tools give early context for decisions the CorpusIQ connectors later measure.

## Limitations

- Brand new - no public track record; listing submitted Aug 27, 2026
- Anonymous rate limits: 300 calls/day, 25/day for price and ETF tools
- Market data depends on third-party providers; macro series sourced from public data (FRED)
- Identity tools (loop persistence, feedback) require the OAuth flow; reads do not
- No portfolio storage by design - it is a read and framework tool, not a portfolio manager

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
