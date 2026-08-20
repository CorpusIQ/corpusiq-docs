---
title: "SavePropTax MCP - California Prop 8 Property Tax Appeals"
description: "Hosted keyless MCP server for California Proposition 8 property tax appeals: free over-assessment checks against recent comparable sales, county form preparation, and owner-completed filing at a flat $29 fee, with the agent never handling signatures or payments"
category: Finance
stars: n/a (new listing)
added: 2026-08-20
source: "mcp.so homepage new arrival (Aug 20, 2026)"
relevance: ★★
tags: [property-tax, real-estate, tax-appeals, california, proposition-8, remote-mcp, keyless]
---

# SavePropTax MCP

**Free, keyless California property tax appeal checks with a $29 owner-completed filing path.** SavePropTax tells an agent whether a California home is over-assessed: it compares the county assessment against recent comparable sales, estimates the annual savings from a Proposition 8 decline-in-value review, and — for qualifying properties — prepares the county's own form and emails a signing link to the homeowner. Checking can only ever lower a tax bill, never raise it.

```
Server type: Hosted remote (Streamable HTTP)
Endpoint: https://saveproptax.com/mcp
Auth: None (keyless, stateless)
Tools: 3
Pricing: Free eligibility checks, flat $29 filing fee paid by the homeowner
License: MIT
Built by: SavePropTax (saveproptax.com)
```

## Why This Matters for Operators

California property owners leave real money on the table every year: when comparable sales support a lower value than the county's assessed value, Proposition 8 lets the owner request a decline-in-value review — but most owners never check, and the filing is paperwork. SavePropTax collapses that into three agent-callable tools with a hard governance rule baked in.

The rule that shapes everything: an agent never handles the signature or the money. The signing link goes to the owner's inbox; the owner reviews the county's own form, signs, and pays. The worst an anonymous caller can do is spend a free check and send a real homeowner a legitimate link to their own property.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `check_property_tax_savings` | Free check of one California home: status, current assessment, comparable-sales opinion of value, and estimated annual savings; qualifying results carry a `continueToken` |
| `start_filing` | Prepares the county Prop 8 decline-in-value form and emails a signing link to the owner; the link is never returned to the client |
| `get_filing_status` | Coarse status only: `awaiting_signature`, `awaiting_payment`, `filed`, `delivered`, `unknown` — no personal information |

Statuses to handle: `qualifies` (the only status carrying a `continueToken`), `fair_assessment`, `not_enough_data`, `not_residential`, `window_closed`, `county_not_served`, `already_filed`, and `address_not_found`.

## Installation

```json
{
  "mcpServers": {
    "saveproptax": {
      "type": "http",
      "url": "https://saveproptax.com/mcp"
    }
  }
}
```

Nothing to install. The server is hosted, stateless, and requires no authentication.

## Configuration

No keys, no configuration. The same capability exists as a plain keyless HTTP API (`/api/agent/check`, `/api/agent/prepare`, `/api/agent/status`) for non-MCP integrations. MIT licensed.

## Business Relevance

- **Property owners** get a free annual over-assessment check without a tax consultant
- **Real estate and wealth advisors** run portfolio-wide checks across client properties
- **Property managers** screen for qualifying units and hand owners a filing-ready link
- **Agent builders** fold tax-savings checks into home-buying and investment workflows

## Integration with CorpusIQ

SavePropTax covers California property tax appeals — a niche CorpusIQ's connectors do not touch. Paired in one session, an advisor can check every client property through SavePropTax while CorpusIQ handles the portfolio layer: QuickBooks for the books, Stripe for advisory billing, and email for the owner-facing signing-link follow-up — then join the two on property address. The $29 owner-paid model matches CorpusIQ's pay-per-value discipline.

## Limitations

- California only, and only for residential parcels in served counties
- Filings are prepared, not submitted by the service; the owner signs and pays
- Coarse filing status by design — no personal information exposed to agents
- New listing (Aug 2026), zero-star repository, single maintainer

## See Also

- [RE Data Refinery MCP — Pay-Per-Query Real Estate Intelligence](/hermes/mcp/servers/external/re-data-refinery-mcp/)
- [Austin MLS MCP — Live Austin Real Estate Listings for AI Assistants](/hermes/mcp/servers/external/austin-mls-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
