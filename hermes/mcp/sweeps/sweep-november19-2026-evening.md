---
title: "MCP Server Discovery - November 19, 2026 (Evening)"
description: "A six-hour window where the directory grew by 285 raw entries and carried all three finds: a loan-limit table, an importer finder, a funding register."
category: "MCP Ecosystem"
last_updated: "2026-11-20"
---

# MCP Server Discovery - November 19, 2026 (Evening)

Fired on the **21:00 MST** tick, six hours after the midday supplement closed at **18:10Z**. For the first time in three passes the canonical moved, and for the first time this week all three catalogued products came out of the directory itself rather than the feed or the submission queue.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,962   against 66,677 at the 18:10Z capture = +285
  servers/1  ..... 7,588  (held)     servers/7  ..... 9,351  (held)
  servers/2  ..... 5,949  (held)     servers/8  ..... 6,590  (held)
  servers/3  ..... 6,518  (held)     servers/9  ..... 4,022  (held)
  servers/4  ..... 6,746  (held)     servers/10 ..... 2,608  (held)
  servers/5  ..... 6,954  (held)     servers/11 ..... 2,637  (held)
  servers/6  ..... 6,756  (held)     servers/12 ..... 1,243   (was 958, +285)
  the twelve counts sum to 66,962 exactly
priority-servers.xml          299 raw,  34 distinct keys
remote-mcp-servers.xml         15 raw,   0 distinct keys
distinct keys, twelve maps    22,952 against 22,717  = +235 keys
distinct keys, union basis    22,986 against 22,752
lastmod rows at or after the cutoff   1,335 raw rows, 509 distinct keys
  of which servers/12         251 keys (the arrival map)
  of which maps 1-11          258 keys in maps whose raw counts did not move
mcp.so /feed                  200, 158,554 bytes, 30 stamps, 26 derived cards,
                              6 cards above the cutoff
submission queue              #7668 to #7685, seventeen arrivals, one number gap
```

The rise is honest and it is narrow: **every one of the 285 new raw entries landed in `servers/12`**, the tail map that has carried each wave of the week, and no other map moved by a single entry. Three readings agree on the shape: the per-map counts, the distinct key set (**+235** on the comparable twelve-map basis) and the stamp window (**251** distinct keys inside `servers/12` against **258** in maps that did not grow, which are re-stamps of keys the capture already carried).

## What shipped

Three servers, each with a guide, and each guided by what the pass could measure rather than by what the card claimed.

- **[FigureDeck](/hermes/mcp/servers/external/figuredeck-mcp/)** at `https://mcp.figuredeck.com/mcp`, *figuredeck* **1.0.0** on protocol **2025-06-18**, stateless with no session id, **three** tools that publish both an `inputSchema` and an `outputSchema`, registry `com.figuredeck/conforming-limits` **1.0.0** published **2026-11-19T02:56:42Z**, no key. The catalog's first federal conforming-limit table. Los Angeles County at **$1,249,125**, exactly **1.5** times the **$832,750** baseline; **3,235** counties with **3,075** at the baseline and **160** high-cost; a true maximum of **$1,299,500** in Kalawao and Maui counties, Hawaii, which sits above the statutory 150 percent ceiling. Every figure reproduced by hand, including a **$450,000** loan at **6.5** percent returning **$2,844.31** a month, **$1,023,950.20** total and **$573,950.20** of interest, and an affordability ladder at **28 / 36 / 43 / 50** percent DTI matching to the cent. Three defects recorded: no validation on `loan_amount` (**-100** returns *"Over 0 payments"* with `isError: false`), a citation on both calculation tools that points at the conforming-limits file instead of an amortisation source, and a `limit` above 100 clamped silently.

- **[Reevi](/hermes/mcp/servers/external/reevi-mcp/)** at `https://reevi.ai/mcp`, *reevi* **1.0.0**, **one** tool, registry `ai.reevi/find-buyers` **1.0.0** published **2026-11-17T15:21:45Z**, keyless with five searches a day per connection. Driven once: **stainless steel kitchen sinks** into the **United States and Germany** from an exporter in **India**, restricted to wholesalers and distributors, returned **12** buyers in **23.1** seconds with fit scores **92 / 88 / 86 / 82 / 80** on the A grades and a reason per company, against a stated pool of **2,388** importers in those markets. The report link answers **200** at **108,134** bytes with no sign-in, two of the returned companies were opened to confirm what the reason claimed, and the free counter decremented from **5** to **4** inside the response.

- **[Raising.fi](/hermes/mcp/servers/external/raising-fi-mcp/)** at `https://raising.fi/api/mcp`, registry `fi.raising/raising` **1.0.0** published **2026-11-19T04:36:21Z**, **documented tier**: no credential is held, so `initialize` answered **401** and no tool was driven. The gate is recorded in full - a complete `WWW-Authenticate` challenge naming one scope, a **251-byte** protected-resource document at **200**, and the issuer's RFC 8414 document at **200** carrying authorization, token, **dynamic registration**, revocation, authorization code with refresh and PKCE **S256**. Five tools are named by the vendor's developer page and two REST surfaces answer without a key: `/api/v1/health` at **200** and `/api/v1/openapi.json` at **200** (**11,917** bytes, OpenAPI **3.1.0**). The guide states plainly that no figure from the dataset appears in it.

## What the wave itself was

The **251** keys stamped inside `servers/12` were worked as a set before any of them was treated as a product. Counted by prefix and by exact prior match:

```text
cotlet-dev-integrations-*        50 slugs   one publisher, per-app integration wrappers
apify-com-cliqtomedia-*           5 slugs   actors, held on the Apify distribution ruling
mambalabsdev/*                    5 slugs   the same publisher fleet already dispositioned
priberry-data/*                   3 slugs   the priberry trio already held
documentation and agents mirrors  30 slugs   docs-, developers-, llms.txt and agents pages
exact prior match on name         22 slugs   adanos, drint x2, fopost, amberflip, chemdraw,
                                             slimchance, cortex, plinth, dmswift and others
remainder                        136 slugs   read by hand: three catalogued, the rest prior
                                             holds under product spellings (contha, optimatika,
                                             visamundi, lafo, sparklayer, tzedek, paletoo,
                                             mebius) or consumer and utility listings
genuine products catalogued        3         FigureDeck, Reevi, Raising.fi
```

A wave of **285** raw entries therefore produced **three** products, and the discipline that made that visible was classifying the whole stamped set before ranking any single slug. The cotlet fleet is one publisher shipping a per-app integration wrapper; previous passes have catalogued its standouts and held the remainder, and this pass adds no product from it.

## What was held

Twenty-three candidates, each with the gate or the class owner named.

| Arrival | Held because |
|---|---|
| node-mantis (feed, 02:44Z) | plain-English browser tasks returning structured data, agent browser-automation class |
| ASIN402 Amazon Data (feed, 19:56Z, registry 1.3.0) | Amazon marketplace data, carried by [Datrace](/hermes/mcp/servers/external/datrace-mcp/) and [Pangolinfo](/hermes/mcp/servers/external/pangolinfo-mcp/) |
| Senpi AI Quant (feed, 19:17Z) | Hyperliquid quant, trading class saturated |
| Aisma (feed, 19:56Z) | video editing, media class |
| VakayMood (feed, 00:43Z) | timeshare inventory, travel class |
| Caoliao QR Code (feed 02:26Z, queue #7681) | QR forms and inspection records, regional Chinese utility with OAuth on the admin side |
| Helve (#7668) | pay-per-call gateway over 313 tools and 255 providers, agent infrastructure rather than a business data surface |
| Gadwal (#7669) | proprietary Mac database client, closed source, local stdio built into a desktop app |
| souq-mcp (#7671) | crypto arbitrage and orderbook telemetry, trading class |
| chemdraw-mcp (#7672) | chemistry structures, science vertical |
| signafAIde (#7673) | signed records of agent tool calls, agent governance class carried by Arobi in the same window |
| Wigoo (#7674) | travel eSIM, travel class |
| Cnamio (#7675) | custom-domain DNS automation, developer infrastructure |
| Prompt and Co (#7676) | shared agent operational memory, knowledge class rather than business data |
| AvatarSay (#7677), Scenewright (#7678) | avatar video and Blender scene generation, media and creative classes |
| Innovative Workspace (#7679) | a not-for-profit consultancy's own services, pricing and FAQs, single-vendor brochure surface |
| GeoReady (#7680) | GEO and llms.txt auditing, visibility class carried by geolint and LogNorm |
| ChinaKit, ChinaVisaCalc, ChinaDriveTest (#7682-7684) | one Chinese publisher's regional utilities, filed inside the same minute |
| Arobi Immaculate (#7685) | pre-action governance verdicts, governance class, free tier of 110 workspace credits |

The queue window is **#7668** to **#7685** with **#7670** absent from the list, so seventeen arrivals rather than eighteen. `/all` was not re-read: **403** by edge policy, the standing condition since 4 November.

## Listing check

Measured rather than inherited:

- mcpservers.org carries `https://mcpservers.org/servers/corpusiq-io` in the fresh twelve-map capture (**15** occurrences including locale forms, beside the fifteen for `/servers/corpusiq/corpusiq-docs`), which is stronger evidence than a detail page that answers **403** by edge policy.
- mcp.so remains not listed: all four slugs (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) answer **404**.
- Glama answers **200** at `/mcp/connectors/io.corpusiq/multi-source-mcp`.
- Smithery answers **200** on the `Cprusiq` server record at `registry.smithery.ai/servers/<publisher>/Cprusiq`.

## Counts

```text
canonical            66,962 against 66,677    +285, all inside servers/12
distinct keys        22,952 against 22,717    +235 twelve-map, 22,986 union
lastmod rows >= cutoff   1,335 rows, 509 distinct keys, 251 of them in servers/12
feed                 158,554 bytes, 30 stamps, 6 cards above the cutoff, 0 shipped
queue                17 arrivals, 0 shipped
candidates held      23 (6 feed, 17 queue) plus 45-fleet and prior-disposition cohorts
guides               3 added
```
