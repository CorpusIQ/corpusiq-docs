---
title: "NuaSense MCP - East African Farm and Market Data"
description: "County fertilizer and crop prices, satellite demand and food security for Kenya, Tanzania, Uganda and Rwanda behind an OAuth MCP gateway"
category: Business Operations
stars: "n/a (hosted; OAuth with dynamic client registration on the endpoint, API key on the REST twin)"
added: 2026-11-10
source: "chatmcp/mcpso submission #7089 filed 2026-11-10T17:21:13Z and the official registry record com.nuasense/agri-data 0.9.0; the endpoint at mcp.nuasense.com measured with a POST initialize that answered 401 and a protected-resource document naming three scopes plus a registration endpoint; the dataset, analysis and limit vocabulary read from the vendor's own machine-readable documentation at api.nuasense.com/index.md and llms-full.txt"
relevance: ★★★★
tags: [agriculture, fertilizer, commodity-prices, kenya, tanzania, uganda, rwanda, food-security, satellite, farm-sensors, oauth, remote-mcp]
last_updated: "2026-11-10"
---

# NuaSense MCP

**An agri-input dealer in Nakuru and a trader in Kampala are asked the same question every week, which is what fertilizer costs right now and whether to buy. Both answer from the last price they heard.** NuaSense is the first server in this catalog that answers it from county price records, says which source each row came from, and, in the one place where it matters most, refuses to answer at all rather than model a number it cannot support.

```text
Server type:  Remote (Streamable HTTP)
Endpoint:     https://mcp.nuasense.com/mcp
Auth:         OAuth, console sign-in, dynamic client registration
Scopes:       market:read, farm:read, alerts:write
Registry:     com.nuasense/agri-data, version 0.9.0
Coverage:     Kenya, Tanzania, Uganda, Rwanda, plus pan-African layers
REST twin:    https://api.nuasense.com/api/nuasense/v1 (API key, 40 datasets)
Docs:         https://api.nuasense.com/index.md and /llms-full.txt
```

## What the endpoint answers before it will talk

A keyless `POST initialize` on both `https://mcp.nuasense.com/` and `https://mcp.nuasense.com/mcp` returned **HTTP 401** with `WWW-Authenticate: Bearer resource_metadata="https://mcp.nuasense.com/.well-known/oauth-protected-resource"`, and the body was a JSON-RPC error object rather than an empty page:

```json
{"jsonrpc":"2.0","id":1,"error":{"code":-32001,
 "message":"Unauthorized: sign in via the connector (OAuth) or send a valid 'Authorization: Bearer ***'."}}
```

That distinction is the one this catalog keeps recording, and it is worth recording again: an error object on the protocol the client speaks proves a working server behind the gate, and an empty 401 proves only a gate. Following the path the header named, `/.well-known/oauth-protected-resource` answered **200**:

```text
resource:              https://mcp.nuasense.com
authorization_servers: https://mcp.nuasense.com
scopes_supported:      market:read, alerts:write, farm:read
bearer_methods_supported: header
```

The authorization-server metadata on the same host adds the part that decides whether an agent can onboard itself at all: `registration_endpoint` at `/register` (dynamic client registration), `grant_types_supported` of `authorization_code` and `refresh_token`, and `code_challenge_methods_supported` of `S256`. An MCP client that supports OAuth with DCR can connect with the URL alone. The vendor's own instruction is one line, quoted verbatim for Claude Code: `claude mcp add --transport http nuasense https://mcp.nuasense.com/mcp`.

Nothing past the handshake was driven, because the session needs a sign-in. Everything below about datasets, analyses and limits comes from the vendor's machine-readable documentation and is labelled as documentation, not as measurement.

## What the product actually is

Two layers, one key. The **farm** layer is the readings from weather stations and soil probes you connect, with the agronomy computed from them: hourly and daily roll-ups, disease and pest risk, a forecast corrected to your station, root-zone water balance, satellite vegetation and SAR indices on your field polygons. The **market** layer is the layer a business operator cares about without owning any hardware: county and market prices for commodities and fertilizer, satellite demand indices, cropland and crop mix by county, food-security phase classifications, rainfall against normal, regulatory signals, and 30-plus ready-made analyses that answer a question in one call.

The declared catalogue is **40 datasets and 339 fields**, split 18 farm datasets with 189 fields and 22 market datasets with 150 fields. The market layer is where the operator questions live, and the paths are plain: `/market/prices` for commodity and fertilizer prices updated daily to monthly by source, `/market/input-prices` for crop-protection and input retail prices, `/market/demand-indices` for satellite demand at a ten-daily and weekly cadence, `/market/food-security` and `/market/fews-population` for the phase classifications and the people-in-need counts, `/market/rainfall-subnational` for dekadal rainfall against normal by admin unit, and `/market/regulatory` for weekly legal and regulatory signals.

## The design decision worth copying

The single most interesting line in the documentation is a refusal. The `/farm/soil-baseline` dataset ships without pH, organic carbon or N, P and K, and the docs say why: modelled values cannot support a fertilizer decision, and current fertility comes only from a soil test. A platform that sells data, in a market where a wrong pH number leads directly to a wrong fertilizer purchase, chose to publish nothing rather than a modelled guess, and wrote the reason into the same page a developer reads.

Two more signs of the same discipline. `/market/trade` and `/market/field-structure` are declared with two fields and answer **451** when called, which is an explicit "unavailable for legal reasons" rather than an empty array that reads like zero. And every market row carries its source and a trust field, with a `signal_type`, `direction`, `trust` and `horizon` filter set on the news dataset, so a client can ask only for high-trust signals instead of taking everything.

## What an operator can ask it

The ready-made analysis layer at `/api/partner/v1/market` is a list of questions with a measured answer, one call each, and it is the most operator-shaped surface in the product. The fertilizer family is the sharpest: `?variety=dap&county=nakuru` for the current price, the rank of dearest and cheapest counties, the price in each individual market inside a county, the trend and the size of the move, seasonality by month of the year, a backtest of whether the seasonal rule would have made money, the retail-minus-wholesale margin, a comparison of official prices against online asking prices, the gap to the world benchmark, and affordability for farmers in the county. The commodity family adds the spread between markets net of a lorry cost the caller supplies, the lag from Nairobi to a local market, county inflation, yield risk, whether the season has started and whether the rain that starts it is coming. Coffee grade AA and tea factory league tables sit beside county briefs, market size, importers and landed cost.

For CorpusIQ readers the useful part is the shape, not the list: each of those is a question an operator would otherwise answer by assembling a spreadsheet from three websites, and each returns a computed answer with the inputs visible.

## Access, units and the limits stated as limits

The market layer and the catalogue open with a free account. A console key carries `market:read`, `farm:read` and `location:read`, and `alerts:write` when alerts are ticked at creation. A key requires a verified phone, which is the one step the vendor keeps for a human.

Pricing is by **units, not calls**: one row of market or location data is one unit, an analysis is one unit and priced as an analysis, and your own farm data is one unit per call whatever it returns.

```text
no credit      100 rows per call   200 units/day   1,000 units/month   30 days history
with credit  1,000 rows per call 1,500 units/day   no ceiling          full history
your station 5,000 rows per call 1 unit per call   no ceiling          full history
rate         60 requests per minute per key
headers      X-Daily-Limit, X-Daily-Remaining, X-Monthly-Remaining,
             X-Credit-Balance, X-RateLimit-*
```

The honest limits are the ones worth writing down. Coverage is four countries, with pan-African layers that are thinner than the county data. Per-field approval means a key may not reach every dataset, so the correct first call is `GET /catalog` with your key and the correct second step is to build only against what it lists. Two market datasets are withheld with 451. The FEWS NET cross-border trade layer runs to September 2024 for East Africa, so a flow question has a stale edge that a client should state. And the licence buys use, not ownership: rows may go inside your product and reporting, not be resold as data.

## The class it enters, with the owners named

Farm data is already in the catalog, and neither neighbour does this. [Regeno Farmwalk](/hermes/mcp/servers/external/farmwalk-mcp/) is UK farm and subsidy data with 24 OAuth-scoped tools over organisations, agreements, parcels and compliance. [upCampo](/hermes/mcp/servers/external/upcampo-mcp/) is a farm management system exposed to chat: harvest progress, per-hectare yields, rain per field, pest alerts, cost per hectare. Both describe **your own operation**. NuaSense is the first entry here that describes the **market around it**: what inputs cost in a named county this week, which counties are building demand, what the food-security phase is, and how the local price compares with the world benchmark. That it carries both layers, and computes spray windows from a station of any brand, is the reason it is a guide rather than a hold.

## Limits, stated as limits

Four countries. Gated at the handshake, so the tool list on the MCP endpoint is documentation rather than measurement; the REST twin is the fully documented surface. A key needs a verified phone. Prices are as fresh as their sources: daily for input prices, monthly for several market layers, and the trade layer carries a 2024 edge. And no part of this replaces a soil test, which the vendor says itself.

## Frequently asked questions

### Is the data a model or a record?

Both, and the difference is labelled. Market rows carry their source and a trust value, and the one dataset where a model would be dangerous, soil baselines, omits fertility fields entirely instead of estimating them.

### Can an agent connect without a human?

The endpoint supports dynamic client registration with PKCE, so the connection is automatable. The account behind it is not: a key is issued only after a verified phone, and the market layer's free allowance is tied to that account.

### What does a question cost?

One unit per analysis call, and one unit per row of market data, with 200 units a day and 1,000 a month before any credit is bought. A county-level answer is a handful of units, which is the intended shape: many small measured questions rather than one bulk export.

### Does it need hardware?

No. The market layer needs nothing but an account. Stations are optional, and the first three connect free, at which point the farm layer begins to answer spray windows, disease risk and irrigation need for the exact location.
