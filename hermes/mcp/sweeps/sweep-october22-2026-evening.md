---
title: "MCP Server Discovery - October 22, 2026 (Evening Sweep)"
description: "Cataloguing Adrails, ad spend read beside Stripe and Shopify revenue behind human approval, plus seventeen submissions dispositioned."
last_updated: 2026-10-24
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october22-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 22, 2026 (Evening Sweep)

A ten-hour delta after the midday supplement. The two browsing surfaces were running on ingestion rather than invention: mcpservers.org `/all` pages 1 to 3 returned 90 unique slugs against the 86 at midday, and the mcp.so `/feed` page 1 carried 27 server cards of which six were posted after the midday capture closed.

The productive lane was the submission window. `#5957` through `#5973` were filed in the window, seventeen issues, and every one was read. One entry cleared the bar.

One discipline note carried from the previous pass: every `/all` slug the ledger named only in a bulk paragraph was read to its detail page this cycle. Sixteen slugs were in that state and all sixteen served real listings rather than 404 shells, so each now carries a disposition in its own right.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [Adrails MCP](/hermes/mcp/servers/external/adrails-mcp/) | Marketing | Ad management for Meta Ads and Google Ads where the ad numbers sit beside the store's own revenue. `https://adrails.ai/api/mcp`, Streamable HTTP with OAuth 2.1, by TBSS Labs, LLC (adrails.ai). Probed live: unauthenticated `POST initialize` returned HTTP 401 with `www-authenticate: Bearer resource_metadata="https://adrails.ai/.well-known/oauth-protected-resource"` and the body `{"error":"invalid_token","message":"Connect to Adrails to continue."}`. That document returned 200: resource `https://adrails.ai/api/mcp`, authorization server `https://adrails.ai/api/auth`, bearer in header, six scopes (`adrails:read`, `adrails:actions:prepare`, `adrails:integrations:manage`, `adrails:workflows:manage`, `adrails:knowledge:write`, `adrails:campaigns:write`). The vendor server card at `/.well-known/mcp/server-card.json` returned protocol 2025-11-25, `serverInfo` Adrails 1.0.0 and the tools capability. 69 published tools: 49 agent tools plus 20 for accounts, integrations, campaign drafts, automations, Knowledge and job status, each documenting its inputs, its per-operation permission, the role it needs and its error contract; `tools/list` returns only what the connection's permissions and the caller's role allow. Three access shapes per tool: read, change (acts at once, needs an idempotency key) and proposal for approval. A proposal returns `status: awaiting_approval`, an `actionId`, a field-by-field preview, an `expiresAt` and an approval link at `adrails.ai/oauth/actions/<actionId>`; any current owner or admin can approve it signed in as themselves, Adrails re-reads the platform and applies the exact change once or blocks it if the entity moved, and the proposal expires 24 hours after it was prepared (30 minutes in-app). Budget changes are capped at 30% each, an increase needs measured spend and results, bulk selection covers at most 40 entities, and everything created starts paused. Idempotency is enforced rather than advisory, errors come back as tool results with `isError` so the model can correct the call, a result over 256,000 bytes is refused whole with no partial figures, and limits run 60 calls a minute per token, 10 changes a minute, 180 a minute per person and 600 per workspace. Business sources read beside ad spend: Shopify, Stripe, Klaviyo, Triple Whale, PostHog, RevenueCat and Google Drive. Two tools carry the entry. `store_revenue` returns gross, refunded and net sales kept apart in each store's own currency and never converted. `business_review` accepts an explanation only when every number quotes its source word for word, from the person's own statement or from a tool result in the connection's history, which is a provenance rule enforced inside the tool rather than a disclaimer beside it. `budget_recommend` compares the latest two complete seven-day windows in the account's time zone and suggests no amount. Pricing from the vendor's own page: Preview free with 10 credits once, Starter $49 a month with 200 credits, Growth $149 with 700, Scale $399 with 2,000, unlimited ad accounts and team members on every paid plan, every connector included, no percentage of ad spend, and MCP tool calls cost zero credits. **Gap named rather than claimed:** no tool call was made. Every tool needs an OAuth connection to a workspace with a connected ad account, so the entry rests on the live 401, the protected-resource metadata, the server card and the vendor's 69-tool reference, and the absent execution is stated in the entry. |

## Also Identified (not catalogued)

From the submission window `#5957` through `#5973`:

- **contix** (`#5957`, two endpoints: `https://api.contix.es/api/v1/mcp` for invoicing behind OAuth 2.1 with dynamic client registration or an API key, and `https://api.contix.es/api/v1/mcp/herramientas` free and keyless): the free endpoint returned 200 with `serverInfo` `contix-herramientas` 1.0.0 and instructions saying it covers Spanish VAT and IRPF arithmetic, DNI/NIE/CIF and IBAN check characters, VIES lookup, Modelo 303 box sums and Veri*factu deadlines; the invoicing endpoint returned `{"detail":"Missing Bearer token"}`. Held as class-covered: the catalogued BeeL MCP already carries Spanish VeriFactu e-invoicing against AEAT at about 120 tools, and NormAPI carries German XRechnung and ZUGFeRD validation, so this is a third regional e-invoice surface rather than a new operator capability.
- **Kurlo** (`#5958`, npm stdio, MIT): the operator's own API collection handed to a coding agent, with secret values shown to the model as `[secret]`. Held as developer tooling.
- **CallSimple** (`#5959`, `https://callsimple.app/mcp`, OAuth 2.1 with dynamic client registration): held in the agent telephony class already covered by the catalogued PlaceCall and the CallForMe hold.
- **A4A** (`#5960`, local stdio, Ed25519 and X25519 keys, no cloud signup): an encrypted agent-to-agent messaging network. Held as agent infrastructure.
- **Tisty** (`#5961`, stdio only, AGPL, no account and no network): a desktop notes, documents and tasks app whose MCP server writes plain Markdown on the operator's own disk. Held as a local desktop productivity app with no hosted data surface to read.
- **Hronaut** (`#5962`, local adapter in a paid desktop app, source-available licence at $4 a month): a per-project visible browser for coding agents. Held as browser and dev infrastructure.
- **Forever In Our Hearts** (`#5963`, keyless streamable HTTP at `mcp.foreverinourhearts.co/mcp`): held as a consumer memorial utility.
- **Edge** (`#5964`, keyless at `https://getedge.cc/mcp` plus an npm stdio package): searches and loads pinned public skills for an agent. Held as agent and developer infrastructure.
- **AnotherSEOGuru** (`#5966`, `https://app.anotherseoguru.com/mcp`, OAuth 2.1 with PKCE and dynamic client registration, 401 on an anonymous initialize): Google Search Console data with a prioritised fix list, site audits, ranks, backlinks, schema and AI visibility plus write-side SEO tasks. Held against the SEO class already saturated by the catalogued DrUrls, HarborRank and MisarSEO, and because the read half is a pass-through of data the operator already owns.
- **Assay** (`#5967`, `https://app.goassay.io/mcp`, OAuth, 401): a marketplace where another agent does the task and is paid only when the work passes your tests or you accept it, with the budget held when a task is posted. Held in the agent labour marketplace class.
- **Muninn** (`#5968`, local stdio, Apache-2.0) and **Mimir** (`#5969`, local stdio, Apache-2.0): code search across Git worktrees and reasoning memory for coding agents. Held as developer tooling; the memory class is already dense.
- **url-to-markdown** (`#5970`, local stdio, TypeScript SDK): held in the web-extraction commodity class.
- **Arch, Church Website Audit and Typewright** (`#5971`, three MIT stdio servers): a paid theological review at $2 or less each plus two website audits. Held as niche vertical and audit-class services.
- **Tanatasa** (`#5972`, remote with guest carts and a checkout link where the buyer pays on the vendor's own site): held in the single-store storefront class.
- **CARDZ** (`#5973`, free read-only, no login): graded trading-card prices, population and daily history. Held as consumer collectibles data.

From the six mcp.so `/feed` cards posted after the midday capture:

- **Altss Public Profiles MCP** (`createdAt 2026-10-23T01:58Z`, hosted HTTP, anonymous read-only): published company-profile summaries with canonical citations. Held against the company-data density already set by the catalogued StackScope and the SalesBook hold.
- **Pactlyst** (`createdAt 2026-10-23T01:34Z`, remote at `api.pactlyst.ai`): the root answered HTTP 404 `{"error":"requested path is invalid"}` and the vendor site presents the product as a concept preview whose own labels read `Planned system`, `not a live API response` and `TRY IT - SIMULATED`. Held: there is no live API to catalog.
- **Canopy API - Amazon Data for Agents** (`createdAt 2026-10-23T01:27Z`): held in the e-commerce product-data class already carried by the catalogued Datrace, Pangolinfo and AMZ Vault entries beside the Logimu Shopping and Ecommerce Data API holds.
- **Eased** (`createdAt 2026-10-22T21:49Z`): a motion component library for shadcn. Skipped as a front-end library with no data surface.
- **MangroveAI** (`createdAt 2026-10-22T21:03Z`, 119 tools for market data, backtesting and paper trading): held in the trading class.
- **screenshotrun-mcp** (`createdAt 2026-10-22T20:10Z`): held as a developer screenshot utility.

From the sixteen `/all` slugs the ledger had only named in bulk, each read to its detail page this cycle and each confirmed a live listing rather than a 404 shell:

- **ACTN** carried its October 21 disposition as an agent labour marketplace; **BEON PASS** carried its October 21 disposition as an access wallet; **Pear** carried its October 20 disposition as an email, calendar and contacts connector; **Wine Labs** carried its October 22 midday disposition as a single-vertical wine data surface; **TwinMind** carried its October 22 midday disposition as a meeting-notes reader; **Visualping** is a page-change monitor whose watch surface is consumer monitoring rather than operator business data.
- **MedicineData (医药数据社)** (`medicine.shanchuangkj.com/mcp`, `X-API-Key`, 21 metered read-only tools over nine capability domains, a 32KB response cap and 20 rows a page, billed per returned row): a Chinese pharmaceutical research database covering drugs, targets, indications, clinical trials, BD deals, financing, patents and sales. Held as regional vertical research data: the catalogued healthcare entries read provider and organisation records, and this reads pipeline data a business operator does not act on.
- **OpenYuri Tools Network** (`https://sitenet-api.openyuri.workers.dev/mcp`, keyless, five read-only tools, CC0 ledger): extractive answers with citation URLs, citation cards and a US seller-compliance change ledger over 62 sites. Held as a cited-answer read surface whose compliance half is already carried by the catalogued Tiana seller-compliance entry.
- **PlanLimits** (`https://planlimits.app/mcp`, keyless, eight read-only tools: plan inventory, recent plan changes, a plan recommendation, task routing across plans, affordability checks and vendor service status): held as developer cost routing for AI subscriptions rather than an operator business surface.
- **Quickbase by Smart Strategy**, **Shipday**, **Treasure Valley Fun Directory**, **Eglise Shop**, **Indiax BookKaro Live Demo**, **Bay Motors Auto Repair** and **Agent Haven**: held in the single-vendor platform connector, delivery operations, local directory, consumer bookstore, live-demo shell, regional service site and agent-social classes respectively, none of which is a new operator data surface.

## What Moved on the Discovery Surfaces?

- The mcpservers.org `/all` capture carried 90 unique slugs on pages 1 to 3 against the midday pass's 86 at a ten-hour gap. The net four is pagination spillover across the featured slots rather than a burst of new listings: every slug resolved to a recorded disposition, a class hold or one of the sixteen bulk-named cards now given its own disposition.
- The mcp.so `/feed` page 1 carried 27 server cards with the newest `createdAt` at `2026-10-23T01:58Z` and the oldest at `2026-10-21T12:59Z`. Six cards were posted after the midday capture closed at 18:05Z, which is the feed's real rate over that window, and all six are dispositioned above.
- The submission window continues to be the highest-yield lane at any gap. Seventeen issues in about nine hours, self-submitted by their maintainers, with a noticeable share of local stdio developer utilities, which is the class the catalog holds by default.

## Method

Sources: mcpservers.org `/all` pages 1 to 3 newest-first through the r.jina.ai reader proxy (90 unique slugs, cross-referenced slug by slug against the index headings, every guide directory, every sweep record and both prior captures), the mcp.so `/feed` page 1 read from the TanStack payload with a browser user agent (27 server cards with `createdAt`), the chatmcp/mcpso issue window `#5957` through `#5973` read over the REST API with full bodies, sixteen `/all` detail pages through the reader proxy, and live JSON-RPC probes against four candidate endpoints. Adrails was settled by an unauthenticated JSON-RPC probe, the RFC 9728 protected-resource document, the vendor server card and the published 69-tool reference; contix by a keyless initialize on its free endpoint and a missing-bearer response on its full endpoint; Pactlyst by a 404 at the root and its own `Planned system` labels.

Catalog 976 to 977 servers (+856 to +857 guides).
