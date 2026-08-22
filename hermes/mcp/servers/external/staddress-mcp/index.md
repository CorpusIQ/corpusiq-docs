---
title: "Staddress AI MCP - Japanese Address Normalization"
description: "Normalize and parse Japanese addresses from any MCP client: structured components, latitude and longitude, confidence scores and address codes, with batch parsing up to 100 addresses and API usage checks. API key required."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-08-22
source: "mcp.so GitHub issue #3686"
relevance: ★★
tags: [addresses, geocoding, japan, data-cleaning, normalization, self-hosted]
---

# Staddress AI MCP

**An AI-powered Japanese address normalization server that turns messy address strings into structured, geocoded data.** Staddress parses Japanese addresses into structured components and returns latitude/longitude, a confidence score and an address code - the exact cleanup step every e-commerce, logistics and CRM pipeline dealing with Japanese customers gets wrong when it ships raw address text into a database. Three tools over stdio, MIT-licensed client, commercial API.

```
Server type: stdio (npx -y @staddress/mcp)
Auth: API key (STADDRESS_API_KEY, st_xxx issued at staddress.com)
API: https://api.staddress.com (STADDRESS_BASE_URL overrides)
Tools: 3 (parse, batch parse, usage)
Pricing: Commercial API; free tier via staddress.com; MIT client
Built by: StaddressAI; repo github.com/StaddressAI/staddress-tools
```

## Why This Matters for Operators

Japanese addresses are structurally hard: kanji variants, building names, block numbers and prefecture/city/street components all run together in free-text fields from checkout forms, CSV imports and support tickets. **Staddress returns the normalized components plus coordinates and a confidence score in one call**, so an operator can deduplicate customers, validate shipping addresses before dispatch, and geocode delivery zones without hand-cleaning. The confidence score is the honest part: low-confidence parses are flagged for human review instead of silently polluting the database.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `staddress_parse` | Normalize and parse a single Japanese address into structured components, latitude/longitude, confidence score and address code |
| `staddress_parse_batch` | Batch parse up to 100 addresses (Standard plan and above) |
| `staddress_get_usage` | Read plan, quota and credit usage |

## Installation

```json
{
  "mcpServers": {
    "staddress": {
      "command": "npx",
      "args": ["-y", "@staddress/mcp"],
      "env": { "STADDRESS_API_KEY": "st_xxx" }
    }
  }
}
```

Keys are issued at staddress.com. The repo also ships SDKs, a CLI and a Claude Desktop Extension (MCPB) for the same API.

## Configuration

The only required setting is `STADDRESS_API_KEY`. `STADDRESS_BASE_URL` is optional and defaults to `https://api.staddress.com`. Because the server runs locally over stdio, all address data flows through your own client process to the Staddress API.

## Business Relevance

- **E-commerce and marketplace operators** validate Japanese shipping addresses before dispatch and deduplicate customers across storefronts
- **Logistics teams** geocode delivery addresses into coordinates for routing and zone planning
- **CRM data teams** clean imported Japanese contact data in bulk with the batch endpoint
- **Analysts** flag low-confidence parses for manual review instead of trusting dirty data

## Integration with CorpusIQ

Staddress cleans the address layer; CorpusIQ reads the business around it. A composed workflow pulls Shopify orders through the CorpusIQ Shopify connector, runs the Japanese shipping addresses through Staddress for normalization and confidence scoring, then writes the cleanup results back into the CRM view through CorpusIQ's HubSpot reads - one pipeline from dirty checkout field to trusted, geocoded customer record. Operators running Japanese-market analytics can then slice normalized-region performance in GA4 through CorpusIQ instead of guessing at prefecture-level aggregation from raw strings.

## Limitations

- Japan-specific - no other country's address formats
- stdio only (no hosted remote endpoint); runs on your machine
- Commercial API behind the key; batch parsing is a paid-plan feature
- New listing (Aug 2026); repo has 0 stars, npm package at v0.1.0
- Confidence scores require human review workflow for low-confidence parses

## See Also

- [Leadgen MCP](/hermes/mcp/servers/external/leadgen-mcp/)
- [Xverum MCP](/hermes/mcp/servers/external/xverum-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
