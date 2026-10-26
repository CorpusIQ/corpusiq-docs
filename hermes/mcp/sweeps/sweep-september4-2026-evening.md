---
title: "Sweep Report - September 4, 2026 (Evening) - CorpusIQ Docs"
description: "Evening MCP catalog sweep: chatmcp/mcpso issues #3918-#3937 plus mcp.so feed and mcpservers.org /all pages 1-3, cataloging 13 new servers with guides (gofact, Factur-X by Orvel, ddmarketer, registry-mcp, Ozon, Wildberries, EuroDNS, PurrPlan, PingRoom, CTlogs.io, Helixar, Velarion, VeriRoute); catalog now 539 servers / 425 guides."
date: 2026-09-04T19:02:00-07:00
sources: [chatmcp/mcpso, mcp.so, mcpservers.org]
status: complete
last_updated: "2026-10-19"
---

# September 4, 2026 - Evening Cron Sweep

**Shift:** Evening (~19:00 MST)
**Prior cutoff:** Sep 4 morning sweep (mcp.so feed + /all pages 1-3), issues cutoff Sep 3 evening (#3917)
**Fresh window evaluated:** chatmcp/mcpso issues #3918-#3937 (19 fresh), mcp.so feed (30 slugs) plus recentServers (8 entries), mcpservers.org /all pages 1-3 (90 slugs batch-classified), mcpservers.org homepage (18 slugs)
**Surfaces:** issues via GitHub API, feed + homepage via curl + parse-homepages.py, /all pages via curl + slug extraction, live probes via batch-probe.py (7 endpoints)
**Result:** 13 new servers catalogued (13 guides), catalog now 539 servers / 425 guides

## Catalogued (13)

| Server | Slug | Source | Verification |
|---|---|---|---|
| gofact | gofact-mcp | issue #3936 | README fully mapped: 11 tools, stdio Go binary, AGPL-3.0, EN 16931 pre-check + PDF/A-3 self-check, legal numbering in locked transactional registry, PDP submission optional |
| Factur-X by Orvel | facturx-orvel-mcp | mcpservers.org /all | 4 tools live-probed keyless at facturx.orvel.dev/mcp (generate_invoice, embed_xml, validate_invoice, extract_invoice) + 2 resources, EU-hosted, free 50 docs/mo, registry io.github.LeBorgneAntoine/facturx |
| ddmarketer | ddmarketer-mcp | issue #3932 | 4 tools live-probed keyless at ddmarketer.com/api/mcp (search_gaps, get_top_gaps, validate_idea, get_dossier), complaint corpus from 8 sources, free |
| registry-mcp | registry-mcp | issue #3927 | 5 tools live-probed keyless at api.foretak.dev/mcp (serverInfo v0.2.0), Norway brreg, MIT code / NLOD 2.0 data, stdio twin uvx/npx |
| Ozon MCP Server | ozon-mcp-server | issue #3921 | PyPI v2.5.0 MIT, 158 tools, Fernet-encrypted tokens, dashboard, context budgeting (476K to 63K tokens measured), OZON_TOOLSETS trimming |
| Wildberries MCP Server | wb-mcp-server | issue #3920 | PyPI v2.6.0 MIT, 197 tools, sibling architecture, corpus measured 770K to 74K tokens, WB_TOOLSETS trimming |
| EuroDNS MCP | eurodns-mcp | mcpservers.org /all | README fully mapped: 82 tools (79 OpenAPI + 3 DNS workflow), guardrails (read-only/billing/destructive), hash-chained audit log, npm @jigsawfr/eurodns-mcp, OAuth 2.1 or shared token |
| PurrPlan MCP | purrplan-mcp | mcpservers.org /all | 18 tools with scopes enumerated in vendor README, endpoint app.purrplan.ai/api/mcp, Bearer or OAuth 2.0 DCR+PKCE, confirmation-gated replies, EUR 9/mo from Pro, lifetime deal |
| PingRoom | pingroom-mcp | issue #3937 | 41 tools live-probed at api.pingroom.io/api/agent/mcp (catalog open), OAuth 2.1 PKCE + DCR for account ops, registry io.pingroom/pingroom active |
| CTlogs.io MCP | ctlogs-mcp | mcpservers.org /all | 5 tools from README, endpoint mcp.ctlogs.io/mcp 401-verified live (OAuth browser sign-in), read-only, Lyalpha GmbH |
| Helixar MCP | helixar-mcp | mcpservers.org /all | 2 remote tools live-probed at mcp.helixar.ai/mcp (serverInfo helixar-security v0.0.1), Sentinel 26 rules, HDP validation, ReleaseGuard stdio-only, Apache-2.0 |
| Velarion | velarion-company-intelligence | mcp.so feed | 12 tools live-probed keyless at velarion-scraper-production.up.railway.app/mcp (serverInfo v3.3.1), 6 free-plan + 6 paid/catalog, exec comp + governance |
| VeriRoute Intel MCP | veriroute-intel-mcp | mcp.so feed | 5 tools from README, endpoint verirouteintel.com/api/mcp, bearer key, US/CA numbers, async bulk to 10,000, registry com.verirouteintel/lookup, repo license not declared |

## Not catalogued (skip prose)

- **Kyma API (#3919):** model catalog, credits and test completions for coding agents - dev utility class.
- **google-maps-mcp-server (#3922):** 0-star repo created today with no description - saturated Google Maps wrapper class (google-maps-scraper-mcp, google-maps-email-extractor already catalogued).
- **padel.how (#3923) / Pickleball3 (#3924):** consumer sports catalogs class.
- **Anima (#3925):** identity for agents (email, US phone, voice, vault) - identity/OTP plumbing class (sms-florin precedent).
- **earn-bounty-scanner (#3926) / earn-dataset-mcp (#3931) / farmdash (#3933) / solana-research-library (#3935):** consumer crypto class (RAVN precedent).
- **G-Guest (#3928):** consumer local booking - consumer regional services class (MyFlohmarkt precedent).
- **MuPag Sandbox Payments (#3929):** sandbox-only test tool, rejects production credentials - dev utility.
- **ResuMakeAi (#3930):** ATS resume score - consumer career utility class.
- **Plainport (#3934):** public-web intake and validation utilities - scraping infrastructure class (Firecrawl-alternative precedent).
- **Orbit (/all):** API-call codegen from task descriptions - dev utility.
- **MemoryGuard (/all):** local-first MCP memory governance for coding agents - agent memory infra class (ShadowGraph precedent).
- **OutSlide (/all):** slide outline preview utility - creator utility class.
- **Crapkit (/all):** CRAP code-complexity scores - dev tool.
- **BeatDesign (/all):** local-first AI media workbench - creator utility class (klo-mcp precedent).
- **PayTech Events (homepage):** fintech conference WebMCP directory - thin events directory class.
- **Trandence (homepage):** consumer trading journal - consumer investing class.
- **Booking.com Hotel Search (homepage):** prior disposition stands (FlightPowers thin vendor surface, Aug 23) - same product, not new.
- **Seedance (homepage):** AI video generation - media generation class (Imaginode/Deep Art precedent).
- **DB Planner (feed):** DB schema editor for dev teams - dev utility.
- **Alien Probe who (recentServers):** x402 single-tool GLEIF resolver with no repo or docs - thin-docs x402 class.

**Feed/recentServers repeats** already catalogued by prior sweeps (Lawstronaut, Strac DLP, Tracetify, Extend, iubenda, Sorank, HiBot, Furrow Forms, Dealwize, Factanker, Nizh, miniOrange, Klarix, Asyntai, ToBid, AuType, Lifesight, NeuralVerge, Farmwalk, Fallax, TheLuckyStrike, TaiLexi) or already disposed (pdfAssistant, FLORA, RAVN, Neither, QuantumProxies, Voibe, dot.tools, MarketCode, PostMCP, OSIR Domain, Trendos, Koongo, AON, Hostinger, QoreNext CRM and Trade Screening, send-email, Backblaze B2, Layers, Mantis, ZenSched, Wagglet, Digital Darts, ListingBott, SEObot AI, DevHunt, Rovyn, MarsX, GospelChannel, MagicMaster, NC Wedding Guide, x402 List, Sirro, VenuNite, Slop, PriceMyRepair).
