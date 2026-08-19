---
title: "PlaceRoot MCP - Keyless Spatial Answers from Overture Maps"
description: "Free keyless MCP server grounding AI agents in open map data: place search, geocoding, neighborhood analysis, street-graph routing, and isochrones via 29 tools, self-hostable under MIT"
category: Location Data
stars: n/a (new listing)
added: 2026-08-18
source: "mcp.so GitHub issue #3631"
relevance: ★★
tags: [geospatial, overture-maps, geocoding, routing, isochrones, real-estate, logistics, keyless, open-source]
---

# PlaceRoot MCP

**Free, keyless MCP server that grounds AI agents in open map data — place search, geocoding, neighborhood analysis, real street-graph routing, and isochrones, anywhere on Earth.** No API key, no account, no vendor platform. Answers are compact and ranked, sized for an agent's context window. Built on Overture Maps open data, MIT licensed and self-hostable.

```
Server type: stdio (self-hosted) or local HTTP
Auth: None (keyless by design)
Install: uvx placeroot  |  uvx placeroot --http  |  npx placeroot
Tools: 29 (search, area analysis, routing, maps)
Pricing: Free
Category: Location Data
Registry: io.github.chuofringer/placeroot (v0.9.6+)
Built by: chuofringer (placeroot.dev)
```

## Why This Matters for Operators

Every site-selection, logistics, or market-analysis question starts with "where." Most spatial MCP options require vendor API keys (Google, Mapbox) or cover one narrow function. PlaceRoot removes both frictions: it is keyless and spans search, area analysis, routing, and maps in 29 tools, so an agent can go from "find retail corridors within 20 minutes of this warehouse" to "isochrone that trade area" without touching a billing console.

Because it runs locally via uvx, no data leaves your infrastructure, and because answers are ranked and compact, they fit agent context windows without truncation.

## Tools & Capabilities

| Area | What it does |
|---|---|
| Place search | Find places by name, category, or area with ranked, compact results |
| Geocoding | Forward and reverse geocoding from Overture open data |
| Neighborhood analysis | Area profiles for trade-area and site-selection questions |
| Routing | Real street-graph routing distances and travel times |
| Isochrones | Drive-time and travel-time catchments around a point |

## Installation

```bash
# stdio (default)
uvx placeroot

# local HTTP server mode
uvx placeroot --http

# or via npx
npx placeroot
```

No key, no account, no environment variables.

## Configuration

```json
{
  "mcpServers": {
    "placeroot": {
      "command": "uvx",
      "args": ["placeroot"]
    }
  }
}
```

## Business Relevance

- **Real estate operators** run trade-area and neighborhood analysis without a GIS team
- **Logistics and last-mile teams** answer drive-time catchment questions from open street graphs
- **Site selectors** screen corridors by isochrone coverage before paying for vendor data
- **Market analysts** geocode and profile locations inside their agent workflow at zero cost
- **Self-hosters** run the whole stack on their own infrastructure under MIT

## Integration with CorpusIQ

CorpusIQ supplies the financial and CRM layer (revenue by customer, invoices, pipeline) while PlaceRoot supplies the spatial layer (where customers are, what a trade area covers, how far delivery stretches). Joined in one agent session, an operator can ask which customers sit inside a 20-minute isochrone and what they spent last quarter — a question neither system answers alone.

## Limitations

- New listing (Aug 2026), small community so far
- Open-data coverage: Overture Maps quality varies by region
- No hosted endpoint published; runs locally or self-hosted
- Routing quality depends on public OSRM/Valhalla instances
- No commercial support or SLA

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
