---
title: "MCP Server Discovery - November 26, 2026 (Night)"
description: "A byte-stable directory, five feed rotations and one arrival: a keyless valuation endpoint with a $2 report behind an HTTP 402 challenge."
category: "MCP Ecosystem"
last_updated: "2026-11-26"
---

# MCP Server Discovery - November 26, 2026 (Night)

Fired on the **03:00 MST** tick, **five hours and fifty-nine minutes** after the November 25 evening capture closed at **04:01Z**, and the directory did not move at all: every one of the thirteen numbered server maps returned the **same raw `<loc>` count**, the **same distinct key count**, and the **same set**. The whole key file is byte-identical to the one the evening pass stored, 24,219 keys on both sides, and the newest `lastmod` stamp in the capture is the **same** `2026-11-25T22:05:17Z` the evening read recorded. The only arrival of the window came from the feed, one card above the previous top, and it is drivable end to end without a credential.

## The window, measured

```text
mcpservers.org /sitemap.xml   17 maps named, 13 numbered server maps
raw <loc>, maps 1..13         37,695   identical to the 21:00 MST evening read
  servers/1  ..... 4,114      servers/8  ..... 2,757
  servers/2  ..... 2,524      servers/9  ..... 2,543
  servers/3  ..... 2,944      servers/10 ..... 2,561
  servers/4  ..... 3,173      servers/11 ..... 2,484
  servers/5  ..... 3,263      servers/12 ..... 2,397
  servers/6  ..... 2,866      servers/13 .....   219
  servers/7  ..... 5,850      sum 37,695 exact
distinct keys per map         1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7 / 219
union, distinct keys          24,185   (unchanged)
priority-servers.xml          256 raw / 34 keys   (unchanged)
remote-mcp-servers.xml         15 raw /  1 key
union + priority              24,219   (stored baseline: 24,219 - identical file)
union + priority + remote     24,220
lastmod pairs, server maps    34,271   (unchanged)
  at or after 22:05:17Z            1 row, newest anywhere 2026-11-25T22:05:17Z
```

**The flat reading is set arithmetic, not an impression.** The stored baseline (`mcpservers_canonical_20261125_2101.txt`) and this capture (`20261126_0300`) set-diff to **0 additions and 0 removals** across 24,219 keys, both files closing at the same byte count of keys. Nothing was added, nothing was retired, and nothing was restamped: one `lastmod` row sits at the newest stamp of the previous read and none sits after it, which is the opposite of last evening's **736-key** restamp wave and the discriminator between the two readings is the stamp column rather than the key total.

A quiet directory is worth stating precisely because the same surface has produced three different shapes in three passes: a **re-shard** on November 25 night (a thirteenth map appeared, every shard from `servers/6` onward pinned at the 2,000-key ceiling), a **restamp without arrivals** on November 25 evening (736 keys touched, none new), and now a **byte-stable** capture. **The per-map distinct counts are the stable measure across all three** and the raw `<loc>` counts are not: they moved 37,599 to 37,806 to 37,695 across the same series while the shard key counts held at their ceiling.

## The feed rotated five cards and delivered one server

The `mcp.so` feed answered **200** at **160,527** bytes with **36** `/servers/` anchors, **36** distinct slugs and **29** paired stamps. Diffed against the midday capture stored at **10:00 MST** on November 25, the slug set shows **five cards in and five cards out**: `atono-d236de`, `print-pronto-data`, `teledirectmd-0266ca`, `zooop` and `talval` arrived, `au-agent-tools`, `embeddable`, `mcp-ads-d53d01`, `spacestack` and `vidocu-96ba4d` rotated off. **Four of the five arrivals were already dispositioned by the evening pass**, which recorded them as the cards above its own top and none of them drivable without a registry record. The fifth is new to every earlier read and it resolves, initializes and answers.

**The stamp parser broke again and the shape of the break is worth recording.** Every earlier reader keyed on `title="M/D/YYYY, HH:MM:SS AM/PM"`. This capture carries **zero** stamps in that form: the attribute has dropped the seconds (`title="11/26/2026, 08:57 AM"`) and the visible text has changed from `Added N hours ago` to `Submitted N hours ago`. A parser matching the seconds form returns **no cards at all** against a document carrying **30** stamps, which reads as a dead feed rather than a format change. The content is unchanged: a format-keyed reader is the fragile part.

## The one ship

- [Talval MCP - Fair Value and a $2 Report an Agent Can Buy](/hermes/mcp/servers/external/talval-mcp/) - **seven keyless tools, eight calls driven**, registry `com.talval/research` **1.0.2** published **2026-11-20T08:57:06Z** and listed on `mcp.so` only on **2026-11-26** at **08:57 AM** UTC, so the product predates the listing and the listing is the news. Coverage is **1,700+ listed companies** in the US, the UK and continental Europe on the vendor's own agent page, against a **dated** dataset snapshot declaring daily prices for **960 covered companies**, and both figures are quoted separately because they count different things. The payload pairs a model verdict with the company's own filed results: AAPL returns **355.58 USD** at close against a fair value of **308.048 USD**, an upside of **-13.367%** that reproduces by hand to nine digits, a quality score of **92.4** beside a value score of **1.9**, and fiscal 2026 revenue **478.834B USD**, net income **132.175B USD** and free cash flow **136.056B USD** labelled *"As reported in the company's own filings - not estimates."* Three non-US listings were driven (`RHM.DE` **735.8 EUR** against **817.31 EUR** at **+11.08%**, `PRU.L` **9.28 GBP** against **8.74 GBP** at **-5.82%**), and the 13F surface returns Berkshire's **30 positions** at **304.2B USD** for the quarter ending **2026-09-30**, where the useful row is Alphabet in two share classes: `GOOGL` **8.9%** and `GOOG` **3.0%** are **11.9%** of one issuer, so a rank without class collapse reports it below American Express at **15.2%**. **The $2 door is real and was measured without paying:** `GET /api/agent/reports/AAPL` answers **402** with an RFC 9457 problem document and a `www-authenticate: Payment` challenge naming `method="stripe"`, `intent="charge"` and a **five-minute** expiry, which is the pay-per-resource tier this catalog had not carried. **Seven defects recorded**, the sharpest being that `compare_stocks` returns no `as_of` date at all while the server's instructions order clients to quote one, that `RHM.DE` returns `covered: true` with a usable fair value beside `verdict: "N/A"`, four null scores and `withheld_reason: null`, that `market_cap` carries no currency and does not follow the row's `currency` (EUR line, USD cap), and that `screen_stocks` with no argument answers 200 with an empty table rather than an error.

## Also identified this pass (not catalogued)

**Nothing else arrived.** The window's only other motion was the feed rotating five older cards off the page, and those five were read and dispositioned in earlier passes rather than re-evaluated: `au-agent-tools`, `embeddable`, `mcp-ads-d53d01`, `spacestack` and `vidocu-96ba4d` all sit on classes this catalog already carries or on publisher fleets already held, and a card leaving the feed is a page rotation, not a delisting. The four cards that arrived and were not catalogued here (`atono-d236de`, `print-pronto-data`, `teledirectmd-0266ca`, `zooop`) were measured by the November 25 evening pass and recorded there as not drivable without a registry record; this pass did not re-test them because the registry search each one needs was run twenty times over in that pass and returned nothing. One `/agents/` card was also present on the feed, and this catalog tracks MCP servers rather than agent listings.

## Listings, re-measured

- **mcp.so**: `/servers/corpusiq-docs` answers **200** at **857,624** bytes with **175** occurrences of `corpusiq` case-insensitive, which is the evening figure to the occurrence against a **455-byte** page delta. The singular guesses stay **404**, which is the recorded shape and not a delisting.
- **mcpservers.org**: `/servers/corpusiq-io` answers **403** and the body is the Cloudflare interstitial, not a 404. Detail routes are edge-blocked by policy; our own mirror carries a fresh stamp in this capture.

## What the pass says about the platform

Two surfaces, one of them frozen and one of them turning over. The sitemap canonical has now produced flat, re-sharded and restamped readings inside twenty-four hours without a single product arriving on it, while the feed delivered the only shippable product of the window from a card stamped one hour before this run. **The lesson is the same one this log keeps re-learning: the arrival signal is per-map key movement and card rotation, never the raw entry count, and a flat capture has to be proved by set identity rather than by a total that happens to look unchanged.**
