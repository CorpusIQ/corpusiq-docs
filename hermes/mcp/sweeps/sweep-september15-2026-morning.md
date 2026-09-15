---
title: "MCP Server Discovery - September 15, 2026 (Morning Sweep)"
description: "Morning sweep over the mcp.so feed (30 server blocks via the r.jina.ai reader proxy - four fresh names above the Sep 14 evening cutoff: AIsa 5h, qrp-mcp 4h, Aard 3h, Checkout Page 2h), chatmcp/mcpso issues #4140-#4147 and mcpservers.org /all pages 1-3 via the r.jina.ai reader proxy. 8 new business-relevant servers catalogued with guides: AIsa MCP (950+ data APIs behind one OAuth key), Aard MCP (macroeconomic data from 170+ official publishers), Checkout Page MCP (40-tool Stripe-native commerce), Cite42 MCP (26-tool AI visibility tracker), Umami MCP (official 23-tool analytics), Get Ads MCP (388 tools across 9 ad sources), Wrenda MCP (per-domain edge MCP with AI citation tracking) and WhatsMCP MCP (WhatsApp numbers for agents, re-check promoted)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-15
---

# MCP Server Discovery - September 15, 2026 (Morning Sweep)

**Source:** mcp.so feed (30 server blocks via the r.jina.ai reader proxy), chatmcp/mcpso issues #4140-#4147 (fresh window past the evening cutoff at #4139), mcpservers.org /all pages 1-3 via the r.jina.ai reader proxy
**Method:** feed proxy parse with slug pairing, issue-body review (GitHub API, local token), mcpservers.org /all slug batch-classification, mcp.so detail pages via the r.jina.ai reader proxy (4 fetches), vendor docs fetches (whatsmcp.com/docs/mcp, cite42.dev/docs, aard.ai, 13 mcpservers.org server pages), guide frontmatter validation (8 fields x 8 guides, em-dash scan, redaction scan)
**Date:** September 15, 2026 10:00-11:00 UTC

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 30 (mcp.so, via r.jina.ai proxy) |
| /all entries classified | 90 across pages 1-3 (via r.jina.ai proxy) |
| GitHub issues reviewed | 8 (#4140-#4147) |
| Detail pages fetched | 21 (mcp.so + mcpservers.org + vendor docs via r.jina.ai proxy) |
| New business-relevant servers | 8 |
| Integration guides written | 8 |

## Core Listing Re-checks

- **mcpservers.org:** LISTED - /all page 1 served fresh via the r.jina.ai reader proxy (12,712 total servers shown).
- **mcp.so:** NOT LISTED (CorpusIQ) - unchanged; no resubmit (account quarantine holds).

## New Servers Catalogued (8)

1. **AIsa MCP** - hosted GTM data stack: one OAuth key in front of 950+ data APIs across SEO and AI visibility (DataForSEO, Semrush, Ahrefs), finance, social, web search, sales and agent mail. Five routing tools (search, get_details, list_categories, use, batch_use) with a max_price_usd cap enforced before any spend; category endpoints preload 32-84 tools. Endpoint mcp.aisa.one/mcp, official registry one.aisa/mcp.
2. **Aard MCP** - macroeconomic and official data from 170+ publishers (World Bank, IMF, BIS, ECB, Eurostat, national statistical offices) over a metadata-universe graph and concept ontology with per-datapoint provenance; supporting skills for agent reasoning. Endpoint api.aard.ai/mcp, OAuth, verified and featured on mcp.so.
3. **Checkout Page MCP** - 40-tool commerce server: checkout pages, events and tickets, bookings, forms, customers, payments, subscriptions, invoices, coupons, tax rates, files and webhooks, with payments on the merchant's own Stripe account. Endpoint mcp.checkoutpage.com, OAuth.
4. **Cite42 MCP** - 26-tool AI search visibility tracker: brand rankings, AI citations and competitor presence across ChatGPT, Claude, Perplexity, Gemini and Google AI Overviews, plus SEO keywords, search/Reddit/YouTube trends and scheduled trackers. npx -y @cite42/mcp stdio with CITE42_API_KEY; $1 free start.
5. **Umami MCP** - official Umami analytics server: 23 read-only tools over the Umami API with web-app permission parity (websites, stats, traffic, metrics, events, sessions, funnels, goals, journeys, retention, attribution, revenue, Core Web Vitals). Cloud endpoint cloud.umami.is/mcp or self-hosted with MCP_ENABLED=1; package @umami/mcp.
6. **Get Ads MCP** - 388 tools across 9 ad sources (Google Ads, Meta Ads, TikTok Ads, Pinterest Ads, Snapchat Ads, Search Console, GA4, Microsoft Advertising 39, Reddit Ads 50 pending). Free read-only plan, organization-scoped accounts, confirm-gated write previews. Endpoint mcp.getmcpads.com/mcp.
7. **Wrenda MCP** - per-domain edge MCP for AI visibility: edge enrichment into markdown with schema, FAQs and entity expansion (up to 12x tokens), crawler pre-rendering for JS-heavy pages, AI citation tracking across six answer engines with drift alerts, and Search Console causal-impact experiments (early access). JSON-RPC at POST /.well-known/mcp; DNS CNAME onboarding.
8. **WhatsMCP MCP** - WhatsApp numbers for AI agents: link a number, mint a workspace-scoped key, agents send and read messages over JSON-RPC. OAuth or Bearer/x-api-key auth at app.whatsmcp.com/mcp, per-number message/contact/call console, inbound webhooks, plan-capped usage. Promoted from the Sep 14 evening re-check disposition after vendor docs confirmed the full product surface (repo github.com/whatsmcp/mcp).

## Identified, Not Catalogued

Benchmark fixtures #4140/#4144/#4147 (cleo-z37, benchmark infra class); Plopino #4141 (share-link class, ctxt.io precedent); kb #4145 (dev utility); Statsnet #4143 and ReadyAgents #4146 (prior dispositions); qrp-mcp and Vivu (prior dispositions); share/artifacts, OpenRevenue, Zens AI (thin docs); ToolForte, Klyf, ALPNAI (utility/creator/dev classes); TTMT, signals-x70, Automan, IraniWallet (crypto/geo-niche/marketplace classes); Readdit Later (consumer); Brain Protocol (agent memory); 404 shells (noteflowai, joinwell52-ai, smartoire); author-slug shells; /all repeats already catalogued or previously disposed (Helio, geolint, Serp Sidekick, Prism, Nebelus, CherryShot, Foliyo, Convert.Online, RankJot, Statable, Day Off, Gambot, Statiko, Radicado Uno, Hilead, Soprano Connect, B2B Creators, CraftStory, VerifyAPI, SenseFold, eSIMfly, Visual Sandbox, PIL, vokse, fax-plus, Microburbs, MiniMax H3 and the Sep 14 disposed set).
