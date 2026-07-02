---
title: "Booyah Index MCP — Southeast Asia Business Directory for AI Agents"
description: "Free AI-readable directory of 3,520 local businesses across 14 Southeast Asian cities. Search restaurants, services, and local businesses in Bangkok, Singapore, Bali, Kuala Lumpur, and more from any MCP client."
category: mcp
tags: [mcp-server, business-directory, southeast-asia, local-business, travel, market-research]
last_updated: 2026-07-02
---

# Booyah Index MCP — SE Asia Business Directory

## What It Is

Booyah Index MCP (`sarapab-th/booyah-index-mcp`) provides an AI-readable directory of 3,520 local businesses across 14 Southeast Asian cities — Bangkok, Singapore, Bali, Kuala Lumpur, Ho Chi Minh City, and more. Market researchers, expansion teams, and travel operators can search and analyze local business landscapes without scraping or manual research.

## Tools Available

| Tool | Description |
|------|-------------|
| Business search | Search by category, city, name, or keyword |
| City browse | List businesses by city with category filters |
| Detail lookup | Full business profiles with location, hours, ratings |

## Quick Start

```bash
npx mcp-remote https://getbooyah.com/api/mcp
```

## Business Use Cases

1. **Market entry research**: "How many coffee shops with 4+ star ratings are there in Chiang Mai?"
2. **Competitive landscape**: "List all co-working spaces in Kuala Lumpur with their ratings and price ranges"
3. **Supplier discovery**: "Find Thai food product suppliers in Bangkok for export to the US"
4. **Travel planning ops**: "Top 10 rated restaurants in Singapore's Chinatown under $30/person"

## Limitations

- **SE Asia only**: 14 cities, no coverage outside Southeast Asia
- **Static directory**: Not real-time — data freshness depends on Booyah's update cycle
- **Limited depth**: 3,520 businesses across 14 cities averages ~250/city

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
