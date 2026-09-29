---
title: "MCP Server Discovery - September 29, 2026 (Morning Sweep)"
description: "Morning sweep over the mcp.so /feed (30 server blocks, direct fetch) and mcpservers.org /all page 1 via the r.jina.ai reader proxy, with 3 mcp.so detail pages and 8 mcpservers.org detail probes. 6 new business-relevant servers catalogued with guides: systemHUB MCP, AccountHub MCP, AgentGrown MCP, Markifact Google Ads MCP, Markifact Meta Ads MCP and VoiceLabs MCP."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-29
---

# MCP Server Discovery - September 29, 2026 (Morning Sweep)

**Source:** mcp.so /feed (30 server blocks, direct fetch with browser UA) + mcpservers.org /all page 1 via the r.jina.ai reader proxy (direct curl Cloudflare-challenged) + 3 mcp.so detail pages (direct fetch) + 5 mcpservers.org detail probes via the reader proxy + 2 vendor pages (markifact.com google-ads-mcp and meta-ads-mcp)
**Method:** feed slug/name pairing, /all slug extraction with prior-sweep disposition cross-reference against the 728-server catalog and the Sep 27 evening plus Sep 28 morning, midday, evening and night disposal prose, detail-page enrichment for endpoint/auth/tools, guide validation (8 frontmatter fields, em-dash scan, title length, 3 FAQ question headings)
**Date:** September 29, 2026 03:00-04:00 MST (10:00-11:00 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 30 (29 servers + 1 client listing) |
| /all entries classified | 30 (page 1 via r.jina.ai proxy) |
| Detail pages fetched | 3 mcp.so direct + 5 mcpservers.org via proxy + 2 vendor pages |
| Candidates cross-referenced | 51 names and slugs against the 728-server catalog plus Sep 27 evening and Sep 28 morning, midday, evening and night disposal prose |
| New business-relevant servers | 6 |
| Integration guides written | 6 |
| Guide validation | 6/6 PASS |

## New Servers Catalogued (6)

**Business Operations**
1. **systemHUB MCP** - SOP software for small and medium businesses. Remote MCP at mcp.systemhub.com/mcp (Streamable HTTP) with OAuth sign-in. Lets Claude, ChatGPT or any MCP-capable AI search, draft, update and publish SOPs, policies and trainings inside the company's systemHUB account.

**Productivity**
2. **AccountHub MCP** - one MCP connection for Gmail, Google Calendar, Drive, Contacts, Slack workspaces and Notion, advertised free. Remote MCP at accounthub.ai/api/mcp with OAuth per connected account.

**Analytics & BI**
3. **AgentGrown MCP** - a site's own Google Search Console and GA4 data for coding agents. Remote MCP at agentgrown.com/mcp with Google sign-in and daily sync. Query clicks, impressions, CTR, position, sessions and conversions by query and landing page. Pay as you go, $10 free credit, failed calls free.

**Advertising & Marketing**
4. **Markifact Google Ads MCP** - approval-gated Google Ads for Claude, ChatGPT and MCP clients. Endpoint api.markifact.com/mcp/google-ads, repository github.com/markifact/google-ads-mcp, installable from the Claude directory. Reporting, account-structure audit, keyword optimization and bid/budget management, every write waiting for operator approval.
5. **Markifact Meta Ads MCP** - approval-gated Facebook and Instagram ads from the same vendor. Endpoint api.markifact.com/mcp/meta-ads, repository github.com/markifact/meta-ads-mcp. Campaign, ad set and creative drafting plus Pixel and CAPI inspection, all writes approval-gated.

**Communication**
6. **VoiceLabs MCP** - TTS, voice cloning and transcription over a hosted remote MCP at app.voicelabs.now/api/mcp (Streamable HTTP, stateless, OAuth 2.1). Seven permission-scoped tools (list_voice_profiles, list_captures, get_generation, speak and transcription tools), official registry name now.voicelabs/voicelabs, seven engines on open-source models.

## Identified, Not Catalogued

- **TaskForceAI** - supervised Agent OS for founders and small teams (brief, queue, approvals, run logs). Early access, no published pricing and no endpoint on the listing, so no guide can be written without guessing.
- **MepMail** - transactional email with a Resend-compatible API, hosted MCP at api-mepmail.je4ndev.com/mcp (OAuth) plus a local stdio server. Email category saturation precedent (Mailbox MCP disposition after Mektup, Loops and Lumail) respected.
- **WarpLink** - mobile deep links, install attribution and real-time link data.
- **Web Hygiene MCP** - live web checks for agents: sitemaps, robots.txt, URL status, broken links, feeds, citations.
- **Wikidata + Google Knowledge Graph MCP** - bounded Wikidata search with optional Google Knowledge Graph cross-checks.
- **Bankrolled.ai** - sourced money facts and scheme lookups for US/UK/CA/AU/NZ.
- **disclosedby** - dated quotes of GDPR art. 28 subprocessor lists, change tracking.
- **Court Rules MCP** - judge-level filing rules, court holidays and enforcement data for US federal courts.
- **MCP Dubai** - open-source Dubai and UAE public data and business setup knowledge (120 tools, stdio, MIT).

## Non-Business Servers (Not Catalogued)

Crypto class: The Coin Daily Research (read-only crypto research), Mooncatcher Wire (crypto news for agents), Gateway Agent Tip Jar (voluntary USDC support terms). Consumer class: Rhylthyme (personal scheduling), Bazous (household cash-flow before payday), BuySignal Deals (UK/CA retail deal search), Upleex (rental marketplace), this trip btw (itinerary maps), L'Oiseau Bleu (Paris ceramic workshops), eSIM-Global.VIP, IbiPoint and e-eSIM (travel eSIM catalogs). Scientific class: Cybergenic Database (cancer gene research). Geo-niche: Aturan.org (Indonesian legal research). Dev utility: whichlib (dependency picking), webfetch (license-first image layer).

## Verification Notes

- 6/6 guides passed validation: 8 frontmatter fields each, zero em-dashes, titles under 60 chars, 3 FAQ question headings per guide.
- Endpoints verified this cycle: systemHUB (mcp.systemhub.com/mcp), AccountHub (accounthub.ai/api/mcp), AgentGrown (agentgrown.com/mcp), Markifact Google Ads (api.markifact.com/mcp/google-ads from the vendor page), Markifact Meta Ads (api.markifact.com/mcp/meta-ads from the vendor page), VoiceLabs (app.voicelabs.now/api/mcp, published on the listing). No endpoint was guessed.
- Markifact repositories verified: github.com/markifact/google-ads-mcp and github.com/markifact/meta-ads-mcp, both named on the vendor pages.
- AgentGrown pricing verified from the mcp.so detail page: pay as you go, $10 free credit, failed calls free.
- Prior-sweep cutoff: Sep 28 night stamp 18:05Z. The feed has rolled past the night top (Firme360 client listing); systemHUB, AccountHub, AgentGrown, ohmyho.st and EQIQs form the new window, of which ohmyho.st and EQIQs were catalogued by the night sweep.
- mcpservers.org /all now shows 13,706 servers (up from 13,611 at the night sweep). Core directory listings otherwise unchanged (mcp.so NOT LISTED, quarantine, no resubmit).
