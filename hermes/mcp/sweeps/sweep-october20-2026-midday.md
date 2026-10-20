---
title: "MCP Server Discovery - October 20, 2026 (Midday Sweep)"
description: "Midday delta cataloguing a full contract-lifecycle server and a sixteen-million-document investment research library, each verified against its live endpoint."
last_updated: 2026-10-20
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october20-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 20, 2026 (Midday Sweep)

Midday delta roughly seven hours after the night capture. The mcp.so `/feed` page 1 returned 26 server cards, of which three were posted inside the window (fynk at 15:45Z, CitySignal AI at 13:16Z and Scento at 10:39Z) and the rest carried dispositions already recorded on October 19 and 20. mcpservers.org `/all` pages 1 to 3 served 90 cards through the r.jina.ai reader proxy, and cross-referencing those slugs against the catalog headings, the on-disk guide directories and the prior sweep prose left two candidates worth evaluating rather than the 15 that a naive slug check called new.

Two entries were catalogued. The pattern this cycle was narrow and specific: both are document libraries that a business already pays for in some other form and that an agent could not previously reach at all.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [fynk MCP](/hermes/mcp/servers/external/fynk-mcp/) | Productivity | Hosted server at `https://app.fynk.com/mcp` for fynk, an EU-hosted contract management platform, and the first full contract-lifecycle entry in this catalog rather than an e-signature point tool. The tool surface runs the lifecycle in both directions: list and read documents, pull the latest signed PDF, create a document from a template, from scratch or from an uploaded PDF, copy an existing one, archive and restore; build templates with parties, dynamic fields and signature blocks; add and remove parties and signatories; move a document through draft, review, signing and done with `workflow_state` reporting every blocker including who still has to approve; and configure the account's own playbooks, checkpoints, teams, tags, document types and metadata fields, where a custom type carries the prompt that decides whether future AI analyses populate it. Verified: unauthenticated `POST initialize` returned HTTP 401 `{"message":"Unauthenticated."}`, so the connection signs in through OAuth 2.0 on the vendor's EU infrastructure and the agent inherits the user's role and document permissions with no elevated path. The mcp.so tool listing enumerates 68 tools while the vendor integration page advertises 47 and its help centre says the set is still expanding. Available on Essential, Business and Pro, testable in the free trial. |
| [ReportGem MCP](/hermes/mcp/servers/external/reportgem-mcp/) | Finance | Hosted server at `https://www.reportgem.com/mcp`, registered as `com.reportgem/global-research`, over 16 million global investment bank reports (Goldman Sachs, Citi, HSBC, UBS, JPMorgan, Morgan Stanley, Barclays, Nomura, with same-day realtime coverage and Chinese titles and translations), 5 million plus reports from 200 plus Chinese brokers and futures houses, 500,000 plus China company filings, SEC filings across 10-K, 10-Q, 8-K, 6-K and 20-F, earnings-call notes, academic papers and the charts and tables inside the reports. Five tools - `search_research`, `search_filings`, `search_meetings`, `search_visuals` and `get_evidence` - and the server's own instructions state the citation contract: prefer `get_evidence` before a material or numeric claim, always preserve the source URL and page reference, never present a no-match document as verified evidence. Verified: unauthenticated `POST initialize` returned HTTP 200 and `tools/list` returned exactly those five tools; reads need an OAuth login, with 10 free credits (about 100,000 returned tokens, 30 days) and metered billing at one credit per 10,000 returned tokens, titles and URLs and empty results free, packages at ¥169 for 400 through ¥499 for 3,000 and no auto-renewal. |

## Held, With Reasons

- **CookieYes** (official, consent management for 1.5 million plus sites, cookie scans and GDPR and CCPA settings) - the consent-management class is covered by the catalogued **ConsentStack MCP** (22 tools, GDPR and CCPA cookie consent end to end), and the privacy and legal class by the catalogued GDPR deadlines entry.
- **Cowboy MCP** (free self-hosted WordPress server, up to 203 tools behind two gateway tools, WooCommerce, per-change undo) - the WordPress class is covered by the catalogued **WordPress MCP** entry from July 15.
- **CitySignal AI** (live road, transit, weather, power and water signals for 13 US cities, week of memory, road cameras) - the city-data slice is covered by the catalogued German city-data server (weather, transit, energy, air quality, 38 tools) plus the locality verticals already recorded as held.
- **Status Is Down** (read-only outage intelligence over 13,500 services, six tools) - already dispositioned on October 19 against the uptime class carried by RealUptime, Healthchecks and PingCheck.
- **OptimistFi** (perpetual futures funding and open interest on 40 venues, liquidation levels, 21 prop firms, sourced theses on 6,100 US stocks) - the perpetuals and trading class is covered by Papertrade AI and the equity-research slice by fAlpha, Alpha Vantage and Horizon Insights.
- **Tokenaissance** (a personal agent for quant and research investment) - the quant and backtest class is dense in this catalog (portfolio analytics, screeners, backtests, DCA backtesting, conformal forecasts).
- **Atwork** (tasks, sheets, rows, comments and pages as agent-writable workspaces), **GanttFather** (27 tools, OAuth), **Velocity** (AI-centric project management) - the project and work-management class is carried by Taskade, Monday, Trello, Taskpend and the catalogued task boards.
- **AEO Inspector**, **Searcherries: AI Visibility and SEO**, **SiteDoctor** (website health, SEO and security scan) - the AEO and SEO scoring class has been saturated since Ranki, geolint, LogNorm and the Creavores AEO Audit catalogued on October 20 night; SiteDoctor adds security headers to a scan class already represented.
- **Kirat Multi Model AI Council**, **AgentLeak**, **drift mandate gate**, **Pinafly UAT**, **Castov**, **PDFOven**, **FlowX**, **rostrum**, **Animation Machine**, **AgentBank**, **mercadopleis**, **Chargezen SmartyTap**, **RedirX**, **Product Page Extractor**, **Elementor MCP Createur**, **check.tattoo**, **Founden** - carried dispositions from October 19 and 20, with drift already catalogued.
- **Scento Perfume Compendium**, **10ML Perfume Finder**, **botchelor**, **Paprika3d**, **appcreator24** - novelty and dev-utility classes, no business data source.

## Sources

- mcp.so `/feed` page 1, 26 server cards with `slug`, `name`, `tagline`, `categoryName` and exact `createdAt` timestamps read from the TanStack Router payload
- mcpservers.org `/all` pages 1, 2 and 3 through the r.jina.ai reader proxy, 90 cards parsed with names, categories, descriptions and logo URLs
- Vendor documentation for both catalogued entries: the fynk integration page, help centre article 759041 and product blog, and the ReportGem detail page with its tool table, pricing table and setup recipes
- Live probes: HTTP `initialize` against `https://app.fynk.com/mcp` (401 unauthenticated) and against `https://www.reportgem.com/mcp` (200), plus `tools/list` on ReportGem returning five tools
- Cross-reference against the catalog headings, the on-disk guide directories and every prior sweep section, including the October 16 to 19 disposition prose

## Listing Status Check

- mcpservers.org `/servers/corpusiq-io` - live, page title and brand content returned through the reader proxy
- mcp.so - not listed; the four slug forms (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) all return 404 and the directory remains in its recorded quarantine, so no resubmission
- Smithery - live at `Cprusiq`
- Glama - listed under `io.corpusiq/multi-source-mcp`; the tool-description quality grade is already escalated to the engineering owners, so no submission action this cycle
