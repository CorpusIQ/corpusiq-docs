---
title: Nomos MCP - Brazilian Regulatory and Legislative Search
description: Read-only MCP search over Brazilian legislative and regulatory data for business operators - bills, official gazettes, central bank and regulator records, every result linking back to the Nomos app for full context.
category: Compliance
stars: n/a (new listing)
added: 2026-08-26
source: "mcp.so GitHub issue #3778"
relevance: ★★★
tags: [brazil, regulatory, legislation, compliance, government-data, due-diligence, sanctions, remote-mcp]
---

# Nomos MCP

**Remote MCP server (Streamable HTTP, API key or OAuth 2.0)** - Nomos MCP gives operators 11 read-only search tools over Brazilian legislative and regulatory data: legislative bills, the federal official gazette, state and municipal gazettes, legislative speeches, legislator social media, Central Bank (BACEN) records, securities regulator (CVM) filings, federal revenue (Receita Federal) data, sector regulator outputs (ANAC, ANEEL, ANVISA and more) and UN Security Council sanctions designations. Every result links back to the Nomos app for full context. Published under the official MCP registry name `pro.nomos/nomos-mcp`, MIT licensed, endpoint live (auth gate verified by HTTP 401 on anonymous initialize).

```
Server type: Remote (Streamable HTTP)
Auth: X-API-Key header, or OAuth 2.0 resource server (authorization header)
Endpoint: https://mcp.nomos.pro/mcp
Tools: 11 (read-only regulatory and legislative search)
Pricing: Not published on the listing
Category: Compliance
Built by: Nomos-Tech (registry pro.nomos/nomos-mcp)
```

## Why This Matters for Operators

Operating in or with Brazil means tracking rules that change constantly: a bill moving through Congress, a new norm in the Diário Oficial, a sanctions designation that blocks a counterparty, a regulator decision that redefines a market. Today that means staff time across half a dozen official portals, each with its own search syntax and document formats.

**Nomos MCP collapses that into one searchable surface agents can drive.** An operator can ask for everything published this week touching their sector, or screen a prospective partner against UN sanctions designations and federal revenue records, and get back results that each link to the official source context in the Nomos app rather than an unverifiable summary.

## Tools & Capabilities

Nomos publishes the live tool list from the endpoint (11 read-only search tools). The table below groups the documented coverage areas from the official listing.

| Coverage area | What operators can search |
|---|---|
| Legislative bills | Proposições under consideration, with linked context |
| Federal official gazette | Diário Oficial da União publications |
| State and municipal gazettes | Local norms and official acts |
| Legislative speeches | What lawmakers said on record |
| News and legislator social media | Public positioning around bills and votes |
| Central Bank (BACEN) | Monetary and financial regulation |
| Securities regulator (CVM) | Market rules and filings |
| Federal revenue (Receita Federal) | Tax and federal revenue data |
| Sector regulators | ANAC, ANEEL, ANVISA and other agency records |
| UN Security Council sanctions | Sanctions designations |

## Installation

```bash
claude mcp add nomos --transport http https://mcp.nomos.pro/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "nomos": {
      "type": "http",
      "url": "https://mcp.nomos.pro/mcp"
    }
  }
}
```

Attach the key as the `X-API-Key` header, or complete the OAuth 2.0 authorization flow on first connect. Nomos documents per-client walkthroughs on its app site.

## Business Relevance

- **Compliance officers** screen counterparties against UN sanctions designations and federal revenue records without portal hopping.
- **Legal and government affairs teams** track bills, gazette publications and regulator output in one query surface with linked official context.
- **Market entrants** research sector regulation (ANAC, ANEEL, ANVISA) before committing to a Brazilian launch.
- **Analysts** monitor legislator positioning and speeches as early signals for policy shifts.

## Integration with CorpusIQ

Nomos complements CorpusIQ's financial connectors with a compliance and regulatory layer for Brazilian operations. An agent working from CorpusIQ's QuickBooks or Stripe data can pull counterparty names and, before onboarding a Brazilian vendor or customer, run Nomos searches against sanctions designations and federal revenue records - keeping the diligence step inside the same workflow that already reads the books. For operators expanding into LATAM, Nomos feeds the risk picture while CorpusIQ handles the operational data the decision is based on.

## Limitations

- Brand new - no track record yet; the GitHub repository linked from the listing is not yet publicly accessible.
- Brazilian data only - other jurisdictions need their own sources.
- Auth required for every call - no anonymous or free tier documented on the listing.
- Read-only - search and context, no document actions or filings.
- Pricing is not published on the listing; confirm costs with the vendor before production use.

## See Also

- [GovGazette MCP - Federal Contract and Award Intelligence](/docs/hermes/mcp/servers/external/govgazette-mcp)
- [SudnoKontrol MCP - Ukrainian Vessel Registry Search](/docs/hermes/mcp/servers/external/sudnokontrol-mcp)
- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
