---
title: "MCP Server Discovery - September 15, 2026 (Midday Sweep)"
description: "Midday sweep over the mcp.so feed (fresh blocks past the morning cutoff via the r.jina.ai reader proxy: Zenith, StoryStudio, Agent Margin Router, Glasser, CoDesign), chatmcp/mcpso issues #4148-#4153 and an mcpservers.org /all pages 1-3 re-check. 6 new business-relevant servers catalogued with guides: Zenith MCP (PSD2 bank sync), Glasser MCP (pay-per-use data APIs), AurasPay Merchant MCP (scoped payment review and links), CoDesign MCP (editable design engine), StoryStudio MCP (AI media studio) and Litescrape MCP (keyless search)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-15
---

# MCP Server Discovery - September 15, 2026 (Midday Sweep)

**Source:** mcp.so feed (fresh blocks past the 10:13Z morning cutoff via the r.jina.ai reader proxy), chatmcp/mcpso issues #4148-#4153 (fresh window past the morning cutoff at #4147), mcpservers.org /all pages 1-3 re-check via the r.jina.ai reader proxy
**Method:** feed proxy parse with slug pairing, issue-body review (GitHub API, local token), mcpservers.org /all slug re-check (diff vs morning crawl), mcp.so detail pages via the r.jina.ai reader proxy (5 fetches), vendor docs fetches (glasser.ai/docs, mcp.auraspay.com, storystudio.cc, litescrape.com, github.com/tillbooks), anonymous JSON-RPC endpoint probes (4 endpoints, all live 401 auth gates), guide frontmatter validation (8 fields x 6 guides, em-dash scan, redaction scan)
**Date:** September 15, 2026 17:00-18:00 UTC

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 30 (mcp.so, via r.jina.ai proxy) |
| Fresh feed blocks past cutoff | 5 (Zenith, StoryStudio, Agent Margin Router, Glasser, CoDesign) |
| GitHub issues reviewed | 6 (#4148-#4153) |
| Detail pages fetched | 14 (mcp.so + vendor docs via r.jina.ai proxy) |
| Endpoint probes | 4 (all HTTP 401 auth gates, all live) |
| New business-relevant servers | 6 |
| Integration guides written | 6 |

## Core Listing Re-checks

- **mcpservers.org:** LISTED - detail page served via the r.jina.ai reader proxy (title "CorpusIQ MCP Server | Awesome MCP Servers", 40+ connectors in the body). Direct curl returns the standing Cloudflare 403.
- **glama.ai:** LISTED - direct slug /mcp/servers/@corpusiq/corpusiq-docs returns 200, title "corpusiq by CorpusIQ | Glama".
- **mcp.so:** NOT LISTED - SSR search shows zero server cards (2 hits = query echo only); no resubmit (account quarantine holds).
- **smithery.ai:** FLIP-FLOP continues - registry search (q=corpusiq) returns the CorpusIQ entry at benoit-p/Cprusiq, while the direct /server/@benoit-p/Cprusiq page 404s at check time. No submission path exists; no action.
- **New-directory scan:** 20-query pass-2 GitHub search (275 candidates). No new submittable MCP directory targets this cycle; all candidates screened against the skip list and status ledger, with fresh rejects logged in the rejected-candidates ledger.

## New Servers Catalogued (6)

1. **Zenith MCP** - PSD2 bank sync for European bookkeeping: 2,400+ banks across 30 countries, normalized transactions (date, counterparty, amount, currency, EUR conversion, balance, category), multi-bank and multi-entity, strictly read-only, OAuth. Endpoint mcp.verified 401 auth gate at sweep time.
2. **Glasser MCP** - pay-per-use data APIs behind one hosted endpoint: seven tools (search, inspect, run, runs_get, runs_list, runs_stop, balance) with inspect-before-run pricing from a shared Workspace balance; OAuth sign-in or API key. Endpoint 401-verified.
3. **AurasPay Merchant MCP** - scoped merchant payments: payment requests, receipts, QR images, CSV export, dashboard stats and review-gated payment links over OAuth 2.0 with PKCE. Merchant developer preview; endpoint 401-verified.
4. **CoDesign MCP** - editable design engine via IMG.LY CE.SDK: structured scenes instead of pixels, brand kits, PSD/IDML/PowerPoint/PDF import, print-ready export, batch variants. npx stdio package @imgly/codesign-mcp.
5. **StoryStudio MCP** - image, video, voice and music generation studio in the agent: Nano Banana 2, GPT-Image 2, FLUX 1.1 Pro, Veo 3.1 Fast, Seedance 2.5, Kling, MiniMax, Wan; Cast & World character consistency; timeline and MP4 export; OAuth with a free 5-credit plan. Endpoint 401-verified.
6. **Litescrape MCP** - keyless search for agents: eight tools (Google, Bing, DuckDuckGo, Google Maps, plus key-only AI Mode, AI Overview, Shopping), free daily allowance per network, npm litescrape-mcp-server 0.1.1 with provenance, official MCP registry entry.

## Identified, Not Catalogued

tillbooks #4148 (pre-alpha Swiss accounting MCP - npm package reserved but unpublished; re-check when installable); toolc #4149 (optimizing compiler for agent tool surfaces - dev utility class); benchmark fixture #4151 (cleo-z37 - benchmark infra class); Litescrape duplicate #4152 (closed by submitter; #4153 canonical); Agent Margin Router (x402 wallet-funded pay-per-call on an ephemeral railway.app endpoint - integration friction, crypto class); /all pages 1-3 unchanged since the morning crawl (all slugs already catalogued or previously disposed).
