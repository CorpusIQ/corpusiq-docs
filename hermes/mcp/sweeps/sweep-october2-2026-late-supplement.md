---
title: "MCP Server Discovery - October 2, 2026 (Late Supplement)"
description: "Late supplement MCP ecosystem sweep: 10 new business-relevant servers catalogued, from agent workspaces to live job data."
last_updated: 2026-10-02
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october2-2026-late-supplement"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 2, 2026 (Late Supplement Sweep)

Late supplement sweep over the mcp.so feed (12 server blocks) and mcpservers.org `/all` (30 slugs), both fetched through the r.jina.ai reader proxy. The mcp.so feed carried only prior dispositions this cycle, so the late afternoon `/all` rollover supplied all ten new business-relevant entries. Every candidate was fetched through its detail page and its endpoint probed before cataloguing.

## New Servers Catalogued

### Dock MCP - Agent Workspace for Docs and Tables

A shared workspace where humans and agents work as teammates, exposed to any agent through its official MCP server. Documents, tables and interactive HTML surfaces become something an assistant reads and writes alongside the team, with per-agent access control and an activity log.

- Endpoint: `https://trydock.ai/api/mcp` (remote Streamable HTTP, OAuth) plus a local stdio bridge over `npx -y @trydock/mcp`
- Surface: 71 capabilities on the hosted server across docs, tables, HTML surfaces, search, comments and agent messaging; the stdio bridge forwards eight workspace and row tools
- Security: API keys stored as SHA-256 hashes server-side, revocation returns 401 immediately

### Leadbay MCP - AI Lead Discovery for Agents

Connects an assistant to a Leadbay account so an agent pulls scored leads, qualifies them with AI research, drafts outreach and logs what was sent. Leads are scored against the operator's target profile, and roughly the top ten per daily batch are AI-qualified further.

- Endpoint: `https://mcp.leadbay.app/mcp` (remote Streamable HTTP, browser OAuth); `/fr/mcp` is a compatibility alias and ChatGPT uses `chatgpt/mcp`
- Surface: lead pull, `leadbay_bulk_qualify_leads`, `leadbay_enrich_titles`, `leadbay_report_outreach`
- Model: daily batch paced by recent engagement, firmographic `score` on every lead with `ai_agent_lead_score` on the top ten

### SendNow MCP - Trackable Document Sharing for Agents

Shares documents as secure trackable links and reports who opened them, which pages they read and when to follow up. Access controls travel with the link: email verification, NDA gates, download blocking, watermarks and expiry.

- Endpoint: `https://share.sendnow.live/mcp` (remote Streamable HTTP, OAuth)
- Surface: document sharing, data rooms, access controls and per-viewer analytics

### MagicMarkets MCP - Sports Markets for Agents

A single static Go binary, `magicmarkets-cli`, over the Magic Markets v2 API, streaming live sports prices, quoting selections, placing and managing orders and inspecting positions. Authenticated with one API key and no request signing.

- Delivery: local stdio via `magicmarkets mcp` or the streamable HTTP transport on localhost
- Surface: `markets`, `offers`, `betslip create`, `order place` and position inspection

### Google Tagmanager MCP - GTM Containers for Agents

Inspects and manages Google Tag Manager containers through the Google Tag Manager API v2 in plain language, working with the real container, workspace and version. Edits land in a draft workspace and publishing is a separate, deliberately destructive step.

- Delivery: npx (`mcp-google-tagmanager`), with a connect flow that catches the OAuth redirect on `127.0.0.1` with PKCE
- Surface: 25 tools - 10 read, 4 draft-creating, 5 altering, deleting, compiling or publishing
- Quota: request spacing at 4.2 seconds to respect GTM's 0.25-requests-per-second project limit

### ASOgenic MCP - App Store Optimization for Agents

Runs an App Store Optimization pass from an agent: research Apple keywords, write and validate metadata, manage screenshots and submit to review. The App Store Connect `.p8` key stays in the client environment while the server mints short-lived JWTs per request.

- Endpoint: `https://mcp.asogenic.com/mcp` (remote Streamable HTTP, per-account bearer key)
- Verification: `asogenic_auth_status` should return `asc_configured: true` and `asc_valid: true`

### MailSenpai MCP - Email Marketing for Agents

Manages a MailSenpai email marketing account from an assistant - lists, subscribers, templates and campaigns - on a server hosted in the European Union.

- Endpoint: `https://mcp.mailsenpai.com/mcp` (remote Streamable HTTP, OAuth)
- Differentiator: EU hosting for teams with data-residency requirements

### TwitterXAPI MCP - X Data for Agents

Gives agents public X posts, profiles, conversations, followers, search and trends through eight hosted MCP tools, without building against the X API directly.

- Endpoint: `https://twitterxapi.com/api/mcp` (remote Streamable HTTP, `tx_live_` bearer key)
- Surface: `search_x` for posts, accounts and trend pages, `get_x_user` for profiles, plus conversations, followers and trends

### VeritaHire MCP - Live US Jobs for Agents

Reads every US job directly from the employer's own careers site and retires it within about 36 hours of the role leaving the site. Keyless and read-only, with posted pay, requirement facts, distance and apply links.

- Endpoint: `https://veritahire.com/mcp` (remote Streamable HTTP, no key)
- Tools verified live through an unauthenticated `tools/list`: `search_live_jobs`, `get_job`, `save_search`, `report_problem`

### Versionly MCP - API Change Monitoring for Agents

Watches third-party APIs in connected GitHub repos, maps breaking changes to calling files and opens a reviewable fix pull request on a deterministic branch, keeping CODEOWNERS, CI and the merge button with the team.

- Delivery: hosted MCP over a GitHub App installation
- Flow: connect selected repos, scan against live vendor changelogs and OpenAPI specs, review the pull request

## Identified But Not Catalogued

The mcp.so feed this cycle (12 server blocks) was entirely prior dispositions: Sooveryn, SocialAPIs, Zyte MCP, AgentGrid.io, Builders in Fintech, FlatHunt, TATUAT.RO, Manifold MCP, Common Paper Contracts, PixelDojo, Aayat AI and Povver, each catalogued or disposed in the September 30 and October 1 sweeps.

Held or skipped on the mcpservers.org `/all` surface:

- **TidyTools** - five Apify pay-per-use web-data actors behind Apify's hosted MCP; Apify-actor class already covered by the Lintlab and Themineworks precedents.
- **Talpy Aya** - WhatsApp AI recruiter with Portuguese-first vendor docs and a REST-plus-MCP connector; thin non-English docs class.
- **Fazy Deals** - read-only consumer deals catalogue for US shoppers; consumer retail class.
- **Meniscus** - liquid-glass design system for coding agents; dev design-utility class.
- **clexo** - local SQLite index over past coding sessions; agent-memory class.
- **feedback-memory** - draft-correction memory with local Postgres and pgvector; agent-memory class.
- **Jotter** and **Very Simple Notes** - cross-assistant context handoff and Markdown notes; personal-productivity class.
- **pmndrs docs** - react-three-fiber and related library docs; dev-utility class.
- **AgentBoard** and **AgentTrust** - agent task coordination and endpoint trust checks; dev infra class.
- **IureOCR** and **IureTranscribe** - local Tesseract OCR and whisper.cpp transcription; local-utility class.
- **Prompt God** - prompt and skill lookup; dev-content utility class.
- **Account Niche Finder** - Chinese-language positioning skill; geo-niche class.
- **Clayre** - brand strategy and content calendar; covered by existing marketing libraries.
- **Skillfully** - paid author skills directory; skill-marketplace class.
- Remaining `/all` slugs (albemarlestudio, goodnightxu2002, ellaguno, sankrant, asogenic aliases and the username-fragment shells) resolved to prior dispositions or 404 shells.

## Channels Used

- mcp.so `/feed` via the r.jina.ai reader proxy (12 server blocks)
- mcpservers.org `/all` via the r.jina.ai reader proxy (30 slugs, late afternoon rollover)
- mcpservers.org detail pages via the reader proxy for every candidate
- Unauthenticated `tools/list` probe on the keyless VeritaHire endpoint
- Direct HTTP status probes on every catalogued endpoint

## Recommendations

1. VeritaHire is keyless and verified live, so it is the strongest quick-add for any operator with a recruiting or hiring-signal workflow.
2. Dock and Leadbay are the two highest-ceiling additions this cycle; both are OAuth and both compose cleanly with the HubSpot and Stripe connectors.
3. Google Tagmanager MCP should be paired with the existing GA4 connector in any measurement-integrity workflow, since the tag change and the resulting data are two halves of one check.
4. The mcp.so feed has now carried only prior dispositions across three consecutive sweeps; watch for the feed to roll and re-anchor before treating it as a live source again.
