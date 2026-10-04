---
title: Zensei MCP - Sector Rotation Data for Agents
description: Keyless remote MCP that gives AI agents a live sector-rotation risk index over 100+ sectors, the stocks driving each move, and a macro regime read.
category: Finance
stars: n/a (new listing)
added: 2026-10-04
source: mcpservers.org
relevance: ★★★
tags: [finance, market-data, sector-rotation, equities, macro, risk, remote-mcp, hosted]
---

# Zensei MCP

**Remote MCP server (Streamable HTTP, keyless)** - the official hosted server from Zensei that puts a live market-regime read inside an AI client. Four read-only tools and one resource expose a 0 to 100 risk index computed across 100+ sectors, the leading and lagging sectors with the stocks driving each move, and a macro risk-on / risk-off regime classification. Point a client at the URL and it lists the tools; no key, no account for the read surface. Also published in the official MCP Registry as `io.github.wegravel/zensei-mcp`.

```
Server type: Remote (Streamable HTTP)
Auth: None (keyless read surface)
Endpoint: https://www.zensei.com/mcp
Tools: 4 read-only + 1 resource (sector index, leaders/laggards, stocks driving moves, macro regime)
Pricing: Free plan available; paid tiers on zensei.com
Category: Finance
Built by: Zensei (wegravel/zensei-mcp on GitHub)
```

## Why This Matters for Operators

Operators reading markets through an assistant usually get stale, unstructured commentary. Zensei replaces that with a **single, decision-shaped index**: one number that says whether conditions are supportive or restrictive, and the sectors and tickers moving against it. The mechanism matters because the index is explicitly framed as risk, not strength - lower is healthier - so an agent can answer "is now a good time to be exposed, and to what?" without the operator assembling it from five tabs.

For founders and finance teams, that turns a vague "how are markets doing" prompt into a defensible read they can act on: rotate attention toward the sectors in favour, size risk against the regime, and cite the driving names in an investor or board update.

**The key advantage is a live, keyless, machine-readable regime read that any client can call without provisioning.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Sector index | Returns the 0 to 100 risk score across 100+ sectors with the four regime bands |
| Leading / lagging sectors | Ranks sectors as leading, lagging, improving or weakening vs the S&P 500 |
| Stocks driving each move | Names the tickers behind each sector's move |
| Macro regime read | Risk-on / risk-off classification for the broader market |

The index combines ten indicators across three layers and maps 0-20 Supportive, 20-40 Vulnerable, 40-70 Stressed and 70-100 Restrictive. A rising number means conditions are worsening.

## Installation

```bash
claude mcp add --transport http zensei-index https://www.zensei.com/mcp
```

Per-client walkthroughs are on zensei.com/mcp, and the plugin manifests for Grok Build and Claude Code live in the GitHub repo.

## Configuration

```json
{
  "mcpServers": {
    "zensei": {
      "type": "http",
      "url": "https://www.zensei.com/mcp"
    }
  }
}
```

The tools are read-only and take no arguments, so there is no scope or key to configure for the read surface.

## Business Relevance

- **Founders and operators** get a plain-language regime read before making hiring, spend or fundraising decisions.
- **Finance and FP&A teams** can fold a sector-rotation signal into planning and market commentary with citations.
- **Investor relations and fundraising** can ground updates in named sectors and tickers instead of generalities.
- **Analysts** can watch rotation across 100+ sectors without a terminal subscription.
- **Agencies and consultants** can back market-timing advice with a consistent, citable index.

## Integration with CorpusIQ

Zensei complements CorpusIQ's business-data connectors. Where CorpusIQ's Stripe, QuickBooks and Shopify connectors show how a business is actually performing, Zensei supplies the market backdrop those numbers land in, so an assistant can answer "our SaaS revenue is up 12%, is the category tailwind still there?" with a live sector read attached.

A composed workflow: pull monthly revenue from CorpusIQ's Stripe connector, pair it with Zensei's sector-rotation and regime read, and have the assistant draft a board update that frames performance against the market rather than in isolation. CorpusIQ reads the business; Zensei reads the market around it.

## Limitations

- Read-only: no positions, orders or account data, only the published index and sector signals.
- The index is a Zensei methodology, not a regulated benchmark.
- Keyless surface covers the index; deeper plans may gate additional data on zensei.com.
- Free-tier scope can change; verify current plan limits before building on it.
- No self-hosting; the server is operated by Zensei.

## FAQ

### What is the Zensei sector index?

It is a 0 to 100 risk score over 100+ sectors, where lower is healthier; it maps to Supportive, Vulnerable, Stressed and Restrictive regimes.

### Do I need an API key to use the Zensei MCP server?

No. The read tools are keyless; add the endpoint and call them.

### Can an agent trade from Zensei data?

No. The server is strictly read-only and exposes no order or position tools.

### Does it work outside US markets?

The index is benchmarked against the S&P 500 and major US sectors; global coverage is not advertised.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
