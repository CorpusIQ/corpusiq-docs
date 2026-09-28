---
title: "MCP Server Discovery - September 28, 2026 (Morning Sweep)"
description: "Morning sweep over the mcp.so feed (30 server blocks, direct fetch) and mcpservers.org /all page 1 via the r.jina.ai reader proxy, with 16 detail pages fetched. 12 new business-relevant servers catalogued with guides: iMario MCP, AgileHero MCP, Faivelo MCP, Scribase MCP, Menivor MCP, Audiogram API MCP, Cortex MCP, SkillsInput MCP, ParrotNotes MCP, AI Layoffs MCP, Cooper Email MCP and Postfleet MCP."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-28
---

# MCP Server Discovery - September 28, 2026 (Morning Sweep)

**Source:** mcp.so feed (30 server blocks, direct fetch, browser UA) + mcpservers.org /all page 1 via the r.jina.ai reader proxy (direct curl Cloudflare-challenged) + 16 detail pages (mcp.so server pages direct, mcpservers.org detail pages via the reader proxy)
**Method:** feed slug/name pairing with age text, /all slug extraction with prior-sweep disposition cross-reference, detail-page enrichment for endpoint/auth/tools, guide validation (8 frontmatter fields, em-dash scan, redaction scan, title length)
**Date:** September 28, 2026 03:00-04:00 MST (10:00-11:00 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 30 (mcp.so, direct fetch) |
| /all entries classified | 30 (page 1 via r.jina.ai proxy) |
| Detail pages fetched | 16 (mcp.so direct + reader proxy) |
| Candidates cross-referenced | 56 tokens against 711-server catalog + Sep 27 disposal list |
| New business-relevant servers | 12 |
| Integration guides written | 12 |
| Guide validation | 12/12 PASS |

## New Servers Catalogued (12)

**Research and project management**
1. **iMario MCP** - synthetic audience research at mcp.imario.ai/mcp. Customer data plus a 5.4-billion-person panel across 59 markets become synthetic audiences calibrated on real data that an assistant can question for pricing, positioning and feature decisions.
2. **AgileHero MCP** - all-in-one agile workspace at mcp.agilehero.io/mcp. Board, backlog, roadmap, whiteboards, retros, metrics and wiki as shared agent tools (promoted from the Sep 27 backlog).
3. **Cortex MCP** - shared knowledge substrate at cortex.page. 70+ permission-checked MCP tools per instance, pages and atoms with embeddings, revision history, agent signup flow via /api/agent-signup, free private workspace.

**Email and communication**
4. **Faivelo MCP** - business email on your own domain at faivelo.com/api/mcp. Read, search and send mail, manage mailboxes and aliases, automatic DNS setup, flat plan with unlimited mailboxes (promoted from the Sep 27 backlog).
5. **Cooper Email MCP** - agent-created inboxes at cooperemail.com/mcp. OAuth 2.1 + PKCE or Bearer keys, cooper_onboard consent flow, published OAuth discovery endpoints.
6. **Postfleet MCP** - agent email infrastructure at api.postfleet.ai/api/mcp. 16 named tools, prompt-injection screening, schema extraction, draft lifecycle with 202 pending_approval gate, npm @postfleet/mcp for stdio.

**Data and databases**
7. **Scribase MCP** - hosted Postgres for coding agents at api.scribase.com/mcp. 44 tools, confirm-gated writes, RLS isolation proven by policy.test before schema.apply, preview branches with sanitized data.
8. **AI Layoffs MCP** - open AI-attributed layoffs register at ailayoffs.org/mcp. No key, CORS-enabled, 0-100 job-loss index with three components and 111 source-cited events, JSON index plus CSV register.
9. **Audiogram API MCP** - podcast search and transcript retrieval at mcp.audiogramapi.com/mcp. Coverage varies by episode; connector flow documented per client.

**Marketing and productivity**
10. **Menivor MCP** - agent-produced vertical video ads at menivor.com/api/mcp. Reel writing, product-page-to-ad, cost quote before render, scheduling and performance, Bearer key, server.json manifest.
11. **ParrotNotes MCP** - in-person meeting notes library at mcp.parrotnotes.app/mcp. Dynamic Client Registration, no API key, search, summarize and save-insights-back tools over the recorded library.
12. **SkillsInput MCP** - career tools at mcp.skillsinput.ai/mcp. Job search, skills intelligence, career roadmaps and resume building, installable with npx add-mcp.

## Identified, Not Catalogued

- **Crypto and on-chain class:** TRDEFI (stablecoin liquidity), Kairos Signal (DePIN telemetry), Capacity Attest (EAS/ERC-8004 attestations).
- **Geo-niche and design utilities:** CUQU (CN social meetups), 550W AI subtitle and watermark removal (CN, two listings), UpRes (image upscaling), Lightdrift (stock images).
- **Dev utilities and personal projects:** Grill (OpenRouter-key decision checker), since-cutoff (Python API diffs), Inferrail (local cost visibility), System One Connector (vague eval connector).
- **Local-personal and consumer class:** Recordist Gateway (localhost meeting app bridge), WhichTrim (vehicle records lookup).
- **Repeats and prior dispositions:** Agent Traffic Lab and Screen Browser (Sep 27 disposed), TheLuckyStrike suite relistings (catalogued as Sep 13 Ops Suite), Etincel (already catalogued).
- **Backlog carried:** Kondo, Telebrief, Wakala, Postbox Services (Sep 27 backlog items whose sources sit on /all pages 2-3, outside this sweep's page-1 window).

## Verification Notes

- 12/12 guides passed validation: 8 frontmatter fields each, zero em-dashes, zero redaction markers, titles under 60 chars, 3 FAQ question headings per guide.
- All endpoint URLs come from vendor pages or directory detail pages fetched this cycle; no endpoint was guessed. Cortex is per-instance and documented as such.
- Tool names: Postfleet (16 named from vendor repo), Scribase (2 named, schema.apply and policy.test), Cooper (cooper_onboard named); the rest use prose-derived capability tables with the live-tool-list caveat per doctrine.
- Prior-sweep cutoff: Sep 27 evening stamp 2026-09-28T02:19:18Z. Feed entries 0-2 (iMario 4h, CUQU 2h, AgileHero 8h) plus /all page 1 fresh slugs formed the new window.
