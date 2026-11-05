---
title: "Korzy MCP - US Parcel, Utility and Grid Data"
description: "Parcel records plus water, sewer, power-plant, grid-capacity and data-center project data for site due diligence in the United States."
category: Real Estate
stars: n/a (hosted, subscription)
added: 2026-11-05
source: "The chatmcp/mcpso submission #6806 (2026-11-05T15:22:33Z) in the November 5 2026 midday window; the official MCP registry record co.korzy/korzy at 1.0.0 published 2026-11-05T13:41:35Z with a streamable-http remote at https://api.korzy.co/mcp; HTTP reads on korzy.co/docs/mcp/ (200, the 16-tool table), korzy.co/docs/authentication/ (200, the key credential and scope rules), korzy.co/pricing/ (200, the plan prices and credit packs), korzy.co/datasets/ (200, the six dataset families) and korzy.co/openapi.json (200, 193,888 bytes, 34 routes with an x-korzy-credits block per route); and one keyless JSON-RPC initialize against the endpoint returning HTTP 401"
relevance: ★★★
tags: [parcel-data, utilities, grid-capacity, data-centers, environmental, site-selection, land, energy, us, read-only]
last_updated: "2026-11-05"
---

# Korzy MCP

**The property data in this catalog answers who owns a parcel, what it is zoned for and what it is worth. None of it answers whether the site can actually be served: whether water and sewer reach it, which treatment plant takes the load, how much transfer capacity the regional grid interface has left, what environmental layers cross the boundary, and which data-center projects are already being built next door.** That is the question a developer, a facilities planner or an expanding operator asks before an option payment, and Korzy answers it at parcel level from public records.

```
Server type: Remote, Streamable HTTP
Endpoint:    https://api.korzy.co/mcp
Auth:        OAuth 2.1 sign-in (agents) or an API key with the mcp:read scope
Version:     1.0.0 (registry co.korzy/korzy, published 2026-11-05)
Tools:       16, all read-only per the vendor
Pricing:     $49/month Professional (3,000 credits), $199/month Business
Coverage:    United States
Vendor:      Korzy, korzy.co (New York City)
```

**The evidence tier is stated rather than implied.** Every tool surface sits behind a credential: a keyless `initialize` against `https://api.korzy.co/mcp` returned **HTTP 401** with `{"detail":"Sign in or provide a valid Korzy credential"}`, so no tool was called and nothing below is a live payload. What was measured: the vendor's own tool table at `korzy.co/docs/mcp/` (**200**), the authentication rules at `korzy.co/docs/authentication/` (**200**), the plan prices at `korzy.co/pricing/` (**200**), the dataset families at `korzy.co/datasets/` (**200**), the registry record at 1.0.0 confirming the endpoint, and the **OpenAPI 3.1 spec** at `korzy.co/openapi.json` (**200**, **34** routes, each carrying an `x-korzy-credits` block). The credit figures below are read from that spec, mapped to the tools by route semantics.

## What the sixteen tools answer

| Tool | What comes back | Credits |
| --- | --- | --- |
| `list_datasets` | datasets, geographic coverage, source dates, layer keys and query limits | **0** |
| `get_state_summary` | parcel record counts and field coverage by state | **0** |
| `get_terrain_metadata` | terrain source resolution, units, coverage and limits | **0** |
| `search_parcels` | parcels at an address; `include_owner=true` adds owner fields and doubles the cost | **1** |
| `get_parcel` | one parcel's attributes by `korzy_id`, plus a map link | **1** |
| `get_site_context` | parcels at a point, **water and sewer service**, nearby treatment plants and nearby data-center projects | **2** (1 to 10, per 10 records) |
| `get_utility_record` | one water, sewer, treatment, gas or fiber record with standardised attributes | **1** |
| `get_environment_context` | environmental layers at a point such as **flood zones and wetlands**, plus nearby cleanup sites | **1 to 2** |
| `get_logistics_context` | nearby ports, rail, roads, airports and warehouses | **1 to 2** |
| `get_data_center` | one data-center project with observations, capacity evidence and a dated timeline | **1** |
| `get_power_plant` | a power plant and its generators | **1** |
| `get_transfer_capacity` | total and available transfer capability for a regional grid interface, in MW | **1** |
| `get_plant_energy_history` | generation, fuel, outages and generator inventory for a plant | **50** |
| `get_regional_energy` | state prices, energy and emissions, or hourly demand and fuel mix | **50** |
| `get_coal_mine_shipments` | reported coal receipts linking a mine to power plants | **10** |
| `get_parcel_terrain` | slope and elevation analysis over a parcel by `korzy_id` | **1** |

The three zero-credit tools are the practical entry point: `list_datasets` returns coverage and limits before any spend, which is how an agent should open a Korzy session.

## Why the utility and grid layer is the reason for the entry

The catalog already carries strong property records. [PropRaven](/hermes/mcp/servers/external/propraven-mcp/) holds 191.3M US parcels with ownership, permits, hazard scores and valuations. [Placestack](/hermes/mcp/servers/external/placestack-mcp/) reads parcel, owner, assessment, sales, permit and zoning records with permitted uses and dimensional standards. [Hercules](/hermes/mcp/servers/external/hercules-property-mcp/) reads ownership, mortgages and pre-foreclosure cases. [DFX](/hermes/mcp/servers/external/dfx-real-estate-mcp/) covers commercial and multifamily with debt timing. All four answer **what the record says about a parcel**.

Korzy answers **what the ground and the networks around it can carry**. `get_site_context` returns water and sewer service areas for a point together with the treatment plants that serve it, and `get_utility_record` reads the individual water, sewer, treatment, gas or fiber record with its attributes. `get_transfer_capacity` returns total and available transfer capability in MW for a named regional interface and date. `get_power_plant` returns the plant and its generators. `get_data_center` returns a project with its capacity evidence and dated timeline rather than a directory listing. `get_environment_context` returns mapped flood and wetland layers plus nearby cleanup sites, and `get_parcel_terrain` runs slope and elevation across the boundary.

The distinct question is the one an operator asks about a specific address: can this site be served, and who else is already building there. [DC Hub](https://dchub.cloud) covers market-level power for data-center siting across 300+ markets with the seven ISO feeds, and the catalog's energy entry reads all seven ISO interconnection queues as market data. Korzy is the parcel-level read of the same question, which is a different unit of decision.

## What it costs, in credits rather than adjectives

Korzy bills tool calls as credits against the same balance as its REST API. A call can make several data requests, and each call counts toward a per-minute rate limit. The credit blocks in the OpenAPI spec are specific: a point query that returns parcels costs **2** credits by default and scales **1 to 10** with per-record pricing at 10 records; `include_owner=true` **doubles** the cost of the parcel and site calls; a single utility, plant, project, environment or logistics record costs **1** to **2**; and the energy reads are the expensive ones at **50** credits for a plant's history or a region's demand and price series, **10** for coal receipts. At the Professional tier of **3,000** credits a month for **$49**, that is 1,500 parcel lookups or 60 regional energy reads, and extra credits are **$16 per 1,000**. Business is **$199** a month with unlimited seats and higher limits. Annual billing is **$490** and **$1,990**.

## Limits the vendor states, and one this pass adds

- **United States only.** The API is built on US public records, and the dataset page scopes coverage to them.
- **Area and list queries are not available yet.** The docs say point, address and record lookups today, with area search coming, so a screening pass has to iterate points rather than pull a polygon.
- **No free tier.** Three summary tools cost nothing to call, but the endpoint returns **402** with `subscription_required` when the account has no active subscription, so the zero-credit calls still need a paid account behind them.
- **Scopes are split.** An `api:read` key cannot use the MCP server and an `mcp:read` key cannot use the REST API; a request outside a key's scope returns **403**.
- **Concentration risk.** Every one of the sixteen tools is a lookup or a calculation and none writes, but the whole surface is one vendor's aggregation of county, state and federal sources, so a source date that lags is invisible unless the agent reads the summary tools first.

## Common questions

### Does Korzy replace a property records API?

No. It reads the parcel, but the entries that answer ownership, zoning, valuation and debt sit beside it: PropRaven and Placestack for records and zoning, Hercules for LLC and owner research, DFX for commercial debt timing. Korzy is the site-feasibility read on top of them.

### Can an agent use Korzy without a subscription?

Not for data. The three summary tools cost zero credits, but the endpoint answers **402** with `subscription_required` when the account behind the key has no active plan, so a subscription is the entry ticket and the credits are the meter.

### Is every Korzy tool read-only?

The vendor states all sixteen are read-only, and the routes in the OpenAPI spec are lookups and calculations with no write verb among them; the one proposal-shaped tool in its Danish-accounting neighbour does not exist here, and nothing in this surface stores a record. The claim is the vendor's, since no call could be made without a credential.

## How to start

1. Call `list_datasets` and `get_state_summary` for the state in question: both cost nothing and both report coverage and source dates.
2. Run `search_parcels` on the street address, then `get_parcel` for the `korzy_id` it returns.
3. Run `get_site_context` on the parcel point for water and sewer service, treatment plants and nearby data-center projects, then `get_environment_context` and `get_logistics_context` for the layers and access.
4. Pull `get_transfer_capacity` for the regional interface and `get_power_plant` for the generators behind it only when the site is still live, because 50-credit energy reads are where a screening budget goes.
