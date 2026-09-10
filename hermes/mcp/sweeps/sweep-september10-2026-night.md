---
title: "MCP Server Discovery - September 10, 2026 (Night Sweep)"
description: "Night sweep over chatmcp/mcpso issues #3999-#4031, mcp.so homepage recentServers and mcpservers.org /all pages 1-2. 6 new business-relevant servers catalogued with guides: mcp-x (official X API v2), Shop MCP (read-only Shopify), WaitingForPower (US energy permitting), Mellow Hub (multi-network publishing), Parlel (keyless professional network search) and Capslane (timestamped YouTube transcripts)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-10
---

# MCP Server Discovery - September 10, 2026 (Night Sweep)

**Source:** chatmcp/mcpso issues #3999-#4031 (30 fetched, fresh window past the Sep 9 night cutoff), mcp.so homepage recentServers (8 blocks), mcpservers.org /all pages 1-2 (60 slugs via r.jina.ai reader proxy)
**Method:** issue-body enrichment, feed $R-block parsing, /all slug extraction + detail-page fetch, live JSON-RPC probes, repo/PyPI/npm verification
**Date:** September 10, 2026 ~03:10 MST (10:10 UTC)

## Summary

| Metric | Count |
|---|---|
| mcp.so issues evaluated | 30 (#3999-#4031) |
| mcp.so homepage recentServers blocks | 8 (all prior dispositions) |
| mcpservers.org /all slugs cross-ref'd | 60 |
| Detail pages fetched | 30 |
| Live JSON-RPC probes | 4 endpoints (2 keyless captured with tools/list, 2 key-challenged = liveness) |
| New servers catalogued | 6 |
| Integration guides written | 6 |
| Skipped (not catalogued) | 45+ |

## New Business-Relevant Servers (6 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| mcp-x MCP | mcp-x | Official X API v2 as 42 Go tools, OAuth 1.0a user context | issue #4031 + repo Role1776/mcp-x (1 star, MIT, created Sep 9) + README tool extraction (42 x_* names) + Official Registry io.github.Role1776/mcp-x 0.1.1 active |
| Shop MCP | shop-mcp | Read-only Shopify catalogue and stock, stdlib-only single file | issue #4030 + PyPI shop-mcp 1.0.1 + repo hello532/shop-mcp (MIT, created Sep 7) + glama scored A/A/B |
| WaitingForPower MCP | waitingforpower-mcp | US energy permitting tracker, keyless remote | issue #4011 + LIVE PROBE (v1.0.0, keyless, 6 tools captured) + repo briandgoldberg/WaitingForPower (MIT) |
| Mellow Hub MCP | mellow-hub-mcp | Multi-network social publishing, 9 networks, scoped keys | /all detail page (full 12-tool docs) + LIVE PROBE (key challenge = liveness) + endpoint www.mellow.world/mcp |
| Parlel MCP | parlel-mcp | Keyless professional network search (people/companies/jobs/agents) | /all detail page + LIVE PROBE (v1.0.0, keyless, 8 tools captured) + endpoint api.parlel.com/mcp |
| Capslane MCP | capslane-mcp | Timestamped YouTube transcripts | /all detail page (3 tools, full install matrix) + LIVE PROBE (key challenge = liveness) + npm @webba_tech/capslane-mcp 0.1.8 (MIT) + repo Webba-Creative-Technologies/capslane-mcp (1 star) |

## Findings

- **mcp-x**: the official X API v2 instead of cookie-driven browser automation. 42 tools across posts (read/write), search with full operator support, users, lists (14 tools), bookmarks and media upload. Destructive hints on all writes, readOnly hints on reads, cost-guard design (x_posts_count sizes topics without post-read spend, batched lookups, manual pagination). Refuses to start without valid credentials; detects the read-only token trap at startup. Category: Social Media Management.
- **Shop MCP**: four read-only tools (search_products, get_product, check_inventory, low_stock_report) over read_products + read_inventory scopes only. One stdlib-only Python file - the whole surface can be read before it is run. Completes the MCP handshake without credentials and only fails on tools/call. Category: Commerce & E-Commerce.
- **WaitingForPower**: keyless remote MCP over the WaitingForPower dataset - 41 state utility/siting commissions plus EIA, LBNL, ORNL and the Federal Permitting Dashboard, normalized into cited project records (stage, delay cause, wait duration). 6 tools live-probed. Category: Data & Analytics.
- **Mellow Hub**: one API call publishes to Instagram, TikTok, YouTube, X, LinkedIn, Threads, Bluesky, Pinterest and Facebook with per-channel validate_post/preview_post, required idempotency keys, per-key grants (autopilot vs review mode, channel scopes, daily quotas) and per-channel outcome reporting (partial failures named). Category: Social Media Management.
- **Parlel**: anonymous free JSON API over a professional network - search_jobs (comp/seniority/remote filters), search_companies (industry/size/hiring), search_people (skill tags), search_agents. Stable URLs for closed roles, contact details never exposed. Category: Business Operations.
- **Capslane**: YouTube transcripts with millisecond timestamps, native/auto/generate modes, job-based polling that fits interactive assistants, workspace allowance billing (status checks free). Remote endpoint + npm + Claude Code plugin marketplace. Category: Content & Research.

## Non-Catalogued (Disposed or Repeats)

- **MCPREADY #4029**: MCP-server correctness gate with HMAC-signed receipts - submission repo unempyd/mcpready returns GitHub 404, artifact unverifiable. Skip.
- **CCS MCP #4020**: already disposed by a prior sweep (local security runtime verification, dev tool).
- **Atako #4019** (agent-platform management - agent infra), **Arkon Vault #4022** (agent continuity vault - agent memory class, Kontexta precedent), **Caliu Notes #4018** (personal-library class), **Keyban #4015** (x402 wallet class, IMBA precedent), **dex-data #4021** (crypto class), **mumo #4005** (multi-model deliberation - agent infra).
- **Consumer**: SavingsLast #4007 (retirement calculators), Movie Planner #4017, LiftTrack, Telegram Calendar, Forge UI (Roblox creator utility).
- **Dev utility class**: sift #4010, 3D Visualizer #4009, schema-bridge #4026, mcp-context-condenser #4025, mcp-smart-git #4024, mcp-doctor #4027, AI Developer MCP Pro Suite #4028 (paid Gumroad bundle), juudd #4006, Veriton #3999, Shiplight (coding-agent browser testing), Idle9 (persistent agent computer - agent infra).
- **Geo-niche**: ead-factory #4013 (Spanish legal-evidence), Aikstockdata (Korean), RuSender + Htmlkin (Russian).
- **Thin docs**: SHAR Production Metadata #4014/#4003 (empty issue body + shell detail page), UK Legislation Changes (no tool list published), Business Verify API (personal docs host, no registry record).
- **Desktop utility**: Plugsight #4002 (macOS USB device monitor).
- **/all nav-only shells (~1900 bytes)**: aceatdev, sadri-dridi, pennyforgeorg, abstractglitch, themsquared, gotchseo, kleinicke, fitsociety, novalyth, gopisrikrishna, hexahedral-inc, peeroren, adsroid.
- **Prior dispositions on /all pages 1-2**: Magic Cloud (hyperlambda), OmniDome (humanmirror), plus the Sep 9 night sweep's catalogued and disposed set still occupying page 1.
- **mcp.so homepage recentServers repeats**: Orthogonal, toll402, Loadster, priostack, pulse-verity, dxpert UNS, GoBuy, Yocoolab - all prior dispositions.

## Notes

- Repo frontmatter fixes bundled: 3 skills-catalog pages from the sibling skills sweep (codebase-design-setup, impeccable-design-polish-setup, resolving-merge-conflicts-setup) had unquoted descriptions with ': ' that failed the repo validate_frontmatter.py gate - quoted, gate green (4,110 files scanned).
- Honcho MCP tools unavailable in this cron session (tool registry miss) - handoff written to GBrain + skill ledger instead.
