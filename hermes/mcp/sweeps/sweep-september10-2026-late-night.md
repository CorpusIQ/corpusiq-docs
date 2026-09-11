---
title: "MCP Server Discovery - September 10, 2026 (Late-Night Sweep)"
description: "Late-night sweep over the mcp.so feed (30 blocks), mcpservers.org /all pages 1-2 via r.jina.ai and chatmcp/mcpso issues #4036-#4054. 7 new business-relevant servers catalogued with guides, all endpoints live-probed over JSON-RPC: Reach MCP (LinkedIn account ops), Nova Amazon MCP (Seller Central profit analytics), Canarics (sales call analytics), Airside Labs (aviation reference data), YoTrends (trend content packs), SEOVally (SEO audits) and GramClaw (Telegram outreach). Plus a HasData guide refresh for 5 new per-connector listings."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-10
---

# MCP Server Discovery - September 10, 2026 (Late-Night Sweep)

**Source:** mcp.so feed (30 blocks, delta = everything above the first prior-disposition name), mcpservers.org /all pages 1-2 via r.jina.ai reader proxy (51 slugs), chatmcp/mcpso issues #4036-#4054 (19 issues)
**Method:** feed $R-block parsing, slug extraction + detail-page fetch (28 pages), live JSON-RPC probes (7 endpoints), tools/list capture on keyless endpoints
**Date:** September 10, 2026 ~19:00 MST (02:00 UTC Sep 11; night-slot rule: dates stay Sep 10, MST)

## Summary

| Metric | Count |
|---|---|
| mcp.so feed blocks evaluated | 30 (13 above the prior-disposition boundary) |
| mcpservers.org /all slugs cross-ref'd | 51 |
| Detail pages fetched | 28 |
| Live JSON-RPC probes | 7 endpoints (2 keyless with tools/list captured, 5 auth-challenged = liveness) |
| New servers catalogued | 7 |
| Integration guides written | 7 |
| Existing guides updated | 1 (HasData MCP) |
| Skipped (not catalogued) | 40+ |

## New Business-Relevant Servers (7 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| Reach MCP | reach-mcp | Operate a real LinkedIn account from an agent - 52 tools, quotas, webhooks | mcp.so feed + listing detail (full 52-tool table) + LIVE PROBE (403 OAuth-gated) |
| Nova Amazon MCP | nova-amazon-mcp | Seller Central + Vendor Central + Ads with SKU-level COGS/VAT/FBM | mcp.so feed + listing detail (15-tool table) + LIVE PROBE (401 OAuth-gated) |
| Canarics MCP | canarics-mcp | Sales-team call analytics + consent-gated AI callbacks, EU-hosted | mcp.so feed + LIVE PROBE (keyless initialize canarics v1.0.0 + tools/list captured start_signup/check_signup_status) |
| Airside Labs Aviation Tools MCP | airside-aviation-mcp | Aviation entity resolution with provenance + EASA use-case atlas | mcp.so feed + LIVE PROBE (keyless initialize v1.1.0 + tools/list captured all 22 tools) |
| YoTrends MCP | yotrends-mcp | Live YouTube/TikTok trends across 9 markets as content packs | /all detail page (8 tools) + LIVE PROBE (401 key-gated with remediation message) |
| SEOVally MCP | seovally-mcp | Scoped SEO + AI-search audits, domain comparison | /all detail page (4 tools) + LIVE PROBE (403 auth-gated) |
| GramClaw MCP | gramclaw-mcp | Telegram outreach workflows: broadcast, drip campaigns, pipeline CRM | /all detail page (6 tool groups) + LIVE PROBE (-32001 key-challenge) |

## Guide Update

- **HasData MCP** - refreshed for the vendor's five new per-connector mcp.so listings (YouTube, TikTok, Instagram, Zillow, Google Search hosted servers) and the official docs 57-API catalogue: new `youtube_*` (4 tools), `tiktok_comments`/`tiktok_search`, `facebook_profile`, `walmart_*` (3), `google_flights`, `google_images`, `google_scholar` families; 40+ -> 57 connector count; `?apis=` filtering and OAuth sign-in confirmed from docs.

## Skipped (also identified, not catalogued)

- **TruVerifAI Panel-review (mcp.so feed)** - four frontier models argue over a coding agent's riskiest designs; multi-model deliberation = agent infra class (mumo precedent).
- **Theyond (mcp.so feed)** - 2-tool job search from employer career pages; thin FoundRole duplicate, consumer job class (Web Remote Jobs precedent).
- **OpenZiti LLM Gateway + MCP Gateway (mcp.so feed)** - NetFoundry zero-trust network infrastructure; no MCP config block or tool names published (thin-docs infra class, Loadster/AuraNet precedent).
- **DropTo Run Publish (/all)** - 3-tool publish-pages-to-URL utility, no-index default, 3-day expiry; dev/content utility class (thin).
- **LoadSnap (/all)** - load-testing platform MCP; dev utility class (Loadster precedent).
- **ZMS AI Creative Suite (/all)** - text-to-video/image creative suite; media generation class.
- **MirrorFly Chat API (/all)** - chat SDK/CPaaS for developers; dev platform class.
- **DB Wizard (/all)** - self-hosted Docker Oracle MCP with config-as-security; dev infra class (self-host precedent mcp-azure-selfhosted).
- **Soprano MCP (/all slug)** - dup-listing shell of already-catalogued Soprano Connect MCP.
- **QverisAI, SignalEdi, Finamatik, Offstereo, Aceatdev, Sadri-Dridi, PennyForge** - nav-only shells / thin detail pages (~1.9KB class).
- **AANet (/all)** - agent-to-agent coordination service; agent infra class.
- **Coinranking chart (/all)** - crypto; **desk-x402 (/all)** - x402 payment class.
- **Username-style slugs** (ashishsinha1602, nagarjuna2997, rafim-dev, cvelasquez, akzar1el) - personal pages, no product surface.
- **Chinese legal-evidence docs slug (yangchunhong3000)** - geo-niche class; **ruagentic** - Russian geo-niche.
- **mcp.so issues #4036-#4054** - benchmark-submission flood (18 synthetic "benchmark MCP server" fixtures: AP exception review, 3PL invoice audit, support trials, etc. = benchmark-fixture class, no real product or endpoint), plus aiochainscan (multi-provider blockchain explorer - crypto class) and pdfcheck-mcp + sensormesh-mcp (PDF validation + sensor mesh - dev utility class).
- **Feed repeats already disposed/catalogued** (orthogonal and below: VenuNite, toll402, Loadster, priostack, pulse-verity, ultimate-web-scraper, artlist, fluenta, varynforge, expired-domains, mailercloud x2, instantclips, dxpert-uns, fundz, prove-ai client block).
- **/all page-1 names carrying Sep 9 night dispositions** per the midday sweep's own notes; page-2 overlap = confirmation signal.

## New Skip-Class Precedents (feed into catalog-precedent-map)

- **Benchmark-fixture submissions**: chatmcp/mcpso issues titled "Add benchmark MCP server: <task>-<date>-<hash>" are synthetic evaluation fixtures (12 synthetic scenarios, no public endpoint or product). Skip on sight; do not fetch details.
- **Per-connector re-listings of a catalogued gateway vendor**: HasData's five individual hosted-server listings (youtube-mcp-server, tiktok-mcp-server, instagram-mcp-server, zillow-mcp-server, google-search-mcp-server) all funnel to the same already-catalogued gateway - update the existing vendor guide with new connector families instead of creating per-connector guides (doc-URL slug re-listing class, Ryze precedent, extended to connector-split listings).

## Convention Notes

- The 03:00 MST sweep this morning shipped its report and index section under the "night" label (pre-existing convention drift, documented in sep10-morning-sweep-patterns). This 19:00 MST run is the true night slot; labeled **late-night** to avoid colliding with the shipped "night" files. Report filename uses the same disambiguation.
- Honcho tools absent from this cron session's tool registry (tool_search returned no honcho matches) - logged; shutdown handoff will go through GBrain only.
