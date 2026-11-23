---
title: "Climatch MCP - A Climate Match for Any City You Pick"
description: "Nine keyless tools over 31,000 towns: monthly climate averages, town-to-town matches, and what grows where, all from TerraClimate."
category: "Data & Analytics"
stars: n/a (vendor-hosted)
added: 2026-11-23
source: "submission #7870 and canonical sitemap arrival /servers/climatch-co-agents; keyless initialize, tools/list and six tools/call requests on 2026-11-23"
relevance: ★★★★
tags: [climate, location, site-selection, agriculture, geospatial, keyless, remote-mcp]
last_updated: "2026-11-23"
---

# Climatch MCP

**Remote MCP server (Streamable HTTP, no authentication)** - nine read-only tools over a town-level climate table built from TerraClimate 1991 to 2020, covering 31,000 towns. It answers three separate questions with the same data: what the weather is like in one place, which places feel like this one, and which crops fit here.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://climatch.co/mcp
Server:      climatch 0.1.0, protocol 2025-06-18
Tools:       9 (search_places, get_climate, find_similar_climates, compare_climates,
             best_weather_in_month, weather_for_the_money, what_grows_here, list_crops, where_to_grow)
Data:        TerraClimate 1991-2020, 31,000+ towns
```

## Why This Matters for Operators

Location decisions are usually argued with anecdotes. A second warehouse, a support team spread across countries, a farm trial plot, a hire who wants to know what summer feels like: each one is a climate question with a number behind it, and the number is normally a monthly average that nobody has time to assemble. This server assembles it per town and, more usefully, computes a **match score** between two towns and states how they differ in words an operator can repeat.

It is also honest about scope. `find_similar_climates` excludes the home country by default and works above a 25,000 population floor, so "somewhere like London but warmer" returns real candidate towns rather than the suburb next door.

## Measured Behaviour

Six calls were driven on 2026-11-23, all keyless.

### One town, twelve months

`get_climate(place="Lisbon")` returned the full monthly table. August is the warmest month at **28.3 C / 83 F**, January the coolest at **14.7 C / 58 F** with nights at **8.1 C / 47 F**, the year carries **680 mm / 26.8 in** of rain at **72 percent** humidity, the best months are **June, May and September**, and the worst are **December and January**. July and August are described as *"almost completely dry"*.

### Two towns, one score, and the difference stated in a sentence

`compare_climates(a="Austin", b="Medellin")` returned:

- **score 6**, `seasonsFlipped: false`
- *"Compared with Austin, Medellin has 18 F (10 C) milder winter nights, 13 F (7 C) cooler summer days and three times the rain."*
- Austin **34 in / 869 mm** a year, Medellin **98 in / 2,482 mm**
- Austin's warmest month is August at **97 F / 36 C**; Medellin's is July at **82 F / 28 C**

The arithmetic reproduces from the returned month arrays, which is the test that matters for a guide: Austin's twelve monthly rain values sum to **869** exactly, its highest monthly high is **36.2 C**, matching the stated `warmestHighC`, and its lowest monthly low is **5.0 C**, matching the stated `coldestLowC`. Medellin's twelve rain values sum to **2,482** exactly.

### A town like this one, but warmer

`find_similar_climates(place="London", adjust=["warmer"], limit=5)` returned **Saint-Nazaire** and **Nantes** tied at rank 1 and 2 with a score of **87**, each with the difference stated: *"More sun"* and *"Wetter winters"*, plus a `compareUrl` for the side-by-side. The response echoes the search parameters it used, including `excludeHomeCountry: true` and `minPopulation: 25000`.

### A crop fit, with the limits named

`what_grows_here(place="Napa")` returned hardiness zone **9b**, **293** frost-free days, last spring frost **Feb 5**, first fall frost **Nov 30**, **861** chill hours, **669 mm / 26.3 in** of rain and **6** dry-season months. Wine grapes score **100** with the variety named as *"Hot-climate (Grenache, Zinfandel, Tempranillo)"*, `rainfedScore` also **100**, `needsIrrigation: false` and `limitedBy: null`. The summary lists its five best fits: wine grapes, barley, garlic, almond and lavender.

### The month ranked by comfort

`best_weather_in_month(month=3, country="ES")` returned **one** place, Las Palmas de Gran Canaria, at **22.2 C / 72 F** with **17 mm** of rain and **70 percent** humidity. Without the country filter the tool advertises thirty towns spread across countries.

## Defects and Limits

- **One advertised tool returns no data.** `weather_for_the_money`, which the manifest describes as ranking cities by weather against cost of living with a `sweet / pricey / tough` quadrant, answered `"Cost-of-living data isn't loaded on this server."` A client that routes a question to it gets an explanation rather than a ranking, and no error code.
- **`adjust` must be an array.** The schema and the description (*"stack freely"*) both imply a list, but passing the bare string `"warmer"` fails validation with a message that reads like a different problem: `expected array, received string at adjust`, then `Too big: expected string to have <=4 characters at adjust`. Send `["warmer"]`.
- **The country filter can return a single row.** `best_weather_in_month` promises thirty towns; with `country="ES"` it returned one. The breadth claim applies only to the unfiltered call.
- **It is climate, not forecast.** The underlying data is TerraClimate 1991 to 2020, so nothing here answers a question about next weekend.

### Does it need a key?

No. `initialize`, `tools/list` and all six `tools/call` requests answered **200** with no authentication header on 2026-11-23.

### Can it be used for agriculture decisions on its own?

Partly. `what_grows_here` gives a fit score, an irrigation requirement and the limiting factor, and `where_to_grow` answers the reverse question for a named crop. Neither replaces a soil test, a water right or local extension advice, and the response says which climate variables it scored on rather than presenting a single verdict.

### What does a low match score mean?

A score of 6 between Austin and Medellin is not a defect: it is two towns with almost nothing in common, stated as such, with the specific divergences named. The score is only useful next to the sentence that explains it, and the server always returns both.

## See Also

- [Location and geospatial data sources in the external catalogue](/hermes/mcp/servers/external/)
- [Sweep report for November 23, 2026 (night)](/hermes/mcp/sweeps/sweep-november23-2026-night)
