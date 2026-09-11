---
title: "MCP Server Discovery - September 11, 2026 (Night Sweep)"
description: "Night sweep over the mcp.so feed (32 server blocks), mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy and chatmcp/mcpso issues #4055-#4064. 6 new business-relevant servers catalogued with guides, 3 endpoints live-verified over JSON-RPC."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-11
---

# MCP Server Discovery - September 11, 2026 (Night Sweep)

**Source:** mcp.so feed (32 server blocks, curl + regex), mcpservers.org /all pages 1-2 (r.jina.ai reader proxy, 58 slugs batch-classified), chatmcp/mcpso issues #4055-#4064 (fresh window past the Sep 10 late-night cutoff at #4054)
**Method:** GitHub issues API, /all slug extraction via reader proxy, JSON-RPC initialize + tools/list probes
**Date:** September 11, 2026 ~03:00 MST (10:00 UTC)

## Summary

| Metric | Count |
|---|---|
| New GitHub issues evaluated | 10 (#4055-#4064) |
| mcpservers.org /all slugs batch-classified | 58 (pages 1-2) |
| mcp.so feed blocks classified | 32 |
| New servers catalogued | 6 |
| Integration guides written | 6 |
| Skipped (not catalogued) | 36+ new names; 9 prior-sweep dispositions respected |

## New Business-Relevant Servers (6 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| CN Evidence MCP | cn-evidence-mcp | Chinese supplier verification - keyless name resolution plus x402 pay-per-call identity, procurement and regulatory evidence | Live-verified: keyless initialize captured "CN Evidence" v1.30.0 (protocol 2024-11-05) + tools/list returned all 3 schemas; registry dev.workers.mikeyang7789.cn-evidence-mcp-public/cn-evidence v0.1.0 |
| SignalEDI MCP | signaledi-mcp | X12 EDI developer experience - docs discovery, fixtures, parse/validate 850/810/856/837P, profile-gated sandbox and production connections, QuickBooks adapters | Not live-probed (stdio npm package); registry io.github.SignalEDI/mcp-server documented on the listing |
| Taskade MCP | taskade-mcp | Official workspace MCP - 62 tools over workspaces, projects, tasks, AI agents, chat, webhooks, knowledge bases, templates, media | Live-verified: hosted endpoint returns HTTP 401 by design (OAuth 2.0 PKCE); npm @taskade/mcp-server resolves |
| schemagate MCP | schemagate-mcp | Identity-scoped schema selection for text-to-SQL - permitted tables only reach the prompt, 65-76% token cuts | Not live-probed (self-hosted PyPI package); MCP entry point, stdio + streamable-http documented |
| SQL Server MCP | sql-server-mcp | Multi-instance DBA console - grouped connections with hot reload, execution plans, index layouts, stored-procedure source | Not live-probed (stdio npm package); @cevelas/mcp-sqlserver v3.0.0 resolves |
| TrendPulse MCP | trendpulse-mcp | Google News discovery + Google Trends analysis - 16 tools, MIT community server | Not live-probed (self-hosted Python package); README documents all 16 tool schemas |

## Findings

- **CN Evidence MCP**: 3 tools - resolve_china_company (free), get_china_supplier_evidence_basic ($0.002 USDC), get_china_supplier_evidence_full ($0.01 USDC). Every record carries source provenance, dataset_coverage and coverage_notes; zero records is not nationwide clearance. x402 v2 on Base (USDC, EIP-3009).
- **SignalEDI MCP**: least-capability profile model - docs (keyless), sandbox, production; domain scopes (platform:documents:read/send, platform:connections:*, platform:quickbooks:*, platform:data:sensitive); deprecated umbrella credentials rejected. Production go-live needs an active immutable version.
- **Taskade MCP**: hosted OAuth 2.0 PKCE at taskade.com/mcp plus local npx with TASKADE_API_KEY. Registry io.github.taskade/mcp-server. Submission is the official resubmission (prior PR #512 closed without merge).
- **schemagate MCP**: Apache-2.0 PyPI library with MCP entry point (stdio or SCHEMAGATE_MCP_TRANSPORT=streamable-http). Measured token reductions 65-76% on bundled benchmark schemas; Vanna migration note included.
- **SQL Server MCP**: npm v3.0.0, GitHub cvelasquez/mcp-sqlserver; the author-level mcpservers.org slug 404s while the /all listing carries the full description.
- **TrendPulse MCP**: uvx mcp-trendpulse; 6 news tools + 10 trend tools; hosted DigestSEO layer explicitly unreleased.

## Skipped (also identified, not catalogued)

- **Prior-sweep dispositions respected** (ruled by the Sep 10 late-night sweep): Theyond, TruVerifAI, OpenZiti LLM-Gateway, OpenZiti MCP Gateway, Drop2Run, LoadSnap, ZMS AI Creative Suite, MirrorFly, MCP DB Wizard. Note: Theyond (keyless, 2 read-only tools, 374K live jobs) and MCP DB Wizard (config-emitted Oracle tools) both probe live today; skips stand unless reversed.
- **#4064** - benchmark fixture (return-review); benchmark class.
- **NetMax #4063** - 14 network-diagnostic tools (speed test, DNS ranking, bufferbloat) for coding agents; dev utility class.
- **Piazza in Festa #4062** - Italian town events from municipal records; geo niche.
- **QY-Stream #4060** - 29-source cross-source news/finance aggregation; media news class (AllNewsAPI precedent).
- **QianYuan #4059** - agent trust and result-reuse layer; agent infra class.
- **Open Task Relay #4058** - public-good task marketplace; TaskMarket class.
- **magents #4057** - shared session bus MCP+CLI; dev infra class.
- **x402-scraper-engine #4056** - HTTP 402 pay-per-call scraper; x402 scraping class (Cracked precedent).
- **CARMOTIF #4055** - automotive design reference search; niche vertical design.
- **Corsair** - open-source integration-layer platform; integration-platform infra class (Atako precedent).
- **Finamatik** - mcpservers.org 404 shell.
- **BusinessQuik** - Apify bank-statement actor, 2 users, pay-per-event; thin and immature.
- **ajmessina, akzar1el** - nav-only shells.
- **Seedfast** - prior disposition (synthetic test-data dev tool).
- **Tokenectomy** - prompt-payload optimizer; dev utility.
- **QVeris Agent Toolkit** - cross-client capability discovery; agent infra class.
- **RUAGENTIC Directory** - meta-directory search; ToolsMonk precedent.
- **Coinranking Pro Chart, DESK LEAD x402** - crypto class.
- **SuperGlookoQuery** - clinical diabetes data audit; healthcare niche.
- **Picatura Naturii** - consumer product catalog.
- **SSL Certificate Check (powmcp)** - dev utility (Perimeter Watch precedent).
- **basile.cc** - French-only MCP; geo niche.
- **iOS Agent Skill** - Swift code-review utility; dev class.
- **Video2x, OffStereo** - media and consumer classes.
- **ego lite, Alpha Vantage** - sponsor repeats (prior dispositions).
- **HasData per-connector listings** (YouTube, TikTok, Instagram, Zillow, Google Search, Yelp, Bing, Amazon, Walmart, Yellow Pages, Glassdoor, Google Images, Redfin, Shopify, Google Scholar, Facebook) - covered by the HasData 57-API family guide.

## Catalog State

- Catalog: 628 → 634 servers; 514 → 520 guides.
- 3 endpoints live-verified over JSON-RPC this sweep (CN Evidence keyless tools/list captured; Theyond also probed live but skip stands; Taskade 401-by-design).
