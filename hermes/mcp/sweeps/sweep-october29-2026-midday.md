---
title: "MCP Server Discovery - October 29, 2026 (Midday)"
description: "Counter finally moved to 18,230: seven finds, all from a 26-issue window, spanning scheduling, invoicing, monitoring and approval."
last_updated: 2026-10-29
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october29-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 29, 2026 (Midday Sweep)

This pass fired at `10:00 MST` against a morning read whose newest feed card was stamped `2026-10-29T08:10:00Z`. Seven hours is a normal midday gap, and for the first time in three reads the curated counter moved: mcpservers.org went from **18,225** to **18,230** while page one rotated to a completely different thirty cards.

## What Was Catalogued

All seven entries came from the **issue window**, which carried 26 submissions between `#6378` and `#6403` in six hours. That is the busiest window of the day so far, and the finds are unusually operator-shaped: a rota, an invoice the tax authority has to authorise, a page that changes price, an approval before anything leaves, a Spanish posting flow with a confirm step, a video ad's real age, and fundamentals as they were known on a date.

[PtData MCP](/hermes/mcp/servers/external/ptdata-mcp/) is the strongest entry of the batch because it was **driven to a full tools list**. `https://api.ptdata.io/mcp` answered `initialize` with **200** over server-sent events, `serverInfo` name `ptdata` version **3.3.2**, and a `mcp-session-id` header. A `tools/list` without that header returned `Missing session ID`, and the same call with it returned **four tools**: `get_index_constituents`, `get_fundamentals`, `get_filing_metadata`, `get_earnings_event`. Every schema takes an `as_of_date`, index membership is **survivorship free**, fundamentals carry source lineage, filings carry amendment linkage, and the earnings tool returns the **8-K acceptance timestamp** with the realized price reaction. Free tier is 120 per minute and 200 per day per IP, reset at UTC midnight.

[SpyWinAds MCP](/hermes/mcp/servers/external/spywinads-mcp/) was also driven keyless: `initialize` **200** listing protocol versions `2026-07-28` through `2025-03-26`, and **five tools** covering a video ad's real age, a store's live ads, a page's live ads, video reuse research and a Shopify product export. The two questions it answers are the ones that decide whether a creative is worth copying, and the export turns research into a sourcing decision. Provenance is Meta's public Ad Library with an explicit non-affiliation notice; `/docs` is a 404, so quotas are unstated.

[Stratum Shifts MCP](/hermes/mcp/servers/external/stratum-shifts-mcp/) answers `initialize` with **401** `Sign in to Stratum Shifts to continue.`, and its protected-resource document names the resource, the authorization server, header bearer, resource documentation at `/support`, and exactly three scopes: `openid`, `email`, `shifts`. The product fills a week inside availability and hour limits, flags every clash instead of resolving it silently, and outputs one link the team reads. Free for one workplace and up to 10 staff.

[BriefPanel MCP](/hermes/mcp/servers/external/briefpanel-mcp/) answers **401** `{"error":"unauthorized"}` with a protected-resource document carrying two scopes, `read` and `write`. Its model is field-level: name the fields, and each check returns typed values with the previous and the current one. Note the discovery host: the apex returns 404 while the `actions` subdomain returns 200.

[Pitstop MCP](/hermes/mcp/servers/external/pitstop-mcp/) is the approval gate rather than the memory store. **401** on a bare initialize, then a document with a single scope `pitstop` and `resource_name` Pitstop. Anything that leaves the firm produces a validation request and a one-time approval link emailed to the owner, and the vendor's own onboarding advice is one recurring task at ask first for 30 days.

[Cobra MCP](/hermes/mcp/servers/external/cobra-mcp/) answers **401** with JSON-RPC `-32001` and a message listing three accepted API-key forms, `Authorization: Bearer`, `X-API-Key` or `?APIkey=mfact_...`. The protected-resource path returns **404**, so this is an API-key surface, which decides whether an OAuth-only client can connect at all. It issues invoices, credit notes and withholding retentions authorised by the SRI in real time, with a free sandbox whose keys are documented as never issuing real tax documents.

[micm.mx MCP](/hermes/mcp/servers/external/micm-mx-mcp/) answers **401** with a document naming exactly three scopes, `posts:read`, `metrics:read` and `posts:write`. The connector is documented in Spanish, stamped 29 October 2026, uses OAuth with PKCE and no API keys, covers Instagram, Facebook and LinkedIn, and states the owner always confirms before anything is scheduled.

## What Was Read and Held

Twenty-six issues arrived and seven became entries. The rest are dispositioned in the catalog so the next pass cannot read them as fresh. `DeskPartner` (69 tools, shared desktop kanban for agents) and `recall` (Claude Code memory for other clients) are developer tools. `Postemi` returns **404** at `postemi.com/mcp` and at its discovery path, so the social publishing class stays covered without a driven surface. `Tera Ads` is Meta ads management and `Convocore` gates on a **workspace secret** rather than OAuth. `tinyrex-mcp` and `PennyData web utility actors` belong to the **Apify actor class**. `Stay Cost Brain` serves an **HTML page rather than JSON-RPC** at its `/mcp` path. `Money You're Owed`, `DrinkedIn Night Out`, `ismail` and `CodeDebut` are consumer or directory-shape holds. The five `.fyi` submissions are the **register-fleet wave** covered by the standing ruling, and `IndustryLens` is already catalogued.

On the feed, seven cards sat above the morning stamp and only two earned guides. `OpenProfit` returns **401** `Missing, expired or revoked API token` and reads as a profit dashboard, `legivel` is Markdown to typeset PDF in the **document rendering class**, `Hashlock Markets` is **crypto OTC**, `Vid Kraken` is a **YouTube downloader**, and `Bright Canoe` could not be reached at `mcp.brightcanoe.com`, so it is held pending an endpoint.

On `/all`, 83 unique slugs across three pages, and the remaining names are class holds. `sellerfox-mcp` is Amazon seller revenue and profit analytics, already covered by the catalogued **AMZ Vault, Pangolinfo and Datrace** surfaces. `trypostit` is a **404 shell**, the Awaken Tax page returned navigation only, `hotel-lobby-org` is a consumer video-trend filter, and the rest are the cohort already held this morning.

## Surfaces This Pass

| Surface | Reading | Delta |
| --- | --- | --- |
| mcpservers.org `/all` p1 to p3 | counter **18,230**, 83 unique slugs, page one fully rotated | counter **+5** after two flat reads |
| mcp.so `/feed` p1 | 27 cards, newest `2026-10-29T16:55:43Z` | seven above the morning stamp |
| chatmcp/mcpso issues | `#6378` to `#6403` | 26 issues in six hours |
| Live probes | twelve endpoints | two driven to tools lists, six 401 with contracts, two failed to serve |

## Catalog Movement

Catalog **1050** to **1057** servers, guides **1198** to **1205**.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [All sweep reports](/hermes/mcp/sweeps/)
