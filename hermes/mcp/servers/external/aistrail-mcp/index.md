---
title: "AIS Trail MCP - Live Vessel Positions and Port Calls"
description: "AIS Trail answers ship questions from broadcast AIS data: live positions, port calls, tracks and sanctions flags by IMO, keyless for the live tools."
category: Compliance & Regulatory
stars: n/a (hosted API, no public repo)
added: 2026-10-21
source: "mcpservers.org /all page 1 (card aistrail-com-docs-mcp)"
relevance: ★★★
tags: [maritime, ais, vessel-tracking, port-calls, sanctions-screening, supply-chain, trade-compliance, remote-mcp]
---

# AIS Trail MCP

**Shipping questions usually need a maritime data subscription to answer. AIS Trail answers them from what vessels actually broadcast, and the live tools answer without a key.**

```
Server type: Remote (Streamable HTTP, stateless, one JSON response per POST)
Endpoint: https://api.aistrail.com/mcp
Auth: none for 6 live tools; an API key (Authorization: Bearer) for the 5 archive tools
Live check: unauthenticated POST initialize returned HTTP 200 (serverInfo aistrail-ais 1.5.1) and tools/list returned 11 tools
Protocol versions accepted: 2026-07-28, 2025-11-25, 2025-06-18, 2025-03-26
Vendor: AIS Trail (aistrail.com)
```

## Why This Matters for Operators

Any business that buys, sells, insures or finances physical goods eventually asks a question about a specific ship: where it is, whether it called at a sanctioned port, whether the arrival date in the spreadsheet is still true. Answering it from public sources means reading a live map and retyping what you see, and answering it properly means a per-seat maritime data subscription that costs more than the question.

AIS Trail serves the same data through the assistant, with the licence and source attribution attached to each answer. Positions are never interpolated and suspicious jumps are flagged rather than smoothed, which matters when the record may end up in a compliance file or an insurance claim.

## What It Actually Does

Eleven read-only tools, split by authentication rather than by topic.

Keyless, from the same live picture as the free public map: `search_vessels` finds ships by name, MMSI or IMO and returns live ships first with ships out of range carrying their last known position for up to seven days; `get_vessel` returns identity, flag, estimated deadweight and size class, last position, speed, course, heading, navigational status, destination and ETA; `vessels_in_area` lists ships heard in the last hour inside a box of up to 5 degrees per side, largest first, with an optional ship type; `vessels_near` does a radius search up to 50 nautical miles around a point or another ship; `find_port` resolves a port from the World Port Index and UN/LOCODE with the `port_id` the archive tools need; `data_status` reports how many ships are live, how far back each source's archive reaches, and whether the service is degraded.

Keyed, from the archive: `vessel_track` returns where a ship has been between two times, at raw resolution up to 24 hours, one minute up to 7 days and one hour up to 366 days, capped at 200 points per call; `vessel_port_calls` lists a ship's port calls with arrival, departure, draught, cargo estimate and a `sanctions` field; `port_calls` lists the ships that called at one port over up to 366 days; `vessel_events` returns computed events including stops, identity changes, gaps and encounters over up to 31 days; `lookup_vessels` returns archive records for up to 20 ships at once with the sanctions lists that name each IMO number, with programmes and dates.

Sanctions screening is the field that changes the use case. Port call and event rows carry the codes of the lists that name the ship's IMO, so an agent can flag a counterparty's vessel rather than describing it.

## Installation

```bash
# keyless live tools only
claude mcp add --transport http aistrail https://api.aistrail.com/mcp

# with archive access
claude mcp add --transport http aistrail https://api.aistrail.com/mcp \
  --header "Authorization: Bearer your_key"
```

Create a key at app.aistrail.com/signup. The vendor recommends a separate key per client because hosted gateways such as Smithery pass the key through.

## Limits Worth Knowing

Tool calls are limited to 10 per second per IP without a key and 20 per second per account with one. Bodies over 64 KB are rejected with 413, requests carrying an `Origin` header get 403, and JSON-RPC batches are not supported. Track requests cost 1 credit per vessel day. Private vessels, meaning pleasure craft, sailing vessels and Class B transponders without a valid IMO, are never listed individually on any plan; area and nearby results only count them.

## Pricing

Free at $0 with 500 credits a month and no card. Starter $29 a month or $290 a year for 15,000 credits, 12 months of history and boxes up to 2 degrees, with no live data and a 24 hour delay. Pro $129 a month or $1,290 a year for 60,000 credits, live positions and a WebSocket stream. Business $249 a month with live data, boxes up to 10 degrees and the highest credit allowance.

## FAQ

### Can I use it without an account?

Yes for the six live tools, which answer from the same picture as the public live map. The archive tools, including tracks, port calls, events and the sanctions lookup, need a key.

### How fresh are the positions?

Live tools report ships heard in the last hour and carry `live_stale_s` when the picture is not current. Archive responses say which source each position came from and carry the attribution the source's licence requires.

### Does it replace a sanctions screening provider?

No. It returns the sanctions codes and list names attached to an IMO number, which is evidence for a review, not a substitute for one.

## See Also

- [Compliance and regulatory servers](/hermes/mcp/servers/external/) in this catalog
- [CorpusIQ connectors](/docs/hermes/mcp/servers/) for the business data side of the same question
