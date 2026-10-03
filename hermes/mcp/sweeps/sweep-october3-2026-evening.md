---
title: "MCP Server Discovery - October 3, 2026 (Evening Sweep)"
description: "Evening sweep cataloguing eight new business-relevant MCP servers spanning social publishing, phone-call automation, growth audits, leads and workspace access."
last_updated: 2026-10-03
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october3-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "discovery"]
---

# MCP Server Discovery - October 3, 2026 (Evening Sweep)

Evening sweep over the mcp.so `/servers` listing (60 slugs) and mcpservers.org `/all` pages 1-3, both via the r.jina.ai reader proxy because direct fetches return the Cloudflare/JS shell without server data. Detail pages were fetched for every candidate; endpoints were probed for liveness. Eight new business-relevant servers were catalogued, each with an integration guide.

## New This Sweep

### VoiceMoat MCP - Voice-Matched Social Publishing

Hosted Streamable HTTP at `app.voicemoat.com/api/mcp` with OAuth and no API keys. VoiceMoat builds a per-platform voice profile from your own published posts and keeps it separate for X and LinkedIn. Fifteen tools split into a free-reading half (`get_me`, `list_profiles`, `get_voice_profile`, `get_analytics`, `list_posts`, `list_creators`, `search_inspiration`) and a credit-spending half (`score_voice_match` at 0 to 100, `get_post_ideas`, `improve_post`, `suggest_hooks`), plus `publish_post` and `schedule_post`. Publishing always asks twice: the first call returns the exact text, the destination account and a one-time code and posts nothing, and only a second call with that code publishes. The endpoint returns 401 unauthenticated, confirming it is live and auth-gated.

### PlaceCall MCP - Agent Phone Calls to Real Businesses

Hosted Streamable HTTP at `api.voygr.tech/mcp` with OAuth or an `X-API-Key` / Bearer header, built by an ex-Google Maps and Search team. Give it a US number or describe a place, plus a task in plain English, and it dials, navigates IVRs and hold, talks to the business and returns one of 17 verified outcomes with the transcript and recording, including explicit failure reasons (dropped calls, busy lines, voicemail, wrong numbers). Batches are supported, so a list of businesses can be contacted at once. First 250 calls are free. The endpoint returns 401 unauthenticated, confirming it is live and auth-gated. Note for Hermes: use the MCP route, not the skill route, because a skill sending an API key by curl to a non-loopback host trips Hermes's own scanner by design.

### LogNorm MCP - Growth Audit and Agent Backlog

Hosted Streamable HTTP at `lognorm.com/api/mcp` with OAuth 2.1 (dynamic client registration and PKCE) and a free plan where agents run on your own Claude or Codex plan. LogNorm audits a site for broken pages, metadata, indexing, AI-crawler access, llms.txt and structured data, ranks the gaps into a shared backlog of moves, and lets an agent claim a move, fix the cause in the repo, open a PR and call `validate_fix` so LogNorm re-checks the affected pages on the live site. It also tracks how ChatGPT, Gemini and Google AI Overviews answer buyer prompts and turns the gaps into moves, which is AI-visibility work rather than only search ranking.

### Solnk MCP - Publish to Nine Social Platforms

Hosted Streamable HTTP at `mcp.solnk.com/mcp`, or a self-hosted MIT Cloudflare Worker, authenticated with a Solnk API key as a Bearer token. One tool surface publishes and schedules to X, Instagram, TikTok, YouTube, Facebook, LinkedIn, Pinterest, Threads and Bluesky, with `solnk_publish` supporting `immediate`, `scheduled` or `draft` and a confirm, cancel and aggregate-status model behind it. Discovery (`initialize` and `tools/list`) is open without a key, and the worker is stateless with no credentials stored at request time.

### RestoSignals MCP - Scored Restaurant Opening Leads

Hosted remote MCP returning deduped restaurant locations, each with an `opening_score` and the signals behind it, filterable by state, city, signal or score in one request shape (`/v1/openings?state=NY&min_opening_score=40`). The listed buyer categories are POS systems, beverage distributors, commercial insurance, kitchen equipment, payment processors, design and build, and linens and uniforms, all of whose next customer is a venue that has not opened yet. Signup with email returns an API key and 100 free trial credits on screen, with no card.

### Thrume MCP - Authorized Recording Evidence

Hosted Streamable HTTP at `dash.thrume.app/mcp` with OAuth and PKCE under a single `recordings:read` scope. A compatible assistant retrieves authorized recording evidence from an account, with the client and connection chosen and approved from inside the Thrume web app. The surface is read-only by design: no tool can add, edit or delete recordings, which makes it an easier connection to approve for teams handling sensitive recordings.

### Staffic MCP - Team Time Tracking and Monitoring

Hosted connector combining time tracking, screenshot monitoring and project management in one platform, so a manager can see how a team spends its hours rather than relying on manual timesheets. Free forever for teams up to three seats, no credit card required, and the demo needs no signup.

### Twelfth MCP - Read-Only Workspace Access

Read-only remote MCP endpoint at `api.twelfth.ai/mcp` accepting an OAuth user token or a workspace bearer key. Twelfth ships first-party setup for Claude, ChatGPT, Gemini, Grok, Glean and Cursor, and this generic endpoint is the client-agnostic escape hatch for everything else. Setup lives under Settings, AI and agents, Generic MCP inside the workspace.

## Listings Verified

| Directory | Status | Evidence |
| --- | --- | --- |
| mcpservers.org | LISTED | Reader-proxy fetch of `/servers/corpusiq-io` returns HTTP 200 with title "CorpusIQ MCP Server \| Awesome MCP Servers" |
| glama.ai/mcp | LISTED | HTTP 200 on the `@corpusiq/corpusiq-docs` slug |
| smithery.ai | REGISTRY ENTRY PRESENT | `benoit-p/Cprusiq` in the registry API response; flip-flop class, no submission path available |
| mcp.so | NOT LISTED | Search returns unrelated servers with no CorpusIQ entry; quarantine holds |
| PulseMCP | LISTED | Reader-proxy fetch of `/servers/corpusiq` returns the CorpusIQ listing |

## Identified But Not Catalogued

**mcpservers.org `/all`:** Magnemo (governed agent memory with entry receipts; agent-memory class already covered by Jotter and clexo), Ownhand (voice-matched writing for Slack, cold email and PR descriptions; content-writing class), PeerPush (product discovery and launch prep), Agent Verifier at packet.guru (keyless agent HTTP API discovery; dev-infra class), QRSalt (QR code generator; commodity utility), OneFindMe (AliExpress shopping search; consumer retail), Kinoify (media generation utility), JANCTION Render (cloud Blender GPU render farm), Insta-Pola (shared event photo galleries; consumer event), Gaia Baby Tracker (read-only baby log), Athmex (endurance training coach), Weight Forecast (weight goal-date tracking), BOIM (Korean vendor directory), Fungsi.id (Indonesian jobs), Calorie API (nutrition lookup), Sketchlib, PeakAI, Grok Bot Wiki and Clair (French-language legal document drafting; regional-language class).

**mcp.so `/servers`:** Local YDB (Docker local-ydb operations; dev-database utility class), with 3GPP, Artibot, Capital.com, Novu, SendRaven, TinyFish, Yocoolab and the rest each catalogued or disposed in the September 28 through October 3 ledgers.

## Notes

- The mcp.so `/servers` listing yielded 60 slugs, almost all prior dispositions; the fresh business-relevant candidates came from the mcpservers.org `/all` rollover across pages 1-3.
- Endpoint liveness was probed with a keyless `tools/list` POST: VoiceMoat, PlaceCall and LogNorm returned 401 (live and auth-gated), confirming they are real hosted endpoints rather than directory shells.
- The two clearest new capabilities this cycle extend agents beyond text APIs: PlaceCall reaches the physical world by phone, and LogNorm closes a growth loop by validating fixes on the live site.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the curated catalog
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - all sweep reports
