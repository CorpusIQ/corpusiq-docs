---
title: "MCP Server Discovery - November 23, 2026 (Night)"
description: "A 204-slug wave, twenty-seven queue arrivals and four products: receipts on a rate card, a climate match, Korean totals and sealed data streams."
category: "MCP Ecosystem"
last_updated: "2026-11-23"
---

# MCP Server Discovery - November 23, 2026 (Night)

Fired on the **03:00 MST** tick, **5.6 hours** after the evening pass closed its baseline at **04:24Z**. The directory moved by a wave rather than a trickle: **204** new slugs against **0** removals, with one map carrying most of it. The queue carried **twenty-seven** arrivals and the feed **four** cards. Four products shipped, and each one prices something an operator otherwise guesses at: a tax rate on a date, a climate match between two towns, a delivered total in won, and a data stream's own inventory record.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          37,555   against 37,243 at the evening capture  (+312)
  servers/1  ..... 4,149     servers/7  ..... 5,858
  servers/2  ..... 2,520     servers/8  ..... 2,734
  servers/3  ..... 2,965     servers/9  ..... 2,614
  servers/4  ..... 3,226     servers/10 ..... 2,619
  servers/5  ..... 3,335     servers/11 ..... 2,535
  servers/6  ..... 2,939     servers/12 ..... 2,061     sum 37,555 exact
distinct keys, maps 1-12      23,610   at 1.59 URLs per key
priority-servers.xml          248 raw, 248 distinct keys
remote-mcp-servers.xml         15 raw, 15 distinct keys
union raw                     37,818   against 37,512 on the 04:24Z baseline  (+306)
distinct keys, union          23,659   against 23,455 at 1.60 URLs per key
union diff                    +204 additions, 0 removals
lastmod, server maps          35,292 stamped pairs; 70 rows at or after 04:24Z, 45 keys
mcp.so /feed                  200, 158,794 bytes, 34 anchors, 30 stamps, 4 cards above the cutoff
submission queue              #7859 to #7885, twenty-seven arrivals with bodies
```

The rise is concentrated: `servers/12` added **224** raw entries, `servers/5` **30**, `servers/4` **25** and `servers/1` **21**, against a fall of **40** in `servers/7` and **8** in `servers/11`. That is not a re-shard of locale forms, because the key set grew by almost exactly the number of additions: **+204** keys on a **+306** raw rise, with the per-key ratio holding at 1.60.

The like-for-like basis matters here and is worth stating. The stored baseline is a **union** capture, so a twelve-map capture diffed against it invents **248** priority and **15** remote removals that are not removals. On the union basis there are **0** removals and the diff is a clean arrival count.

The `lastmod` evidence agrees with the set arithmetic from the other direction. **70** rows carry a stamp at or after the cutoff, running from **04:24:03Z** to **07:04:41Z**, and they collapse to **45** keys because two slugs are stamped many times inside the window: `local-falcon-mcp` **15** times and `jitsucom/jitsu` **12**. Of the 45, **42** were already in the baseline and **3** are new arrivals (`guuskeunen/sprint-review`, `irrigator-dev`, `grainulator-dev`). Our own mirror `/servers/corpusiq/corpusiq-docs` is stamped **05:27:14Z**, so the mcpservers.org listing of this docs repository refreshed inside this window.

## What the 204 additions actually are

A wave this size needs decomposing before it becomes a product count:

- **12 Apify actor slugs** (`apify-com-cliqtomedia-*`, `apify-com-monkey-d-scraping-*`, `apify-com-dedicatedcrest-*`), the standing hold class on Apify transport.
- **67 documentation or marketing mirrors** - slugs ending in `-docs`, `-help`, `llms-txt`, `for-agents`, `-developers`, `-assistants`, `well-known` or `mcp-connect`. These are agent-facing pages for products, not new products.
- **51 namespaced repository slugs** (`owner/repo`), including five `abigaildavised/*` China consumer verticals whose product pages were dispositioned on 2026-11-22 night and are re-entering under namespace slugs, and a five-item `sino*` family (`sinoagritech`, `sinoailab`, `sinobiodata`, `sinogreentech`, `sinotechintel`) all pointing at one `mcp-connect` template.
- **74 plain product slugs**, where the shippable material sits. Four were reached and shipped; the rest are recorded as not reached rather than dispositioned, because a 204-slug wave read in one pass produces guesses, not evidence.

Named from the wave for the next pass, not catalogued here: `cheap-gpus-com-mcp` on the FinOps class already carried by OpenCloudCosts, Costory, Infrawise, GPUFinder and CoreHu; `contextbolt-com-seo` on the SEO and AI-visibility class this catalogue publishes; `llmdocs-dev` on docs retrieval; `invohub-app-connect-quickbooks` as an accounting connector; and the `domainvet`, `linkvet`, `utilvet` and `livedproof` quartet, which look like one author's `*-pages-dev` fleet.

## Shipped (4, all driven)

- [Avanciq MCP - VAT Rates and Invoice Checks With Receipts](/hermes/mcp/servers/external/avanciq-mcp/) - a feed card at **09:53Z**, age **seven minutes** at the read. Six tools, no auth: a VAT rate on a date with the authority feed and its read date, official code tables for Brazil, Mexico and Poland, EN 16931 validation artefacts, and nine kinds of exact arithmetic. A German rate came back **19.0** standard and **7.0** reduced with `source_read` **2026-11-12** and a receipt id; an invoice claimed at **119.90** was called `incorrect` against **119.99** with a **-0.09** difference, reproduced by hand (3 x 33.33 = 99.99, 20 percent = 19.998, half-up = 20.00); and **250,000** at **4.49** percent over **365** days returned `correct` at **11,225** interest. It publishes its own metering and coverage: **71** jurisdictions served, **30** not covered, and `einvoice_rule` free.
- [Climatch MCP - A Climate Match for Any City You Pick](/hermes/mcp/servers/external/climatch-mcp/) - submission **#7870** plus a canonical sitemap arrival at `/servers/climatch-co-agents`. Nine keyless tools over 31,000 towns on TerraClimate 1991-2020. Lisbon returns August at **28.3 C** and **680 mm** a year with May, June and September as its best months; Austin against Medellin scores a **6** match with **869 mm** against **2,482 mm** of rain, and both annual figures reproduce as the exact sum of the twelve monthly values; London adjusted `["warmer"]` returns Saint-Nazaire and Nantes at **87**; Napa returns hardiness zone **9b**, **293** frost-free days and wine grapes at **100** rainfed. One advertised tool is dead: `weather_for_the_money` answers *"Cost-of-living data isn't loaded on this server."*
- [Moa MCP - Korean Prices Compared With Shipping](/hermes/mcp/servers/external/moa-mcp/) - submission **#7872**, twelve keyless tools over a Korean marketplace. `search_products("텀블러")` returns **16,677** matches and ten with price, shipping and total side by side, where a 7,100 won tumbler carries a 3,000 won delivery and a 4,500 won tumbler ships free; the response flags **3** stale prices and offers a `cursor`. `answer_link` returns one comparison URL across **three** domestic and **two** overseas sellers. The defect is worth the entry: the cheapest "wireless earbuds under 30,000 won" was a **1,700 won earbud cleaning brush**, so the delivered-total logic is right and the relevance is not.
- [STRATA MCP - Sealed Data Streams Priced Per Call](/hermes/mcp/servers/external/strata-trashpan-mcp/) - a feed card at **06:01Z**, **118** tools over sixteen streams from andQ Inc. in Japan. The free floor is an inventory probe, and it answered with a record that a buyer can decide on: `recordExists: true`, `checkCount 6`, `changeCount 3`, `firstSeenAt` **2026-11-07**, `lastCheckedAt` **2026-11-23T05:02:42Z**, a record hash and a Rekor seal batch dated **2026-11-23**. The paid floor refuses cleanly at **0.006 USDC** per call over x402, with an Apify pay-per-event and an API key as the two alternatives. First x402 data marketplace in this catalogue.

## Also identified this pass (not catalogued)

**Queue, twenty-seven arrivals (#7859 to #7885).** Held with the gate or the class named: the **HenryCrawl** ten (#7860 to #7869), every one an Apify-actor endpoint on the standing transport ruling; the **mambalabsdev** five (#7873 to #7877) on the standing fleet ruling; **Zero-Proxy MCP Suite** (#7884) as six Apify Standby endpoints behind one bearer key, the same aggregator class; **Flowmingo** (#7885), measured at **401** with `Missing credential` and a bearer challenge; **Conqueror** (#7882), measured at **401 invalid_token** with a protected-resource document, held as an SEO toolset on a class this catalogue already publishes; **past.dev** (#7880), whose account server answers **401** with a protected-resource document while its documentation server answers **200** keyless with three tools, held on the memory class; **Reddit MCP** (#7879) on the social-data class behind paid tiers; **Nanobananana** (#7881) on media generation; **geolith** (#7859), measured at **401 `missing_api_key`**, on the geocoding class; **Phation** (#7883) as a local npm stdio package; and **Browsa** (#7871) as local stdio in front of a paid cloud browser, on the saturated browser-automation class. **OpenSubtitles** (#7878) was measured keyless and healthy (**200**, seven tools, `opensubtitles 2.0.3`) and held on the media and transcript class rather than refused on access.

**Feed, four cards above the cutoff.** **Avanciq** shipped. **STRATA** shipped. **pagesmith-ai** (08:58Z) answered **404 `page not found`** at `/mcp` and **401** at the bare host with a protected-resource document and the scopes `read write deploy`, so the product exists as an OAuth-gated deployment tool and was not reached further. **memory-fit** (06:22Z) answered **401** with a protected-resource document in front of **107** tools over training, sleep and recovery data read from Garmin, Wahoo, COROS, Polar and Apple Health, held on the health-data class.

**Sitemap arrivals named and not catalogued.** `guuskeunen/sprint-review`, `irrigator-dev` and `grainulator-dev` are the three keys that entered inside the stamp window, all three small utilities with no readable surface at the sitemap level.

### Why did a 204-slug wave still produce zero removals?

Because the directory added rather than replaced. The union key set rose by **204** while the raw entry count rose by **306**, so the new keys arrived with their own locale forms instead of borrowing entry slots from existing rows. A composition change would show a flat or falling key set with a stable raw count, which is the pattern the 2026-11-12 evening pass recorded.

### Why ship only four of 204?

Because a slug is not a product. Two thirds of the wave is documentation mirrors, Apify actors and namespaced duplicates of products already dispositioned. The four that shipped were the ones with a live readable surface and a number an operator can act on.

### What did the night pass not do?

It did not re-read `/all`, which has answered **403** by edge policy since 4 November, and it did not disposition the 70 product slugs it named as not reached. Both are stated rather than implied: the wave is larger than one pass, and the next pass owns the remainder.
