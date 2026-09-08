---
title: "MCP Server Discovery - September 8, 2026 (Evening Sweep)"
description: "Evening sweep over the mcp.so feed (30 server blocks) and mcpservers.org /all page 1 via the r.jina.ai reader proxy. 2 new business-relevant servers catalogued with guides across domain intelligence and agent-native SEO research."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-08
---

# MCP Server Discovery - September 8, 2026 (Evening Sweep)

**Source:** mcp.so feed (30 server blocks, TanStack Router $R-stream), mcpservers.org /all page 1 (r.jina.ai reader proxy; direct curl Cloudflare-challenged)
**Method:** feed $R-block parsing, /all page 1 slug extraction, mcp.so detail pages (direct curl with browser UA), JSON-RPC liveness probes (initialize, tools/list), vendor docs and well-known manifests
**Date:** September 8, 2026 ~18:00-18:40 UTC

## Summary

| Metric | Count |
|---|---|
| mcp.so feed blocks above prior boundary | 2 (varynforge, expired-domains-mcp-karma-domains) |
| mcpservers.org /all page 1 | 30 entries (all classified; 0 new) |
| Detail pages fetched | 2 (mcp.so x2) |
| Endpoints probed | 3 (karma initialize x402 response + health ok, varynforge initialize + 57-tool discovery) |
| New servers catalogued | 2 |
| Integration guides written | 2 |
| Skipped (not catalogued) | feed repeats already catalogued/disposed + page-1 slugs unchanged from morning sweep |

## New Business-Relevant Servers (2 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| Expired Domains MCP (Karma.Domains) | expired-domains-mcp | Domain intelligence for SEO operators and investors | initialize returns x402 payment_required with USDC pack offers (Base + Solana); /health ok; well-known manifest v2.4.0; vendor docs list 31 tools |
| VarynForge MCP | varynforge-mcp | Agent-native SEO research and briefing | initialize ok (serverInfo v1.21.0); tools/list public with 57 tools; tools/call returns OAuth 2.1 protected-resource metadata (RS256) |

## Findings

- **Karma.Domains MCP**: hosted at mcp.karma.domains/mcp. 31 tools across reports, account, workflow and 13 live checkers (WHOIS, DNS, Moz backlinks/anchors/spam, SimilarWeb traffic, archive age). Pro plan required; OAuth or Bearer API key; 60 req/min shared rate limit; live checks 1 credit each; SEO enrich 3-22 credits; x402 USDC agent packs $1.50/100, $6/500, $20/2000. Repo karma-domains/expired-domains-mcp (MIT, 0 stars, created Sep 7).
- **VarynForge MCP**: hosted at app.varynforge.com/api/mcp. 57 tools covering projects, competitor tracking, credit-gated research runs, opportunity clusters, keywords and page dossiers, per-channel briefs (article, X, LinkedIn, Reels, YouTube), draft linting, published-article ledger and a 30-day market radar. OAuth 2.1 with dynamic client registration; free tier for project creation, niche analysis and sitemap mapping. The mcp.so listing tagline still reads as flight search - stale copy; the live endpoint serves the SEO research platform (marketing site: varynforge.com, "Agent-Native SEO Research").
- **GitHub API pass skipped**: the search endpoint returned 422 ("User flagged as spammy") on the topic:mcp pushed:2026-09-08 query. Primary sources (feed + /all page 1) were complete, so no loss of coverage.

## Non-Catalogued (Disposed or Repeats)

- **mcpservers.org /all page 1**: all 30 slugs unchanged from the morning sweep - 404 shells (cartonpliant, rakutentech, maxweb4u, author slugs georgi-petkov, kolganovr, oscardvs, xkallex, zsadigzade) and previously ruled families (Datapika, Advisors AI, Memra, MCP ADMIN, Ergonia Works, Rendi, SnipperApp, FrameThrower, Carpedia, Wellness Project, BagIQ, Capawesome, Convert3D, marketcode, export-tools = Export Poe Chats).
- **mcp.so feed repeats**: Mailercloud (both slugs), InstantClips, JsonCut, Fundz, Countersignatory, Fruit Stand, Beamtrace, LoomaScale, Velarion Company Intelligence (all catalogued) plus previously disposed listings (dxpert UNS, GoBuy, Create Prints, Tessryx, Saaskly, PostNitro, Yocoolab, TrueClicks, YouSpot, VeriRoute, DB Planner, Dealwize, PriceMyRepair, Factanker, miniOrange, agent.social, studiofromthesea, Alien Probe).

## Actions Taken

- 2 integration guides written (expired-domains-mcp, varynforge-mcp), validator 2/2 PASS.
- Index updated: last-updated line (590 servers, +476 guides), evening sweep section, docs-links tail block.
- Frontmatter gate: python3 scripts/validate_frontmatter.py green.
- Pushed to main; remote hash verified; Mac Mini resynced.
