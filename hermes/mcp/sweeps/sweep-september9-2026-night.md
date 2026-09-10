---
title: "MCP Server Discovery - September 9, 2026 (Night Sweep)"
description: "Night sweep over the mcp.so feed and mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy. 10 new business-relevant servers catalogued with guides: ViralHunt (social trending + publishing), Comunicate (press release distribution), CourtListener (US legal research), Soprano Connect (multi-channel messaging), ConnectMachine (contact CRM), mnemiq (tunable text-to-SQL), Sqemo (database schema design), ToHuman (AI text humanizer), Modelglass (AI model pricing) and VenuNite (US events data)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-09
---

# MCP Server Discovery - September 9, 2026 (Night Sweep)

**Source:** mcp.so feed (30 server blocks; 4 new above the evening sweep's dispositions), mcpservers.org /all pages 1-2 (r.jina.ai reader proxy; page 1 had fully rolled since the evening sweep - ~30 fresh submissions in the last hour)
**Method:** feed $R-block parsing, /all slug extraction + detail-page fetch via proxy, vendor docs fetch
**Date:** September 9, 2026 ~17:30 MST (00:30 UTC Sep 10)

## Summary

| Metric | Count |
|---|---|
| mcp.so feed server blocks evaluated | 30 (4 new above evening dispositions) |
| mcpservers.org /all pages fetched | 2 (~60 slugs) |
| Detail pages fetched | 38 |
| New servers catalogued | 10 |
| Integration guides written | 10 |
| Skipped (not catalogued) | 25+ (infra classes, dev utilities, thin docs, shells, consumer) |

## New Business-Relevant Servers (10 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| ViralHunt MCP | viralhunt-mcp | Trending discovery across 12 networks + scheduling/publishing - 20 tools, growth_24h velocity, best-time-to-post | detail page carries full docs: npx viralhunt-mcp with VIRALHUNT_API_KEY, MIT, Official MCP Registry io.github.rodvan/viralhunt-mcp, free 7-day token |
| Comunicate MCP | comunicate-mcp | Press-release distribution - catalogue search, drafts, SEO checks, editorial plans, order publication | detail page: 19 named tools, app.comunicate.top/mcp, API key + OAuth 2.1, two-lock spend control (permission switch + key scopes) |
| CourtListener MCP | courtlistener-mcp | US legal research - CourtListener API v4, GovInfo statutes, Regulations.gov | detail page + repo: FastMCP, Docker (ghcr.io/travis-prall/court-listener-mcp), opinion/docket/court/person/audio tools + citation family |
| Soprano Connect MCP | soprano-connect-mcp | Multi-channel business messaging - SMS, voice, RCS, WhatsApp templates, Viber, push, email | repo soprano-mcp/mcp (MIT, Python 3.12): uv run mems-mcp stdio or streamable-http, pluggable per-request upstream auth, local 127.0.0.1:8000 |
| ConnectMachine MCP | connectmachine-mcp | Digital business cards + contact CRM - contacts, networks, cards, meeting transcript Q&A | detail page: hosted mcp.connectmachine.ai/mcp, 20+ named tools, Glama + Smithery + MCP Registry listed |
| mnemiq MCP | mnemiq-mcp | Tunable text-to-SQL - enrich/build/ask pipeline, role-scoped queries, grounding per answer | repo agenticfabriq/mnemiq: open-source, uv run mnemiq enrich/build/ask/serve --http, pipeline-as-settings |
| Sqemo MCP | sqemo-mcp | Database schema design + ERD governance - introspect, drift check, diff, SQL/DBML export | npm sqemo-mcp (MIT, io.github.sqemo/sqemo): 15 named tools, local .erd.json free, cloud ERDs via npx sqemo-mcp login |
| ToHuman MCP | tohuman-mcp | AI text humanizer - single humanize tool, 4 intensity levels | detail page: hosted tohuman.io/mcp, free API key in Authorization header, no storage |
| Modelglass MCP | modelglass-mcp | Live AI model pricing + routing - costs, comparisons, routing recommendations | detail page: modelglass-api.vercel.app/mcp, free Bearer key, Claude Code + VS Code, REST /v1/models |
| VenuNite Events MCP | venunite-mcp | US live events data - 400K+ events, read-only search with quota transparency | vendor docs page: mcp.venunite.com/v1/mcp keyless fair-use trial (5/min, 100 calls/day), Builder key, applied_filters + explicit quota states |

## Findings

- **ViralHunt MCP**: 20 tools drive the full discover -> time it -> publish -> verify -> correct loop. Every metric carries sample size and time window; `growth_24h` separates early trends from fading ones. Free token (7-day trial, no card), MIT, npm + Official MCP Registry. Category: Social Media Management.
- **Comunicate MCP**: press distribution with two independent spend locks - a platform-level "AI assistants may order and publish" switch plus API-key scopes, with every switch change in the audit log. RON pricing. Category: Marketing.
- **CourtListener MCP**: three US legal sources (CourtListener v4, GovInfo, Regulations.gov) in one self-hosted FastMCP server with a citation tool family (batch lookup, parsing, verification) - agents can cite primary sources instead of paraphrasing. Category: IP/Legal.
- **Soprano Connect MCP**: enterprise CPaaS messaging (SMS, voice, RCS, WhatsApp templates, Viber, push, email) as a self-hosted MCP server with credentials selected per request and never stored. MIT, Python 3.12, stdio + Streamable HTTP. Category: Communication & Email.
- **ConnectMachine MCP**: hosted contact CRM with meeting-transcript Q&A and action-item generation - networking data stays agent-queryable. 20+ tools, nothing to install. Category: CRM & Sales.
- **mnemiq MCP**: open-source text-to-SQL where every pipeline stage is a readable setting; answers show the SQL, tables read and grounding; role-scoped queries. Category: Data & Analytics.
- **Sqemo MCP**: governed schema design - naming checks, drift detection against the live database, ERD diffs, SQL (7 dialects) and DBML export. MIT npm package. Category: Database & Data Engineering.
- **ToHuman MCP**: hosted humanizer with intensity levels (minimal/subtle/medium/heavy) and no text storage - removes the manual humanize step from AI-drafting pipelines. Category: Content.
- **Modelglass MCP**: live model pricing/capabilities with routing recommendations inside Claude Code - stops overpaying on model calls. Free persistent keys. Category: AI Operations.
- **VenuNite Events MCP**: keyless read-only US events search with explicit quota states (row_budget_exhausted, location_unavailable) and applied_filters transparency - agent-safe local data. Category: Location Data.
- **/all page-1 rollover**: the page the evening sweep classified at ~23:30 UTC had fully rolled by 00:30 UTC - every page-1 name this sweep was new, while page 2 carried the evening sweep's disposed set. Confirms the re-sweep rule: same-day sweeps must re-pull /all, never assume page stability.

## Non-Catalogued (Disposed or Repeats)

- **Orthogonal**: unified gateway for company data, scraping, enrichment and financial APIs with per-request pricing at mcp.orthogonal.com - tool-marketplace infra class (ToolRouter precedent), no tool list published.
- **Loadster**: load-testing platform MCP at api.loadster.com/mcp - dev utility class, no published tool names (thin docs).
- **mFlow**: shared Kanban board for Claude sessions - free Standalone tier, but no published MCP endpoint.
- **MarginGlow AI Signal**: evidence-based small-business opportunity intelligence - beta, no published endpoint.
- **Dart**: agent-orchestration PM tool (100K teams) - /docs/mcp 404s, no MCP docs surface.
- **Harmny**: detail page returns the vendor app's source-code dump, not product docs.
- **ToolsMonk**: tool-directory search utility (5 read-only tools) - meta-directory class.
- **MiniMax H3 Max**: text-to-video model listing (h3-max.com) - media generation class; official MiniMax MCP already catalogued.
- **Piloxa, OmniDome, Course Profiler**: detail-page shells (nav-only markdown).
- **Open Agent Remote Index**: agent index infra; **Promptessor**: prompt-management dev utility; **Offensive360**: code SAST dev utility; **Keploy**: traffic-to-tests dev utility; **mcp-multiplexer**: MCP aggregation infra; **Odysseus Web MCP**: saturated web-search wrapper class; **skillmem**, **Material Model**: agent memory/coordination infra; **AgentMesh.help**: open-race task marketplace (TaskMarket class); **Online Pizza**: consumer novelty; **Brixa Studio**: design-tool class; **Magic Cloud**: low-code dev platform; **Vocemo**: consumer Mac app; **Compendio**: local docs RAG dev utility; **GenToon**: consumer art; **SendCheck**: x402 payment pre-validation (x402 infra class); **toll402**: x402 pay-per-call SDK (crypto/x402 class).
- Already catalogued or disposed repeats on /all pages 1-2: Ryze Google Ads (doc-URL slug variant of the night-sweep catalogued server), Alpha Vantage, MiniMax, Reflex, VetAgent, Wafeq, Site Passport, Ultralayer, plus the evening sweep's disposed set.
