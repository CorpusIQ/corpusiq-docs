---
title: "MCP Server Discovery - November 10, 2026 (Night)"
description: "A six-hour gap with 194 new server URLs, seven queue arrivals and three feed cards, where two operator-facing entries earned guides"
category: MCP Ecosystem
added: 2026-11-10
last_updated: 2026-11-10
source: "the mcpservers.org thirteen-sitemap canonical read from its new /sitemaps/ paths (63,847 raw loc entries, 20,398 distinct server URLs), the mcp.so feed read cache-busted, the chatmcp/mcpso submission window #7054 to #7060, and the official MCP registry for candidate resolution"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 10, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the November 9 evening sweep. The canonical grew by **194** server URLs, the submission queue carried **seven** arrivals, the feed carried **three** new cards, and two entries earned guides: the first commerce warehouse in the catalog whose metric definitions ship as tools, and the first conversion-tracking surface that can only propose.

```text
Surfaces:    13 server maps, 63,847 raw <loc> entries, 20,398 distinct server URLs
             (20,204 at the 21:00 MST capture from 63,652 raw: 194 additions, 0 removals)
Feed:        145,011 bytes cache-busted, 34 cards, 3 above the evening cutoff
Queue:       #7054 to #7060, 7 issues, no gaps, all arrivals
Catalogued:  2 servers, 2 guides
Crossref:    194 additions, 88 zero-hit on headings, guide directories and sweep prose
```

## The window, measured

The first mechanic of this pass is that the sitemaps **moved**. `https://mcpservers.org/servers/1.xml`, the path every prior pass used, now answers **404** to a plain urllib request and a **403** with a 5 KB interstitial to a browser user agent. The sitemap index at `https://mcpservers.org/sitemap.xml` answers **200** and names the new location, `https://mcpservers.org/sitemaps/servers/1.xml` through `11.xml`, plus `priority-servers.xml` and `remote-mcp-servers.xml`. Thirteen maps were read from the new path, every one **200** on the first attempt:

```text
servers/1.xml   7,588 locs    servers/7.xml   9,351 locs
servers/2.xml   5,948 locs    servers/8.xml   6,588 locs
servers/3.xml   6,518 locs    servers/9.xml   4,035 locs
servers/4.xml   6,744 locs    servers/10.xml  2,601 locs
servers/5.xml   6,940 locs    servers/11.xml    452 locs
servers/6.xml   6,768 locs    priority 299, remote 15
                              total 63,847 raw entries
```

After the inline locale prefixes were stripped (**43,434** prefixed entries) and the `/servers/` subset was taken, the union is **20,398** distinct server URLs. The 21:00 MST capture on disk held **20,204**, and the set diff came back **194 additions and 0 removals**. Two maps, `servers/12.xml` and `servers/13.xml`, answered 404 on three attempts each and are not part of the index, so the thirteen-map composition matches the evening pass exactly.

`mcpservers.org/all` answered **403** by edge policy, the standing condition since November 4, and the reader proxy answered **401** on bad IP reputation, so that surface contributed nothing again.

The feed was read cache-busted at **145,011** bytes with **34** cards, three of them above the evening cutoff: `seedance-2` at `06:46Z`, `myzucoins` at `06:04Z` and `secretpass` at `05:58Z` on November 10. The queue carried **seven** numbers from **#7054** to **#7060** with no gaps and every one an arrival.

## Catalogued: 2 servers, 2 guides

**[SourceMedium MCP](/hermes/mcp/servers/external/sourcemedium-mcp/)** at `https://mcp.sourcemedium.com/mcp` is the first commerce warehouse in this catalog whose canonical metric definitions are tools rather than conventions. The handshake answered **401** with the useful header, `WWW-Authenticate: Bearer resource_metadata=".../.well-known/oauth-protected-resource/mcp"`, and following that path returned a **200** protected-resource document naming one AuthKit issuer and the scopes `openid profile email offline_access`. The vendor documents **nine** tools on the current tool set and **eleven** on the earlier one, and the split matters to anyone counting: `describe_table` and `describe_tables` survive only on older connections, while `search_data_catalog` now does their job and reaches the customer's own tables as well. The published tool order is the transferable part: `get_data_context`, then `search_data_catalog`, then `query_metrics` when a named metric matches, then describe and `run_bigquery_sql` only when it refuses. The limits are published as numbers too, **500** warehouse rows before truncation, **100** Shopify and Meta records per page, **10 GiB** of billed bytes per query, **60 s** warehouse and **30 s** platform query time, **256 KiB** per response. It is also one of the few vendors in this catalog that documents **Hermes** by name, with `hermes mcp add sourcemedium --url https://mcp.sourcemedium.com/mcp --auth oauth` and `hermes mcp test sourcemedium` on its own connection page. Registry record `com.sourcemedium/source-medium` 1.7.0, active since 2026-09-01. Nothing was driven past the handshake because the session needs a workspace login, and the guide says so.

**[Signal Beam MCP](/hermes/mcp/servers/external/signal-beam-mcp/)** at `https://app.signalbeam.co/mcp` is the first entry here whose write scope is a verb the model cannot complete alone. The protected-resource document lists exactly two scopes, `sites:read` and `changes:propose`, and every change lands as a proposal an owner or admin approves in the dashboard; a connection can also be created read-only, which removes the second scope. An unauthenticated `POST initialize` answered **401** with a JSON-RPC error object, `-32600 Sign in to use this server`, rather than an empty body, which is a small correctness detail worth recording because a bare 401 leaves a client unsure whether the URL was right. What it reads is the part an operator feels first: totals against the prior period, revenue by source and campaign, the event log, one event's outcome at each destination platform, events held for consent and why, custom event frequency, and an audit that checks the script is on the live page and looks for pixels installed twice. What it cannot do removes four familiar failures: no delete tool for a site, pixel or rule, no access to ad accounts or campaigns, no editing or publishing of the website, and emails and phone numbers kept only as hashes that are never handed over. Registry record `co.signalbeam/signal-beam` 1.0.0, published **2026-11-10T06:14:37Z**, hours before this pass.

## Also identified this pass, with the owner or the reason named

The queue was seven arrivals and every one is class-covered. **Reliant Forge** (**#7054**) deploys an app from an agent with no account and holds on the deployment class, since the catalog already covers hosted deploy surfaces and this one is a developer convenience rather than an operator decision. **Patchwork** (**#7055**) edits Claris FileMaker `.fmp12` files through Claris' own command-line tools with re-export verification and numbered undo, held as a developer file-format tool: the audience is FileMaker developers, not the operator asking a business question, and no FileMaker entry exists because none has been worth one. **Xpensiv** (**#7056**) is a design model scoring an app for AI-default looks, held on the design and code-review classes. **Buildcord** (**#7057**) builds Discord bot flows with 19 annotated tools over OAuth 2.1, held on the app-builder class. **RunLater** (**#7058**) calls any public URL later on a schedule with retries and a run log, held on the monitoring class carried by changedetection.io, Visualping and Cronitor, with the added reason that a server able to POST to arbitrary public URLs is a write surface an operator should approve deliberately rather than connect casually. **Moose Tracker** (**#7059**) is a music tracker with a synth and a sample library, a creative tool. **Lumichess** (**#7060**) is keyless chess analysis, a consumer surface.

From the feed, all three cards hold: `seedance-2` on media generation through the KreatorFlow key, `myzucoins` as documentation search for one layer-1 network, and `secretpass` as coupon and voucher search, all three resolved through the official registry rather than read off the card.

The 194-URL canonical wave decomposes rather than repeats. **29** are documentation-path mirrors of products already listed (the `docs-`, `-docs-` and guides path forms that mcpservers.org mints per vendor page), **60** are namespace-form slugs, and the largest single contributor is the **mambalabsdev** fleet at **15** new items in this window, on top of the 19 that landed in the previous wave, each a one-input scraper or enricher (Amazon price and stock, Google Maps places, Google Trends, Facebook and Bluesky posts, Zillow listing details, US import records buyer finder, healthcare provider NPI). That fleet has prior disposition as a fleet, and this window adds no item that changes it. **4** slugs are one vendor's DuoLeads documentation set, **3** are Byondr image and receipt tools, and **2** are Rowhouse Software pages for Platemark and a games server. Of the 194, **88** came back zero-hit against headings, guide directories and sweep prose, and those were resolved in bulk through the official registry rather than guessed: **SourceMedium** and **Signal Beam** became guides, **Tamtam** (B2B leads from buying signals) holds on the sales-intelligence class with the buying-signal slice already carried by Hilead, **KoalaFix** (team memory with provenance per fact) holds on the agent-memory class beside [PLUR](/hermes/mcp/servers/external/plur-mcp/) and [Azquo](/hermes/mcp/servers/external/azquo-mcp/), **Voicent** (calls, texts and CRM on your own gateway) holds on the voice class carried by VoIP Studio and the voice-agent entries, **TellMyShop** (PrestaShop and WooCommerce changes with preview and undo) holds on the store-operations class, **mcp-ads.com** (Google, Meta, TikTok and LinkedIn ads from chat) holds on the ad-ops class that [PaidSync](/hermes/mcp/servers/external/paidsync-mcp/) owns, **Knocklog** holds beside [Agent Help Network](/hermes/mcp/servers/external/agent-help-network-mcp/) and [NMOS crawl analytics](/hermes/mcp/servers/external/nmos-crawl-analytics-mcp/), **UnlimitedMessaging** holds on the messaging class, **Featureloom** on project management, **Platform201** and **Causly** on developer tooling, **PigmentaLab** on print pre-press, **SocialDataApi**, **Rizamo** and **Mostra** on the saturated social data and publishing classes, **Glimpze** on support QA, and **Aperiodic** on crypto market micro-structure. The remaining zero-hit slugs are single-purpose submission-firehose entries, each one input to one output, and are held in that class rather than enumerated here.

## Core listing check

Measured rather than inherited. The four mcp.so detail routes answered **404** for `corpusiq`, `corpusiq-io`, `corpusiq-mcp` and `io.corpusiq`, which is the recorded bare-slug failure and not a delisting. The official registry returned four active records for `io.corpusiq/multi-source-mcp`: 1.0.0 published 2026-05-25 with the older "30+ business systems" description, 1.0.1 and 1.0.2 in October, and **1.0.3** published 2026-10-24 with "One governed MCP endpoint for 40+ business systems. Read-only, source-cited answers." The 30+ against 40+ drift recorded as closed in the November 6 pass is still closed on the newest version; the earlier versions keep their old text, which is how a registry works and is not a regression.

## FAQ

### Why did the sitemap URLs change this pass?

`https://mcpservers.org/servers/N.xml` no longer serves. It answers 404 to a plain request and a 403 interstitial to a browser user agent, and the sitemap index at `https://mcpservers.org/sitemap.xml` now points at `https://mcpservers.org/sitemaps/servers/N.xml`. Any script pinned to the old path reads a block that is not a permission decision; read the index first and follow what it names.

### What does a window of 194 additions and 0 removals mean?

That nothing was withdrawn or renamed in the six hours. The additions are then a question of composition rather than volume: of these 194, 29 are documentation-path mirrors of already-listed products and 15 belong to one publisher's fleet, so the count is larger than the number of new products. A window with removals is read the other way, by pairing each removal against the addition set by basename before treating it as churn.

## Counts

Canonical **20,398** against **20,204**, **194** additions and **0** removals from **63,847** raw loc entries across thirteen maps; feed **145,011** bytes with **34** cards and **3** above the evening cutoff; queue **7** arrivals, all arrivals; **204** candidates evaluated (194 additions, 7 queue, 3 feed); **40** registry lookups across the zero-hit set; two endpoints measured to the handshake plus a protected-resource document each; **2** servers catalogued and **2** guides; guide tree **1,136** directories before this pass and **1,138** after; **1,280** catalog entries before and **1,282** after; **1,552** Markdown files under `hermes/mcp/` before and **1,555** after.
