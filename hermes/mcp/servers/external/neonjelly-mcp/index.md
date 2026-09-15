---
title: "Neonjelly MCP - Shopify Store Intelligence for Agents"
description: Ecommerce intelligence over a catalog of 1.37M Shopify stores - store lists with contact and traffic filters, product and price change feeds, competitor stack teardowns and product-idea saturation research, all inside any MCP client
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-09-03
source: "mcp.so GitHub issue #3917"
relevance: ★★★
tags: [shopify, ecommerce, competitor-analysis, market-research, lead-generation, remote-mcp, api-key]
---

# Neonjelly MCP

**Remote MCP server (Streamable HTTP) for ecommerce intelligence over 1.37 million Shopify stores.** The catalog answers the questions operators, agencies and investors actually ask: who are my competitors, what are they selling and changing, what products are saturating or heating up, and which stores match a target profile. Fifty-nine tools, live-verified, keyed by identity instead of accounts - mint a trial, get a connect URL with the key embedded in the path, and ask from any MCP client.

```
Server type: Remote (Streamable HTTP)
Auth: Key-in-path connect URL, or Bearer / X-Api-Key header
Endpoint: https://mcp.neonjelly.io/mcp (connect: https://mcp.neonjelly.io/c/<njc_...>/mcp)
Tools: 59 (store resolution, market maps, competitor teardowns, dropship screening, product research)
Pricing: 14-day trial (100 calls/day, no card), paid from $29/mo
Category: Ecommerce Intelligence
Built by: Neonjelly (germanas)
```

## Why This Matters for Operators

Store intelligence that used to take a scraping project or a $5,000 data subscription now starts with one MCP connect. The tools are organized by persona - VC, competitor, dropship, merchandiser - so the same endpoint serves an operator researching a niche, an investor building a diligence pack, or a brand mapping its competitor stack. The signal layers run deep: product and price change feeds, tech-stack comparisons across stores, vendor overlap, and saturation scoring from UNTAPPED to SATURATED per product idea.

**Identity is the key.** There are no user accounts. Your connect URL carries the key, and `whoami` reports plan, quota and rate limits without metering. Trial signals-watches are gated (403) - paid plans unlock the full watch-and-alert surface.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `resolve_store` | Brand or URL to candidate stores; the card when there is one hit |
| `brief_market` / `cohort_tam` | One-page TAM: verticals, geos, movers; filtered cohort rollups |
| `find_peers` | Same vertical + country + visit band + comparison |
| `diligence_pack` | VC-grade memo for one domain: card, growth, traffic, stack, bestsellers, changes, contacts |
| `compare_stacks` | 2-8 domains: shared vs exclusive apps tagged by role |
| `competitor_moves` | Store + product changes, vertical movers, signal insights |
| `screen_dropship` / `source_map` | Dropshipper detection; SKU search grouped by vendor |
| `niche_research` | Semantic product-idea search + saturation report + stores selling the hit |
| `trending_product_ideas` | Product ideas heating up, paired with seller lists |

## Installation

Mint a trial at neonjelly.io/start (no account, no card) and paste the connect URL into Cursor, Claude, VS Code or Windsurf. Or attach the key to the bare endpoint as a Bearer header or `X-Api-Key`. Registry name: `io.neonjelly/mcp`.

## Configuration

No config beyond the key. Rate limits on the trial are 100 calls/day at 20/min, one trial per IP. `whoami` (free, unmetered) reports plan, used-today, remaining quota and expiry before you burn the budget.

## Business Relevance

D2C brands research niches and competitors before launch; agencies screen prospects by traffic and category; investors diligence store cohorts without a data team; dropshippers map suppliers and winning SKUs. All of it in chat, cited to the catalog, inside the agent that is already doing the analysis.

## Integration with CorpusIQ

CorpusIQ's 40+ connectors cover your own commerce and marketing stack (Shopify, Stripe, Google Ads, GA4). Neonjelly covers the outside world: the store catalog, competitor changes and market saturation that context for every business decision. A CorpusIQ agent answering "should we enter this category" can pull its own numbers from CorpusIQ and the market numbers from Neonjelly in the same conversation.

## Limitations

- Shopify stores only (no Amazon marketplace data)
- Signals watches (ongoing alerts) are paid-plan only; trial gets 403 on those tools
- Trial quota resets daily and is per-IP

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [BestAppify MCP - Shopify App Store Intelligence](/docs/hermes/mcp/servers/external/bestappify-mcp)
- [Mercopilot MCP - Shopify & Google Ads Operating Bridge](/docs/hermes/mcp/servers/external/mercopilot-mcp)
- [HasData MCP - Marketplace and Web Data Gateway for Agents](/docs/hermes/mcp/servers/external/hasdata-mcp)
- [Koongo MCP - Product Feed and Marketplace Operations](/docs/hermes/mcp/servers/external/koongo-mcp)
