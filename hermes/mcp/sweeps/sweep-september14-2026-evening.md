---
title: "MCP Server Discovery - September 14, 2026 (Evening Sweep)"
description: "Evening sweep over the mcp.so feed (30 server blocks via the r.jina.ai reader proxy), chatmcp/mcpso issues #4135-#4139, the mcp.so homepage recentServers (14 fresh blocks) and a fresh mcpservers.org /all page-1 crawl via the r.jina.ai reader proxy. 9 new business-relevant servers catalogued with guides: Helio MCP (open-source governance proxy for agent tool calls), geolint MCP (AI-search readiness linter, 51 rules), Serp Sidekick MCP (live SEO and AI-visibility data, 15 tools), Prism MCP (contract deadline reader, 8 tools), Nebelus MCP (governed agent building for regulated industries, ~48 tools), CherryShot MCP (product photography and video ads), Foliyo MCP (branded client reports and proposals), Convert.Online MCP (file conversion across 400+ formats) and RankJot MCP (real Google rankings in one tool)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-14
---

# MCP Server Discovery - September 14, 2026 (Evening Sweep)

**Source:** mcp.so feed (30 server blocks via the r.jina.ai reader proxy), chatmcp/mcpso issues #4135-#4139 (fresh window past the midday cutoff at #4134), mcp.so homepage recentServers (fresh blocks), mcpservers.org /all page 1 via the r.jina.ai reader proxy
**Method:** feed proxy parse, /all slug batch-classification, issue-body review, mcp.so detail pages via the r.jina.ai reader proxy (5 fetches), mcpservers.org server pages via the r.jina.ai reader proxy (6 fetches), npm registry verification (3), PyPI verification (1), JSON-RPC live probes (5 endpoints + 1 re-probe)
**Date:** September 14, 2026 ~17:00-18:30 MST (Sep 14 23:00 - Sep 15 01:30 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 30 (mcp.so, via r.jina.ai proxy) |
| /all page-1 entries classified | 30 (via r.jina.ai proxy) |
| GitHub issues reviewed | 5 (#4135-#4139) |
| Detail pages fetched | 11 (mcp.so + mcpservers.org via r.jina.ai proxy) |
| Packages verified | 4 (npm @gethelio/proxy 0.14.0, npm @iliasabk/geolint 0.3.2, PyPI rankjot-mcp 0.1.0, npm repo links) |
| Endpoints live-probed | 6 (prism, nebelus, cherryshot, foliyo, convert, serpsidekick - all HTTP 401 auth gates; whatsMCP re-probe 401) |
| New business-relevant servers | 9 |
| Integration guides written | 9 |

## Core Listing Re-checks

- **mcpservers.org:** LISTED - /all page 1 served fresh via the r.jina.ai reader proxy (12,712 total servers shown); direct curl still Cloudflare-challenged.
- **mcp.so:** NOT LISTED (CorpusIQ) - no corpusiq server object in the feed or homepage SSR; no resubmit (account quarantine holds).
- **glama.ai / PulseMCP / smithery.ai:** unchanged from the midday check (LISTED).

## New Servers Catalogued (9)

1. **Helio MCP** - open-source MCP governance proxy (Apache-2.0, npm @gethelio/proxy 0.14.0 verified, repo gethelio/helio verified live). Sits between agents and MCP servers: denies destructive tool calls, rate-limits, caps cumulative spend across paying tools, routes over-limit actions to approval, and writes a hash-backed audit trail. Starts in audit-only mode until policies are enabled; self-hosted.
2. **geolint MCP** - AI-search readiness linter (MIT, npm @iliasabk/geolint 0.3.2 verified). 51 rules across AI crawler access (51 tokens), llms.txt, structured data, citability and technical foundations, with a scored report and a fix per finding; runs in CI via a GitHub Action and serves an MCP stdio mode.
3. **Serp Sidekick MCP** - live SEO and AI-visibility data for assistants: 15 tools covering keyword research, Search Console mining (read-only), competitor gaps, page audits and brand mentions across ChatGPT and Google AI Overviews. OAuth (Google sign-in), endpoint serpsidekick.com/mcp 401-verified; free Search Console tier, credits from $5.
4. **Prism MCP** - contract deadline reader: every deadline with exact date, consequence and source sentence, computed from the contract's own rules. 8 tools (review/get/unlock/upcoming/list/account/buy/feedback); endpoint prism.parad1gm.com 401-verified; 3 free contracts then $0.50 each.
5. **Nebelus MCP** - enterprise agentic-AI platform for regulated industries; ~48 tools expose the Construction API for governed agent building (agents as drafts, locked guardrails, grounding-trace claim-to-source verification, EU/KSA residency). OAuth 2.1 or org API key; api.nebelus.ai endpoint 401-verified.
6. **CherryShot MCP** - product photography and video ads from one photo (on-model shots, lifestyle scenes, marketplace images, short video ads). 6 tools (credits/models/create and poll shoot/video); Bearer API key; endpoint 401-verified.
7. **Foliyo MCP** - branded client reports, proposals and research pages: reusable client brands, static HTML publishing, PIN and email gates, stable share links updatable from another authorized client. OAuth 2.1 with scoped workspace write; foliyo.io/mcp 401-verified; CLI available.
8. **Convert.Online MCP** - file conversion across 400+ formats (images, video, audio, documents, ebooks, fonts, CAD) with 5 tools (list formats, list options, upload, convert, get job). OAuth or API key; mcp.convert.online 401-verified; published in the official MCP registry as online.convert/file-converter.
9. **RankJot MCP** - real Google rankings in one tool: check_rank(domain, keyword, country) returns the 1-based position (or null), the ranking page, the top 10 results and remaining quota. stdio via uvx; PyPI rankjot-mcp 0.1.0 verified; MIT; free tier with 25 lookups a month.

## Also Identified (not catalogued)

WhatsMCP (WhatsApp for AI agents - endpoint 401-verified but no published tool list, re-check next cycle), Vivu (video library search with natural language - media library class), Nano Studio Pro (personal asset repository, 35 detection-aware search and generation tools - creative asset utility class), Liner MCP (cited web and academic search with quick-answer and deep-research agents - general search class), Featureflip #4139 (official feature-flag server, 19 tools, npm @featureflip/mcp - dev tool class, LaunchDarkly precedent), ProxyCove #4135 (proxy provisioning with agent-driven signup - browser infrastructure class, prior disposition), Skills Anywhere (local Agent Skills loader over MCP - dev utility), Lathe (managed Postgres/Redis provisioning - dev database class), Speedbot (agent speed dating - novelty), BenchBoss (agent chess with public standings - novelty), MIDIRestyle (MIDI restyle - creator utility), Firedraw (Firestore diagramming - dev utility), okmq (message queue - dev utility), FCoP (coding-agent task handoffs - dev infra), Access Log Forensics (log analysis - dev utility), AI Trading Signals (crypto signals - crypto class), Ramus (disposable Android emulator - dev tool), AntiBrow (persistent browser profiles - scraping infrastructure class), Niu Lai (2026 box-office data - media niche), Almirall (pharma official listing - vendor niche), Immersive Commons (SF venue events - local niche), PostOnce (social scheduling - social-posting utility class), and benchmark fixtures #4136/#4138. Feed and /all repeats already catalogued or previously disposed: AfterLaunch, NinjaChat, B2B Creators, CraftStory, LandLens One, Recordwire, VerifyAPI, SimFuse, SomaCheck, Mobile Text Alerts, UmmahAPI, Midpoint Card Prices, UX Jobs, Mailbox MCP, Microburbs, Fee Optimizer, MiniMax H3, Kairos Signal (prior #3799 disposition), plus the Sep 14 midday and Sep 12 sweep sets.

## Notes

- The midday sweep's six pages were re-verified live before this run (all HTTP 200 on docs.corpusiq.io), so no deploy gap was carried into this sweep.
- GitHub REST search quota was exhausted partway through (authed, HTTP 403) - repository existence checks fell back to plain HTTP status probes (gethelio/helio 200, epolat/rankjot-mcp 200) and npm/PyPI metadata, which carry canonical repository links.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [MCP Ecosystem Sweeps](/docs/hermes/mcp/sweeps)
