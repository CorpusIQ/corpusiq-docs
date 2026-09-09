---
title: "MCP Server Discovery - September 9, 2026 (Evening Sweep)"
description: "Evening sweep over the mcp.so feed (30 server blocks) and mcpservers.org /all pages 1-3 via the r.jina.ai reader proxy. 8 new business-relevant servers catalogued with guides: AgentLedger (agent spend management), Vibe Prospecting (Explorium B2B data), Wafeq (accounting books), Agent Watch (endpoint monitoring), Ultralayer (market intelligence), TrustScan (MCP security scanning), Yandex Metrika (web analytics) and Site Passport (AI-agent readiness checks)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-09
---

# MCP Server Discovery - September 9, 2026 (Evening Sweep)

**Source:** mcp.so feed (30 server blocks, TanStack Router $R-stream), mcpservers.org /all pages 1-3 (r.jina.ai reader proxy; direct curl Cloudflare-challenged)
**Method:** feed $R-block parsing, /all slug extraction + detail-page fetch via proxy, vendor docs fetch, WebMCP manifest probe (sitepassport.org)
**Date:** September 9, 2026 ~16:30 MST (23:30 UTC)

## Summary

| Metric | Count |
|---|---|
| mcp.so feed server blocks | 30 |
| mcpservers.org /all pages 1-3 | 89 slugs batch-classified |
| Detail pages fetched | 15 (via r.jina.ai proxy) |
| WebMCP manifests probe-verified | 1 (sitepassport.org - full tools list, keyless) |
| New servers catalogued | 8 |
| Integration guides written | 8 |
| Skipped (not catalogued) | 404 shells, adult search, prior dispositions, thin docs, sandbox-only, dev/consumer classes |

## New Business-Relevant Servers (8 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| AgentLedger MCP | agentledger-mcp | Per-agent spend management - x402/MPP/API-key tracking, budget caps, audit trail | detail page carries full docs: endpoint, 5 named tools, REST curl examples, free beta / $19 Pro |
| Vibe Prospecting MCP | vibe-prospecting-mcp | Explorium live B2B data - lead lists, contact enrichment, firm research, CSV export | full-path detail fetch (explorium-ai/vibeprospecting-mcp) resolved rich docs after morning's author-slug 404; OAuth endpoint vibeprospecting.explorium.ai/mcp |
| Wafeq MCP | wafeq-mcp | Wafeq accounting books - 251 API endpoints as safety-categorized MCP tools | GitHub README (ohneben/Wafeq-MCP, MIT): 253 tools, 9 safety categories, stdio + Streamable HTTP, Docker, registry-listed |
| Agent Watch MCP | agent-watch-mcp | MCP endpoint monitoring - liveness, latency, schema drift, auth posture, price integrity | detail page carries full docs: /mcp endpoint, v1/probe + v1/watch REST, free 5-endpoint tier, $19/$99 plans |
| Ultralayer MCP | ultralayer-mcp | Realtime market intelligence - news, filing diffs, sentiment, alerts | full-path detail fetch (ultralayerhq/ultralayer-plugin) resolved docs after morning's author-slug 404; endpoint api.ultralayer.ai/v0/mcp, OAuth/API key, MIT |
| TrustScan MCP | trustscan-mcp | MCP server and AI skill security scanner - Unicode injection, MCP001-006, secrets, typosquat | detail page carries full docs: endpoint, 2 named tools, 4 check classes, keyless, free, registry io.github.entradox/trust-scan |
| Yandex Metrika MCP | yandex-metrika-mcp | Full Yandex Metrika API - 108 Management/Logs/Stat methods | full-path detail fetch (artgas1/yandex-metrika-mcp) resolved rich docs after morning's author-slug 404; npm package, MIT, 10 default tools, _meta transparency contract |
| Site Passport MCP | site-passport-mcp | AI-agent readiness checks - llms.txt, robots.txt AI directives, schema.org, WebMCP manifest | LIVE WebMCP manifest probe: sitepassport.org/.well-known/mcp.json serves tool check_wordpress_agent_readiness, keyless, Streamable HTTP |

## Findings

- **AgentLedger MCP**: hosted at agent-ledger-production-0ff8.up.railway.app/mcp (Streamable HTTP). Five tools (ledger_track, ledger_set_budget, ledger_report, ledger_alerts, ledger_list_agents) with agent-secret write auth - reads open, writes require the secret issued on first track call. Budget caps enforced with a 402 at track time. Free beta up to 3 agents, Pro $19/mo via Stripe. Registry io.github.entradox/agent-ledger. Same vendor as Perimeter Watch, Agent Watch, TrustScan and QuoteOS. Category: Finance.
- **Vibe Prospecting MCP**: hosted at vibeprospecting.explorium.ai/mcp (Streamable HTTP, browser OAuth, no API key). Explorium's B2B data: company search, contact discovery/enrichment, firm research (firmographics, technographics, funding, competitors), sample-first previews with explicit CSV exports. Per-client walkthroughs for Claude Code/Desktop, Codex, Gemini CLI, Manus and Hermes. Category: Lead Generation & Web Scraping.
- **Wafeq MCP**: community MIT server (github.com/ohneben/Wafeq-MCP) exposing all 251 Wafeq Public API endpoints as spec-generated tools plus 2 handwritten ones - 253 total, tagged with 9 safety categories and readOnlyHint/destructiveHint annotations. stdio or Streamable HTTP via Docker (localhost:8765), idempotency keys on 146 write endpoints, whole-period report validation, tenant verification at startup. Registry io.github.ohneben/wafeq-mcp. Category: Finance.
- **Agent Watch MCP**: hosted at agent-watch-api-production.up.railway.app/mcp. Monitors MCP registry endpoints and paid agent services (x402/MPP) for liveness, latency (p50/p95), schema drift, auth posture (RFC 9728) and price integrity (Phase 1). Open probe API (POST /v1/probe), watch API tied to checkout email. Free 5 endpoints, Builder $19/mo, Team $99/mo, Data API metered. Category: DevOps.
- **Ultralayer MCP**: hosted at api.ultralayer.ai/v0/mcp (OAuth or bearer from console.ultralayer.ai). Market news separating new information from repeats, developments with impact scores, event timelines, company outlooks, disclosure changes, stakeholder analysis, sentiment and alerts; point-in-time safety for backtests; MIT plugin repo. Listed on Glama, MCP Registry and Smithery. Category: Finance.
- **TrustScan MCP**: hosted at trust-scan-production.up.railway.app/mcp (Streamable HTTP, keyless, free). Two tools (trust_scan_server with typosquat check, trust_scan_file). Four check classes: invisible Unicode prompt-injection, dangerous patterns MCP001-MCP006 (eval/exec, shell, raw sockets, unsafe deserialization, obfuscated base64), hardcoded secrets, typosquat via Levenshtein distance. v0.1.0, registry io.github.entradox/trust-scan. Category: Compliance.
- **Yandex Metrika MCP**: npm yandex-metrika-mcp-server (MIT, npx install). All 108 Yandex Metrika API methods (Management 95, Logs 7, Stat 6) generated from official docs; 10 tools exposed by default with one-variable enablement for the rest. No-silent-substitution contract: every response carries _meta with applied filters, server decisions, retry counts, truncation flags; robot filter disclosed in schema and _meta. OAuth token redacted from echoed request URLs. Category: Data & Analytics.
- **Site Passport MCP**: WebMCP manifest live-verified at sitepassport.org/.well-known/mcp.json (Streamable HTTP, keyless). One tool: check_wordpress_agent_readiness - live-checks a site for llms.txt, AI-crawler robots.txt directives, schema.org markup and a WebMCP manifest. Category: SEO.
- **Morning 404-shell supersessions**: the morning sweep's author-slug 404 rulings (explorium-ai, artgas1, ultralayerhq) were based on author-level pages; full author/name detail paths resolved rich docs for Vibe Prospecting, Yandex Metrika and Ultralayer. Magenest Odoo's full path (magenestjsc/advanced) confirmed 404 - remains a shell.

## Non-Catalogued (Disposed or Repeats)

- **QuoteOS**: keyless insurance-quoting middleware (checkEligibility, getAutoQuotes, getHomeQuotes) but synthetic sandbox data only - premature per the Krimskrams rule.
- **Magenest Odoo**: mcpservers detail page 404 shell (confirmed this sweep).
- **PRIMAMCP**: German-language legal research from official sources (8 named tools) - morning disposition as geo niche respected.
- **Onymu**: thin tagline-only mcp.so listing.
- **priostack**: agent context/memory orchestration SDK - agent memory infra class, Memwyre precedent.
- **LinkScale**: link-in-bio platform detail page with no MCP endpoint or tool docs - thin docs (morning disposition).
- Repeats already disposed by the morning sweep: WattScope, AgentRender, Collide, Kontexta, Rogue, Torquantis, VitaeContext, Lexicon, ContextSwitch, Flash, Index TTS, Surli, Nullheim, 3DAssets Dev, ARADIA, FlightPowers, Seedance, dxpert UNS, adult-search trio (NudiTok, Desaira, tik-tok.porn), remaining 404 shells.
- Feed repeats already catalogued or disposed: Artlist, Ultimate Web Scraper, Emailchaser, DCA Method, SoundGTM, Expired Domains, Mailercloud, InstantClips, JsonCut, Fundz, Rechnungslotse, Countersignatory, Formdall, LoomaScale, Beamtrace, PostNitro, Yocoolab, TrueClicks, YouSpot, Fluenta, VarynForge, Saaskly, Fruit Stand, GoBuy, Create Prints, Tessryx, VeriRoute, Alien Probe, agent.social, studiofromthesea, Prove AI, pulse-verity, dxpert UNS tools.
