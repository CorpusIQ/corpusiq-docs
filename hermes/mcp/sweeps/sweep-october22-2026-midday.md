---
title: "MCP Server Discovery - October 22, 2026 (Midday Sweep)"
description: "Midday delta cataloguing three operational surfaces with real tool calls: support cases with approval gates, dated subprocessor records, CNC sourcing."
last_updated: 2026-10-24
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october22-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 22, 2026 (Midday Sweep)

A midday delta about seven hours after the night capture. The three surfaces rotated which one carried the work: mcpservers.org `/all` pages 1 to 3 returned 89 unique slugs against the night pass's 85, the mcp.so `/feed` page 1 was almost entirely the night sweep's own dispositions with four cards the ledger had never named, and the chatmcp/mcpso issue window #5924-#5954 supplied the two business-data records.

All three catalogued entries were driven with a real tool call rather than a handshake, and the first is a reversal: a server held twelve hours earlier on a partial tool count now carries 108 tools and the case surface that hold said was missing.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [Summer MCP](/hermes/mcp/servers/external/summer-mcp/) | Business Operations | Support operations with approval gates. `https://api.gosummer.ai/mcp`, keyless discovery and OAuth on every tool call. Probed live: `POST initialize` returned HTTP 200, serverInfo `summer` 0.2.2 on protocol 2025-03-26, and `tools/list` returned 108 tools. The protected-resource metadata at `https://api.gosummer.ai/.well-known/oauth-protected-resource` returned HTTP 200 with resource `https://api.gosummer.ai/v1`, authorization server `gosummer.ai` and nine scopes from `setup` to `automation.manage`. The surface is a full support operation: cases with search by customer, order, tracking or Stripe ID, short-lived attachment downloads, investigation requests, prepared actions, assignment and routing, quality assessments, company knowledge with revision history, customer guides with draft, preview, publish and custom-domain DNS checks, service metrics and commitments, Intercom migration, Messenger conversations and consented leads, privacy export and deletion requests, signed webhooks, service accounts, and credentials listed by name and version only. What earns the entry is the write discipline stated inside the tools: an investigation completing is not approval, prepared actions wait for a person inside Summer, publishing needs explicit rights on exact revisions. Reversal recorded: the October 21 evening sweep held this as vertical help-center publishing on 62 tools; the operator data surface it said was missing is the case and investigation family, now counted at 108 tools. Gaps named: sold to telehealth, no published price list, and nine OAuth scopes mean connection scoping is the operator's job. |
| [disclosedby MCP](/hermes/mcp/servers/external/disclosedby-mcp/) | Compliance | Dated GDPR subprocessor record. `https://disclosedby.com/api/mcp`, keyless. Probed live: `POST initialize` returned HTTP 200, serverInfo `disclosedby` version 2, and `tools/list` returned 7 tools: `list`, `as_of`, `changes`, `changes_across`, `named_by`, `resolve`, `in_chain`. Driven with a real call: `list` on `notion.so` returned the company page plus each reading held with capture timestamps, row counts and an evidence hash, 14 suppliers in the 2022 capture against 17 in the 2023 and 2024 captures, the later readings adding Anthropic and OpenAI. Record scale at capture: 352 companies read, 9,806 entries quoted, 563 subprocessors with a page, 4,901 changes on record, checked to 2026-10-22. `as_of` answers what a list said on a signing date; `in_chain` walks every path from the companies a buyer uses to one subprocessor. Pricing from the vendor page: every list and change free to read, cite and link with no account, MCP keyless at one company per call, the watch $99 a month up to 200 lists with a key for agents. First vendor supply-chain entry in the compliance class, which held licenses and leases per location and an auditable tool-call trail. Gaps named: coverage is whoever publishes a list, readings are dated by when the page was read rather than when the vendor changed it, and `resolve` is exact-match only so a chain built on an unresolved name is built on nothing. |
| [CNC Compass MCP](/hermes/mcp/servers/external/cnc-compass-mcp/) | Manufacturing & Industrial | Supplier sourcing from a brief. `https://cnccompass.com/mcp`, keyless with a per-IP quota for anonymous REST callers. Probed live: `POST initialize` returned HTTP 200, serverInfo `CNC Compass` 1.30.0, `tools/list` returned 3 tools: `search_suppliers`, `get_supplier`, `list_facets`. Driven with two real calls: `search_suppliers` on "aluminum CNC machining with anodizing, medium volume" returned a parsed brief, an explicit missing quantity field, a follow-up question and supplier rows carrying scores, match reasons, a verified-source-factory flag, profile and inquiry URLs and the evidence quote from each supplier's own page, against 507 published records; `list_facets` with `field=process` returned 472 CNC milling, 317 CNC turning, 226 sheet metal fabrication, 160 grinding, 99 five-axis, 91 EDM, 66 3D printing and 17 Swiss machining. Only person-reviewed records are indexable, and a field is a claim from the cited source rather than a capability guarantee, which is why every match ships its quote. Sourcing step the manufacturing class lacked, next to the catalogued process knowledge surface and the supplier price-drift tool. Gap named: Chinese machining suppliers only. |

## Also Identified (not catalogued)

- **Terminal Tax** (`https://mcp.terminal.tax/v1/hosted-mcp`, keyless 200, serverInfo `terminal-tax` 0.312.0, 3 tools): an Authorized IRS e-file Provider that files one original tax year 2025 US federal individual return, no state return. Consumer tax filing rather than an operator data surface, in the class that already holds the consumer personal-finance ledger.
- **Signatoro** (`https://signatoro.com/mcp`, 200, serverInfo `signatoro` 1.0.1, OAuth 2.1 with dynamic client registration): held because the endpoint contradicted the submission. Its tools hold the signed-in person's email signature block and `get_signature` returns that as html and text, a productivity utility rather than the e-signature action the issue described.
- **Caybl** (`https://api.caybl.ai/mcp`, 401 for a missing bearer token): held as a competing product, not a catalog entry. Its own page sells a hosted Google Ads, Analytics and Search Console MCP with a free 50-credit chat of its own.
- **Outrank**, **Weeklane**, **Johto Data**, **Faceabot**, **Lumi Trades**, **Mage**: held against the saturated SEO class, personal planning, agent-payments, tool-directory, trading and media-generation precedents respectively.
- **mambalabsdev** five new submissions (partner and member directory extractor, personal email to company resolver, person LinkedIn URL resolver, company headcount estimator, local rank and map pack tracker): class-covered by the vendor-suite ruling rather than re-litigated per item.
- **Feed cards never named before**: Clevera (how-to videos and help-center management, media generation), Tinymusic (consumer music generation), Dead Brands Bot Arena (agent entertainment), and an unofficial ChatGPT top-up reseller skipped as a resale service with no data surface.
- **404 shells**: recap-raven, lucyd-trade and superbotgg detail pages returned 404. Every other `/all` slug on pages 1 to 3 matched a recorded disposition.

## Directory Listing Re-verification

Run alongside this sweep, since the prior two sweeps deferred it:

| Directory | Status | Evidence |
|---|---|---|
| mcpservers.org | LISTED | `/servers/corpusiq-io` serves the page, title "CorpusIQ MCP Server \| Awesome MCP Servers" |
| smithery.ai | LISTED | registry `?q=corpusiq` returns `Cprusiq`, displayName CorpusIQ |
| PulseMCP | LISTED | one server for corpusiq, `https://www.pulsemcp.com/servers/corpusiq` |
| Glama | LISTED | `/mcp/servers/CorpusIQ/corpusiq-docs` serves the record, title "corpusiq by CorpusIQ"; connector record at `/mcp/connectors/io.corpusiq/multi-source-mcp` |
| mcp.so | NOT LISTED | six slug forms probed 404 (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`, `corpusiq-multi-source-mcp`, `multi-source-mcp`); account quarantine holds, no resubmit |

No new third-party MCP directories surfaced in this cycle's search; the directory-discovery lane is unchanged since the last dirsub pass.

## Method

Sources: mcpservers.org `/all` pages 1 to 3 newest-first through the r.jina.ai reader proxy (89 unique slugs, cross-referenced slug by slug against the index headings, the guide directories and every sweep record); mcp.so `/feed` page 1 (30 server cards read from the TanStack payload, four never named before); chatmcp/mcpso issue window #5924-#5954 fetched with bodies in one call. Every candidate was settled by a live JSON-RPC probe, and the three catalogued servers were driven with real tool calls whose returned values appear above.

Catalog 972 to 975 servers (+852 to +855 guides).
