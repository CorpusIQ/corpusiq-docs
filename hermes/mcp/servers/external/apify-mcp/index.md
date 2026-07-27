# Apify MCP Server ★★★ Official

**Source:** mcpservers.org · **Last updated:** July 26, 2026 (evening sweep)  
**GitHub:** [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) ⭐ 2,200+  
**Endpoint:** `https://mcp.apify.com` (Streamable HTTP, hosted)  
**Auth:** OAuth 2.0 (Apify account) or API token  
**Category:** Web Scraping / Data Extraction

---

## Overview

The **official Apify MCP server** connects AI agents to Apify's ecosystem of thousands of ready-made web scrapers, crawlers, and automation tools (called "Actors"). Agents can search the Apify Store for scrapers targeting specific websites, execute them, and retrieve structured data — all through natural language.

With 2,200+ GitHub stars and official status, this is the definitive web data extraction MCP for AI agents. The hosted endpoint at `mcp.apify.com` supports OAuth, output schema inference, and the latest features.

## Key Capabilities

- **Search Actors** — Find scrapers for any website or data source (`search-actors`)
- **Inspect Actors** — Get parameters, pricing, README, and input schema (`fetch-actor-details`)
- **Run Actors** — Execute a scraper/automation and retrieve results (`call-actor`)
- **Fetch results** — Retrieve paginated dataset items from completed runs (`get-dataset-items`)
- **Search docs** — Look up Apify platform guides and integration docs (`search-apify-docs`)

## What You Can Scrape

| Category | Examples |
|----------|----------|
| **Social Media** | Instagram, TikTok, Twitter/X, LinkedIn, YouTube, Facebook |
| **Search Engines** | Google Search, Google Maps, Bing, DuckDuckGo |
| **E-commerce** | Amazon, eBay, Shopify stores, AliExpress, Etsy |
| **Business Data** | Google Maps businesses, LinkedIn companies, Crunchbase |
| **Real Estate** | Zillow, Realtor.com, Airbnb |
| **News & Content** | News sites, blogs, RSS feeds |
| **Custom** | Any website via Puppeteer/Playwright Actors |

## Integration

### 1. Claude Desktop

```json
{
  "mcpServers": {
    "apify": {
      "type": "http",
      "url": "https://mcp.apify.com",
      "auth": "oauth"
    }
  }
}
```

### 2. Hermes Agent (config.yaml)

```yaml
mcp:
  servers:
    apify:
      type: http
      url: https://mcp.apify.com
      auth: oauth
```

### 3. Local Alternative (stdio)

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "apify-mcp-server"],
      "env": {
        "APIFY_TOKEN": "your-apify-token"
      }
    }
  }
}
```

⚠️ The hosted endpoint at `mcp.apify.com` supports output schema inference not available in the local stdio version.

## Business Operator Use Cases

1. **Competitor Price Monitoring** — "Scrape Amazon for all competitors' prices on [product category] weekly"
2. **Lead Generation** — "Extract all marketing agencies in Austin from Google Maps with contact details"
3. **Market Research** — "Get the top 100 posts from r/SaaS this month with engagement metrics"
4. **Brand Monitoring** — "Search Twitter/X for mentions of our brand daily"
5. **Job Market Analysis** — "Scrape LinkedIn for all 'AI Engineer' postings in Berlin"

## Pricing

- **Apify MCP server:** Free (Apify platform feature)
- **Apify platform:** Free tier ($5/month credit), paid plans from $49/month
- **Actor execution costs** vary — most are pennies per 1,000 results
- **OAuth:** No additional cost

## Security Considerations

- OAuth 2.0 authentication — industry standard
- API token scoped to specific Actors and data access
- All Actor runs logged in Apify Console
- ⚠️ Respect robots.txt and website ToS when configuring scraping Actors

## Verdict

★★★★★ — The definitive web scraping MCP. Official, hosted, OAuth-secured, and backed by Apify's marketplace of thousands of pre-built scrapers. Essential for any operator who needs web data flowing into their AI workflows — from competitor monitoring to lead generation to market research.
