---
title: Ultimate Web Scraper MCP - Cloud Scraping for Agents
description: Cloud scraping platform MCP at mcp.ultimatewebscraper.com - agents extract whole Shopify, WooCommerce, Magento and Salesforce Commerce Cloud catalogs, build contact lists, map sitemaps and run scheduled automations over OAuth with a free tier.
category: Lead Generation & Web Scraping
stars: n/a (new listing)
added: 2026-09-09
source: mcp.so
relevance: ★★★
tags: [web-scraping, ecommerce, product-data, lead-lists, sitemap, data-extraction, shopify, remote-mcp]
---

# Ultimate Web Scraper MCP

**Remote MCP server (Streamable HTTP, OAuth)** - a cloud scraping platform your AI agent drives in plain English: real browsers and location-picked proxies scrape thousands of pages and hand back a clean table you can query, export or re-run on a schedule. Listed on mcp.so under Data & Analytics, verified and featured.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in; bearer key alternative)
Endpoint: https://mcp.ultimatewebscraper.com/mcp
Tools: 13 (catalog extractors, page scraper, contact and map extractors, sitemap mapping, automations, data cleanup)
Pricing: Honest free tier; paid plans via Stripe checkout; free Chrome extension included
Category: Lead Generation & Web Scraping
Built by: Ultimate Web Scraper (ultimatewebscraper.com)
```

## Why This Matters for Operators

An agent on its own reads a handful of pages, one at a time, and gets blocked by bot walls. **Ultimate Web Scraper MCP turns a single sentence like "extract every product and variant from shop.example.com" into a complete table** - 4,000 pages per job on cloud browsers with proxies in the location you pick. For an e-commerce operator that means competitor catalogs, supplier lists and market maps in minutes instead of days of manual clicking.

The platform extractors matter most: Shopify, WooCommerce, Magento and Salesforce Commerce Cloud stores all have dedicated extractors that produce one row per variant with price, SKU, stock and images - no selectors, no scripts. The same connection builds lead lists across thousands of sites and pulls map listings with ratings, phones and hours.

## Tools & Capabilities

The mcp.so listing shows no extracted live tool list; the 13 tool names below come from the vendor's MCP documentation and the live list is served from the endpoint.

| Tool | Purpose |
|---|---|
| `scrape_pages` | One row per URL from similar pages - products, listings, articles, jobs, real estate |
| `extract_shopify_store` | Full Shopify store or named collections into one row per variant (price, SKU, options, images, availability) |
| `extract_catalog` | WooCommerce, Magento or Salesforce Commerce Cloud store into one row per variant/product |
| `extract_contacts` | Lead lists across many sites - emails and social profile links, deep scan to contact pages |
| `extract_map_places` | Name, rating, review count, address, phone, website and hours from map place pages |
| `discover_sitemap` | Map every page of a site from its sitemap, grouped into sections |
| `select_sitemap_urls` | Pick which mapped URLs feed the page extractor - no manual URL lists |
| `analyze_website` | Detect platform, find the sitemap and pick the right approach before scraping |
| `run_automation` | Run any saved automation with cost estimated from run history first |
| `update_automation` | Reschedule or pause an automation and read its latest results |
| `deduplicate_rows` | Remove duplicate rows after a scrape |
| `delete_rows` | Drop unwanted rows |
| `merge_columns` | Rename or merge columns in the result table |

## Installation

```bash
claude mcp add ultimate-web-scraper --transport http https://mcp.ultimatewebscraper.com/mcp
```

The vendor publishes per-client setup snippets (Claude, Claude Code, Cursor, VS Code) at ultimatewebscraper.com/mcp.

## Configuration

```json
{
  "mcpServers": {
    "ultimate-web-scraper": {
      "type": "http",
      "url": "https://mcp.ultimatewebscraper.com/mcp"
    }
  }
}
```

Auth is OAuth: the first connect opens a browser window to sign in to your Ultimate Web Scraper cloud account and authorize access; later sessions reuse the credentials. A bearer header alternative is shown in the vendor's setup snippets.

## Business Relevance

- **E-commerce operators** extract entire competitor or supplier catalogs into one table with variants, prices and SKUs
- **Lead-gen teams** build contact lists across thousands of company sites in a single run
- **Local service operators** pull map listings with ratings, phones and hours for market mapping
- **Analysts** keep any scrape on a daily schedule and query fresh tables from chat
- **Marketplace sellers** monitor pricing and availability changes without writing a scraper

## Integration with CorpusIQ

Ultimate Web Scraper MCP feeds CorpusIQ's e-commerce and prospect connectors from the outside in: an operator asks CorpusIQ for competitor pricing from Shopify data while Ultimate Web Scraper pulls the competitor's live storefront into the same conversation, so CorpusIQ can compare margins against live market prices instead of stale exports. For prospecting, scraped contact lists pair with the catalogued lead-research servers (Crawdar, YouSpot) - raw discovery from Ultimate Web Scraper, qualification from the research layer, follow-up from the CRM connectors.

## Limitations

- Brand new listing - no track record yet
- Cloud-only scraping; no self-host option published
- Paid plans gate volume; the free tier is honest but capped
- No extracted live tool list on the directory listing; tools documented from vendor docs
- Credentials and jobs live on the vendor's cloud

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
