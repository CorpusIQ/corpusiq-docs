---
title: "MCP Server Discovery - November 4, 2026 (Night)"
description: "Night sweep: two keyless finance surfaces driven end to end, a 191-entry ingestion wave dispositioned by class, and 12 endpoints probed."
last_updated: 2026-11-04
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november4-2026-night"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 4, 2026 (Night Sweep)

## Summary

Five hours after the evening pass, and the shape of this window was different from the last three. The submission window carried twelve items, the mcp.so `/feed` turned over by ten, and mcpservers.org took the wave nobody had dispositioned: an **ingestion of about 191 entries** between the evening pass's read at **19,148** and this pass at **19,342**, most of it a single-vendor documentation fleet and a batch of author-handle submissions.

The canonical read settles when that wave landed. The twelve-sitemap refresh returned **19,305** server URLs, and the **19,339**-line capture taken at 22:02 the same night contained every one of them: the set difference is **zero additions and 34 removals**, and those 34 are the priority-sitemap slugs (`github-mcp-server`, `slack-mcp-server`, `notion-mcp-server` and siblings) that the server sitemaps do not carry. So the wave arrived between the evening read and 22:02, and no new server has entered the sitemaps in the five hours since.

Two arrivals earned guides and both were driven without a credential. **ExitValue.ai M&A Multiples MCP** answers what a private business in one of 106 industries sells for, with the deal count behind every median. **AllClear Lending MCP** names the institutions funding a business by industry and state, with a source page per program and a published ladder for what to do after a decline. Both are finance surfaces where the catalogue previously held either public-market data or rate benchmarks, and neither angle was covered.

The reading rule this pass is about what a wave is worth. About 191 entries arrived and one of them, plus one from the submission window, was worth a guide. The wave is not noise to be counted, and it is not a cohort to be catalogued item by item either: it decomposes into vendor documentation routes, official first-party connectors that duplicate what a client already holds, and vertical utilities. Each of those has a precedent already in the catalogue, and the disciplined answer is one grouped disposition line rather than 190 entries.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included, one call | **12** submissions **#6707** to **#6718**, none read by the evening pass, which closed at **#6706** |
| mcp.so `/feed` | direct fetch with a browser UA, `createdAt` timestamps parsed | **28** cards, newest `2026-11-04T09:41:03Z`, ten cards dated after the Integrate.io card the evening pass catalogued |
| mcpservers.org `/all` | r.jina.ai, pages 1 to 7 | counter **19,342** against **19,148** at the evening read, **201** unique slugs across seven pages, **191** with no prior disposition |
| mcpservers.org twelve-sitemap canonical | direct fetch, 12 sitemaps, locale prefixes auto-stripped | **19,305** server URLs against **19,339** in the 22:02 capture, **0** additions and **34** removals, all 34 being priority-sitemap slugs |
| Endpoint probes | keyless `initialize` plus `tools/list` | **12** endpoints, **4** answering **200** (exitvalue-ai **1.1.0**, allclear-lending **0.1.0**, dilutionscan-mcp **0.19.0**, shibasim **1.0.0**) and **8** answering **401** |

## New Servers Catalogued

### ExitValue.ai M&A Multiples MCP - What an Industry Sells For

Relevance: HIGH. **Tier 1, driven** (`initialize` **200** as `exitvalue-ai` **1.1.0**, `tools/list` returning all **4** tools, three of them called).

The catalogue had two adjacent surfaces and neither answered this question. [ROIC.ai MCP](/hermes/mcp/servers/external/roic-ai-mcp-server/) prices public companies with a ticker and 60,000 of them; [DFX Intelligence MCP](/hermes/mcp/servers/external/dfx-intelligence-mcp/) reads private credit exposure off BDC filings. What neither holds is the transaction price of a private business in a named line of work, which is the number an owner asks for and the number nobody publishes outside a paywalled database.

ExitValue publishes it, and the response shape is better than the prose. `list_industries` returns **15** verticals with **106** sub-verticals, each with the bracketed id a caller must pass. `get_valuation_multiples` for HVAC returned **EV/EBITDA median 9.6x** with a middle 50% of **8.4x to 14.8x** on **n=11**, and **EV/Revenue median 0.95x** at **0.60x to 2.20x** on **n=13**, over **14** disclosed transactions with a median deal size of **$135 million**. `compare_industries` on dental, HVAC and SaaS returned **11.0x** (n=80, middle 50% **7.17x to 14.0x**), **9.6x** (n=11) and **14.66x** (n=414, middle 50% **8.7x to 25.31x**), with the full sample returned as **1,560** disclosed transactions.

The refusal is what makes the numbers usable. `get_multiples_trend` on HVAC returned no years at all and said why: not enough disclosed transactions at **n < 10** in any single year. The bracket object in the same pass came back empty while the pooled all-sizes figure was published and labelled as pooled. Both refusals arrived `isError: false` with the reason stated, so an agent relaying them says something true instead of something made up.

The limits are stated in the guide rather than smoothed over. Pooled nine-year medians hide the cycle, the universe is US disclosed transactions and therefore skewed large, and every response carries a `calculator_url` with `src=mcp` that is a marketing funnel inside the tool output and separable from the structured data.

### AllClear Lending MCP - Named Lenders and the Decline Ladder

Relevance: HIGH. **Tier 1, driven** (`initialize` **200** as `allclear-lending` **0.1.0**, `tools/list` returning all **8** tools, five calls made, one of them rejected against the decline enum).

[MonitorBankRates MCP](/hermes/mcp/servers/external/monitorbankrates-mcp/) benchmarks the price of a loan across 8,000 institutions and ranks HMDA lenders. It does not answer who funds a restaurant in Texas, which programs are actually brokerable, or what to do after a decline. AllClear answers all three, and it does it with named institutions and a source URL per program.

`find_lenders` for restaurants in Texas returned **12** matches with **4** returned at the limit. Each row is a record: Celtic Bank for hotel and restaurant FF&E plus restaurant construction as special-use CRE, up to **$2 million** at up to **100 percent LTV** on its own page, broker path `referral_partner`, `confidence: sourced`; Ready Capital for SBA 7(a) restaurant acquisition, cited to a published spotlight deal. Rows with a single source are labelled **unverified** in the same field, which is the difference between a directory and a lead list.

`industry_overview` is the part an owner should read first. Restaurants in Texas: ease tier **A**, ease score **88**, NAICS **7225 / 7224**, **7** product types that fit, SBA eligible, **14** lenders serving and **0** restricting, with **Toast Capital** and **Square Loans** flagged as embedded and **not brokerable**, and a `verifier_note` carving out nightclubs as a restricted sub-segment. The `why` field cites its own arithmetic, including **16,354** SBA 7(a) loans to NAICS **722511** across FY20 to FY25 from a third-party FOIA tally.

`next_best_option` takes the reason for the decline, and the reason is enforced as an enum: a call with `"credit"` was rejected `-32602` with all fifteen accepted values listed. The valid call for `low_personal_credit` returned **Bitty** and **Credibly** at a 500 to 550 floor, with the instruction to show the MCA cost in math and never call it a loan, then a dated come-back plan. The stated principle orders options cheapest first and shows a revenue-based advance last with its full cost, which is the opposite of the payout-ranked default.

Two things in the guide are stated as weaknesses. `state_rules` for Texas carries real dated facts (HB 700 registration with the OCCC through NMLS by **2026-12-31**, the SBA Form 159 referral rule, and non-citizen ownership making a business ineligible since 2026-03-01) and then returns `researched: false` with every lane status `unknown`, so the surface reports the part of the state it has not covered. And `report_outcome` plus `lender_stats` create a two-sided graph where the reporter chooses whether to report and a `reporter_key` is self-declared, so approval rates are evidence of direction before they are a market rate.

## Read and Held, With the Measurement Behind Each

The wave's largest cohort is a documentation fleet. Fifteen entries in `/all` pages 1 to 2 are one repository, `foreverworks/mcps`, published as separate listings: Google Workspace, Notion, Bitwarden, Porkbun, Home Assistant, Expo EAS, App Store and Google Play reviews, trademark search, TypeSafe, plus Romanian financial administration in four pieces (BNR exchange rates, ANAF e-Factura, ANAF SPV, ONRC trade register) and Oblio invoicing. One author, one repo, separate cards, and the single-author fleet rule applies: catalogue the standout, group the remainder. The standout candidate is e-Factura, and it was held because Romanian e-invoicing is regional financial administration of the class already carried by the regional tax and e-invoicing guides, and because four sibling listings from the same repo would have to be catalogued or held together rather than one of them picked. Google Workspace and Notion are held as first-party connectors that most clients already hold natively.

The second cohort is the vendor documentation server, about 25 entries whose slug reads `-docs-mcp` or `-docs-mcp-server` (Cartrelay, Hirelabs, Ziva.sh, Teddit.io, Echoly, MachineMail, Cloud Alter Ego, La Prueba, Mooi, SimpleVerifier, AskEditor, Mailazy, Robylon, Skael, Buddy, APKCube, IsMyNumberSpam, Back4App, Webclaw, Recl, Rainbrand). Each is a retrieval surface over its vendor's own documentation. That class is held as a whole: a documentation route answers questions about a product, not questions about the business, and the catalogue carries operator data surfaces rather than product manuals.

The third cohort is lead generation and outreach: Embers (warm leads from LinkedIn engagement), Sumora (approval-first B2B outreach), Skael (German B2B lists), Patto (PR and link building), UGC Chart (Trybe creator sales ranking). The class is carried by the lead-generation entries already held (Leadbay, Vibe Prospecting, VOYGR) and by the creator-analytics set ([IQfluence](/hermes/mcp/servers/external/iqfluence-mcp/), [AffiliateSpy](/hermes/mcp/servers/external/affiliatespy-mcp/), [GenViral](/hermes/mcp/servers/external/genviral-mcp/), [Viral Manager](/hermes/mcp/servers/external/viral-manager-mcp/)). UGC Chart answered **401** `sign_in_required`, and its own pitch is that it adds data points on top of Trybe, a single creator network, which makes it a second view of one platform rather than an independent measurement.

Ads and social publishing: Orphex (ad performance across platforms with a change-approval step), Apogee (bulk ad launcher for Meta, TikTok and Snapchat), SyncBooster, Echoly, 24Repost (cross-posting Telegram, MAX and VK, answered **401** `-32001` in Russian). Class carried by the ads and social entries already held, including the change-approval pattern.

Scraping and browser infrastructure: Scrappy (hosted headful Chrome on residential IPs with saved logins), Webclaw, MapsScraper. Class carried by ScrapeAtlas, Browserless and Crawl4AI.

AI visibility and SEO scoring: Teddit.io (is your brand named by ChatGPT, Claude, Perplexity), pixelcove citation-tracker, pixelcove topic-scorer, Krafters. Class carried by geolint and LogNorm, both already held.

Site quality: Useful Work appeared on the feed at `2026-11-04T04:51:22Z` with typo, wrong-price, stale-text, broken-link and expiring-certificate checks against a live site. Held because the class is carried by [SiteGoalie](/hermes/mcp/servers/external/sitegoalie-mcp/) and [SquirrelScan](/hermes/mcp/servers/external/squirrelscan-mcp/), both already catalogued, and because the feed card publishes no endpoint to probe.

CRM and revenue systems: Deskhand (hosted CRM with 28 tools per key), NOVA for Kommo, Finwise (personal budgets rather than a business ledger), Reciba (Brazilian payment receipts), Volanea (agentic inboxes). Class carried by the CRM and email entries already held.

Property and public records: Homedex UK (estate agent listings plus HM Land Registry sold prices), BatchData (property, ownership and mortgage). Class carried by the property group, from [Hercules](/hermes/mcp/servers/external/hercules-property-mcp/) to Fonciq and HeritageDeed.

Public-market and tax filing: SN Data answered **401** with OAuth protected-resource metadata and offers financial statements, insider trades, House trades and short interest, a class already dense with ROIC, Signal8, fAlpha and BDE. DilutionScan answered keyless **200** as `dilutionscan-mcp` **0.19.0** with **34** tools over warrants, convertibles, shelves, ATMs and float, and was held on a measured reason rather than a category: its submission states that tool calls require a DilutionScan Pro subscription, the same subscription behind Signal8 Pro, and Signal8 is already catalogued from this vendor. IRISfile (Irish FIRE and 1099 to IRIS XML) is regional tax filing of a class already carried.

Outside operator scope, named so the next pass does not re-triage them: Fortrip (**401**), shibaSIM (**200**, 3 travel eSIM tools), OpenVerein (**401**, German club administration), Neat Icons (**401**, license required), Shellway (**401**, SSH relay), Lingviko German noun genders, FateTell BaZi astrology, FindBroadband and its outage checker, Kurodyne marketplace, PrizePicks, the empty-leg and private-airport indexes, Está no Ir, ScareMap, Heatwayve, Bodywise, afk-rig and IMPOSSIBREW.

## What This Pass Changed

The guide tree moved from **1,096** directories to **1,098**, and entries counting single-file guides from **1,240** to **1,242**. The catalogue's finance coverage now holds three distinct angles where it held two: public-company multiples ([ROIC.ai](/hermes/mcp/servers/external/roic-ai-mcp-server/)), private-credit exposure ([DFX](/hermes/mcp/servers/external/dfx-intelligence-mcp/)), and private-company transaction multiples ([ExitValue](/hermes/mcp/servers/external/exitvalue-ai-mcp/)). On the funding side, rate benchmarks ([MonitorBankRates](/hermes/mcp/servers/external/monitorbankrates-mcp/)) now sit beside named commercial lenders with brokering rules ([AllClear](/hermes/mcp/servers/external/allclear-lending-mcp/)).

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [ExitValue.ai M&A Multiples MCP](/hermes/mcp/servers/external/exitvalue-ai-mcp/)
- [AllClear Lending MCP](/hermes/mcp/servers/external/allclear-lending-mcp/)
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/)
