---
title: "Pocket Drives MCP - Luxury and Exotic Vehicle Rental Marketplace"
description: "Read-only MCP for the Pocket Drives peer-to-peer marketplace: search luxury, exotic and EV rentals from independent hosts, get quotes with daily breakdowns, taxes and deposits, check monthly availability, read renter reviews and browse host showrooms. No auth, Streamable HTTP."
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-08-22
source: "mcp.so GitHub issue #3680"
relevance: ★★
tags: [travel, car-rental, marketplace, vehicles, booking, read-only, peer-to-peer]
---

# Pocket Drives MCP

**A peer-to-peer luxury, exotic and EV rental marketplace behind nine read-only MCP tools.** Pocket Drives lets agents search marketplace inventory by location, dates and category, pull full vehicle detail with host policies, get a line-item quote (daily breakdown, taxes, deposit, total), check a monthly availability calendar, read published renter reviews and browse host showrooms. Booking finishes in the iOS app; the MCP surface is public and needs no auth.

```
Server type: Remote (Streamable HTTP)
Auth: None (read-only)
Endpoint: https://pocketdrives.ai/mcp
Registry: ai.pocketdrives/pocket-drives
Tools: 9 (search, detail, availability, quote, location, airports, venues, host, reviews)
Pricing: Free
Built by: PocketList Inc (pocketdrives.ai); repo github.com/lifeofjer/pocket-drives-mcp
```

## Why This Matters for Operators

Rental marketplaces hide their real cost in taxes, deposits and delivery fees, and hosts price with wildly different policies. **Pocket Drives exposes the actual quote math as a tool**, so an agent can compare a Lucid from one host against a G-Wagon from another on total price, not sticker rate. Markets covered today: Salt Lake City, Scottsdale, Orange County, Palm Springs and Las Vegas. The value sits in the pricing transparency - every quote carries the daily breakdown, taxes and deposit in one structured answer.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `drives_search_vehicles` | Search marketplace inventory by location, dates, category and filters |
| `drives_vehicle_detail` | Full detail for one vehicle: rates, host info, organization policies |
| `drives_get_quote` | Line-item quote: daily breakdown, taxes, deposit, total for a date range |
| `drives_vehicle_availability` | Monthly availability calendar with daily rates |
| `drives_vehicle_reviews` | Published renter reviews for a vehicle |
| `drives_location_suggest` | Autocomplete cities, airports and venues for search input |
| `drives_airport_search` | Airports offering delivery pickup, with delivery fee info |
| `drives_venue_search` | Stadiums, arenas and venues offering delivery pickup |
| `drives_host_showroom` | Host profile by username: bio, locations, team, social links |

All nine tools are verified live (server v1.0.0). The marketplace is peer-to-peer: hosts are independent operators, not a Pocket-owned fleet.

## Installation

Remote HTTP server with no auth - add it directly to any MCP client:

```json
{
  "mcpServers": {
    "pocketdrives": {
      "type": "http",
      "url": "https://pocketdrives.ai/mcp"
    }
  }
}
```

Booking is intentionally out of scope for the MCP layer - quotes and inventory are read-only, and the reservation completes in the Pocket Drives iOS app.

## Configuration

None required. The endpoint is public and keyless. If a workflow needs a reservation, the agent hands off the quote reference to the iOS app, which keeps payments and driver verification out of the agent path.

## Business Relevance

- **Travel planners and concierge desks** quote real total prices for exotic rentals in supported markets
- **Corporate travel ops** compare hosts on policy (mileage, delivery, deposit) before committing
- **Marketplace researchers** watch inventory mix, pricing and host concentration by market
- **Event and production teams** source specialty vehicles with venue and airport delivery

## Integration with CorpusIQ

Pocket Drives is the vehicle layer; CorpusIQ is the money layer. A composed workflow has Pocket Drives pull the quote while CorpusIQ reads the traveler's card spend from Stripe and the trip budget from QuickBooks, so the agent recommends a rental against the actual cost center instead of a guess. Fleet or concierge operators can log quoted-vs-booked spread across markets through CorpusIQ's analytics connectors.

## Limitations

- Five US markets today (Salt Lake City, Scottsdale, Orange County, Palm Springs, Las Vegas)
- Read-only - booking, payments and driver verification stay in the iOS app
- Peer-to-peer marketplace: vehicle condition and host reliability vary by host
- New listing (Aug 2026); pricing and policy data reflect hosts, not PocketList Inc
- No API key tier or write path exposed over MCP

## See Also

- [Secondhand MCP](/hermes/mcp/servers/external/secondhand-mcp/)
- [TradeBrite Dutch Vehicle Context](/hermes/mcp/servers/external/dutch-vehicle-context/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
