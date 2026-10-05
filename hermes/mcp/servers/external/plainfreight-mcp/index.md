---
title: "Plain Freight MCP - China to US Freight Quotes for Agents"
description: "Keyless MCP for China-to-US freight: rough estimates, goods checks, delivered-duty-paid offers and shipment tracking, 100 g to 2,000 kg door to door."
category: Commerce & E-Commerce
stars: n/a (hosted service, plainfreight.com)
added: 2026-10-05
source: "chatmcp/mcpso issue #4737 (com.plainfreight/quotes)"
relevance: ★★
tags: [logistics, freight, imports, china, ecommerce, shipping, keyless, remote-mcp]
---

# Plain Freight MCP

**Freight quotes from China to a US address, without a sales call.** Plain Freight runs the same pricing engine a human customer is quoted from, and exposes it as an open MCP endpoint: one all-in delivered-duty-paid number covering freight, US customs clearance, import duty and delivery, for shipments from 100 g to 2,000 kg, door to door. No API key, no signup, no waiting for a rep to email back.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: None (keyless); fair-use limits of 20 offers per hour per IP and 4 per email address
Endpoint: https://plainfreight.com/api/mcp
Server: plain-freight v1.0.0 (live initialize handshake captured)
Tools: 5 (estimate_price, check_goods, generate_offer, check_offer_status, track_shipment)
Coverage: China to US, 100 g to 2,000 kg, door to door
Built by: plainfreight.com
```

## Why This Matters for Operators

Landed cost is the number importers get wrong most often: the quote that matters includes customs clearance and duty, not just freight. Plain Freight returns exactly that as one delivered-duty-paid figure, and says which mode the duty treatment applies to (included on door to door air and sea, paid at import on air consolidation). For a business pricing a product from a Chinese supplier, that turns "what will this actually cost to my door" into a two-tool question an agent can answer while the sourcing conversation is still open.

## Tool Surface

| Tool | What it does | Records |
|---|---|---|
| estimate_price | Rough price for a shipment | Nothing |
| check_goods | Whether goods can ship from China to the US and which documents they need | Nothing |
| generate_offer | Prices a real shipment and returns the offer | A quote request |
| check_offer_status | Reads the result of the second check on an offer | Read-only |
| track_shipment | Reads a booked shipment from its tracking link | Read-only |

After a firm offer, the vendor runs a second check that verifies volumetric weight, goods class and certifications, and can surface follow-up questions or hold the offer for a person.

## Authentication

None. The endpoint is open and stateless: initialize and tool calls need no account, and the vendor applies fair-use limits of 20 offers per hour per IP and 4 per email address, with programmatic volume available on request. For agents that can only send email, the vendor accepts quote requests by email and replies in the same thread.

## Installation

Claude Code:

```bash
claude mcp add --transport http plainfreight https://plainfreight.com/api/mcp
```

Cursor and other clients:

```json
{
  "mcpServers": {
    "plainfreight": {
      "type": "http",
      "url": "https://plainfreight.com/api/mcp"
    }
  }
}
```

The server answers a bare GET with 405 (POST only) and completes a full initialize handshake unauthenticated.

## Business Relevance

- **E-commerce and DTC importers** price landed cost from China inside the same session where they compare suppliers.
- **Sourcing teams** check whether a product can ship and which documents it needs before committing to an order.
- **Operators with booked shipments** track them from the same connection that priced them.

## Integration with CorpusIQ

Landed cost is a margin input, and CorpusIQ holds the rest of the margin picture. Composed, an agent can pair a Plain Freight delivered-duty-paid quote with revenue and ad spend from CorpusIQ's Stripe, Shopify and ad connectors to test whether a product still makes money at the quoted cost, and with China sourcing data from connectors like SeekAPI when choosing between supplier candidates.

## Limitations

- Coverage is one lane: China to US addresses, 100 g to 2,000 kg, door to door.
- Fair-use limits (20 offers/hour/IP, 4/email) are built in; high-volume use needs the vendor's programmatic path.
- generate_offer records a quote request; estimate_price and check_goods record nothing.
- Duty treatment differs by mode and the offer states which applies; reading the offer terms is part of using the tools.

## FAQ

### Do I need an account or API key?

No. The endpoint is open and keyless, with fair-use limits per IP and per email address.

### Does the quote include import duty?

It is a delivered-duty-paid figure: freight, US customs clearance, import duty and delivery. Duty is included on door-to-door air and sea, and paid at import on air consolidation; the offer says which applies.

### Can it check whether a product can ship at all?

Yes. check_goods answers whether a product can ship from China to the US and which documents it needs, and records nothing.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [The Company Atlas MCP - Trade Data and Company Registries](/hermes/mcp/servers/external/company-atlas-mcp/)
- [SeekAPI MCP - China Supplier Screening for Agents](/hermes/mcp/servers/external/seekapi-mcp/)
- [Undercart MCP - Shopify Store Intelligence for Agents](/hermes/mcp/servers/external/undercart-mcp/)
