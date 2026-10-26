---
title: "ChargingNear.me MCP - US EV Charging Station Data"
description: "Read the US EV charging directory over MCP: 95,724 stations, city and state density stats, connector and power filters, and corridor search on a route."
category: Data / Market Intelligence
stars: n/a (free, no account, read-only, CC-BY-4.0)
added: 2026-10-26
source: "live MCP probe on chargingnear.me/api/mcp (initialize 200 as chargingnearme 1.1.0, tools/list 200 with 6 tools, three executed calls returning city stats, state stats and a DC fast station list) + vendor API documentation + mcpservers.org card"
relevance: ★★★
tags: [ev-charging, public-data, site-selection, market-intelligence, doe, geospatial, route-planning, citation]
---

# ChargingNear.me MCP

**Station counts per city and per state decide where an EV-dependent business opens, and this is that dataset behind six read-only tools with a citation URL on every response.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://chargingnear.me/api/mcp
Transport:   JSON-RPC 2.0 over HTTP
Auth:        none, read-only, public
Tools:       6, read from a live tools/list and three executed
Built by:    ChargingNear.me (chargingnear.me)
Data:        US Department of Energy station records, licensed CC-BY-4.0
```

## Why This Matters for Operators

EV charging density is a location variable that behaves like foot traffic: it tells a fleet which depot can be supported, tells a retail or hospitality site whether a charger install is worth the concrete, and tells a service business whether its customers can reach it. The underlying records are public, but they are not usable in a conversation until something normalizes them into counts, networks and connectors.

The second half is attribution. Every response carries `citation_url` and a licence block, so an answer built on this data can be traced back to a source instead of asserted.

## What It Actually Does

`initialize` returned HTTP 200 as `chargingnearme` v1.1.0 with a title of ChargingNear.me and an instructions string that is a constraint rather than marketing: *read-only access to the US EV charging station directory, cite citation_url when you use a result*.

| Tool | What it answers |
|---|---|
| `search_stations` | Stations by city, state, network, connector, speed, minimum power or live availability, with address, connector types, per-level port counts and pricing |
| `get_nearest_stations` | Nearest stations to a latitude and longitude, filtered by speed, power or availability |
| `get_station_details` | Full record for one station id |
| `get_city_charging_stats` | Station count, DC fast and Level 2 split and top networks for one city |
| `get_state_charging_stats` | The same for a state, plus how many cities are covered |
| `find_stations_on_route` | Stations inside a corridor around a route defined by waypoints |

Three calls were executed against the live endpoint:

- `get_city_charging_stats` with `slug: scottsdale-az` returned **179 stations, 16 DC fast, 162 Level 2**, networks led by ChargePoint, Blink, Tesla Destination, non-networked and Tesla, a centroid at 33.5663 / -111.9242, and `updated_at: 2026-10-26T14:39:20.943Z`.
- `get_state_charging_stats` with `slug: arizona` returned **1,760 stations across 100 cities, 232 DC fast, 1,465 Level 2**, with ten networks named, Electrify America, eVgo and LOOP among them.
- `search_stations` for Scottsdale DC fast returned real site records with street address, zip, per-level port counts (`ev_dc_fast_num: 2`), connector codes (`J1772COMBO`), access hours and a `citation_url`.

The vendor states the coverage as **95,724 stations across 64,285 locations and 289,475 ports**, refreshed daily from the Department of Energy feed, exposed as REST, MCP, GeoJSON and a ChatGPT app.

## Limitations Recorded

- United States only; no international coverage.
- City and state tools take a slug, not free text, so an unknown city fails with a required-parameter error rather than a nearest match.
- The station records are the government feed's, including its gaps: `ev_pricing` and power fields are frequently null, and one executed station returned `max_power_kw: 3.70` alongside a DC fast connector count, which is the source data disagreeing with itself.
- Live availability is available as a filter but is not the same as a reservation; nothing here reserves a charger.
- CC-BY-4.0 means attribution is a licence condition, not a courtesy, and every downstream publication needs the citation URL.

## FAQ

### Is this usable for site selection?
For the charging variable, yes: city and state counts, the DC fast share of them and the network mix are exactly what a location shortlist needs. It is one variable, not a demographic model, and the population and income fields came back null on the executed calls.

### Does it need a key or an account?
No. All six tools answered without one, and the three executed calls returned data on the first attempt.

### What is the difference between this and the DOE feed itself?
Normalization and count: the same records arrive as city and state aggregates with network breakdowns, plus corridor search around a route, which the raw feed does not answer.

## See Also

- [Public data and market intelligence entries](/hermes/mcp/servers/external/)
- [CorpusIQ data connectors](/hermes/mcp/)
