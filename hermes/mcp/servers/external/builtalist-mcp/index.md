---
title: "Builtalist MCP - 32,000 Buildings Worth the Detour"
description: "Five keyless tools over 32,000 works of architecture, plus competitions, live exhibitions, and one filter that does nothing."
category: "Travel / Architecture"
stars: "0 (hosted Streamable HTTP at https://builtalist.com/mcp, keyless, no account; five tools, all five driven)"
added: 2026-11-17
source: "the mcp.so submission queue entry #7507 filed 2026-11-17T11:31:55Z, and a driven session on 2026-11-17 in which twenty-two tools/call requests were run against the live endpoint with no credential"
relevance: ★★★
tags: [architecture, travel, buildings, exhibitions, competitions, culture, keyless, remote, mcp]
last_updated: "2026-11-17"
---

# Builtalist MCP

**Ask an assistant what architecture to see in a city and it names four buildings it is confident about, all famous, none of them near each other.** The information that decides whether a detour is worth a morning is not the building's name. It is whether the thing is open, whether it is the one example of its style in that city or one of nineteen, and what else is within walking distance.

Builtalist answers that with 32,000 works from antiquity to the present, ranked so that the ones that justify a journey come first, and it adds two surfaces the vendor description does not advertise: competitions and exhibitions that are open this week.

```
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://builtalist.com/mcp
Server:        builtalist, title "Builtalist", version 1.0.0
Protocol:      2025-06-18
Auth:          none
Tools:         5 (buscar_obras, ver_obras, buscar_historias,
                  buscar_concursos, buscar_exposiciones)
Website:       https://builtalist.com
Listed on:     the mcp.so submission queue as #7507
```

## The evidence tier

Keyless and driven. `initialize` answered **200** as `builtalist` **1.0.0** on protocol **2025-06-18**, `tools/list` returned five schemas, and **twenty-two** `tools/call` requests were run across all five tools, including four calls designed to make a filter fail. Everything below is the server's own output.

## The tool surface

All five tool names and every argument is in Spanish, which is worth knowing before wiring an agent to it: `ciudad`, `arquitecto`, `rango`, `visitable`, `limite`. A model with an English-only tool description will still read the schemas, but the argument names it must send are not English.

| Tool | Arguments | What it returns |
|---|---|---|
| `buscar_obras` | texto, arquitecto, ciudad, pais, cerca, etiquetas, desde, hasta, rango, visitable, orden, limite | Up to 20 works, most notable first, each with architects, year, place, tier and a link |
| `ver_obras` | ids, nombres | One record per work: why it is essential, sources cited, materials, and a photo with its licence |
| `buscar_historias` | texto | Long-form editorial stories with a read time |
| `buscar_concursos` | texto, desde, hasta, limite | Architecture competitions with the entry count and the winners |
| `buscar_exposiciones` | texto, desde, hasta, limite | Exhibitions open now, with address, closing date and ticket price |

## The ranking is the product

The instructions say about 2,600 works are essential and 3,300 more are featured. Those tiers are what the `rango` argument selects, and they behave consistently across cities:

```text
Barcelona, no range filter      518 works
Barcelona, rango=esencial        30 works
Madrid,    no range filter      756 works
Madrid,    rango=esencial        32 works
arquitecto=Gaudí                 23 works
```

So the essential tier is roughly 4 to 6 percent of a city's holdings, and it is not a keyword filter: the Barcelona four returned first were the Sagrada Família, Casa Batlló, Casa Vicens and Casa Milà, which is the answer a good local would give and not the answer a popularity index gives. Asking for one architect narrows to 23 works across every city rather than within one, which is the behaviour a traveller planning a Gaudí trip actually wants.

## Competitions and exhibitions, which the listing does not mention

The submission describes architecture worth visiting. The server also answers two research questions that a tourism listing cannot:

`buscar_concursos` returned competitions with the competition itself as the result and the **entry count and every winning team** attached. A 1989 Madrid museum competition came back with 13 entries and four named winners; a 1965 San Sebastián competition with 12 entries and three. That is the record of how a building was chosen, not only what was built.

`buscar_exposiciones` answered with the current date in the answer itself: *Exhibitions open in Madrid on 17 November 2026 (62)*. Each row carried the venue with a street address and postcode, the closing date, the price (including the reduced rate and what it is included in), and a two-sentence description. Six weeks of expiry is the difference between a list of museums and a plan for the afternoon.

## Provenance on the detail record

`ver_obras` is the page a suspicious reader should open first, because it shows its work:

```text
- Why it is essential in Builtalist: Gaudí's remodelling with an undulating
  façade and dragon roof, a UNESCO World Heritage Site
- Cited by 3 sources
- Materials and features: renovation, World Heritage Site, museum,
  apartment building, sandstone, aluminium, mosaic, glazed tile, cast iron,
  ceramic, cast iron
- Part of: Casa Amatller
- Photo: upload.wikimedia.org/.../Casa_Batlló,_Antoni_Gaudí.jpg (Canaan, CC BY-SA 4.0)
```

The citation count, the Wikimedia photo and the photographer's licence are all present. `ver_obras` also accepts a name instead of an ID and returned the identical record for "Casa Batlló", so an agent holding a name from a conversation can resolve it without a search step.

## The defect that made the filter test worth running

The `buscar_obras` schema advertises `visitable`. It does not filter:

```text
ciudad=Barcelona                    -> 518 works, ids bt-6wgi33n, bt-1ce0f9d8ab, ...
ciudad=Barcelona, visitable="si"    -> 518 works, ids bt-6wgi33n, bt-1ce0f9d8ab, ...
ciudad=Barcelona, visitable="no"    -> 518 works, ids bt-6wgi33n, bt-1ce0f9d8ab, ...
ciudad=Barcelona, visitable="maybe" -> 518 works, ids bt-6wgi33n, bt-1ce0f9d8ab, ...
```

Four calls, one count, one identical ID list in one identical order. Two separate faults are recorded here. The filter accepts its three values and changes nothing, and an out-of-enum value (`maybe`) is accepted silently instead of being refused the way `ciudad=Atlantisville` is. An agent that asks for places it can actually go inside will be given the whole city and no indication that the constraint was dropped.

This is the kind of defect that only appears when a filter is driven twice with opposite values. It is written down here rather than glossed because every other tool in the surface behaves correctly, and a reader should know which one does not.

## What it refuses well

An invented city is answered with a teaching refusal rather than an empty list:

> There is no city called "Atlantisville" in Builtalist. Try its English name (Lisbon, Munich, New York), the country, or "cerca" with its location.

Three recovery paths in one sentence, which is what a refusal should be. It also documents a real constraint: city names are matched in English, so a client sending `München` or `Lisboa` will miss unless it uses the local `cerca` route instead.

A minor inconsistency: IDs are not a fixed length. Casa Batlló is `bt-1ce0f9d8ab` (12 characters), the Sagrada Família is `bt-6wgi33n` (10), and a competition result was `bt-d83123aac2`. Any validation pattern assuming a constant width will reject valid IDs.

### Can an agent plan an architecture trip with this?

Yes, and the shape is unusually good for it. `cerca` takes a location, `rango` restricts to the essential tier, `ciudad` scopes to a city, and `buscar_exposiciones` adds what is open while the traveller is there. The gap is the inert `visitable` filter: opening hours and access are not answerable through this surface, so a plan built on it should not promise entry.

### Is the data current?

The exhibitions answer carried the day it was asked (17 November 2026) and closing dates within the week, so that surface is live. Sanity checks on the works side held: the Sagrada Família story states the church was begun in 1882 to a Neo-Gothic design, that Gaudí took it over from 1883, and that its tallest tower was finished in 2026, all of which match the public record. Read times are quoted per story (14 minutes for that one), which is a detail almost no data surface volunteers.

## Why it earns a page

The catalog had no architecture worth visiting surface, and `architect` appeared here only in software-architecture guides and a held Revit connector. More to the point, this is a curated dataset rather than a wrapper: the tier system, the competition record and the dated exhibition list are three different kinds of research answer from one keyless endpoint, and the detail record carries its citations and image licence.

It earns the entry with a defect attached, and the defect is the useful part for anyone about to build on it.
