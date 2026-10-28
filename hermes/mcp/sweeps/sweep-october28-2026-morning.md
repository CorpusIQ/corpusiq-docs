---
title: "MCP Server Discovery - October 28, 2026 (Morning Sweep)"
description: "Five finds in an eight hour window, led by three servers that read a site's own numbers and one that delegates the shop to an agent."
last_updated: 2026-10-28
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october28-2026-morning/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 28, 2026 (Morning Sweep)

Eight hours after the late pass the mcpservers.org counter had not moved at all: 17,913, the same figure recorded at 02:04 GMT, with ninety slugs across pages one to three and page one in the identical order. That is the first zero-move window measured on this surface since the October 24 night pass, and it changes where the work goes. Breadth cost three fetches and returned nothing, so the delta came from the two surfaces that do move at this gap: the mcp.so feed, whose newest card was submitted about an hour before the read, and the submission window, which advanced from `#6271` to `#6286`.

The shape of this window is measurement. Three of the five finds answer a version of the same question - what do my own numbers say, and which one should I work on - from Search Console, Google Analytics, Bing and a first party crawl. A fourth measures how four assistants describe a site. The fifth is the only one that acts, and it acts behind an approval.

## What Was Catalogued

Five entries earned guides. Each was read to the level its own surface allowed, and where a surface could not be driven the reason is named in the entry rather than the class blamed.

[Crevio MCP](/hermes/mcp/servers/external/crevio-mcp/) is the delegation entry. `https://mcp.crevio.co/mcp` answered a bare `initialize` with **HTTP 200** as `crevio-api` 2.0.0 on protocol `2025-06-18`, advertising tools, resources and three extensions (skills, events, tasks), and `tools/list` returned **twenty tools** with read-only and destructive hints on each. The pair that matters is `ask_crevio`, which hands a job to Crevio's own agent and waits for the result, and `run_script`, which runs JavaScript with bun on the account's computer so hundreds of API calls happen in one step with no agent turn between them. Writes pause a run in `needs_input` with pending approval ids and `resolve_approvals` is the only way forward, every action lands in `list_audit_events`, and OAuth 2.1 with dynamic client registration works on the Free plan while API tokens need Business.

[SEO Audit Console MCP](/hermes/mcp/servers/external/seo-audit-console-mcp/) is the technical audit entry and the most directly useful of the five for anyone running a site. `@houtini/seo-audit-console` is on npm at **0.17.0**, published 2026-08-03 and modified 2026-10-25, **Apache-2.0**, source at `github.com/houtini-ai/seo-audit`. It pulls Search Console history, runs a polite first-party crawl and stores both in **local SQLite joined on a normalised URL**, then ranks **143 checks by recoverable clicks** across **64 tools**. Every finding is labelled deterministic or judgement, and the output includes the fix (JSON-LD, a 301 map, internal-link suggestions) rather than only the finding. Search Console and the crawl are free; DataForSEO is optional and cached for 20 days, and the vendor prices a weekly portfolio refresh for eight sites at about $0.22.

[dotTide MCP](/hermes/mcp/servers/external/dottide-mcp/) answers the portfolio problem rather than the single-site problem. `dottide` is on PyPI at **0.3.1** across three releases, installed with `uvx dottide`, MIT, and filed as submission `#6274` at `05:37:12Z`. One Google service account reads Search Console and GA4 for every site it has been granted, **even when those properties sit under different Google accounts**, plus Bing Webmaster Tools, WordPress.org, Firefox Add-ons and GitHub. Nine tools, three prompts (Weekly review, What to work on, Index check), GA4 traffic with **AI assistant referrals counted separately**, and credentials in the operating system secret store rather than the config file. Every scope is read-only and `discover` writes the configuration from the properties the key can actually read. No endpoint exists to probe, which the entry states.

[AEO Engine MCP](/hermes/mcp/servers/external/aeo-engine-mcp/) is the AI visibility entry, and it is the cleanest free surface of the window. `https://aeoengine.ai/mcp` answered `initialize` with **HTTP 200** as `aeo-engine-aeo-report` 2.0.0 on protocol `2025-03-26`, and `tools/list` returned exactly two tools with full schemas. `run_aeo_report` takes a domain and a **real work email that is MX validated with disposable domains rejected**, runs up to about ten minutes, and returns a per-engine breakdown with provenance, competitor gaps, the measured questions, competitor evidence, a named share of voice and a `markdown_summary` written to be read aloud. `get_aeo_report_status` polls one job and its status vocabulary is honest about the middle (`needs_review` and `running` versus terminal `complete`, `partial`, `failed`). One competitor pins on the public path; five need an agency key.

[AhaSend MCP](/hermes/mcp/servers/external/ahasend-mcp/) is the email infrastructure entry. `https://mcp.ahasend.com/mcp` answered a bare `initialize` with **HTTP 401 and the body `no bearer token`**, which is the correct account-gated shape, so the surface is the vendor documentation plus the MIT source at `github.com/AhaSend/ahasend-mcp`. OAuth 2.1 with a browser login and no key to copy, a **50 recipient default cap** on a single send, campaigns that show the details and send only after the user confirms, received email **hidden from the agent unless enabled and then marked untrusted**, tool exposure scoped by the API key with a read-only mode, and a free plan of **1,000 emails a month** on servers in the EEA with ISO 27001. The local developer binary `cmd/ahasend-mcp-dev` takes `AHASEND_API_KEY` and `AHASEND_ACCOUNT_ID`.

## What Was Held

Named so the next pass cannot read any of them as fresh.

- **OneStore** (`#6286`) is the near miss of the window. The submission advertises 43 tools for App Store and Play Store management at `https://www.onestore.so/en/mcp`, but that URL answers **GET 200 as a page and POST 405**, and `https://onestore.so/mcp` only 307-redirects to it, so no JSON-RPC surface could be confirmed. Held on shape until it answers `initialize`.
- **PressBotics** is on the feed and its endpoint is real: `https://mcp.pressbotics.com/mcp` returned **HTTP 401 with the body `Unauthorized: connect Pressbotics via OAuth.`** There is no published tool reference behind it, so the entry would be an endpoint and an auth mechanism. Held until a tool list exists.
- **Signal Feed API** sells daily market-regime context per call at 0.10 USDC on Base through x402, with rules derived from the seller's own **paper research accounts**, a first issue dated 2026-10-26 and no track record. Held on class as an unproven paid signal feed.
- **imageat** and **Gemini MCP** are both creative generation with a credit or key cost, held on class alongside getimg and Cardboard AI. The Houtini Gemini server is worth remembering for one pattern rather than for its tools: thirteen tools that preview images, SVGs and video **inline through MCP Apps** instead of returning a file path.
- **GhostPaw Affinity** (`#6283`) keeps local relationship memory with affinity and trust scores and a contact cadence. Held on class as personal memory rather than an operator record, though the cadence model is the interesting half.
- **Conciergr Timetable** (`#6281`), **Kite** (`#6278`), **MediaLit** (`#6277`), **Nhost** (`#6284`), **WTFM** (`#6285`), **godspeed** (`#6282`), **Inbox eSIM** (`#6276`) and **PlushSource** (`#6275`) were each read and held on class: one vertical timetable app, hosted Discord bot building, storage and CDN infrastructure, managed backend tooling, help-guide generation from source code, a desktop study app, consumer travel eSIM purchase over the Machine Payments Protocol, and a single-niche manufacturer directory with bundled data.
- **Seller Fees Calculator** (`#6279`) and **US Freelancer Tax Calculator 2026** (`#6280`) are both local deterministic math on bundled tables, held on class: marketplace fee math is already carried by FlipProfit and Seller Profit Doctor, and the tax tables carry a year in the package name so the entry would age faster than the catalogue.
- **`#6272` and `#6273`** were opened and closed by mistake. **Agent Bounty Feed** filed four times in the previous window and is recorded there as a filing pattern, not re-read.
- Carried feed cards already dispositioned in earlier passes and left alone: TruLata, RelayLink, TestWell Lab Tests, LoreKeeper, Mythex, Launchdog, drop.media, PixelFlow, Pidgeon, Ask a human expert, StalkChain (a client, not a server).

## Directory Status Re-Verified

- **mcpservers.org** `/all` pages one to three read through the r.jina.ai reader proxy at the 10:0x GMT stamp: **90 unique slugs, counter 17,913**, unchanged from the 02:04:34 GMT read, with page one in the identical order. First zero-move window since October 24.
- **mcp.so** `/feed` page one read through `web_extract`: **30 cards**, newest submitted about an hour before the read (AhaSend), against a prior newest of `2026-10-27T22:39:16Z`. Five cards were new to this catalogue.
- **chatmcp/mcpso** submission window: **`#6272` to `#6286`** over the authenticated GitHub API, fifteen issues of which two were opened by mistake, so thirteen substantive submissions, against a prior window ending at `#6271`.
- **Catalog** 1023 to **1028 servers**, guides 1171 to **1176**.

## FAQ

### Why is there no new server from mcpservers.org this time?

The counter did not move between 02:04 and 10:0x GMT and page one returned in the same order, so there were no new listings to find. The feed and the submission tracker carried the delta instead.

### Which of these five can an operator use today without paying?

Three. SEO Audit Console is free and open source with an optional paid key for competitor data, dotTide is free and read-only with a Google service account, and AEO Engine's public report is free and keyless. Crevio works on its Free plan through OAuth. AhaSend has a free tier of 1,000 emails a month.

### What does the approval model in Crevio actually protect?

Writes. A run that reaches an action it is not authorised for pauses in `needs_input` with pending approval ids, and `resolve_approvals` is the only path forward. If the account grants more autonomy, the pause does not happen, so the account setting is the control rather than the tool.

### Why hold OneStore when the submission lists 43 tools?

Because a submission is a claim and an endpoint is evidence. `https://www.onestore.so/en/mcp` answers GET with a page and POST with **405**, so there is no way to confirm the tool list or the auth shape, and a guide built on the claim alone would read as verified.
