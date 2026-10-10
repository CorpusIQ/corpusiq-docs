---
title: "PackIndex MCP - Packaging Cost Index for Your Agent"
description: "Live packaging cost indices, forecasts and quote checks for operators: materials, finished packs, carbon scores and supplier quotes, answered in chat."
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-10-10
source: "mcpservers.org /all (page 2) + vendor site opnplatform.com; catalogued at the October 10, 2026 midday sweep"
relevance: ★★★
tags: [packaging, supply-chain, e-commerce, procurement, market-data, oauth, remote-mcp]
---

# PackIndex MCP

**Remote MCP server that puts the packaging cost index inside your assistant** - live prices for the raw inputs, materials, semi-finished goods and finished packs that make up packaging, plus 12-week forecasts, carbon scores, supplier quote checks and RFQs to suppliers, answered in the conversation where sourcing decisions already happen. The fresh business-relevant find of the October 10 midday sweep, catalogued with the endpoint probed live (keyless initialize returns 200; `tools/list` shows all 26 tools).

```
Server type: Remote (Streamable HTTP at https://opnplatform.com/api/mcp)
Auth: OAuth 2.1 with scoped permissions (read indices, Design Studio, PACKIQ agents, Trade Exchange RFQs); an opn_ API key works as a Bearer token for scripts
Tools: 26 - 18 callable without sign-in and 8 account tools (Design Studio, Trade Exchange, PACKIQ agents)
Indices: 426 live indices across raw inputs, materials, semi-finished and finished packs, refreshed every 5 minutes
Category: Commerce & E-Commerce
Built by: OPN (opnplatform.com; PackIndex at opnplatform.com/data)
```

## Why This Matters for Operators

Packaging is one of the largest controllable cost lines for any business that ships a physical product, and the market moves on commodity inputs - oil, gas, power, recovered fibre, resins, pulp. Most teams price it once a quarter from supplier quotes and find out too late that the input side moved. PackIndex hands the live index to the assistant: check whether a supplier quote is fair against the benchmark before signing, see where a material sits in its 12-month range, recalculate an index-linked contract, or forecast next quarter - inside the same thread where the sourcing decision is being made. Pricing, transparency and timing land in one place.

## Tools & Capabilities

| Tool group | What it covers |
|---|---|
| Search and read | `search_indices` (find codes by material, input, format or plain words), `get_live_index`, `get_prices` (up to 20 codes in one call for watchlists), `get_index_history` (every point for up to 3 months, weekly closes beyond), `get_all_indices`, `get_market_movers` (biggest risers and fallers by layer and window) |
| Explain and compare | `compare_regions` (one material across regions), `explain_price_move` (splits a change into its inputs over 1w to 1y), `packindex_query` (plain-English questions about costs or which agent to use) |
| Benchmark checks | `check_quote` (a supplier price vs the PackIndex benchmark: difference, FAIR / HIGH / LOW verdict, 12-month range position and, with a quantity, the overpayment), `price_adjustment` (recalculate an index-linked contract price), `get_carbon_index` (kg CO2e with A-D grades) |
| Forward-looking | `get_index_forecast` (12-week projection with confidence), `estimate_packaging_price` (corrugated RSC box price from dimensions and flute, with a low/mid/high band and next-quarter projection) |
| Design Studio | `draft_packaging_spec`, `cost_packaging_spec`, `compare_packaging_options`, `update_project`, `list_my_projects` - brief to spec, bill of materials anchored to live index values, right-size / lightweight / substitute options with cost and carbon savings (uses Suite runs) |
| Trade Exchange | `find_suppliers`, `search_exchange_listings`, `post_rfq` (request quotes from up to 3 suppliers), `get_my_rfqs` |
| PACKIQ agents | `list_packiq_agents`, `get_agent_chain`, `run_packiq_agent` - procurement, manufacturing, compliance, finance and logistics co-workers (uses PACKIQ credits) |

## Installation

```json
{
  "mcpServers": {
    "packindex": {
      "url": "https://opnplatform.com/api/mcp"
    }
  }
}
```

Claude Code: `claude mcp add --transport http packindex https://opnplatform.com/api/mcp`. The first tool that needs your account opens the OPN sign-in (OAuth); scripts can send an `opn_` API key as a Bearer token instead.

## Configuration and Safety

- Per-user connections: every connection carries the user's own plan, runs and credits; `packindex:read` is always included and the other scopes (Design Studio, PACKIQ, Trade Exchange) can be unticked at consent.
- The read tools need no sign-in (live values with Essential and above). Design Studio, PACKIQ and Trade Exchange tools are labelled creates-or-changes-data and operate on your account.
- RFQs send through the OPN Trade Exchange within your plan's monthly limits (up to 3 suppliers per request); nothing is bought or paid for by the server.
- The server advertises the MCP Apps UI extension, so clients that support it can render richer views of index data.

## Business Relevance

- **E-commerce and DTC brands**: check packaging quotes against a live benchmark before committing, and forecast the box cost for next quarter's volumes.
- **Procurement and sourcing teams**: recalculate index-linked contracts when inputs move, and pull supplier offers with their benchmarks in one conversation.
- **Finance and operations**: carbon scores (Green Index) per pack with A-D grades feed sustainability reporting without a separate data pull.

## Integration with CorpusIQ

The market side and your own numbers answer different halves of the same question. Ask PackIndex what materials and finished packs cost right now, then ask CorpusIQ for your own inputs from the connectors you already have - Shopify for orders and product costs, QuickBooks for spend, Stripe for revenue. The benchmark and your business picture land in one conversation, with every number traceable to its source.

## Limitations

- Read tools work without sign-in, but the depth of live data follows your plan (live values on Essential and above; some Exchange surfaces fall back to delayed data on lower tiers).
- Account tools spend plan resources: Design Studio uses Suite runs, PACKIQ uses credits, RFQs count against monthly Exchange limits.
- The per-box price estimate covers corrugated RSC (FEFCO 0201) directly; other formats go through Design Studio.
- Supplier coverage follows the OPN Trade Exchange network, so availability varies by material and region.

## FAQ

### Do I need an account to use PackIndex MCP?

No for the read tools - search, live indices, history, forecasts, carbon scores, market movers, region compares, price-move explanations, quote checks, index-linked price adjustments, box price estimates and supplier search all work without sign-in, with live values on the Essential plan and above. Design Studio, Trade Exchange and PACKIQ tools need an OPN account and use your plan's runs, credits or RFQ limits.

### What can the agent actually answer?

Live and historical packaging prices across raw inputs, materials, semi-finished goods and finished packs; 12-week forecasts; carbon scores with A-D grades; biggest risers and fallers; why a price moved; whether a supplier quote is fair against the benchmark; index-linked contract recalculation; and a corrugated box price from dimensions and flute.

### Can the agent commit me to anything?

It can draft and cost packaging specs, run PACKIQ agents and send RFQs to up to 3 suppliers through the Trade Exchange within your plan's monthly limits - each of those is a labelled account action using your own runs or credits. The read tools cannot change anything.

## See Also

- [SoldFetch MCP - eBay Market Data for Your Agent](/hermes/mcp/servers/external/soldfetch-mcp/)
- [Datrace MCP - Amazon Market Data for Your Agent](/hermes/mcp/servers/external/datrace-mcp/)
- [Gemalli B2B Trade MCP - Global Wholesale Sourcing for Agents](/hermes/mcp/servers/external/gemalli-b2b-trade-mcp)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
