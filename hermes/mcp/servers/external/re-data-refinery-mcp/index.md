---
title: "RE Data Refinery MCP - Pay-Per-Query Real Estate Intelligence"
description: "RE Data Refinery MCP server combines live Zillow data with county GIS, tax delinquency, sheriff sales, permits and probate records into scored property intelligence, paid per query in USDC on Base via x402 — no subscription"
category: Real Estate
stars: n/a (new listing)
added: 2026-08-19
source: "mcp.so GitHub issue #3648"
relevance: ★★
tags: [real-estate, property-data, investment-analysis, x402, usdc, base, zillow, flipping, wholesale]
---

# RE Data Refinery MCP

**Pay-per-query real estate intelligence: live Zillow listings enriched with county-level data and scored for investment.** RE Data Refinery turns messy property data into clean, scored, AI-ready intelligence for Columbus, OH and 14 surrounding metro cities — combining ZillAPI listings with GIS zoning, tax delinquency, sheriff sales, permits, and probate records, then computing flip score, wholesale score, rental yield, and market heat for every property.

```
Server type: Local (Python, stdio/SSE) + hosted worker
Auth: EVM wallet with USDC on Base (x402 pay-per-call)
Worker URL: https://re-data-refinery.ares-hms.workers.dev
Tools: 10
Pricing: $0.25-$0.50 USDC per lookup (free health/credits tools)
Category: Real Estate
Built by: RE Data Refinery (Columbus, OH)
```

## Why This Matters for Operators

Real estate investors stitch together MLS feeds, county records, and their own scoring spreadsheets — usually across three or four subscriptions. RE Data Refinery collapses that into one agent-callable surface with per-query micropayments: agents pay $0.25–$0.50 USDC per lookup via x402 on Base, with no subscription, no API tiers, and no minimum commitment.

The differentiator is enrichment depth: county GIS, tax delinquency, sheriff sales, permits, and probate records sit alongside standard listing fields, and proprietary flip/wholesale/rental-yield/market-heat scores come pre-computed per listing. A free local fallback mode supports development without spending USDC.

## Tools & Capabilities

| Tool | What it does | Price |
|---|---|---|
| `refinery_health` | API health, cached property count, rate limits | Free |
| `refinery_credits` | Upstream ZillAPI credit balance | Free |
| `refinery_properties` | Scored property lists by city with price filters | $0.35 (free cached) |
| `refinery_property_detail` | Full scored detail for one property (ZPID) | $0.35 |
| `refinery_property_price_history` | Price/transaction timeline | $0.25 |
| `refinery_property_tax_history` | Tax and assessment history | $0.25 |
| `refinery_property_schools` | School ratings near a property | $0.25 |
| `refinery_search` | Natural-language property search | $0.50 |
| `refinery_scored_search` | Search filtered by investment criteria | $0.50 |
| `refinery_payment_status` | x402 configuration and active API base | Free |

## Installation

```bash
pip install "x402>=2.20.0" eth-account httpx
git clone https://github.com/areshms/re-refinery-mcp.git
cd re-refinery-mcp
export EVM_PRIVATE_KEY=0x...
```

## Configuration

```json
{
  "mcpServers": {
    "re_refinery_mcp": {
      "command": "python3",
      "args": ["/path/to/re-refinery-mcp/re_refinery_mcp.py"],
      "env": {
        "EVM_PRIVATE_KEY": "${EVM_PRIVATE_KEY}",
        "X402_SPEND_CAP": "$1"
      }
    }
  }
}
```

The wallet must hold USDC on Base mainnet for paid lookups. Payments settle automatically via the x402 protocol using Permit2 signatures and the Coinbase CDP facilitator. `X402_SPEND_CAP` sets a per-payment cap (default $1). MIT licensed.

## Business Relevance

- **Flippers and wholesalers** source and score deals from chat instead of spreadsheets
- **Rental investors** filter by rental yield and market heat across 14 metro cities
- **Analysts** pull tax, price, and school histories per property on demand
- **Agent builders** fold property scoring into larger investment workflows with spend caps

## Integration with CorpusIQ

RE Data Refinery covers property sourcing and scoring — a domain CorpusIQ's connectors do not touch. Paired in one agent session, an investor can source and score properties through RE Data Refinery while CorpusIQ handles the financial layer: QuickBooks for the business books, Stripe for payments, and banking for deal funding — then join the two on property address or LLC name. CorpusIQ's x402-aware spend discipline (caps, per-call pricing) mirrors RE Data Refinery's pay-per-query model.

## Limitations

- Coverage is Columbus, OH metro (14 cities, 150+ seeded properties) — not national
- Requires a funded wallet and x402 client; USDC on Base only
- New listing (Aug 2026), zero-star repository, single maintainer
- Paid lookups depend on the hosted Cloudflare worker's uptime
- Local free mode uses a different (limited) data path than paid worker lookups

## See Also

- [Austin MLS MCP — Live Austin Real Estate Listings](/hermes/mcp/servers/external/austin-mls-mcp/)
- [Live Listing Proof MCP — Fail-Closed Listing Verification](/hermes/mcp/servers/external/live-listing-proof-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
