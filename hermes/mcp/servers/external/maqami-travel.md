---
title: "Maqami Travel MCP — Hotel Booking for AI Agents"
description: "Search, compare, and book hotels across 249 countries from any MCP client. 65 tools for hotel discovery, reservation management, and travel planning — directly from AI agents."
category: mcp
tags: [mcp-server, travel, hotel-booking, commerce, hospitality, travel-tech]
last_updated: 2026-07-08
---

# Maqami Travel MCP Server ★ New (July 2 PM)

## Overview

Maqami Travel MCP (`mcp.maqami.co`) is the first hotel-booking MCP server, giving AI agents access to 65 tools across 249 countries. Search hotels by destination, dates, amenities, and price range; compare properties; manage reservations; and integrate hotel booking directly into agent workflows. Travel operators, concierge services, and corporate travel managers can now build AI-driven booking experiences without leaving their MCP client.

**Key advantage**: 65 purpose-built tools, 249-country coverage, hosted remote endpoint — zero infrastructure to manage.

## Key Features

- **Hotel search**: Search properties by destination, check-in/check-out dates, guests, price range, star rating, and amenities
- **Property details**: Full hotel profiles — photos, amenities, room types, policies, reviews
- **Booking management**: Create, modify, and cancel reservations; retrieve booking confirmations
- **Price comparison**: Compare rates across properties and room types
- **Geographic coverage**: 249 countries with localized property data
- **Remote hosted**: No local installation — connect via SSE endpoint at `mcp.maqami.co`

## Installation

```bash
# Remote SSE — no local install needed
hermes mcp add maqami-travel --url https://mcp.maqami.co/
```

## Configuration

```json
{
  "mcpServers": {
    "maqami-travel": {
      "url": "https://mcp.maqami.co/",
      "transport": "sse"
    }
  }
}
```

## Business Relevance

- **Travel & Hospitality**: Travel agencies and OTAs can embed AI-powered hotel search and booking directly in customer-facing AI assistants
- **Corporate Travel**: Enterprise travel managers can delegate hotel sourcing and booking to AI agents with policy enforcement (budget caps, preferred chains)
- **Concierge Services**: High-touch concierge and lifestyle management services can offer 24/7 AI-driven hotel recommendations and reservations
- **Event Planning**: Conference and event organizers can source room blocks and compare venue-adjacent hotels programmatically
- **Travel Content**: Travel bloggers, publishers, and comparison sites can enrich content with real-time hotel availability and pricing

## Integration with CorpusIQ

Maqami Travel complements CorpusIQ's 37+ business connectors by opening the travel vertical — the first hotel-booking capability in the CorpusIQ ecosystem. Combined with CorpusIQ's email automation (Gmail/Outlook), CRM tools (Attio, OnePageCRM), and document generation (PandaDoc), operators can build end-to-end travel booking workflows:

- AI agent searches hotels → books optimal option → sends confirmation email → creates CRM record → generates invoice

The 249-country coverage aligns with CorpusIQ's global operator base, and the remote SSE transport pattern matches existing CorpusIQ MCP integrations for zero-friction deployment.

## Limitations

- Hotel-only — no flights, car rentals, or experiences (yet)
- Requires Maqami account/API access for booking operations
- Remote-hosted — depends on third-party uptime
- Pricing and availability subject to provider data freshness

## See Also

- [CorpusIQ Commerce Connectors](/hermes/mcp/servers/external/#commerce--e-commerce)
- [AirLabs MCP — Aviation Data](/hermes/mcp/servers/external/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
