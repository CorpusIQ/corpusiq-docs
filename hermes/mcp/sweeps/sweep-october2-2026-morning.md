---
title: "MCP Server Discovery - October 2, 2026 (Morning Sweep)"
description: "Morning MCP ecosystem sweep: 1 new business-relevant server catalogued, covering Facebook and Instagram data tools for agents."
last_updated: 2026-10-02
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october2-2026-morning"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 2, 2026 (Morning Sweep)

Morning sweep over the mcp.so feed (30 server blocks, direct fetch with a browser user agent using the TanStack `$R[N]` payload pattern) and mcpservers.org `/all` (22 slugs) via the r.jina.ai reader proxy, with detail pages fetched for every candidate. Feed-order recency against the October 1 midday anchor and the `/all` slug set against the prior ledger turned up one genuinely new business-relevant entry.

## New Servers Catalogued

### SocialAPIs MCP - Facebook and Instagram Data for Agents

Facebook and Instagram public data behind a single API key, with no Meta developer app or app review. The server exposes 47 read-only tools covering Facebook pages, posts, comments, groups, the Ads Library, Marketplace, profiles, reels and search, plus Instagram profiles, posts, reels, highlights, audio-based reel lookup and location search.

- Endpoint: `https://mcp.socialapis.io/mcp` (remote Streamable HTTP)
- Local install: `npx -y @socialapis/mcp` with an API key
- Auth: API key as an `Authorization: Bearer` header
- Free tier: 200 calls per month; every tool response carries `creditsCharged` and `creditsRemaining`

The tool list was verified live by posting a keyless `tools/list` request to the endpoint, which returned all 47 tool names and their schemas without authentication. Tool listing works without a key; tool calls require one.

Operator relevance: the Ads Library and Marketplace surfaces are the ones Meta makes hardest to reach programmatically, and they are exactly what competitor ad research, brand monitoring and resale pricing work needs. Competitor ad discovery, page engagement tracking and Marketplace price monitoring all become single tool calls.

[Read the full guide](/hermes/mcp/servers/external/socialapis-mcp/)

## Identified But Not Catalogued

- **esimoa** - travel eSIM comparison, remote MCP at api.esimoa.com; consumer travel class.
- **BulkTranscripts** - YouTube transcripts plus channel and playlist listings; media utility class.
- **allcams.fm** - live webcam rooms across five platforms, tagged 18+; consumer class.
- **SayLive** - publishes static sites from a conversation; dev publishing class, prior disposition.
- **Sooveryn** - AI personas with project memory for coding agents; agent-memory class already covered.
- **IBM Engineering Lifecycle Management MCP** - REQUISIS-hosted ALM connector at elm-connector.com; enterprise ALM class outside the connector catalog.
- **Generate Greetings** - personalized greeting cards in 13 languages; consumer utility.
- **Desearch** - AI, X and web search with page extraction; saturated web-search class.
- **Daski** - remote MCP at daski.io with a one-line description; thin docs.
- **Stele** - shared memory for coding agents; agent-memory class.

## Notes On Prior Dispositions

Manifold MCP and Common Paper Contracts MCP re-surfaced in the ledger prose and in the feed, but both were catalogued on September 30 and are prior dispositions rather than new entries. The same applies to Genchi, PixelDojo, AgentGrid.io, Zyte, FlatHunt, TATUAT.RO, Porkbun, Aayat AI, Povver, uplika, prodready, oceanalt-aml-mcp, MemeSwap MCP and gtm-api, which is the July 28 LinkedIn MCP entry under its feed alias.

Every mcpservers.org `/all` slug this cycle (22) resolved to a prior-sweep disposition, including Median (catalogued September 28), Worthbase and Cold Leads and DoDomain (catalogued September 27 and October 1), and Hermann, upAPI, Notifly, SekkeiFlow, BioFlow and Honest Elf (disposed or catalogued in September sweeps).

## Catalog Totals

774 servers (+660 guides) after this sweep.
