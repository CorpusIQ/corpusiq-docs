---
title: "EX & GO MCP - Ukraine Classifieds With Seller Registration"
description: "Forty-five categories in ten languages, real UAH prices, and the seller's registration number; the read-only public door needs no account."
category: "E-Commerce"
stars: n/a (vendor-hosted, MIT client repo)
added: 2026-11-22
source: "chatmcp/mcpso submission #7842 filed 2026-11-22T21:33:29Z; keyless initialize, tools/list, seven tools/call probes and the protected-resource document on 2026-11-22"
relevance: ★★★
tags: [classifieds, marketplace, ukraine, eastern-europe, product-feed, keyless, oauth]
last_updated: "2026-11-22"
---

# EX & GO MCP

**Remote MCP server with two doors - a read-only public endpoint that needs no account, and an OAuth endpoint for posting and account work.** The public door answers questions about a live classifieds marketplace in Ukraine and Eastern Europe: 45 categories, prices in hryvnia, geolocated cities named in ten languages, and the seller's business registration number where the seller is a trader.

```
Server type: Remote (Streamable HTTP)
Endpoints:   https://exgo.io/mcp/public   (read-only, no auth)
             https://exgo.io/mcp          (OAuth 2.1, PKCE, dynamic client registration)
Server:      exgo 2.0.0, protocol 2025-06-18
Tools:       6 on the public door
Registry:    io.exgo/marketplace 2.0.1, published 2026-11-22T21:34:00Z (2.0.0 on 2026-11-15)
Repo:        https://github.com/notformal/exgo-mcp (MIT)
Scopes:      listings:read, listings:write, partner:read
```

## Why This Matters for Operators

A marketplace with an agent door is a pricing and sourcing surface, not just a shop. The public tools answer what a thing costs in a city today, and the listing record carries the seller's legal identity: a Ukrainian sole trader's name, registration number, declared address, and whether the platform has verified that record. For anyone buying, arbitraging or reselling across that region, that is the difference between a phone number in an advert and a counterparty you can check.

## Measured Behaviour

Seven calls were driven on 2026-11-22 against the public door, all keyless. Every figure is quoted from the response.

| Call | Arguments | Answer |
|---|---|---|
| `list_categories` | none | **45** categories, each with its attribute set and names in 10 languages |
| `search_listings` | `category: elektronika` | **242** listings, **11** pages |
| `search_listings` | `q: iphone` | **10** listings, first is *Apple iPhone 16 128GB Teal (MYED3)* |
| `get_listing` | a returned id | full record: **698** UAH, `kyiv`, lat **50.4501**, lng **30.5234**, condition `new`, status `ACTIVE` |
| `account_links` | none | `signedIn: false` plus register, post, cabinet, plans, partners, API-token and `openapi.json` links |
| `list_live_shows` | none | `live: []`, `upcoming: []` at the read |
| `search_listings` | `city: Kyiv` | **400** `unknown city` |

### The taxonomy is product-feed grade

The category tree is not a loose tag list. Electronics carries `condition, brand, gtin, mpn, identifier_exists, merchant_language, merchant_excluded, color, size, gender, age_group, item_group_id, material, pattern`; phones add `model, memory, os`; laptops add `devicetype, ram, storagetype, screen`; cars carry `body, transmission, engine, drive`; flats carry `rooms, area, floor, floorstotal, buildingtype, renovation`. That attribute vocabulary is the Google Merchant Center set, which means an agent can filter on the same fields a feed submission uses.

Each category name ships in Bulgarian, Czech, English, Hebrew, Polish, Romanian, Russian, Slovak, Slovenian and Ukrainian. The city record does the same: `kyiv` resolves to Київ, Киев, Kyiv, Kijów, Kiev, Kyjev, Kijev, Киев and קייב in one object.

### The seller block is the part worth keeping

The listing returned a trader, not an anonymous advert:

```text
seller.trader.name                ФОП ЩЕРБАНЬ ОЛЕКСАНДР ІВАНОВИЧ
seller.trader.registrationNumber  1888904931
seller.trader.address             Полтава вул. Оксанченка 7-21
seller.trader.selfCertified       true
seller.trader.verified            false
seller.trader.phone               +380****4512   (masked in the listing payload)
```

The two flags are separate and both are published: `selfCertified` is what the seller declared, `verified` is what the platform checked. An agent that reports "verified seller" from `selfCertified: true` would be wrong on this payload.

### Prices are stated in the local currency, not normalised

Every listing carries `price` and `currency` (`UAH` in all reads), with no conversion. A question about a USD budget needs the exchange rate from somewhere else, and the server does not pretend to have it.

## Defects Recorded

- **City is slug-only and there is no city list.** `city: Kyiv` returns HTTP 400 `unknown city`; the working form is `kyiv`. No tool returns the valid city set, so an agent has to read a city slug out of a listing it already has.
- **An empty exact match returns a `related` array with `total: 0`.** `search_listings` on `legkovi-avto` at `maxPrice: 10000` returned no items and a `related` block of unrelated parts. Read `total`, never `items.length`, before telling a user the market is empty or full.
- **`attributes` filtering is undocumented in the tool description.** The schema accepts an `attributes` object and the categories publish the keys, but the accepted value forms are not stated.

## Setup

Read-only use needs nothing:

```bash
claude mcp add --transport http exgo-public https://exgo.io/mcp/public
```

Posting and account tools need the OAuth door at `https://exgo.io/mcp`; the protected-resource document at `https://exgo.io/.well-known/oauth-protected-resource/mcp` names the three scopes.

## What It Cannot Do

- **No write tools on the public door,** by design. All six are reads.
- **No cross-border price comparison** and no currency conversion.
- **No seller due diligence beyond the published fields.** The registration number is a string to check against the Ukrainian register, not a verification the server performs.

## See Also

- [Marketplaces MCP RU - Russian Marketplaces in One Connector](/hermes/mcp/servers/external/marketplaces-mcp-ru/) - the neighbouring regional marketplace surface
- [Print and Mail Company MCP - Physical Mail From an Agent](/hermes/mcp/servers/external/print-and-mail-company-mcp/) - the fulfilment step after a purchase
