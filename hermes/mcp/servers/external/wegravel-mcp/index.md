---
title: "WeGravel MCP - Delivered Gravel Price by ZIP"
description: "A Florida bulk materials surface that turns a job size into a delivered truckload price for a ZIP code, with all four read-only tools driven here"
category: "Manufacturing & Industrial"
stars: "n/a (hosted; keyless, no account and no API key, Florida delivery ZIPs only)"
added: 2026-11-10
source: "the mcp.so feed card for wegravel at 2026-11-10T14:05Z and the mcp.so detail page at /servers/wegravel, which names the endpoint https://www.wegravel.com/mcp; the endpoint itself, where a keyless initialize answered 200 as wegravel 0.1.0, tools/list returned four read-only tools, and list_materials, calculate_quantity, get_prices and compare_prices were each driven to a live answer"
relevance: ★★★
tags: [construction, building-materials, aggregates, pricing, florida, quote, landscaping, streamable-http, keyless, remote-mcp]
last_updated: "2026-11-10"
---

# WeGravel MCP

**A contractor quoting a driveway does not need a price per ton. He needs the price of the truck that has to arrive, and those are two different numbers.** WeGravel's MCP server answers the second one: give it a material, a quantity and the delivery ZIP, and it returns a delivered total in dollars with the truck fee already inside it, plus a quote form on the vendor's site with the job filled in. Every tool is read-only, the endpoint is keyless, and the arithmetic that most surprised the measurement is in the full-load comparison it volunteers.

```text
Server type:  Remote (Streamable HTTP)
Endpoint:     https://www.wegravel.com/mcp
Auth:         none, no account and no API key
Tools:        4, all annotated readOnlyHint true and idempotentHint true
Scope:        Florida delivery ZIP codes only
Registry:     no official registry record found for this server
Discovery:    mcp.so feed, card created 2026-11-10T14:05Z
```

## What the endpoint says about itself

A keyless `POST initialize` answered **200** as `wegravel` **0.1.0** on protocol `2025-06-18` with no session id, so it is stateless, and its instruction string is the whole product in five sentences:

> WeGravel delivers bulk soil, sand, gravel and mulch in Florida only. A price needs the 5-digit ZIP code of the delivery address and a material slug from list_materials. For an area and a depth, calculate_quantity returns orderQuantity and unit for get_prices. get_prices returns one total in US dollars with delivery included. compare_prices prices several materials at one ZIP code. A ZIP code outside Florida has no price. quoteUrl opens the quote form on wegravel.com with the job filled in.

An instruction string that states its own geographic limit, names the tool that produces the argument for the next tool, and says plainly which ZIPs return nothing is a better spec than most vendor pages. `tools/list` returns exactly four tools, and every one carries the same annotations: `readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true`, `openWorldHint: false`. Nothing here writes, and nothing here reaches outside the vendor's own price book.

## Driven: the catalogue behind the slugs

`list_materials` returned the material list with a slug, a name, a category, a description and a unit for each row. The slugs are what every other tool takes, and the units differ by material: aggregates are sold by the `ton`, soils and mulches by the `yd3`. Categories seen in the response were `gravel-stone`, `soils-dirt` and `recycled-materials`, and the recycled row is described as same performance at lower cost and lower carbon, which is the kind of claim a buyer can test against the price rather than accept.

This matters more than it reads: the arguments are enums, not free text. A call with `material: "gravel"` did not fail silently, it returned a `McpToolInputError` naming the nine slugs that match: `4-crushed-stone`, `57-crushed-stone`, `67-crushed-stone`, `ballast-rock`, `gabion-stone`, `pea-gravel-89`, `rip-rap`, `road-base`, `stone-dust-screenings`. An agent that guessed is told exactly what to guess next.

## Driven: job size to order size

`calculate_quantity` with `57-crushed-stone`, a 30 by 20 foot area and 4 inches of depth returned the whole chain in one object:

```json
{"areaSqFt":600, "cubicYards":7.41, "tons":10, "unit":"ton",
 "orderQuantity":13, "safetyMarginPercent":25, "truckLoads":1}
```

Two things are worth pointing at. The unit it hands the next call is the material's selling unit, `ton`, not the unit the human thinks in, cubic yards. And `orderQuantity` is **13**, not the 10 tons the geometry produces, because the tool applies its own 25 percent safety margin and says so in a field rather than quietly inflating the number. A quoting assistant that overwrote that field with its own arithmetic would quote low and cost the operator the difference.

## Driven: the price, and the number that actually moves

`get_prices` for 7.4 cubic yards of `57-crushed-stone` at ZIP **33139** (Miami Beach) returned:

```text
total       $1,081.07     unitPrice $146.09 / yd3     truckLoads 1
fullLoad    16.8 yd3 at $114.39 / yd3 = $1,921.75
note        One truck carries up to 16.8 cubic yards. A full load costs
            $1,921.75 ($114.39 per cubic yard), $840.68 more than this
            order. A small order costs more per unit because the truck
            fee is the same.
```

That note is the product insight, computed by the server and volunteered to the assistant: at 7.4 cubic yards the unit price is **$146.09**, at 16.8 it is **$114.39**, so 27 percent of the unit price at the smaller size is the truck, not the stone. An operator deciding whether to order the rest of the project now, or to split it across two jobs, needs that comparison more than he needs either price. A server that returned only `total` would leave him to discover it on the invoice.

`compare_prices` at the same ZIP returned the same lens across materials, cheapest first, with the destination resolved for the reader:

```text
Fill Dirt            $44.89 / yd3   full load 18 yd3  = $808.02
Black Shredded Mulch $51.16 / yd3   full load 18 yd3  = $920.88
Road Base            $53.03 / ton   full load 21 ton  = $1,113.63
```

Each row carries a `quoteUrl` with the ZIP, the material slug and the estimated quantity already in the query string, and a `pageUrl` for the city and material page, so the last step is a form that is already filled rather than a search an operator repeats.

## The limit is the design, and it is stated

A call at ZIP **30303** (Atlanta) returned `UnsupportedZipError` with `"This ZIP is not supported. Please choose a Florida ZIP."` and `stateCode: GA` in the cause object. The address resolution works and the service is deliberately one state, which is the honest shape for a business that owns its own trucks. One more argument detail a client has to get right: the `unit` field accepts `yd3` or `ton` only, and `cubic_yard` is rejected by the schema with a message that lists the two valid values.

## The class it enters, with the owners named

Materials and construction neighbours already in the catalog are adjacent rather than overlapping. [FindingSteel](/hermes/mcp/servers/external/findingsteel-mcp/) carries GB steel section properties and a welded-section calculator: the properties of a member, with no price in it. **ATLASS OS**, **nebelus**, **profitelligence** and **klarix** sit in construction ERP, project and financial intelligence, which is what a contractor runs after the material is bought. What none of them answers is the question that precedes the purchase order, which is what the truck costs delivered to this address today. This entry is also a narrower kind of surface than the catalog usually carries: one supplier's own price book for one state, with no account and no key, which makes it useful for a quote and not for a market comparison across suppliers. That distinction is worth stating in the guide rather than discovering in use.

## Limits, stated as limits

One state, Florida, decided by delivery ZIP. One supplier's prices, so this is not a marketplace and not a benchmark. No order history and no time series, so a trend question has no answer here. No ordering, no account and no cart: the server ends at a quote link. And the depth of the material list is the vendor's catalogue, which is broad for a single supplier and still one catalogue.

## Frequently asked questions

### What does the price include?

Delivery to the given Florida ZIP, as one total in US dollars. The response also returns the per-unit price and the full-load equivalent, which is where the difference between the two lives.

### Why is the per-unit price higher for a small order?

Because the truck fee is fixed. At ZIP 33139 the same crushed stone is $146.09 per cubic yard at 7.4 yards and $114.39 per cubic yard when the truck is filled to 16.8 yards. The server computes and states that gap rather than leaving it to the invoice.

### Does it need an account or an API key?

No. The initialize handshake, the material list, the quantity calculator and the price lookup all answered without a credential.

### Can an agent outside Florida use it?

Only for the arithmetic. Any ZIP outside Florida returns `UnsupportedZipError` with the state code in the cause, so a client should treat the state as an argument it validates before it calls.
