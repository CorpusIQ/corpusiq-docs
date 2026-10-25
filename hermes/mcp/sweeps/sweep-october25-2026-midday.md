---
title: "MCP Server Discovery - October 25, 2026 (Midday Sweep)"
description: "Six servers added since the night read and three names no record had ever held: one gateway over seven business services clears the bar, two transactional utilities do not."
last_updated: 2026-10-25
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october25-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 25, 2026 (Midday Sweep)

Seven hours after the night pass and the directory had moved again, by six. mcpservers.org served 17,360 servers at the 17:00Z read against 17,354 at 04:01Z, which is small enough that the page one body barely changed, so this pass read pages one to three, cross-referenced ninety slugs against the catalog, every sweep report and the last-sweep ledger, and then read the submission window that opened after the night pass closed.

One entry clears the bar, and it clears it on a gap rather than a feature: the first single endpoint in this catalog that fronts a CRM with an action layer.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [Context4 MCP](/hermes/mcp/servers/external/context4-mcp/) | Business Operations / CRM | One remote endpoint over seven business services, with a permission per connected account. `https://context4.me/mcp` answers an unauthenticated `initialize` with HTTP 401 and its own error contract, `{"type":"urn:context4:error:authentication_required","status":401,"code":"authentication_required","request_id":"..."}`. Discovery is complete: `/.well-known/oauth-protected-resource/mcp` returns 200 with resource `https://context4.me/mcp`, authorization server `https://context4.me`, scope `mcp:tools` and bearer in header; `/.well-known/oauth-authorization-server` adds authorize, token, register and revoke, `authorization_code` plus `refresh_token`, and `token_endpoint_auth_methods_supported: ["none"]`, a public client with PKCE. Five stable meta-tools carry the whole surface (`CONTEXT4_SEARCH_TOOLS`, `CONTEXT4_GET_TOOL_SCHEMAS`, `CONTEXT4_MANAGE_CONNECTIONS`, `CONTEXT4_WAIT_FOR_CONNECTIONS`, `CONTEXT4_MULTI_EXECUTE_TOOL`), with strict input schemas that reject unknown fields and cap `arguments` at 65,536 serialized characters. The provider actions come from the vendor's published catalog, `https://context4.me/docs/connectors.json`, read in this sweep: seven connectors marked beta and 164 actions, amoCRM 21, Bitrix24 23, GitHub 24, Grafana 38, Linear 18, Pipedrive 15 and Sentry 25, OAuth 2 on five and an API key on Grafana and Sentry. A parallel HTTP API at `https://context4.me/v1` and a Composio-compatible base at `https://context4.me/compat/context4/v1` show the execution layer is proxied, which is how one endpoint carries seven services. Catalogued for the slot nothing else fills: no Pipedrive, Bitrix24 or amoCRM entry existed anywhere in the catalog, and no other entry exposes several business services behind per-account consent with a search-then-execute tool model. Limitations recorded rather than smoothed over: no tool call in this sweep because every action needs an OAuth session and a connected provider account, zero results for `context4` in the official MCP registry on October 25, all seven connectors beta by the vendor's own label, Russian-language documentation and console, homepage illustrations showing services absent from the published catalog including Wazzup and FinTablo, and no public price list on the pages read. |

## Candidates Read and Held

**Three names had never been recorded anywhere, and two of them were utilities.** The token crossref returned nine slugs with no hit in the catalog, the sweep reports or the ledger; six of the nine resolved to prior dispositions once their name forms were matched, as Proxy's ad library, b59.link, Design Check, Urban Game Theory, Peak Answer and Ink Studio, every one held earlier this month. The remaining three were read properly.

- **email59** (`icedsg/email59-mcp`), transactional email sending from agents with free address and list checks, from the same publisher as b59.link. Held as a sending utility rather than a system of record; the mailbox class is already carried, and a send-only surface gives an assistant nothing to read back.
- **MandarinClips MCP** (`indexflowing/mandarinclips-mcp`), 180,000 Chinese cinema dialogue clips with HSK grammar for language teachers. Held as single-market reference data per the standing regional rule. Real corpus, no business record.

**The submission window, #6044 to #6104, sixty issues, carried four re-surfacing names and one repeat.** Beancount.io (#6071) returned and stayed held on the existing ruling: hosted plain-text ledgers with BQL are accounting for a developer audience, and the carried ledgers are QuickBooks, Caribooks, Oracle and ATLASS. PenlyDoc (#6088) is e-signature, and the legal class already holds SignWell, SignSimple, PandaDoc and Binderwork. Simafri Suite (#6068) is own-domain email, calendar, contacts, files and helpdesk queues, held against the inbox class carried by Ficiel, Mailroom, Kaption, Bumblebox and Secure Email. TalkToAds (#6050) is Meta ads management against PaidSync, Markifact, Meta Ads Official, Adrails and the uplads hold.

**Agent and developer infrastructure, held.** nokk (a Rust headless browser passing Cloudflare without Chromium), Ask Key (a macOS credential manager that hands values to a process rather than a transcript), Kerno (backend runtime QA inside the coding loop), ComputeFirst (483 deterministic operations as a keyless endpoint), Lookout (Vercel Analytics over MCP) and Backdraw (image generation through a signed-in ChatGPT session, which its own submission says may conflict with OpenAI's terms). Each is infrastructure for building agents, not a business system an operator's assistant would connect twice.

**Content, media and vertical, held.** pitchboom and Renderster as video generation and clipping, FrameAnyPhoto as consumer print ordering, Postey against the social publishing class carried by UniPost, ViewsBase, Postkey, FeedSquad and Sendcove, GetMattered and LucyESL inside the job-search class, MarketMirror as simulated buyer testing, NetArz FX Rates as single-country currency data, Banktivity as personal finance, Quantplay as Indian broker access, DayPlay and RYC as consumer travel, and Beatrail-adjacent DealScore, IdeaKiller, BotCQ, paparats, runbook-ai, Buddy, Tattoo Brief, GhostPaw Questlog, txscribe and the VNCNT Labs pair.

**Two publisher bursts, held as groups.** The `mambalabsdev` quartet (#6046 to #6049) is the same fleet class-covered on October 24, and the `catalyst-labs` five (#6062 to #6066) plus the `textforagents` nine (#6074 to #6082) are single-author bursts of civic-data readers, agent utilities and concept servers, held once as families rather than eighteen times.

## Directory Behaviour

The directory counter moved twice inside one day, 17,243 to 17,354 overnight and 17,354 to 17,360 by midday, which is the first real movement since October 23 and the reason this pass read the listing rather than the feed. The feed barely moved: page one served thirty cards with the newest at `2026-10-25T13:50:07Z`, and only two were posted after the night capture, `next-generation-movers-free-moving-quotes-remote-mcp` as a licensed interstate mover quoting moving jobs and `agent-media` turning a screenshot into a ten-second vertical UGC video ad. Both held, the second inside the media-generation class that held Vadyu, Axiom Lab and Seedance3 this month.

## Listing Re-Verification

| Directory | State | Evidence |
|---|---|---|
| mcpservers.org | LISTED | `/servers/corpusiq-io` returns the CorpusIQ title page |
| mcp.so | ABSENT | 404 on `corpusiq`, `corpusiq-io`, `corpusiq-mcp` and `io.corpusiq` |
| Glama | LISTED, new URL shape | the `io.corpusiq%2Fmulti-source-mcp` server route now 301-redirects to a query URL that returns 200 with CorpusIQ present, so the old direct route reading is a shape change rather than a delisting |
| Smithery | LISTED | registry query returns the CorpusIQ server with `unlisted: false` |
| Official MCP registry | LISTED | `io.corpusiq/multi-source-mcp` 1.0.0 with a `streamable-http` remote |

No new directory was submitted this cycle. The discovery lane re-surfaced the same big names the ledger already screened and rejected, including microsoft/mcp as an official-catalog-only repo, the Claude community plugins repo as a read-only portal-gated mirror, and the large agent-skills catalogs as product repositories rather than server directories.

Catalog 987 to 988 servers (+1,135 to +1,136 guides). Sources: mcpservers.org `/all` pages 1, 2 and 3 via r.jina.ai (90 cards against 17,360 servers), mcp.so `/feed` page 1 with a browser user agent (30 cards, newest `2026-10-25T13:50:07Z`), the chatmcp/mcpso issue window #6044 to #6104 with full bodies over the authenticated GitHub API, the vendor's `llms.txt`, tool reference, OAuth reference and `connectors.json` for Context4, the official MCP registry search API, and live probes: JSON-RPC `initialize` and both OAuth discovery documents on Context4, plus the four-slug mcp.so check, the Smithery registry query and the mcpservers.org listing page.
