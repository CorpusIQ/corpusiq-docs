---
title: "MCP Server Discovery - September 29, 2026 (Midday Sweep)"
description: "Midday sweep over the mcp.so /feed (30 server blocks, direct fetch) and mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy, with 4 detail pages fetched. 4 new business-relevant servers catalogued with guides: HeyLead MCP, Omentir MCP, NM Signals MCP and SMAT MCP."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-29
---

# MCP Server Discovery - September 29, 2026 (Midday Sweep)

**Source:** mcp.so /feed (30 server blocks, direct fetch) + mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy + 1 mcp.so detail page (direct fetch) + 3 mcpservers.org detail pages via the reader proxy + Omentir agent guide (omentir.com/agents.md) and SMAT connection docs
**Method:** feed slug/name pairing, /all slug extraction with token-probe cross-reference against the 734-server catalog and disposal prose, targeted context greps for generic-token hits (Failure class B), detail-page enrichment for endpoint/auth/tools, guide validation (8 frontmatter fields, em-dash scan, title length, FAQ question headings)
**Date:** September 29, 2026 10:00-11:30 MST (17:00-18:30 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 29 server blocks |
| /all entries classified | 32 (pages 1-2 via r.jina.ai proxy) |
| Detail pages fetched | 1 mcp.so direct + 3 mcpservers.org via proxy + 2 vendor doc pages |
| Candidates cross-referenced | 44 names and slugs against the 734-server catalog plus sweep disposition prose |
| New business-relevant servers | 4 |
| Integration guides written | 4 |
| Guide validation | 4/4 PASS |
| Directory listing checks | glama listed, mcpservers.org listed, smithery listed (benoit-p/Cprusiq), mcp.so not listed (moderation deletion state) |

## New Servers Catalogued (4)

**Marketing**
1. **HeyLead MCP** - LinkedIn outreach from your own account. Remote MCP at heylead.dev/mcp (Streamable HTTP) with OAuth browser sign-in, no API key. Builds two to four buyer personas from one sentence, previews the LinkedIn search, then drafts warm-up, invitation, opening message, follow-ups, InMail and email fallback per person. Approval-gated until autopilot; replies answered from campaign facts. Six campaign goals (sell, find a job, hire, find partners or investors, find a vendor, research interviews). Human-pace sending limits. Free tier plus Pro at $29 per account per month. MIT client at github.com/D4umak/linkedin-outreach-mcp.

2. **Omentir MCP** - workspace-scoped lead discovery and outreach. Remote MCP at omentir.com/api/agent/v1/mcp with OAuth (chat apps) or Bearer token (coding agents). Product profile, lead finders including CSV outreach and custom sequences, qualified LinkedIn leads, activity, send schedules, live inbox replies and workspace switching. MIT open source at github.com/vanshyadav1408/Omentir with a published agent guide at omentir.com/agents.md.

**SEO**
3. **NM Signals MCP** - AI crawler visibility audits. Remote MCP at app.nyman.media/api/mcp with Bearer auth (nms_live_ production keys, Premium or Partner plan required). Two tools: audit_url and get_quota. Designed pairing with a coding agent for a bounded audit, fix and re-verify workflow.

**Social Media**
4. **SMAT MCP** - Instagram and Facebook publishing. Remote MCP at api.smat.chat/api/mcp with OAuth sign-in, brand-scoped. Access levels at connection time: read only, create content, create with AI, full access with publishing, plus validity duration and per-action credit limits. Scopes smat:read, smat:write, smat:generate, smat:publish. Drafts, 2 to 6 slide carousels, paid caption and image generation with explicit confirmation, scheduling and publishing. Included in every paid plan (Starter, Pro, Studio) and the free trial.

## Identified, Not Catalogued

- **elmah.io MCP** - error log, deployment and org statistics access for the elmah.io error logging platform (Developer Tools category on the feed). Dev infra class.
- **Webshare** - official Webshare proxy management MCP (proxies, usage, plans, billing) with OAuth sign-in. Dev infra class.
- **trip1** - agent hotel booking paid in USDC on Base over x402, plus Trip1 agent skills. Consumer travel class.
- **AQL PropertyCheck** - Gold Coast, Australia property due diligence (planning, flood, bushfire, land use, school catchments). Geo-niche class.
- **HaberChat** - WhatsApp inbox for Claude and ChatGPT (read and send). Communication saturation class after odichat.
- **Beemm Vision** - design tool drive from Claude or Cursor (projects, workflows, gallery). Dev utility class.
- **MX Verdict** - free read-only email and DNS checks (SPF, DKIM, DMARC, MX, blacklists). Dev utility class.
- **AnswerLine** - AI answers, citations and source URLs aggregated from ChatGPT, Gemini, Copilot and Google Search. Search utility class.
- **Dive Kit** - scuba decompression and gas planning. Consumer class.
- **Robozukan** - Japanese catalog of physical devices AI agents can control. Geo-niche class.
- **SubmitraX MCP** - form backend for static sites and JAMstack apps. Dev infra class.

## Non-Business Servers (Not Catalogued)

Crypto class: The Coin Daily Research, Mooncatcher Wire, Gateway Agent Tip Jar (morning sweep dispositions respected). Consumer class: eSIM-Global.VIP, IbiPoint, e-eSIM, Upleex, Bazous, BuySignal Deals, L'Oiseau Bleu, Cybergenic Database (morning sweep dispositions respected). Feed and /all repeats already disposed by the Sep 29 morning sweep and prior sweeps: treg.to, Metabind demo, CUQU, Pocket Network, Senaro, WarpLink, Wikidata + Google Knowledge Graph MCP, disclosedby, Court Rules MCP, TaskForceAI, TinyFish, Texas RRC Wellbore Intelligence and the Sep 27 evening and Sep 28 sweep sets.

## Directory Listing Status Check

- **glama.ai/mcp** - LISTED (HTTP 200 at glama.ai/mcp/servers/CorpusIQ/corpusiq-docs)
- **mcpservers.org** - LISTED (live page at mcpservers.org/servers/corpusiq-io via reader proxy, published 17:02Z today)
- **smithery.ai** - LISTED (registry API resolves displayName CorpusIQ at benoit-p/Cprusiq)
- **mcp.so** - NOT listed ("No servers match" empty state; moderation-deletion doctrine, no re-submit)

## New Directory Search

The two-pass GitHub directory search (20 queries, unauthenticated, 212s) surfaced no new eligible MCP directory targets. All directory-style candidates were precedent-rejected (RankSpotAI flow too thin, Vaquill legal-only, xakpc .NET-only, lirantal stale) or failed the scope-fit or stale gates (MCPHubCloud 2025, melodic-software 20 stars plugin marketplace). No submissions made this cycle.
