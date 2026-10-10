---
title: "MCP Server Discovery - October 10, 2026 (Night Sweep)"
description: "Night sweep cataloguing eBay sold-listing data for pricing research, with a zero-delta canonical check and the fresh issue-window dispositions."
last_updated: 2026-10-10
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october10-2026-night/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 10, 2026 (Night Sweep)

Night sweep over the mcp.so `/feed` (30 server links via the direct TanStack fetch), mcpservers.org `/all` pages 1-3 through the r.jina.ai reader proxy (the fresh cohort diffed against the October 9 r96 canonical capture of 15,042 server URLs, and a fresh twelve-sitemap refresh, r97, confirming zero additions and zero removals), and the fresh chatmcp/mcpso issue window #5066-#5074, with vendor docs and live endpoint probes for every candidate. One new business-relevant entry, catalogued with a guide: eBay sold and active listing data for pricing and product research.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [SoldFetch MCP](/hermes/mcp/servers/external/soldfetch-mcp/) | Commerce & E-Commerce | eBay sold and active listing data as three tools - keyword search with price and condition filters, category browsing and item details across eight eBay sites, for comps, pricing and product research |

## Sources

- mcp.so /feed (30 server links, direct TanStack fetch; every block cross-checked against the newest sweep sections)
- mcpservers.org /all pages 1-3 via the r.jina.ai reader proxy (90 slugs, every one inside the r96 set; the twelve-sitemap canonical refresh r97 came back zero additions and zero removals)
- chatmcp/mcpso issues #5066-#5074 (fresh window since the evening cutoff at #5065)
- Vendor docs and live endpoint probes for every candidate (SoldFetch: unauthenticated initialize returns 401 "Unauthorized"; the public server card matches `tools/list`; docs live at docs.soldfetch.com)

## Also Identified (Not Catalogued)

On the mcp.so feed, the only fresh entry beyond the prior dispositions was Lochless (a hosted text index for LLM apps and agents; search-infra utility class per the takibi-base and Search & Trends holds); the rest of the 30-block feed was repeats or prior dispositions from the October 3-9 ledgers (DeFade, Nullprint, Kinetune, UXMachine, CompanyData, BoardMark, UXKIN, Onsomble, Shipfound, Takibi Base, TRMNL, nittim, FeedShine, FUSE Health, Shopify SEO Expert, Aisle, MarginPad, CovaSyn, Priors, Multi Upload Tool, Rumoro, iDevice Buyer's Guide, Rivalize, EximAgent, Optimus MCP, Clipping Alpha, 3GPP Scout, MilliGate and the rest).

On mcpservers.org, the canonical refresh across the twelve sitemaps came back byte-stable against the r96 capture - 15,042 server URLs, zero additions, zero removals - and the /all pages 1-3 sample resolved entirely inside the r96 set: every sample member carries a prior disposition from the October 6-9 ledgers, including the evening sweep's full 126-cohort ledger and its class-group remainder.

From the fresh chatmcp/mcpso issue window #5066-#5074: SoldFetch catalogued above; evaluated and held - exit1.dev (uptime monitoring with HTTP, TCP, UDP, WebSocket and ICMP monitors, status pages and email and webhook alerts; the uptime class is covered by the catalogued HostTracker, RealUptime, APIzone, Drumbeats and pingcheck entries - the closest call of the cycle), Varosity (60+ generative media models behind one key; aggregator class per PZERO and Superpowers, media-generation class per bitHuman), ELDRICK (golf club fitting trained on 100,000+ fittings; consumer sports class), netatmo-energy-mcp (smart-home thermostats and radiator valves; consumer home class per the Homey bridge disposition), Jet Browser (a bounded WPE WebKit runtime verifier; dev-testing utility class), remove-ai-label (AI-label and metadata inspection and removal for image and video files; media utility class), Loker Dollar Jobs (worldwide remote jobs with USD pay; jobs-data class covered per Worklittle, Jobyap and Level) and munche-meo (a Korean writing-style checker with a style-guide RAG mode; regional language utility).

## Result

Catalog moved from 889 servers (+775 guides) to 890 servers (+776 guides).
