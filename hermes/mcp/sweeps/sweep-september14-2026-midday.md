---
title: "MCP Server Discovery - September 14, 2026 (Midday Sweep)"
description: "First sweep after the September 13-14 network outage. Midday sweep over the mcp.so feed (30 server blocks via the r.jina.ai reader proxy), chatmcp/mcpso issues #4090-#4134 and a fresh mcpservers.org /all page-1 crawl. 6 new business-relevant servers catalogued with guides: Statable MCP (cookieless web analytics, 25 tools), Day Off MCP (PTO and time tracking), Gambot MCP (WhatsApp Business messaging and CRM, 77 tools), Radicado Uno MCP (Colombian company due diligence, 6 tools), Statiko MCP (Telegram channel intelligence, 10 tools) and Hilead MCP (signal-based B2B prospecting)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-14
---

# MCP Server Discovery - September 14, 2026 (Midday Sweep)

**Source:** mcp.so feed (30 server blocks via the r.jina.ai reader proxy), chatmcp/mcpso issues #4090-#4134 (fresh window past the night sweep's #4089 cutoff), mcpservers.org /all page 1 via the r.jina.ai reader proxy
**Method:** feed proxy parse, /all slug batch-classification, issue-body review, mcp.so detail pages via the r.jina.ai reader proxy, npm registry verification, JSON-RPC live probes
**Date:** September 14, 2026 ~09:45-11:00 MST (Sep 14 16:45-18:00 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 30 (mcp.so, via r.jina.ai proxy) |
| /all page-1 entries classified | 30 (via r.jina.ai proxy) |
| GitHub issues reviewed | 45 (#4090-#4134) |
| Detail pages fetched | 5 (mcp.so server pages) |
| npm packages verified | 2 (gambot-mcp 1.0.0, @statable/mcp 0.1.0) |
| Endpoints live-probed | 5 (4x HTTP 401 auth gates, 1x open initialize) |
| New business-relevant servers | 6 |
| Integration guides written | 6 |

## Core Listing Re-checks

- **mcpservers.org:** LISTED - direct curl hits the 403 Cloudflare wall; r.jina.ai reader proxy returns 200 with title "CorpusIQ MCP Server | Awesome MCP Servers" and the full listing copy.
- **glama.ai:** LISTED - canonical slug /mcp/servers/@corpusiq/corpusiq-docs returns HTTP 200.
- **smithery.ai:** LISTED - registry `?q=corpusiq` returns benoit-p/Cprusiq, displayName CorpusIQ, unlisted=false; no flap this cycle.
- **mcp.so:** NOT LISTED - SSR search shows zero /server/ links and only query-echo hits; account quarantine holds (~52nd cycle), no resubmit.
- **PulseMCP:** LISTED - proxy 200, title "Official CorpusIQ MCP Server | PulseMCP".
- **toolsbot.com:** NEW - LISTED (submitted Sep 12 via web form): homepage schema.org ItemList position 1 and card with the submitted description linking to corpusiq.io; canonical /t/ slug page not yet resolving (card href renders as /t).
- **agentndx.ai:** NOT LISTED - control slug identical to /agents/corpusiq (catch-all shell); escalation gate (due Sep 14) reached, flagged for the watch cycle.

## New Servers Catalogued (6)

1. **Statable MCP** - EU cookieless web analytics; 25 tools (traffic, breakdowns, conversions, live, setup); OAuth remote at mcp.statable.com/mcp, stdio via npx @statable/mcp; endpoint 401-verified live.
2. **Day Off MCP** - PTO and time tracking for 50,000+ companies; leave, attendance, timesheets, approvals, reports; OAuth at mcp.day-off.app/mcp; endpoint 401-verified live.
3. **Gambot MCP** - WhatsApp Business API (Meta-approved BSP); 77 documented tools across messaging, templates, campaigns, CRM records, money documents, users and onboarding; stdio via npx gambot-mcp, MIT repo; npm gambot-mcp 1.0.0 verified.
4. **Radicado Uno MCP** - Colombian company due diligence; 6 source-linked tools (SECOP II procurement, RUES registry, NIIF financials, sanctions/OFAC signals, procurement network, source freshness); bearer key at mcp.radicadouno.co/mcp; endpoint 401-verified live.
5. **Statiko MCP** - public Telegram channel intelligence; 10 read-only tools (trending topics, channel profiles and metrics, similar channels, post history, post stats, timeline); initialize and tools/list open; tool calls need Pro or Business (Pro from $20/mo).
6. **Hilead MCP** - signal-based B2B prospecting; funding, hires, expansion and tech-change signals; read-focused OAuth 2.1 scopes with sending and enrichment deliberately not exposed; from $49/mo; endpoint 401-verified live.

## Also Identified (not catalogued)

Fax.Plus (fax send/receive - comms utility class), vokse (household budgeting - consumer personal-finance class), Visual Sandbox (multi-model media generation - media generation class), PIL (personal Instagram library - personal knowledge class), SenseFold (personal Markdown memory - personal library class), Innovalyxx Sovereign Edge (x402 cyber-physical tools, client-listing class), eSIMfly MCP (eSIM business API - communication utility class, npm @esimfly/mcp present). Fresh issue window: AnkusDrive #4090 (FreeCAD 280+ tool CAD suite - industrial CAD class), Hicortex #4091 (agent fleet memory), design.60fps #4092 (iOS motion library - dev), inferenceindexer #4093 (inference pricing - FinOps/dev), HiringIndex #4094 (job postings from thirteen ATS boards - jobs class, OpenHire sibling), Apify Public Data Scrapers #4095 (Apify family covered), FractalAI #4096 (post-quantum x402 proofs - crypto), EmpirioLabs #4097 (live endpoint, product surface not yet documented - thin docs), snapmcp #4098 (visual captures - dev utility), Dasha Compute #4100 (prior disposition), Utuh watcher #4102 (thin utility), Fee Optimizer #4103 (crypto venue fees), SmartTokenGuard #4104 (AI video credit guard - dev utility), Microburbs #4126 (Australian property data - geo niche), AssetFare #4127 (crypto routing), Penniless Data Utilities #4128 (x402 tooling), Przypominamy #4129 (Polish SMS/voice - geo niche), mcptask.online #4130 (agent dev infra), OutfitMaker #4131 (consumer), JetAPI #4132 (multi-channel messaging gateway - utility class), benchmark fixture #4133, Tegas #4134 (AI video shorts - media generation), and the HasData per-connector family #4115-#4125 (covered by the HasData 57-API family guide). mcpservers.org /all page 1 carried utility, dev and author-shell slugs (paged-website-upload, anew, GPT Image 2.5, Fidelis local memory, crossplane, statsnet, apify-scrapers, browsermcp, melbis, aria-icons, eaglevirtual, eigma, maxion, data-olympus, gadak-dev, the mcginnis OSS-tool family, captionpipe, paxaver, xfinlab, movie-planner) with no fresh business-relevant finds. Feed repeats already catalogued or previously disposed (B2B Creators, CraftStory, LandLens One, Draxlr, RedReplier, Recordwire, VerifyAPI, Mobile Text Alerts, SomaCheck, Midpoint Card Prices, Tribeunal, TruVerifAI, UmmahAPI, SimFuse, UX Jobs, NinjaChat) carry their prior dispositions.

## Directory Maintenance Notes

- No new directory submissions fired this cycle: the pass-2 GitHub discovery run (20 queries, 250 candidates) was saturated with skill-marketplace and pre-rejected repos; the four fresh candidates screened all failed vetting (Ibexoft/awesome-startup-tools-list and Think-Cube/Ecommerce-Awesome have issues disabled; elenahao66/Awesome-billing-automation has zero issue/PR flow; ScaleLeap/awesome-amazon-seller is a weak fit). Rejects logged to references/rejected-directory-candidates.md.
- Pre-submission duplicate scan clean: 8 open + 7 closed corpusiq issues and 3 PRs, all in known repos (adw0rd duplicates, best-of-ai, Scottcjn, TensorBlock, NousResearch, corpusiq-docs #105).
- toolsbot.com verified live 2 days after submission; agentndx.ai watch escalated per the pre-armed Sep 14 gate.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [MCP Ecosystem Sweeps](/docs/hermes/mcp/sweeps)
