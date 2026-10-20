---
title: "MCP Server Discovery - October 20, 2026 (Midday Supplement)"
description: "Supplement sweep working the unrun issue window: a municipal financial statement library and a keyless breach-intelligence surface, both probed live."
last_updated: 2026-10-20
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october20-2026-midday-supplement/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 20, 2026 (Midday Supplement)

A supplement about an hour after the midday capture, and the useful part of it was not the directory front pages. The mcp.so `/feed` carried two cards posted after the midday snapshot (KissCode and Workspace369, both at 17:26Z), and mcpservers.org `/all` page 1 was unchanged. The real gap was elsewhere: the last two passes both recorded the chatmcp/mcpso issue window as not run, and the window had been closed at #5712 on the October 18 night sweep. Ninety-four submissions had arrived since, and they produced both entries below.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [MuniSpot MCP](/hermes/mcp/servers/external/munispot-mcp/) | Finance | Hosted server at `https://www.munispot.com/api/mcp` over standardized municipal financial statements for 21,000+ US municipalities and 64,700+ fiscal-year reports across 50 states, plus a MuniScore rating with a factor breakdown and per-municipality economic indicators. Six tools: `search_municipalities` (filters including fund balance percentage and score band), `get_municipality`, `get_financials`, `get_scores_history`, `compare_municipalities` and `get_economy`. Verified: unauthenticated `POST initialize` returned HTTP 401 `{"jsonrpc":"2.0","error":{"code":-32000,"message":"Missing API key ..."}}`, so the connection is an `X-API-Key` header (or a bearer token) rather than OAuth. Access ladder read from the vendor's own pages: the free API tier is 100 calls a month at 20 a minute and 100 a day against core endpoints only (entities, profiles, scores); the dashboard trial is 14 days with no card; analyst plans run $6,990 and $19,990 a year; full MCP access including statements, ACFR line items and every fiscal year sits under the Professional and Enterprise API plans, quoted on contact. Registry `com.munispot/municipal-data`, npm `@munispot/mcp`. **Catalog gap closed:** the government data in this catalog was the money going out (GovContractRadar, GovContractScout, GovTrade, SAM.gov and Acquisitions.gov); none of it was the money already committed, which is what a solvency question needs. |
| [XposedOrNot MCP](/hermes/mcp/servers/external/xposedornot-mcp/) | Security and Intelligence | Keyless remote server at `https://api.xposedornot.com/mcp` over a breach index: 794 breaches, 11,717,004,638 exposed records, a separate paste index, last breach added 2026-10-14. Verified by execution rather than by reading: unauthenticated `POST initialize` returned HTTP 200 (`XON_MCP`, "XposedOrNot Breach Intelligence", version 2.0.0), `tools/list` returned six tools (`check_email_breaches`, `get_breach_analytics`, `list_breaches`, `domain_breach_summary`, `get_breach_metrics`, `get_recent_breaches`), and a live `tools/call` to `get_breach_metrics` returned the counts quoted here. The tool that earns the entry is `domain_breach_summary`: breach count, affected accounts, pastes and trend for a whole domain, which turns a per-address errand into vendor due diligence. Read-only, no key, no account, free. **Catalog gap closed:** the breach-check class existed only as one of nine tools inside OpenOSINT MCP, which queries HaveIBeenPwned with an operator-supplied key one address at a time; there was no dedicated breach-intelligence surface and no domain aggregate at all. |

## Held, With Reasons

- **KissCode** (skill for agents to join a relationship network where agents and people meet) and **Saloon** (agent social network for dating, hiring and intros) - the agent social network class is a recorded disposition, held on the KissCode ruling and cited again by the Saloon hold on October 13.
- **Workspace369** (all-in-one app for agencies, freelancers, consultants and service teams: clients, work, invoices over Streamable HTTP with OAuth) - a single-vendor business-app connector, the Kasar CRM, TeamShift and Taskhold class. The product is a competitor surface, not a data source.
- **Lebanese Legislation** (laws, articles, court rulings and the Official Gazette in Arabic and French, verbatim, keyless, registry `com.lebaneselegislation/mcp`) - the regional legal class is one of the densest in this catalog (Corpus Law, LEGAION, aka-recht, Zitierfest, with NyayAssist held). A new jurisdiction is a coverage variant, not a class.
- **Howseen** and **Searcherries** (AI answer visibility across ChatGPT, Gemini, Perplexity, AI Overviews) - AEO and visibility scoring have been saturated since Ranki, geolint and LogNorm, with the Creavores AEO Audit catalogued on the October 20 night sweep.
- **MetricDuck** (SEC filings, XBRL facts, full-text EDGAR search, sector-normalized peer comparison, stock screening; keyless initialize 200) - the equity data class is carried by fAlpha, Alpha Vantage and Horizon Insights, and ReportGem was catalogued this same day for the sell-side library behind the numbers.
- **Chorus** (Meta, Google Ads and LinkedIn campaign planning with confirm-cards and paused-by-default launches) and **Duchamp** (ad research over curated running ads) and **Adflipr** (Shopify and WooCommerce email marketing) - ad operations and advertising intelligence classes, covered by PaidSync and OpenAdLibrary, with the e-commerce email class carried by the ESP connectors.
- **Finch Agent Marketplace**, **Needhave**, **ribcage-agent-services** (verification and research desk) - agent-to-agent marketplace and services boards; the agent-commerce class per steward-mcp, WHP Standing and the Saloon ruling.
- **PostData** (`api.postdata.cloud`, keyless, six tools under device names such as `publish_reading`, `get_history`, `wait_for_reading`) - IoT sensor telemetry keyed by public device name. No business data source behind it.
- **TidyData Tools** (public holidays, business days, ECB currency conversion, time zones, sunrise, DNS/WHOIS, keyless) - commodity lookup utilities, the class carried by the time, calendar and DNS utility holds.
- **Terminal Tax** (hosted 2025-original-return filing, no auth), **Instant DSCR Term Sheet** and **Instant Fix-and-Flip Term Sheet** (written term sheets for business-purpose loans, no auth), **DIVID Planner** (savings plan against market scenarios), **Venly Finance** (stablecoin settlement, reads real data, writes mock-only) - single-purpose financial utilities, one narrow output each. The tax and lending document classes are carried by boomtax, Taxley and ai2fin-tax.
- **DeviL** (matches software already built against Italian SMEs that may need it), **Leadbase**, **Verified.net** (email and contact verification), **Mobile Phone Waterfall**, **Agent to Brokerage Resolver**, **AppTrack Ninja** (App Store charts and ASO keyword tracking) - B2B matching, contact enrichment and app-market data. Contact enrichment is a recorded commodity class since the MailTester trio, and the mambalabsdev fleet that carries several of these has its standouts catalogued.
- **MuniSpot's neighbours in the window**: **Cookie Consent Audit**, **WCAG Accessibility Audit** and the **Google Ads Transparency Monitor** from the same mambalabsdev batch - the consent and accessibility audit classes are dense, and the ads-transparency slice is carried by OpenAdLibrary.
- **CloudCorpRecords fleet** (prwatch, greenlight, claimcheck, gatefile, agentmail) - contribution-workflow utilities plus an agent mailbox; the agent email class is saturated per Mektup, Voidmail and Mailows.
- **Browser and automation utilities**: Waldo (macOS accessibility tree, Apache-2.0), Monito (plain-English browser tests), optics-framework (Android, iOS, TV, web and BLE automation), Rush (cloud sandbox agent runs), cloneproof, accesslumens, Artifact Publisher - developer and QA tooling, the class of the browser-automation and dev-utility holds.
- **Memory and knowledge utilities**: Synaplan (self-hosted RAG workspace), sqlite-graph-memory, bantamkit, claude-code-memory-skill, Squirrel Brain, Screvi - local agent memory and reading libraries, the class of alethech and the catalogued Agentic Memory MCP plus Linksee.
- **Media and content generation**: Creatify Ad Agent, Levea, Stivio, cuttingfloor, Shotkiln, Voidless, SlickFast, rostrum - the media-generation class, which is the most heavily represented in this catalog.
- **Uptime and monitoring**: Fettle, OpenUptime, Status Is Down - the uptime class carried by RealUptime, Healthchecks and PingCheck.
- **Regional and niche data**: K-Stock (Korean equities and OpenDART), MedicineData (Chinese medical data), AI Guanchao News, Trench Report and Grey Ridge Signals (Solana and Base on-chain), FrontRowTickets, Home Renovation Free Tools, 9bot (WhatsApp community management), NeverApply and ApplyKoala (job search), Offhand, Briefflink (German paper letters) - geo-niche and consumer verticals, plus two crypto trader utilities.
- **Developer tooling remainder**: Stratigraph, RepoLens, DevSpeak, DVERA, Rowsmith, lakeboard-converter, Tupana, Multi Calendar, SuperMailOS, MailBeast, Mailows, XposedOrNot's neighbour Compass DaaS (an update request, not a listing) - thin or class-covered, no business data source.

## Sources

- chatmcp/mcpso issue window **#5713 to #5816** (94 submissions after the #5666 to #5712 window closed on the October 18 night sweep), read through the authenticated GitHub issues API in three paginated calls with bodies included
- mcp.so `/feed` page 1 (30 cards, two posted after the midday capture at 17:26Z) and the mcp.so detail page for `workspace369`
- mcpservers.org `/all` page 1 through the r.jina.ai reader proxy (30 cards, no change against the midday capture)
- Vendor documentation for both catalogued entries: the MuniSpot MCP server page, pricing page, tool list and registry entry, and the XposedOrNot issue body and live tool surface
- Live probes: HTTP `initialize` against `https://www.munispot.com/api/mcp` (401, missing API key) and `https://api.xposedornot.com/mcp` (200), `tools/list` on XposedOrNot (six tools), and `tools/call get_breach_metrics` on XposedOrNot returning the catalog counts
- Cross-reference against the on-disk guide directories (1,097 before this sweep), the sweep index and every prior sweep section, with class-term greps for municipal finance, breach, procurement, app-store data and tax before any disposition

## Listing Status Check

- mcpservers.org `/servers/corpusiq-io` - live, unchanged
- mcp.so - still quarantined; the four slug forms return 404, so no resubmission
- Smithery and Glama - not re-probed this pass (probe set owned by the night sweep), no change expected

## Not Run

- The twelve-sitemap canonical refresh: the night sweep owns it, and this pass added no new canonical capture
- mcpservers.org `/all` page 4: no signal on pages 1 to 3 justified the read
