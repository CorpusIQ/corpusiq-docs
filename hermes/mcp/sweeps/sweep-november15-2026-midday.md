---
title: "MCP Server Discovery - November 15, 2026 (Midday)"
description: "A directory flat to the byte for three hours, four feed cards, fifteen queue arrivals, and one ship decided by markup against margin."
category: "MCP Ecosystem"
last_updated: "2026-11-15"
---

# MCP Server Discovery - November 15, 2026 (Midday)

Fired on the **10:00 MST** tick, seven hours after the night sweep closed at 03:55 MST. The directory came back **byte-identical** to a capture taken three hours earlier, the feed carried **four** cards, the submission queue carried **fifteen** arrivals, and **one** server ships: eleven construction calculators whose value is arithmetic a contractor can check by hand.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, thirteen maps named, eleven of them server maps
raw <loc> entries, maps 1-11     65,333   against 65,045 at the 10:02Z night capture (+288)
per-map counts                   7,588 / 5,949 / 6,518 / 6,744 / 6,952 / 6,756 /
                                 9,351 / 6,590 / 4,030 / 2,607 / 2,248
per-map movement                 servers/11 1,960 to 2,248, the other ten held exactly
byte identity                    11 of 11 maps identical to the 14:01Z capture on disk
servers/11 composition           2,248 raw entries, 1,627 distinct keys,
                                 45 keys repeated, 621 surplus entries (one slug 15 times)
distinct keys, locale-stripped   21,593   against 21,593 = identical
priority-servers.xml             200 with 299 raw entries and 34 distinct keys
lastmod at or after 10:02Z       zero rows
newest lastmod                   2026-11-15T08:30:32Z (trycua/cua), before the cutoff
mcp.so /feed                     200 at 156,316 bytes, 36 anchors, 30 stamped cards
                                 four above the cutoff: webhooky 10:02Z, luvvoice 10:05Z,
                                 osmo-phone-calls 10:39Z, snewpapers-reearch 13:48Z
submission queue #7388 to #7402  15 arrivals, no gaps
```

## The directory grew by duplication, not by products

The raw count in `servers/11` rose by **288** inside the window and the map has been byte-stable since **14:01Z**, which is two facts that only reconcile one way. That file now carries **2,248** `<loc>` entries across **1,627** distinct keys: **45** keys are repeated, contributing **621** surplus entries, and the repeat count is not a rounding artifact. `simvito-esim-mcp`, `simplyboost-mcp`, `picardo-mcp`, `anymail-finder-mcp`, `bot-appetit-mcp`, `wegravel/mcp`, `uncanny-automator-mcp`, `brandlio-mcp`, `tieline-mcp`, `telerivet-mcp` and `truedialog-mcp` each appear **15** times in the same file.

Three proofs agree that no product arrived: every one of the eleven maps is **byte-identical** to the 14:01Z capture, the distinct key set reads **21,593** on both, and **zero** `lastmod` rows carry a stamp at or after the 10:02Z cutoff. A re-served duplicate does not get a new stamp. The count moved; the catalog did not.

`priority-servers.xml` answered **200** with **299** raw entries at `/sitemaps/priority-servers.xml`, which the index no longer names. `/all` was not re-read: it has answered **403** direct since 4 November, and page-1 membership is therefore absent from this pass rather than asserted.

## The feed and the queue

Four cards above the cutoff, counted as slug sets rather than as stamp counts, because one product can be stamped twice in a window. `webhooky` is an npm stdio push-notification tool at registry `io.github.MatthiasMAigner/webhooky-mcp` **1.0.5**, no account, one environment variable. `luvvoice` is `io.github.franzsy5/luvvoice-mcp` **1.0.2**, text to speech over 200 voices that needs a vendor API token, which puts it in the media-generation class this catalog already carries several times over. `osmo-phone-calls` publishes `https://api.getosmo.app/mcp` and has no registry record under that name. `snewpapers-reearch` has no registry record either and its detail page carries no endpoint.

The queue ran **#7388** to **#7402** with no gaps. The arrivals worth naming: **Thmenu** (27 tools, restaurant platform), **Beringio** (a shared team hub over OAuth 2.1 with PKCE), **Runearc** (email inboxes for agents), **ClipFlux** (faceless video, 32 tools), **TollNode**, **jobsite-math**, **Pageree**, **AppBoard.pro**, **Camino al Mil** and the two Marcoco27 sentinels.

## Catalogued: Jobsite Math

[jobsite-math-mcp](/hermes/mcp/servers/external/jobsite-math-mcp/) came from the queue at **#7394**, filed 14:30Z. It is a local stdio server installed from npm, MIT licensed, with **eleven** US construction calculators and no network calls. It was installed and driven: `initialize` answered as `jobsite-math` **0.1.0** on protocol **2025-06-18**, `tools/list` returned eleven schemas, and **eighteen** `tools/call` requests were run.

The finding is the markup and margin pair. Cost 1,000 at 20 percent markup returned a price of **1,200**, a profit of **200** and a margin of **16.667** percent; the same cost at 20 percent margin returned **1,250**, **250** and a markup of **25** percent. `mode` is a required argument, so a caller cannot leave the ambiguity in place, and both figures come back together. The hourly rate tool divides by the margin rather than adding it: pay plus overhead plus reserve of 122,000 against a 10 percent margin returned revenue of **135,555.56** and a rate of **117.87** an hour over 1,150 billable hours, where adding 10 percent would have produced about 105 an hour and buried the margin.

Every other figure was reproduced independently: 33.333 cubic feet on a 10 by 10 slab at four inches and 1.2346 cubic yards; 12.566 cubic feet in a 24 inch column; 5.498 cubic feet in a 24 inch tube with an 18 inch core; 7,000 pounds and 3.5 tons of gravel at 105 pounds per cubic foot; 960 bricks on a 20 by 8 wall after 20 square feet of openings, against a brick-plus-joint footprint that gives 6.857 per square foot; 39 mortar bags from 38.4; 472 square feet, 2.697 gallons and 3 whole gallons for a 12 by 10 room; 15 drywall sheets from 14.75; 26 deck rows at 5.625 inches of board plus gap; and a hip roof whose ridge of 16 feet, plate-to-ridge of 6 feet and hip rafter of 19.5 feet each follow from the geometry of a 40 by 24 building at 6-in-12.

Two argument rejections were recorded honestly as my errors rather than as defects: `heightFt` on a round column and `bulkDensityLbPerCuFt` on gravel were both refused by name, with the schema printing `heightIn` and `densityLbPerCuFt`. **First entry in this catalog for the US construction trades**: roof pitch, drywall, deck boards, board feet and construction estimating all returned **zero** across the 1,324 guide files.

## Held, with the reason named

- **Thmenu** (#7401) is the closest call of the pass and it is held on substance, not on quality. Twenty-seven tools, keyless for the public surface, with a genuinely instructive design: 30-minute agent order sessions, one-time confirmation links for anonymous carts, and owner-side writes that land as **DRAFT** change sets rather than live edits. But its public directory carries exactly **one** opted-in venue (`baykara-firin-kafe`, TR) and the owner half of the 27 tools needs an account this host does not hold, so a guide today would describe a schema rather than an experience. Queued for a driven pass once the directory has venues in it.
- **TollNode** (#7395) is not a toll dataset despite its name. Its own `initialize` instructions describe AI models and live data priced per call in USDC on Base, so it is the x402 pay-per-call aggregator class already carried by `toll402`, `sendcheck` and `SiteCheck`.
- **Beringio** (#7398) and **Runearc** (#7397) need an account or a bearer key and open no keyless surface, so they are queued rather than dismissed.
- **ClipFlux** (#7396) is the faceless-video class this catalog already carries at length, on OAuth.
- **Revalidation Deadline Sentinel** (#7400) and **Operating Authority Sentinel** (#7399) are the Marcoco27 fleet, held the way the earlier waves of that publisher were held: a named owner per class, and the freight-compliance pair already covered by the catalogued carrier-compliance server.
- **Camino al Mil** (#7402) is a football statistics surface in Spanish: a hobby vertical.
- **webhooky**, **luvvoice**, **osmo-phone-calls** and **snewpapers-reearch** from the feed: a push notifier, text to speech, a phone-call agent, and a news research surface with no endpoint published. Each is class-covered or absent an access path.
- **AppBoard.pro**, **Pageree**, **Thmenu**'s landing-page and menu neighbours, and **NEOMA P-CAM** are recorded as class-covered utilities.

## Core listing, re-measured

Not inherited. **mcpservers.org LISTED**, proved from the platform's own index rather than from a detail page: the fresh capture carries `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`. The detail page answers **403** by edge policy, the standing condition. **mcp.so LISTED** at `/server/corpusiq-docs`, **200** on both the singular and plural routes, with a **200** control (`anyreach`) and four guessed slugs (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) answering **404**, so the route is live and the slugs are simply not ours. **Glama LISTED** twice: `/mcp/servers/CorpusIQ/corpusiq-docs` **200** and `/mcp/connectors/io.corpusiq/multi-source-mcp` **200**, while the `@`-prefixed form answers 404 as recorded. **Smithery REGISTRY-LIVE, CHANNEL-DEAD**: the `?q=` search endpoint answers **500**, which is their server bug and never a listing signal.

## Counts

| Measure | Before | After |
|---|---|---|
| Raw `<loc>`, maps 1-11 | 65,045 | 65,333 |
| Distinct keys, locale-stripped | 21,593 | 21,593 |
| Additions / removals | 0 | 0 |
| Server maps byte-identical to the 14:01Z capture | | 11 of 11 |
| Feed cards above cutoff | | 4 |
| Queue arrivals | | 15 |
| Servers catalogued | | 1 |
| Guides written | | 1 |
| Held with the class owner named | | 10 |
