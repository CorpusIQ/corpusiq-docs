---
title: "LucidRents Building Intelligence MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Apartment building intelligence from public records for NYC, LA, and Chicago: violations, 311 complaints, rents, landlord records, and more via MCP
category: Financial Data
stars: n/a (new listing)
added: 2026-08-17
source: mcp.so GitHub issue #3612
relevance: ★★★
tags: [real-estate, property-data, landlord, rental-intelligence, public-records, remote-mcp, no-auth]
---

# LucidRents Building Intelligence MCP

**Remote MCP server (Streamable HTTP, read-only, no auth) serving apartment building intelligence from public records for New York City, Los Angeles, and Chicago.** Roughly 2 million buildings across the three metros are covered. An agent can search a building, pull its full report (violations, 311 complaints, reviews, rents, landlord), look up the landlord's portfolio record, and compare similar buildings, all without an API key or account.

```
Server type: Remote (Streamable HTTP)
Auth: None (public read-only surface)
Endpoint: https://lucidrents.com/api/mcp
Tools: 5 (building search, building report, landlord record, similar buildings, market summary)
Pricing: Free
Category: Real Estate Data
Built by: LucidRents (lucidrents.com/for-ai)
```

## Why This Matters for Operators

Property managers, landlords, investors, and tenant-side operators all need the same baseline: what is this building, who owns it, and what does its violation history say. That data lives in scattered municipal records. LucidRents packages it into five MCP tools with no auth step, so an agent can answer "give me the violation and 311 history on every building this landlord owns in Brooklyn" in one session instead of a day of public-record hunting.

The no-auth design is deliberate and scoped: only aggregated public records are served, so there is no tenant PII or payment surface to protect. That makes it safe to expose to any agent without a credential lifecycle to manage.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_buildings` | Find buildings by address or name across NYC, LA, and Chicago |
| `get_building_report` | Full building profile: violations, 311 complaints, reviews, rents, landlord, similar buildings |
| `get_landlord_record` | Landlord-level rollup: portfolio size, violation totals, worst building |
| Similar-building lookup | Compare a target building against comparable properties in the same market |
| Market summary | Area-level context for a neighborhood or submarket |

## Installation

```bash
claude mcp add --transport http lucidrents https://lucidrents.com/api/mcp
```

No account, no key, no approval screen. The first call returns data immediately.

## Configuration

```json
{
  "mcpServers": {
    "lucidrents": {
      "type": "http",
      "url": "https://lucidrents.com/api/mcp"
    }
  }
}
```

## Business Relevance

- **Property managers** screen buildings and landlords before taking on management contracts
- **Tenant-side operators** check violation and complaint history before signing a lease or negotiating concessions
- **Investors** run acquisition due diligence across a landlord's whole portfolio in one agent session
- **Real estate analysts** compare a building against similar properties with the same tool that pulls the report
- **Legal and compliance teams** assemble violation histories with citable public-record sourcing

## Integration with CorpusIQ

CorpusIQ's connectors answer the money questions (Stripe charges, QuickBooks invoices, rent-roll level revenue in your accounting system). LucidRents answers the property questions those connectors cannot: physical building history, landlord behavior, and municipal violations. A property operator can run CorpusIQ for the financial picture and LucidRents for the building picture inside the same agent session, then join the two views on address or landlord name.

## Limitations

- Brand new listing (Aug 17, 2026), no track record yet
- Coverage limited to NYC, LA, and Chicago
- Public records only: no rent-roll, lease, or tenant data
- No auth means no per-tenant scoping (not needed for the data served)
- Hosted-only: no self-host option published

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
