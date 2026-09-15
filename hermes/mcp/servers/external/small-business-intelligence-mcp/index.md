---
title: Small Business Intelligence MCP - Metro Records
description: "Free keyless MCP server joining 25 public-records datasets (1.57M rows) for the seven-county Minneapolis-St. Paul metro plus nine analytical frameworks for tearing down small businesses and local markets anywhere in the US; CC BY 4.0 data."
category: Business Operations
stars: "0 (new listing, 2016judea/small-business-intelligence-mcp)"
added: 2026-08-31
source: "chatmcp/mcpso issue #3856 (Aug 31, 2026 afternoon sweep)"
relevance: ★★★
tags: [mcp-server, small-business, market-research, public-records, real-estate, local-intelligence, keyless]
---

# Small Business Intelligence MCP (by Brick & Mortar)

**Free, keyless MCP server that knows where the public records are.** Brick & Mortar joins 25 public-records datasets - 1,573,968 rows covering parcels, recorded sales, assessor values, licences, permits, inspections, emergency calls, contamination, flood data and wages - for the seven-county Minneapolis-St. Paul metro, then layers nine analytical frameworks on top for tearing down a small business or a local market anywhere in the US. No account, no key, nothing to log in to.

```
Server type: Hosted, remote (Streamable HTTP), read-only
Endpoint: https://brickandmortar.dev/mcp
Auth: none (keyless, anonymous)
Registry: io.github.2016judea/small-business-intelligence
Repo: github.com/2016judea/small-business-intelligence-mcp (MIT)
Server info: small-business-intelligence v0.1.0 (live-probed Aug 31, 2026)
Tools: 11 (read-only)
Data: CC BY 4.0, also downloadable at brickandmortar.dev/datasets/
```

## Why This Matters for Operators

Joined public records are normally assembled county by county, in person or through paid data brokers. This server ships them joined, for free, over MCP.

First, **the metro dataset answers property questions directly.** What a property sold for and when, who owns it and what it is assessed at, plus permits, inspections, contamination and flood history - one tool call instead of a county-portal crawl.

Second, **the teardown frameworks are the real operator value.** Nine tools walk through structured due diligence: business teardown, competitor landscape mapping, review intelligence, local visibility audit, pricing benchmark, broker diligence prep, and market opportunity scan. Each returns a research plan grounded in which public record actually settles the question.

Third, **the compose_report tool assembles outputs into a client-ready deliverable.** Sellers, brokers and site-selection teams get a polished report from the same session that gathered the evidence.

## Tools and Capabilities

All eleven tools were live-probed and verified Aug 31, 2026:

| Tool | What it returns |
|------|-----------------|
| `data_source_atlas` | A source-first research plan: which public record actually settles a local-market or property question |
| `twin_cities_datasets` | The published MSP metro datasets with real row counts, column names and update dates |
| `twin_cities_records` | Joined public-records answers for the seven-county metro: sales, ownership, values, permits, inspections |
| `business_teardown` | Full structured teardown of one named small business: digital presence, reviews, competitive position, pricing |
| `competitor_landscape` | Local competitive set for a category and metro: true competitors vs adjacent players, saturation signals |
| `review_intelligence` | Public-review mining: complaint taxonomy, theme extraction, sentiment trajectory |
| `local_visibility_audit` | Map-pack factors, listing consistency, category selection and site fundamentals for local search |
| `pricing_benchmark` | Defensible local pricing comparison with normalization across differing service bundles |
| `broker_diligence_prep` | Pre-diligence framework for brokers and buyers, including SDE framing for owner-run businesses |
| `market_opportunity_scan` | Gap analysis for a category and metro: underserved demand, oversaturation, whitespace |
| `compose_report` | Assembles prior tool outputs into one polished, client-ready report |

## Installation

No auth, no account. Add the endpoint to any MCP client:

```json
{
  "mcpServers": {
    "small-business-intelligence": {
      "type": "http",
      "url": "https://brickandmortar.dev/mcp"
    }
  }
}
```

## Configuration

Nothing to configure. The endpoint accepts anonymous JSON-RPC; the dataset files are also available for direct download at brickandmortar.dev/datasets/ under CC BY 4.0.

## Business Relevance

- **Business buyers and brokers** run teardowns and diligence prep before a letter of intent.
- **Franchise and site-selection teams** scan local competitive saturation and visibility before committing to a market.
- **Local service operators** benchmark pricing and audit their local search presence against the competitive set.

## Integration with CorpusIQ

Brick & Mortar's local intelligence is the outside view; CorpusIQ is the inside. An operator evaluating a market can ask CorpusIQ for the books of the current business (QuickBooks, Stripe, HubSpot) and ask Brick & Mortar for the local environment: what the property sold for, who the competitors are, where pricing sits, and what the reviews say. Together they cover the two halves of a buy-side or expansion decision - internal financials and external market position - in one agent conversation.

## Limitations

- The joined 25-dataset records cover the seven-county Minneapolis-St. Paul metro only; other metros get the analytical frameworks but no joined records.
- Brand new listing: repo created Aug 8, 2026, zero stars.
- All tools are read-only; nothing writes back to any source system.
- Data recency varies by county source; treat row counts and update dates as the freshness signal.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [Worklittle Jobs MCP - Job Search and Market Data](/docs/hermes/mcp/servers/external/worklittle-jobs)
