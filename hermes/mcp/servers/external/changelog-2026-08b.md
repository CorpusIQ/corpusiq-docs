---
title: "Catalog Sweep Log Archive - August 16-31, 2026"
description: "External MCP server catalog sweep log, August 16-31, 2026 archive: directory movement, measured candidates, hold decisions"
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/changelog-2026-08b/"
robots: "noindex,follow"
last_updated: "2026-11-23"
tags: ["mcp server", "model context protocol", "sweep log"]
---

# External MCP Server Catalog - Sweep Log, August 16-31, 2026

Archive for August 16-31, 2026. Discovery passes appear newest first. The [current sweep log](/hermes/mcp/servers/external/changelog) carries the most recent passes.

Archive: [August 1-15, 2026](/hermes/mcp/servers/external/changelog-2026-08a) | [September 1-15, 2026](/hermes/mcp/servers/external/changelog-2026-09a)

## 🆕 August 31, 2026 - Evening Cron Sweep (2 New, 2 Guides)

Evening sweep sourced from the mcp.so homepage recentServers array and the mcpservers.org homepage latest array (the fresh window after the afternoon sweep). 2 new business-relevant servers catalogued with guides, one live-verified over JSON-RPC: CarChat Inventory MCP (official MCP for the carchat.io live-dealership-inventory search - 6 tools covering plain-English inventory search with structured filters, VIN and listing detail, curated metro category pages, a dealer directory with per-dealer counts, live market price statistics by body style and metro, and a consent-gated buyer inquiry relay to the selling dealer - endpoint carchat.io/mcp live-probed as carchat v1.0.0 with all 6 tools, no auth, MIT), ConsentStack MCP (hosted consent management platform MCP - 22 tools for GDPR/CCPA cookie consent end to end: site creation, draft-staged banner configuration and publishing, install snippets, compliance scans and tracker categorization over OAuth 2.1 - endpoint app.consentstack.io/api/mcp 401-verified live, registry io.consentstack/cookie-consent).

[CarChat Inventory MCP - Live US Dealership Inventory and Market Prices](/hermes/mcp/servers/external/carchat-inventory-mcp) · 6 tools, no-auth endpoint, live-probed.
[ConsentStack MCP - Agent-Managed Cookie Consent and Compliance](/hermes/mcp/servers/external/consentstack-mcp) · 22 tools, OAuth 2.1, registry-listed.

**Also identified (not catalogued):** GridCarbon (grid carbon intensity for 45 zones from ENTSO-E, EIA-930 and NESO - pre-alpha single-dataset utility class), Onchain Diary (read-only Web3 on-chain security knowledge base, 97 articles plus 220 glossary terms - niche educational class), CordFind Generator Compatibility MCP (generator guide search and extension-cord sizing - consumer DIY class), Vaanzari Commerce (Banarasi saree discovery and shopping workflows - consumer commerce class), Firefly III MCP Server (self-hosted personal finance with scoped read/write/delete tools - personal-finance class), SigVest (personal portfolio analysis, news impact and tax harvesting - consumer investing class). mcp.so recentServers repeats and prior dispositions (file2markdown, BiGapi, DrillerDB, MagicPixel.art, Forency, TikTok Transcript MCP, CrawlForge).

## 🆕 August 31, 2026 - Late-Day Sweep (3 New, 3 Guides)

Late-day sweep over chatmcp/mcpso issues #3858-#3863 (past the afternoon cron's #3857 cutoff). 3 new business-relevant servers catalogued with guides, all live-verified over JSON-RPC: Gemalli B2B Trade (global B2B trade read toolset - wholesale product search with category/country/MOQ/price filters, verified manufacturer catalog, sanctions screening and HS codes; no auth for reads, endpoint gemalli.com/api/mcp verified as gemalli-mcp v0.1.0), DFX Real Estate Intelligence (9 tools over US commercial and multifamily real estate - property and parcel resolution, ownership, recorded sales, measured coverage, near-term commercial debt timing; no key for 8 of 9 tools, endpoint verified as dfx-real-estate v0.2.0), VulX Watch (independent security review for AI-built apps - watch a GitHub repo, read-only status of the last reading, never a patch; OAuth GitHub, endpoint live but token-gated).

[Gemalli B2B Trade MCP - Global Wholesale Sourcing for Agents](/hermes/mcp/servers/external/gemalli-b2b-trade-mcp) · product search, verified manufacturers, sanctions/HS codes, live-verified.
[DFX Real Estate Intelligence MCP - US Property, Parcel and Debt Data](/hermes/mcp/servers/external/dfx-real-estate-mcp) · no-key, debt timing, coverage honesty, live-verified.
[VulX Watch MCP - Independent Security Review for AI-Built Apps](/hermes/mcp/servers/external/vulx-watch-mcp) · watch-not-patch, OAuth GitHub, endpoint live.

**Also identified (not catalogued):** BioVet MCP (Moscow veterinary clinic network - single-city vertical class), Neuronto Agentic Resource Discovery (agent dev infrastructure class), NEX Agent (A2A agent on Base with x402 payments - crypto/dev class), EditItAll MCP (local-first in-browser editors - dev utility class), JSONGuy (JSON formatter/validator - dev utility class), Truth Bear GAUGE (Bitcoin-anchored fact verification - niche trust class), Aluvia takedown request (#3852, administrative). yg3-mcp (#3858) already catalogued.

## 🆕 August 31, 2026 - Afternoon Cron Sweep (4 New, 4 Guides)

Afternoon sweep over chatmcp/mcpso issues #3848-#3857 (the fresh window after the midday sweep) plus an mcpservers.org /all page-1 cross-ref. 4 new business-relevant servers catalogued with guides, two live-verified over JSON-RPC: Edgrapi MCP (hosted SEC EDGAR structured data - Form 4 insider trades with cluster-buy detection, typed 8-K events, CUSIP-aggregated 13F holdings diffed quarter over quarter, 13D/G stakes, XBRL fundamentals and ratios - endpoint api.edgrapi.com/mcp probed with all 9 tools), Small Business Intelligence by Brick & Mortar (keyless local-market intelligence - 25 joined public-records datasets and 1.57M rows for the seven-county Minneapolis-St. Paul metro plus nine teardown and market-scan frameworks for any US metro - endpoint brickandmortar.dev/mcp probed as small-business-intelligence v0.1.0 with all 11 tools), DocMake MCP (official template-to-DOCX/PDF generation platform - 6 stdio tools with strict rendering, MCP resources and a guided render prompt - npm @docmake/mcp v0.1.1, registry io.docmake/mcp), Atomic Mail MCP (programmable email inbox for agents - JMAP stdio proxy @atomicmail/mcp-github v0.3.26, proof-of-work signup, custom-domain sending behind a human dashboard control plane - 255-star MIT repo, catch-up from the /all page).

[Edgrapi MCP - SEC EDGAR Structured Data for Agents](/hermes/mcp/servers/external/edgrapi-mcp) · hosted, live-probed 9 tools.
[Small Business Intelligence MCP - Metro Records and Teardowns](/hermes/mcp/servers/external/small-business-intelligence-mcp) · keyless, live-probed 11 tools.
[DocMake MCP - Template-Driven DOCX and PDF Generation](/hermes/mcp/servers/external/docmake-mcp) · stdio, npm verified.
[Atomic Mail MCP - Programmable Inbox for AI Agents](/hermes/mcp/servers/external/atomic-mail-agentic) · stdio, 255 stars.

**Also identified (not catalogued):** Truth Bear GAUGE #3850 (resubmission of the already-catalogued truth-bear-gauge entry - BuyWhere precedent), JSONGuy #3851 (JSON formatter/repair - dev utility class), EditItAll #3854 (in-browser editors - creator/desktop utility class), NEX Agent Co. #3855 (A2A agent with x402 - agent infra class), Neuronto ARD Index #3857 (agentic resource discovery - agent infra class); /all page repeats and catch-ups: Automated Video App, CampingRoute, Agent Reliability, Percona Pg, Terminal MCP, GetBirthChart, Fanus AI, Soulfield Lens (prior disposition), Render MCP, Rumors Lines, Th Memory and Trvrse (creator, consumer, dev-infra and consumer-entertainment classes).

## 🆕 August 31, 2026 - Midday Sweep (3 New, 3 Guides)

Midday sweep sourced from the mcpservers.org /all page (newest-first), cross-checked against the morning sweep's dispositions. 3 new business-relevant servers catalogued with guides, two of them live-verified over JSON-RPC: SEC EDGAR Full-Text Search MCP (Apify-hosted actor wrapping sec.gov/edgar/search as tools - keyword search with every form filter, company lookup, filing document retrieval - for diligence, competitive intelligence and public-company research), Trooth Network MCP (remote read-only no-auth trust layer - witnessed Trust Profiles, outside-in domain security reads, Trust Ledger Token verification - endpoint api.trooth.co/public/mcp initialize-verified as trooth-mcp v1.1.0), Saaskly MCP (official UK/EU B2B IT and telecom comparison data - VoIP, transactional email, cloud management, SEO/GEO/AEO, social media - endpoint saaskly.com/mcp initialize-verified as saaskly v1.0.0, stateless).

[SEC EDGAR MCP - Full-Text Filing Search for Agents](/hermes/mcp/servers/external/sec-edgar-mcp) · Apify-hosted, form filters, company lookup.
[Trooth Network MCP - Witnessed Company Trust Records](/hermes/mcp/servers/external/trooth-mcp) · remote no-auth, source-labeled provenance, live-verified.
[Saaskly MCP - Evidence-Based B2B Software Comparison](/hermes/mcp/servers/external/saaskly-mcp) · official hosted, UK/EU comparisons, live-verified.

**Also identified (not catalogued):** Florida Sunbiz MCP (Florida Division of Corporations records - single-US-state registry class), SEO Landing MCP (agent skill for building SEO landing pages - dev tooling class), LegalAIMCP (law-firm AI directory with scoring - vertical directory class), Soulfield Lens MCP (AI-text review layer - QA utility class, morning-sweep disposition), OpenQR MCP (QR generation with scan analytics - marketing utility class), Gamedai NFL MCP and futbolatlas (consumer sports class, prior-sweep disposition), FlashDesk MCP and ShadowGraph (dev automation / agent infra classes, prior-sweep dispositions).

## 🆕 August 31, 2026 - Morning Cron Sweep (1 New, 1 Guide)

Morning sweep sourced from chatmcp/mcpso issues #3845-#3847 (fresh window after the night sweep's #3844 cutoff), the mcp.so homepage and feed, and the mcpservers.org homepage. 1 new business-relevant server catalogued with a guide: OpenHire MCP (agent-native job protocol over ~120 employers' first-party ATS APIs - 16,000+ live AI/infra, autonomous-driving and embodied-AI postings in the US, Europe and China with verified_at freshness stamps, ghost_score stale-listing detection and deep-linked employer apply URLs; stdio via uvx openhire or pipx, local-first matching so a résumé never transits the server, MIT, registry io.github.gzchenhao/openhire v0.2.0).

[OpenHire MCP - AI, Infra, and Robotics Jobs from Employer ATS APIs](/hermes/mcp/servers/external/openhire-mcp) · 5 tools, local-first privacy, stdio via uvx.

**Also identified (not catalogued):** ShadowGraph #3846 (local-first decision memory for AI agents - agent dev infrastructure class, AURORA precedent), local-gpu-imagegen #3847 (local ComfyUI/WebUI/Diffusers image generation for agents - creator utility class, klo-mcp precedent), treg.to (pay-per-call gateway to 3,028 third-party APIs - API-gateway infrastructure class), Gamedai NFL MCP (fantasy football scores and start/sit calls - consumer sports class), FlashDesk MCP (remote desktop control from Claude Code - dev automation class), Hispanic Legacy MCP (Spanish science and culture knowledge base - niche educational class), Soulfield Lens MCP (independent AI-text review layer - QA utility class). mcp.so homepage and feed repeats were prior-sweep dispositions (File2Markdown, BiGapi, DrillerDB, MagicPixel, CrawlForge, Ransack, Genviral, AgendaForge, BidSkim, OmniSocials, SocialRobot, Hologrow, Forency, Tactiq, Gemina, Contextflo); mcpservers.org homepage slugs beyond the five evaluated above were famous-name re-indexes.

## 🆕 August 30, 2026 - Night Cron Sweep (6 New, 6 Guides)

Night sweep sourced from chatmcp/mcpso issues #3840-#3844 (fresh window after the midday sweep's #3839 cutoff), the mcp.so feed and mcpservers.org /all pages 1-3. 6 new business-relevant servers catalogued with guides: Wiki.js MCP (ni-c; 62 tools over pages, version history, tags, assets, comments, users, groups and system settings on a self-hosted Wiki.js 2.x - grep_pages compensates for Wiki.js' title-only search, update_page refuses stale overwrites and destructive ops need a server-issued confirmation token; stdio via npx @ni-c/wikijs-mcp, MIT, registry io.github.ni-c/wikijs-mcp v0.1.2), imap-mcp (ni-c; read-only-by-default IMAP mailbox operations with a deliberate no-send design - BODY.PEEK preserves unread state, messages arrive nonce-fenced with SPF/DKIM/DMARC verdicts and prompt-injection-shape flags and drafts save to your own Drafts folder; stdio via npx @ni-c/imap-mcp, MIT, registry io.github.ni-c/imap-mcp v0.2.0), Tactiq MCP (meeting transcript intelligence - search, read and summarise Google Meet, Zoom and Teams transcripts across your whole meeting history; hosted at mcp.tactiq.io with Tactiq sign-in, a verified Claude connector and a free plan), Gemina MCP (document intelligence - extract, tag, search and aggregate invoices, receipts, contracts, forms and your own templates with 13 tools over OAuth 2.1 or an API key; api.gemina.co/api/v1/mcp/, free FileTag tier, EU/US/Israel/Asia data residency), HasData MCP (marketplace and web data gateway - zillow and redfin real estate, airbnb and booking hospitality, indeed and glassdoor hiring, yelp and yellowpages local business, shopify and amazon e-commerce, SERP, Maps, Trends and more from one hosted endpoint; mcp.hasdata.com/mcp with an x-api-key, credit-priced), Contextflo MCP (governed team data queries - connect BigQuery, Snowflake, Postgres, Redshift, Databricks or ClickHouse and ask questions or build live dashboards in chat with table-level access control; mcp.contextflo.com/mcp, endpoint live-verified). The HasData batch resolves the Aug 29 midday "future catch-up candidates" note.

[Wiki.js MCP - Self-Hosted Wiki Knowledge Operations for Agents](/hermes/mcp/servers/external/wikijs-mcp) · 62 tools, confirmation-token admin ops, stdio via npx.
[imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/hermes/mcp/servers/external/imap-mcp) · 11 tools, deliberate no-send design, MIT.
[Tactiq MCP - Meeting Transcript Intelligence for Agents](/hermes/mcp/servers/external/tactiq-mcp) · hosted, verified Claude connector, free plan.
[Gemina MCP - Document Extraction and Tagging for Agents](/hermes/mcp/servers/external/gemina-mcp) · 13 tools, OAuth or API key, free FileTag tier.
[HasData MCP - Marketplace and Web Data Gateway for Agents](/hermes/mcp/servers/external/hasdata-mcp) · 40+ connector tools, x-api-key, credit-priced.
[Contextflo MCP - Governed Team Data Queries for Agents](/hermes/mcp/servers/external/contextflo-mcp) · warehouse connectors, table-level access control.

**Also identified (not catalogued):** projectlaunch.ai #3844 (pre-launch agent-facing site with zero pricing and an intent-capture tool - premature class, Krimskrams precedent), NoteMCP #3842 (hosted personal notes and long-term memory for a single user - personal-library class, smry Product and Savee precedent), MCP Emails #3841 (resubmission of the prose-only "Mcp Emails" entry already in the catalog body since the June 22 sweep - BuyWhere precedent; the entry still lacks a guide directory), FlightQueue (airport security wait times and FAA delays - consumer travel class), FlightSeatMap (seat maps and reviews - consumer travel class), Airport Lounge List (lounge access lookup - consumer travel class), Quidli Connect (handle-to-wallet resolution and token sending - token payment plumbing class), Blooket Simulator (classroom game - consumer class), Shotlingo (language-learning app - consumer class), fetch-cwe-list (CWE security-list fetcher - dev utility class). /all page repeats were prior-sweep dispositions (Valmera, Kivgraph, Fatenava, OctoWatch, CSVBox, Tillpad, devinchen2014 scrapers, SocialDataX family, granola re-index and the thin-docs slug list).

## 🆕 August 30, 2026 - Midday Cron Sweep (1 New, 1 Guide)

Midday sweep sourced from chatmcp/mcpso issues #3835-#3839 (fresh window after the morning sweep's #3834 cutoff), the mcp.so homepage and mcpservers.org /all pages 1-3. 1 new business-relevant server catalogued with a guide: Laver (official MCP server from the laver.app team project management tool - 59 tools over kanban boards, tickets, comments, subtasks, labels, custom fields, attachments, wiki pages, automations and published links; stdio via npx @laver/mcp with a workspace-scoped API key that acts as the person who created it; versioned writes with a 409 re-read-and-retry contract so an agent and a person can work the same board at once; MIT, registry io.github.Developyn/laver-mcp v0.5.0; free plan up to 3 billable people, Pro £2.99/person/month).

[Laver MCP - Kanban Boards, Sprints and Team Wiki for Agents](/hermes/mcp/servers/external/laver-mcp) · 59 tools, versioned writes, stdio via npx.

**Also identified (not catalogued):** Faxer #3836 (resubmission of the fax-ops utility already skip-classed in four prior sweeps - utility class), 402Signal #3837 (fail-closed x402 endpoint router - x402 infrastructure class, 402oracle precedent), mcpx #3838 (MCP client, not a server), kwnva.design portfolio #3839 (personal studio portfolio catalog - portfolio class), file2markdown (document and web-page to Markdown conversion for agents - dev utility class, BiGapi and Booklet precedent). mcpservers.org /all pages 1-3 and the mcp.so homepage carried no other new slugs - the remaining never-seen slugs (pfsense-mcp-server, etch-mcp, mdedit-agent-plugin, kitchensink4word, mcp-light-memory, wuwei-mcp, deskmcp, rhizome-mcp, nanoparse-mcp, enviadores-mcp, phi-guard-mcp, memesh-llm-memory, ghiblimcp) return generic directory pages with no listing (thin-docs class); all other slugs were morning-sweep or prior-sweep dispositions.

## 🆕 August 30, 2026 - Morning Cron Sweep (2 New, 2 Guides)

Morning sweep sourced from mcpservers.org /all pages 1-4 (43 slugs), the mcp.so feed (30 entries) and latest tab, and chatmcp/mcpso issues #3831-#3834. 2 new business-relevant servers catalogued with guides: Relm (official API-first CRM for AI agents - 41 MCP tools over contacts, companies, deals, activities, pipelines, automations, drip sequences, templates and webhooks; Streamable HTTP at api.relmcrm.com/mcp with OAuth 2.1 DCR or bearer keys, live/test modes where test keys write to a sandboxed dataset auto-deleted after 7 days, idempotent creates, optimistic concurrency with version-conflict detection, RFC-9457 errors carrying valid_options and suggestions, HMAC-signed webhooks, and Free 1k requests/month through Pro $29/mo to Scale $249/mo; endpoint live-verified - serverInfo relm v0.17.1 plus a public 41-tool tools/list), Sequel (hosted natural-language Google Search Console analytics from sequel.sh - the Sequel CLI provisions an org-scoped read-only OAuth connection into Claude Code, Cursor, VS Code, Windsurf, Zed, Codex, OpenClaw or Hermes; plain-English queries over clicks, impressions, CTR and position by query, page, device, country and date with 25k rows per request and a 16-month lookback, plus cross-source joins with GA4, Stripe, HubSpot, Ahrefs, Apollo and 20+ other sources; no raw public endpoint - connection flows through the CLI).

[Relm MCP - API-First CRM for AI Agents](/hermes/mcp/servers/external/relm-mcp) · 41 tools, OAuth 2.1 or bearer key, live-verified endpoint.
[Sequel MCP - Google Search Console in Natural Language](/hermes/mcp/servers/external/sequel-mcp) · CLI-provisioned, read-only OAuth, cross-source joins.

**Also identified (not catalogued):** smry Product #3831 (read-it-later library, feeds, notes and page-change monitors for an agent's own research - personal-library class, Savee/MarkIt precedent), VASTlint #3832 (IAB VAST/VMAP/DAAST ad-tag validation - single-purpose ad-tech QA class), yotta-verify-mcp #3833 (pre-install security scanner for agent skills - dev-tool class, Sentinel Scan precedent), sandbase-harness #3834 (stdio bridge to the SandBase agent harness - dev infra class), BaseBounty (x402 bounty board on Base with ERC-8183 escrow - agent task-marketplace class, TooHardBasket precedent), MCP Rigor (natural-language acceptance testing for MCP servers - dev-tool class, dsh-verify precedent), Open Call Portals (live-entertainment booking infrastructure - entertainment vertical niche), iLook Face Analysis (consumer face-scoring - consumer class), Rare Cloud/Behzad9 (GitHub profile listing with no MCP surface - thin docs), BiGapi (no tools detected, output-layer file operations - dev publishing class, plyo-mcp precedent). Feed and /all repeats already evaluated in prior sweeps (Genviral, Spike, Appbot, TuFirma, DrillerDB, Ransack, AgendaForge, BidSkim, OmniSocials, SocialRobot, TikTok Transcript MCP, Forency, AdaptlyPost, MagicPixel.art, YOUB, CrawlForge, Foremerge, OrbitWan, Katto, Uwear.ai, Graviti, Speccy x402, Jitsu, Hologrow, OpenLore, Legion MCP, fhirHydrant, YouTube Transcript AI, QuanticData, Windframe, Alpha Sophia, Poly-Glot AI Workspace, Otto Webmaster, TakeNorFree, LoanCalculatorMCP, BestElectricProducts, ViralDanceMaker, Footix, MarketMaster, Metalend, OpenBoss, IronShard, Hexum, Strunk, PilotMyX, ConnectPeon, SuggestAPI, Sirveil, BidSwarm, WonderCal, Maroo, Helena bioinformatics, AgentCouch).

## 🆕 August 29, 2026 - Evening Cron Sweep (4 New, 4 Guides)

Evening sweep sourced from the mcp.so feed (30 submissions), mcpservers.org /all pages 1-3 (30 slugs) and chatmcp/mcpso issues #3827-#3830 (fresh window after the midday sweep's #3826 cutoff). 4 new business-relevant servers catalogued with guides: Genviral (official hosted MCP from the Genviral social media platform - 16 tools across four OAuth scopes covering account reads, analytics, trend research, the content library, post preparation, publishing, and AI generation of images, videos and slideshows in Studio; publishes to TikTok, Instagram, YouTube, Pinterest, LinkedIn, Facebook, X, Bluesky, Mastodon and Telegram with idempotency-key duplicate-safe publishing and per-workspace scoping; endpoint 401-verified live), Spike (official incident management MCP from spike.sh - 51 tools with an API key or 59 with OAuth over incident stats and MTTA/MTTR, create/ack/resolve, on-call rotations and overrides, alert routing, outbound webhooks and escalation policies; stateless bridge with no destructive tools; endpoint live-verified), Appbot (official beta MCP from the app review intelligence platform - App Store and Google Play reviews, ratings, sentiment, topics, emotions, keywords, feature requests and competitor comparisons in natural language; OAuth at api.appbot.co/mcp), TuFirma (Spanish electronic-signature MCP - 24 tools over the public API to consult documents and templates, create signature flows, upload PDFs, and sign, request OTP, remind, cancel or reject; tf_sk_* API key with scoped permissions; endpoint live-verified).

[Genviral MCP - Social Media Creation and Publishing for AI Assistants](/hermes/mcp/servers/external/genviral-mcp) · 16 tools, 4 OAuth scopes, 10 platforms, idempotent publishing.
[Spike MCP - Incident Management and On-Call for AI Assistants](/hermes/mcp/servers/external/spike-mcp) · 51-59 tools, API key or OAuth, no destructive actions.
[Appbot MCP - App Review Intelligence for AI Assistants](/hermes/mcp/servers/external/appbot-mcp) · beta, OAuth, reviews, sentiment, topics, feature requests.
[TuFirma MCP - Spanish Electronic Signatures for AI Assistants](/hermes/mcp/servers/external/tufirma-mcp) · 24 tools, scoped API key, Streamable HTTP.

**Also identified (not catalogued):** Neurobird Search #3827 (2-tool web search with quote verification - saturated web-search class, Ransack and QuanticData precedent), Award Travel Finder #3828 (consumer award-flight search - travel class), plyo-mcp #3829 (durable artifact publishing for coding agents - dev publishing class, thing and Booklet precedent), Noodle Biomedical Literature Discovery #3830 (biomedical literature - niche research class). mcp.so feed repeats and prior dispositions (DrillerDB, Ransack, AgendaForge, BidSkim, OmniSocials, SocialRobot, TikTok Transcript MCP and Forency catalogued in earlier sweeps; AdaptlyPost, MagicPixel.art, YOUB, CrawlForge, Foremerge, OrbitWan, Katto, Uwear.ai, Graviti, Speccy x402, OpenLore, Legion MCP, fhirHydrant, YouTube Transcript AI, QuanticData, Windframe and Poly-Glot AI Workspace skip-classed in prior sweeps). mcpservers.org /all dispositions: Otto Webmaster already catalogued as Otto MCP in the morning sweep; TakeNorFree (domain availability lookup - Domain Search King class), LoanCalculatorMCP (consumer loan-math utility), BestElectricProducts (consumer editorial content), ViralDanceMaker (consumer creative), plus midday-sweep skips (Footix, MarketMaster, Metalend, OpenBoss, IronShard, Hexum, Strunk, PilotMyX, ConnectPeon, SuggestAPI, Sirveil, BidSwarm, WonderCal, Maroo) and the Helena bioinformatics and host-dump slugs.

## 🆕 August 29, 2026 - Midday Cron Sweep (13 New, 13 Guides)

Midday sweep sourced from chatmcp/mcpso issues #3817-#3826 (fresh window after the morning sweep's #3816 cutoff), the mcp.so feed (30 slugs), and mcpservers.org /all pages 1-3 (90 slugs). 13 new business-relevant servers catalogued with guides: 

[Israel Business Intelligence MCP - Israeli Company Verification for Agents](/hermes/mcp/servers/external/israel-business-intelligence-mcp) · 3 tools live-probed, x402 verify_company (0.05 USDC), keyless discovery.
[Sourcey MCP - Startup Credits and Agent Readiness Data](/hermes/mcp/servers/external/sourcey-mcp) · 8 tools live-probed, keyless catalog reads, signed change feed.
[ISO 20022 Generator MCP - SEPA XML and SWIFT MT103 from Chat](/hermes/mcp/servers/external/iso-20022-generator-mcp) · 4 tools, XSD-validated output, API key, 401-verified live.
[Equibles MCP - SEC Filings and Market Data for AI Agents](/hermes/mcp/servers/external/equibles-mcp) · 61 tools, primary regulatory sources, 202 stars, AGPL.
[Insourcia MCP - French Company Intelligence for AI Agents](/hermes/mcp/servers/external/insourcia-mcp) · SIREN/SIRET search, ownership graphs, OAuth or API key.
[Apple Ads MCP - App Store Campaign Operations from Your Terminal](/hermes/mcp/servers/external/apple-ads-mcp) · 24 tools, local Go binary, receipt-gated writes, read-only default.
[Google Search Console MCP (ni-c) - Property Setup and Search Analytics](/hermes/mcp/servers/external/google-search-console-ni-c-mcp) · 21 tools, three Google APIs, setup_site ownership flow.
[CRM Solid MCP - Social DM Inbox and Scheduling Across 12 Networks](/hermes/mcp/servers/external/crmsolid-mcp) · 13 tools, inbox summary, API key.
[Cookie Free Analytics MCP - Cookieless GDPR-First Web Analytics](/hermes/mcp/servers/external/cookiefreeanalytics-mcp) · read-only aggregates, OAuth 2.1 PKCE, EU-hosted.
[healthchecks-mcp - Cron Job Health and Failure Forensics for Agents](/hermes/mcp/servers/external/healthchecks-mcp) · 14 tools, get_ping_body tracebacks, read-only keys.
[PolicyForge MCP - Legal Policies Generated and Audited from Your Codebase](/hermes/mcp/servers/external/policyforge-mcp) · 11 tools, free unlimited audits, version-tracked.
[PreVibe MCP - SaaS Product Research and Validation for Agents](/hermes/mcp/servers/external/previbe-mcp) · Google sign-in, market and competitor research.
[AngelOne MCP - Indian Market Trading and Portfolio Data for Agents](/hermes/mcp/servers/external/angelone-mcp) · 32 tools, SmartAPI, TOTP auto-login, Apache-2.0.

**Also identified (not catalogued):** Humanizer PRO #3817 (AI text humanizer - content-manipulation class), ntfy-mcp #3819 (pub-sub notification infra - dev tool class), woodpecker-ci-mcp #3820 (CI engine control - dev tool class), Orphograph #3825 (bitcoin-anchored agent notary - agent provenance infra class), MarketMaster (Kalshi/Polymarket prediction-market data - consumer gambling class, ParlayAPI precedent), Oblique Markets (x402 payment plumbing - infra class), Metalend (DeFi stablecoin yield - crypto niche), Tillpad (agent storage infra), WonderCal (agent scheduling infra), Quartermaster (game-asset vault), Valmera (agentic video editor - native-creator class), Footix (football betting analytics - gambling class), IronShard (object storage sandbox), Hexum (coding-agent cost control), Kivgraph (code graph), Firekeep (agent memory infra), Fatenava (astrology - consumer), OpenBoss (game), SuggestAPI (commerce agent gateway - thin docs), APISelf (local desktop apps), Sirveil (consumer privacy lookup), BidSwarm (rank-bidding board), Strunk (Google Docs writing workflow - Booklet class), OctoWatch DLP (thin MCP docs), PilotMyX (X-only posting - thin docs), Peon/ConnectPeon (thin docs), AdaptlyPost (no directory page - thin), CSVBox (thin MCP docs, endpoint 405 - dev-importer class), devinchen2014 X/Weibo scrapers (consumer social class).

## 🆕 August 29, 2026 - Morning Cron Sweep (8 New, 8 Guides)

Morning sweep sourced from chatmcp/mcpso issues #3811-#3816 (fresh window after the night sweep's #3810 cutoff), the mcp.so homepage and feed, and the mcpservers.org homepage plus /all pages 1-3. 8 new business-relevant servers catalogued with guides: YG3 MCP (marketing operations for autonomous agents - 197 live-verified tools over client snapshots, brand, blog content, LinkedIn, Google Ads PPC, outbound, and approvals; one unauthenticated POST provisions a sandbox workspace and returns a bearer token, repo MIT), GrowSurf MCP (official GrowSurf referral and affiliate program MCP - safe REST wrappers for campaigns, rewards, tracking installs, participants, webhooks, and analytics; npm package plus hosted remote at mcp.growsurf.com), site-spec (local deterministic audit of the website layer browsers do not render - 40 checks over robots.txt, llms.txt, canonical/noindex, JSON-LD, headers, accessibility, and trackers with automatic repair for 17; 4 tools, Apache-2.0), CN Intel Board (China hard-tech supply chain intelligence - 33 information-gap signals across semiconductors, solid-state batteries, eVTOL, and innovative drugs, an H1 2026 earnings tracker, prediction track record, and edge Q&A; 6 tools, bearer auth, 401-live), Contexter (one shared project context across ChatGPT, Claude, Telegram, and any MCP client - 26 OAuth-scoped tools: 8 read, 7 save, 5 share, 6 remove; free early access), NoClick (workflow automation MCP - 47 documented tools for workflows, checkpoints, nodes, executions, credentials, and skills, plus a no-code builder that turns 150+ apps into a hosted MCP server; OAuth 2.1 PKCE), PairBook (portfolio risk and correlation engine - Euler risk contributions, diversification ratio, and issuer-sourced ETF overlap warnings across 4,700+ US stocks and ETFs; keyless free API, MIT), Otto (hosted marketing-data connector - live Meta Ads, GA4, and Search Console reads plus website ops in chat; $99/mo founding, 7-day trial, 401-live).

[YG3 MCP - Marketing Operations for Autonomous Agents](/hermes/mcp/servers/external/yg3-mcp) · 197 tools, one-POST agent provisioning, MIT.
[GrowSurf MCP - Referral and Affiliate Program Operations](/hermes/mcp/servers/external/growsurf-mcp) · campaigns, rewards, webhooks, analytics.
[site-spec MCP - Machine-Readable Website Audits and Auto-Fixes](/hermes/mcp/servers/external/site-spec) · 40 checks, 17 auto-fixable, local stdio.
[CN Intel Board MCP - China Hard-Tech Supply Chain Intelligence](/hermes/mcp/servers/external/cn-intel-board) · 6 tools, signals plus earnings tracker.
[Contexter MCP - Shared Project Context Across AI Assistants](/hermes/mcp/servers/external/contexter) · 26 tools, OAuth 2.1, free early access.
[NoClick MCP - Workflow Automation for AI Assistants](/hermes/mcp/servers/external/noclick-mcp) · 47 tools, OAuth PKCE, app-to-MCP builder.
[PairBook MCP - Portfolio Risk and Correlation Analysis](/hermes/mcp/servers/external/pairbook-mcp) · keyless, 11.3M pairs, daily refresh.
[Otto MCP - Live Marketing Data and Website Operations in Chat](/hermes/mcp/servers/external/otto-mcp) · Meta, GA4, GSC, $99/mo founding.

**Also identified (not catalogued):** dataloupe #3813 (offline stdio explorer for local CSV/Parquet/Excel - local data-file utility class, redundant with existing local tooling), thing #3815 (durable artifact publishing for coding agents - dev publishing utility class, Booklet precedent: versioned links and comments but no measurable readership). /all catch-up skips: YardStock (named NZ dealer used-car inventory - micro geo-niche consumer data), SafeSelect (read-only Postgres/MongoDB access for coding agents - dev tool class), Domain Search King (.com availability via RDAP - thin single-purpose utility), TooHardBasket (escrow agent task marketplace - TaskMarket class), Blck Alpaca Knowledge Base (vendor marketing knowledge base - prose content, not data), Savee (design bookmarking - consumer creative utility), PersonaCLI (local personal notes workspace - consumer productivity), MCP Marketplace (880-server search directory - agent infra), search2chart (charting utility - dev class), Lyrenth (web extraction - saturated scraping class), AgentMailkit (local email digests - personal utility), Session Bridge (browser automation - dev automation class), Maroo and Kalyvox (no repo or description), plus consumer/crypto repeats (YNAB, Pi Delegate, Parlay, OpenEphemeris, Bilibili, Zhihu). Future catch-up candidates: the HasData batch (Airbnb, Booking, Zillow MCPs). · **Sources:** chatmcp/mcpso issues #3809-#3810 + mcp.so homepage/feed + mcpservers.org homepage · **Catalog:** 411 servers (+297 guides)

## 🆕 August 29, 2026 - Night Cron Sweep (1 New, 1 Guide)

Night sweep sourced from chatmcp/mcpso issues #3809-#3810, the mcp.so homepage new arrivals and feed, and the mcpservers.org homepage. 1 new business-relevant server catalogued with a guide: Packy Tracking MCP (official hosted MCP for the Packy parcel-tracking API - 10 tools to create and manage trackers, list and auto-detect couriers, and wire delivery-status webhooks; OAuth 2.1 with API-key fallback, credit-based pricing on tracking creation only, endpoint live-verified via 401 plus public health checks).

[Packy Tracking MCP - Parcel Tracking and Courier Webhooks](/hermes/mcp/servers/external/packy-tracking-mcp) · 10 tools, OAuth + API key, credit-priced trackings, /health + /ready.

**Also identified (not catalogued):** compteparticulier #3809 (French consumer login-guide knowledge base - consumer content class), Unofficial Apple Music for macOS #3810 (local consumer media utility), MagicPixel.art (pixel-art generator for game assets - creative utility class), PickADive MCP (recreational dive-conditions data - consumer class), XcodeBuildMCP (Sentry iOS/macOS build tooling - dev-tool class), TouchDesigner Bridge MCP (creative production software bridge - creative class).

## 🆕 August 28, 2026 - Evening Cron Sweep (6 New, 6 Guides)

Evening sweep sourced from chatmcp/mcpso issues #3802-#3807 (cutoff #3801, the Aug 27 night sweep high-water mark), the mcp.so homepage new arrivals, and the mcpservers.org homepage. 6 new business-relevant servers catalogued with guides: Askline (hosted GEO/AEO brand monitoring - 22 verified tools showing what ChatGPT says about a brand plus the SEO that feeds it: keyword and SERP research, competitor gaps, backlinks, AI citations, AI share of voice, and free Search Console reads; per-user URL token, $35/mo, endpoint live-probed), TX ESBD Procurement (Texas state procurement intelligence on the Apify MCP gateway - roughly 60,000 solicitations searchable by structured NIGP code with an agency dictionary, date windows, and an old-to-new change feed; your own Apify token, actors verified, 401 liveness confirmed), Vocaneo (official keyless French workforce-data MCP - 13 live-probed tools over jobs, RNCP/RS diplomas and certifications, 135,000 trainings, training centers, skills comparison, and career pathways; registry com.vocaneo/vocaneo v1.0.1), Safe Mind (official stdio MCP for Germany's legally required psychological risk assessment, GBU Psyche - 12 tools for accounts, departments, survey drafts, and anonymity-protected aggregated results; npm safe-mind-mcp), TikTok Transcript MCP (Apify-gateway remote that transcribes public TikTok videos with an AI speech model across 90+ languages - timings, speaker labels, SRT/VTT, confidence scores, and metadata; own Apify token, registry io.github.deapi-ai), Forency (website technology-stack detection for prospecting and competitive intelligence - CMS, ecommerce, analytics, CRM, payments, CDN, hosting; hosted endpoint plus stdio package, free 100 scans/month, 401 liveness confirmed).

[Askline MCP - AI Search Visibility for Brands](/hermes/mcp/servers/external/askline-mcp) · 22 tools, GEO/AEO monitoring, $35/mo, per-user URL token.

[TX ESBD Procurement MCP - Texas Government Contract Intelligence](/hermes/mcp/servers/external/tx-esbd-procurement-mcp) · ~60k solicitations, NIGP codes, change feed, Apify gateway.

[Vocaneo MCP - French Jobs, Diplomas, and Training Data](/hermes/mcp/servers/external/vocaneo-mcp) · 13 tools, keyless remote, official registry.

[Safe Mind MCP - Psychological Risk Assessment for German Employers](/hermes/mcp/servers/external/safe-mind-mcp) · 12 tools, GBU Psyche compliance, stdio.

[TikTok Transcript MCP - AI Transcriptions of Public TikTok Videos](/hermes/mcp/servers/external/tiktok-transcript-mcp) · 90+ languages, SRT/VTT, Apify gateway.

[Forency MCP - Website Technology Stack Detection for Agents](/hermes/mcp/servers/external/forency-mcp) · hosted + stdio, free 100 scans/mo.

**Also identified (not catalogued):** PZERO #3802 (prepaid inference MCP - resubmission of the AI model marketplace already disposed in prior sweeps, UnificAlly class), SaveState #3803 (encrypted portable agent memory - agent infrastructure class, BanditDB precedent). mcp.so homepage repeats already evaluated in prior sweeps (CrawlForge, Ransack, Foremerge, Katto, Speccy x402, Hologrow); mcpservers.org homepage slugs were famous-name re-indexes (atlassian, blender, calcom, chrome-devtools, context7, firecrawl, github, granola, minimax, playwright, proxyman, railway, supabase) plus prior-sweep dispositions (AgentCloud, Count Nanocorp, Floot, Runbear).

## 🆕 August 28, 2026 - Night Cron Sweep (1 New, 1 Guide)

Night sweep sourced from the mcp.so feed (30 submissions) and mcpservers.org /all pages 1-3 (43 slugs). 1 new business-relevant server catalogued with a guide: OmniSocials (official hosted MCP from the OmniSocials social media management platform - 42 tools matching the full public API over posts, media, analytics, hashtag sets, social inbox and webhooks across 11 platforms including Instagram, Facebook, LinkedIn profile and company page, YouTube, TikTok, X, Pinterest, Bluesky, Threads, Mastodon and Google Business; Streamable HTTP at mcp.omnisocials.com with scoped API keys or OAuth 2.1 DCR, plus a local stdio option via npx @omnisocials/mcp-server; endpoint 401-verified live - resolves the Aug 27 verification flag, MetricFire precedent).

[OmniSocials MCP - Multi-Platform Social Publishing for AI Agents](/hermes/mcp/servers/external/omnisocials-mcp) · 42 tools, 11 platforms, API key or OAuth 2.1, remote endpoint.

**Also identified (not catalogued):** YOUB (consumer endurance-training account connector - consumer fitness niche). Feed and /all pages 1-3 carried only night-sweep and prior-sweep repeats (CrawlForge, Ransack, AgendaForge, Foremerge, BidSkim, OrbitWan, Katto, Uwear.ai, Graviti, Speccy x402, Jitsu, Hologrow, OpenLore, Legion MCP, fhirHydrant, YouTube Transcript AI, QuanticData, Windframe, Alpha Sophia, HostTracker, Batru, Magic Hour, Ice Juice, Routebase, SSH MCP Server, Agentic Atlas, RE Data Refinery, SocialRobot, and the mcpservers.org dispositions incl. Helena Good and the loki-freedomlab Walletwatch slug).

## 🆕 August 27, 2026 - Night Cron Sweep (11 New, 11 Guides)

Night sweep sourced from mcpservers.org /all pages 1-3 (44 slugs, host-dump and prior-sweep slugs excluded), the mcp.so feed (33 entries), chatmcp/mcpso issues #3794-#3801, and vendor detail pages. 11 new business-relevant servers catalogued with guides: LiveDataLink (hosted public-data aggregation - 284 tools across 59 domains behind one bearer key: stocks, options, crypto, SEC EDGAR, FRED, sanctions, federal courts, CVE, weather, FMCSA, real estate and more; free key with 1,000 calls/month minted in-conversation, plans from $10/mo), SprintCheckout (official payment-platform MCP - 6 tools read payment settings and paid orders, pull receipts, create payment links and mint API keys under OAuth 2.1 PKCE with scoped, instantly revocable consent; POST-only Streamable HTTP at mcp.sprintcheckout.com/mcp), AstroFabric (agentic growth-ops OS over MCP - one mission_agent tool, or the granular catalog via ?tools=all: on-page SEO audits, AI-visibility checks, email-deliverability audits, Google Search Console data, LinkedIn and Google Ads research, HubSpot CRM writes; OAuth with DCR+PKCE or key-embedded URL at www.astrofabric.ai/api/mcp - upgraded from the Aug 26 thin-docs skip now that the endpoint is verified, MetricFire precedent), Foliora (managed AI-search GEO/AEO platform - read-only 3-tool MCP hands agents product facts and preview links while humans run the snapshots; no key at v0, registry ai.foliora/search), QoreNext CRM (5 tools submit companies for address verification, top-parent hierarchy mapping and duplicate detection from JSON/CSV/Excel, then poll async results; X-API-Key at mcp.qorenext.com/crm, MIT), QoreNext Trade Screening (4 tools screen entities against OFAC/MEU/Entity List sanctions and run full trade due diligence with red-flag and negative-news analysis plus async report polling; X-API-Key at mcp.qorenext.com/tradescreening, MIT - vendor notes an intermittent 422 on new submissions as of Aug 19), AgendaForge (official AI-native event platform MCP - 53 tools over events, sessions, speakers, agendas, CFP forms, submissions, sponsors, ticketed attendees and email sends with every write proposed for in-app human approval; OAuth 2.1 at mcp.agendaforge.app/mcp), Jawz (22 read-only macro-economics tools - regime classification, financial conditions, G4 central-bank balance sheets, growth and inflation indicators, event calendar, ETF look-through, plus a four-chapter investing decision framework; anonymous reads at jawz.ai/api/mcp, OAuth for identity only), Flyn (8 short-link tools with click analytics and QR generation, OAuth on the free plan), Ransack (hosted search and research with source-attributed answers - 6 tools including multi-step cited reports and semantic memory over fetched pages; Bearer key at ransack.tools/mcp, trial free), Intesta (keyless registry of attested business fact passports with an A0-A4 trust ladder - 5 tools search entities, read passports and answer only from attested facts).

[LiveDataLink MCP - Live Public Data for AI Agents](/hermes/mcp/servers/external/livedatalink-mcp) · 284 tools, 59 domains, one bearer key, free tier.

[SprintCheckout MCP - Payment Links and Orders for Coding Agents](/hermes/mcp/servers/external/sprintcheckout-mcp) · 6 tools, OAuth 2.1 PKCE, scoped revocable consent.

[AstroFabric MCP - Agentic Growth Missions for Operators](/hermes/mcp/servers/external/astrofabric-mcp) · mission_agent tool, SEO/AI-visibility/email audits, HubSpot writes.

[Foliora MCP - Managed AI Search Preview for Agents](/hermes/mcp/servers/external/foliora-mcp) · 3 read-only tools, no key, GEO/AEO snapshots.

[QoreNext CRM MCP - Company Hierarchy and Address Verification](/hermes/mcp/servers/external/qorenext-crm-mcp) · 5 tools, async submit/poll, JSON/CSV/Excel dedupe.

[QoreNext Trade Screening MCP - Sanctions and Restricted-Party Checks](/hermes/mcp/servers/external/qorenext-tradescreening-mcp) · 4 tools, OFAC/MEU/Entity List plus trade due diligence.

[AgendaForge MCP - Event Operations for AI Agents](/hermes/mcp/servers/external/agendaforge-mcp) · 53 tools, human-approved writes, OAuth 2.1.

[Jawz MCP - Live Macro Reads and a Disciplined Investing Loop](/hermes/mcp/servers/external/jawz-mcp) · 22 read-only tools, anonymous reads.

[Flyn MCP - Short Links, Click Analytics and QR Codes](/hermes/mcp/servers/external/flyn-mcp) · 8 tools, OAuth on the free plan.

[Ransack MCP - Source-Attributed Search and Research for Agents](/hermes/mcp/servers/external/ransack-mcp) · 6 tools, cited reports, semantic memory.

[Intesta MCP - Attested Business Fact Passports](/hermes/mcp/servers/external/intesta-mcp) · 5 tools, A0-A4 trust ladder, keyless.

**Also identified (not catalogued):** Kairos Signal #3799 (DePIN telemetry across 457 networks with per-query pricing - crypto/niche class), Crawlforge (28-tool scraping and deep-research server - saturated web-scraping class, rasterly/Parse.bot/MaxCrawl precedent), AlphaBridge (126-tool WordPress server with FTP/SFTP deploy - dev tool class, mcpservers.org detail page 504'd), Mini Course Generator (course-authoring MCP with no published endpoint or tool list - thin MCP docs). mcpservers.org /all dispositions: FarmDash (DeFi intelligence), Sceneplane (cloud Blender 3D), KinoPipe (FFmpeg-as-a-service media utility), AlgoVesta (16-exchange crypto trading), BanditDB (agent decision memory - agent infra), ElloMind (therapy booking - consumer niche), PZERO (AI model marketplace), Walletwatch (Solana wallet lookup - crypto consumer), KnowMapped (visual knowledge maps), ReverseGPT (AI humanizer utility), Deep Art AI (image/video generation), MCPPlatform (REST-to-MCP gateway - agent infra), Soccer API (sports niche), SpecMCP (German TI healthcare specs - geo-niche), Autonomy x402 Tools (x402 pay-per-call - payment plumbing). Host-dump slugs (railway-app/cloud-run/x402-feed patterns) and prior-sweep skips (Marketingburos, BillTruth, SocialData, Synapse, Wagglet, Screenies, CoAnimator, Speko, ScreenMocks) excluded without refetch; More Good Reviews confirmed already catalogued Aug 25.

## 🆕 August 27, 2026 - Evening Cron Sweep (3 New, 3 Guides)

Evening sweep sourced from chatmcp/mcpso issues #3792-#3793 (Aug 27 13:02 - 15:47 UTC), the mcp.so homepage and feed (30 feed slugs and 8 recentServers cross-referenced), and the mcpservers.org homepage (18 slugs cross-referenced). 3 new business-relevant servers catalogued with guides: TubeScout (local keyless YouTube research server - filtered video search, engagement resonance, resilient transcripts single or batch of 10, channel scans and YouTube autocomplete as search-demand data, plus 6 context-aware research skills for idea mining, niche validation and demand-gap analysis; stdio via npx -y tubescout, MIT), DrillerDB (official remote MCP connector for the water-well and drilling contractor operating system - 45 tools, 37 read-only, over projects, customers, invoices, work orders, crews, schedules, equipment, compliance and well logs; OAuth 2.0 PKCE with tenant isolation, audit logging and approval-gated writes; endpoint 401-verified live, registry com.drillerdb/drillerdb v1.0.0), BidSkim (hosted UK public procurement intelligence - 8 read-only tools over Find a Tender, Contracts Finder, Public Contracts Scotland and Sell2Wales, entity-resolved to one record per opportunity; search_renewals surfaces expiring contracts with incumbents, buyer and supplier profiles carry award histories; OAuth 2.1 or x-api-key header at mcp.bidskim.com/mcp, 401-verified live).

[TubeScout MCP - Keyless YouTube Research for AI Agents](/hermes/mcp/servers/external/tubescout-mcp) · 6 keyless tools plus a research skill pack, npx install, MIT.

[DrillerDB MCP - Field Service Data for Drilling Contractors](/hermes/mcp/servers/external/drillerdb-mcp) · 45 tools, 37 read-only, OAuth PKCE, approval-gated writes.

[BidSkim MCP - UK Tenders and Procurement Intelligence](/hermes/mcp/servers/external/bidskim-mcp) · 8 read-only tools, contract renewals with incumbents, OAuth or API key.

**Also identified (not catalogued):** Foremerge (open-source coordination protocol for coding agents built above Git - Rust CLI plus MCP, 50 stars - dev tool class, kbdb and AI Commander precedent), OrbitWan (Wanchain blockchain explorer: address, transaction, block and validator search - crypto/niche class, no MCP surface on the site), plus feed and homepage repeats already evaluated in Aug 24-27 sweeps (Katto, Uwear.ai, OmniSocials, Graviti, Speccy x402, Jitsu, Hologrow, OpenLore, Legion, fhirHydrant, YouTube Transcript AI, QuanticData, Windframe, Alpha Sophia, HostTracker, Batru, Magic Hour, Ice Juice, Routebase, SSH MCP Server, Agentic Atlas, RE Data Refinery, AgentRisk M2M, OAIA Arena, ReactVision, uxgen, SocialRobot, and the mcpservers.org homepage's 18 already-mapped slugs).

## 🆕 August 27, 2026 - Morning Cron Sweep (1 New, 1 Guide)

Morning sweep sourced from chatmcp/mcpso issues #3787-#3791 (Aug 27 03:52 - 08:31 UTC), the mcp.so homepage and feed (30 feed slugs and 8 recentServers cross-referenced), and the mcpservers.org homepage (18 slugs cross-referenced). 1 new business-relevant server catalogued with a guide: Golf Intelligence by Stracka (proprietary golf course dataset - 20 years of course-by-course mapping with laser, drone, airplane and satellite capture, updated daily since 2007; free course-group search, then credit-metered scorecards, GPS geometry, course details and green slope images; client-credentials headers at mcp.golfintelligence.com/mcp, live-probed serverInfo golf v1.0.0 with all 5 read-only tools confirmed; Personal $49 / Starter $399/mo plans).

[Golf Intelligence MCP - Golf Course Data for AI Agents](/hermes/mcp/servers/external/golf-intelligence-mcp) · 5 read-only tools live-probed, free search, credit-metered lookups with confirm_spend gate.

**Also identified (not catalogued):** SwarmIO #3788 (hosted research swarm writing cited reports - agent infra class, no business data), Vifo #3789 (AI travel journal written by the user's agent - consumer app class), Oblique Markets #3790 (x402-paid tool marketplace: market stats, provider lookup, catalog diffs, experiment scoreboard - x402 infrastructure class, 402oracle precedent), Focuh #3791 (personal ADHD task system for coding agents - personal productivity class). Feed/homepage catch-ups recorded for a future sweep: Katto (AI video clipping into scored, captioned 9:16 shorts, mcp.so recentServers, createdAt Dec 2024 - creator/media utility class, klo-mcp precedent), Graviti (agent trust index with paid verification and a tamper-evident public ledger at graviti.thesingulariti.ai - agent infra class), YouTube Transcript AI (keyless YouTube transcript fetching, createdAt Jul 31 - dev utility class).

## 🆕 August 26, 2026 - Night Cron Sweep (4 New, 4 Guides)

Night sweep sourced from chatmcp/mcpso issues #3780-#3786 (Aug 26 20:53 - Aug 27 01:48 UTC), the mcp.so homepage and feed, and the mcpservers.org homepage (18 slugs cross-referenced). 4 new business-relevant servers catalogued with guides: Centipid ISP Billing (hosted billing and network-management data for ISPs and WISPs - revenue and payment reports, subscriber status and expirations, MikroTik sessions and diagnostics, voucher stock, M-Pesa payments; 23 tools, 20 read-only, the 3 network-changing actions file in-app approval requests and return pending_confirmation; per-workspace API key at mcp.centipidbilling.com/mcp, 401-verified live, registry com.centipidbilling/billing), Security Recipes (keyless read-only CVE intelligence, remediation playbooks and agentic security governance packs - 75 tools live-probed at security-recipes.ai/mcp, serverInfo security-recipes-mcp v3.4.7; CVE catalog scoped to Medium/High/Critical with evidence and bounded change plans; Apache-2.0), Legalize MCP (consolidated legislation as data with point-in-time law_at_date and git-SHA citations - 7 read-only tools confirmed via the public tools.json, OAuth 2.1 with dynamic client registration at legalize.dev/mcp, 401-verified live, MIT), BestPrice Shopping (keyless Greek-market product search, delivered-total offer comparison and 30/90/180-day price history - 3 tools live-probed at mcp.bestprice.gr, serverInfo bestprice-agent-commerce v1.5.1, fail-closed category bounds).

[Centipid ISP Billing MCP - Subscriber and Network Operations Data](/hermes/mcp/servers/external/centipid-billing-mcp) · 23 tools, 20 read-only, MikroTik diagnostics with in-app approval for changes.

[Security Recipes MCP - CVE Intelligence and Remediation Playbooks](/hermes/mcp/servers/external/security-recipes-mcp) · 75 tools live-probed, keyless, Apache-2.0.

[Legalize MCP - Point-in-Time Legislation with Git Provenance](/hermes/mcp/servers/external/legalize-mcp) · 7 tools, OAuth 2.1, law_at_date with git SHA citations.

[BestPrice Shopping MCP - Greek Market Price Comparison](/hermes/mcp/servers/external/bestprice-shopping-mcp) · 3 tools live-probed, keyless, delivered-total comparison.

**Also identified (not catalogued):** Axiom by Elevated AI #3786 (x402 routing and non-custodial crypto swaps - payment plumbing class, Kura and 402oracle precedent), ox402-utils #3784 (88 paid tools via x402 on a trycloudflare endpoint - x402 utility infra class), ArcadeOps Public Discovery #3782 (read-only discovery surface for a governed agent mission-control product - agent infra class, no business data). Feed catch-ups recorded for a future sweep: OmniSocials (official social publishing and analytics MCP across 11 platforms, mcp.so feed, createdAt Jul 9 - social management class, needs repo and endpoint verification), Uwear.ai (AI fashion photoshoots from flat-lay product images, createdAt Jul 25 - creative utility class, 3dlogo-adjacent), FastGPU (live GPU price comparison across 28+ providers on mcpservers.org - endpoint not verifiable from public pages, MetricFire thin-docs precedent). mcpservers.org homepage slugs mapped to established skip classes: AgentCloud (hosted iOS simulator - dev tool), Count Nanocorp (shared-expense ledger - consumer finance), ProxyLoom (multi-tenant MCP gateway - agent infra), Runbear (AI agent deployment to Slack - agent infra). Feed and homepage repeats already evaluated in Aug 24-26 sweeps (Speccy x402, Jitsu, Hologrow, OpenLore, LM Legion, fhirHydrant, QuanticData, Windframe, Alpha Sophia, HostTracker, Routebase, Agentic Atlas, RE Data Refinery, AgentRisk M2M, OAIA Arena, ReactVision, uxgen, BitBrowser, Shotstack, Agency AI, SSH MCP Server, SecondSim, Batru, Ice Juice, Granola, Minimax, Proxyman).

## 🆕 August 26, 2026 - Midday Cron Sweep (6 New, 6 Guides)

Midday sweep sourced from chatmcp/mcpso issues #3758-#3778 (Aug 26 03:35 - 17:59 UTC) and mcpservers.org /all pages 1-3 (all new slugs mapped to established skip classes). 6 new business-relevant servers catalogued with guides: Nomos MCP (11 read-only search tools over Brazilian legislative and regulatory data - bills, the federal official gazette, state and municipal gazettes, speeches, legislator social media, Central Bank, CVM, Receita Federal, sector regulators and UN sanctions; X-API-Key or OAuth 2.0 at mcp.nomos.pro/mcp, 401-verified live), Korea Ground-Truth (8 tools unifying five Korean government sources - NTS business registration, DART corporate profiles, MOLIT apartment prices, road-name addresses and statute search; free 50-credit key, hosted at kr-groundtruth-mcp.vercel.app, stateless INIT 200 verified), ScreenVerity (free U.S. exclusion, debarment and licence screening with Ed25519-signed receipts naming the exact list snapshots checked - 3 tools, stdio via npx, no key or account, MIT), w0 MCP Server (GEO/AEO measurement - a brand's AI Recommendation Rate and Recommendation Inclusion Rate over buyer-intent questions - 1 tool, keyless hosted at w0-mcp-server.modernai.workers.dev, endpoint live behind the Workers access layer), UGC VZ (free directory of real UGC creators in DACH - profile search with city, topic and verification filters, pricing and reach comparison, gated outreach requests with status lifecycle; 5 tools, no auth, stateless INIT 200 verified), iFillPDF (hosted AI PDF form detection and filling - scanned and photographed form field maps, signature image fields, page operations; OAuth protected resource at mcp.ifillpdf.com, 401-verified live, free tier without account).

[Nomos MCP - Brazilian Regulatory and Legislative Search](/hermes/mcp/servers/external/nomos-mcp) · 11 read-only tools, API key or OAuth, every result links official source context.

[Korea Ground-Truth MCP - Official Korean Data for Agents](/hermes/mcp/servers/external/korea-groundtruth-mcp) · 8 tools over NTS/DART/MOLIT/law sources, free 50-credit key, agent-native billing.

[ScreenVerity MCP - U.S. Exclusion and Debarment Screening](/hermes/mcp/servers/external/screenverity-mcp) · 3 free tools, signed audit receipts, explicit coverage reporting.

[w0 MCP Server - Brand AI Recommendation Rate Lookup](/hermes/mcp/servers/external/w0-mcp) · 1 tool, keyless, AEO/GEO measurement with honest not-measured responses.

[UGC VZ MCP - DACH UGC Creator Discovery for Agents](/hermes/mcp/servers/external/ugc-vz-mcp) · 5 tools, no auth, outreach gated on explicit brand request.

[iFillPDF MCP - AI PDF Form Detection and Filling](/hermes/mcp/servers/external/ifillpdf-mcp) · Hosted Streamable HTTP, OAuth, registry-published since 2026-07-27.

**Also identified (not catalogued):** SocialDataX family #3770-#3775 (six hosted read-only social-data wrappers - TikTok, X, Instagram, Zhihu, Bilibili, YouTube - filed within 3 minutes by one vendor, commercial X-data reseller class, same class as the SocialData and TwitterAPIs skips), Apple Mail MCP #3777 (local macOS stdio over Mail's SQLite index - consumer utility class), AI Commander #3765 (remote shell, detached jobs and file transfer for agents - dev infra, SSH MCP Server class), Helena Good #3764 (scientific infrastructure sponsorship paid in Solana USDC - crypto/niche class), kbdb #3762 (local file-based knowledge base, 30 tools, stdio - dev tool class), Pīpīwai Trail #3761 (park and road status - consumer niche), Vedaksha #3760 (Vedic astrology - consumer class), BuyWhere #3767 (resubmission of the already-catalogued entry). mcpservers.org /all pages 1-3 dispositions: the x402-payable family (Live Entity Verification, Public Tenders ES EU, Document Conversion API, Calibrated Similarity Search API, WebSocket Session Manager, Agent Verification API, ERC8004 Agent Liveness, New x402 Listings Feed, Onchain Activity Index, URL Metadata API, x402 Receipt Verifier - crypto/payments class per RE Data Refinery and Speccy x402 precedent), SoccerAPI (consumer sports data), Walletwatch via the loki-freedomlab slug (Solana wallet lookup - already evaluated in the Aug 25 night sweep), MCP Platform (REST-to-MCP gateway with policy controls - agent infra class, XGuard precedent), Deep Art AI (consumer image generation - Magichour class). Feed page 1 carried only morning-sweep repeats.

## 🆕 August 26, 2026 - Morning Cron Sweep (3 New, 3 Guides)

Morning sweep sourced from the mcp.so feed (newest 30 submissions) and mcpservers.org /all pages 1-3. 3 new business-relevant servers catalogued with guides: SocialRobot (remote social media scheduling and analytics across Instagram, LinkedIn, X, TikTok, Facebook, Threads, Pinterest, Bluesky and Mastodon - 18 documented tools covering create/list/reschedule/delete posts, presigned media uploads, account and post analytics, follower demographics, best-time-to-post, TikTok creator info and LinkedIn Company Page targeting; Streamable HTTP at socialrobot.io/api/mcp, OAuth 2.0 PKCE or API key, free on every plan), Hologrow (read-only e-commerce data layer for AI - platform OAuth, sync, freshness and schema handled upstream so agents only read, five discovery tools plus installable analysis skills; remote at mcp.hologrow.ai/mcp), MetricFire (official Hosted Graphite monitoring MCP - metric pattern and tagged search, Graphite render as JSON/CSV/raw/PNG/SVG, alert CRUD with AND/OR criteria, notification channels and scheduled mutes; endpoint mcp.hostedgraphite.com with X-HostedGraphite-MCP-Token auth - resolves the Aug 23 thin-docs skip, endpoint now verified from the mcpservers.org detail page).

[SocialRobot MCP - Social Media Scheduling and Analytics for AI Agents](/hermes/mcp/servers/external/socialrobot-mcp) · 18 tools, OAuth PKCE or API key, 9 platforms, free tier.

[Hologrow MCP - E-Commerce Data Layer for AI Agents](/hermes/mcp/servers/external/hologrow-mcp) · Read-only, hosted OAuth/sync/schema, remote endpoint.

[MetricFire MCP - Natural Language Infrastructure Monitoring](/hermes/mcp/servers/external/metricfire-mcp) · Official, token auth, metrics/render/alerts/channels/mutes.

**Also identified (not catalogued):** SocialData (Twitter/X data reseller, 14 read-only tools billed per result - commercial X-data wrapper class, same class as the TwitterAPIs skip from Aug 25), OpenLore (serve docs to agents as a virtual filesystem over SSH/MCP - local dev tool class), fhirHydrant (self-hosted Node.js FHIR server with SMART Backend Services - healthcare dev infra, no hosted service), Legion MCP (multi-model LLM deliberation councils - agent infra class), Speccy x402 MCP (pay-per-call x402 wrapping of Polymarket/Python/FFMPEG - crypto/payments class), RE Data Refinery (x402 real-estate pay-per-query - crypto/payments class), YouTube Transcript AI (hosted transcript utility - BulkTranscripts precedent), BillTruth (Texas electricity plan cost data from state-filed EFLs - regional niche data), Marketingburos (Dutch marketing-agency directory with RFQs - regional niche), WorkerKit (AI worker kits marketplace - agent infra class), CoAnimator (agentic animation studio - media production class), Screenies (App Store screenshot-set generator - dev/marketing asset), Synapse by Myelix Labs (agent knowledge/token efficiency - agent infra class), Wagglet (AI coding-task handoff - agent infra class), Speko (voice agents, TTS/STT and call transcripts - telephony utility), ScreenMocks (design mockup generator - dev tool), MetricFire was previously skipped Aug 23 (endpoint unverifiable) - now catalogued above with the endpoint verified. Feed repeats already evaluated in Aug 24-25 sweeps (QuanticData, Windframe, AgentRisk M2M, OAIA Arena, uxgen, ReactVision, Batru, SecondSim, Routebase, Magichour, Mangii, SSH MCP Server, Agentic Atlas, Jitsu, Ship24, Alpha Sophia, HostTracker, Ice Juice, Shotstack, Agency AI, TEOS, SenderKit, GovGazette, Partsgraph, More Good Reviews, TwitterAPIs, Lacuna, ORANO, Xi Pe).

## 🆕 August 25, 2026 - Night Cron Sweep (3 New, 3 Guides)

Night sweep sourced from chatmcp/mcpso issues #3750-#3757 (Aug 25 18:03 - Aug 26 01:34 UTC), the mcp.so homepage and feed, and mcpservers.org /all pages 1-3 plus the homepage. 3 new business-relevant servers catalogued with guides: Transcodely (hosted agent-native video infrastructure - transcode gs://, s3:// or https:// sources into renditions, host with an adaptive ladder and CDN player link, AI WebVTT captions and EUR usage reads; 7 tools, OAuth 2.1 PKCE or app-scoped key, 401-verified live), Rapidly (idea validation with Lean Canvas, riskiest-assumption hypothesis with researched pass mark, and Pretotyping experiment build prompts - 21 tools, bearer token or OAuth, registry co.rapidly/rapidly), PopOff Data (reality-TV social analytics - Instagram/TikTok follower time series at ~30-minute resolution, follow graphs, engagement and citation-ready season CSVs; 12 tools, API-key, $79/mo with 5,000 calls).

[Transcodely MCP - Video Transcoding and Hosting for AI Agents](/hermes/mcp/servers/external/transcodely-mcp) · 7 tools, OAuth or app key, billable creates scoped per app.

[Rapidly MCP - Idea Validation, Lean Canvas and Pretotyping](/hermes/mcp/servers/external/rapidly-mcp) · 21 tools, bearer token or OAuth, free trial with 5 ideas.

[PopOff Data MCP - Reality-TV Social Analytics for AI Agents](/hermes/mcp/servers/external/popoff-data) · 12 tools, API key, $79/mo flat with 5,000 calls.

**Also identified (not catalogued):** AgentSeed #3750 (AST-level code verification and anti-hallucination guardrails for coding agents - dev tool class), Spoolis #3752 (outcome verification for result-shaped agent purchases - commerce infra, no business data carried), SSSNACK #3755 (agent self-registration design network - agent community infra class), 1Claw #3757 (HSM-backed agent secrets vault and signing - agent security infra class). Homepage and /all slug dispositions: BoardRepo (KiCad/Altium PCB search - niche hardware dev data), PZERO (AI model marketplace aggregator - UnificAlly class), Walletwatch (Solana wallet lookup - crypto consumer class), AstroFabric (agentic OS for deploying growth/revenue agents - agent orchestration infra, ADA Turbo class), WaveMaster (surf forecasting - niche consumer data), Hird (Hird language compiler introspection - dev tool class). Already evaluated in prior sweeps: CorpusLaw, Real Wave GHL, BulkTranscripts, xRocket (myrocket slug), Normi DVF (all catalogued), Appraisily (skip). Famous-name mcpservers.org homepage slugs are re-indexes.

## 🆕 August 25, 2026 - Evening Cron Sweep (9 New, 9 Guides)

Evening sweep sourced from chatmcp/mcpso issues #3746-#3749 (Aug 25 10:47 - 16:48 UTC), the mcp.so homepage and feed, and mcpservers.org /all pages 1-3. 9 new business-relevant servers catalogued with guides: Alpha Sophia (official MCP from the US healthcare provider and organization database - resolve_entity plus search, count and market_size tools over procedures, diagnoses, affiliations, publications and clinical trials; OAuth remote at api.alphasophia.com/v1/mcp), BeeL (Spanish VeriFactu e-invoicing with AEAT - about 120 OpenAPI-derived tools for invoices, correctives, NIF validation, series and fiscal guardrails; OAuth remote plus stdio), CivicDataForge (government-records evidence relay - 14 live-probed tools covering STR permits across 31 sources, LEIE exclusion screening, property violations, restaurant inspections, childcare licensing, EPA ECHO and Norwegian company evidence; Apify-token auth), Partsgraph (keyless parts catalog with datasheet provenance, compatibility checks and priced BOM building - 11 tools live-probed on the demo catalogue), Nacha MCP (stdio ACH file parser with structural and arithmetic validation and IAT support - 2 tools), 1Lookup (phone, email and IP verification with DNC status, deliverability and proxy detection - OAuth 2.1 remote, 401-verified live, credit-based), HostTracker (official uptime-monitoring MCP from the 2004-vintage monitoring network - 65 tools, synchronous checks from 300+ locations, Bearer token), SenderKit (transactional messaging over MCP - 18 tools for templates, sends, delivery inspection and inbound management), More Good Reviews (project-scoped review management - customers, review requests, Google and Facebook reply publishing with a confirm gate, agency variant for white-label).

[Alpha Sophia MCP - US Healthcare Provider and Market Data](/hermes/mcp/servers/external/alpha-sophia-mcp) · Official, OAuth-gated, provider/org/clinical-trial search and market sizing.

[BeeL MCP - Spanish VeriFactu E-Invoicing Compliance](/hermes/mcp/servers/external/beel-mcp) · ~120 OpenAPI-derived tools, OAuth remote plus stdio, MIT repo.

[CivicDataForge MCP - Government Records Evidence Platform](/hermes/mcp/servers/external/civicdataforge-mcp) · 14 live-probed tools, Apify-token auth, STR/LEIE/EPA records.

[Partsgraph MCP - Electronic Parts Search and BOM Building](/hermes/mcp/servers/external/partsgraph-mcp) · Keyless demo catalogue, 11 tools probed, compatibility checks.

[Nacha MCP - ACH File Parsing and Validation](/hermes/mcp/servers/external/nacha-mcp) · stdio, structural and arithmetic validation, IAT support.

[1Lookup MCP - Phone, Email and IP Verification](/hermes/mcp/servers/external/1lookup-mcp) · OAuth 2.1 remote, DNC/deliverability/proxy checks, 401-verified live.

[HostTracker MCP - Uptime Monitoring from 300+ Locations](/hermes/mcp/servers/external/hosttracker-mcp) · Official, 65 tools, Bearer token, operating since 2004.

[SenderKit MCP - Transactional Messaging from Your Assistant](/hermes/mcp/servers/external/senderkit-mcp) · 18 tools, hosted plus stdio, structured outputSchema results.

[More Good Reviews MCP - Review Management and Reputation Ops](/hermes/mcp/servers/external/more-good-reviews-mcp) · Project-scoped sign-in, Google/Facebook replies with confirm gate.

**Also identified (not catalogued):** ParlayAPI #3749 (sports-odds and should-I-bet layer - consumer gambling class), BlinkCodes #3746 (x402 gift-card and eSIM store - purchase plumbing, not business data), dsh-verify #3748 (browser acceptance testing - dev tool, resubmission of the Aug 18 skip), QuanticData (generic web-access utility - catch-up), AgentRisk M2M (x402 DeFi pre-trade risk - agent infra class), Windframe (AI UI design tool - dev/design class), OAIA Arena (trading-agent scoreboard - agent infra class), Context.dev (web scraping infra for AI products - dev utility class), AgentsGetPaid (x402 payment kit - payagents class, already noted), Lacuna Music (AI song generator - consumer media), ORANO (personal workspace and memory - agent infra), PublicSignalData (Polymarket and whale-trade signals - crypto signals class), TwitterAPIs (commercial X API wrapper - thin wrapper over the official API), Xi Pe (pastebin - consumer utility), VehicleFeeCalc (AI-skills listing, not an MCP server - skills-catalog class), PennyOCR (paid OCR dev utility), XGuard (MCP discovery gateway - agent infra), amem (local agent memory - agent infra), ADSBiq (community aircraft lookup - niche aviation data), secret_mcp (design analysis - dev tool), DotLy ID (domain and biolink registrar - consumer utility), Fresh Jots (thin-docs notes app), EasyGroupFlights (group airfare booking - travel booking class), ADA Turbo (agency OS visualizer - agent infra), Roast My Design System (design audit - dev tool). Also the dockndevai infra family on /all pages 1-3 (already noted Aug 24) and repeats of prior skips (Magichour, Frantic, CLSTR, Agent Conductor, payagents).

## 🆕 August 25, 2026 - Morning Cron Sweep (8 New, 8 Guides)

Morning sweep sourced from chatmcp/mcpso issues #3735-#3745 (Aug 24 19:19 - Aug 25 09:37 UTC), the mcp.so homepage and feed, and the mcpservers.org homepage. 8 new business-relevant servers catalogued with guides: Korea Business Verify (keyless hosted KYB checks against the Korean National Tax Service - 2 live-probed tools, free pilot), Jitsu (official MCP from the open-source Segment alternative, 5,043 stars - agents manage CDP destinations, streams, functions and query live events over OAuth 2.1 at use.jitsu.com/mcp), RentSeek Evidence (no-auth latest-FY executive compensation with filing source links - get_executive_compensation and list_available_tickers probed), Harness Atlas (keyless wire-harness manufacturer directory and XrefBase part cross-reference - find_manufacturer and find_alternative probed), xRocket Exchange MCP (hosted spot market data with 10 probed tools plus stdio trading bounded by an operator-set daily limit), Ship24 Tracking (official hosted MCP across 2,500+ carriers - 11 documented tools at api.ship24.com/mcp with API-key auth), GovGazette (39 live-probed federal procurement tools - SAM.gov opportunities, awards, vendors, exclusions, recompetes; 19 public, 20 OAuth-gated), Worklittle Jobs (4-million-listing job search with visa, distance and salary filters plus market overview statistics - 21 live-probed tools).

[Korea Business Verify MCP - Live KYB Checks for Korean Companies](/hermes/mcp/servers/external/korea-business-verify) · Keyless, 2 tools probed, NTS live data, free pilot.

[Jitsu MCP - Manage Customer Data Pipelines from AI Agents](/hermes/mcp/servers/external/jitsu) · Official, 5,043-star CDP, OAuth 2.1, 9 documented tools.

[RentSeek Evidence MCP - Executive Compensation with Source Links](/hermes/mcp/servers/external/rentseek-evidence) · No-auth public endpoint, 2 tools probed.

[Harness Atlas MCP - Wire-Harness Sourcing and Part Cross-Reference](/hermes/mcp/servers/external/harness-atlas) · Keyless, XrefBase equivalence groups, registry-listed.

[xRocket Exchange MCP - Spot Market Data and Trading for Agents](/hermes/mcp/servers/external/xrocket-mcp) · 10 market tools probed, daily-limit stdio trading.

[Ship24 Tracking MCP - Package Tracking Across 2,500+ Carriers](/hermes/mcp/servers/external/ship24-tracking) · Official hosted, 11 tools, API-key auth.

[GovGazette MCP - Federal Contract and Award Intelligence](/hermes/mcp/servers/external/govgazette-mcp) · 39 tools probed, 19 public, OAuth watches.

[Worklittle Jobs MCP - Job Search and Market Data for AI Agents](/hermes/mcp/servers/external/worklittle-jobs) · 21 tools probed, 4M+ listings.

**Also identified (not catalogued):** Vauban Pay MCP (x402 payment tools for MCP clients - payment plumbing class), SeenRelay (cooperative freshness infrastructure for AI agents - agent infra class), 123skills (skill market run by AI agents - agent community infra class), geo-tool-check (local CLI scoring page readability for AI search - dev utility class), loot-agent-mcp (on-chain game tools on Robinhood Chain - consumer game class), Batru (Dota 2 / Deadlock / Marvel Rivals win-rate prediction - consumer gaming class), WorkerKit Directory (AI worker kit marketplace - agent infra class), Proxyman MCP (network debugging tool - dev tool class). Feed and homepage repeats already evaluated in Aug 23-24 sweeps (Ice Juice Trading, Agentic Atlas, RE Data Refinery, Truth Bear GAUGE, BitBrowser, Mangii, Hypnothera, Shotstack, Agency AI, SSH MCP Server, AdminLanding, Granola, and the famous-name mcpservers.org homepage slugs).

## 🆕 August 24, 2026 - Evening Cron Sweep (2 New, 2 Guides)

Evening sweep sourced from the mcp.so feed (newest 30 submissions) and mcpservers.org /all pages 1-3 (all 38 slugs cross-referenced; zero new beyond prior evaluations). 2 new business-relevant servers catalogued with guides: Ice Juice Trading (hosted rules-based strategy automation on your own Alpaca brokerage - build, backtest, deploy, pause and tune risk knobs over OAuth 2.1 or API key at mcp.icejuicetrading.com/mcp; live endpoint confirmed via HTTP 401 auth gate; broker connect, billing and the emergency flatten stay human-only; paper trading free on every plan, live trading paid), Agentic Atlas (stateless read-only consultation surface for field-tested agent-system design patterns - 8 live-probed tools, no auth at agentic-atlas.dev/mcp, revision-coherence markers refuse stale reads after a corpus promotion).

[Ice Juice Trading MCP - Automated Trading on Your Alpaca Account](/hermes/mcp/servers/external/ice-juice-trading) · 401-verified auth gate, human-only rails, free paper tier.

[Agentic Atlas MCP - Field-Tested Agent-System Design Patterns](/hermes/mcp/servers/external/agentic-atlas) · 5 tools live-probed, keyless, stateless (Release v1.0.6, refreshed Sep 8 2026).

**Also identified (not catalogued):** uxgen (e-commerce conversion component library for coding agents - vendor states tool execution is not switched on yet and every call returns an explicit refusal; $29/mo, no trial - dev-asset class), OAIA Arena (AI trading-agent track-record scoring against 2,048 coin-flipping monkeys - no published tool list, crypto/verification class), ReactVision MCP (44-tool ViroReact XR renderer for coding agents - dev tool class). Feed repeats already evaluated in Aug 21-24 sweeps (RE Data Refinery, Truth Bear GAUGE, Agent Conductor, CodeSentinel, BitBrowser, Mangii, Hypnothera, Shotstack, Agency AI, TEOS WARN Act, Routebase, SecondSim, Context.dev, Dados B3, AskRentAI, Signal Nodus, lucid.page, Hermoso, QR Planet, HTML/CSS to Image).

## 🆕 August 24, 2026 - Midday Cron Sweep (4 New, 4 Guides)

Midday sweep sourced from chatmcp/mcpso issues #3726-#3734 (Aug 24 10:50-17:48 UTC), the mcp.so homepage and feed, and mcpservers.org /all page 1. 4 new business-relevant servers catalogued with guides: Salesbot (hosted LinkedIn and Sales Navigator MCP with 48 safety-gated tools - lead discovery, human-approved outreach, inbox workflows, campaigns, and a built-in CRM; anonymous tools/list verified all 48 tool names at app.salesbot.cz/api/mcp with x-mcp-api-key auth), Social Glass (evidence-backed cultural intelligence for brand and research teams - search Insights, Posts, Creators, and Audiences in permitted organizations over OAuth at mcp.socialglass.ai/mcp), SudnoKontrol MCP (keyless read-only search over the Ukrainian national vessel registries - search by registration number, name, or owner plus aggregate statistics; 4 tools verified by live probe, every result links an official QR-verified registry excerpt), Google Flights Search (hosted real-time fare search from FlightPowers - one-way and round-trip tools over date ranges and destination lists with Google historical price range verdicts and buy links; BYO RapidAPI key, free tier, anonymous tools/list verified both tool names).

[Salesbot MCP - LinkedIn Prospecting and CRM with Human Approval](/hermes/mcp/servers/external/salesbot-mcp) · 48 tools verified, approval-gated sends, x-mcp-api-key.

[Social Glass MCP - Cultural Intelligence for Brand and Research Teams](/hermes/mcp/servers/external/social-glass-mcp) · OAuth remote endpoint, evidence-backed insights search.

[SudnoKontrol MCP - Ukrainian Vessel Registry Search](/hermes/mcp/servers/external/sudnokontrol-mcp) · Keyless, 4 tools probed, QR-verified official excerpts.

[Google Flights MCP - Real-Time Fare Search with Price Verdicts](/hermes/mcp/servers/external/google-flights-mcp) · 2 tools, BYO RapidAPI key, free tier and free ad-supported endpoint.

**Also identified (not catalogued):** Sentinel Scan (free CLI for MCP manifest security and prompt-injection testing - dev tool), ParetoStudio (local prompt/agent/skill library manager - dev utility), Concord MCP (cross-harness communication for coding agents - dev infra), 54ch10-mcp (pre-interact wallet/URL risk briefs paid in x402 USDC - x402 infra class), AgentRisk M2M (pre-trade DeFi agent security with x402 micropayments - crypto/x402 class), SSH MCP Server (developer tools homepage arrival). Feed and homepage repeats already evaluated in Aug 23 sweeps (RE Data Refinery, Truth Bear GAUGE, Agent Conductor, CodeSentinel, BitBrowser, Mangii, Hypnothera). Note: the Aug 23 skip of Booking.com Hotel Search was the same FlightPowers vendor with a thin listing; the Google Flights product above is fully documented with a live endpoint, repo, and registry ID, so it clears the thin-docs bar.

## 🆕 August 24, 2026 - Morning Cron Sweep (8 New, 8 Guides)

Morning sweep sourced from chatmcp/mcpso issues #3719-#3725 (Aug 24 07:39-09:41 UTC), the mcp.so feed, and mcpservers.org /all pages 1-3. 8 new business-relevant servers catalogued with guides: Acquisition.gov MCP (deterministic read-only access to official FAR Overhaul model parts, the agency-deviation index, deviation PDFs and RFO guidance; 5 verified stdio tools returning content hashes and canonical URLs; uvx install, no credentials, from the 1102tools-dev federal contracting family), Universal Poison Armor (open-source prompt-injection and dataset-poisoning firewall: sanitize_document and scan_dataset_for_anomalies on a local FastMCP server plus SKILL.md behavioral directives), SalesTouch (LinkedIn GTM prospecting platform: account, conversation, outreach, publishing, durable scheduling and paginated extraction tools through an OAuth endpoint at salestouch.io/api/mcp, v0.8.0, mutations gated on operator approval), Agency AI MCP (hosted ad manager for Meta and Google accounts: 14 typed tools including create_ad, set_campaign_status, get_anomalies, get_pacing and get_recommendations), Lavox Memory (local-first macOS meeting recorder whose on-device Whisper transcriptions and typed decision index become queryable memory over MCP, decisions stored with rejected alternatives and reasoning), Electronics RFQ Agent (RFQ-to-quote automation: parses PDF/Excel/Word RFQs and prices line items against SAP, Epicor, Oracle and Dynamics via MCP, 9 tools with fill-rate audit), Phonotheca MCP (read-only full-text search over interview transcript archives, speaker-labelled passages with timestamps and citations), Shotstack MCP (official hosted video editing API at mcp.shotstack.io: render video and images, template rendering with merge values, template CRUD, render status and Studio links).

[Acquisition.gov MCP - FAR Overhaul and Agency Deviations](/hermes/mcp/servers/external/acquisition-gov-mcp) · 5 verified tools, content hashes, canonical URLs, no credentials.

[Poison Armor MCP - Prompt-Injection Firewall for AI Agents](/hermes/mcp/servers/external/poison-armor-mcp) · Local FastMCP sanitizer, dataset anomaly scanning, MIT.

[SalesTouch MCP - LinkedIn GTM Prospecting for AI Agents](/hermes/mcp/servers/external/salestouch-mcp) · OAuth remote endpoint, approval-gated mutations, v0.8.0.

[Agency AI MCP - Meta and Google Ads Management from Chat](/hermes/mcp/servers/external/agency-ai-mcp) · 14 typed tools, hosted at s.agencyai.app/mcp.

[Lavox MCP - Local-First Meeting Memory for AI Agents](/hermes/mcp/servers/external/lavox-mcp) · On-device Whisper, decision index with reasoning, macOS.

[Electronics RFQ Agent MCP - RFQ-to-Quote ERP Automation](/hermes/mcp/servers/external/electronics-rfq-mcp) · 9 tools, SAP/Epicor/Oracle/Dynamics via MCP.

[Phonotheca MCP - Interview Transcript Search for Agents](/hermes/mcp/servers/external/phonotheca-mcp) · Read-only archive search, speaker-labelled citations.

[Shotstack MCP - Video Editing API for AI Agents](/hermes/mcp/servers/external/shotstack-mcp) · Official hosted endpoint, template merge rendering, API key.

**Also identified (not catalogued):** 1102tools 8-server federal data family named in issue #3721 (bls-oews, ecfr, federal-register, gsa-calc, gsa-perdiem, regulations-gov, sam-gov, usaspending-gov - pre-existing April 2026 mcp.so listings surfaced by a publisher-migration update, catch-up candidates for a future sweep), AgentPub (agent-to-agent private messaging network - agent community infra class, Fomite precedent), Quantum Readiness Scan qrp-mcp (offline codebase crypto scanner - dev tool), Fleetpost (server-less agent mailbox coordination - agent infra), Daytime Agent Market (Base Sepolia testnet task marketplace - agent infra, TaskMarket class), MetricFire (official infra-monitoring MCP - endpoint not verifiable from public pages, thin docs), BitBrowser MCP service (antidetect browser automation - thin docs, dev automation class), Tseha (design-system serving for coding agents - dev tool), NobGit (git hosting platform MCP - dev tool), Swarme (governed MCP tool-access marketplace - thin docs), Frantic (agent bounty board paid in USDC on Base - agent marketplace class), Claude News (Anthropic news feed - news category covered by Webz.io and NewsMind), Figs Relationship Expert (consumer therapy persona), Lucid Page (Markdown to shareable page - doc publishing utility, Booklet class), Ssave (TikTok/Instagram/YouTube downloader - consumer media utility), mcp.so homepage and feed repeats already evaluated in Aug 23 sweeps (Mangii, Hypnothera, Agent Conductor, CodeSentinel, QR Planet, RADAAR, Dados B3, Upfirst, Xverum, Simplepages, Signal Nodus, SavePropTax, Hermoso, AskRentAI, Truth Bear, TEOS WARN Act).

## 🆕 August 23, 2026 - Night Cron Sweep (11 New, 11 Guides)

Night sweep sourced from chatmcp/mcpso issues #3712-#3718 (Aug 23 16:42-02:00 UTC), the mcp.so feed, and mcpservers.org /all pages 1-3 (~90 newest slugs); Octura's endpoint was live-probed. 11 new business-relevant servers catalogued with guides: TEOS WARN Act Layoff Intelligence (5,964 normalized US WARN notices covering 545,647 workers across CA, TX, NY, IL, NC, refreshed every 12 hours from primary state sources; API key, mcp.tppflow.com/mcp), Walmart Marketplace MCP (234 operations across 28 bundled OpenAPI specs with spec-driven discovery and automatic OAuth2, PyPI), Ozon Seller MCP (151 tools over Seller and Performance APIs, multi-shop), Epovest (hosted GEO/AEO measurement: canon, trackers, surfaces, corroborations; OAuth 2.1 PKCE at mcp.epovest.com/mcp), Octura Site Tools (30 live-probed deterministic ERP, tax, payroll and inventory calculators, keyless at octurasolutions.com/mcp), KD Scout (zero-dependency keyword difficulty, opportunity scoring and content briefs), Real Wave GHL MCP (native GoHighLevel workflow building, OAuth at mcp.realwave.com/mcp), OffenderSearch MCP (all 58 US sex-offender registries in one call, scored and provenance-tagged), GreenCalculus (audit-traced carbon accounting, 11 tools, registry com.greencalculus/api), Normi DVF MCP (17.4M+ geocoded French property transactions, 8 tools), PassportCraft MCP (EU Digital Product Passports for textiles, batteries and general goods, OAuth at passportcraft.com/api/mcp).

[TEOS WARN Act Layoff Intelligence MCP - US Mass-Layoff Data for AI Agents](/hermes/mcp/servers/external/teos-warn-act-mcp) · 5,964 normalized notices, 12-hour refresh, Bearer API key.

[Walmart Marketplace MCP - 234 Marketplace Operations via Spec-Driven Discovery](/hermes/mcp/servers/external/walmart-marketplace-mcp) · PyPI package, automatic OAuth2, multi-seller.

[Ozon Seller MCP - 151 Tools for Russian Marketplace Operations](/hermes/mcp/servers/external/ozon-seller-mcp) · Seller + Performance APIs, multi-shop, MIT.

[Epovest MCP - AI Visibility Measurement for Businesses](/hermes/mcp/servers/external/epovest-mcp) · GEO/AEO tracking, canon, corroborations, OAuth 2.1.

[Octura Site Tools MCP - Deterministic ERP and Tax Calculators](/hermes/mcp/servers/external/octura-site-tools-mcp) · 30 live-probed tools, keyless.

[KD Scout MCP - Keyword Research Arithmetic](/hermes/mcp/servers/external/kd-scout-mcp) · Difficulty, opportunity scoring, content briefs, no keys.

[Real Wave GHL MCP - Native GoHighLevel Workflow Building](/hermes/mcp/servers/external/realwave-ghl-mcp) · OAuth sign-in, builds real GHL automations.

[OffenderSearch MCP - Nationwide Registry Screening](/hermes/mcp/servers/external/offendersearch-mcp) · 58 registries, batch of 1,000, scored citations.

[GreenCalculus MCP - Audit-Traced Carbon Accounting](/hermes/mcp/servers/external/greencalculus-mcp) · 11 tools, pinned data versions, CSRD-ready.

[Normi DVF MCP - French Property Market Data](/hermes/mcp/servers/external/normi-dvf-mcp) · 17.4M+ geocoded transactions, 8 tools.

[PassportCraft MCP - EU Digital Product Passports](/hermes/mcp/servers/external/passportcraft-mcp) · ESPR compliance drafting, OAuth, free plan.

**Also identified (not catalogued):** GH issues #3712-#3718 skips (motion-menu 597 design patterns - dev/design tool, AURORA Agent decision-context compiler - agent dev infra, TRAECNclaw TraeCN desktop automation - local dev tool, MCP Marketplace directory-search utility - dev tool, BuyWhere and Atlas Verified - repeats of already-evaluated entries, TANCO SkillHub - skills catalog not an MCP server), SecondSim (2-tool UK eSIM checkout funnel - consumer telecom utility, Roamzy class), NotFair Plugin (marketing SKILLS library not an MCP server - listing overclaims 117 hosted tools), CLSTR (free keyless agent news feed - news category covered by Webz.io and Newsmind), Botsify (white-label chatbot platform), ClipMyApp (app-marketing video creation - no published tool list), Famulor (omnichannel contact-center management), Meistron (German crafts business software - geo-niche), Unplain (document-to-PDF publishing - doc utility), Socializioz (AI social media employee - thin docs), FrankKi (printed-letter API - postal utility), Magichour (AI media model aggregator - UnificAlly class), WickedAPI (market data - thin docs), 9-bot (WhatsApp group automation), Nautilinks (French backlink marketplace - geo-niche), Den (Korean construction standards - geo-niche), Neotic and Calaf (thin docs / niche), plus dev-tool slugs on /all pages 1-3 (dockndevai 8-server infra burst, framework-mcp, reqlan, cortex-connector, doco, commitlore, vinvai, ytdlp-transcript, m00nreport, diffcontext, plurality-memory, swarm-tips, hireme, macadress, betadrop, cli_revit, contextstream, geolens, canonic, payagents x402 wallet plumbing, lvtd x402 skill market).

## 🆕 August 23, 2026 - Evening Cron Sweep (2 New, 2 Guides)

Evening sweep sourced from chatmcp/mcpso issues #3704-#3711 (Aug 23 11:48-16:42 UTC) plus the mcp.so and mcpservers.org homepages (all repeats of prior evaluations). 2 new business-relevant servers found: Atlas Verified, an official-registry supply-chain verification server (organic certification against the USDA Organic Integrity Database, OFAC screening, FDA import controls, document authentication with 30+ checks, structured trade intelligence from 50+ attributed sources; OAuth 2.0 + PKCE at api.atlasverified.ai/mcp, 401 auth gate confirmed live); and OEDON, a hosted x402 Bitcoin on-chain intelligence server (fee pressure, mempool stats, address analytics, hashrate, difficulty, block tips, mining pools, tx lookup, whale alerts; live-probed oedon v0.2.0 at oedon.dev/mcp, 0.005 USDC per query). 6 skipped: symfony-agent-mcp, annolux, LUNO, target5, BuyWhere, GateCore.

[Atlas Verified MCP - Supply Chain Compliance and Trade Verification](/hermes/mcp/servers/external/atlas-verified-mcp) · Official registry v1.0.0, OAuth 2.0 + PKCE, 50+ attributed trade data sources.

[OEDON MCP - Bitcoin On-Chain Intelligence for AI Agents](/hermes/mcp/servers/external/oedon-mcp) · Live-probed v0.2.0, x402 pay-per-call in USDC on Base, 0.005 USDC per query.

**Also identified (not catalogued):** symfony-agent-mcp (read-only Symfony codebase introspection, 1,677 tools - dev tool), annolux (curated bilingual web search - search utility class, same as Context.dev), LUNO (AI backend platform, no tools listed - dev infra), target5 (agent debate board with hash chain - agent community infra), BuyWhere (SEA shopping search - resubmission of an already-catalogued entry), GateCore (governed agent procurement marketplace - agent infra).

## 🆕 August 23, 2026 - Overnight Cron Sweep (1 New, 1 Guide)

Overnight sweep sourced from chatmcp/mcpso issues #3699-#3700 (Aug 22 19:56-22:34 UTC), the mcpservers.org homepage slugs, and the mcp.so homepage recentServers. 1 new business-relevant server found: BulkTranscripts, a hosted remote YouTube research server with 7 live-probed tools for transcript fetching (single or batch of 20), video/channel/playlist search, channel archive listing and free new-upload tracking; keyless start with 50 free transcript extractions per IP, then one-time credit packs, cached transcripts always free. 6 skipped: Markovo (file and URL to Markdown conversion CLI, dev utility), deja-vu (local memory over coding-agent session histories, dev infra), Agents Get Paid Kit (x402 payment plumbing for agents), Public Signal Data (Apify-actor wrapper with no first-party endpoint, thin vendor surface), Appraisily (appraisal lead-gen funnel with a six-result auction teaser, thin data surface), Fresh Jots (agent and script logging notebook, agent infra class).

[BulkTranscripts MCP - Hosted YouTube Transcripts and Channel Research](/hermes/mcp/servers/external/bulktranscripts-mcp) · Live-probed 7 tools (server v1.0.0), keyless free tier, no install.

**Also identified (not catalogued):** Markovo (customer-side file and public-URL to Markdown converter - dev utility class, same as Booklet), deja-vu (local BM25 memory over coding-agent session histories - agent dev infra), Agents Get Paid Kit (x402 payment plumbing - spend caps and AUP tooling), Public Signal Data (curated Apify actors behind mcp.apify.com - thin vendor surface), Appraisily (appraisal lead funnel with up to six auction results per search - thin data surface), Fresh Jots (shared notebook for scripts and agents - agent infra class).

## 🆕 August 23, 2026 - Morning Cron Sweep (4 New, 4 Guides)

Morning sweep sourced from chatmcp/mcpso issues #3701-#3703 (Aug 23 04:42-07:48 UTC), the mcp.so homepage recentServers and feed, and the mcpservers.org homepage. 4 new business-relevant servers found, all live-probed: FluentEDI (hosted X12 EDI document toolbelt), Domain MCP (Dynadot domain, DNS and transfer management), Kirah Local Services (local business discovery and booking), Truth Bear GAUGE (verifiable government data with cryptographic proof, x402 pay-per-call). 5 skipped: Infyicon, Context.dev, DotLy ID, Hypnothera, plus feed and homepage repeats already evaluated.

### FluentEDI MCP ★★★ - August 23 (morning)

Hosted keyless X12 EDI toolkit: edi_parse, edi_validate and edi_build for the 850/856/810/855/997 retail transaction set plus JSON repair, contract-drift detection, cron and time utilities. `fluentedi.com/mcp` (live-probed v1.0.0, 17 exposed tools with a tool_call dispatcher; batch of 20 calls per round trip). Free, no key, no signup, stateless. · [Guide →](/hermes/mcp/servers/external/fluentedi-mcp)

### Domain MCP ★★★ - August 23 (morning)

Dynadot domain portfolio management from an agent: 108 API actions grouped into 10 composite tools covering registration, renewals, DNS records, nameservers, WHOIS contacts, transfers, folders and aftermarket auctions. npm `domain-mcp` v2.0.0 (MIT, 12 stars), npx install with DYNADOT_API_KEY, sandbox mode included. · [Guide →](/hermes/mcp/servers/external/domain-mcp)

### Kirah Local Services MCP ★★★ - August 23 (morning)

Local services marketplace with booking: search businesses, read service catalogs (price, duration, deposit, intake), check live availability and create, reschedule or cancel bookings with guest checkout. `kirah.ai/api/mcp` (live-probed kirah-agent-gateway v2.16, 10 tools), keyless, OpenAPI published. · [Guide →](/hermes/mcp/servers/external/kirah-local-services-mcp)

### Truth Bear GAUGE ★★★ - August 23 (morning)

Official government data (SEC, FDA, USGS, NOAA signals) with cryptographic proof: free find_signal coverage checks and verify_citation hash recomputation, paid records pay-per-call over x402 in USDC on Base. `api.truthbear.co/mcp` (live-probed v1.0.0, 3 tools), no API key. · [Guide →](/hermes/mcp/servers/external/truth-bear-gauge)

**Also identified (not catalogued):** Infyicon (161,000+ free icon library with SVG retrieval - design assets, not business data), Context.dev (web-data infrastructure for AI products - saturated web-scraping category, same class as rasterly), DotLy ID (biolink and domain-registration vendor, endpoint not probeable - thin niche surface, Registly class), Hypnothera (personalized hypnosis sessions - consumer wellness, Jul 17 listing), plus feed and homepage repeats already evaluated (Agent Conductor, CodeSentinel, QR Planet, RADAAR, My AskAI, Dados B3, SavePropTax, Xverum, Hermoso, Simplepages, DPF, Webz.io, ship.page, Upfirst).

## 🆕 August 22, 2026 - Docs Maintenance Sweep (2 New, 2 Guides)

Docs maintenance sweep sourced from chatmcp/mcpso issues #3689-#3698 (Aug 22 06:24-18:02 UTC). 2 new business-relevant servers found: Corpus Law, a remote legal-search and business-formation server (551,201+ provisions of US federal, state and municipal law across 18 jurisdictions with verbatim citations, plus agent-native LLC/nonprofit intake checklists, NAICS lookup and prefilled filing handoffs; anonymous free tier, live-probed v1.2.1, 7 tools confirmed); and Breakreach, an AI-native social scheduling server covering 12 platforms with best-time slots, media upload and unified analytics (live HTTP 401 auth gate confirmed). 6 skipped: Mangii (manga image generator, consumer media), CCS Runtime Evidence (local security runtime verification, dev tool), Secret MCP (GDWEB design analysis, dev utility), Adtivity (analytics SDK installer into codebases, dev tool), a11y-toolkit (local WCAG accessibility suite, dev tool), Lachesis (compiler-precise code property graph, dev infrastructure - same class as the Lachesis skip in the morning sweep).

### Corpus Law MCP ★★★ - August 22 (docs maintenance)

US legal search and business formation over MCP: 551,201+ provisions of federal, state and municipal law across 18 jurisdictions (16 fully searchable), vector + full-text searchable with verbatim citations and full-text lookup. Formation tools collect the exact state-specific LLC/nonprofit intake checklist, map plain-English descriptions to NAICS codes, and generate prefilled filing handoffs. 7 tools at `corpuslaw.us/api/mcp` (live-probed, anonymous tools/list returned all 7; server v1.2.1). Free tier: 100 searches/month per IP, no OAuth, no session state. (freemium) · [Guide →](/hermes/mcp/servers/external/corpus-law-mcp)

### Breakreach MCP ★★★ - August 22 (docs maintenance)

AI-native social media scheduling across 12 platforms (X, Instagram, TikTok, LinkedIn, Bluesky, Reddit, Telegram, Discord and more): 9 tools to create, schedule and analyze posts, with best-time slots, media upload and unified analytics. `api.breakreach.com/mcp` (live HTTP 401 auth gate confirmed for anonymous callers). Bearer API key required. (commercial) · [Guide →](/hermes/mcp/servers/external/breakreach-mcp)

**Also identified (not catalogued):** Mangii (remote manga image generator - consumer media, same class as UnificAlly skip), CCS Runtime Evidence (npx security runtime verification - local dev tool), Secret MCP (evidence-grounded web design analysis - dev utility), Adtivity (analytics SDK installer + churn prediction for founders - installs into codebases, dev tool), a11y-toolkit (local WCAG 2.2 accessibility suite - dev tool), Lachesis (compiler-precise code property graph - dev infrastructure).

## 🆕 August 22, 2026 - Evening Cron Sweep (4 New, 4 Guides)

Evening sweep sourced from the mcp.so Feed (newest 30 submissions) and mcpservers.org /all pages 1-3 (newest ~50 slugs). 4 new business-relevant servers found: Antwork, a hosted social publishing server with 35 tools across 8 platforms and OAuth 2.1 scopes; Gex Live, a measurement-only SPX dealer-positioning server with a plain-English backtesting Lab; Sprkly, a shortform publishing server with queue-based approval gates and scoped keys; and ship.page, a zero-config HTML deployment server from the lucid.page team. All four endpoints live-probed (Antwork HTTP 401 auth gate as expected; Gex, Sprkly and ship.page returned full tool lists to anonymous tools/list calls). 10 skipped (see the skip paragraph below).

### Antwork MCP ★★★ - August 22 (evening)

Hosted social publishing for LinkedIn, X, Instagram, Facebook, Threads, TikTok, Pinterest and YouTube: 35 tools across identity, workspaces, social accounts, voice profiles, posts, publishing, analytics and media. Per-platform voice profiles learned from existing content; OAuth 2.1 with PKCE and DCR, granular read/write/publish/media scopes; publish_post returns per-platform status. `api.antwork.io/mcp` (live-probed HTTP 401 auth gate). Free plan; Pro and Business tiers. (commercial) · [Guide →](/hermes/mcp/servers/external/antwork-mcp)

### Gex Live MCP ★★ - August 22 (evening)

Measurement-only SPX dealer positioning from the 0DTE tape: zero-gamma flip, call/put walls and hold band for 1,000+ finished sessions. Three free keyless tools (`list_sessions`, `get_session`, `get_levels`) plus a five-tool Lab that compiles plain-English ideas into rules, backtests and quant-optimizes them. `mcp.gex.live/mcp` (live-probed, anonymous tools/list returned the 3 free tools). No signals by design; Lab runs cost credits. (freemium) · [Guide →](/hermes/mcp/servers/external/gex-live-mcp)

### Sprkly MCP ★★ - August 22 (evening)

Shortform publishing to TikTok, Facebook, Instagram, YouTube and Threads through a queue-based approval model: 16 tools for media, drafts, scheduling, account listing, analytics and approval requests. No publish-now tool, published posts are agent-read-only, keys scoped per account and per action. `sprkly.app/api/mcp` (live-probed, anonymous tools/list returned all 16 tools). OAuth or `sk_live_` key; MCP included in paid plans and trial. (commercial) · [Guide →](/hermes/mcp/servers/external/sprkly-mcp)

### ship.page MCP ★★ - August 22 (evening)

Zero-config HTML deployment from any agent: `deploy_html` and `deploy_files` return live unguessable URLs with no signup; claim tokens attach anonymous drops to an account; Pro adds named drops and 30-day expiry. 7 tools at `ship.page/mcp` (live-probed, anonymous tools/list returned all 7). From the lucid.page team; free anonymous tier, Pro $4/mo. (freemium) · [Guide →](/hermes/mcp/servers/external/ship-page-mcp)

**Also identified (not catalogued):** Taskfolk (already catalogued Aug 20 overnight), BCMS (mcp.so client listing with no MCP server surface - thin docs), Atoa (GitHub org slug listing SDK repos with no MCP endpoint or tool list - thin docs), Gifi (AI-text-watermark inspection and rewriting), Agent Conductor and CodeSentinel (AGENTS.md/skill-registry and codebase-health dev tools from a single author - dev infra), FaceSign (step-up verification SDK for developers), Booking.com Hotel Search (consumer travel), Seedfast (PostgreSQL synthetic test-data generator - dev tool), Opportunity Atlas (Northeast Ohio construction opportunity data - geo-niche).

## 🆕 August 22, 2026 - Morning Cron Sweep (3 New, 3 Guides)

Morning sweep sourced from chatmcp/mcpso issues #3683-#3690 (Aug 22 03:54-07:49 UTC) plus both directory homepages and the mcp.so Feed (all homepage and feed candidates were repeats already evaluated, except html-css-to-image, a dev utility in the skip class). 3 new business-relevant servers found: Crisphive, a hosted field-service dispatch and technician scheduling server with 43 OpenAPI-generated tools and preview/commit safety on every mutation; Dados B3, an auditable Brazilian stock fundamentals server with point-in-time multiples and public methodology; and Staddress AI, a Japanese address normalization server returning structured components, coordinates and confidence scores. Crisphive's endpoint verified live via its HTTP 401 auth gate; Dados B3 live-probed with all 14 tools confirmed. 2 skipped: Lachesis (compiler-precise code property graph, dev infrastructure) and x402 Bazaar Doctor (x402 payment diagnostics, same class as the 402oracle skip).

### Crisphive MCP ★★★ - August 22 (morning)

Field-service dispatch and technician scheduling over MCP: 43 tools generated from the same OpenAPI spec as the REST SDKs, covering customers, service catalog, live availability, job booking, work orders, dispatch, CRM and fleet. Preview/commit pairs on every mutation, idempotency keys and typed error codes; deterministic sub-3-second cascade rescheduling. OAuth 2.1 (DCR + PKCE) or API key at `api.crisphive.com/mcp`; `chsk_test_` keys hit an isolated sandbox. (commercial, sandbox keys) · [Guide →](/hermes/mcp/servers/external/crisphive-mcp)

### Dados B3 MCP ★★★ - August 22 (morning)

Auditable Brazilian stock (B3) fundamentals, 2010-today: 14 tools covering 402 listed companies plus Brazilian REIT (FII) rankings. Point-in-time multiples priced on the first session after each filing's publication, Piotroski F-Scores with every criterion auditable, republication tracking and CVM source accounts for every figure. Public methodology, no auth on the free tier at `dadosb3.com/mcp/` (live-probed v1.29.0). (free tier; keys for full coverage) · [Guide →](/hermes/mcp/servers/external/dados-b3-mcp)

### Staddress AI MCP ★★ - August 22 (morning)

Japanese address normalization over stdio: parse unstructured Japanese addresses into structured components with latitude/longitude, confidence score and address code, batch parsing up to 100, and API usage checks. `npx -y @staddress/mcp` with a `STADDRESS_API_KEY`. (commercial API, MIT client) · [Guide →](/hermes/mcp/servers/external/staddress-mcp)

## 🆕 August 22, 2026 - Overnight Cron Sweep (2 New, 2 Guides)

Overnight sweep sourced from chatmcp/mcpso issues #3680-#3682 (Aug 21 19:05-23:20 UTC) plus the mcp.so and mcpservers.org homepages. 2 new business-relevant servers found: FinalPeace, a statute-cited US estate document requirements server with 50-state execution rules, an urgency-ordered after-a-loss checklist and a planning-gap assessment, and Pocket Drives, a read-only P2P marketplace for luxury, exotic and EV rentals with line-item quotes, availability calendars and host showrooms. Both endpoints live-probed before publishing. 5 skipped: LatticeNet (agent-publishing community infra, same class as The Fomite), UnificAlly (AI media model aggregator, dev utility), Claude News (niche Claude/Anthropic news feed), 2328 Documentation (vendor docs surface), Bifrost Gateway (self-hosted AI gateway infra).

## 🆕 August 21, 2026 - Afternoon Cron Sweep (11 New, 11 Guides)

Afternoon sweep sourced from the mcp.so Feed (newest 30 submissions), chatmcp/mcpso issues #3673-#3679 (Aug 21 11:08-17:36 UTC), and the mcpservers.org /all TanStack state. 11 new business-relevant servers found: a read-only Rent Manager portfolio intelligence server, primary-source SEC intelligence priced per call, a multi-app OAuth integration platform, the official Riddle interactive-content MCP, a scope-gated social publishing server, and six more covering docs publishing, LinkedIn voice content, website conversion provisioning, TomTicket helpdesk, Shopify App Store intelligence and Mobbin design research. 7 skipped (x402/crypto/dev-infra/geo-niche classes).

### AskRentAI MCP ★★★ - August 21 (afternoon)

Hosted read-only MCP for Rent Manager portfolios: plain-English NOI, rent roll, delinquency, vacancy, lease-expiration, work-order, vendor-spend and financial-report questions answered from live data. OAuth, Streamable HTTP at `api.askrentai.com/mcp`; $10/user/mo, 7-day trial; read-only by design - no write path back to the property system. (commercial, trial) · [Guide →](/hermes/mcp/servers/external/askrentai-mcp)

### Signal Nodus SEC Filings MCP ★★★ - August 21 (afternoon)

Primary-source SEC intelligence, priced per call: 27 tools including sentence-level year-over-year 10-K/10-Q diffs, 8-K events, 13D/13G activist stakes, Form 4 insider trades, 13F holdings, IPO pipeline, full-text EDGAR search since 2001, XBRL financials with numeric claim verification, plus federal awards and lobbying. Endpoint `mcp.signalnodus.ai`; prepaid Bearer key or x402 per-call on Base; `lookup_company` free. (pay-per-call) · [Guide →](/hermes/mcp/servers/external/signal-nodus-mcp)

### One MCP ★★★ - August 21 (afternoon)

One hosted MCP server for Gmail, Slack, Stripe, Shopify, HubSpot, Notion, Linear, Salesforce, QuickBooks and more: four tools - list integrations, search platform actions, read action knowledge docs, execute - over OAuth with per-connection scoped grants. `mcp.withone.ai/mcp`. (commercial) · [Guide →](/hermes/mcp/servers/external/one-mcp)

### Riddle Quiz Maker MCP ★★★ - August 21 (afternoon)

Official Riddle.com MCP: 62 tools to create and manage quizzes, polls, surveys, personality tests, forms, predictors, minigames and leaderboards with branching logic, custom design, live stats, lead capture and embed code. OAuth at `riddle.com/creator/api/v3/mcp`. (commercial) · [Guide →](/hermes/mcp/servers/external/riddle-mcp)

### Maeve Social MCP ★★★ - August 21 (afternoon)

Social publishing with scope-gated agent access: planning, scheduling, media and analytics reads are open, drafting needs permission, and anything public requires by-name confirmation (`publish_now:cnt_...`). Hosted at `api.maevesocial.com/mcp` (live-probed HTTP 401 auth gate). (commercial, 3-day trial) · [Guide →](/hermes/mcp/servers/external/maeve-social-mcp)

### lucid.page MCP ★★ - August 21 (afternoon)

Publish Markdown as a typeset shareable page from any agent: `publish_doc` works anonymously with a claim-token flow; an `lp_` key adds updates with revisions, private docs, listing/deletion and multi-chapter bundles. Seven tools at `lucid.page/mcp`. (free; Pro analytics) · [Guide →](/hermes/mcp/servers/external/lucid-page-mcp)

### LinkedIn Ghostwriter MCP ★★ - August 21 (afternoon)

ContentIn's voice-preserving LinkedIn writer: `write_post_in_my_voice` drafts from VoiceDNA trained on your posts, with schedule/publish via LinkedIn's official API and honest analytics read-back (unmeasured ≠ zero). Eight tools at `mcp.contentin.io/mcp-server` with an X-MCP-Key header. (commercial) · [Guide →](/hermes/mcp/servers/external/linkedin-ghostwriter-mcp)

### ClaraConverts MCP ★★ - August 21 (afternoon)

MCP provisioning for a 24/7 website conversion agent: 9 tools cover pricing, trial-tenant creation, embed snippet, site-knowledge refresh, integration config, Cal.com event types and upgrade links. Public tools keyless; Bearer token after `create_trial_tenant`. `claraconverts.com/mcp`. (freemium, from $49/mo) · [Guide →](/hermes/mcp/servers/external/claraconverts-mcp)

### TomTicket MCP ★★ - August 21 (afternoon)

TomTicket helpdesk over stdio: list and read tickets, reply as operator with work time, internal comments, transfers, status transitions and finish, plus customers, organizations, chats, departments and KB. `npx -y mcp-tomticket` with a `TOMTICKET_TOKEN`. (open source) · [Guide →](/hermes/mcp/servers/external/tomticket-mcp)

### BestAppify MCP ★★ - August 21 (afternoon)

Shopify App Store intelligence for AI clients: 40 tools covering keyword rankings, opportunities, competitor tracking, review intelligence, forum mentions, listing changes, revenue and churn. Bearer key at `bestappify.app/api/mcp`; free tier 100 req/day, no card. (freemium) · [Guide →](/hermes/mcp/servers/external/bestappify-mcp)

### Mobbin MCP ★★ - August 21 (afternoon)

Official Mobbin MCP: natural-language search over 600,000+ real product screens - screens, multi-step flows and website sections - with inline images and canonical mobbin_url citation. Three tools, OAuth at `api.mobbin.com/mcp`. (commercial) · [Guide →](/hermes/mcp/servers/external/mobbin-mcp)

**Also identified (not catalogued):** TaskMarket (x402 worker-market infra - #3673), rasterly (Firecrawl alternative, saturated web-scraping category - #3676), Magpie Capital (Solana lending - crypto, #3677), Skycloak (128-tool Keycloak IAM management - dev/IT infra), Parse.bot (browser-automation API builder - saturated category), AdminLanding (France/Switzerland rental-compliance - geo-niche, consistent with Saymon RU and eCourts India skips), Roboterradar RadarScore (humanoid-robot ratings dataset - research niche), plus mcpservers.org /all slugs reviewed and skipped (HostDeFi, ToolYour, DeepSearch, Melt, Registly, Signal Sprint, MaxCrawl - dev/niche tools) and Feed repeats already catalogued or previously skipped (Hermoso, RADAAR, Upfirst, Webz.io, Simplepages, DPF, Xverum, SavePropTax, Waqi, Bitroad, QR Planet, 3gpp-mcp, CSOAI GSPC, FineData.ai, Sonar ASO, Raccha AI, My AskAI).

## 🆕 August 21, 2026 - Morning Cron Sweep (3 New, 3 Guides)

Morning sweep sourced from chatmcp/mcpso submission issues filed after the overnight cutoff (#3669 through #3672, Aug 21 07:22-09:47 UTC) plus both directory homepages (all homepage candidates were repeats already evaluated). 3 new business-relevant servers found: a read-only self-hosted IMAP email server, a hosted RSS semantic-search and digest service, and Korean AEC standards with clause references. 1 skipped (Kura, x402 agent-wallet infrastructure, consistent with prior x402-infra decisions).

### your-mail-mcp ★★ - August 21 (morning)

Read-only, self-hosted IMAP email for MCP clients: ten read-only tools (`search`, `ids`, `files`, `count`, `show`, `thread`, `text`, `folders`, `refresh`, `attachment`) over a one-way mbsync mirror indexed by notmuch, served through OAuth 2.0 with Dynamic Client Registration. No send, delete, move or tag exists in the process. Docker or static Go binaries; junk and trash excluded by default; prompt-injection markers on all mail text. (self-hosted, free) · [Guide →](/hermes/mcp/servers/external/your-mail-mcp)

### Newsmind MCP ★★ - August 21 (morning)

Hosted RSS for AI clients: 29 tools for reading and briefing, full-text and semantic search, story clustering and dedupe, keyword watches with scheduled email digests, subscriptions and OPML import/export. OAuth 2.1 in Claude, ChatGPT and Gemini, Bearer PATs for other clients; 14-day trial then from $24/year. Endpoint live at `newsmind.app/mcp` (HTTP 401 to anonymous probes, the expected gate). (paid, trial) · [Guide →](/hermes/mcp/servers/external/newsmind-mcp)

### den MCP ★ - August 21 (morning)

Korean AEC standards (KDS, KCS, KS, building statutes) answered with the clause citation attached; abstains when it has no grounds and labels snippet scope (domestic norm vs foreign reference vs analysis). Ten tools including `k_snippets`, `compare`, `scenario`, `site_context` and `review_plan`, plus `as_of` for historical standards. Bearer token, free beta at den.archi; endpoint live (HTTP 401 unauthenticated, the expected gate). (free beta) · [Guide →](/hermes/mcp/servers/external/den-archi-mcp)

## 🆕 August 21, 2026 - Overnight Cron Sweep (4 New, 4 Guides)

Overnight sweep sourced from chatmcp/mcpso submission issues filed after the evening cutoff (Aug 20 20:13 through Aug 21 00:48 UTC), the mcpservers.org /all TanStack state (30 newest), and both directory homepages. 4 new business-relevant servers found: a keyless 13-tool website QA and AI-visibility toolkit, a carbide grade cross-reference for machining procurement, the official Webz.io news search MCP, and LiveSend document publishing with read analytics.

### Superflow Free Tools MCP ★★ - August 21 (overnight)

Thirteen keyless website QA and AI-visibility tools on one remote endpoint: `check_ai_visibility` (ChatGPT, Claude, Perplexity, Google AI reach), `check_robots_txt_for_ai`, `generate_llms_txt` per the llmstxt.org convention, `validate_json_ld`/`generate_json_ld`, `check_social_preview`, `detect_tech_stack`, `capture_full_page_screenshot`, `generate_alt_text`, `build_utm_url`, `page_to_markdown`, `check_favicon`, `hash_md5`. Hosted keyless at `usesuperflow.ai/api/mcp`; live-probed Aug 21 (server v1.0.0, 13 tools). (free) · [Guide →](/hermes/mcp/servers/external/superflow-free-tools)

### CuttingToolsAI MCP ★★ - August 21 (overnight)

Brand-neutral carbide grade cross-reference for machining: one read-only `grade_xref` tool returns catalog-verified comparable insert grades across manufacturers at the same ISO application position, with provenance per row; unknown codes return empty rather than a guess. Keyless Cloudflare Worker endpoint; backed by the public cuttingtoolsai.eu/api/xref REST API. (MIT, free) · [Guide →](/hermes/mcp/servers/external/cuttingtoolsai-mcp)

### Webz.io News Search MCP ★★ - August 21 (overnight)

Official vendor MCP from Webz.io: `news_search_by_webz` natural-language global news search with domain, country, language, sentiment, and 17-category filters, a 30-day recency window, and k up to 50 - results carry title, URL, publish date, and excerpt for citable research. Hosted at `news-search-mcp.webz.io/mcp` with a Bearer token (free key); ships an Agent Skill file. (commercial, free tier) · [Guide →](/hermes/mcp/servers/external/webz-news-search)

### LiveSend MCP ★★ - August 21 (overnight)

Publish LLM-written reports to permanent, trackable, password-protected links: 12 tools across five intentions - publish (`create_document`, `add_version`), revise (`edit_document`, `list_versions`, `restore_version`), protect (`set_password`), measure (`get_analytics`, `get_comments`), and find (`list_documents`, `get_document`, `list_team_documents`, `share_document`). Hosted remote with a one-time browser approval flow; readers get a plain browser link. (freemium, 3 docs free) · [Guide →](/hermes/mcp/servers/external/livesend-mcp)

**Also identified (not catalogued):** no_human (local stdio coding-task bridge, dev tool - #3665), klo-mcp (native macOS video editor, creator tool - #3667), The Fomite (agent community memory/message-board infra), ego lite browser and kogiQA (browser tooling for coding agents), RADAAR (already catalogued), plus repeats already evaluated in prior sweeps (QR Planet, Xverum, SavePropTax, CSOAI GSPC, 3gpp-mcp, Waqi, Bitroad, Alpha Vantage, Arcaeon Ledger, and the /all and homepage slugs covered by the Aug 20 evening report).

## 🆕 August 20, 2026 - Evening Cron Sweep (11 New, 7 Guides)

Evening sweep sourced from chatmcp/mcpso submission issues filed after the morning cutoff (Aug 20 10:44 through 16:42 UTC), the mcpservers.org /all JSON-LD page (30 newest), and both directory homepages. 11 new business-relevant servers found: an AI phone receptionist for small businesses, the official UK Pay by Bank payments MCP, dependency license verdicts computed against your distribution model, competitor ad creative intelligence, landing pages built and measured from chat, email verification with catch-all detection, and Northeast Ohio construction opportunity intelligence - plus four catalog entries covering US job-posting search, a natural-language data platform, a 254-tool education platform surface, and a database intelligence layer.

### Upfirst MCP ★★★ - August 20 (evening)

First-party MCP server for Upfirst, the AI phone receptionist for small businesses: nine tools to review call transcripts (`list_calls`, `get_call_details`, `get_call_transcript`), audit and fix receptionist knowledge (`get_agent_knowledge`, `create_agent_knowledge`, `update_agent_knowledge`), and manage skills, transfer rules, schedules, and agent settings (`create_agent_skill`, `update_agent_skill`, `update_agent_by_id`). Hosted remote with an in-app OAuth connector flow - the endpoint URL is provisioned from the Upfirst app. (commercial, free tier) · [Guide →](/hermes/mcp/servers/external/upfirst-mcp)

### Atoa MCP ★★★ - August 20 (evening)

First-party payments MCP from Atoa, the FCA-authorised UK payments platform: `process_payment`, `get_payment`, `capture_payment`, `cancel_payment`, full customer CRUD (`create/get/update/delete_customer`, `list_customers`), `initiate_refund`/`cancel_refund`, `get_transactions`, `create_webhook`/`delete_webhook`, plus bank feeds and human-approval flows for the money-out path. Hosted at `mcp.atoa.me/mcp` with a Bearer SDK token and `X-Atoa-Env` sandbox/production header; local npx mode available. (commercial, PCI DSS / ISO 27001 / SOC 2) · [Guide →](/hermes/mcp/servers/external/atoa-mcp)

### LicenseGuard MCP ★★★ - August 20 (evening)

License-compliance verdicts computed against your distribution model - the same AGPL dependency is blocked for SaaS, allowed for internal use, and allowed as a build-time devDependency. Three tools (`check_dependency_license`, `check_manifest_licenses`, `explain_license`) with clause-cited verdicts, transitive lockfile audits across npm, PyPI, Go and crates.io, and a guarantee that incomplete scans are never reported clean. Hosted keyless at `license-guard.rcc-aoki.workers.dev/mcp` plus a local stdio Docker image. (Apache-2.0, free) · [Guide →](/hermes/mcp/servers/external/license-guard-mcp)

### AdMapix MCP ★★ - August 20 (evening)

Competitor ad creative intelligence over the AdMapix API: `search_creatives` by keyword, app name, advertiser, category, or ad copy with creative-type, country, and date-range filters and sorting by first seen, relevance, estimated impressions, or days active - raw structured records with media URLs and metrics. Local stdio via `uvx --from admapix-mcp` (PyPI v1.0.0) with an `ADMAPIX_API_KEY`. (commercial API, open-source server) · [Guide →](/hermes/mcp/servers/external/admapix-mcp)

### Simplepages MCP ★★ - August 20 (evening)

Landing pages built, edited, and measured from chat: describe a page and it builds one in your workspace, edit headlines in place, list pages and sites with status, and pull visitors, leads, and revenue per page or workspace. Hosted remote with an OAuth connect flow scoped to one workspace; publishing stays a human action. (commercial) · [Guide →](/hermes/mcp/servers/external/simplepages-mcp)

### Giggal.ai MCP ★★ - August 20 (evening)

Email verification with catch-all detection inside any MCP client: deep mailbox existence checks that resolve catch-all, accept-all, and SEG-protected addresses, plus credit and verification-history lookup. Hosted at `mcp.giggal.ai/mcp` with an API key scoped to `verify:read`. (commercial, credit-based) · [Guide →](/hermes/mcp/servers/external/giggal-mcp)

### Opportunity Atlas MCP ★★ - August 20 (evening)

Verified Northeast Ohio construction opportunity intelligence for AI agents: free `scout_capabilities` and `scout_preview` tools keyless, with a registered-agent surface for the full pipeline at capped rates (20 req/min, 100/day) and hashed 90-day keys. Supabase-hosted remote at `zmxwkvmxcfjgwbrtxxhl.supabase.co/functions/v1/scout-mcp`. (free public beta) · [Guide →](/hermes/mcp/servers/external/opportunity-atlas-mcp)

### Magnificent Jobs MCP ★★ - August 20 (evening) (catalog entry)

Semantic search over 3.5M+ live US job postings pulled hourly straight from company ATS boards - positions LinkedIn and Indeed miss - with 211K+ added the day of listing. Free, read-only, no key; `npx magnificentjobs`. (free)

### DPF MCP ★★ - August 20 (evening) (catalog entry)

Natural-language data ingestion, transformation, and analytics platform with an operator-safe access model: DPF holds no standing credentials - access runs through a revocable AWS IAM role you control, and SFTP connections use a generated RSA-4096 keypair whose private half is never returned by any API call. (commercial)

### Teachfluence MCP ★★ - August 20 (evening) (catalog entry)

Production MCP server for Teachfluence, the all-in-one platform for online educators: 254 tools across 29 families covering courses, community, forms, CRM, support, and revenue behind OAuth 2.1 with per-organization default-deny and an audit row on every call. (commercial)

### Terno MCP ★★ - August 20 (evening) (catalog entry)

Database intelligence layer that bridges AI agents and enterprise data with strict access controls and LLM-optimized schema context for warehouse-scale databases; hosted OAuth connection or embedded directly into Django projects. (open source)

### Also identified (not catalogued)

GitHub submissions reviewed and skipped this cycle: Proactive Vault (personal CRM for macOS - GitHub repo 404 at evaluation time), Wondel Skills (skill-loader dev tool), AI Developer Toolkit (AI-dev guide search), 2anki (consumer Anki-deck converter), Fine Structure (full-stack app builder - dev). mcpservers.org /all slugs reviewed and skipped: Clio for Creatio (platform dev tool), GlianaAI (x402 model-gateway infrastructure), RiverScript (transcript-fetching niche), MarkIt (personal bookmarking), FaceSign (step-up verification dev flows), POB (Path of Exile gaming), Chamnan (Claude Code security plugin), AST MCP (TypeScript project access - dev), AgentTrust (XRPL blockchain referee), Agentic HIL (embedded-hardware dev), Seedfast (synthetic test data), HTTP 402 AI Tollbooth (x402 infrastructure), QR Planet (QR-code design utility). Repeats already catalogued or previously skipped: Booking.com Hotel Search (FlightPowers thin vendor surface), Football Charts (sports skip precedent), 60fps, MindMap AI, Vital Care Finder, CSOAI GSPC, Waqi, Bitroad, 3gpp-mcp, RADAAR.

## 🆕 August 20, 2026 - Morning Cron Sweep (3 New, 3 Guides)

Morning sweep sourced from chatmcp/mcpso submission issues filed after the overnight cutoff (Aug 20 02:00 through 09:46 UTC) plus both directory homepages. 3 new business-relevant servers found: a Romanian official-registry lead-generation server with contact extraction and domain audits, a self-hosted YouTube research server with local semantic corpora, and a 750M-profile people search with job-change prediction. Skipped: Vital Care Finder (consumer healthcare appointment booking).

### Leadgen MCP ★★ - August 20 (morning)

Romanian business data and lead enrichment for AI agents: official ONRC registry lookup across 4.2M+ firms, director and legal-representative search (diacritic-insensitive), website contact extraction, and WHOIS/DNS/SPF-DMARC domain audits - 4 tools verified live via JSON-RPC probe. Remote at `hermes.adrianhomelab.com/mcp` (no auth, validation phase); registry `io.github.darksider4all/leadgen-mcp`. (MIT) · [Guide →](/hermes/mcp/servers/external/leadgen-mcp)

### tube-bridge MCP ★★ - August 20 (morning)

Self-hosted YouTube research for AI agents: 17 tools for video and channel discovery, timestamped transcripts, comments, playlists, ephemeral frames at exact milliseconds, and private local semantic-search corpora (SQLite + sqlite-vec + local embeddings). 14 tools keyless via `uvx tube-bridge`; optional YouTube API key for 3 tools; Docker and self-hosted HTTP options. (MIT, PyPI v1.1.6) · [Guide →](/hermes/mcp/servers/external/tube-bridge-mcp)

### Xverum MCP ★★ - August 20 (morning)

People search and enrichment across 750M professional profiles: plain-English search by role, seniority, skills, industry, and location, full profile pulls with work history, and Next Move Signal job-change prediction. Hosted remote at `mcp.xverum.com/mcp` with x-api-key header (OAuth in progress); registry `com.xverum/mcp`. (MIT) · [Guide →](/hermes/mcp/servers/external/xverum-mcp)

### Also identified (not catalogued)

GitHub submissions reviewed and skipped this cycle: none beyond the overnight set. mcpservers.org homepage slug skipped: Vital Care Finder MCP (consumer doctor/dentist appointment booking - consistent with the MindMap AI consumer-niche skip).

## 🆕 August 20, 2026 - Overnight Cron Sweep (5 New, 5 Guides)

Overnight sweep sourced from chatmcp/mcpso submission issues filed after the afternoon cutoff (Aug 19 16:03 through Aug 20 02:00 UTC) plus both directory homepages. 5 new business-relevant servers found: SAP analytics market intelligence with citation URLs and day-rate benchmarks, a California Proposition 8 property tax appeal service, the TradeBrite Dutch property and vehicle context pair built on official open registers, and the Taskfolk project-management MCP. Skipped: soccer prediction-market odds, x402 agent-infra tooling, an unpublished npm grant-search package, and consumer/design niches.

### Analytics Legends MCP ★★ - August 20 (overnight)

Hosted read-only market intelligence for the SAP analytics services market: consulting firm directory searchable by country and SAP module, day-rate benchmarks (P25/P50/P75 by geography, stack and seniority with sample sizes), contract radar, and curated market news - every row carrying a `citation_url` and every response stating its population size. Remote at `analyticslegends.ai/mcp`; 14 tools keyless, 6 subscriber. (MIT) · [Guide →](/hermes/mcp/servers/external/analytics-legends-mcp)

### SavePropTax MCP ★★ - August 20 (overnight)

California Proposition 8 property tax appeals from any MCP client: free over-assessment checks against recent comparable sales with estimated annual savings, county form preparation, and a signing link emailed to the homeowner - the agent never handles signatures or money. Keyless remote at `saveproptax.com/mcp`, flat $29 filing fee paid by the owner. (MIT) · [Guide →](/hermes/mcp/servers/external/saveproptax-mcp)

### Dutch Property Context MCP ★★ - August 20 (overnight)

One verified property report per Dutch address, linking nine official open sources (BAG construction year and floor area, energy label, CBS neighbourhood stats, noise and air quality, monument status, schools) with explicit match-confidence and observation-only signals. Free keyless remote at `property-context.tradebrite.nl/mcp`. (MIT) · [Guide →](/hermes/mcp/servers/external/dutch-property-context)

### Dutch Vehicle Context MCP ★★ - August 20 (overnight)

One verified vehicle report per Dutch licence plate from eleven official registers: APK/MOT history with readable defects, odometer verdict, full recall chain with risk and remedy, and severity-sorted buyer signals; theft status deliberately excluded and stated in every answer. Free keyless remote at `vehicle-context.tradebrite.nl/mcp`. (MIT) · [Guide →](/hermes/mcp/servers/external/dutch-vehicle-context)

### Taskfolk MCP ★★ - August 20 (overnight)

First-party project-management MCP mirroring Taskfolk's roughly 180-operation REST API (issues, projects, sprints, comments, agents) with scoped API keys, webhooks, and per-call usage and audit views. Remote at `taskfolk.ai/api/mcp/v1`. (commercial, developer surface on workspace plans) · [Guide →](/hermes/mcp/servers/external/taskfolk-mcp)

### Also identified (not catalogued)

GitHub submissions reviewed and skipped this cycle: Front of Goal Odds Agent (soccer prediction-market data - consistent with the footballcharts and livetennisapi sports skips), Vibes-Coded (x402 pay-per-call agent utilities - consistent with the 402oracle infrastructure skip), Krimskrams Paid APIs (npm package not yet published, mixed grant-search and marketplace-admin scope, x402 wallet setup). mcpservers.org slugs reviewed and skipped: 60fps Design (motion-reference design niche), MindMap AI (consumer mind-mapping), FlightPowers hotel support (thin vendor support surface). mcp.so homepage arrival skipped: CSOAI GSPC measurement (already noted in prior sweeps).

## 🆕 August 19, 2026 - Afternoon Cron Sweep (4 New, 4 Guides)

Afternoon sweep sourced from chatmcp/mcpso submission issues filed after the morning cutoff (Aug 19 10:55 through 16:03 UTC). 4 new business-relevant servers found: an OAuth 2.1 connectivity gateway for 30+ business apps, the official WaveSpeed media-generation server, a pay-per-query real estate data refinery settled in USDC on Base, and a verified multi-source intelligence mesh with signed, source-declared verdicts. mcp.so homepage arrivals were repeats (CSOAI org previously noted; Waqi, Bitroad, FineData, TravelAnimator repeats); mcpservers.org homepage showed no new slugs.

### MCPGRAM MCP ★★ - August 19 (afternoon)

One OAuth 2.1 gateway connecting Slack, GitHub, Google, Salesforce, and 30+ business apps to any MCP client: per-workspace consent, per-user token isolation, and dual paths (OAuth for Claude/Cursor, bearer workspace key for HTTP clients). Remote at `mcpgram-mcp-server.vercel.app/mcp` or stdio self-host. (no license declared) · [Guide →](/hermes/mcp/servers/external/mcpgram-mcp)

### WaveSpeed MCP ★★ - August 19 (afternoon)

Official media-generation server for the WaveSpeed platform: run any image, video, audio, or 3D model on the live catalog with schema introspection, `@path` local-file upload, honest pre-spend price quotes (`unpriced_inputs` disclosure), and balance checks. `npx -y @wavespeed/mcp` with `WAVESPEED_API_KEY`; registry `ai.wavespeed/mcp`. (MIT, 30★) · [Guide →](/hermes/mcp/servers/external/wavespeed-mcp)

### RE Data Refinery MCP ★★ - August 19 (afternoon)

Pay-per-query real estate intelligence: live Zillow listings enriched with county GIS, tax delinquency, sheriff sales, permits, and probate records, scored for flip/wholesale/rental-yield/market-heat across 14 Columbus metro cities. $0.25-$0.50 USDC per lookup via x402 on Base, no subscription. Python stdio/SSE at `github.com/areshms/re-refinery-mcp`. (MIT) · [Guide →](/hermes/mcp/servers/external/re-data-refinery-mcp)

### SYNTHORA MCP ★★ - August 19 (afternoon)

Intelligence agency for AI agents: 30 verified multi-source tools (sanctions screening, crypto market data, prediction markets, maritime chokepoint intel, WHO and macro data) with Ed25519-signed, source-declared verdicts and pay-per-call x402 USDC settlement on Base. Remote at `mcp.hergertsynthora.com/mcp`; browse free, pay per call. (hosted, no key to browse) · [Guide →](/hermes/mcp/servers/external/synthora-mcp)

### Also identified (not catalogued)

GitHub submissions reviewed and skipped this cycle: footballcharts-mcp (sports data - league tables and model probabilities for 93 football leagues; consistent with the livetennisapi consumer-sports skip). Homepage arrival skipped: CSOAI GSPC measurement (csoai-org compliance infrastructure, previously noted in the July 3 scan). Feed repeats already catalogued or previously skipped: Waqi, Bitroad, FineData.ai, TravelAnimator.

## 🆕 August 19, 2026 - Morning Cron Sweep (4 New, 4 Guides)

Morning sweep sourced from chatmcp/mcpso submission issues filed after the Aug 18 evening cutoff (Aug 19 03:07 through 07:45 UTC). 4 new business-relevant servers found: the Misar family of sales, email, and blog-publishing servers plus a local MCP bridge to a 2,000+ model catalog. mcp.so homepage arrivals were all repeats of already-catalogued or skipped servers; mcpservers.org homepage showed no new slugs.

### MisarReach MCP ★★ - August 19 (morning)

Outbound sales from any MCP client: 27 tools for lead list building and qualification, email verification, multi-step multi-channel outreach sequences, deliverability checks, and pipeline review. Optional API key with browser login tool; remote at `api.misar.io/reach/mcp` or `npx -y @misarreach/mcp`. (MIT, free tier) · [Guide →](/hermes/mcp/servers/external/misarreach-mcp)

### MisarMail MCP ★★ - August 19 (morning)

Email operations from any MCP client: 54 tools for transactional sends, multi-step campaigns, contacts and segments, automations, A/B testing, domain warmup, and deliverability audits. Remote at `mail.misar.io/api/mcp` or `npx -y @misarmail/mcp`. (MIT, free tier) · [Guide →](/hermes/mcp/servers/external/misarmail-mcp)

### Misar.Blog MCP ★★ - August 19 (morning)

Blog publishing from any MCP client: 23 tools for articles, series, analytics, comments and reactions, newsletter subscribers, and AI-assisted writing, with readOnly/destructive/idempotent annotations on every tool. Remote at `api.misar.io/blog/mcp` or `npx -y @misarblog/mcp`. (MIT, free tier) · [Guide →](/hermes/mcp/servers/external/misarblog-mcp)

### SandBase CLI ★★ - August 19 (morning)

Local MCP bridge connecting 25 AI client targets to a catalog of 2,000+ AI models and APIs: discovery, schema and pricing inspection, execution with async polling, and per-run cost tracking. `npx -y @sandbaseai/cli connect`. (Apache-2.0) · [Guide →](/hermes/mcp/servers/external/sandbase-cli)

## 🆕 August 18, 2026 - Evening Cron Sweep (5 New, 5 Guides)

Evening sweep sourced from chatmcp/mcpso submission issues filed after the afternoon cutoff (Aug 18 19:22 through Aug 19 01:18 UTC) plus the mcpservers.org homepage. 5 new business-relevant servers found: SEC financial intelligence with insider and 13F tools, keyless spatial answers from Overture Maps, live Austin MLS data, headless form infrastructure, and fail-closed listing verification for commerce agents. The mcp.so homepage carried no new arrivals this cycle (all repeats already catalogued or skipped).

### Profitelligence MCP ★★ - August 18 (evening)

Hosted remote MCP server for financial intelligence on first-party SEC data: seven read-only tools covering market snapshots, company and insider deep dives, multi-signal screening, position health checks, 13F holdings and manager activity, semantic search across filings, and account state. Stateless pass-through design, no trade execution. Streamable HTTP at `mcp.profitelligence.com/mcp` with OAuth 2.1 or API key; free tier. Registry `io.github.profitelligence/mcp-server`. (commercial, free tier) · [Guide →](/hermes/mcp/servers/external/profitelligence-mcp)

### PlaceRoot MCP ★★ - August 18 (evening)

Free, keyless MCP server grounding agents in open map data: place search, geocoding, neighborhood analysis, street-graph routing, and isochrones with 29 tools, anywhere on Earth. MIT, self-hostable via `uvx placeroot` or `npx placeroot`; registry `io.github.chuofringer/placeroot`. (open source) · [Guide →](/hermes/mcp/servers/external/placeroot-mcp)

### Austin MLS MCP ★★ - August 18 (evening)

Live Austin-area MLS listings in any MCP assistant: active listing search by neighborhood, price, beds, and schools, closed-sale comps within a radius, and market stats (median price, inventory, days-on-market) by city, ZIP, or school district. Free remote server at `mls.neuhausre.com/mcp`, updated every few minutes, built by NeuhausRE.com. (free) · [Guide →](/hermes/mcp/servers/external/austin-mls-mcp)

### Fillo MCP ★★ - August 18 (evening)

Headless form infrastructure over MCP: provision a workspace, build and publish forms, and read responses. Forms render natively via `@usefillo/react` and `@usefillo/dom` SDKs instead of iframes; file uploads go browser-direct to customer-owned storage. MIT, remote at `fillo.so/api/mcp` or stdio via `npx -y @usefillo/mcp`; registry `io.github.jacobfunch/usefillo`. (open source) · [Guide →](/hermes/mcp/servers/external/fillo-mcp)

### Live Listing Proof MCP ★★ - August 18 (evening)

Fail-closed listing verification for commerce agents: verify a public product, marketplace, classified, or auction listing against a claim before citing it, returning explicit removed, blocked, unreachable, unsupported, or insufficient-evidence states instead of invented facts. Streamable HTTP MCP at `live-listing-proof.mattskowronis.workers.dev/mcp`, $0.02 USDC per check via x402 on Base, no key. Registry `dev.workers.mattskowronis.live-listing-proof/verify-listing`. (commercial, micropayments) · [Guide →](/hermes/mcp/servers/external/live-listing-proof-mcp)

### Also identified (not catalogued)

GitHub submissions reviewed and skipped this cycle: calibreweb-mcp (personal ebook library, consistent with the freshrss/linkwarden/audiobookshelf media skips), rustpad-mcp (collaborative text-editor dev tool), Saymon RU Data API (Russian-market entity data with x402 micropayments and no license - niche geography), osm-mcp (consumer travel planning, consistent with the TravelAnimator skip), mealie-mcp (personal recipe manager), Polyrama (prediction-market trading research, consistent with the traderspy skip), FeedRecall (memory category saturated after screenpipe and prior memory servers). ABAPilot (SAP ECC MCP, issue #3638) already catalogued. mcpservers.org slugs reviewed and skipped: My AskAI (vendor documentation search, thin surface), a9n9 Deep Research (paid research utility), eCourts India (India-specific legal niche).


---

## 🆕 August 18, 2026 - Afternoon Cron Sweep (3 New, 3 Guides)

Afternoon sweep following the morning run, sourced from chatmcp/mcpso submission issues filed after the morning sweep cutoff (Aug 18 11:54 UTC through 13:33 UTC) plus the mcp.so homepage new-arrivals list. 3 new business-relevant servers found: local-first workflow memory for AI agents from a YC S26 company, managed social-account infrastructure with 91 tools, and AI UGC video-ad generation. mcpservers.org homepage carried no new business-relevant slugs this cycle.

### Screenpipe MCP ★★★ - August 18 (afternoon)

Local-first workflow memory for AI agents: screen, audio, app and meeting context recorded on-device 24/7, exposed to Claude, Codex and Cursor through a searchable MCP server against the local API at localhost:3030. YC S26, 21,061★. stdio via `npx -y screenpipe-mcp`; source-available under the [Screenpipe Commercial License](https://github.com/screenpipe/screenpipe/blob/main/LICENSE.md). See [current plans](https://screenpipe.com/onboarding). · [Guide →](/hermes/mcp/servers/external/screenpipe-mcp)

### TokPortal MCP ★★★ - August 18 (afternoon)

Managed social infrastructure API: real TikTok, Instagram and YouTube accounts created, warmed and operated by human account managers in 16+ countries, with 91 MCP tools for account bundles, video upload and scheduling at scale, analytics, ban lifecycle and webhooks. OAuth 2.1 Streamable HTTP at `app.tokportal.com/api/ext/mcp` or stdio via `npx -y tokportal-mcp`; credit-based. (commercial) · [Guide →](/hermes/mcp/servers/external/tokportal-mcp)

### UnrealUGC MCP ★★ - August 18 (afternoon)

AI UGC video ads from eleven typed MCP tools: browse video models, creators and voices, estimate credit cost before spending, start async generations and poll for output. stdio via `npx -y @unrealugc/mcp` or hosted HTTP at `unrealugc.com/api/mcp`, MIT. (commercial) · [Guide →](/hermes/mcp/servers/external/unrealugc-mcp)

### Also identified (not catalogued)

GitHub submissions reviewed and skipped this cycle: moodle-mcp-server-aql (education-niche LMS, consistent with the Aug 11 Canvas/Moodle skip). Homepage arrival skipped: 3gpp-mcp (telecom specification access for LLMs, engineering niche). Feed repeats already catalogued or previously skipped: Waqi, Bitroad, FineData.ai, Sonar ASO, Lemon.io, TravelAnimator, ListingGood.

Morning sweep sourced from the mcp.so homepage new-arrivals list, chatmcp/mcpso submission issues filed after the Aug 17 evening sweep (Aug 17 evening through Aug 18 07:43 UTC), and the mcpservers.org homepage (no new business-relevant slugs this cycle). 7 new business-relevant servers found: a hosted QuickBooks Online connector with write tools and Canadian coverage, agent-run cold-email infrastructure, a PII-redaction privacy layer with audit logging, an ASO tool suite for both app stores, a GitLab engineering-operations server, Thailand Post shipping for agents, and a 14-server business-math suite.

### Caribooks MCP ★★★ - August 18 (morning)

Hosted QuickBooks Online over MCP with 160+ read and write tools - invoices, payments, bills, journal entries, aged receivables, P&L - covering Canada and the US, where Intuit's official Claude connector is US-only. OAuth 2.1, Streamable HTTP at `caribooks.com/api/mcp`; CA$39 per company/month, free 14-day trial, ledger data passes through and is never stored. (commercial) · [Guide →](/hermes/mcp/servers/external/caribooks-mcp)

### Coldrig MCP (agent-cold-email) ★★★ - August 18 (morning)

Agent-native cold-email infrastructure as 28 MCP tools: buy domains, provision mailboxes, run warmup, launch sequences, handle replies, monitor deliverability. Bearer token remote at `agent-cold-email-api.yaakovscher.workers.dev/mcp` or stdio via `npx agent-cold-email`; sandbox free, live sending $99/month. (commercial) · [Guide →](/hermes/mcp/servers/external/agent-cold-email-mcp)

### Waqi - AI Privacy Layer MCP ★★ - August 18 (morning)

Hosted PII-redaction layer between business tools and AI: Stripe, Xero, CRM, and 13 more connectors fetched read-only, redacted before the model sees anything, with a post-redaction audit log and per-person tokens. HTTP at `waqi.bilazann.com/api/mcp/YOUR_TOKEN`; from £99/month. (commercial) · [Guide →](/hermes/mcp/servers/external/waqi-mcp)

### Sonar ASO MCP ★★ - August 18 (morning)

App Store Optimization for AI agents across iOS and Google Play: keyword research with difficulty and popularity, daily rank tracking, review mining, ASO audits, and revenue estimates - 25 tools on real Apple/Google store data. stdio via `npx -y @sonarapp/mcp`; free rate-limited mode, prepaid credits from $10, Indie $19/month. (commercial, free tier) · [Guide →](/hermes/mcp/servers/external/sonar-aso-mcp)

### GitLab MCP (zereight) ★★ - August 18 (morning)

GitLab engineering operations over MCP: projects, merge requests, issues, pipelines, wiki, releases, tags, and milestones via stdio, SSE, or Streamable HTTP with PAT, OAuth, or read-only auth. 1,898★, `npx -y @zereight/mcp-gitlab`. (open source) · [Guide →](/hermes/mcp/servers/external/gitlab-mcp)

### ProShip MCP ★ - August 18 (morning)

Thailand Post fulfillment for AI agents: create shipments, print PDF labels, track Thai-carrier parcels, and manage orders through ProShip's order-management platform, with in-chat account signup. MIT, Streamable HTTP at `mcp.proship.me/mcp`. (open source) · [Guide →](/hermes/mcp/servers/external/proship-mcp)

### Moltline Studio MCP Suite ★★ - August 18 (morning)

Fourteen audited remote MCP servers for business math: merchant fees and charge-to-net, paste-your-data CSV analytics and A/B tests, business-day/SLA math, and MCP agent governance, plus a supporting eight-server set. Streamable HTTP at `mcp.moltlinestudio.com/<endpoint>`, anonymous free tier. (commercial, free tier) · [Guide →](/hermes/mcp/servers/external/moltline-studio-mcp)

### Also identified (not catalogued)

GitHub submissions reviewed and skipped this cycle: VisionGemma (local single-tool vision OCR - Windows-only, thin surface), otto (0-star paper-trading testbed for auditable agent finance - experiment-stage), 402oracle (x402 attestation infra - consistent with prior x402 skips), opengist-mcp (self-hosted gists - dev tool), livetennisapi-mcp (consumer sports data), traderspy (crypto signals), designesy-org (design-QA dev tool), dsh-verify (browser acceptance testing - dev tool). Feed repeats already catalogued or previously skipped: Bitroad, Lemon.io, ListingGood, TravelAnimator, AuraNet Omni-Oracle Engine, MeshMarket.

## 🆕 August 17, 2026 - Evening Cron Sweep (9 New, 9 Guides)

Evening sweep following the midday run, sourced from the mcp.so homepage new-arrivals list and the chatmcp/mcpso submission issues filed after the midday sweep (Aug 17 afternoon through 23:57 UTC). 9 new business-relevant servers found: rental building intelligence for NYC/LA/Chicago, US federal contracting data, a two-store app portfolio console, pre-flight ad audience validation, an agent marketplace with capped spending, four-marketplace resale research, Atono agile project management, encrypted agent messaging with gated settlement, and persona-voiced content humanization. mcpservers.org homepage carried no new business-relevant slugs this cycle.

### LucidRents Building Intelligence MCP ★★★ - August 17 (evening)

Apartment building intelligence from public records for New York City, Los Angeles, and Chicago, roughly 2 million buildings: violations, 311 complaints, reviews, rents, and landlord portfolio records. Read-only, no auth, Streamable HTTP at `lucidrents.com/api/mcp`; 5 tools. (free) · [Guide →](/hermes/mcp/servers/external/lucidrents-mcp)

### AwardCast MCP ★★★ - August 17 (evening)

Public US federal contracting data for AI agents: open SAM.gov solicitations, agency buying profiles, contractor award history, recompete radar with named incumbents, closing-price ranges by agency and NAICS, and a forecast accuracy scorecard. No auth, Streamable HTTP at `awardcast.ai/mcp`; 8 tools with citable search/fetch URLs. (free) · [Guide →](/hermes/mcp/servers/external/awardcast-mcp)

### StorePilot MCP ★★★ - August 17 (evening)

A whole app portfolio across Google Play and the App Store from one local MCP server: crash and ANR vitals against Google's bad-behavior thresholds, anomaly detections, installs, ratings, earnings, and reviews. stdio via `pip install storepilot`, MIT, Python 3.11+; 34 tools. (open source) · [Guide →](/hermes/mcp/servers/external/storepilot-mcp)

### Inside Ads MCP ★★ - August 17 (evening)

Pre-flight audience validation for products you just shipped: reach, click range, and CPC estimates against a budget, with an explicit no-inventory verdict when no matching ad inventory exists, then landing-page parse and campaign generation on your go-ahead. OAuth, Streamable HTTP at `app.inside.ad/api/mcp`. (commercial) · [Guide →](/hermes/mcp/servers/external/inside-ads-mcp)

### Bitroad MCP ★★ - August 17 (evening)

A marketplace where AI agents buy goods and services under spending caps, with returns and disputes as protocol features. Streamable HTTP at `app.bitroad.ai/api/v1/mcp`, docs at bitroad.ai/docs. (commercial) · [Guide →](/hermes/mcp/servers/external/bitroad-mcp)

### Secondhand MCP ★★ - August 17 (evening)

Search Facebook Marketplace, eBay, Depop, and Poshmark from any MCP client with price, condition, category, size, and color filters; deep-research search/fetch with citable listings. Local npm (MIT) or hosted remote with OAuth at `secondhandmcp.com/mcp`. (free tier) · [Guide →](/hermes/mcp/servers/external/secondhand-mcp)

### Atono MCP Server ★★ - August 17 (evening)

Atono agile project management over MCP: backlog, bugs, sprints, epics, and timeboxes with AI-generated investigation context, plus work-item creation and updates. Docker image `atonoio/atono-mcp-server`, Apache-2.0. (open source) · [Guide →](/hermes/mcp/servers/external/atono-mcp-server)

### xete MCP ★★ - August 17 (evening)

Encrypted agent messaging plus non-custodial Solana settlement where the agent drafts a payment it cannot sign and a separate verify tool proves the draft before a human signs. stdio via `uvx xete-mcp`. (open source) · [Guide →](/hermes/mcp/servers/external/xete-mcp)

### Personhood MCP ★★ - August 17 (evening)

Rewrites AI-generated text to read as human in preset or custom persona voices for LinkedIn posts, cold emails, DMs, and tweets. Hosted, Bearer key, Streamable HTTP at `api.givepersonhood.com/mcp`; free credits then per-generation billing. (commercial) · [Guide →](/hermes/mcp/servers/external/personhood-mcp)

### Also identified (not catalogued)

GitHub submissions reviewed and skipped this cycle: FineData.ai (one-line listing with no tool docs, thin-docs rule), cute-web-scraper (local scraping utility, saturated category), komnet (git-backed coordination for coding agents, dev tool), Booklet (markdown publishing for dev docs), Dizko (city events, consumer), and three personal self-hosted media tools (freshrss-mcp, linkwarden-mcp, audiobookshelf-mcp). Feed repeats already catalogued or previously skipped: ListingGood, Mektup, TravelAnimator, AuraNet Omni-Oracle Engine.

## 🆕 August 17, 2026 - Midday Cron Sweep (11 New, 11 Guides)

Scanned mcp.so Feed (30 newest submissions) and mcpservers.org /all page 1 (newest submissions) - a same-day sweep eight hours after the morning run. 11 new business-relevant servers found: company signal intelligence, a nine-network social publisher with render-accurate previews, two multi-agent coordination layers, a Magento commerce bridge, Taiwan legal research, WhatsApp/Telegram bot operations, Korean market measurements, keyless web retrieval, an agent-fleet CLI adapter, privacy-first short links, and Tenable MSSP orchestration.

### Bounce Watch MCP ★★★ - August 17 (midday)

Company signal intelligence over MCP - 3 million dated events across 39 types (funding rounds, senior hires, office openings, partnerships, named customer wins, certifications, layoffs, distress indicators), each weighted 1 to 10, plus coverage blocks on every response and webhook-pushed standing watches. OAuth 2.1 or `X-API-Key`, Streamable HTTP at `api.bouncewatch.com/api/v1/mcp`; 10 tools, five ready-made workflow prompts, 2,500 free credits, paid from 99 EUR/month. (commercial) · [Guide →](/hermes/mcp/servers/external/bounce-watch-mcp)

### Ravenpost MCP ★★★ - August 17 (midday)

Social publishing across nine networks over MCP - Instagram, TikTok, X, LinkedIn, Facebook, Telegram, Threads, Bluesky, and YouTube - with `preview_post` rendering each post exactly as the network will show it before anything goes live. OAuth or personal token, Streamable HTTP at `api.ravenpo.st/mcp`; 21 tools, workspace-scoping refusal built in, registry `st.ravenpo/ravenpost`. (commercial) · [Guide →](/hermes/mcp/servers/external/ravenpost-mcp)

### Ledgenter MCP ★★★ - August 17 (midday)

The shared work-management office for AI agents - projects, dependency-ordered tasks with atomic leased claims, append-only decisions, a semantic knowledge wiki, and a cross-agent handoff inbox. stdio via `npx @ledgenter/mcp` with a per-actor API key against the hosted service; registry `com.ledgenter/mcp`. (commercial) · [Guide →](/hermes/mcp/servers/external/ledgenter-mcp)

### WisWes Magento MCP ★★ - August 17 (midday)

Magento 2 over MCP - 22 typed tools across catalog, cart, checkout, customer, sales, and wishlist served from the store's own web server at `/mcp`, nightly vector-index catalogue push, tiered auth (catalog public, cart and orders identified). Composer `wiswes/magento-mcp` v1.0.7, GPL-3.0, Magento 2.4.4-2.4.7. (open source module) · [Guide →](/hermes/mcp/servers/external/wiswes-magento-mcp)

### Taiwan Law MCP ★★ - August 17 (midday)

Taiwan legal research against official sources - Ministry of Justice statutes, Judicial Yuan judgments, constitutional interpretations, and Legislative Yuan history, 14 tools with a source URL on every result and an intent-analysis gate. Free, no key, Streamable HTTP at `legaltech.org.tw/mcp`; self-host via npx or Docker. (free) · [Guide →](/hermes/mcp/servers/external/taiwan-law-mcp)

### DOS AI MCP ★★ - August 17 (midday)

WhatsApp and Telegram AI assistants over MCP - projects, prompts, conversations, leads, analytics, and balance through 13 tools with no destructive operations by design and project-scoped keys. Bearer key, Streamable HTTP at `dosai.pro/api/mcp`; OpenAPI spec and llms.txt published. (commercial) · [Guide →](/hermes/mcp/servers/external/dos-ai-mcp)

### Cliometry MCP ★★ - August 17 (midday)

Measured Korean market data - SK Hynix ADR premium, realized leverage multiples for KODEX/SOXL/TQQQ, VIX regime labels, and Korean semiconductor relative rotation, all pre-computed daily with source URLs and as-of dates. No auth, Streamable HTTP at `mcp.cliometry.com`; CC BY 4.0. (free) · [Guide →](/hermes/mcp/servers/external/cliometry-mcp)

### mcp-retrieval ★★ - August 17 (midday)

Keyless web retrieval in Go - parallel DuckDuckGo Lite search, Bing image search, and page-to-Markdown scraping with per-item status semantics and browser-grade TLS fingerprints. stdio or HTTP, MIT, Docker or prebuilt binaries. (open source, free) · [Guide →](/hermes/mcp/servers/external/mcp-retrieval)

### 5dive MCP ★★ - August 17 (midday)

Agent-fleet operations over MCP - file tasks, inspect and message agents, and read the daily standup digest by shelling out to the local 5dive CLI's JSON surface, inheriting its auth and audit log. stdio via `npx @5dive/mcp`, MIT. (open source) · [Guide →](/hermes/mcp/servers/external/5dive-mcp)

### Linkonda MCP ★★ - August 17 (midday)

Privacy-first short links - shorten, bulk-shorten, list, update, and delete with total redirect counts only and no visitor data collected. stdio via `npx -y @veranoapp/linkonda-mcp`; anonymous free tier (10 links, 30-day expiry), persistent links on a paid plan. (commercial, free tier) · [Guide →](/hermes/mcp/servers/external/linkonda-mcp)

### Tenable MSSP MCP ★★ - August 17 (midday)

Tenable MSSP orchestration over MCP - Hexa AI tool runs across child containers behind an explicit allowlist, bulk CVE queries across up to 10 tenants concurrently, CSV finding reports. Python 3.14 stdio, MIT, MSSP Portal admin keys required. (open source) · [Guide →](/hermes/mcp/servers/external/tenable-mssp-mcp)

**Also identified (not catalogued):** Raccha AI (early-access agent utility toolbox - KV storage, FIFO queue, JWT/hash utilities; manifest-only repo with no live tool list, dev infra rather than operator tooling), adb-mcp (Android debug bridge - device-level dev tool), Runemap (ASCII weather-radar maps - consumer utility), Hermitsh Texts (classical literature search - not business tooling), Lodging Decision MCP (travel lodging decision kernel - consumer, unauthenticated alpha). Feed and /all repeats already catalogued or previously skipped this cycle: Lemon.io, ListingGood, TravelAnimator, Roamzy, AuraNet Omni-Oracle Engine, Kaiva Bridge, MobileMRR, Mektup, PDI Bridge, GovTrade, ApexVol, Etincel, CryptoStruct, World Monitor, API Direct, JobYap, Kin, NexusTrade, Snipara, RADAAR, BlazingCDN, Cost Seg Smart, easydocforms, Just Domain, Fakto wFirma.

**Key observation:** The agent-orchestration layer is productizing from both directions in a single day - Ledgenter's durable shared office and 5dive's fleet CLI adapter attack the same stateless-agent problem from hosted-service and local-CLI directions. Second, the honesty-handle pattern keeps spreading: Bounce Watch's coverage blocks (absence must mean something before "quiet" is reported) extend Candor's evidence handles from finance into sales intelligence, and Ravenpost's write-nothing previews apply the approval-gate doctrine to publishing. Third, commerce and compliance are going vertical-specific - WisWes Magento and Taiwan Law both bet that deep coverage of one platform or one jurisdiction beats broad but shallow tooling.

---

## 🆕 August 17, 2026 - Cron Sweep (11 New, 11 Guides)

Scanned mcpservers.org /all pages 1-3 (newest submissions) and mcp.so Feed (30 newest submissions). 11 new business-relevant servers found - a spread across listening, commerce, content, finance, memory, compliance, and operations: intent-based social listening, Amazon AI-readiness scoring, approval-gated short-form content production, a personal-finance workspace with evidence handles, a local-first memory substrate, pay-per-call compliance endpoints, Italian tax tooling, asset management, developer hiring, media generation, and commodities research.

### SnitchFeed MCP ★★★ - August 17

Intent-based keyword monitoring over MCP - 33 tools covering LinkedIn, X, Reddit, Hacker News, and Bluesky with OAuth, Streamable HTTP at `api.snitchfeed.com/mcp`, for sales, marketing, product research, and reporting. (commercial) · [Guide →](/hermes/mcp/servers/external/snitchfeed-mcp)

### ListingGood MCP ★★ - August 17

Amazon AI Recommendation Engine over MCP - free AI-readiness and compliance scoring for listings, A9- and shopping-agent-tuned copywriting for US/UK/EU/JP, and POA suspension rescue. API key, Streamable HTTP at `listinggood.com/mcp`; free tier unlimited checks, paid from $10/mo. (commercial) · [Guide →](/hermes/mcp/servers/external/listinggood-mcp)

### ReelsFarm MCP ★★ - August 17

AI short-form social content over MCP - avatars, product scenes, UGC videos, slideshows, scheduling, and publishing across ~30 tools in seven groups, with Review-mode `confirm_action` gates before any mutation. OAuth or API key, Streamable HTTP at `mcp.reelsfarm.com/mcp`. (commercial) · [Guide →](/hermes/mcp/servers/external/reelsfarm-mcp)

### Candor Finance MCP ★★ - August 17

Personal-finance workspace for AI agents - accounts, balances, transactions, budgets, goals, holdings, and debts, every number carrying freshness, coverage, and evidence handles. OAuth 2.1 with dynamic client registration; Streamable HTTP at `api.candor.money/mcp`; read-only toward banks, no money-moving tools; registered as `money.candor/candor-finance` on the official MCP Registry. (commercial) · [Guide →](/hermes/mcp/servers/external/candor-finance-mcp)

### Exomem ★★ - August 17

Local-first memory substrate for MCP agents - hybrid FTS5 + vector search over your own Markdown/Obsidian vault, governed review queues, evidence and supersession history in plain files, measured at 864 ms across 50,000 notes. AGPL-3.0, `pip install exomem`, self-hosted, no account. (open source) · [Guide →](/hermes/mcp/servers/external/exomem-mcp)

### Invoket MCP ★★ - August 17

68 pay-per-call verification endpoints as typed MCP tools - IBAN validation, sanctions screening, phone validation, French and EU law in force, weather, and medication data - paid in USDC on Base over x402 with non-custodial BYOK signing and per-call/per-session spend caps. stdio via `@invoket/mcp`; discovery-only mode free. (commercial, pay-per-call) · [Guide →](/hermes/mcp/servers/external/invoket-mcp)

### Imperio MCP ★★ - August 17

Italian tax and compliance tooling over MCP - Codice Fiscale, P.IVA, IBAN, ATECO, IVA (reverse charge and split payment), IMU, forfettario, F24, FatturaPA/SDI, INTRASTAT, NIS2 scope, and VIES-live anti-fraud payee verification, all deterministic official algorithms with no LLM inference. JSON-RPC 2.0, stateless, `imperioutils.com/api/mcp`; anonymous and free; registered `com.imperioutils/fisco-it`. (free) · [Guide →](/hermes/mcp/servers/external/imperio-mcp)

### A4B CMMS MCP ★★ - August 17

Asset and maintenance management over MCP - 24 tools covering assets, workspaces, maintenance tasks, users, invites, and QR codes, plus 9 read-only `a4b://` resource templates. OAuth 2.1 + PKCE, multi-tenant, full audit logging; Streamable HTTP at `a4b.ai/mcp`. (commercial) · [Guide →](/hermes/mcp/servers/external/a4b-cmms-mcp)

### Lemon.io MCP ★★ - August 17

Hire vetted senior developers from chat - write job descriptions, prepare technical interviews, and request engineers without leaving the conversation. `github.com/lemon-io/lemon-io-mcp`; no parseable config block published (tools served from the endpoint). (commercial marketplace) · [Guide →](/hermes/mcp/servers/external/lemon-io-mcp)

### ViewMax MCP ★★ - August 17

AI video, image, music, and speech generation over MCP - Sora-class video models via `generate_video`, plus image, music, and speech tools with OAuth (Claude) or API-key auth and credit-based billing. Streamable HTTP at `viewmax.studio/api/mcp`. (commercial) · [Guide →](/hermes/mcp/servers/external/viewmax-mcp)

### Arc Research MCP ★★ - August 17

Commodities research over MCP - knowledge-graph search, CFTC COT positioning with week-over-week flows and oscillators, EIA storage and NOAA/GFS/ECMWF weather, futures quotes, and private stories/journals. Bearer token included with Arc Research Starter; Streamable HTTP at `getarcresearch.com/mcp`; registry name `com.getarcresearch/arc-research`. (commercial, subscription) · [Guide →](/hermes/mcp/servers/external/arc-research-mcp)

**Also identified (not catalogued):** Kashif by BottleTech (free 0-100 website audit scoring SEO/AI-readiness/mobile speed - agency lead funnel with no published MCP endpoint or tool list; GOJI-class skip), Marian Coach Mentoring AI (one-person engineering-coaching sales agent - personal sales surface, not operator tooling), Claix (AI document extraction - REST API docs page with no MCP endpoint or tools; thin-docs rule), YourImageShare MCP (free image/video hosting upload/list/delete - consumer utility), Roamzy (crypto-paid eSIM - consumer), TravelAnimator (travel videos - consumer), AuraNet Omni-Oracle Engine (repeat - REST-first x402 oracle pack already evaluated and skipped Aug 16 night), a Chinese raw-IP listing (shenshaoyin, endpoint on 121.40.18.232 - junk signal, repeat). Feed and /all repeats already catalogued or previously skipped this cycle: Kaiva Bridge, MobileMRR, Mektup, PDI Bridge, GovTrade, ApexVol, Etincel, CryptoStruct, World Monitor, API Direct, JobYap, Kin, NexusTrade, Snipara, RADAAR, BlazingCDN, Cost Seg Smart, easydocforms, Just Domain, Fakto wFirma, FARPY, CoinLobster, EM+x, Mercopilot, DreamThreads, MagicSlides, Wapiworld, Agent Utility, Ignatius, ctxt.io, APITube, Legalcode, Lumail, MainBook, Studex, Croncool, Import.io, Tutorializer, Daily Studio, Datadog, Loops, a trycloudflare host-dump slug, Pixero, Routebase, Seomely, WEM Price Compare, Polyblog.

**Key observation:** The approval-gate pattern is now the default across three distinct domains - ReelsFarm's Review-mode `confirm_action` on publishing, Candor's permission-only workspace changes, and Invoket's pre-signature spend caps all encode the same doctrine CorpusIQ ships natively: the agent proposes, the human confirms, the audit trail records. Second, evidence-handle design is spreading from financial data into memory - Candor's freshness/coverage handles and Exomem's file-native evidence and supersession history both make the record distinguishable from the conclusion. Third, AI-readiness has become a service category of its own: ListingGood scores listings for Amazon's AI and shopping agents the way Seomely scores pages for Google indexation.

---

## 🆕 August 16, 2026 - Daily Cron Sweep (9 New, 9 Guides)

Scanned mcpservers.org /all pages 1-3 (newest submissions) and mcp.so Feed (30 newest submissions). 9 new business-relevant servers found - the largest single-day sweep since August 15 morning: agent-owned email mailboxes, a hosted scraping engine from an established data vendor, the official Lumail email-marketing MCP with confirmation gates, a Shopify + Google Ads operating bridge, free legal research across 44 jurisdictions, bank-statement conversion, presentation generation, news intelligence, and auto-expiring share links.

### Mektup MCP ★★★ - August 16

Email infrastructure for AI agents - register domains, create mailboxes, send and receive mail, and manage threads, drafts, and folders through 41 tools. A real inbox, not a one-way sending API. Remote Streamable HTTP at `mcp.usemektup.com/mcp` with a Bearer token (`mek_live_...`); MIT, `github.com/WeeCi/mektup-mcp`. (commercial) · [Guide →](/hermes/mcp/servers/external/mektup-mcp)

### Import.io MCP ★★★ - August 16

Hosted web scraping from an established data vendor (Import.io, Aperture pricing intelligence) - render pages in a real browser, extract structured fields, capture screenshots, with proxy routing, country targeting, and CAPTCHA handling. OAuth or Bearer key, Streamable HTTP at `mcp.import.io/mcp`. 10,000 free successful calls, then $0.0002 per successful call with a monthly spend cap; blocked and failed requests never billed. (commercial) · [Guide →](/hermes/mcp/servers/external/import-io-mcp)

### Mercopilot MCP ★★★ - August 16

Shopify store + Google Ads account over MCP - plain-English questions about revenue and ad spend, a ranked fix list with estimated value per fix, and approval-gated changes applied directly in Shopify or Google Ads. OAuth, no API key, Streamable HTTP at `api.mercopilot.com/mcp`; 9 tools. (commercial) · [Guide →](/hermes/mcp/servers/external/mercopilot-mcp)

### Lumail MCP ★★★ - August 16

Official Lumail email-marketing MCP - subscribers, campaigns, graph-based Workflows, tags, segments, and analytics over dual endpoints: an OAuth catalog that cannot send, publish, or delete, and an API-token catalog with every high-impact action behind a five-digit, single-use confirmation code. `lumail.io/mcp` (OAuth) · `lumail.io/api/mcp/sse` (token). (commercial) · [Guide →](/hermes/mcp/servers/external/lumail-mcp)

### Legalcode MCP ★★ - August 16

Free legal research over MCP - statutes, case law, and regulatory guidance across 44 jurisdictions with 299 packaged legal skills (NDA review, DPIA generation, contract analysis). Searches processed, never stored; EU-hosted. No API key on the free tier (30 requests/day); Pro $25/mo. `mcp.legalcode.md/mcp`. (commercial, free tier) · [Guide →](/hermes/mcp/servers/external/legalcode-mcp)

### MainBook MCP ★★ - August 16

PDF bank statements to checked Excel, CSV, or JSON with balance validation - 5 tools (`convert_bank_statement`, `get_conversion`, `list_conversions`, `get_balance`, `output_folder`), folder-scoped local access, no account-mutation tools. Local stdio via `uvx mainbook-mcp` with a `MAINBOOK_API_KEY`; 1 page = 1 credit, 20-page signup grant. (commercial) · [Guide →](/hermes/mcp/servers/external/mainbook-mcp)

### MagicSlides MCP ★★ - August 16

Presentations, documents, spreadsheets, and meeting notes from chat - 70+ templates, hosted share links, an editor, and PPTX/PDF export, with agentic in-place revision of existing docs. No API key (account sign-in); early access free. (commercial) · [Guide →](/hermes/mcp/servers/external/magicslides-mcp)

### APITube News MCP ★★ - August 16

News intelligence over MCP - 500,000+ sources in 60+ languages filtered by sentiment, entities, topics, and source quality. Hosted JSON-RPC at `mcp.apitube.io/` with a Bearer key; `search_news` + `suggest` tools and four ready-made prompts (`monitor_company`, `topic_sentiment`, `breaking_news`, `compare_coverage`). (commercial) · [Guide →](/hermes/mcp/servers/external/apitube-news-mcp)

### ctxt.io MCP ★★ - August 16

Auto-expiring share links for agent output - diffs, logs, reports, and self-contained HTML (inline CSS/SVG, scripts stripped) with `read_context` and token-authorized deletion. Stateless, no auth, free up to 1-day TTL; $1 per 30-day Pro link with an ACP programmatic-checkout path via Stripe Shared Payment Token. `ctxt.io/mcp`. (freemium) · [Guide →](/hermes/mcp/servers/external/ctxt-io-mcp)

**Also identified (not catalogued):** DreamThreads DreamGraph (dream-thread consumer novelty - unclear niche), Croncool (cron scheduling for developers - dev tool), Studex Portal (education/study portal - education niche per Aug 11 decision), Tutorializer (docs-to-tutorials - dev content utility), Wapiworld (one-line listing, no MCP depth), Agent Utility (Cloudflare workers.dev exposed-port listing - host-dump class), FDE Lessons API (education). Feed repeats already catalogued or previously skipped this cycle: GovTrade, ApexVol, Etincel, CryptoStruct, World Monitor, API Direct, JobYap, Kin, NexusTrade, Snipara, RADAAR, BlazingCDN, Cost Seg Smart, easydocforms, Just Domain, Fakto wFirma, FARPY, CoinLobster, EM+x, SceneF, LabTestSuperstore, Prose Coach, Clipkit, CR8 Agent Commons, x402 Merchant Check, directree, WEM Price Compare (repeat of the Aug 15 morning skip - consumer/affiliate). Page 3 of /all carried only repeats (hermoso, holoweave, polymarketscan, graspi, shhots, markupbase, helpdocs, teai, waldo, customer-tiering, emx, folklore).

**Key observation:** The email category went from gap to crowded in 48 hours - Loops (Aug 15 morning) added execution, Mektup adds agent-owned inboxes, and Lumail ships the most complete confirmation-gate implementation documented yet with dual safety profiles. Second, established web-data vendors are entering MCP directly - Import.io's hosted scraping engine with per-call pricing and spend caps extends the vendor-first-party pattern from observability and email into data acquisition. Third, commerce operations gained its first approval-gated store + ads bridge (Mercopilot), pairing with the RADAAR/OnePostly social layer toward an agent-addressable commerce stack with human approval at the write path.

---

## 🆕 August 16, 2026 - Evening Cron Sweep (2 New, 2 Guides)

Scanned mcpservers.org /all pages 1-3 (newest submissions) and mcp.so Feed (30 newest submissions). 2 new business-relevant servers found - verified-revenue mobile app acquisition data with a live valuation model, and a hosted database-to-MCP gateway with per-tool access control and audit logging.

### Kaiva Bridge MCP ★★ - August 16 evening

Hosted database-to-MCP gateway - point it at any Postgres database or OpenAPI spec and get a secure, hosted MCP endpoint with per-tool access control and every call written to an audit log. Schema read, typed tools generated; no server to write, nothing to host. The listing is a live read-only demo of a synthetic commerce dataset (6 tools: `list_products`, `get_order`, `get_product`, `list_customers`, `list_orders`, `get_inventory`). Streamable HTTP at `api-demo.kaiv.ai/api/bridge/mcp/commerce-demo`; create your own at `kaiv.ai/bridge`. (commercial) · [Guide →](/hermes/mcp/servers/external/kaiva-bridge-mcp)

### MobileMRR MCP ★★ - August 16 evening

Mobile app acquisition marketplace data over MCP - search and filter listings by MRR, asking price, category, and platform; compare candidates on price, profit multiple, and verification status; view provider-backed revenue (direct RevenueCat/Superwall connections, not self-reported screenshots); estimate valuations with a live model. 5 tools (`search_listings`, `get_listing`, `get_leaderboard`, `compare_listings`, `estimate_valuation`), no auth, Streamable HTTP at `mobilemrr.com/mcp`. (commercial, free) · [Guide →](/hermes/mcp/servers/external/mobilemrr-mcp)

**Also identified (not catalogued):** Feed and /all repeats already catalogued or previously skipped this cycle: Ignatius The Younger AI slug resolves to FDE Lessons API (education - repeat of the Aug 16 daily skip), WEM Price Compare (repeat of the Aug 15 morning skip - consumer/affiliate), Presidential Agenda trycloudflare slug (host-dump noise). AIO.GEO confirmed already catalogued with guide (Aug 15 morning).

**Key observation:** Verified-revenue marketplaces are now MCP-addressable - MobileMRR extends the marketplace-data pattern to mobile apps with provider-backed verification and a live valuation endpoint, the first acquisition-marketplace server in the catalog. Second, Kaiva Bridge lands on the agent-governance segment the Aug 13 evening sweep flagged as fastest-growing: per-tool access control plus a full audit log turns "give the agent your database" from a credentials handoff into a scoped, audited connection.

---

