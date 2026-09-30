---
title: "MCP Server Discovery - September 30, 2026 (Morning Sweep)"
description: "Morning sweep over the mcp.so /feed (29 server blocks, direct fetch) and mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy, with 11 detail pages fetched. 7 new business-relevant servers catalogued with guides: Vouched MCP, SignalPipe MCP, MentionFox MCP, Kresmion MCP, Family Office Registry MCP, Ownware Catalogue MCP and OceanAlt AML MCP."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-30
---

# MCP Server Discovery - September 30, 2026 (Morning Sweep)

**Source:** mcp.so /feed (29 server blocks, direct fetch) + mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy + 11 detail pages via the reader proxy (5 mcp.so server pages, 6 mcpservers.org detail pages)
**Method:** feed slug/name pairing with feed-order recency (the late evening sweep's Porkbun and GAIP entries anchored the feed; the 5 entries ahead of them were evaluated fresh), /all slug extraction with name and tagline classification, two-round token-probe cross-reference against the 750-server catalog plus all disposal prose (sweep reports, .last-sweep files, index.md), context greps for generic-token hits, detail-page enrichment for endpoint/auth/tools, guide validation (8 frontmatter fields, title and description length, em-dash scan, redaction scan, FAQ question headings, See Also directory checks)
**Date:** September 30, 2026 03:00-03:30 MST (September 30, 2026 10:00-10:30 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 29 server blocks (30 slug/name pairs, 29 unique) |
| /all entries classified | 60 (pages 1-2 via r.jina.ai proxy) |
| Detail pages fetched | 11 via the reader proxy |
| Candidates cross-referenced | 67 names and slugs against the 750-server catalog plus disposal prose |
| New business-relevant servers | 7 |
| Integration guides written | 7 |
| Guide validation | 7/7 PASS |

## New Servers Catalogued (7)

**SEO**
1. **Vouched MCP** - open-source SEO data server with a provenance envelope on every fact. Endpoint vouchedhq.com/mcp (OAuth) or self-hosted on Cloudflare Workers with a bearer token. 19 read-only tools: Search Console performance and indexing, GA4 analytics, DataForSEO market data (keywords, SERPs, backlinks, competitor gaps), plus AI citation discovery and AI answer visibility, the AEO angle that keyword-only servers miss. GitHub muditjuneja/vouched, MIT, 0 stars.

**Sales & Outreach**
2. **SignalPipe MCP** - buying-intent lead detection with a three-judge swarm (Skeptic, Analyst, Optimist), nurture engine with 14 signal types and permanent objection memory, and an approval-gated sender. Endpoint api.signalpipe.io/mcp with a bearer operator key, 29 tools, $29/mo (3,000 judgements) or $79/mo (9,000). Plugin MIT licensed (AbYousef739/signalpipe, 0 stars); the managed brain is a subscription.

**Research**
3. **MentionFox MCP** - cited reports and monitoring. Endpoint mentionfox.com/mcp (OAuth or personal access key), 9 tools: source_check verifies claimed credentials against official records, get_snapshot and get_full_report write source-cited briefs, scan_for_mentions finds daily brand mentions with sentiment and buy-ready flags. Credit-based pricing with per-tool costs visible to the agent.

**Finance**
4. **Kresmion MCP** - cross-asset market intelligence with a cited source behind every record. Endpoint kresmion.com/api/mcp with a self-serve read-only bearer key, 35 tools over prediction markets (Polymarket, Kalshi), labeled whale flows, ETF flows, equity signals, 13F and congressional trades, macro regime and a published signal track record. Free during beta (10,000 calls/mo, 120 req/min), signed webhooks, bulk CSV backfills.
5. **Family Office Registry MCP** - sourced, dated records of 388 verified family offices across Switzerland, Liechtenstein, Austria, Germany and Dubai. Endpoint familyofficeregistry.com/api/mcp, keyless open tier with search_registry and get_record (25 records/page, 60 calls/hour); CHF 99/mo or CHF 890/year for full records. States explicitly what it does not hold: no AUM estimates, no personal emails, no ranking.

**ERP**
6. **Ownware Catalogue MCP** - 48 self-hosted business apps exposing 274 MCP tools: purchase approvals (Approva), fixed assets (Assetora), PO matching (Cargora), petty cash (Cashora), certificates (Certora), timesheets (Clockora) and more. Per-install endpoints at https://your-install/mcp with bearer keys that can be minted read-only (write tools then not advertised), an audit log, and no delete or outbound-email tools anywhere.

**Compliance**
7. **OceanAlt AML MCP** - AML screening with verifiable evidence receipts. Local stdio server (npx -y oceanalt-aml-mcp), 12 tools: 9 free keyless (address screening across EVM, Tron, Solana and Bitcoin, payee readiness, control baseline checks, calldata intent decoding, signed requirements verification, payment gate) and 3 paid x402 tools ($0.10 to $0.30 in USDC on Base). The wallet key stays local and signs only one authorization per paid call.

## Identified, Not Catalogued

- **prodready** - free code due-diligence (118 read-only checks, 18-dimension review) plus a paid SDLC delivery suite. Dev infra class, per the MeroFoundry ruling.
- **RichAPI** - live B2B enrichment waterfalls billed only on verified records. Saturation class after Databar.ai and Deeplead.
- **Anomaly AI** - AI data analyst for spreadsheets; the detail page carries no published MCP tools, endpoint or auth. Thin docs class.
- **uplika** - hosted multi-channel social publishing (Threads, Instagram, YouTube, Facebook, Bluesky, Telegram). Saturation class after ContentStudio, SMAT, PostBazooka and BulkPublish.
- **dum** - approval-gated campaign planning and on-brand post drafts. Saturation class after Rebbel, which shipped the same positioning in the late evening sweep.
- **How To Make Money On Snapchat** - five read-only tools returning Snap creator-monetization rules. Creator-monetization niche.
- **MemeSwap MCP** - memecoin research reads, route quotes and unsigned transaction construction. Crypto class.

## Non-Business Servers (Not Catalogued)

The /all pages 1-2 consumer, geo-niche and dev-utility slugs were disposed this cycle: Cody (Slack support ops, saturation after Userport and Odichat), Suggix (product feedback and roadmap), Adviserry (newsletter digest), Tempi (meeting booking), PDFHaul (PDF utilities), Hookova (creator utility), LinkBunny (nofollow link assignments), MateMCP, Swebsy, Tokmeter, LiteLambda, NoMac, Symbioza, Friday, Arroway, Pizza Developer, AgentHop, Auth Your Agent, GeoSource-MCP, ImmoDocs, Gilbert, Clipy, VideoGen, betterimage, AI was here, SelectaRank, pcb.express, TrueProxies, Apify LintLab, Monocrawl, Jagent Graders, ECRP, CovaSyn, Revit Model MCP, ssh-mcp, Orisu, 3D Texel Design, Garmin Training, Agentboxd (email class saturation), Agent Credit Bureau, Well Prepped Life Booking, Bay Area Mobile Dog Wash, Lifeguard Training NY and Tradehand. Prior dispositions respected: elmah.io MCP and Minimax H3. Feed repeats already disposed or catalogued by prior sweeps: trip1, Webshare, AQL PropertyCheck, Firme360, TokElements, MeroFoundry, systemHUB, AccountHub, AgentGrown, ohmyho.st, Selfstorming, Porkbun, Rebbel, Dumpster Controls, Unipile, fAlpha, GAIP Agents and HeyLead.

## Directory Listing Status Check

Carried forward from the Sep 29 late evening sweep, not re-verified this cycle: glama.ai listed, mcpservers.org listed, smithery listed (benoit-p/Cprusiq), mcp.so not listed (moderation deletion state), PulseMCP listed.

## Verification Notes

- Work ran on the Spark clone (HEAD 082ab2d1b pre-sweep, one commit ahead of remote from the late evening sweep). The Mac Mini clone was level on catalog counts and was resynced after push.
- Feed timestamps skew ahead of wall clock (observed up to 12 hours); feed ORDER was the recency signal, anchored on the late evening sweep's Porkbun and GAIP entries.
- The first feed parse captured only 15 of 29 server blocks (regex shape); the second pass with slug/name pairing captured all 30 pairs and surfaced three extra fresh entries (uplika, How To Make Money On Snapchat, MemeSwap MCP), all disposed.
- Real star counts from unauthenticated GitHub API: vouched 0, signalpipe 0. Both recorded as-is per the young-repo precedent.
- No live endpoint probes were needed: all 7 catalogued servers publish their endpoint and auth on the listing or in vendor docs.
- Zero invented tool names: Vouched and SignalPipe tool tables come from the listings' published tables; Kresmion groups come from its OpenAPI-backed product areas; Ownware and OceanAlt groups come from the vendor-published tool lists.
