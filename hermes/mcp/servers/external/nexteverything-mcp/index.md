---
title: "Next Everything MCP - BOM Pricing and Ordering for Builds"
description: "Next Everything prices an electronics bill of materials across JLCPCB, DigiKey and Mouser, flags shortages and turns the quote into an order."
category: Manufacturing & Hardware
stars: n/a (hosted, no public repo)
added: 2026-10-21
source: "mcpservers.org /all page 1 (card nexteverything-io-docs)"
relevance: ★★★
tags: [bill-of-materials, electronics, procurement, supply-chain, component-pricing, manufacturing, inventory, remote-mcp]
last_updated: "2026-10-24"
---

# Next Everything MCP

**A bill of materials is a spreadsheet full of promises until somebody checks stock, price breaks and lifecycle status line by line. Next Everything does that check inside the assistant and returns a priced build you can order.**

```
Server type: Remote (Streamable HTTP) at https://mcp.nexteverything.io/mcp
Auth: bearer API key from the account dashboard (Authorization header)
Live check: POST initialize returned HTTP 401 Unauthorized without a key
Tools: 8 (create_project, check_bom, update_bom_line, find_parts, get_part, find_alternatives, place_order, order_status)
Catalog: 630,000+ in-stock parts from the JLCPCB/LCSC library, refreshed daily, with DigiKey and Mouser checked live per line
Vendor: Next Everything (nexteverything.io)
```

## Why This Matters for Operators

Procurement for a hardware build is a join across three distributor catalogs, a price ladder that changes with quantity, and a lifecycle risk nobody reads until the part is unavailable. The three failures that cost money are all visible only when the numbers sit side by side. A part that is in stock at one distributor but on allocation at another. A price break one unit above the quantity you planned, where buying ten more boards costs less than buying what you need. A part marked not recommended for new designs that is about to strand the next run.

The usual fix is a buyer with browser tabs, or a spreadsheet that was accurate the day it was saved. Next Everything makes the comparison the tool call: every BOM line is matched to an orderable part, priced for the quantity you actually want, and checked for stock, lifecycle status and footprint availability before you commit.

## What It Actually Does

The flow is a project, not a chat. `create_project` opens a build and returns a `project_id` and a dashboard URL that a person can watch while the agent works: current BOM, chosen part per line, price and stock, the problems found, the quotes and the orders.

`check_bom` takes the BOM as CSV or TSV text plus the board count and returns the matched lines, the per-distributor price comparison, the shipments with estimated shipping, and a `quote_id`. Problems come back flagged rather than silently repaired: out of stock, not enough stock, a part the manufacturer is phasing out, an uncertain match, an MPN and a distributor number on the same line pointing at different parts, no footprint, and the JLCPCB extended-part fee when assembly is requested. Problem lines carry alternatives, checked ones first, and unmatched lines say when the item is not an electronic component at all.

`update_bom_line` edits the project without resending the file, and re-prices the whole build, so accepting an alternative is one call and one new quote. `find_parts` searches in stock parts by part number, words, category, package, manufacturer or electrical spec, with values read as specs (`resistor 33 ohm 1/4W axial` searches through-hole 33 ohm parts of at least a quarter watt). `get_part` returns every offer with its full price ladder, datasheet, pinout and recent stock trend, and `find_alternatives` does the same for a swap. `place_order` requests an order against a quote and charges nothing: the team re-checks live stock and prices and emails a payment link, and `order_status` follows it.

Shipping economy is a real option rather than a note: `minimize_shipments` defaults to true, which moves lines to fewer distributors when the shipping saved exceeds the price difference, and `false` buys the cheapest source for every line.

## Installation

```bash
# Claude Code
claude mcp add --transport http nexteverything https://mcp.nexteverything.io/mcp \
  --header "Authorization: Bearer nx_live_your_key"
```

Create a free account at nexteverything.io/signup, copy the API key from the dashboard, and replace the placeholder. Setup guides exist for Claude Code, Claude Desktop, Cursor, Codex CLI, Windsurf and VS Code.

## Verification

Probed 2026-10-21 from the Spark host: an unauthenticated `POST initialize` to `https://mcp.nexteverything.io/mcp` returned HTTP 401, so the endpoint is live and gate-kept. Tool list and limits read from the vendor's own MCP documentation page on mcpservers.org: eight tools, request bodies over 2 MB rejected with 413, 401 for a missing or invalid key, 503 when the key cannot be checked. Quotes are in US dollars and valid 24 hours; import duties are not included and shipping is estimated per distributor.

## FAQ

### Does it order parts without asking?

No. `place_order` requests an order for a quote and charges nothing. The team re-checks live stock and price, then emails a payment link, which the caller can also see on the project dashboard.

### Where do the prices come from?

The JLCPCB/LCSC catalog is the daily-refreshed base, 630,000+ in-stock parts. DigiKey and Mouser are checked live for every BOM line, so the comparison is against current distributor stock rather than a cached snapshot.

### What counts as a problem line?

Out of stock, insufficient stock, a part the manufacturer is phasing out, an uncertain match, mismatched MPN and distributor numbers on one line, a missing footprint, and the extended-part assembly fee when JLCPCB assembles the board. Each comes back flagged with the alternatives that were checked.

## See Also

- [CorpusIQ connectors](/docs/hermes/mcp/servers/) for the read-only business data side of the same question
- [Manufacturing and hardware servers](/hermes/mcp/servers/external/) in this catalog
