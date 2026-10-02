---
title: "MCP Server Discovery - October 2, 2026 (Evening Sweep)"
description: "Evening MCP ecosystem sweep: 1 new business-relevant server catalogued, a bookkeeping ledger with financial reporting for agents."
last_updated: 2026-10-02
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october2-2026-evening"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 2, 2026 (Evening Sweep)

Evening sweep over the mcp.so feed (29 server blocks) and mcpservers.org `/all` (30 slugs), both fetched through the r.jina.ai reader proxy. The direct mcp.so fetch now returns only the Cloudflare/JS shell with no server data in the initial HTML, so the reader proxy carried the feed as well as the directory listing. Feed-order recency against the October 2 morning anchor turned up no genuinely new mcp.so entry; the one new business-relevant server came from the mcpservers.org `/all` surface.

## New Servers Catalogued

### SuperBooks MCP - Bookkeeping and Financial Reports for Agents

A company's accounting ledger behind one MCP endpoint. SuperBooks exposes bank transactions, invoices, customers, time-tracking projects, documents, receipts and categories, alongside a reporting layer that answers revenue, profit and loss, burn rate, runway and spending questions. Access is scoped by credential, so a read-only key can read the books without any ability to change them.

- Endpoint: `https://api.superbooks.io/mcp` (remote Streamable HTTP)
- Auth: OAuth (PKCE with dynamic client registration) or an API key minted in the app
- Surface: Code Mode, where `tools/list` returns `search_tools` and `execute_typescript`, reaching 45 backend tools across 12 domains plus `list_teams`
- Rate limit: 120 requests per minute, counted per credential
- Safety: the eight destructive tools need the `apis.all` scope plus the team's **Destructive AI tools** setting

Operator relevance: most finance MCP servers stop at one data source, whereas SuperBooks is the ledger itself, so an agent reads the same numbers the accountant sees. The eight report tools covering revenue, profit and loss, burn rate and runway are the numbers that drive hiring, pricing and fundraising, and they sit next to the transactions and invoices that produce them rather than in a separate analytics tool.

[Read the full guide](/hermes/mcp/servers/external/superbooks-mcp/)

## Identified But Not Catalogued

The full mcp.so feed this cycle was prior dispositions, checked against the sweep index and the `servers/external/index.md` ledger:

- **esimoa** - travel eSIM comparison, remote MCP at api.esimoa.com; consumer travel class.
- **BulkTranscripts** - YouTube transcripts plus channel and playlist listings; media utility class.
- **allcams.fm** - live webcam rooms across five platforms, tagged 18+; consumer class.
- **SayLive** - publishes static sites from a conversation; dev publishing class.
- **Sooveryn** - AI personas with project memory for coding agents; agent-memory class.
- **IBM Engineering Lifecycle Management MCP** - REQUISIS-hosted ALM connector at elm-connector.com; enterprise ALM class outside the connector catalog.
- **SocialAPIs** - catalogued in the October 2 morning sweep.
- **gtm-api** - LinkedIn MCP, catalogued July 28 as linkedin-mcp-gtm.
- **Stele** - shared memory for coding agents; agent-memory class.
- **Daski** - remote MCP at daski.io with a one-line description; thin docs.
- **Generate Greetings** - personalized greeting cards; consumer utility.
- **Desearch** - AI, X and web search with page extraction; saturated web-search class.
- AgentGrid.io, MCP DB Wizard, Zyte, FlatHunt, TATUAT.RO, Porkbun, PixelDojo, Aayat AI, Povver, uplika, prodready, oceanalt-aml-mcp, MemeSwap MCP, Genchi, Manifold MCP and Common Paper Contracts - all catalogued or disposed in the October 1 and September 30 sweeps.

On the mcpservers.org `/all` surface, **FlyBest** (luxury hotel booking, consumer travel class, disposed October 1 evening) re-surfaced, and the remaining slugs (upstream-mcp, outcomeci-mcp, daski-mcp, www-honestelf-com-docs-mcp, medianfi-com-claude-cowork, bestax, proposal-biz, resolvedmarkets, worthbase, coldleads, heyhermann, blastak, india-jobs, clino, 8b-com, sekkeiflow, bioflow, dodomain, usetyton, notifly, upapi, plus the non-server username fragments the parser picks up from the listing) resolved to prior-sweep dispositions.

## Notes On Prior Dispositions

The morning sweep's catalogued entry, SocialAPIs, and its held list (esimoa, BulkTranscripts, allcams.fm, SayLive, Sooveryn, IBM ELM, Generate Greetings, Desearch, Daski, Stele) all re-surfaced at the top of the feed and were re-confirmed as prior dispositions rather than treated as new. gtm-api, which appears mid-feed, is the LinkedIn MCP catalogued on July 28 under its feed alias, and Stele is the shared-memory server repeatedly disposed in the agent-memory class.

## Catalog Totals

775 servers (+661 guides) after this sweep.
