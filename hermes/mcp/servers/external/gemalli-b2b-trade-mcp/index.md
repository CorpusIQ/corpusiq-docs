---
title: "Gemalli B2B Trade MCP - Global Wholesale Sourcing for Agents"
description: "Hosted remote MCP for global B2B trade: wholesale product search with category/country/MOQ/price filters, verified manufacturer catalog, sanctions screening and HS codes. No auth for the read toolset. Endpoint gemalli.com/api/mcp, live-verified."
category: Commerce
stars: "n/a (hosted service)"
added: 2026-08-31
source: "chatmcp/mcpso issue #3859 (Aug 31, 2026)"
relevance: ★★★
tags: [mcp-server, b2b, trade, sourcing, manufacturers, sanctions, hs-codes]
last_updated: "2026-10-19"
---

# Gemalli B2B Trade MCP

**Wholesale sourcing, agent-native.** Gemalli is a global B2B trade platform where manufacturers, buyers and trade agents close deals directly, themselves or through their AI agents. Its MCP server exposes the read side: search wholesale products with category, country, MOQ and price filters, inspect product details, browse a verified manufacturer catalog, and screen counterparties with sanctions and HS-code data.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://gemalli.com/api/mcp
Auth: none for the read toolset
Protocol: MCP 2025-06-18
Registry: com.gemalli/trade (domain-verified)
Tools: 9 (search_products, get_product, list_manufacturers, get_manufacturer, sanctions/HS-code screening, ...)
Built by: Gemalli (gemalli.com)
```

## Why This Matters for Operators

Sourcing and vendor qualification are slow, trust-heavy workflows. Gemalli gives an agent the trade side of the picture.

First, **structured wholesale data.** Category, country, MOQ and price filters mean an agent can answer "which verified manufacturers in Vietnam make small-batch packaging under $0.40/unit" instead of sending the buyer down a directory rabbit hole.

Second, **verification is built in.** The manufacturer catalog carries verification status, so the agent's answer distinguishes vetted suppliers from listings.

Third, **compliance context.** Sanctions screening and HS codes inside the same server mean a sourcing answer can carry the trade-compliance signals an operator would otherwise look up separately.

## Tools and Capabilities

| Tool | Purpose |
|------|---------|
| `search_products` | Wholesale product search with category, country, MOQ and price filters |
| `get_product` | Product detail: specs, price range, MOQ, images, manufacturer |
| `list_manufacturers` | Catalogue of verified manufacturers |
| `get_manufacturer` | Manufacturer profile and verification status |
| Trade compliance tools | Sanctions screening and HS-code data on the read toolset |

## Verification (Aug 31, 2026)

- **Live JSON-RPC initialize verified**: POST to `https://gemalli.com/api/mcp` returned `gemalli-mcp v0.1.0` with tools capability and instructions describing the B2B trade platform and sourcing tools.
- Submission (#3859) documents 9 tools, no-auth read toolset, and the official registry record `com.gemalli/trade`.
