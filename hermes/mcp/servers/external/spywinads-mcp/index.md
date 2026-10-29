---
title: "SpyWinAds MCP - How Old a Video Ad Really Is"
description: "Meta ad intelligence from the public Ad Library: a video ad's true age, every store running the same creative, and a Shopify export."
category: Marketing
stars: ★★★ (keyless 200 verified, 5 tools listed live)
added: 2026-10-29
source: "live probe of https://spywinads.com/mcp: initialize returned HTTP 200 advertising protocol versions 2026-07-28 through 2025-03-26 with a tools capability, and tools/list returned five tools with their descriptions"
relevance: ★★★
tags: [ads, meta-ads, competitive-intelligence, creative-research, ecommerce, shopify, keyless, remote-mcp]
last_updated: "2026-10-29"
---

# SpyWinAds MCP

**A winning video ad is the cheapest market research a store can get, and the hardest thing to verify. The date on the ad library card is not the date the ad started, and the store running it is rarely the store that made it.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://spywinads.com/mcp
Auth:        none on the probe, keyless tools/list returned 200
Protocols:   2026-07-28, 2025-11-25, 2025-06-18, 2025-03-26
Tools:       5, verified live
Data source: Meta's public Ad Library
```

## Why This Matters for Operators

Two questions decide whether a piece of creative is worth copying. How long has it been running, and how many stores are running it. A video that has been live for eleven months has passed the market's own test. A video that appears in forty stores at once is either a licensed template or a clone, and both facts change what you should do with it.

The five tools answer exactly those questions and little else.

```
spywin_lookup_video_ad         one video: its real age and reuse picture
spywin_spy_store_ads           everything a domain is running right now
spywin_get_page_ads            everything a Facebook page is running
spywin_get_video_reuse_research  the stores sharing one video
spywin_export_shopify_product  the product behind an ad, as a store record
```

The last tool is the one that closes the loop. Most ad research ends with a screenshot and a note. This one returns the product in a shape a store operator can act on, which turns a research session into a sourcing decision.

The store question is usually asked the wrong way round. Operators ask which ads are winning, when the better question is which stores are running the same winning ad and how their pricing differs. `spywin_get_video_reuse_research` is built for that second question.

## What Was Verified

`initialize` on `https://spywinads.com/mcp` returned **HTTP 200** with a JSON-RPC result listing `supportedVersions` from `2026-07-28` down to `2025-03-26` and a `tools` capability. `tools/list` returned five tools by name: `spywin_lookup_video_ad`, `spywin_spy_store_ads`, `spywin_get_page_ads`, `spywin_export_shopify_product`, and `spywin_get_video_reuse_research`.

Both calls succeeded without a credential, so this is a keyless surface in this pass and the tool list is observed rather than claimed.

The data provenance is stated on the vendor's own site: Meta's public Ad Library, with an explicit disclaimer that SpyWinAds is not affiliated with or endorsed by Meta.

## Limits Worth Recording

The vendor's `/docs` path returns 404, so the tool descriptions are the only published reference found this pass. Rate limits, quotas and any paid ceiling are not documented on a reachable page.

Every figure is a reading of the Ad Library at a moment in time, and the library itself is not complete. Ads that never ran publicly, and spend figures, are not in it.

The audience is e-commerce, dropshipping, print on demand, brands and agencies, and the surface reflects that. There is no general business intelligence here beyond the ad record.

## FAQ

### Do I need an account or API key?

Not for the calls made this pass. `initialize` and `tools/list` both answered 200 without a credential.

### Where does the data come from?

Meta's public Ad Library, as stated on the vendor's site, with an explicit non-affiliation notice.

### Can it tell me what a competitor spends?

No. Spend is not in the public library and no tool here claims it. Age, reuse and the stores involved are the measurable facts.

## See Also

- [Marketing servers in this catalogue](/hermes/mcp/servers/external/)
- [Connecting CorpusIQ to your own data sources](/hermes/mcp/)
