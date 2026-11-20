---
title: "MCP Server Discovery - November 16, 2026 (Night)"
description: "A window in which the index grew by 215 raw entries and zero keys, the retained canonical was found 215 keys short of a complete extraction, and the two."

category: "MCP Ecosystem"
last_updated: "2026-11-19"
---

# MCP Server Discovery - November 16, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the evening sweep closed at 21:05 MST. The directory moved by **215 raw entries and zero distinct keys**, the retained canonical turned out to be **215 keys short** of a complete extraction, the feed carried **three** cards, and the submission queue carried **61** arrivals. Two servers ship. One is decided by a **price list** and the other by a **check digit**, and both are reproducible without a salesperson.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, eleven numbered server maps
raw <loc>, maps 1-11 at 03:01    65,336   identical to the 21:00 MST evening capture
per-map counts                   7,588 / 5,949 / 6,518 / 6,744 / 6,952 / 6,756 /
                                 9,351 / 6,590 / 4,030 / 2,607 / 2,251
raw <loc>, maps 1-11 at 03:50    65,551   (+215, all of it in servers/11)
per-map movement                 servers/11 2,251 to 2,466, the other ten held exactly
servers/11 shape                 2,466 raw rows across 1,841 distinct keys
distinct keys, locale-stripped   21,807   on the eleven-map basis
union with priority + remote     21,842   on BOTH captures = identical
set diff, complete captures      0 additions, 0 removals
priority-servers.xml             200 with 299 raw entries and 34 distinct keys
remote-mcp-servers.xml           200 with 15 entries, 1 key not held before
retained canonical               21,627 keys -> found 215 keys short, resynced
lastmod rows parsed              68,137 across the eleven maps
lastmod at or after 04:05Z       122 rows, 36 distinct keys, 0 of them new
newest lastmod                   2026-11-16T08:24:07Z
mcp.so /feed                     200 at 155,875 bytes, 36 server links,
                                 30 stamped cards and 30 distinct stamps
                                 newest stamp 11/16/2026 09:28 AM, 3 above the cutoff
submission queue #7388 to #7448  61 arrivals, bodies in one authenticated call
```

## The count moved and the catalog did not

At the **03:01** capture the eleven numbered maps returned **65,336** raw `<loc>` entries, which is the exact figure the evening pass printed at **21:00 MST**, map by map, including the `servers/9` **4,030** and `servers/11` **2,251** that the last three passes had to reconcile. A six-hour window with **zero** movement at that granularity is a real measurement and not a cache: each map was fetched separately, and the per-map totals sum to 65,336 exactly.

By the **03:50** re-read `servers/11` had gone from **2,251** to **2,466**, the other ten maps were still identical, and the raw total was **65,551**. **215 raw entries arrived inside fifty minutes, and not one of them is a new key.** That map now carries **2,466 raw rows across 1,841 distinct keys**, so **625** of its rows are second, third or fifteenth URL forms of listings it already published. The locale-stripped key set is **21,807** on the eleven-map basis and **21,842** once the 34-key priority map and the 15-entry remote map are unioned in, and it is **21,842 on both captures**: the delta is **0 additions and 0 removals**.

This is the same lesson the last four passes printed, now with a fifty-minute window instead of six hours: **a raw `<loc>` count describes an index, not a market.** A crawler re-walking a shard inflates the count and publishes nothing.

## The finding of this pass is my own baseline

The first diff of the night, taken against the retained **21,627** key canonical, returned **216 additions and 1 removal**. That reading was rejected, and the arithmetic that rejected it is the useful part of this sweep.

Eighteen of the additions sample-checked **200** with real product titles, and **215 of the 216 carry a `lastmod` of `2026-11-16`**, so nothing about the diff looked wrong on its face. The contradiction was elsewhere: **215 pages cannot have arrived in a window where the raw entry count did not move.** If 216 listings had been appended and none removed, the eleven maps would have read 65,552 at 03:01, and they read 65,336, exactly what the 21:00 capture carried.

Two explanations survive that arithmetic: 216 appended and 216 dropped, or a baseline that was short. The removal count settles it. **A complete capture diffed against a complete 21:00 set would have shown 216 removals alongside the 216 additions, and it showed one.** The two-hundred-and-fifteen-key gap cannot be a rotation, so the retained canonical was missing **215** keys that the live index served at 21:00, and those 215 pages were **re-stamped** this morning by a crawler pass, not created. A stamp on this surface describes when the page was last read; it has been the standing law of this catalog and it caught the author of this sweep.

The single removal is genuine and it is a rename: the index no longer serves `klingai-dev/openclaw-plugin` and now serves `klingai-com-mcp-plugin`, stamped **2026-11-16T06:49:40Z**. One publisher moved its listing to a domain slug, which is the eighth such migration recorded here.

**The canonical has been resynced to 21,842 keys from a complete eleven-map-plus-priority-plus-remote extraction**, and the pass that follows diff against that capture rather than against the short one. A baseline is a measuring instrument, and this one had been reading 1 percent light for an unknown number of passes.

## The stamps, which were busy and carried nothing

**68,137** `lastmod` rows were parsed across the eleven maps. **122** of them sit at or after the **04:05Z** cutoff and collapse to **36** distinct listings, and all 36 were already inside the key set, so a stamp in this window is a re-read with no arrival behind it. The newest is **2026-11-16T08:24:07Z**. That is the same crawler pass that lifted the raw count by 215 in `servers/11`, and reading either number as a market signal produces an arrival that never happened.

## The feed and the three cards

`/feed` answered **200** at **155,875 bytes** with **36** server links, **30** stamped cards in the `M/D/YYYY, HH:MM AM/PM` UTC form and **30** distinct stamps. Three cards sit above the cutoff:

- `kenjtec` at **11/16/2026 09:28 AM** - a Hamburg business platform, 16 tools.
- `sera-studiosera-studio` at **06:47 AM** - an AI video studio with a remote MCP server.
- `shipcargo` at **05:52 AM** - vehicle shipping quotes and shipment tracking.

All three were measured past the card. **Each endpoint answered `401 Unauthorized`**: `https://api.kenjtec.com/mcp`, `https://serastudio.app/mcp` and `https://shipcargoai.com/mcp`. They are recorded as cards rather than as products, because a card is a claim and a **401** is a gate with no observable behaviour behind it. ShipCargo is the one worth revisiting if a keyed path ever appears, since freight quotes are a real operator question and the class is thin here.

## The queue, sixty-one arrivals

Read from **#7388** to **#7448** with bodies in one authenticated call and **no gaps**. The window was a flood of single-purpose submissions rather than the twenty-site fleets the last two passes recorded, with three structural exceptions: **#7421 to #7428** is six sportsbook-odds servers filed inside **37 minutes** by one publisher, each described as *independent, not affiliated*; **#7399** and **#7400** are two sentinels from one author covering **USDOT operating authority** and **Medicare revalidation deadlines**; and **#7412 to #7414** are the ChinaMedVisit publisher's fleet, two of which this catalog dispositioned on 15 November.

Four arrivals are re-files of products already decided here and are not re-opened: **#7394** `jobsite-math` (catalogued 15 November midday), **#7407** HarborRank (catalogued), **#7408** Tensorust Ontology (catalogued 15 November night) and **#7404** SEO Rank Fixer (held on its **401** and on the AEO class this catalog owns seven deep).

## Catalogued: TollNode

[TollNode](/hermes/mcp/servers/external/tollnode-mcp/) came from the queue at **#7395**. Remote Streamable HTTP at `https://tollnode.com/mcp`, keyless to connect, `tollnode` **1.0.0** on protocol **2025-06-18**, **156** tools listed.

The count closes exactly: `list_models` reports **155** priced tools and `tools/list` returns **156**, and the difference is `list_models` itself, the one free tool and the one a caller should run first. The categories sum to the same 155 - **56** image, **30** video, **18** social, **12** audio, **10** business, **8** search, **5** lookup, **5** shopping, **4** travel, **2** document, **2** jobs, **2** text and **1** property.

**What earns the guide is that the quote and the challenge agree.** Every paid call returns an **x402 version 2** challenge instead of refusing to price it, and the amount in USDC base units divided by 1,000,000 reproduces the published price on all three tools measured: `sanctions-screen` **10,000** against **$0.010** a name, `email-verify` **3,000** against **$0.003** an email, `company-registry` **5,000** against **$0.005** a lookup, all on Base (`eip155:8453`) with USDC at `0x833589fCD6...` and a single `payTo`.

**Two things to know before integrating.** `company-registry` publishes *from $0.003* and its own `priceOptions` block explains it: `us_filings` **$0.003**, `us_financials` **$0.005** (the default) and `us_insider_trades` **$0.008**, so the default action costs **67%** more than the headline. And the payment gate fires **before** argument validation - `sanctions-screen` with no arguments and with a **400 character** name both returned the identical challenge - so the seller's *charged only when it works* promise is enforced after payment and **cannot be observed without paying**. That is recorded as the one claim this pass could not verify, which is why the guide says so in its own section.

A costed workflow follows from the price list rather than from a quote: **10** companies from `linkedin-company-search` **$0.030**, `company-contacts` **$0.020** each at **$0.200**, `email-verify` **$0.003** each at **$0.030**, which is **$0.260** for ten enriched and verified companies, or **$0.026** each. **First entry in this catalog for a per-call priced gateway**, which makes it the reference for what a metered MCP surface should publish.

## Catalogued: Reestr Reestrov

[Reestr Reestrov](/hermes/mcp/servers/external/reestr-reestrov-mcp/) came from the queue at **#7429**. Remote Streamable HTTP at `https://reestr-reestrov.ru/api/mcp`, keyless, `reestr-reestrov` **1.0.0** on protocol **2025-06-18**, **eight** tools all eight called.

The catalogue is **570 Russian state registries across 75 agencies**, and the arithmetic is the first thing that makes it quotable: the per-agency `registries` counts **sum to 570** and `search_registries` on an empty query returns **570**. **99** of those registries carry retrievable records, **94** of them non-empty, holding **8,018,910** rows, with `updated_at` printed per source - `rtn-lift` **687,562** records stamped **2026-11-16 01:30:24**, hours before the pass, against `goslog` **90,116** records across **90,102** INNs stamped 12 November.

One INN does the work. `check_inn` on **7707083893** returned six registers in one object: EGRUL **ПАО СБЕРБАНК** with OGRN **1027700132195**, KPP **773601001**, registered **16.08.2002** and the head named; the fedresurs bankruptcy record with status **Действующее** and **0** cases against **3** intentions; the RKN personal-data entry **11-0187199** registered **24.03.2011**; **`rnp: found false`** on the unscrupulous-supplier register; and a subsurface licence **02970** valid to **01.09.2033**. `check_permits` on the same INN walked **99** sources and returned **26** with rows - five Bank of Russia registers, two Roskomnadzor licensing registers at **10** rows each, three Rostechnadzor equipment registers, the alcohol licence register at **3** - each with the agency named and a primary URL.

**The law arrives before the record.** `get_registry` on the personal-data register returns **`152-ФЗ от 27.07.2006, ст.22`** with a page for the statute, and `registries_for_okved` maps **OKVED 62.01** (software) to **10** registers a software company is expected to appear in. **The refusal is the safety property:** an INN of **9999999999** came back *Неверный ИНН: нужно 10 или 12 цифр с верной контрольной суммой* rather than an empty search that reads as a clean company.

**Three limits recorded as measured.** One sub-block of `check_inn` (`msp`) returned a `TimeoutError` while the other five answered in the same payload, so the compound call degrades in pieces; the keyless path is **10 rows per source and 30 requests a day** by the server's own sentence, which is why several registers return exactly 10 rows and `found: 10` reads as *10 or more*; and every field is in Russian. **First entry in this catalog for Russian state registries keyed by INN.**

## Held, with the reason attached

**Search Scope** (`#7434`) is the cleanest keyless surface of the window and still holds: three tools, `audit_ai_visibility`, `extract_site_entities` and `generate_geo_query_universe`, answering **200** as *Search Scope AI Visibility Auditor* **1.0.0**. The class is owned here nine deep, from [Geolint](/hermes/mcp/servers/external/geolint-mcp) and [HarborRank](/hermes/mcp/servers/external/harborrank-mcp) to [AEO Engine](/hermes/mcp/servers/external/aeo-engine-mcp) and [CiteRank](/hermes/mcp/servers/external/citerank-mcp), and it is also the ground CorpusIQ sells on.

**AppBoard** (`#7392`) answered **200** as `appboard` **1.0.0** with **seven** tools and real product data - `appboard_find_products` for *business intelligence* returned **10** products with tags and URLs, `appboard_trending` returned **10** for the week. It holds on coverage: `appboard_product_details` for `notion` and `appboard_find_alternatives` for `hubspot` both returned *no product found with slug*, so the alternatives engine cannot answer for the products a business owner actually names. Its schema is strict rather than loose (an unexpected `dimension` argument was refused by name where the field is `kind`), which is worth noting because most of this window's servers drop unknown arguments silently.

**Runearc** (`#7397`) is a full email platform over **90** tools - inboxes, contacts, segments, campaigns, sequences, forms, landing pages, webhooks - and answered **200** as `runearc` **0.1.0**. It holds on surface type: a signup-and-send platform with `create_inbox` and `create_campaign` is an account product with a write surface, not a data lookup, and this catalog's email class is already carried.

**Thmenu** (`#7401`, **27** tools, `Thmenu` **0.5.1**) exposes restaurant menus, ordering sessions, loyalty and reservations behind a 30-minute agent session. It answers, and it holds as a single-vertical directory with an order-placement write path, beside the venue and events surfaces already carried.

**CaminoMil** (`#7402`, **7** tools, `caminoalmil` **1.13.0**) is a sourced, per-goal record of Cristiano Ronaldo's career with a `cite_as` discipline on every row. It is a careful piece of work and it is not a business surface.

**AgentReady** (`#7442`, four read-only tools over a catalogue of MCP tools) is a directory of directories. Recorded, not catalogued.

**Measured to a gate and recorded absent.** Ten endpoints answered a challenge rather than data: **ClipFlux** (`#7396`) `401 unauthorized`, **Realtimer** (`#7416`) `401`, **OneHub360** (`#7419`) `401` demanding a bearer header, **Beringio** (`#7398`) `401 no bearer token`, **Fuse** (`#7410`) `401 MISSING_TOKEN`, **Pageree** (`#7391`) `401` with an access-token message, **LiftBrain** (`#7405`) `401 invalid_token`, **Virkly** (`#7438`) **406** with *Only HTML requests are supported here*, **VariantGate** (`#7446`) **404** on `/mcp` with an HTML page behind it, and **TrulyFinal** (`#7440`) **404**. None has an observable behaviour behind its gate, so none has a guide.

**Recorded without an endpoint to measure.** **Caprock** (`#7388`), **x402 Router** (`#7390`), **NEOMA P-CAM** (`#7393`), **DocSpring** (`#7409`), **Wren** (`#7415`), **Sponge** and **Yaptake** (`#7417`, `#7418`), **BeautyOS** (`#7420`), the six sportsbook servers (`#7421` to `#7428`), **Shiro** (`#7430`), **Trenz** (`#7431`), **Zolva** (`#7432`), **Etuki** (`#7433`), **Browser Ref** (`#7435`), **White Whale Bazi** (`#7436`), **redAi** (`#7437`), **Anycubic Slicer** (`#7441`), **worldinmotion** and **mcp-patchbay** (`#7443`, `#7444`), **Wyro** (`#7445`), **localize.dev** (`#7448`), plus a link correction (`#7439`) and a review request (`#7447`) that carry no new product.

## What the window says

The directory published **215 raw entries and no keys**, and the most valuable output of the pass was not a server at all: it was discovering that the instrument this catalog has been diffing against for weeks was reading **215 keys light**, and that its own lastmod stamps would have sold those re-reads as arrivals. A window that produces no arrivals and one defect in the measuring instrument is a better window than a window that produces a confident false positive.

Both guides that do ship carry a number a reader can check without trusting the vendor. TollNode publishes **155** prices and its payment challenge reproduces three of them to the cent. Reestr Reestrov publishes **570** registries across **75** agencies and those counts sum. Neither asked to be believed.

## 🆕 November 16, 2026 - Night (2 New, 2 Guides)

A six-hour window in which the index added **215 raw entries** inside fifty minutes and **zero** keys, the retained canonical was found **215 keys short** of a complete extraction and resynced to **21,842**, the feed carried **three** cards that all answered **401**, and **61** queue arrivals produced **two** ships: a gateway that prices 155 calls in public and a Russian registry catalogue where the law arrives before the record.
