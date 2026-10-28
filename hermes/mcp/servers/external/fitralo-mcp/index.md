---
title: "Fitralo MCP - European Road Freight Carrier Search"
description: "Find European road freight carriers by lane, equipment and certificate across 32 countries, keyless and read-only, and get contact details to call."
category: Logistics / Supply Chain
stars: ★★★ (200 keyless, full tools/list verified)
added: 2026-10-28
source: "live probe of https://fitralo.com/mcp returning HTTP 200 keyless on initialize as fitralo 3.73.33 on protocol 2025-06-18 with a full tools/list of 2 tools, plus the vendor page fitralo.com/ai and the carrier count printed on fitralo.com on 2026-10-28"
relevance: ★★★
tags: [freight, logistics, carriers, transport, europe, procurement, supply-chain, mcp]
last_updated: "2026-10-28"
---

# Fitralo MCP

**A load needs the right trailer, the right certificate and a carrier already running that lane. The broker who answers first is the one who knows who runs it.**

```
Server type: Remote (Streamable HTTP), keyless
Endpoint:    https://fitralo.com/mcp
Auth:        None for search and profiles
Tools:       2 at tools/list
Limit:       300 calls an hour per address, all tools together
Coverage:    15,763 carriers, 32 countries, updated 2026-10-28
```

## Why This Matters for Operators

Freight is the line item that quietly decides whether a small importer makes money, and the search for capacity is still done by phoning brokers. The knowledge is who runs a lane, who has a reefer that actually reaches Rome, who carries ADR and who will take groupage with a tail lift.

This server turns that knowledge into two calls. The agent writes the load in plain words, gets back the carriers that fit with what the search understood, and then opens the profile of the one worth calling, with the phone number and the email address attached.

It is catalogued because the business surfaces in this catalogue already cover parcels and US regulatory checks, and none of them answers this question: who moves this pallet from Venlo to Rome. `Ship24` tracks parcels across 2,500 carriers and `Carrier Ledger` vets US motor carriers against FMCSA records, so the freight forwarder searching capacity in Europe had no entry until now.

## What It Returns, Verified

A bare `initialize` on `https://fitralo.com/mcp` returned **HTTP 200** with no credential, `serverInfo` name `fitralo`, version `3.73.33`, on protocol `2025-06-18`. `tools/list` returned **two tools**, and both are read-only:

- **`search_carriers`** takes a plain-language load, the loading and delivery places as a town, postcode or country, plus what the load needs, and the vendor's own examples are the shape of the thing, `reefer from Venlo to Rome`, `ADR tank Rotterdam to Poland`, `groupage Germany to Italy, tail lift`, with `based in Italy` narrowing by country. It returns the carriers that fit, best first, at most ten by default and up to twenty-five, plus `carriers_that_fit` counting every match and a `results_url` for the full list on the site. The answer also reports what the search understood, so a mis-parse can be corrected by phrasing the query again rather than by guessing at filters.
- **`get_carrier`** returns one carrier's profile with its **phone, e-mail and website** plus where and how it carries. Contact details are deliberately held back from search results, so the agent has to pick a carrier before it can reach one.

The coverage number is the vendor's own and it was read on the day: the Fitralo homepage printed **15,763 carriers covering 32 countries, updated 28 October 2026**. The vendor documents the MCP address for Claude, ChatGPT and Gemini and states the commercial position plainly, free, no login and no commission.

## Limits Worth Recording

This is a directory, not a marketplace. It prices nothing, quotes nothing and books nothing, and the tool descriptions say so on every call. A rate still comes from the carrier, and the negotiation is still the operator's. The carriers are those that chose to be listed, so a carrier missing from a result is not proof that it does not exist, which matters before anyone reads absence as a finding. Coverage is **European road freight** only, so a sea, air or intercontinental load is out of scope. The rate limit of 300 calls an hour per address is generous for a person and not generous for a bulk enrichment job, and a query without a route or a need returns an error telling the agent how to write it rather than an empty list.

## FAQ

### Does it give freight rates?
No. It returns carriers that fit a lane with their contact details. Pricing and booking are the carrier's, and the server states it changes and books nothing.

### Do I need an API key or an account?
No. Both tools answer without a credential, and the rate limit is per address at 300 calls an hour across all tools.

### What happens when no carrier fits the load?
`carriers_that_fit` returns 0 and the list carries the closest carriers instead of an empty answer, so the agent can see how the query was read and widen it.

### Which countries are covered?
32 countries of European road freight, with 15,763 carriers listed at the time of writing, and the search accepts English, with the vendor documenting use in 14 languages.

### Can an agent contact a carrier on my behalf?
It can retrieve the phone number, e-mail and website with `get_carrier`, which is what the vendor exposes. Sending the enquiry is your decision and your outbound channel, not the server's.
