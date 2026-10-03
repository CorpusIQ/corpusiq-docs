---
title: "MCP Server Discovery - October 3, 2026 (Midday Sweep)"
description: "Midday sweep of mcp.so and mcpservers.org cataloguing two new business-relevant MCP servers: Toffu for ad account operations and RankOrg for SEO content."
last_updated: 2026-10-03
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october3-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "discovery"]
---

# MCP Server Discovery - October 3, 2026 (Midday Sweep)

Midday sweep over the mcp.so `/servers` listing (50 slugs) and mcpservers.org `/all` pages 1-3, both via the r.jina.ai reader proxy because direct fetches return the Cloudflare/JS shell without server data. Detail pages were fetched for every candidate; endpoints were probed for liveness. Two new business-relevant servers were catalogued, each with an integration guide.

## New This Sweep

### Toffu MCP - AI Marketing Agent for Ad Accounts

Hosted Streamable HTTP at `mcp.toffu.ai/mcp`. The vendor ships an agent-native onboarding path: `POST /agent/signup` returns an `api_key` and `company_id` with no email required, and a real email can be supplied to make the account human-claimable later. Eight tools are published in the machine-readable capability doc at `toffu.ai/.well-known/toffu.json`: `send_message`, `get_task_result`, `query_campaign_performance`, `creative_report`, the staged `propose_change` / `apply_change` / `undo_change` triple, and `fetch_memory`. The read/write split matters for operators running paid acquisition on more than one platform: an agent can propose a campaign edit, hold it for approval, and still roll it back. OAuth 2.1 + PKCE with Dynamic Client Registration is available for clients that prefer a consent flow. The endpoint returns 401 unauthenticated, confirming it is live and auth-gated.

### RankOrg MCP - SEO Content Engine for Agents

Remote MCP at `rankorg.com/api/mcp` with OAuth 2.0 (RFC 8414 discovery, RFC 7591 Dynamic Client Registration, PKCE) or a personal access token for headless clients. Twelve tools split explicitly into read and write: `getSiteContext` (call first to ground everything), `listContent` (filter by today, scheduled, published or all), `getContent`, `getSearchPerformance` (live Google Search Console clicks, impressions, CTR, average position, top pages, top queries and a daily trend), `getTopicalMap` (clusters through topics and subtopics to keywords with demand, difficulty, rankability and which keywords already have scheduled or published articles), plus `researchKeywords`, `generateArticle`, `updateContent`, `rescheduleContent`, `publishContent` and `mergeContent` / `unmergeContent`. The vendor documents `publishContent` as public and effectively irreversible, to be invoked only after explicit confirmation.

## Listings Verified

| Directory | Status | Evidence |
| --- | --- | --- |
| mcpservers.org | LISTED | Reader-proxy fetch of `/servers/corpusiq-io` returns HTTP 200 with title "CorpusIQ MCP Server \| Awesome MCP Servers" |
| glama.ai/mcp | LISTED | HTTP 200 on the `@corpusiq/corpusiq-docs` slug |
| smithery.ai | REGISTRY ENTRY PRESENT | `benoit-p/Cprusiq` in the registry API response; flip-flop class, no submission path available |
| mcp.so | NOT LISTED | Search returns unrelated servers (Medplum, Hostinger, PLUR, Termany and others) with no CorpusIQ entry |
| PulseMCP | LISTED | Reader-proxy fetch of `/servers/corpusiq` returns the CorpusIQ listing |

## Identified But Not Catalogued

**mcp.so `/servers`:** Casefile (self-hosted agent case-file memory and hand-off tracker; agent-memory class already covered by the Jotter and clexo dispositions), q-ring (quantum-themed local secret keyring for coding agents; dev secrets-utility class), OrangePro (local-first behavior mapping and test generation with mutation testing; dev-qa class), Muumuu Domain MCP (first remote MCP from a Japanese domain registrar, GMO Pepabo; regional consumer service). The remaining slugs were catalogued or disposed in prior sweeps, including AON Agent Offer Network, Hostinger, BlazeCDN, Clipkit, Coinlobster, Crawlforge, Datris, EqIQ, Etincel, Farpy, Fhirhydrant, FiatDock, Foremerge, Gologin, Groundwork, Heylead, Ibanforge, Lawstronaut, Legion, LocalCan, Modelglass, Openlore, Patsnap, Perfex, SCDV, Snipara, Somacheck, Strac, Subtext, Sugra, Tracetify and OpenZiti.

**mcpservers.org `/all`:** Kinoify (media generation utility), Bond (Discord MCP; communication saturation), Buildix Hyperliquid Orderflow (crypto liquidation data), Momentra (agent identity with a trial allowance; agent infra class), Search Fragments (search-answer utility; saturated web-search class), OneFindMe (AliExpress shopping search; consumer retail class), QRSalt (QR code generator; commodity utility), OperatorNest (local stdio tooling; dev utility class). The remainder of the three pages resolved to prior-sweep dispositions, non-English marketing pages and username-fragment 404 shells.

## Notes

- The mcpservers.org `/all` page 1 was **zero-churn** at roughly a two-hour gap from the morning sweep; pages 2 and 3 carried the fresh slugs. This matches the established pattern that same-day short-gap sweeps should treat `/all` page 1 as a cross-check and look deeper for turnover.
- The mcp.so feed's entire top block (PredictionMarketsPicks, Sooveryn, SocialAPIs, Zyte, AgentGrid.io, Builders in Fintech, FlatHunt, TATUAT.RO, Manifold, Common Paper, PixelDojo, Aayat AI) was prior dispositions from the October 1 through October 3 morning ledgers.
- Two candidates with zero catalog hits were assessed and rejected on class: Casefile (agent memory, already covered) and Muumuu Domain (regional consumer domain registrar).

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the curated catalog
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - all sweep reports
