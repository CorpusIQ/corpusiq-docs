---
title: "MCP Server Discovery - October 22, 2026 (Midday Supplement)"
description: "A one-hour supplement cataloguing Muvia BI, a governed 231-tool data platform, and holding BootForm as form infrastructure."
last_updated: 2026-10-22
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october22-2026-midday-supplement/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 22, 2026 (Midday Supplement)

A supplement about one hour after the midday delta. At that gap the two browsing surfaces had nothing left to give: mcpservers.org `/all` pages 1 to 3 returned 86 unique slugs and every one matched a disposition already in the ledger, and the mcp.so `/feed` page 1 carried 27 server cards, all previously named. The work came from the third lane, the chatmcp/mcpso submission window, where two issues had been filed after the midday capture closed at #5954.

Both of the new submissions were probed live. Neither could be driven with a tool call, because both require an account the sweep does not create, and that gap is stated in the entry rather than hidden by a handshake.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [Muvia BI MCP](/hermes/mcp/servers/external/muvia-bi-mcp/) | Business Intelligence & Analytics | Governed data platform for agents. `https://api.muviabi.com/mcp/v1`, JSON-RPC 2.0 over POST with an SSE answer, protocol 2025-06-18, by Superduck S.r.l. Probed live: unauthenticated `POST initialize` returned HTTP 401 with `www-authenticate: Bearer resource_metadata="https://api.muviabi.com/.well-known/oauth-protected-resource/mcp/v1/"`; that document returned 200 (resource `https://api.muviabi.com/mcp/v1/`, authorization server on the same host, bearer in header) and the authorization server metadata returned authorization, token, registration and revocation endpoints, `authorization_code` plus `refresh_token` grants, `code_challenge_methods_supported: ["S256"]` and `client_id_metadata_document_supported: true`. 231 tools from the vendor reference: 113 read and 118 write, split 96 proposal, 12 confirmed in Muvia and 10 not available to API keys. Modules: Flows 36, Lab 26, Assets 24, Alarms 20, Notebooks 19, Dashboards 18, Sources 18, Analysis 17, Nodes 15, Core 12, Project 8, Annotations 7, Predictors 7, Documents 4. The reads are the operator surface: `query_sql` and `describe_sql` over the data lake, `read_lineage`, `run_query_checks` and `set_query_checks`, `list_quarantine`, `list_dataset_readers`, `list_datasets`, `read_dataset`, `list_alarms` with `investigate_alarm` and `shelve_alarm`, `list_dashboards` with `create_dashboard` and `add_widget`, `list_predictors` with `promote_predictor_version` and `reject_predictor_version`, and `get_action` for the outcome of a write. What earns the entry is that the governance travels with the protocol: a write files a proposal a person approves in Muvia or the company policy applies, a key writes only when an administrator has allowed writes through assistants, and a key can be granted only scopes the granting administrator holds, never `superadmin`, capped by the company's enabled modules. Rate limits 120 a minute per key and 100,000 a day per company in fixed windows with `X-RateLimit` headers on every response. Gaps named: an account is required with the AI connectors module, the only public entry is a 14-day trial, both pricing paths returned 404 so no price list exists to quote, and the protected-resource metadata advertises an empty scope list while tools declare scopes individually. **No tool call was possible**, which is the difference between this entry and the three catalogued at midday. |

## Also Identified (not catalogued)

- **BootForm** (`https://mcp.bootform.com/mcp`, OAuth 2.1, `POST initialize` returned HTTP 401 carrying the server's own message, `Sign in to BootForm to use this MCP server. Your MCP client opens the browser for you.`, 20 tools from the submission: `bootform_create_form`, `bootform_get_snippet`, `bootform_configure_form`, `bootform_get_submissions`, `bootform_mark_submission`, `bootform_moderate_submission`, `bootform_check_spam`, `bootform_add_email`, `bootform_add_verified_email`, `bootform_add_discord`, `bootform_add_slack`, `bootform_add_webhook`, plus workspaces and account reads): held as website and form infrastructure. The data behind it is submissions the customer's own page collected, and the value is routing them to email, Slack, Discord or a webhook with spam checks and moderation, which is builder plumbing rather than an operator data surface. Pricing from the vendor's page: Free at 250 submissions a month with MCP access included on every plan, Starter $10 monthly, Pro $29, Business $99, and the REST API and two-factor sign-in on all tiers.
- **A1 Towing NYC** (`a1towingnyc-com` on mcpservers.org `/all`) carried its midday disposition as a single-city service site, checked here only because the bulk class of the previous pass named it in a paragraph rather than in a list.
- **Pear** carried its October 20 disposition as an email, calendar and contacts connector, unchanged.

## Source Behaviour

- The mcpservers.org `/all` capture stamped `Thu, 22 Oct 2026 17:01:19 GMT` returned 86 unique slugs against the midday pass's 89. The three-card difference is pagination spillover at the featured slots, not churn: every slug resolved to a prior disposition.
- The mcp.so `/feed` page 1 was read 55 minutes after the midday capture and carried 27 server cards against 30. Every card already held a disposition, including the four that the midday pass named for the first time (Clevera, Tinymusic, Dead Brands Bot Arena and the ChatGPT top-up reseller).
- The submission window is the only lane that moves at a one-hour gap. `#5955` and `#5956` were filed at 17:29Z and 17:40Z, both after the midday window closed, and both self-submitted by their maintainers.

## Method

Sources: mcpservers.org `/all` pages 1 to 3 newest-first through the r.jina.ai reader proxy (86 unique slugs cross-referenced against the index headings, every guide directory and every sweep record); mcp.so `/feed` page 1 read from the TanStack payload with browser user agent (27 server cards); the chatmcp/mcpso issue list and both new issue bodies over the REST API. Muvia was settled by an unauthenticated JSON-RPC probe plus the RFC 9728 protected-resource and authorization-server documents, and its tool inventory by the vendor's published `mcp-tools` reference. BootForm was settled by an unauthenticated probe carrying the server's own error and by its pricing page.

Catalog 975 to 976 servers (+855 to +856 guides).
