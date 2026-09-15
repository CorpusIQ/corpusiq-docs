---
title: "LocationLists MCP - US Business Location Datasets for Agents"
description: "Keyless remote MCP server over 725 ready-to-use CSV datasets of US business locations - dealer networks, licensed contractors, retail and restaurant chains, 14.2 million locations total. Agents search datasets, preview real rows, get line-item quotes, and mint Stripe checkout links for one-time dataset purchases."
category: Business Data
stars: n/a (new listing)
added: 2026-09-11
source: mcpservers.org /all
relevance: ★★★
tags: [lead-lists, business-locations, datasets, b2b-sales, keyless, remote-mcp]
---

# LocationLists MCP

**Remote MCP server (Streamable HTTP, keyless)** - ready-to-use CSV datasets of US business locations, searchable and purchasable from chat. Each dataset is compiled from the official locator, association directory or state license register that publishes it, so an agent can find dealer networks, licensed contractors, or store chains, preview up to 10 real rows, quote line-item prices, and hand back a Stripe checkout link - nothing is charged until the human pays.

```
Server type: Remote (Streamable HTTP, stateless JSON)
Auth: None
Endpoint: https://locationlists.com/mcp
Tools: 5 live-probed (search_datasets, get_dataset, get_sample, get_quote, create_checkout)
Pricing: One-time $9-$199 per dataset by record count; emailed download link after Stripe payment
Catalog: 725 datasets + 1 bundle, 14,248,853 US business locations
Registry: io.github.kylehawke-stack/locationlists
Category: Business Data
Built by: LocationLists (locationlists.com)
```

## Tools

| Tool | Purpose |
|---|---|
| search_datasets | Find datasets by brand, product line, location type or category - returns slug, name, record count, coverage and page URL |
| get_dataset | Full record for one dataset - fields, record and state counts, refresh cadence, real last-modified date, FAQs, sample URL |
| get_sample | Up to 10 real rows from the live file, spread across the dataset, as JSON plus CSV text |
| get_quote | Line-item prices and total for one or more datasets, and flags a bundle if it covers several requested brands for less |
| create_checkout | Opens a Stripe Checkout session for a dataset and returns the payment URL and session id - charges nothing by itself |

Categories cover Healthcare, Retail, Industrial, Nonprofits, Equipment, Furniture, Breakfast, Hardware, Grills, Mattresses and Outdoor Furniture. A read-only ChatGPT profile at locationlists.com/mcp/chatgpt exposes search, dataset and sample only - no prices or checkout.

## Connection

1. No auth and no installation - point any MCP client at the endpoint as a remote Streamable HTTP server.
2. Claude Code one-liner - `claude mcp add --transport http locationlists https://locationlists.com/mcp`
3. First moves - `search_datasets` for a brand or location type, `get_sample` to preview real rows, `get_quote` for the price, then `create_checkout` to hand the buyer a payment link.

## Verification (Sep 11, 2026 evening sweep)

Endpoint live-probed over JSON-RPC: keyless `tools/list` returned the full tool set with input schemas (category enums, 1-50 limit bounds, row caps) and read-only annotations on the first four tools. The registry listing (server.json in the repo) matches the live surface, and the live catalog.json dated 2026-09-11 reports the 725-dataset, 14.2M-location figures above.

## See Also

- [GoodLeads MCP - New-Business Leads for Agent Outreach](/docs/hermes/mcp/servers/external/goodleads-mcp)
- [Crawdar MCP - Qualified Prospect Research for Agents](/docs/hermes/mcp/servers/external/crawdar-mcp)
- [LeadGen MCP - Company Registry Lookups and Domain Audits](/docs/hermes/mcp/servers/external/leadgen-mcp)
