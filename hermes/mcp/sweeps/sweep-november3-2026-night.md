---
title: "MCP Server Discovery - November 3, 2026 (Night)"
description: "Night sweep of mcp.so and mcpservers.org: a 260-entry counter jump on the newest page, an AI supply-chain BOM and a free Polish registry earning guides, 30 arrivals dispositioned."
last_updated: 2026-11-03
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november3-2026-night"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 3, 2026 (Night Sweep)

## Summary

Four hours after the evening pass and the two surfaces behaved in opposite directions. The mcp.so homepage had turned over by exactly **two** cards past the evening stamp, and both were payments and modelling products rather than the usual developer tooling. The mcpservers.org `/all` newest page had turned over completely: the counter moved **18,885 to 19,145**, **260** entries in ten hours, and the thirty newest slugs shared nothing with the thirty the night pass dispositioned.

Two arrivals earned guides. **agent-bom MCP** is an AI supply-chain BOM that answers which credential a vulnerable package can actually reach, driven twice on this box: an offline demo scan in 0.8 seconds and a live stdio session listing **8** tools. **firmy.ai MCP** is the Polish business registers over MCP with a free keyless mode, driven through six of its eight tools against a real company, with filed statements, two sanctions lists and public tenders all returning dated answers.

One reading rule earned a second surface. The mcp.so homepage was fetched twice, once plainly and once cache-busted, and the plain read was a **CDN copy missing both new cards**: **97** parsed objects against **78** distinct on the second read, with `sheetsfinance` and `snapex-pay` only present on the cache-busted page. The two-read rule that had been applied to `/all` since the November 2 night pass now applies to mcp.so as well. The read whose newest stamp has moved is the live one.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| mcp.so homepage `recentServers` | direct, read twice, second read cache-busted with a different user agent | first read **97** objects, missing both new cards; second read **78** distinct, newest `2026-11-03T08:51:34Z` against the evening stamp of `2026-11-03T03:04:06Z`, **2** above it |
| mcpservers.org `/all` | r.jina.ai with `X-Return-Format: html`, read twice | **19,145** on both reads against **18,885** at the night pass, **30** newest slugs, none of them previously catalogued as a guide |
| Endpoint probes | keyless JSON-RPC | **200** on `firmy.ai` (**8** tools, **6** called), `agentoutposts` (**4** tools, **3** called), `runheed` (`initialize`), `pay.snapex.pro` (`initialize`, session id issued); **401** on `data.sheetsfinance.com` with `resource_metadata` |

## New Servers Catalogued

### agent-bom MCP - The Blast Radius of an AI Supply Chain

Relevance: HIGH. **Tier 1, driven** (offline demo scan plus a live stdio session, `serverInfo` `agent-bom` **0.113.0**, `tools/list` returning **8** tools).

The product is an inventory of the AI layer rather than the dependency file. It discovers the agents installed on a machine or in a repository, the MCP servers each one connects to, the packages those servers pull, and the credentials in the environment beside them, then joins that to CVE data and prints the path a compromised package would take to reach a secret.

The offline demo run in **0.8** seconds found **5** agents, **10** servers and **23** packages (**14** PyPI, **9** npm), with **15** vulnerabilities, a posture grade of **F 37/100**, credential hygiene as the top driver over **14** credentials, **5** toxic combinations and one CISA KEV at EPSS **99** percent. The two findings that justify the tool are the reachability ones: CVE-2023-36258 in `langchain@0.0.150` carries a blast radius of `llm-orchestrator → ANTHROPIC_API_KEY +1` at EPSS **1** percent, and CVE-2020-14343 in `pyyaml@5.3` reaches `shell-runner-service` at EPSS **5** percent. A flat severity list ranks the pillow bug first and buries both.

It earns a guide on a graph the catalogue does not have. [TrustScan MCP](/hermes/mcp/servers/external/trustscan-mcp/) inspects one server or skill for injection, dangerous code, secrets and typosquatting. [AgentTrust MCP](/hermes/mcp/servers/external/agenttrust-mcp/) returns a trust decision on an endpoint. [glc PromptGuard MCP](/hermes/mcp/servers/external/glc-promptguard-mcp/) scores one prompt or tool output. Each reads an artefact; none of them joins agent to server to package to credential.

Guide: [agent-bom MCP](/hermes/mcp/servers/external/agent-bom-mcp/)

### firmy.ai MCP - A Polish Dossier Without an Account

Relevance: HIGH. **Tier 1, driven** (`initialize` HTTP 200 as `firmy.ai` **1.0.0**, **8** tools listed, **6** called live, `get_account` confirming `mode: "free"`, `authenticated: false`).

One endpoint over the Polish registers with a free mode that needs no account and declares the state of every section before it is asked for. Two modes rather than one paywall: free reads what the service already holds and returns `AUTH_REQUIRED` per missing section, Pro (still unavailable) would fetch on demand at up to 40 operations per call.

Measured on CD PROJEKT RED S.A., KRS 0000006865: NIP 7342867148, REGON 492707333, entered 2001-04-06, last entry 2026-08-10, share capital 99,910,510 PLN, **14** officers, **29** documents. Financials for 2024 from the filed statement: revenue **985,030,000** PLN against **1,230,199,000** the year before, a fall of **19.9** percent, net income **469,874,000**, EBITDA **379,785,000**, net margin **47.7** percent. Screening: sanctions `verdict: "clear"` across the EU and MSWiA lists `as_of 2026-11-03`, tenders `found: false` since 2024-02-01 across BZP and TED `as_of 2026-11-03`, while the profile page carried `as_of 2026-08-10`. Market screening returned ORLEN at **294,976,000,000** PLN, Jeronimo Martins Polska at **101,987,368,889** and Totalizator Sportowy at **52,248,125,432.71**.

Two defects go into the guide because driving found them: `rank_companies` on `margin` returns percentages up to **3,569,778.83** and on `altman` returns **33,576.07** points, ratio artefacts from near-zero denominators sorting above every real company; and `search_companies` returns `regon: null` on every row while the dossier on the same KRS holds REGON 492707333. A rejected section name is handled well: `INVALID_INPUT` with a hint listing all **22** valid sections and a corrected `suggested_call`.

It earns a guide because Poland is the thin spot here. [company-atlas-mcp](/hermes/mcp/servers/external/company-atlas-mcp/) carries eight markets and Poland is not among them; [UK Companies House](/hermes/mcp/servers/external/uk-companies-house-mcp/) and [registry-mcp](/hermes/mcp/servers/external/registry-mcp/) are single jurisdictions; [Prometiam Risk MCP](/hermes/mcp/servers/external/prometiam-risk-mcp/) covers thirteen European countries including PL but puts Polish financial statements on its Scale tier and screening from Starter.

Guide: [firmy.ai MCP](/hermes/mcp/servers/external/firmy-ai-mcp/)

## Read and Held

**From the mcp.so feed (2 new cards).** `SnapEX Pay` (`2026-11-02T23:02:51Z`) answered a keyless `initialize` as `snapex-pay` **1.0.1**, issued an `Mcp-Session-Id`, and ships a remote endpoint at `https://pay.snapex.pro/mcp` beside an npm package and a Docker image under registry name `pro.snapex/pay`: self-serve merchant accounts, invoices, receiving, payouts and exchange for agents. Held on the agent-payments class, which already carries [FiatDock](/hermes/mcp/servers/external/fiatdock-mcp/) with x402 settlement, CoinVello and the x402 surfaces. `SheetsFinance` (`2026-11-03T08:51:34Z`) returned a measured **401** at `https://data.sheetsfinance.com/mcp` with `resource_metadata` pointing at `/.well-known/oauth-protected-resource/mcp/`, and builds DCF, comps and dividend models as a live Excel or Google Sheets workbook through an add-on whose formulas refresh, over 30+ years of statements and 80,000+ symbols. Held on the valuation class carried by [Valuation API](/hermes/mcp/servers/external/valuation-api-mcp/), [HotelValora](/hermes/mcp/servers/external/hotelvalora-mcp/) and [InvestSights](/hermes/mcp/servers/external/investsights-mcp/); the live-formula workbook is the one feature worth a second look if an operator asks for a model rather than a number.

**From mcpservers.org `/all` (30 newest slugs, 28 held).** Four of the thirty had already been dispositioned in the submission window and are recorded here so the next pass does not read them as fresh: `Sumora` (approval-first B2B LinkedIn and Instagram outreach, #6617), `Pocket Archive` (OAuth document archive, #6639), `Frank` (AI-moderated customer interviews, #6524) and `Varity` (application deploys, #6578), with `UGT` (#6640) and `JustGains` held in earlier windows.

Of the rest, the operator-adjacent arrivals are held on class rather than on quality. `Runheed` answered a keyless `initialize` as `runheed` **0.1.0** with error groups, full context and a resolve call, held on the error-tracking surface a coding agent already reaches, developer infrastructure rather than an operator answer. `Useful Work` finds typos, wrong facts, broken links, slow pages and expiring certificates and domains on a live site, held on the site-audit class which carries twenty-plus SEO entries, with certificate and domain expiry recorded as the one angle no guide here covers. `SEO Content Machine` plans and writes pages through a desktop app that has to be running, held as localised tooling on the saturated SEO class. `Landsight` reads New Zealand LINZ parcel, title and building-footprint records, held on the land class carried by [UK Land Registry](/hermes/mcp/servers/external/uk-land-registry-mcp/) and on geography. `Agent Outposts` answered keyless with **4** tools and **42** outposts - Airbnb, Amazon, American Airlines, Best Buy, Kroger and Peet's Coffee marked `industry_leader`, the rest `collecting_demand` - each brand carrying a five-intent door-state document (`menu_browse`, `prices`, `inventory`, `ordering`, `tracking`) with an evidence URL, a `checked_at` date and a version stamp of `census-2026-11-01`, plus intent registration and change polling. Held on the agent-commerce reachability class carried by [ARC MCP](/hermes/mcp/servers/external/arc-agentic-report-card-mcp/), which already answers which stores an agent can buy from and what a brand's agent facts are; this is the brand-level demand registry of the same question, flagged for a second look rather than promoted, because ARC measures checkout while this measures five intents across QSR, airlines, hotels and pharmacy.

The remainder are utilities, verticals and developer tooling outside the operator scope of this catalogue: `iCloud for Agents` (macOS Mail, Contacts, Calendars, Notes and Reminders over a local bridge, in the saturated email and calendar class), `Trend0x` (crypto and stock trading terminal with backtests), `afk-rig` (3D auto-rigging with 170+ animations), `LionTech` (a Vietnamese listing with no endpoint, tool list or repository), `Discord Timestamp Generator` (a stateless timestamp formatter), `Bodywise` (56 sports-science calculators and CoFID foods, consumer fitness), `Peykan` (a virtual CAN bus for a car), `admcp` (Android debugging over ADB, local stdio), `Interview Prep MCP` (offline graded interview questions), `call-grokbot` (a local stdio wrapper with four tools that drives an existing Grok bot), `A/B Test Sample Size Calculator` (sample size, duration, z-test, chi-square and Fisher exact with peeking checks, the peeking check being the only part that differs from a formula), `readfirst` (per-file rules and risk maps for coding agents, local only), `Recipe Nutrition Calculator` (USDA FoodData Central macros with FDA label rounding), `AP Score Distributions` (College Board AP percentiles), `Estate and Gift Tax Exemption Calculator` (federal exemption 2025-2026 including the OBBBA $15M amount), `Zap! KiCad autorouter` (hosted PCB routing) and `ctxd` (open-source context sync and source reads for agents).

## Count

The guide tree held **1,090** guide directories before this pass and holds **1,092** after it, **1,237** entries counting single-file guides before and **1,239** after. Sources: the mcp.so homepage `recentServers` block read twice, the second read cache-busted; the mcpservers.org `/all` newest page read twice through the r.jina.ai reader proxy with `X-Return-Format: html` at counter **19,145**; keyless JSON-RPC sessions on `https://firmy.ai/mcp` (**8** tools, **6** called), `https://api.agentoutposts.com/mcp` (**4** tools, **3** called), `https://runheed.com/api/mcp` and `https://pay.snapex.pro/mcp`; a measured **401** on `https://data.sheetsfinance.com/mcp`; and two local runs of `uvx agent-bom` (scan `--demo --offline` and `mcp server` over stdio, **8** tools). The chatmcp/mcpso submission window was not read this pass; the scope was the two directory surfaces the schedule names.
