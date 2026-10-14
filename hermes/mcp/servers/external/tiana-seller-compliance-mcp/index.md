---
title: "Tiana & Co. MCP - Marketplace Seller Compliance"
description: "Free US seller compliance checks: which safety certificate a product needs, what major marketplaces ask for, and UFLPA and OFAC supplier screening."
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-10-13
source: "chatmcp/mcpso issue #5268 + official MCP registry (October 13, 2026 evening sweep)"
relevance: ★★
tags: [compliance, ecommerce, marketplace-sellers, amazon, walmart, tiktok-shop, uflpa, ofac, keyless, remote-mcp]
---

# Tiana & Co. MCP

**Remote MCP server (Streamable HTTP, no account or API key)** - free US compliance checks for marketplace sellers: which safety certificate a product needs, what the major marketplaces ask for, supplier screening, this week's rule changes and what a customs hold means. Every answer names its source and read date.

```
Server type: Remote (Streamable HTTP)
Auth: None (the checks are free; no account or key)
Endpoint: https://www.tiana-co.com/api/mcp
Tools: 5 (certificate, marketplace asks, supplier screening, rule changes, customs hold)
Pricing: Free
Built by: Tiana & Co. LLC (tiana-co.com; the /for-ai page documents the MCP surface)
Listing: chatmcp/mcpso issue #5268; official MCP Registry io.github.1294962213sh/tiana-co-free-checks
```

## Why This Matters for Operators

A missing certificate is not a paperwork problem, it is a listing problem and sometimes a shipment problem. A product flagged for the wrong safety documentation gets blocked on Amazon, Walmart, TikTok Shop or Etsy, and a supplier on a screening list turns into a customs hold with weeks of inventory stuck behind it.

This server answers the five questions behind those incidents: which certificate the product needs (CPC, GCC, FCC, and the FDA import steps), what each marketplace actually asks for it, whether a supplier appears on UFLPA, OFAC or Consolidated Screening lists, what changed in seller rules this week, and what a customs hold notice means. Every answer carries its source and read date, so the reasoning can be checked rather than trusted.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| seller_compliance.which_certificate | Which safety certificate a product needs (CPC, GCC, FCC, FDA import steps) and why |
| seller_compliance.marketplace_asks | What Amazon, Walmart, TikTok Shop and Etsy each ask for the certificate |
| seller_compliance.screen_supplier | Screen a supplier against UFLPA, OFAC and the Consolidated Screening lists |
| seller_compliance.what_changed | This week's seller-rule changes across the marketplaces |
| seller_compliance.shipment_held | What a customs hold notice means, from the seller's own account of it |

## Installation

```
claude mcp add --transport http tiana https://www.tiana-co.com/api/mcp
```

Any MCP client that speaks Streamable HTTP can add the same URL, with no sign-in.

## Configuration

```json
{
  "mcpServers": {
    "tiana-co": {
      "type": "http",
      "url": "https://www.tiana-co.com/api/mcp"
    }
  }
}
```

## Business Relevance

- **Marketplace sellers** check certificate requirements before a product launch instead of after a listing block
- **Import and sourcing teams** screen suppliers against UFLPA and OFAC lists in the same tool where the certificate question gets answered
- **Agencies and consultants** run the same checks across client catalogs, with cited sources they can hand to the client
- **Operations leads** decode a customs hold notice and get to the paperwork rather than the guesswork

## Integration with CorpusIQ

Tiana covers the seller-compliance layer: certificates, marketplace requirements and supplier screening. CorpusIQ answers the surrounding business question from connected sources such as store data, email, spreadsheets and accounting, so a compliance question raised in an email can pull the certificate answer, the supplier screen and the order context into the same thread.

Used together: ask CorpusIQ for the operating view (suppliers, orders, correspondence) and ask Tiana for the compliance view (certificate, marketplace requirements, screening). Tiana stays the source for the specific checks; CorpusIQ remains the place the rest of the question is answered alongside.

## Limitations

- US rules and US marketplaces; sellers in other jurisdictions will find the screens useful but the certificate guidance is US-focused
- An information layer, not legal advice: every answer cites its source and read date, and rulings should be verified with a qualified professional before acting
- Read-only: it answers questions and does not file anything with a marketplace or authority
- A young service (v1.3.0 at listing time); check the cited read dates for currency

## FAQ

### Is it really keyless?

Yes. A live probe returned 200 on initialize and `tools/list` with all 5 tools, no account or API key.

### Which marketplaces does it cover?

Amazon, Walmart, TikTok Shop and Etsy for the "what does the marketplace ask for" checks, with the certificate guidance (CPC, GCC, FCC, FDA import steps) and supplier screening (UFLPA, OFAC, Consolidated Screening) applying generally to US imports and sales.

### Is this legal advice?

No. It is a compliance information layer: every answer names its source and read date so the reasoning can be checked, and anything consequential should be verified with a qualified professional.

### What does it cost?

The checks are free.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [marketplaces-mcp-ru - Russian Marketplace Seller Operations for Agents](/hermes/mcp/servers/external/marketplaces-mcp-ru/)
- [The Art of Service MCP - Compliance Framework Crosswalks](/hermes/mcp/servers/external/theartofservice-compliance-mcp/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
