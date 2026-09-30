---
title: "MCP Server Discovery - September 30, 2026 (Midday)"
description: "Midday sweep of the mcp.so feed and mcpservers.org: four new servers catalogued with integration guides, plus core listing verification."
category: mcp-directory
tags: [mcp, discovery, sweep, directories]
---

# MCP Server Discovery - September 30, 2026 (Midday)

**Date:** September 30, 2026 10:00-11:10 MST (September 30, 2026 17:00-18:10 UTC)
**Sources:** mcp.so /feed (30 server blocks, direct fetch, browser user agent) and mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy, with seven detail pages fetched.
**Result:** 4 new business-relevant servers catalogued with guides. Catalog 757 to 761 servers, guides +643 to +647.

## Discovery

Feed-order recency: the morning sweep's OceanAlt AML entry anchors the feed, so the two entries ahead of it (Aayat AI, Povver) were evaluated fresh. Both are genuinely new and both were catalogued. The `/all` pages carried two more (Adviserry, Blog2Social) that the morning sweep had not reached. Everything else in the feed and on `/all` pages 1-2 was a repeat of prior dispositions, checked against the morning sweep ledger prose and the `external/.last-sweep` file.

## New servers catalogued

- **Povver MCP** (Fitness and training data, read and write) - 38 tools over Streamable HTTP at `mcp.povver.ai/mcp`, OAuth sign-in for browser clients or a bearer API key for Cursor, Windsurf, Claude Code and scripts. 25 read tools cover set-level history, per-lift strength climbs, muscle volume, plateau detection and the recommendations queue; 13 write tools cover routines, templates, finished workouts, coach memories and periodization plans; 3 more are marked destructive so clients confirm first. Live set-by-set logging is deliberately not exposed. Vendor docs publish the full tool list, so nothing here is inferred.
- **Aayat AI MCP** (Pay-per-use data and tools) - 160 tools behind one keyless endpoint at `aayatai.com/mcp`, metered per call rather than per seat. Crypto token safety and rug checks, cited web search, page-to-Markdown, current library docs, package safety, company research and UK/EU open data. 20 free calls a day, then USDC over x402 or prepaid credits. A live `tools/list` probe returned HTTP 200 with real tool schemas (`token-safety` at $0.02 per call), and failed calls are never charged.
- **Adviserry MCP** (Newsletter knowledge base and drafted actions) - 13 tools at `adviserry.com/api/mcp` behind a bearer token. Source search across newsletter panels and uploaded documents, panel and issue reads, proactive insight readback, and a distinct action layer: `search_actions` and `get_actions` return copy-ready deliverables with the sources they were built from, `update_action_status` marks them shipped and feeds future synthesis, and `get_user_context` / `update_context` manage the advisor profile with a confirmation preview on anything destructive. 500 tool calls per rolling hour.
- **Blog2Social MCP** (Multi-network social publishing) - hosted server at `api.blog2social.com/mcp` over OAuth, spanning 30+ social, blogging and community networks with per-network post types and media support. Nineteen documented REST operations cover user auth, network connect and list, post create and remove, and video upload. Included for reach breadth with a saturation note (see below).

## Core listing verification

- **mcpservers.org:** LISTED. Direct curl returns the Cloudflare 403 wall; the reader proxy returns the CorpusIQ MCP page with the product tagline, so the listing is live.
- **glama.ai/mcp:** LISTED. The `@corpusiq/corpusiq-docs` slug returns 301 (redirect to the canonical listing).
- **smithery.ai:** registry entry present at `benoit-p/Cprusiq`. No submission path exists (login-walled), and the listing flips multiple times per day, so no action taken.
- **PulseMCP:** LISTED. Reader proxy title reads Official CorpusIQ MCP Server.
- **mcp.so:** NOT LISTED. The search SSR payload carries no server cards; the account-level instant moderation state from August 12 still stands, so no resubmission was attempted.

## Also identified (not catalogued)

Povver-adjacent consumer fitness entries aside, the following were evaluated and disposed in this sweep. From the mcp.so feed: prodready, uplika, How To Make Money On Snapchat, MemeSwap MCP, MeroFoundry, Rebbel, Dumpster Controls, Unipile, fAlpha, TokElements, GAIP Agents, HeyLead, elmah.io MCP, trip1, Webshare, Firme360, systemHUB, AccountHub, AgentGrown, ohmyho.st, EQIQs, Selfstorming, Uxia, Texas RRC Wellbore Intelligence and TinyFish - all either catalogued by earlier sweeps or disposed in their ledgers. From `/all` pages 1-2: TrackIQ (Amazon seller analytics, to be evaluated next cycle with a detail fetch), pdf.net (PDF editing in chat, commodity document utility), SMAT (OAuth social publishing, saturation class after ContentStudio, Rebbel and Blog2Social), HaberChat (WhatsApp inbox, saturation class after Odichat), Agent Credit Bureau (crypto risk assessment over x402), ECRP (elder care resource planning, consumer care-navigation niche), Well Prepped Life (Bay Area meal-prep booking, regional consumer service), Beemm Vision, MX Verdict, AnswerLine, Dive Kit, Robozukan, SubmitraX and Tempi.

## Skip classes added

- **Commodity in-chat document tools:** pdf.net joins PDFHaul and PDFGate as a saturated class unless the server exposes something beyond editing and merging.
- **Consumer fitness data:** Povver was catalogued on the strength of its published tool surface and read-write split, but the class is thin for operator relevance; future consumer fitness and training entries start at LOW unless they carry business data.
- **Multi-network publishing saturation extended:** Blog2Social catalogued at LOW relevance, but ContentStudio, Rebbel, SMAT, uplika and PostBazooka already cover the class. No further publishing entries this week without a differentiating surface.
- **Regional consumer services on `/all`:** Well Prepped Life and ECRP extend the geo-niche and consumer-care precedent (Bay Area Mobile Dog Wash, Lifeguard Training NY) already logged on September 30 morning.

## Verification

All four guides passed the inline validator (title 30-60, description 100-155, eight required frontmatter fields, added date, dash scan, FAQ heading check, See Also path existence) and the repo frontmatter validator. The local pre-commit gate reports `warn` on the AEO FAQ rule for all four, which is accepted house style for guide files (question-style headings are not used in this class).
