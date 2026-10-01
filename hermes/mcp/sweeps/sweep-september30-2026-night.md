---
title: "MCP Server Discovery - September 30, 2026 (Night)"
description: "Night sweep of the mcp.so feed and mcpservers.org: three new servers catalogued with integration guides."
category: mcp-directory
tags: [mcp, discovery, sweep, directories]
---

# MCP Server Discovery - September 30, 2026 (Night)

**Date:** September 30, 2026 (night slot)
**Sources:** mcp.so /feed (30 server blocks, direct fetch with a browser user agent) and mcpservers.org /all via the r.jina.ai reader proxy, with four detail pages fetched (mcp.so detail pages plus the /all listing page).
**Result:** 3 new business-relevant servers catalogued with guides. Catalog 762 to 765 servers, guides +648 to +651.

## Discovery

Feed-order recency against the evening anchor (PixelDojo at the top, TrackIQ below it). Four entries in the current feed and /all listing had no prior disposition in the sweep index or the `servers/external/index.md` ledger:

- **Common Paper Contracts** - catalogued (see below).
- **Genchi** - catalogued (see below).
- **Manifold MCP** - catalogued (see below).
- **TATUAT.RO** - evaluated from the feed. Public Streamable HTTP server for a Romanian tattoo and piercing supply store, six tools over catalogue search, shipping estimation and cart links, no authentication. Genuinely well documented, but it is a single-store consumer retail catalogue rather than a business-operator data or operations surface. Consumer retail class, outside the catalog. Skipped.

Everything else in the feed and on the /all page matched a prior disposition or an already-catalogued guide, checked against the sweep index and the `servers/external/index.md` ledger. Of note, Adviserry, SignalPipe, Vouched and Family Office Registry were catalogued in the September 30 midday sweep; Anomaly AI and Tokmeter were disposed in that same sweep's also-identified prose. All four were re-confirmed as already covered rather than treated as new.

## New servers catalogued

- **Common Paper Contracts MCP** (Agreement workflow for agents) - remote Streamable HTTP at `api.commonpaper.com/mcp`, OAuth with no API key. Find agreements by type, status, created date or recipient; check viewed and signed status with full history; create and send NDAs, Cloud Service Agreements, DPAs, BAAs, Professional Services Agreements, Letters of Intent, Pilot Agreements, Software Licenses and Design Partner Agreements from standard or custom templates; edit drafts, resend, reassign or void, generate a shareable signing link and download PDFs, with template management on top. The safety split is the point: read tools run without interrupting the conversation while anything that creates, sends or voids an agreement asks first. Relevance THREE because the surface produces legally binding documents and the approval gate is the correct default. The directory listing exposed no fetchable tool list at catalog time, so the guide describes capabilities rather than inventing tool identifiers.

- **Genchi MCP** (Project deadline risk from team confidence votes) - remote Streamable HTTP at `genchi.com/api/mcp`, OAuth sign-in against a Genchi account, free for teams up to 10 with a two-week trial above. Six tools: list initiatives (portfolio or a single project tree), get confidence (score and trend with chart), get blockers, get weekly summary, create initiative and Slack connection status. Votes are anonymous one-click confidence responses to an automated Slack prompt, combined per project into a score tracked over time. Privacy by design: no tool returns a name alongside a vote, individual values are shuffled on every response, each user sees only their own projects, and any user or admin can revoke a connection. Relevance THREE for engineering leaders because the delivered insight is portfolio risk rather than another status board.

- **Manifold MCP** (Hosted marketing data for agents) - remote Streamable HTTP at `mcp.manifoldmcp.com/mcp`, OAuth or an API key, pay per call with 500 free credits per new workspace. One connection covers keyword research, SERPs, backlinks and site audits, AI answer visibility across ChatGPT, Perplexity and Google AI Overviews, social data from Reddit, YouTube, TikTok, Instagram, LinkedIn, X and Facebook, ad libraries and B2B lead enrichment. Verified and featured on mcp.so. Relevance THREE because it collapses five key-management surfaces into one endpoint and adds AI-answer visibility alongside classic SEO. The guide notes the listing's own contradiction (the FAQ states no auth is required while the vendor overview describes OAuth or an API key) rather than picking one and stating it as fact.

## Core listing verification

- **mcpservers.org:** LISTED. Direct curl returns the Cloudflare 403 wall; the reader proxy returns the CorpusIQ MCP page, so the listing is live.
- **glama.ai/mcp:** LISTED. The `@corpusiq/corpusiq-docs` slug redirects to the canonical listing.
- **PulseMCP:** LISTED. Reader proxy title reads Official CorpusIQ MCP Server.
- **smithery.ai:** registry entry present. No submission path exists (login-walled) and the listing is unstable, so no action taken.
- **mcp.so:** NOT LISTED. The search SSR payload carries no server cards; the account-level instant moderation state from August 12 still stands, so no resubmission was attempted.

## Also identified (not catalogued)

TATUAT.RO (public Romanian tattoo-supply catalogue, consumer retail class, six tools, no auth), plus the feed and /all repeats already disposed by the September 30 evening, midday and morning sweeps, the September 29 sweeps and earlier ledgers: PixelDojo, TrackIQ, LinkBunny, Agent Cody, SignalPipe, Vouched, Adviserry, Family Office Registry, Anomaly AI, Tokmeter, prodready, uplika, How To Make Money On Snapchat, MemeSwap MCP, MeroFoundry, Rebbel, Dumpster Controls, Unipile, fAlpha, TokElements, GAIP Agents, HeyLead, elmah.io MCP, trip1, Webshare, systemHUB, AccountHub, AgentGrown, ohmyho.st, EQIQs, Selfstorming, Uxia, Texas RRC Wellbore Intelligence, TinyFish, pdf.net, SMAT, HaberChat, Agent Credit Bureau, ECRP, Well Prepped Life, Beemm Vision, MX Verdict, AnswerLine, Dive Kit, Robozukan, SubmitraX, Tempi, Garmin, health-os, MateMCP, Swebsy, NoMac, Monocrawl, betterimage, Hookova, PDFHaul, LiteLambda, Suggix, Arroway, Friday, ImmoDocs, Gilbert, Clipy, VideoGen, pcb.express, TrueProxies, SelectaRank, Revit Model, Symbioza, CovaSyn, AgentHop, Auth Your Agent, GeoSource, Agentboxd, AQL PropertyCheck and Firme360.

## Skip classes held

- **Consumer storefront catalogues:** TATUAT.RO is a single-store retail catalogue with no operator data surface. The catalog tracks business-operator data and operations tools, so retail storefronts stay out unless they serve a B2B workflow.
- **Contract surfaces with no published tool list:** Common Paper is catalogued on capabilities rather than tool identifiers; the guide says so explicitly instead of guessing names. A future cycle can add exact tool names if the vendor publishes its reference.

## Verification

The three new guides passed the inline checks (title length, description length, required frontmatter fields, added date, dash scan, See Also path existence) and the repository frontmatter validator over the whole docs tree (4,740 files, all valid). The SEO validator reports 0 errors and 2 warnings, both the accepted index-coverage advisory for this file class. The class-level AEO advisory from the local pre-commit gate is accepted house style for this file class, as it is for the rest of the external catalog.
