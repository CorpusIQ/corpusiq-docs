---
title: "MCP Server Discovery - November 24, 2026 (Night)"
description: "A directory flat to the key, a feed with its anchors back, and two products that both gate on OAuth: a venue CRM and a documentation engine."
category: "MCP Ecosystem"
last_updated: "2026-11-24"
---

# MCP Server Discovery - November 24, 2026 (Night)

Fired on the **03:00 MST** tick, **5.7 hours** after the evening pass stored its baseline at **04:24Z** and shipped four. The directory added nothing: every per-map count is identical to the evening capture, the key set is the same **23,894** and the `lastmod` window is empty after the evening batch. The material in this window came from two places that are not the sitemaps at all, the feed and the submission queue, and both ships are the same shape: a real operator product behind a complete OAuth discovery chain, which is the evidence tier this catalogue trusts most when a credential is not available.

## The window, measured

```text
mcpservers.org /sitemap.xml   sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12         37,769   identical to the 04:16Z evening capture
  servers/1  ..... 4,171     servers/7  ..... 5,864
  servers/2  ..... 2,516     servers/8  ..... 2,739
  servers/3  ..... 2,936     servers/9  ..... 2,634
  servers/4  ..... 3,221     servers/10 ..... 2,575
  servers/5  ..... 3,327     servers/11 ..... 2,524
  servers/6  ..... 2,906     servers/12 ..... 2,356     sum 37,769 exact
raw total incl. priority + remote   38,036
distinct keys, maps 1-12     23,894   identical to the evening capture
union with priority          23,943   evening 23,928, +15 locale forms of one remote slug
priority-servers.xml         252 raw, 34 distinct keys
remote-mcp-servers.xml       15 raw, 1 distinct key in fifteen locale forms
lastmod, server maps         34,486 stamped rows; ZERO at or after 2026-11-24T04:30Z
newest stamp on the surface  2026-11-24T00:27:03Z  (the evening ingestion batch)
mcp.so /feed                 200, 159,377 bytes, 30 cards, 30 stamps, 5 above the cutoff
queue window                 #7941 - #7965, twenty-five filings 04:32Z to 09:23Z
```

**Zero arrivals, proven on the key set rather than the count.** The twelve numbered maps returned the same **37,769** raw `<loc>` entries as the evening capture, the block still sums exactly, and the distinct key set is **23,894** on both. The lastmod scan makes the strongest statement available: **34,486** stamped rows with **not one** at or after the evening cutoff, the newest stamp anywhere on the surface being **00:27:03Z**, which is the batch the evening pass already catalogued. A directory that has not stamped a page in **ten hours** has not published one.

The union reading moved by **fifteen** and the movement is one remote slug. `remote-mcp-servers.xml` carries **one** distinct key, `clockwise`, printed in fifteen locale forms (`/de/`, `/pt-BR/`, `/zh-TW/` and the rest). Those are the fifteen. A union count in this catalogue is only comparable to another union count on the same normalisation basis, and the remote route takes locale prefixes that the servers route does not.

**The feed's anchors came back.** Last evening's pass recorded that `mcp.so/feed` had regressed to a React shell with no `/servers/` hrefs in the served HTML. This pass paired **30** stamps to **30** slug anchors, slug for slug, with no gap. The regression is closed and the pairing recipe works again; the stamp format is still `title="M/D/YYYY, HH:MM AM/PM"` in UTC, and it is still the only reliable date on the page.

## Shipped (2, both driven to their gate)

- [Spacestack MCP - Venue Bookings Inside the Assistant](/hermes/mcp/servers/external/spacestack-mcp/) - a mcpservers.org arrival and a feed card at **04:10Z**. The catalog's first venue-management entry, and the most complete OAuth chain in recent memory: **401** with `resource_metadata` -> protected-resource document **200** naming exactly two scopes, `spacestack:read` and `spacestack:write` -> RFC 8414 document **200** with authorization code, refresh, dynamic registration and PKCE **S256**. The product side is the reason to read the guide: the connector acts **as the signed-in team member with that person's role**, the connect step offers **Read only or Read and write** per person, and the workspace switch is **off by default** with the vendor documenting that turning it off **disconnects everyone straight away**. It cannot delete, send anything to a client, take or refund a payment, or change billing, and what it can do is the venue's actual day: check a date, read the calendar, add a lead, book a tour. **$99 per venue a month billed yearly, $1,188 a venue a year**, unlimited seats, 30-day trial with no card.
- [Vidocu MCP - Documents Turned Into Training Videos](/hermes/mcp/servers/external/vidocu-mcp/) - a feed card at **08:11Z**. **146** tools by the vendor's own documentation, **168** by the mcp.so listing, behind the opposite of an identity token: **17 resource scopes** on the protected-resource document and **44** on the authorization server, from `videos:write` to `locks:write`. Its issuer is `api.vidocu.ai` while the sign-in screen is on `vidocu.ai`, so a client that enforces same-origin on the authorization endpoint will refuse a server that is correctly configured - a client bug that reads like a vendor bug. The work it does is operator work: a PDF, DOCX, PPTX or Keynote becomes one finished video unattended; a video becomes a step-by-step help article; `get_article` reads one back without paying to regenerate it; `get_credit_costs` prices a job before it starts. **Analysis is 50 credits a minute**, so a 10-minute walkthrough is a Starter plan's whole month, and the Knowledge Center add-on is **$100 a month** on paid plans.

## Also identified this pass (not catalogued)

**The best hold is measured, not waved past.** **1Alexander AI Visibility Tracker** (feed, **08:43Z**) answers `initialize` **200** keyless as **1.0.1** with an instructions string and returns a full **17-tool** `tools/list` with schemas, annotations and `_meta.securitySchemes` naming OAuth scope `mcp:live`; `tools/call` is where it gates. It is the strongest evidence tier of the pass and it is still a hold, because prompt-level AI visibility is the most crowded class in this catalogue: **AI Visibility Analytics**, **SEOforGPT**, **geolint**, **LogNorm**, **OperStack** and **Conqueror** already own it. Named here so the next pass does not re-open it as new.

**Feed cards above the cutoff, other than the two ships.** **Embeddable** (**08:09Z**) is a widget and landing-page builder at `https://mcp.embeddable.co/mcp` with **15** tools and a `whoami` that reports the workspace and the connection's own permissions, held on the page-builder class. **mcp-ads** (**07:03Z**) is already a catalogue entry; the card is a relisting of a product this catalogue holds, not an arrival.

**The queue, twenty-five filings, all dispositioned.** **Trakis** (#7965, free no-key SEO checks and a 25-page audit, registry `io.trakis/seo-checks`) is the closest miss and holds on the saturated site-audit class (**Auditspark**, the SEO+GEO pair, the third-party site-check hold) rather than on access. **Atalaya AI crawler check** (#7956) holds on the same AEO class, where **geolint** already ships **51** crawler tokens. **runofsho** (#7959, run-of-show rundowns, API key today with OAuth planned) holds as adjacent to the event class this pass just entered. **DispatchNode** (#7944, field service, Clerk OAuth, **17** tenant tools) holds on the dispatch class owned by **Crisphive**. **MarketPounce** (#7943, **246** tools over a brand growth desk, Clerk OAuth) holds on the marketing-data class carried by **Otto**, **Manifold** and **Metrinel**. **CleanedWeb** (#7955) is an API catalogue with a genuinely keyless `?profile=public` door and holds on the API-directory class. **OCRRouter** (#7954) holds on document intelligence, **Quantisnow SEC EDGAR** (#7952) on public filings, **Cozu** (#7957) on art and 3D assets, **getoolkit-mcp** (#7958) on local utility tools, **Inku Japanese** (#7953) as a consumer learning surface.

**Sirfus CAR** (#7941) is worth naming for its consent design rather than cataloguing: three tools answer with no sign-in and contact nobody, and sending a request needs a **6-digit code texted to the person's own phone** before any business is contacted. That is a control pattern this catalogue would like to see copied.

**Formation Lane US LLC Fees & Deadlines** (#7942) is free, keyless and exactly the kind of statutory-data surface this catalogue ships, and it could not be reached: the TLS handshake returns `TLSV1_ALERT_ACCESS_DENIED` from this egress on both urllib and curl. It is recorded as **unreachable from here**, not as a hold on merit, and it is the first queue item to retry next pass.

**Two fleets and one publisher.** The **five mambalabsdev** filings (#7960 to #7964: YC jobs, XING jobs, Naver blog search, Moz domain authority, Yahoo Finance quotes) are one author's Apify actor wrappers under the standing transport ruling. The **seven-site fleet** from one publisher (#7945 to #7951: OwnlyBrand, PeakRoam, JinXinCai Printing, HT Waterless Radiant, SpeedyDrone, PSL Modular, Truvana Tech) is a new pattern worth recording: each site publishes its own keyless read-only MCP with an `ask_expert` tool that requires the named person's consent, which is the same idea as Sirfus CAR from the other direction. Held as one fleet on the local-business-site class.

## Listings

Both of our own surfaces are present in this capture: `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs` sit inside the **23,894** key set, so mcpservers.org remains **LISTED** on both. This pass did not re-read `/all`, which has answered **403** by edge policy since 4 November, and it did not re-measure Glama, Smithery or the official registry; the midday pass measured those and its states stand.

### Why ship two of thirty?

Because the other twenty-eight either repeat a class this catalogue already covers, arrive as fleets under one transport ruling, or answer nothing that can be certified. The two that shipped share a single property the holds do not: a **published authorization contract** whose every hop answers **200** and whose scopes say what a token can do. For an operator deciding whether to connect a chat assistant to the system that runs their bookings, that chain is the difference between a product and a promise.

### What did this pass not do?

It did not execute a single authenticated call. Both guides describe tool surfaces and plan rules from the vendors' own documentation and measure the gate itself, which is the honest ceiling when no credential exists and no keyless schema is published. It did not settle the Vidocu tool count of **146** against **168**, and it did not retry Formation Lane from a second egress.
