---
title: "Import.io MCP - CorpusIQ Docs"
description: Hosted web scraping over MCP — render pages in a real browser, extract structured data, capture screenshots, with proxy routing, country targeting and CAPTCHA handling. 10,000 free calls, then $0.0002 per successful call.
category: Lead Generation & Web Scraping
stars: n/a (new listing)
added: 2026-08-16
source: mcpservers.org
relevance: ★★★
tags: [web-scraping, data-extraction, browser-automation, proxy, pricing-intelligence, hosted]
---

# Import.io MCP

**Hosted scraping engine (Streamable HTTP, OAuth or Bearer token)** — Import.io, the established web-data vendor behind Aperture pricing intelligence, now ships a hosted MCP endpoint. Agents get browser rendering, structured extraction, screenshots, and HTML retrieval with proxy routing, country targeting, and CAPTCHA handling — no scraping infrastructure to run.

```
Server type: Hosted remote (Streamable HTTP)
Auth: OAuth (most clients) or Bearer API key (scripts)
Endpoint: https://mcp.import.io/mcp
Tools: importio_render, importio_extract_data, importio_get_html, importio_action_screen_capture
Pricing: 10,000 free successful calls, then $0.0002 per successful call; monthly spend cap
Category: Lead Generation & Web Scraping
Built by: import.io (pricing intelligence, Aperture)
```

## Why This Matters for Operators

Built-in browsing answers one-off questions; repeatable extraction needs a real engine. Import.io gives agents the parts operators actually fight for: JavaScript rendering for dynamic pages, country-targeted results when geography changes the answer, CAPTCHA handling for defended sites, and structured field extraction instead of raw HTML that burns model context. The pricing model is unusual and operator-friendly — you pay only for successful calls, malformed or blocked requests are never billed, and a monthly spending limit is a hard stop.

This is a major vendor entering MCP, not a hobbyist scraper: Import.io has run pricing intelligence for retail and brand teams for years, so the MCP surface inherits that reliability story.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `importio_render` | Render a page in a real browser before extraction |
| `importio_extract_data` | Extract defined fields as clean structured data |
| `importio_get_html` | Retrieve raw or rendered HTML for inspection |
| `importio_action_screen_capture` | Capture screenshots as visual evidence |

Included in the platform: proxy routing (datacenter to residential), country targeting, and CAPTCHA support.

## Installation

```json
{
  "mcpServers": {
    "importio": {
      "url": "https://mcp.import.io/mcp"
    }
  }
}
```

Most clients open the OAuth flow automatically. For scripts or clients without OAuth, create an API key at mcp.import.io/app/keys and send it as a bearer token (`Authorization: Bearer mcp_live_...`). Claude users can install the plugin instead: `claude plugin marketplace add import-io/mcp-plugin` then `claude plugin install importio-web-scraper`.

## Business Relevance

- **Competitor price monitoring** becomes an agent task — structured fields across retailer sites with geography control
- **Lead research** can pull structured company and contact data from defended sites that block naive scrapers
- **Data pipelines** get a managed extraction layer without maintaining proxy pools or headless browsers
- **Due diligence** gains screenshot evidence and country-correct pricing checks

## Integration with CorpusIQ

Import.io pairs with CorpusIQ's connectors as the unstructured-data acquisition layer: CorpusIQ pulls structured records from QuickBooks, Shopify, and GA4, while Import.io turns competitor sites and public pages into comparable structured fields. The pricing-intelligence use case is the natural joint workflow — track competitor pricing via Import.io, benchmark against internal margins from CorpusIQ's finance connectors, and act on the gap.

## Limitations

- Per-call pricing after the free 10,000 calls requires budgeting discipline; one agent task can burn several calls
- Usage is metered per successful tool call — heavy automation needs the monthly cap configured up front
- No published tool schemas beyond the four core tools; extraction specifics are learned from the docs
- Hosted service — data flows through Import.io infrastructure

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
