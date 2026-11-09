---
title: "MCP Server Discovery - November 9, 2026 (Midday Supplement)"
description: "One hour after the midday pass: the canonical held at 20,204 servers, two feed cards arrived, and both became guides"
category: MCP Ecosystem
added: 2026-11-09
last_updated: 2026-11-09
source: "the mcpservers.org thirteen-sitemap canonical (63,650 raw loc entries, 20,204 distinct server URLs), the mcp.so feed read twice (plain and cache-busted), and the chatmcp/mcpso submission window #7015 to #7021"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 9, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday pass. The canonical did not move, the queue carried seven arrivals, and the two servers this pass catalogues both came from the feed rather than the queue: a 48-tool market-data endpoint that answers discovery without a key, and a vacation-rental property manager that does not answer at all until you authenticate.

```text
Canonical:   20,204 distinct server URLs from 63,650 raw <loc> entries across 13 maps
             (20,204 at the midday capture from 63,649 raw: no new distinct server URL)
Feed:        146,544 bytes plain, 146,580 cache-busted, 29 cards, 2 above the midday stamp
Queue:       #7015 to #7021, 7 issues, no gaps, all arrivals
Catalogued:  2 servers, 2 guides
Evaluated:   9 candidates (7 queue arrivals plus 2 feed cards)
```

## The window, measured

The thirteen server maps, `servers/1.xml` through `servers/11.xml`, `priority-servers.xml` and `remote-mcp-servers.xml`, returned **63,650** raw `<loc>` entries and **20,204** distinct server URLs after the inline locale prefixes were stripped before the `/servers/` subset was taken. The midday capture one hour earlier reported the same **20,204** distinct URLs from **63,649** raw entries, so the window produced **no new distinct server URL**; the single extra raw entry is a duplicate rather than an arrival.

Stated as a limit rather than a convenience: the midday set was not retained on disk, so this pass proves the **count** held and does not claim a set-identical diff. A rename pair would read the same way, which is why the editorial delta this window rests on the feed and the queue instead.

mcpservers.org `/all` answered **403** by edge policy, the standing condition since November 4, so that surface contributed nothing and is not evidence of anything missing.

The mcp.so feed was read twice, **146,544** bytes plain and **146,580** cache-busted, **29** cards on both reads with the same set: **28** server cards and one client card. Two sit above the midday stamp `2026-11-09T16:30:43Z`, and both are this pass's finds:

```text
17:06:33Z  nowistay      Nowistay - run your vacation rental business from ChatGPT or Claude
17:44:15Z  tradingdata   TradingData - free market data for AI agents through one MCP URL
```

The submission queue carried **7** numbers from **#7015** to **#7021** with no gaps, every one an arrival: SavedThat, GMPSignal filed twice, one Mamba Labs extractor, WhisperShortcut, OttoQuest and NOID Agent Kit.

## Catalogued: 2 servers, 2 guides

**[TradingData MCP](/hermes/mcp/servers/external/tradingdata-mcp/)** at `https://mcp.tradingdata.io` is the rare case where the discovery half of the protocol is open: a keyless `initialize` answered **200** as server `tradingdata` **0.1.0** on protocol `2025-06-18`, and `tools/list` returned all **48** tools. `tools/call` then answered JSON-RPC `-32001`, "A valid API key or OAuth access token is required to call tools", so the surface is inspectable and the data is not. The protected-resource document names one scope, `market:read`, with `https://tradingdata.io` as the authorization server. The 48 tools carry options chains with greeks, SEC XBRL statements, insider and institutional holdings, ETF holdings, COT positioning and short interest, crypto and on-chain metrics, commodities and FX, and a macro family that separates a series from a release and from a **revision**, which is the distinction that keeps a restated number out of a model's answer. Two measured details are recorded in the guide: the vendor's claim of 800,000+ macro series and timestamped quotes is a vendor claim, and the two OAuth well-known routes disagree on the resource identifier (`mcp.tradingdata.io` on the bare path, `tradingdata.io/mcp` on the `/mcp` variant), so a client should register against the host it actually calls.

**[Nowistay MCP](/hermes/mcp/servers/external/nowistay-mcp/)** at `https://api.nowistay.com/mcp` is the gated case, and the gate is the interesting part. A keyless `initialize` answered **401** with `{"detail":"Missing bearer token"}`, and the public protected-resource document lists **fourteen** scopes in seven read and write pairs across properties, calendar, bookings, missions, messages, guides and knowledge. That is the shape of an operating system rather than a feed, and it is why the guide can describe the permission model without seeing a single tool: a reporting assistant can hold the read half while a separate operations assistant holds the write half. The product is a PMS and channel manager for vacation rentals across Airbnb, Booking.com, Vrbo, Expedia and Agoda, with staged writes as the documented default: every change is shown before it lands, read-only questions never mutate data, and OTA-sourced reservations stay read-only. It is the first short-term-rental entry here; the four property-software neighbours already catalogued all assume a lease measured in months.

## Held this pass, with the class owners named

- **SavedThat** (**#7015**, `app.savedthat/library`) searches the videos a user saved from Instagram Reels, TikTok and YouTube by what was said in them, with quote, timestamp and link, plus transcription libraries of public creators. OAuth 2.1 with dynamic client registration, eight tools, one of them a Stripe Checkout widget. Held on the video-transcript class carried by BulkTranscripts, CuePrecise and capslane; the saved-library framing is a personal-collection surface rather than a new data capability.
- **GMPSignal** (**#7016** and **#7017**, one product filed twice as a starter kit and a hosted API) is a 40-tool surface whose endpoint is `mcp.apify.com/?actors=...`, wrapping Apify actors across crypto, prediction markets, KYB, sanctions and CISA KEV feeds. Held on the standing Apify-actor hold class and the October 7 Mamba Labs fleet ruling: distribution through an actor gateway does not make the wrapper a connector.
- **mcp-ai-list-extractor-any-website** (**#7018**, mambalabsdev) is one tool over an Apify actor, and the twenty-first package from the same publisher in this window. Held on the same ruling, and on the class already carried by the catalogued extraction tools.
- **WhisperShortcut** (**#7019**, mgsgde/whisper-shortcut, 76 stars) is a macOS menu-bar dictation and meeting-notes app with an MCP server bound to `127.0.0.1:47823` behind a read key or a write key. Held on the meeting-capture class, which already carries transcription across that surface, and on the local-install tier: it is a capable app whose MCP is a companion interface, not a hosted data source.
- **OttoQuest** (**#7020**, `com.ottoquest/mcp`) searches US used-car listings against estimated market values, looks up a VIN and its reported history, values a car without a VIN, lists dealer inventory, checks NHTSA recalls and manages deal alerts, over OAuth 2.1 with PKCE and CIMD. This is the closest call of the pass and it is held on named owners rather than a category: CarChat Inventory already serves live US dealership inventory with VIN detail and market price statistics, and Dutch Vehicle Context serves one verified vehicle report per plate from eleven official registers. OttoQuest's addition is valuation without a VIN; the class is held, so it is held.
- **NOID Agent Kit** (**#7021**, `com.onrender.noid-agent-kit/noid-agent-kit`) mixes invoices and receipts, whale and new-token alerts, and a launch checklist, metered in credits, on a free `onrender.com` host, with the listing itself stating it is not affiliated with the chain it names. Held on the crypto-alert and agent-payments classes and on substance: three unrelated surfaces behind one name is a kit, not a connector.

## Core listing check, measured rather than inherited

Both catalogued guides cross-link neighbours that exist on disk, and the four mcp.so direct slugs for our own listing remain absent as measured in the midday pass; `/all` remains the standing **403** rather than a delisting read. No change to our own listing state this window.

## Counts

Canonical 20,204 distinct URLs from 63,650 raw `<loc>` entries across 13 maps, against 20,204 from 63,649 at the midday capture. Feed 146,544 and 146,580 bytes, 29 cards, 2 above the midday stamp. Queue 7 arrivals across #7015 to #7021. **9** candidates evaluated, **2** endpoints measured, **2** servers catalogued with **2** guides. Guide tree **1,133** directories before this pass and **1,135** after; **1,276** entries before and **1,278** after; **1,547** Markdown files under `hermes/mcp/` before and **1,549** after.
