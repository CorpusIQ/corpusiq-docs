---
title: "MCP Server Discovery - November 2, 2026 (Midday)"
description: "Midday sweep of the mcp.so submission window, the mcp.so feed and the mcpservers.org newest page: one new server catalogued, a keyless local-business shelf, and all five tracked listing surfaces re-probed."
last_updated: 2026-11-03
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november2-2026-midday"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 2, 2026 (Midday Sweep)

## Summary

Seven hours after the night pass, and the delta sat in the place the gap predicted: the submission window, not the feeds. **36** submissions landed on `chatmcp/mcpso` between **#6585** at `04:09:42Z` and **#6620** at `16:36:30Z`, and every one of them was read with its body in a single authenticated call. The mcp.so `recentServers` block carried **30** cards with a date and the newest at `2026-11-02T14:39:24Z`, five above the night stamp of `2026-11-02T09:04:11Z`. The mcpservers.org `/all` page behaved as recorded for the fourth pass running: the first fetch returned **18,732**, a counter below the night read, with thirty slugs that were the previous page, and the second fetch, cache-busted with a nanosecond stamp and a different user agent, returned **18,887** with the page turned over.

One arrival earned a guide. **Versum MCP** is a free, keyless, read-only index of US local businesses built from the businesses' own websites, and it answered six tools live: **128** trades, **5,398** cards, a menu price of **$12.95** with the quote from the shop's own page attached, and an honest `availability: unknown` beside it.

All five tracked listing surfaces were re-probed this run because the night pass recorded them as not run.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| chatmcp/mcpso issues | one authed call, bodies included | window **#6585** to **#6620**, **36** submissions, all read |
| mcp.so homepage `recentServers` | direct, 30 cards with a date | newest `2026-11-02T14:39:24Z`, five above the night stamp `2026-11-02T09:04:11Z` |
| mcpservers.org `/all` | r.jina.ai, `X-Return-Format: html`, read twice | first read **18,732** (stale, previous page), second read **18,887** live, 30 slugs |
| Canonical capture window | existing captures on disk | no fresh twelve-sitemap refresh this class; the night capture is the baseline |
| Listing surfaces | 5 probes | all recorded below |

## New Servers Catalogued

### Versum MCP - The Local Shop Shelf an Agent Can Quote

Relevance: HIGH. **Endpoint driven keyless** (`initialize` HTTP 200, `serverInfo` `versum-catalog` **1.6.0**, **13** tools in 50,179 bytes of schema, six tools called live).

A free read-only index of real local businesses in the United States, read from each business's own public website. `list_niches` returned the whole index in one object: **128** trades, **5,398** cards, **9,300** businesses, with per-trade coverage states and the city zones behind them, each carrying the date it was last passed. Restaurant is **783** cards over **1,042** businesses and `partial` for a stated reason; florist is **183** over **316** and `complete`.

The measured answer is the shape worth copying. `search_catalog` for pizza in Tampa returned **12** matches inside **15** miles, and the top card is a real shelf: Green Bench Brewing Co., **0.3** miles away, `(813) 867-8804`, FOUR CHEESE PIZZA at **$12.95** and Pepperoni at **$14.50**. `get_offering` returns the price as a claim with its evidence: `price_state: confirmed, basis: published, source: semantic_html`, `evidence.quote: "$ 12.95"`. Beside it, `availability_state: unknown, basis: not published`. Somebody can be told what a pizza costs and cannot be told whether it is in stock, and both arrive labelled. `find_business` with `needed_by` resolved the timestamp to `open_at` and returned a task card with the hours state `confirmed`, the reasoning `open at 19:00 by the published hours`, and the five cheapest items priced. `quote_order` failed honestly: `placed: false`, `reason: no_public_cart`, with a note that the shop's public cart priced it in its own session which was emptied, only the delivery address was sent, and nothing was kept.

It earns a guide because nothing else here reads a local shop's own shelf: [GBPly MCP](/hermes/mcp/servers/external/gbply-mcp/) manages your own profile, [Listings API MCP](/hermes/mcp/servers/external/listings-api-mcp/) publishes out to 80 plus directories, and [GoodLeads MCP](/hermes/mcp/servers/external/goodleads-mcp/) sells new-business filing leads. [Undercart MCP](/hermes/mcp/servers/external/undercart-mcp/) is the nearest neighbour and covers online Shopify stores, not the shop with a Squarespace menu and a phone number.

Guide: [Versum MCP](/hermes/mcp/servers/external/versum-mcp/)

## Also Identified (Not Catalogued)

From the mcp.so feed, the five cards above the night stamp resolve to covered classes: `paperjoy-01f7bf` sends real handwritten postcards inside Poland (consumer print, the `paddock-cards` precedent); `442ball` serves football club power ratings (sports data); `builders-in-fintech` is a fintech news and funding feed (news syndication); `eddyter-ai-rich-text-editor-mcp` is a rich-text editor integration (content tooling); `forge-by-ui8` is a hosted agent front-end from a design-asset vendor (developer tooling).

From the submission window, the substantive candidates were read to body level and held on class:

- **Local Business Facts (Agentric)** (#6590) - one tool, `lookup_business {url, country}`, and it answered keyless with real facts on `halelifebakery.com`: `confidence: 0.86`, `name` from `schema.org`, `phone` with an `e164` form, `address`, `fetched_at 2026-11-02T17:03:13Z`, **every field** carrying its own `source`, `method` and `confidence`. It works, and it is held on class rather than on quality: business enrichment by URL is carried by [Vibe Prospecting MCP](/hermes/mcp/servers/external/vibe-prospecting-mcp/) and [Leadbay MCP](/hermes/mcp/servers/external/leadbay-mcp/), and a single prepaid-credit tool at `$10 per 500 lookups` does not add a surface this catalogue lacks. Worth promoting if a wanted-by field ever needs a per-field confidence score.
- **Sumora** (#6617) - an approval-first B2B outreach agent over LinkedIn and Instagram, OAuth or bearer, self-described as "Shopify for AI agents"; sales and lead-generation class, carried by [Leadbay MCP](/hermes/mcp/servers/external/leadbay-mcp/) and the outreach cluster.
- **Evalmee** (#6602) - online exams and assessment authoring, OAuth with dynamic client registration; education authoring class.
- **Peerlytics** (#6599) - a read-only explorer for the Peer (ZKP2P) protocol on Base, two tools; consumer crypto analytics.
- **Binnacle** (#6605) - a local AI engineering control plane for coding agents, stdio only; developer tooling.
- **Narva** (#6611) - faceless YouTube and Shorts production in 32 languages; video generation class, saturated.
- **Raywake** (#6620) - 500 plus image, video and audio models with a USD quote before generation; media generation class, saturated.
- **Untitled UI** (#6606), **Dynobase** (#6607), **knock** (#6601), **Keep Mac Awake** (#6600), **memreduct-mcp** (#6597), **TweakThis** (#6594), **AttriKit** (#6592) - developer tooling, desktop utilities and mobile attribution.
- **Mono eSIM** (#6618), **Cyclesite** (#6604), **WebAZ** (#6587), **byondr Receipt Maker** (#6591), **Numbers2Excel** (#6614), **LetsBot** (#6595), **Perisclaw** (#6596) - travel, a used-bike marketplace, shopping-agent product discovery, a receipt generator, a file converter, and two WhatsApp surfaces in the saturated messaging class.
- **AlphaPrime** (#6619) - trading signals and market data; the stock and market slice is carried by Altair, ValuEdge, fAlpha and BDE plus nine EDGAR surfaces.
- **Faxend** (#6610 and #6613) and **Tempost** (#6608 and #6612) - the same two products submitted twice each inside a two-hour window, a resubmission pattern rather than four arrivals.
- **fixRAgent** (#6586) - catalogued at the October 14 midday pass, not a new arrival.
- **Chris Pereira agent desk** (#6585), **iMpact agent desk** (#6588), **Global Connect Show** (#6589) - single-vendor and single-person promotional desks.
- **Gang** (#6616), **Vibresia** (#6615), **Versum** (#6603, catalogued), **McpStamp Check** (#6593) - a consumer CLI, a music visualiser, the new entry, and a readiness scorer in the directory-and-benchmark class that `testedmcp-com` already occupies.

From `/all`, the unledgered slugs are `hologramxyz` (detail route answers a **404** shell, so the listing is real and the page is not published yet), `perisclaw-mcp` (the Perisclaw hold above) and `nova-civai-co-agent-product-admin` (the second surface of the single-vendor Nova fleet held at the night pass). Every other slug on the page resolved to an existing guide directory.

## Core Listing Verification

All five surfaces re-probed in this pass, since the night run recorded them as not run.

| Surface | Result |
| --- | --- |
| mcpservers.org `/servers/corpusiq-io` | **LIVE** - HTTP 200 through the reader proxy, title `CorpusIQ MCP Server \| Awesome MCP Servers`, 18 CorpusIQ mentions in the body |
| Smithery | **LIVE via the registry API** - `GET /servers/<publisher>/Cprusiq` returned 200 with a publisher-scoped `qualifiedName`, `displayName: CorpusIQ`, a deployment URL, tools and resources. The HTML page route 404s, and a control test on two unrelated published servers returned the same 404, because the web directory migrated to an Arcade-powered directory and every old `/server` route went with it - a recorded migration, not a delisting. The search endpoint returned HTTP 500 vendor-side on both attempts |
| Glama connector | **LIVE** - `/mcp/connectors/io.corpusiq/multi-source-mcp` HTTP 200, 2.7 MB body, and the connector is the first result on the connectors search for corpusiq |
| Glama repo listing | **LIVE** - `/mcp/servers/CorpusIQ/corpusiq-docs` HTTP 200 |
| Official MCP registry | **ACTIVE** - `io.corpusiq/multi-source-mcp` in the v0 servers feed with `remotes[0]` `streamable-http` at `https://mcp2.corpusiq.io/mcp`, status `active` |
| mcp.so | **NOT LISTED** - all four direct slugs (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) answer **404**; unchanged and expected, the free route is sign-in gated and the paid route was declined |

## Verification

- The guide was written against live responses, not the vendor page. Six tools were called: `list_niches`, `search_catalog`, `find_business`, `get_card`, `get_offering`, `quote_order`.
- Two argument-shape corrections were found by driving rather than reading: `get_card` and `get_offering` take `id`, while `quote_order` and `place_order` take `offering_id` and `business_id`, and a wrong field name returns `-32602` against a schema with `additionalProperties: false`.
- The counts in the guide are the server's answers on the day, not the submission issue's. The issue says **7,415** cards; `list_niches` said **5,398** cards over **9,300** businesses across the same **128** trades. The difference is recorded rather than reconciled away.
- The Smithery 404 was tested against a control set before it was written down: two unrelated published servers 404 the same way, so the site's page route moved and the listing did not disappear.

## Sources

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Versum MCP](/hermes/mcp/servers/external/versum-mcp/)
