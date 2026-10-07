---
title: "UK Land Registry MCP - Sold Price Packs for Agents"
description: "HM Land Registry Price Paid data for England and Wales: sold prices and area comparisons with thin-sample warnings, as free peeks or one-time packs."
category: Real Estate
stars: n/a (new listing)
added: 2026-10-06
source: "chatmcp/mcpso issue #4831 (Oct 6, 2026 evening sweep)"
relevance: ★★
tags: [uk, property, real-estate, land-registry, price-data, open-data, remote-mcp, keyless]
---

# UK Land Registry MCP

**Remote MCP server (Streamable HTTP, keyless)** - HM Land Registry Price Paid data for England and Wales, built for estate agents, conveyancers and analysts: sold prices and area comparisons for a postcode, from a free peek to one-time £0.49 packs.

```
Server type: Remote (Streamable HTTP, Cloudflare Worker)
Auth: None (keyless discovery; packs pay per use)
Endpoint: https://uk-lr-mcp.donniertf.workers.dev/mcp
Tools: 4 (discovery, two pack tools, redeem)
Pricing: Free sample; GBP 0.49 one-time per pack
Built by: donniertf (uk-mcp-fleet)
Source: HM Land Registry Price Paid (Open Government Licence v3.0)
```

## Why This Matters for Operators

Sold-price data is the ground truth of a local property market: what actually changed hands, when, at what price, and how the surrounding area compares. The official record is public, but pulling it into a usable comparison usually means form-filling on a government site and copying rows into a spreadsheet.

This server turns the question into a prompt: sold prices around a postcode, then a comps pack with median and mean summaries - and honest thin-sample warnings when the data is too sparse to support a number. For property-adjacent operators (agents, investors, proptech, home-services), the market view arrives in the conversation, with flags instead of false confidence.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `price_paid_discover` | Free peek: up to 5 Price Paid sales for a postcode, outcode or town (e.g. M1); cached 24h |
| `price_paid_pack` | Paid pack of recent sales: address, price, date, type, tenure; Stripe Checkout link, one-time token redeem |
| `area_comps_pack` | Paid compound comps pack: Price Paid sample plus summary stats and `risk_flags` |
| `redeem_pack` | Instructions to redeem a paid Stripe Checkout session |

Free sample: `GET /v1/discover/price-paid?area=E1` (up to 5 sales).

## Installation

```bash
claude mcp add uk-land-registry --transport http https://uk-lr-mcp.donniertf.workers.dev/mcp
```

Discovery is keyless. Paid packs return a Stripe Checkout URL inside the tool result; pay GBP 0.49 and redeem with the one-time token.

## Configuration

```json
{
  "mcpServers": {
    "uk-land-registry": {
      "url": "https://uk-lr-mcp.donniertf.workers.dev/mcp"
    }
  }
}
```

## Business Relevance

- **Estate agents and conveyancers** pull sold-price context for a street or postcode from the chat.
- **Property investors** sanity-check asking prices against recorded sales with comps and warnings.
- **Proptech products** feed structured sold-price rows into agent workflows without scraping portals.
- **Home-services businesses** read area turnover as a demand signal for local campaigns.

## Integration with CorpusIQ

CorpusIQ's read-only connectors cover the business's own numbers - jobs, invoices, ad spend. The Land Registry server covers the market the business sells into: what nearby property actually sold for. Pair "how is our quarter" with "what is the local market doing" in one conversation.

## Limitations

- England and Wales residential sales only; it is not the register of title and not a valuation.
- Thin areas return few or no sales - the comps pack surfaces that as a warning rather than filling gaps.
- Free samples are capped (5 sales, 24h cache); full results are behind one-time GBP 0.49 packs.
- The fleet's pages offer a refund within 7 days if a pack comes back empty or errors.

## FAQ

### What does the free peek give me?

Up to 5 recent sold-price rows for a postcode, outcode or town, cached for 24 hours - a working sample of the pack data.

### Which areas are covered?

England and Wales residential sales from HM Land Registry Price Paid. Scotland and Northern Ireland are not included.

### How much does a pack cost?

GBP 0.49 per pack, paid once via Stripe Checkout from inside the tool call. Discovery is free.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Dutch Property Context MCP - Netherlands Property Reports](/hermes/mcp/servers/external/dutch-property-context/)
- [UK Planning MCP - Planning Applications by LPA](/hermes/mcp/servers/external/uk-planning-mcp/)
