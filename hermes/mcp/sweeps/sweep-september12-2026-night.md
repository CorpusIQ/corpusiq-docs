---
title: "MCP Server Discovery - September 12, 2026 (Night Sweep)"
description: "Night sweep over the mcp.so feed (30 server blocks, 2 fresh names past the midday cutoff), mcp.so homepage recentServers (8 blocks, all repeats), a fresh mcpservers.org /all page-1 crawl (00:05 UTC) via the r.jina.ai reader proxy and chatmcp/mcpso issues #4087-#4089. 7 new business-relevant servers catalogued with guides: Attensira MCP (AI-search visibility, 33 tools), StayingAPI MCP (cross-OTA accommodation data, 7 tools), stocks.team MCP (point-in-time SEC facts, 47 operations), 0xinsider MCP (Polymarket trader analytics, 57 operations), aiworker-data MCP (x402 pay-per-call data, 20 tools live-probed), moysklad-mcp-ru (MoySklad ERP, 32 tools) and upCampo MCP (farm management, permission-mapped)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-12
---

# MCP Server Discovery - September 12, 2026 (Night Sweep)

**Source:** mcp.so feed (30 server blocks), mcp.so homepage recentServers (8 blocks), mcpservers.org /all page 1 via the r.jina.ai reader proxy (fresh 00:05 UTC crawl, 30 entries), chatmcp/mcpso issues #4087-#4089
**Method:** feed $R-block parsing, /all slug batch-classification, issue-body review, vendor docs fetch (r.jina.ai + raw .md twins), GitHub API + OpenAPI verification, JSON-RPC live probes
**Date:** September 12, 2026 ~19:00-21:00 MST (Sep 13 02:00-04:00 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 30 (mcp.so) |
| Homepage recentServers | 8 (all repeats) |
| /all page-1 entries classified | 30 (fresh 00:05 UTC crawl) |
| GitHub issues reviewed | 3 (#4087-#4089) |
| Detail pages fetched | 10 |
| OpenAPI contracts fetched | 2 (stocks.team 47 ops, 0xinsider 57 ops) |
| Endpoints live-probed | 2 (DDMarketer re-probe 4 tools, aiworker-data 20 tools) |
| New business-relevant servers | 7 |
| Integration guides written | 7 |

## Core Listing Re-checks

| Directory | Status | Evidence |
|---|---|---|
| mcpservers.org | LISTED | /all page 1 served fresh via r.jina.ai (direct curl still CF-challenged) |
| mcp.so | NOT LISTED (CorpusIQ) | No corpusiq server object in feed/homepage SSR; no resubmit (quarantine holds) |

## New Business-Relevant Servers

| Server | Category | Why it matters | Endpoint |
|---|---|---|---|
| Attensira MCP | SEO | AI-search visibility data with 33 tools across 8 groups - share of voice, prompt and competitor management, automations, receipts with citation timelines; OAuth 2.1 or workspace API key | https://mcp.attensira.com/mcp |
| StayingAPI MCP | Data & Analytics | Cross-OTA accommodation data (Airbnb, Booking.com, Vrbo, Google Hotels) in one schema - 7 read-only tools incl. compare_prices with min/median, OAuth 2.1 PKCE, credit-based | https://mcp.stayingapi.com/mcp |
| stocks.team MCP | Finance | Point-in-time SEC filing facts with provenance - 47 OpenAPI operations, local MCP adapter, paid beta from $9.99/mo | https://stocks.team/api |
| 0xinsider MCP | Finance | Real-time Polymarket trader analytics - 57 operations (trader PnL, whale trades, sharp/smart money flows, insider-radar), remote endpoint + npm stdio | https://api.0xinsider.com/api/v1/mcp |
| aiworker-data MCP | Data & Analytics | x402 pay-per-call data layer - 20 tools live-probed (DeFi yields, Polymarket odds/backtests, token safety, news, HN mentions, claim checks), $0.005-$1 per call | https://aiworker.duckdns.org/mcp |
| moysklad-mcp-ru | ERP | MoySklad Russian ERP - 32 tools over an 892-method JSON API 1.2 catalogue, two-gate write model, uvx stdio, MIT (repo pushed 2026-09-12) | stdio (uvx moysklad-mcp-ru) |
| upCampo MCP | Business Operations | Brazilian farm management - production, rain, pests, work orders, stock, fleet, costs with per-farm permission mapping and confirmed writes | https://mcp.upcampo.com.br/mcp |

## Skipped (Not Catalogued)

- **#4089 Sato Hub** - daily-rebuilt index of onchain agent tooling with Sato Scores; agent-ecosystem infrastructure class (Fomite precedent).
- **#4088 OwnerSpec** - cited home water treatment reference; consumer home-improvement class.
- **#4087 VoyageHacks** - fact-checked travel guides plus booking links; travel consumer class (SimFuse precedent).
- **ux-jobs (feed, fresh past cutoff)** - 4,000+ UX job search; job-board consumer class (Theyond precedent).
- **InvisibleAPI** - social publishing to Instagram and X; MCP endpoint and tool names not yet published in docs - re-check next cycle.
- **WhatsApp Shop Manager** - Shopify/Woo/GMC to WhatsApp sync; no documentation available.
- **Utility/consumer classes from /all page 1:** ezpzfile, universal-host-manager, BackBond, ABAP ADT, agent-canary, Tallybook, yueying, MarkuprPlus, Dasha Compute, Omni Flash, Picmovi, Ninjachat, SayLive, DiscFinder, Quran Majeed.
- **Prior-sweep dispositions respected:** DDMarketer (catalogued Sep 4 - re-probed live this sweep, 4 tools confirmed unchanged), Zambo, moysklad family note resolved (marketplace family covered; moysklad-mcp-ru is the ERP, catalogued separately), CQC Provider / England Works Watch (UK geo-niche family), all feed and homepage repeats from the Sep 10-12 sweeps.

## Actions Taken

1. Wrote 7 integration guides (attensira-mcp, stayingapi-mcp, stocks-team-mcp, 0xinsider-mcp, aiworker-data-mcp, moysklad-mcp-ru, upcampo-mcp) following the ddmarketer guide shape; all 7 PASS the per-guide validator on the first pass.
2. Live-probed 2 endpoints over JSON-RPC: DDMarketer (keyless, 4 tools - confirms the Sep 4 guide) and aiworker-data (keyless initialize + tools/list, 20 tools, server v0.2.0).
3. Fetched 2 OpenAPI contracts (stocks.team: 47 operationIds; 0xinsider: 57 operationIds) for exact tool tables.
4. Verified moysklad repo (MIT, 2 stars, pushed 2026-09-12) and stayingapi manifests (server.json, smithery.yaml, glama.json).
5. Updated catalog index.md (last-updated line, top sweep section, docs-links tail block). Catalog now 659 servers (+545 guides).
6. Frontmatter gate green (4,228 files scanned, all valid).
7. Stamped .last-sweep and committed the sweep to corpusiq-docs main.
