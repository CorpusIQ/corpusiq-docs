---
title: "MCP Server Discovery - September 9, 2026 (Morning Sweep)"
description: "Morning sweep over the mcp.so feed (30 server blocks) and mcpservers.org /all pages 1-3 via the r.jina.ai reader proxy. 5 new business-relevant servers catalogued with guides: Artlist (official AI creative suite), Ultimate Web Scraper (cloud catalog extraction), Emailchaser (cold email operations), DCA Method (keyless DCA backtesting, live probe-verified) and SoundGTM (partner program management, 19 server-card tools)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-09
---

# MCP Server Discovery - September 9, 2026 (Morning Sweep)

**Source:** mcp.so feed (30 server blocks, TanStack Router $R-stream), mcpservers.org /all pages 1-3 (r.jina.ai reader proxy; direct curl Cloudflare-challenged)
**Method:** feed $R-block parsing, /all slug extraction + detail-page fetch via proxy, vendor docs fetch, JSON-RPC liveness probe (tools/list)
**Date:** September 9, 2026 ~03:00 MST (10:00 UTC)

## Summary

| Metric | Count |
|---|---|
| mcp.so feed server blocks | 28 (plus 2 client-kind) |
| mcpservers.org /all pages 1-3 | 89 slugs batch-classified |
| Detail pages fetched | 33 (via r.jina.ai proxy) |
| Endpoints probe-verified | 1 (dcamethod.com/api/mcp - full tools/list, keyless) |
| New servers catalogued | 5 |
| Integration guides written | 5 |
| Skipped (not catalogued) | 404 shells, adult search, prior dispositions, thin docs, dev/consumer classes |

## New Business-Relevant Servers (5 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| Artlist MCP | artlist-mcp | Official AI creative suite - image, video, music, voice-over generation | verified + featured mcp.so listing submitted by Artlist; endpoint mcp.artlist.io/mcp over OAuth; vendor docs list 4 capabilities; Claude/ChatGPT/VS Code support |
| Ultimate Web Scraper MCP | ultimate-web-scraper-mcp | Cloud scraping platform - Shopify/WooCommerce/Magento/SFCC catalog extraction, contacts, map places, automations | mcp.so detail + vendor docs; 13 named tools; endpoint mcp.ultimatewebscraper.com/mcp, OAuth with bearer alternative |
| Emailchaser MCP | emailchaser-mcp | Official cold-email connector - 67 tools, 10 areas, scoped revocable keys | vendor MCP docs page; endpoint app.emailchaser.com/api/mcp with API key from Settings > Integrations & API |
| DCA Method MCP | dca-method-mcp | Free keyless DCA backtesting - crypto/stocks/commodities, 15+ years history | LIVE PROBE: anonymous tools/list returned list_assets, run_dca_backtest, get_method with full schemas |
| SoundGTM MCP | soundgtm-mcp | Partner program management - pipeline, deals, commissions, outreach | published unauthenticated server card (com.soundgtm/partner-tracker) with all 19 tools + scopes; OAuth 2.1 with bearer alternative |

## Findings

- **Artlist MCP**: hosted at mcp.artlist.io/mcp (Streamable HTTP, OAuth). The full Artlist AI creative suite - image generation, video generation, music generation and voice-over - as four agent tools. Official listing from Artlist (the stock media company), verified + featured on mcp.so, category Media & Design. Supported clients: Claude, ChatGPT, VS Code; Cursor and Codex not yet. Category assigned: Content (Treza video-pipeline precedent).
- **Ultimate Web Scraper**: hosted at mcp.ultimatewebscraper.com/mcp (Streamable HTTP, OAuth with bearer alternative). 13 documented tools including dedicated storefront extractors (Shopify, WooCommerce, Magento, Salesforce Commerce Cloud - one row per variant with price/SKU/stock/images), scrape_pages, extract_contacts, extract_map_places, sitemap discovery and selection, analyze_website, automation control and data cleanup. Honest free tier, paid plans via Stripe, 4,000 pages per job, location-picked proxies. Category: Lead Generation & Web Scraping (Crawdar precedent).
- **Emailchaser MCP**: hosted at app.emailchaser.com/api/mcp with scoped API keys (read-only keys supported). 67 tools (vendor claim, Sep 2026) across 10 areas: campaigns, leads, replies, sender accounts, ICPs, autopilot, credits, done-for-you infrastructure, blocklist, webhooks. Every call runs under the key's scopes and rate limits. Category: Sales & Outreach.
- **DCA Method MCP**: hosted at dcamethod.com/api/mcp (Streamable HTTP, KEYLESS). Live tools/list probe captured all three tools with schemas: list_assets (optional crypto/stocks/commodities filter), run_dca_backtest (symbol, amount, frequency daily/weekly/biweekly/monthly, date range; returns invested, final value, profit, CAGR, average buy price, best/worst month, purchase count), get_method (method summary and links). 15+ years of Yahoo Finance and CoinLore data. Free, open, educational-only. Category: Finance.
- **SoundGTM MCP**: hosted at partnertracker.soundgtm.com/api/mcp (OAuth 2.1: scopes read/read_write/openid/email; bearer key alternative). Registry name com.soundgtm/partner-tracker. All 19 tools recovered from the published unauthenticated server card with scopes and summaries - pipeline_summary, list_deals, list_stalled_deals, get_deal, update_deal_stage, convert_deal, attach_deal_to_partner, list_partners, get_partner_detail, invite_partner, list_programs, get_action_queue, get/save_ideal_partner_profile, list_pending_commissions, authorize_commissions (no money movement), mark_commission_paid (bookkeeping only), send_announcement, draft_partner_email (Gmail draft, never sends). Free up to 10 partners. Category: Marketing (Ambassly affiliate precedent).
- **GitHub API pass skipped**: prior sweeps hit the 422 spam-flagged wall; primary sources were complete.

## Non-Catalogued (Disposed or Repeats)

- **Prove AI**: mcp.so client-kind listing (startup research engine, "scores ideas with live market data") - client entry, idea-validation class with Fluenta precedent.
- **pulse-verity**: signed crypto index prices for 5,000+ assets, 5 read-only tools - crypto class.
- **Perimeter Watch**: TLS expiry, dangling DNS and lookalike-domain monitoring ($9-19/mo Stripe plans) with no published MCP endpoint or tool list - thin docs.
- **Aave MCP**: official Aave listing with "No documentation available" - thin docs.
- **Emit** (RSS-email pipes), **Emails MCP** (IMAP triage - email category saturated), **WattScope** (energy niche), **LinkScale** (link-in-bio utility), **AgentRender** (render API, working-name stage), **Collide** (agent conflict awareness), **Kontexta** (context vault), **Rogue** (agent base camp), **Torquantis** (agent marketplace), **VitaeContext** (career utility), **Lexicon** and **ContextSwitch** (macOS utilities), **Flash** (flashcards), **Index TTS** (voice cloning), **PRIMAMCP** (German geo-niche), **3DAssets Dev** (3D search), **ARADIA** (compute infra), **Nullheim** (text world), **Surli** (URL shortener).
- **Adult search excluded**: NudiTok, Desaira, tik-tok.porn.
- **404 shells**: sanggonboy, siweina, timurrakhmatullin86, artgas1, leek-emperor, explorium-ai, sharp-api, materialmodel, magenestjsc, earthkingmortal-design, ultralayerhq, juansitoai85-hub, johgirard, rulogb, liza-studio, oscardvs, snipperapp, rakutentech, cartonpliant, zsadigzade, maxweb4u, xkallex, capawesome-team, georgi-petkov.
- **Host-dump noise**: 4 exposed-port railway-app-status slugs.
- **Prior dispositions re-listed**: FlightPowers, Seedance, Wan 3.0, dxpert UNS, ego lite (sponsor).
- **Pages 2-3 repeats** ruled by the Sep 8 night sweep (Datapika family, Advisors AI, Memra, MCP ADMIN, Ergonia Works, SnipperApp, FrameThrower, Carpedia, Wellness Project, BagIQ, Capawesome, Convert3D, marketcode, export-tools, Formdall, JsonCut).
- **Feed repeats**: catalogued (Fluenta, Beamtrace, Countersignatory, Expired Domains Karma, Fruit Stand, Fundz, InstantClips, LoomaScale, Mailercloud, PostNitro, TrueClicks, VarynForge, Velarion, Yocoolab, VetAgent, Alpha Vantage) or disposed (agent.social, Alien Probe, Create Prints, Tessryx, Saaskly, YouSpot, VeriRoute, DB Planner, Dealwize, PriceMyRepair, Factanker, miniOrange, dxpert UNS, Onymu, studiofromthesea, GoBuy).

## Actions Taken

- 5 integration guides written (artlist-mcp, ultimate-web-scraper-mcp, emailchaser-mcp, dca-method-mcp, soundgtm-mcp).
- Index updated: last-updated line (596 servers, +482 guides), morning sweep section, docs-links tail block, frontmatter date.
- DCA Method endpoint live probe-verified (keyless tools/list, 3 schemas captured).
- SoundGTM server card fetched unauthenticated (19 tools + scopes).
- Pushed to main; remote hash verified.
