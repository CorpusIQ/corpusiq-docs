---
title: "MCP Server Discovery - September 8, 2026 (Night Sweep)"
description: "Night sweep over the mcp.so feed (30 server blocks) and mcpservers.org /all page 1 via the r.jina.ai reader proxy. 1 new business-relevant server catalogued with a guide: Fluenta MCP, hosted idea validation with Launch Readiness Scores."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-08
---

# MCP Server Discovery - September 8, 2026 (Night Sweep)

**Source:** mcp.so feed (30 server blocks, TanStack Router $R-stream), mcpservers.org /all page 1 (r.jina.ai reader proxy; direct curl Cloudflare-challenged)
**Method:** feed $R-block parsing, /all page 1 slug extraction, mcp.so detail page via r.jina.ai proxy, vendor docs fetch, JSON-RPC liveness probe (initialize)
**Date:** September 8, 2026 ~19:00 MST (02:00 UTC Sep 9)

## Summary

| Metric | Count |
|---|---|
| mcp.so feed server blocks | 29 |
| mcpservers.org /all page 1 | 30 entries (all classified; 0 new) |
| Detail pages fetched | 1 (mcp.so fluenta via r.jina.ai) |
| Endpoints probed | 1 (fluenta initialize 401 bearer-key challenge) |
| New servers catalogued | 1 |
| Integration guides written | 1 |
| Skipped (not catalogued) | feed repeats already catalogued/disposed + page-1 slugs unchanged from evening sweep |

## New Business-Relevant Servers (1 guide)

| Server | Slug | Class | Verification |
|---|---|---|---|
| Fluenta MCP | fluenta-mcp | Business idea validation with Launch Readiness Scores (LRS) | initialize probe returns HTTP 401 with www-authenticate Bearer realm="Fluenta Public API" and OpenAPI resource_metadata; vendor docs list 14 tools, scopes and error semantics |

## Findings

- **Fluenta MCP**: hosted at fluenta.space/backend/api/v1/mcp (Streamable HTTP, JSON-RPC 2.0). Scores business ideas on six live market signals (demand, pain, competition, monetisation, timing, distribution) into a Launch Readiness Score (LRS). Free sandbox X-Ray (no credits, no writes), full X-Ray at 2,000 credits with a read_write key (xray_submitted while queued, xray_result when complete), plus scored-ideas search, compare, collections, pipeline bookmarks, reports, account and usage tools. Free tier carries 2,000 credits (one full X-Ray plus unlimited reads); Premier plan beyond that. Keys never expire until revoked. Errors: 401 bad key, 402 out of credits, 403 wrong scope, 429 rate limited with Retry-After. Docs at fluenta.space/docs/api-and-mcp; OpenAPI at /backend/api/v1/ext/openapi.json (public, no key). Author: Fluenta Tech LLC, submitted by Oleg Ivanov; Verified + Featured on mcp.so, categoryName Productivity. Category assigned: Data & Analytics (ddmarketer-mcp precedent - validated SaaS opportunity intelligence).
- **GitHub API pass skipped**: prior same-day sweeps hit the 422 "User flagged as spammy" wall; primary sources (feed + /all page 1) were complete, so no loss of coverage.

## Non-Catalogued (Disposed or Repeats)

- **mcpservers.org /all page 1**: all 30 slugs unchanged from the evening sweep - previously ruled families (Datapika, Advisors AI, Memra, MCP ADMIN, Ergonia Works, Rendi, SnipperApp, FrameThrower, Carpedia, Wellness Project, BagIQ, Capawesome, Convert3D, marketcode, export-tools = Export Poe Chats) plus 404 shells (cartonpliant, rakutentech, maxweb4u, author slugs georgi-petkov, kolganovr, oscardvs, xkallex, zsadigzade), plus already-catalogued JsonCut, Formdall and Treza listings.
- **mcp.so feed repeats**: already catalogued (Expired Domains Karma, VarynForge, Mailercloud both slugs, InstantClips, JsonCut, Fundz, Countersignatory, Fruit Stand, Beamtrace, LoomaScale, Velarion, PostNitro, Yocoolab, TrueClicks) or previously disposed (agent.social, Alien Probe, Create Prints, Tessryx, Saaskly, YouSpot, VeriRoute, DB Planner, Dealwize, PriceMyRepair, Factanker, miniOrange, dxpert UNS, Onymu, studiofromthesea, GoBuy).

## Actions Taken

- 1 integration guide written (fluenta-mcp), validator PASS.
- Index updated: last-updated line (591 servers, +477 guides), night sweep section, docs-links tail block.
- Frontmatter gate: python3 scripts/validate_frontmatter.py green.
- Pushed to main; remote hash verified; Mac Mini resynced.
