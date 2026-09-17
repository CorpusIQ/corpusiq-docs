---
title: "MCP Discovery Sweep - August 30, 2026 (Night)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august30-2026-night/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# MCP Discovery Sweep - August 30, 2026 (Night)

- **Run:** Aug 30, 2026 ~02:00 UTC (19:00 MST), Spark (fresher clone; Mac Mini up but stale at Aug 29 night)
- **Shift label:** Night (~19:00-23:00 MST convention; first Aug 30 night section, no collision)
- **Issue window:** chatmcp/mcpso #3840-#3844 (cutoff: midday sweep high-water mark #3839)
- **Sources:** chatmcp/mcpso issues, mcp.so homepage (recentServers), mcp.so feed, mcpservers.org homepage, mcpservers.org /all pages 1-3
- **Catalogued:** 6 new servers + guides (443 servers, +329 guides)
- **Commit:** pushed to main from Spark

## Catalogued

- **Wiki.js MCP** (issue #3840) - ni-c stdio server for self-hosted Wiki.js 2.x: 62 tools over pages, version history, tags, assets, comments, users, groups and system settings via the GraphQL API. grep_pages compensates for title-only default search, update_page is compare-and-swap, destructive/admin ops need server-issued confirmation tokens, WIKIJS_READ_ONLY and WIKIJS_ALLOWED_PATHS confinement, no API-key-minting tool. npm @ni-c/wikijs-mcp v0.1.2, MIT, registry io.github.ni-c/wikijs-mcp v0.1.0-v0.1.2. Repo 0 stars, created Aug 30, 2026. Guide at `hermes/mcp/servers/external/wikijs-mcp/`, relevance ★★.

- **imap-mcp** (issue #3843) - ni-c stdio server for any IMAP mailbox with a deliberate no-send design: folders, search, read via BODY.PEEK (unread state preserved), agent-side seen tracking, attachment saves, draft-only replies. Messages arrive nonce-fenced with SPF/DKIM/DMARC verdicts, prompt-injection-shape flags and defused markdown images. Writes off unless IMAP_READ_ONLY=false, deletes via human elicitation, 11 tools (6 essential mode). npm @ni-c/imap-mcp v0.2.0, MIT, registry io.github.ni-c/imap-mcp v0.2.0. Repo 0 stars, created Aug 26, 2026. Guide at `hermes/mcp/servers/external/imap-mcp/`, relevance ★★.

- **Tactiq MCP** (mcp.so feed catch-up, listed Aug 15) - hosted meeting transcript intelligence: search, read and summarise Google Meet, Zoom and Teams transcripts across the whole meeting history. Endpoint mcp.tactiq.io live-verified (anonymous initialize 401 missing_token = sign-in auth, Jitsu/Taskfolk class). Verified Claude connector (two-click connect), works with Cursor, ChatGPT, Gemini and any MCP client. Free plan; paid tiers lift the plan gate on summary-content reads (free/Pro plans can find meetings but not read summary content). No public repo. Guide at `hermes/mcp/servers/external/tactiq-mcp/`, relevance ★★★.

- **Gemina MCP** (mcp.so feed catch-up, listed Jul 21) - hosted document intelligence: 13 tools to extract, tag, search and aggregate invoices, receipts, contracts, forms and custom templates. OAuth 2.1 sign-in or API key at api.gemina.co/api/v1/mcp/, free FileTag tier, EU/US/Israel/Asia data residency. Tool names recovered from the listing state (extract_document, files_create_upload, files_create_extraction_upload, get_extraction_result, list_extractions, index_document, query_documents, aggregate_documents, tag_file, tag_url, custom_template, submit_extraction_feedback, explain_* helpers). No public repo. Guide at `hermes/mcp/servers/external/gemina-mcp/`, relevance ★★.

- **HasData MCP** (mcpservers.org /all catch-up; resolves the Aug 29 midday "future catch-up candidates" note) - hosted web-data gateway: 40+ connector tools over real estate (zillow_listing/property, redfin_listing/property), hospitality (airbnb_listing/property, booking_place/search), hiring (indeed_job/listing, glassdoor_job/listing), local business (yelp_place/reviews, yellowpages_place/search), e-commerce (shopify_collections/products, amazon_*), search and trends (google_serp family, google_maps_*, google_trends_search, google_travel_*, bing_serp, duckduckgo_serp) and social (tiktok_*, instagram_*, google_images, web_scraping). Endpoint mcp.hasdata.com/mcp, x-api-key header (HASDATA_API_KEY), connector selection via ?apis= param, credit-priced. Tool names recovered from docs.hasdata.com/mcp-server. Guide at `hermes/mcp/servers/external/hasdata-mcp/`, relevance ★★.

- **Contextflo MCP** (mcp.so feed catch-up, listed Jul 9) - governed team data queries: connect BigQuery, Snowflake, Postgres, Redshift, Databricks or ClickHouse (or CSV upload), ask questions and build live auto-refreshing dashboards in chat, with table-level access control. Endpoint mcp.contextflo.com/mcp live-verified (anonymous initialize returns JSON-RPC 401 Authentication required). Docs at contextflo.com/docs with MCP client pages for Claude and ChatGPT. No public MCP repo (0-star org repos). Capability-level tools table with caveat. Guide at `hermes/mcp/servers/external/contextflo-mcp/`, relevance ★★.

## Also identified (not catalogued)

- projectlaunch.ai #3844 - pre-launch agent-facing site with zero pricing and an intent-capture tool - premature class, Krimskrams precedent.
- NoteMCP #3842 - hosted personal notes and long-term memory for a single user - personal-library class, smry Product and Savee precedent.
- MCP Emails #3841 - resubmission of the prose-only "Mcp Emails" body entry already in the catalog since the June 22 sweep - BuyWhere precedent; noted that the entry still lacks a guide directory.
- FlightQueue, FlightSeatMap, Airport Lounge List - consumer travel class.
- Quidli Connect - handle-to-wallet resolution and token sending - token payment plumbing class (Kura/402oracle precedent).
- Blooket Simulator (classroom game), Shotlingo (language-learning app) - consumer class.
- fetch-cwe-list (CWE security-list fetcher) - dev utility class.
- /all page repeats were prior-sweep dispositions: Valmera (native-creator class), Kivgraph (code graph), Fatenava (astrology), OctoWatch DLP (thin docs), CSVBox (thin docs, endpoint 405), Tillpad (agent storage infra), devinchen2014 X/Weibo scrapers (consumer social class), SocialDataX family (commercial social-data reseller class), granola (famous-name re-index), and the thin-docs slug list from the midday sweep. Catalogued-with-guide repeats: Insourcia, PolicyForge, PreVibe, AngelOne, Security Recipes, Cookie Free Analytics.

## Mechanics

- Cross-reference: bare-brand grep over index.md with variant generation (hyphen->space, stripped, dot->space, bare brand) plus full-line context reads to distinguish catalogued vs skip-prose vs false-positive hits; 135 unique slugs checked.
- Registry verification: npm registry (versions, publish dates), official MCP registry search (confirmed io.github.ni-c/wikijs-mcp v0.1.0-v0.1.2 and io.github.ni-c/imap-mcp v0.2.0), GitHub API (stars, license, creation dates).
- Endpoint probing: batch-probe.py on mcp.tactiq.io (401 missing_token) and app.tactiq.io/mcp (405, app path); direct initialize on mcp.contextflo.com/mcp (401 Authentication required). 401-is-liveness doctrine applied for both hosted services.
- Tool-name recovery: HasData from the vendor's official docs page; Gemina from the mcp.so listing state; Contextflo and Tactiq as capability-level tables with the explicit caveat line (anonymous enumeration refused).
- Index patched with one atomic Python patcher (assert-before-write: last-updated line, top sweep section, docs-links tail block); guides validated with bundled validate-guides.py (6/6 PASS) plus See Also dir-existence and label-accuracy checks against real target titles (7 labels corrected pre-commit).
- Shift label collision check: grep for "Night Cron Sweep" before naming - no Aug 30 night section existed.
