---
title: "MCP Server Discovery - September 8, 2026 (Morning Sweep)"
description: "Morning sweep over the mcp.so feed (30 server blocks) and mcpservers.org /all page 1 via the r.jina.ai reader proxy. 3 new business-relevant servers catalogued with guides across email marketing, e-commerce short-form video ads and agent video/image authoring."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-08
---

# MCP Server Discovery - September 8, 2026 (Morning Sweep)

**Source:** mcp.so feed (30 server blocks, TanStack Router $R-stream), mcpservers.org /all page 1 (r.jina.ai reader proxy; direct curl Cloudflare-challenged)
**Method:** feed $R-block parsing, /all page 1 slug extraction, detail pages via r.jina.ai (mcp.so author-segment fetch + mcpservers.org), keyless JSON-RPC liveness probes (mailercloud 401), listing-level tool documentation (InstantClips 10-tool detail page)
**Date:** September 8, 2026 ~09:30-10:15 UTC

## Summary

| Metric | Count |
|---|---|
| mcp.so feed fresh blocks above prior boundary | 3 (mailercloud x2, instantclips) |
| mcpservers.org /all page 1 | 30 entries (all classified; 1 new) |
| Detail pages fetched | 4 (mcp.so x2, mcpservers x1, vendor docs x1) |
| Endpoints probed | 1 (mailercloud 401 liveness) |
| New servers catalogued | 3 |
| Integration guides written | 3 |
| Skipped (not catalogued) | 1 dup slug + 8 404-shell page-1 slugs + page-1 repeats already disposed |

## New Business-Relevant Servers (3 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| Mailercloud MCP | mailercloud-mcp | Email marketing platform operations | mcp.so Verified + Featured; endpoint mcp.mailercloud.com/mcp probe-verified live (HTTP 401 on initialize = API-key gated) |
| InstantClips MCP | instantclips-mcp | E-commerce short-form video ads | mcp.so detail page carried full 10-tool documentation with brand-decision guardrails; OAuth 2.1 at app.instantclips.ai/mcp; repo InstantStudioAI/instantclips-mcp |
| JsonCut MCP | jsoncut-mcp | Video/image authoring for agents | mcpservers.org detail (published Sep 7 22:41Z) documented jsoncut_v2_* authoring loop, upload tickets, review frames; X-API-Key auth at mcp.jsoncut.com/mcp |

## Skipped (not catalogued)

- Mailercloud second listing (mailercloud-ab7bcd) - duplicate slug of the same product with a thin tagline-only entry; one guide covers both listings
- dxpert UNS tools - feed re-check, industrial IoT namespace validation, disposed Sep 7 evening
- mcpservers.org /all page-1 404 shells: cartonpliant, rakutentech, maxweb4u and author-slug pages (georgi-petkov, kolganovr, oscardvs, xkallex, zsadigzade) - generic "Awesome MCP Servers" 404 shell on detail fetch, not valid listings
- Page-1 repeats already ruled by the Sep 7 evening sweep: Datapika family (4 slugs), Advisors AI, GoBuy, Memra, MCP ADMIN, and the evening sweep's other 22 dispositions
- Feed repeats already catalogued (Fundz, Countersignatory, Fruit Stand, Beamtrace, LoomaScale) or already disposed by prior sweeps (GoBuy, Create Prints, Tessryx, Saaskly, PostNitro, Yocoolab, TrueClicks, YouSpot, VeriRoute, DB Planner, Dealwize, PriceMyRepair, Factanker, miniOrange, Nizh, Lawstronaut, agent.social, studiofromthesea, Alien Probe)

## Actions Taken

- 3 guides written to hermes/mcp/servers/external/<slug>/index.md
- Index updated: last-updated line (588 servers, +474 guides), top morning sweep section, tail block entry
- `.last-sweep` stamped (hermes/mcp/.last-sweep)
- validate-guides script 3/3 PASS; repo validate_frontmatter.py green (4,012 files)
