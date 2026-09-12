---
title: "MCP Server Discovery - September 12, 2026 (Morning Sweep)"
description: "Morning sweep over the mcp.so feed (30 server blocks) and mcpservers.org /all page 1 via the r.jina.ai reader proxy. 2 new business-relevant servers catalogued with guides, both endpoints live-verified: Pixelesq MCP (official website management, 62 tools, OAuth 2.1 PKCE) and LandLens One MCP (Tamil Nadu property due diligence with cited legal answers). Also fixed two unquoted source values from the Sep 11 evening sweep."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-12
---

# MCP Server Discovery - September 12, 2026 (Morning Sweep)

**Source:** mcp.so feed (30 server blocks, TanStack Router $R-stream), mcpservers.org /all page 1 (r.jina.ai reader proxy; direct curl Cloudflare-challenged), chatmcp/mcpso issues #4080-#4082
**Method:** feed $R-block parsing, /all slug extraction + detail-page fetch via proxy, vendor docs fetch, JSON-RPC liveness probes (initialize)
**Date:** September 12, 2026 ~03:00 MST (10:00 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 30 (mcp.so) |
| /all slugs batch-classified | 26 (page 1, r.jina.ai) |
| GitHub issues reviewed | 3 (#4080-#4082) |
| Detail pages fetched | 8 |
| Endpoints live-probed | 2 (both 401 auth-gated as documented) |
| New business-relevant servers | 2 |
| Integration guides written | 2 |

## New Business-Relevant Servers

| Server | Category | Why it matters | Endpoint |
|---|---|---|---|
| Pixelesq MCP | Business Operations | Official MCP for Pixelesq websites: pages, sections, collections, SEO metadata, Search Console, analytics, redirects, theme - all draft-first | https://mcp.pixelesq.app/mcp (OAuth 2.1 PKCE, 62 tools) |
| LandLens One MCP | Real Estate Data | Tamil Nadu property due diligence: cited legal answers, 30-check verification, 25 years of registered prices, build scope, change tracking | https://verified.realestate/mcp (API key / OAuth) |

## Skipped (Not Catalogued)

- SlateVM MCP: Apple-silicon VM platform, 45 tools - local macOS app over a Unix socket; desktop-utility class.
- MatPlotLibNet: local .NET chart rendering - dev tool class.
- failecho, loudreader slugs: detail pages 404 - listing shells.
- EU AI Act Compliance (#4081): submission lists no tools, repo unverifiable - thin-docs class.
- Errand (#4082): Seoul geo-niche errand dispatch service.
- requisition-audit (#4080): a2awire benchmark fixture - benchmark infra class.
- Prior-sweep dispositions respected: Briefing Service (media-news class), Open Task Relay (task-marketplace class), both disposed in the Sep 11 evening sweep.

## Actions Taken

1. Wrote 2 integration guides (pixelesq-mcp, landlens-one-mcp) following the recordwire guide shape.
2. Live-probed both endpoints over JSON-RPC initialize: Pixelesq returned 401 with OAuth protected-resource metadata and exact scopes; LandLens returned 401 with bearer realm LandLens and protected-resource metadata.
3. Updated catalog index.md (last-updated line, top sweep section, docs-links tail block). Catalog now 648 servers (+534 guides).
4. Fixed two unquoted source values from the Sep 11 evening sweep (recordwire-mcp, clauseai-mcp) flagged by the repo frontmatter gate.
5. Stamped .last-sweep and committed the sweep to corpusiq-docs main.
