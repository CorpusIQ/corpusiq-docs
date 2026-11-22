---
title: "eSIMX MCP - Travel eSIM Plans Priced in USD"
description: "Two keyless tools over the eSIMX travel catalogue: plan search by destination, days and data, and a whole-trip comparison that prices a multi-country route."
category: "Travel"
stars: n/a (vendor-hosted)
added: 2026-11-22
source: "mcp.so feed card stamped 2026-11-22 06:11 (UTC) for slug esimx-mcp; keyless initialize, tools/list and four tools/call requests on 2026-11-22"
relevance: ★★★★
tags: [esim, travel, data-plans, pricing, keyless, remote-mcp]
last_updated: "2026-11-22"
---

# eSIMX MCP

**Remote MCP server (Streamable HTTP, no authentication)** - two read-only tools over a travel eSIM catalogue. One searches plans by destination, duration and data volume; the other prices a whole multi-country trip and says whether one regional plan beats buying per country.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://api.esimx.com/mcp
Server:      esimx-public-catalog 1.0, protocol 2025-11-25
Tools:       2 (search_plans, compare_trip_options)
Currency:    USD, prices returned as cents and as strings
```

## Why This Matters for Operators

Travel connectivity is a pricing question with a coverage trap. A single-country plan looks cheap until the itinerary crosses a border, and a regional plan looks expensive until it replaces three purchases. This server is the first in this catalogue that answers both sides: it returns the plan list for one country, and it compares one whole-trip plan against one local plan per stop with the installation count and the total.

It is also unusually careful about what it is not. Three caveats ride on every response:

> eSIMX catalog only; not live supplier inventory or a market-wide lowest-price claim.
> 1024 MB = 1 GB. Unlimited allowances may be subject to fair use and throttling; high-speed quota is unknown.
> Obtain or activate each plan in time under its purchase, installation or first-connection start rule.

## Measured Behaviour

Four calls were driven on 2026-11-22, all keyless, each response stamped with a `checked_at` timestamp in UTC.

### One country, with the match count exposed

`search_plans(destination="Japan", days=7, limit=5)` returned **matched_count 37**, five shown, `truncated: true`. The cheapest rows:

| Plan | Price | Validity | Data | Activation |
|---|---|---|---|---|
| Japan 3GB 7Days | **3.50 USD** | 7 days | 3,072 MB | automatic |
| Japan 3GB 30Days | **3.80 USD** | 30 days | 3,072 MB | automatic |
| East Asia 3GB 7Days | 3.80 USD | 7 days | 3,072 MB | automatic |

The third row is the interesting one: thirty cents more than the cheapest single-country plan buys regional coverage instead of Japan alone. Every plan also carries `tethering`, a `product_url` that lands on the plan, and an `allowance_type` of `total` rather than daily.

`search_plans(destination="Portugal", days=15, min_data_mb=5000, limit=4)` returned **matched_count 30**, and the top two rows priced identically at **4.80 USD** for 5,120 MB over 30 days:

- **Europe 5GB 30Days** - 39 coverage country codes (AL, AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IS, IT, LI, LT, LU, LV, MD, ME, MT, NL, NO, PL, PT, RO, RS, SE, SI, SK, TR, UA, VA), throttle speed recorded as `128kbps`
- **Portugal 5GB 30Days** - Portugal only, same price, same throttle

A buyer going to Lisbon alone gains nothing from the regional plan. A buyer continuing to Spain gets 38 more countries for free, and the response makes that comparison possible without a second search.

### A whole trip, priced two ways

`compare_trip_options` with Japan for 7 days above 3,000 MB and South Korea for 4 days above 1,000 MB returned `total_days: 11` and the stops laid out as day ranges (1 to 7, then 8 to 11). Two options came back:

```text
single_plan    East Asia 5GB 30Days   7.80 USD   installation_count 1
               covers JP + KR among 11 country codes
local_plans    Japan 3GB 7Days + South Korea plan, one installation per stop
```

One installation against two, at a stated total. That is the decision a traveller is actually making, and the server states the trade rather than picking for them.

### A destination it does not hold is a clean not-found

`search_plans(destination="Atlantis", days=7)` returned `status: "destination_not_found"` with `candidates: []` and `isError` false. A named miss, not an exception. An agent can say "not in this catalogue" instead of retrying.

### One defect worth knowing before integrating

`compare_trip_options` declares `stops` without documenting its runtime requirements, and refused two calls in a row:

```text
arguments.stops[] requires destination
arguments.stops[] requires min_data_mb
```

Both keys are mandatory per stop even though the schema presents them as fields of the stop object. And separately, the server only answers `tools/list` when the client sends the `MCP-Protocol-Version: 2025-11-25` HTTP header. With the version negotiated only in the request body, `initialize` returns 200 and then `tools/list` returns **HTTP 400** with *Unsupported or missing legacy protocol version*. Most current clients send the header; a thin client that does not will fail at the second call with no obvious cause.

## What It Cannot Do

- It reads a catalog, not live inventory. Availability and supplier stock are not reported, and the response says the catalogue is not a market-wide lowest-price claim.
- Prices are USD list prices. Taxes and payment-method conversion are outside it.
- Two tools only: discover and compare. There is no purchase, activation or top-up path.
- Unlimited allowances carry an unknown high-speed quota, throttling is possible, and the response states that early purchase does not guarantee whole-trip coverage.

## Frequently Asked Questions

### Can an agent compare one regional plan against buying per country?

Yes. `compare_trip_options` returns a `single_plan` option with its installation count and total price beside a `local_plans` option that prices each stop, so the trade between one installation and the cheapest per-country plans is visible in a single response.

### Does it need an API key?

No. Both tools answered keyless on 2026-11-22, with prices quoted in USD and a `checked_at` timestamp on every response.

### Why did tools/list fail after a successful initialize?

Because the server requires the `MCP-Protocol-Version` HTTP header on subsequent calls in addition to the protocol version in the initialize body. Sending the header resolves it; the body-only negotiation does not.

## See Also

- [Travel and connectivity data sources in the external catalogue](/hermes/mcp/servers/external/)
