---
title: "MCP Server Discovery - October 11, 2026 (Night Sweep)"
description: "Night sweep cataloguing Automattic's official WordPress.com MCP server and a manufacturing capability graph with instant quotes."
last_updated: 2026-10-24
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october11-2026-night/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 11, 2026 (Night Sweep)

Night sweep over the mcp.so `/feed` (30 server links via the direct TanStack fetch), mcpservers.org `/all` pages 1-5 through the r.jina.ai reader proxy (149 slugs, zero fresh against the October 10 r101 canonical capture), a fresh twelve-sitemap canonical refresh (r102: 15,142 URLs, zero additions and zero removals after locale-prefix auto-stripping), and the fresh chatmcp/mcpso issue window #5109-#5117, with vendor docs and live endpoint probes for every candidate. Two new business-relevant entries, each catalogued with a guide: Automattic's official WordPress.com MCP server, and a manufacturing capability graph with materials, processes, tolerances and instant quotes.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [WordPress.com MCP](/hermes/mcp/servers/external/wordpress-com-mcp/) | Business Operations | The official Automattic server for WordPress.com: one OAuth connection reaches every site on the account and 60+ abilities cover posts, pages, comments, media, stats, plugins, collaborators, backups, scans and site structure; every write requires explicit confirmation and some deletes are permanent by design |
| [MechanoFab MCP](/hermes/mcp/servers/external/mechanofab-mcp/) | Manufacturing & Industrial | A manufacturing capability graph for agents: 20 keyless engineering tools across material search, comparison and equivalents, compliance checks, process specs, equipment matching, ISO 2768 tolerances, industry requirements, part mass and `quote_calc` for instant 3D printing prices |

## Sources

- mcp.so /feed (30 server links, direct TanStack fetch; fresh items this cycle: WordPress.com catalogued above and Kourier held on class; every other block cross-checked against the October 3-10 ledgers as a repeat or prior disposition)
- mcpservers.org /all pages 1-5 via the r.jina.ai reader proxy (149 slugs; the sample resolved entirely inside the October 10 r101 canonical capture - zero fresh)
- Twelve-sitemap canonical refresh (r102): byte-stable at 15,142 normalized server URLs, zero additions and zero removals, after locale-prefix auto-stripping (`de`, `es`, `fr`, `hi`, `id`, `ja`, `ko`, `pt-BR`, `ru`, `th`, `tr`, `vi`, `zh-CN`, `zh-TW`) and `%23` fragment normalization; artifact `mcpservers_canonical_20261011_r102.txt`
- chatmcp/mcpso issues #5109-#5117 (9 fresh submissions since the evening cutoff at #5108)
- Vendor docs and live endpoint probes for every candidate (WordPress.com: POST initialize returns 401 with OAuth protected-resource metadata; MechanoFab: keyless initialize returns 200, `mechanofab-mcp-server` v0.1.0, and `tools/list` returns all 20 tools; Kourier: keyless initialize returns 200 as `kourier-info` v1.0.0 - every hold was classification-based)

## Also Identified (Not Catalogued)

**mcp.so feed:** the fresh entry beside the catalogued one was Kourier (flat-rate hosted DeepSeek inference discovery and onboarding, 7 tools including pricing, model limits, setup instructions and a human-approved checkout flow; held on the inference-plan discovery and provider-onboarding class per the disposed inferenceindexer #4093 and PZERO #3802 entries). Every other block was a repeat or prior disposition from the October 3-10 ledgers (agentpixel, midwest-legal-docs, SlopIt, server-noonien, FlexQueries SEO, Rootz Archive, Lochless, DeFade, Nullprint, Kinetune, UXMachine, CompanyData, BoardMark, Your Move Exercise Video API, UXKIN, Onsomble, Shipfound, Takibi Base, TRMNL, nittim, FeedShine, FUSE Health, Shopify SEO Expert, Aisle, MarginPad, CovaSyn, Priors, Multi Upload Tool and the rest).

**mcpservers.org /all and sitemaps:** pages 1-5 (149 slugs) all resolve inside the r101 canonical set, and the twelve-sitemap refresh was byte-stable - zero additions, zero removals. No new material on this surface this cycle.

**chatmcp/mcpso issue window #5109-#5117:** MechanoFab catalogued above. Held: zima-mcp (plain-SSH load, disk and container checks plus allowlisted container restarts for a ZimaBlade or any Docker host; single-author homelab and host-ops utility, class adjacent to the catalogued HomeLab Monitor) and the pooriaarab US register-directory fleet resubmitted across #5109-#5115 (MarriageLicense.fyi, MemoryCareHomes.fyi, DishDirectory.com, ITINAgents.fyi, PublicAdjusters.fyi, ADHDEvaluations.fyi and MRIPrices.fyi; prior disposition from the October 10 evening sweep, held as class).

## Result

Catalog moved from 896 servers (+782 guides) to 898 servers (+784 guides).
