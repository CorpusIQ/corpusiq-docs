---
title: "MCP Server Discovery - November 28, 2026 (Midday)"
description: "A flat canonical proved by set identity, three feed cards, twenty-one filings and two driven guides: SEC deadlines and immigration case law."
category: "MCP Ecosystem"
last_updated: "2026-11-28"
---

# MCP Server Discovery - November 28, 2026 (Midday)

Fired on the **10:00 MST** tick **six hours** after the night capture, which had recorded the largest single arrival this surface has produced in three days. This pass found the directory **flat** and spent its evidence budget on the queue instead. Two servers were catalogued, both driven end to end before a line was written: a statutory deadline calculator whose arithmetic reproduces by hand, and the first US immigration surface on this shelf.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, 17 maps named, 15 server-bearing maps read
raw <loc>, all server maps    39,098   (night read 39,089, +9 duplicate forms)
  servers/1 ..... 4,067   distinct 1,987      servers/8 ..... 2,774   distinct 2,000
  servers/2 ..... 2,510   distinct 1,990      servers/9 ..... 2,574   distinct 2,000
  servers/3 ..... 2,949   distinct 1,994      servers/10 .... 2,577   distinct 2,000
  servers/4 ..... 3,173   distinct 1,999      servers/11 .... 2,523   distinct 2,000
  servers/5 ..... 3,341   distinct 1,996      servers/12 .... 2,407   distinct 2,000
  servers/6 ..... 2,843   distinct 2,000      servers/13 .... 1,211   distinct 1,067
  servers/7 ..... 5,889   distinct 2,000      priority .....   245   distinct 34
                                              remote .......    15   distinct 0
union of keyed slugs          25,067   (stored 04:30 baseline 25,067)
set diff                       0 added, 0 removed
lastmod rows, server maps     35,544   newest 2026-11-28T10:48:03Z
mcp.so /feed                  200, 158,029 bytes, 37 anchors, 30 stamps
mcp.so queue                  #8288-#8309, 21 filings, newest 16:59:13Z
```

**Flat is proved by set identity, not by a total.** The raw count rose by nine while every per-map distinct count held at its ceiling and `servers/13` read **1,067** against **1,068**; the keyed union set-diffed against the stored 04:30 capture to **zero additions and zero removals** across the same **25,067** keys, with both files carrying 25,067 lines. Nine raw rows without a key or a product is the duplicate-form shape this surface has produced before, and the per-map distinct count is the only measure that has held across all nine shapes.

**One slug left the directory inside the window.** `shortformkit-com-mcp-server` is present in the 03:00 capture, absent from the 04:30 sibling capture, and has **no trace in any of the thirteen fresh maps** on a raw-text grep - so it is recorded as a withdrawal rather than as a diff artefact. It carried no catalogue entry and no guide.

## Three feed cards, none shipped

The mcp.so feed answered **200** at **158,029** bytes with **37** card anchors and **30** stamps. The minute-resolution `title` attribute the night read found missing from every anchor is **back**, so cards were paired by document order:

- **`pdfcraft`** at **16:24Z** - `api.pdfcraft.ai/v1/mcp` answered **401** with `WWW-Authenticate: Bearer scope="pdfcraft:use", resource_metadata="https://api.pdfcraft.ai/.well-known/oauth-protected-resource/v1/mcp"`, an OAuth tier with a single scope, and the vendor's own pages describe PDF OCR and EPUB translation. **Held on the document-conversion class**, which this shelf already covers with PDF-to-Excel and PDF/CSV parsers.
- **`watchfor`** at **13:52Z** - already probed and held by the night pass on the monitoring class behind Cronitor, Runheed and uptrack, 20-plus tools.
- **`meridian-1770cf`** at **10:50Z** - `mcp.the-meridian.ai/mcp` answered **401** with the plainest possible body (`{"success":false,...,"code":"UNAUTHORIZED"}`) and no `WWW-Authenticate`. The vendor is **already catalogued** as the Meridian QuickBooks connector, so this is a second slug for a listed product, not an arrival.

## Twenty-one filings, two shipped

The queue carried **#8288** to **#8309** with **#8298** absent from the sequence, newest **16:59:13Z**.

- **[SEC Filing Deadlines MCP](/hermes/mcp/servers/external/sec-filing-deadlines-mcp/)** (#8301) - sixteen tools covering 10-K, 10-Q, 20-F, 11-K, 8-K and Forms 3, 4, 5, each answer citing the rule text, its URL and a SHA-256 of the copy read. Four calls: a stored free sample, two free-trial calls and two paid routes that returned their x402 challenge. The arithmetic reproduces by hand on every line, including a non-accelerated deadline that moves off Friday 24 December 2027 because the Christmas holiday is observed that day.
- **[Merito MCP](/hermes/mcp/servers/external/merito-mcp/)** (#8300) - the first US immigration surface here: four keyless searches over **6,501** classified AAO decisions, each record carrying per-criterion findings with reasons, plus a readiness scorer that returns the questions it needs instead of guessing an answer. Three defects recorded, led by a `criteriaTotal` that does not reconcile with the criteria the same record lists.

The rest are held with the class or the address named:

- **g-digital by Garrigues, third wave** (#8291 `ead-enterprise-suite` v2.1.1, #8293 `gocertius` v2.1.1, #8299 `ead-factory` v1.5.0) - the same publisher whose EAD Enterprise Suite and GoCertius filings were dispositioned on the November 27 and 28 passes, all three requiring `MCP_AUTH_USER_KEY` and a service token before any call.
- **mambalabsdev, seventh wave** (#8308 `mcp-tcgplayer-card-prices`, #8309 `mcp-podcast-ratings-chart-ranks`) - Apify actors behind `APIFY_TOKEN`, listing their tools without one, on the class already recorded across six previous waves.
- **`APIFor`** (#8302) - **401** with `resource_metadata` on `mcp.apifor.dev/mcp`, holidays, postal codes, airports and universities: an open-data reference class, and gated at the first call.
- **`JsonExport`** (#8290) - keyless and **driven**: `json_to_table` converted a three-record array with a nested object and an array into **3 rows x 10 columns**, dotted keys (`customer.name`), expanded array members (`lines.0.sku`) and a BOM-prefixed CSV. Held on the data-conversion class the PDF and CSV parsers already own, not on behaviour.
- **`ExpiryRegister`** (#8292) - already dispositioned: the November 27 night pass recorded it initializing into an in-band **401**, and the renewal-roster class has an owner in RenewRoster.
- **`HookKeep`** (#8295) - webhook inbox and replay; the webhook debugging class already has a catalogued entry.
- **The AI-visibility pair, `Shruwd`** (#8306) and the design-to-code trio **`CoDesignFlo`** (#8307), **`Penkit`** (#8305), **`Deframer`** (#8304) - both classes are saturated here, AI visibility behind geolint, LogNorm and Sway, design-to-code behind the Figma readers.
- **`CaptureBatch`** (#8297) screenshots, **`Merito`'s neighbour `AiGuild`** (#8303) Discord server building, **`Genesis x402 APIs`** (#8296) on the email-authentication, DNS and uptime classes, **`OfficeRoutines`** (#8294) on a local release install plus the Office document class, **`Another`** (#8289) as a localhost-only Android bridge, and **`Freeplay Launch`** (#8288) as a game-portal QA vertical.

## Listings, re-measured

| Surface | Result |
| --- | --- |
| mcpservers.org `/servers/corpusiq-io` | **403**, Cloudflare interstitial - the standing edge policy toward this network, not a delisting; both slugs are present in the fresh canonical capture |
| mcp.so `/servers/corpusiq-docs` | **200**, 856,882 bytes |
| Glama `/mcp/connectors/io.corpusiq/multi-source-mcp` | **200**, 732,171 bytes |
| Official registry `io.corpusiq/multi-source-mcp` | four records **1.0.0** to **1.0.3**, every one carrying the `https://mcp2.corpusiq.io/mcp` remote |
| Anthropic connectors directory watch | **1,227** pages scanned, **zero** matches, exit **0** - unchanged, submission still in review |

## Counts

- Canonical: **39,098** raw against 39,089, per-map distinct held, union **25,067** against 25,067, **0 additions and 0 removals**, one withdrawal inside the window.
- Feed: **37** anchors, **30** stamps, **3** cards above the night set, **0** shipped from the feed.
- Queue: **21** filings, **2** catalogued with guides, **19** held with the class or gate named.
- Endpoint probes: **7** servers touched (16 tools listed on the deadline service, 15 on Merito, 1 on JsonExport, 401 on pdfcraft, APIFor and Meridian), **4** tools driven to a result, **2** paid routes measured at 0.005 USDC without paying.
- Listings: **5** surfaces measured, **1** edge refusal named as policy.
