---
title: "BasedOnBusiness — Google Maps Business Leads MCP"
description: "Google Maps business & lead data API and MCP server. Search, enrich (email, social, tech stack), and export leads across 195 countries."
source: www.basedonb.com
stars: 0
language: N/A (Hosted SaaS)
transport: Streamable HTTP
auth: API Key
category: Marketing & Lead Gen
last_updated: 2026-07-21
---

# BasedOnBusiness — Google Maps Business Leads MCP

**Google Maps lead generation platform with MCP integration.** Search businesses on Google Maps, enrich them with email, social media, and tech stack data, and export qualified leads — all through AI agent commands. Covers 195 countries.

## What It Does for Operators

- **Google Maps search** — Find businesses by category, location, and filters across 195 countries
- **Lead enrichment** — Get emails, social profiles, and technology stack for each business
- **Export-ready** — Data formatted for CRM import and outreach workflows
- **AI agent-native** — All search and enrichment accessible through MCP tools

## Installation

```bash
# No installation — hosted API
# Sign up at basedonb.com for API key
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "basedonbusiness": {
      "type": "url",
      "url": "https://www.basedonb.com/docs"
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `search_businesses` | Search Google Maps for businesses by category + location |
| `enrich_lead` | Get email, social profiles, and tech stack for a business |
| `batch_search` | Search multiple categories/locations in one query |
| `export_leads` | Export enriched leads as CSV/JSON for CRM import |

*Note: Tool names are approximate. Full documentation at basedonb.com/docs.*

## Operator Use Cases

1. **Sales Teams** — "Find all marketing agencies in Austin with 10-50 employees" → enriched lead list
2. **Recruiters** — Search for companies by tech stack to identify hiring targets
3. **Market Researchers** — Map competitive landscapes by business category and location
4. **Agency Owners** — Find potential clients in specific verticals and geographies

## CorpusIQ Angle

BasedOnBusiness is a lead generation powerhouse for operators. Paired with CorpusIQ's business data connectors, operators can: (1) discover leads via BasedOnBusiness, (2) qualify them with enrichment data, (3) manage the pipeline in HubSpot (CorpusIQ CRM connector), and (4) track financial performance in QuickBooks — all through AI agent commands.

## Limitations

- Requires paid API key for full enrichment data
- Data accuracy depends on Google Maps listings + enrichment sources
- Rate limits on batch searches
- Email enrichment may not be available for all businesses
