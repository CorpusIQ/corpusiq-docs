---
title: The Company Atlas MCP - Trade Data and Company Registries
description: Remote MCP over customs trade data from 36 markets and company registries across eight markets, with free monthly credits.
category: Business Operations
stars: n/a (new listing)
added: 2026-10-04
source: mcpservers.org
relevance: ★★★
tags: [business-operations, trade-data, customs, company-registry, due-diligence, compliance, remote-mcp, oauth]
---

# The Company Atlas MCP

**Remote MCP server (Streamable HTTP, Google OAuth)** - the hosted server behind The Company Atlas. Two surfaces in one connection: customs trade declarations from 36 markets (look up individual shipments, rank the companies behind a product or a route, and open one company's trade by product code, partner country and counterparty) and company registry lookups across eight markets including Hong Kong and Uganda. Focused per-market paths such as `/mcp/hong-kong` and `/mcp/uganda` connect straight to a single registry when that is all you need.

```
Server type: Remote (Streamable HTTP)
Auth: Google OAuth (sign in once)
Endpoint: https://thecompanyatlas.com/mcp (per-market: /mcp/hong-kong, /mcp/uganda)
Tools: Trade search and breakdowns; per-market registry search and profiles
Pricing: Free accounts get 50 credits a month; 1 credit per call, across every market
Category: Business Operations
Built by: The Company Atlas
```

## Why This Matters for Operators

Two questions come up constantly for operators and neither is answered by internal data: who really is this company, and what does the flow of goods around a product or route actually look like. The Company Atlas answers both from public records. The trade surface returns the customs lines themselves - parties, goods, ports, weights and declared value - so an operator can see who imports what, rank the companies behind a product, and watch a route grow or shrink.

The registry surface covers eight markets: Hong Kong (search by English or Chinese name, entity type, registered address and incorporation dates, then a full profile by 8-digit BRN including former names), Uganda (companies, plus every director, secretary and shareholder with position, occupation, nationality and share amounts), and six more including UAE, Singapore, Florida, Colorado, Vietnam and India.

**The key advantage is counterparty diligence and trade research from public records, reachable from the same assistant that reads your own business data.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `Trade_search_trades` | Customs lines one shipment at a time: HS code prefix match, buyer and seller substrings (semicolon splits alternatives), date, value, country and port filters; up to 10 lines per call with the total returned for paging |
| `Trade_company_trade_volume_by_year` | Ranks matched companies by declared value and customs-line count, per calendar year |
| `Trade_hs_code_breakdown` | Trade broken down by product code |
| `Trade_partner_breakdown` | Trade by partner country |
| `Trade_year_country_breakdown` | Trade by year and country |
| `HongKong_search_companies` | Hong Kong registry search by English or Chinese name, entity type, address and incorporation date range |
| `HongKong_get_company` | Full Hong Kong profile by 8-digit BRN, including former names |
| `Uganda_search_companies` | URSB search by name, entity type, industry, active status and registration date range |
| `Uganda_get_company` | Full URSB profile by BRN: capital, former names, and every director, secretary and shareholder with share amounts |
| `Uganda_search_parties` | Every company a person or corporate body is a director, secretary or shareholder of |

National IDs, passport numbers, birth dates and personal contact details are not returned. Hong Kong covers currently active companies only and does not include directors, shareholders or filed documents - those stay with the Companies Registry at cr.gov.hk.

## Installation

Add the server URL as a custom connector in Claude (Customize, Connectors, Add custom connector), a remote server in Cursor, or any MCP-compatible client:

```
https://thecompanyatlas.com/mcp
```

Sign in with Google when prompted. For a single market, use the focused path (`https://thecompanyatlas.com/mcp/hong-kong` or `https://thecompanyatlas.com/mcp/uganda`).

## Configuration

```json
{
  "mcpServers": {
    "company-atlas": {
      "type": "http",
      "url": "https://thecompanyatlas.com/mcp"
    }
  }
}
```

Streamable HTTP transport, Google OAuth, no API key to paste. Free accounts get 50 credits a month at one credit per call, and every market is included on the free plan.

## Business Relevance

- **Supplier and customer verification** - confirm a counterparty exists, is active, and who its directors and shareholders are before extending terms.
- **Trade research** - find who imports a product into a market, or how a route has moved year over year, for sourcing and pricing decisions.
- **Competitive mapping** - rank the companies behind a product category by declared value, then open one company's trade by product code and counterparty.
- **Market expansion** - check registration activity in a new market (for example, companies incorporated in a city over a date range) before committing to it.
- **Compliance groundwork** - registry evidence for onboarding files, with the explicit reminder to re-verify at the source registry for formal use.

## Integration with CorpusIQ

CorpusIQ reads the business you are inside; The Company Atlas reads the public record around it. Before a supplier becomes a connected vendor, the registry answers who they are and who stands behind them; after they are connected, CorpusIQ's read-only connectors show what actually transacts.

A composed workflow: screen a prospective wholesale customer in Hong Kong or Uganda through the registry, check their import history on the trade surface, then let the assistant compare that public profile against your own revenue data in CorpusIQ once the relationship is live. Public records outside, operating data inside, one assistant across both.

## Limitations

- A normal account receives up to 10 customs lines per call; the response includes the total so results can be paged.
- Values are in invoice currency and markets differ (some report USD, some VND); a raw sum across rows is not a market total.
- Party name matching to company IDs is not finished for 2026 lines, so recent rows can show buyer and seller as text with an empty ID.
- Hong Kong covers active companies only, without directors, shareholders or filed documents; verify formally at cr.gov.hk.
- Registry data should be re-checked at the source before formal use; the service markets itself as research, not legal clearance.
- Year ranges reflect the declarations loaded per market; markets marked limited have thinner coverage.

## FAQ

### What is The Company Atlas?

A hosted MCP service with two surfaces: customs trade declarations from 36 markets, and company registry lookups across eight markets via focused per-market endpoints.

### Does it cost anything to start?

No. Free accounts get 50 credits a month and every market is included; one credit is used per call.

### What does the Hong Kong search return?

Active companies from the Companies Registry searched by English or Chinese name, BRN, entity type, address and incorporation dates, with former names on the full profile. Directors and shareholders are not included.

### What does the Uganda search return?

URSB-registered entities by name, type, industry, status and dates, plus every director, secretary and shareholder a company or person is tied to, with share amounts.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [registry-mcp - Company Registry Data for AI Agents](/hermes/mcp/servers/external/registry-mcp/)
- [OpenBase MCP - French Company Registry](/hermes/mcp/servers/external/openbase-mcp/)
