---
title: "MCP Server Discovery - November 6, 2026 (Night Sweep)"
description: "Night pass where the sitemap jumped 215 slugs and the jump was backlog, not products, and one server was catalogued: a metric layer that infers itself."
last_updated: 2026-11-06
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november6-2026-night"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 6, 2026 (Night Sweep)

## Summary

This pass fired on the **03:00 MST** tick, six hours after the November 5 evening read, and the shape was unusual: the sitemap moved more than it has in any single window this week while the feed and the submission queue barely moved at all.

The mcpservers.org twelve-sitemap canonical went from **19,513** to **19,728** server URLs after stripping the locale prefixes - **215 additions and zero removals**. That reads like the largest arrival wave of the week until the composition is examined: **45** of the 215 are one author's `mambalabsdev` fleet that this ledger already held as a single line on November 5, **18** are `-docs-mcp` documentation mirrors that name products already dispositioned, and a family of the rest are the same products this catalog already read under their product spelling (DataXAPI, getwork.dev, Growth Radar, RoomLab, Torvex, Ezo Watcher, Desktop Steward, Faxbeep, Harbor, Motion Reel, Piratex, Shipbook). Of the **100** slugs that survived a first crossref pass, **65** were resolved through the official MCP registry API and every one of them fell into a class this catalog already carries, except one.

mcp.so was nearly flat: **108** distinct cards in the `recentServers` payload with the newest at `2026-11-06T08:46:04.639Z`, and only **two** cards above the evening stamp (`apteka-online` and `alalanet`), both vertical or trust-layer surfaces in carried classes. The submission queue contributed **15** numbers from `#6832` to `#6846`, two of them listing updates and one a single author's 58-server monorepo.

**One** server was catalogued: a semantic layer that infers itself from a warehouse's own statistics and then lints an agent's SQL against it. It is the first entry here that derives the definitions rather than asking a human to declare them, and it was driven end to end on this machine rather than quoted from a page.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| mcpservers.org twelve-sitemap canonical | 14 sitemap documents fetched directly with plain urllib, locale prefixes stripped, set difference against the November 5 04:31 capture | **19,728** server URLs against **19,513**. **215** additions, **0** removals. A raw union reads **76,336** URLs across the index (static, priority, `servers/1..10`, skills, remote), **62,920** of them under `/servers/`, **43,192** carrying an inline locale prefix that was stripped before diffing |
| mcpservers.org `/all` | not read | Cloudflare refuses `/all` and every detail page to a direct fetch (**403**) and the reader proxy is answering **401 03** bad IP reputation. A standing condition, not an incident |
| mcp.so homepage | direct fetch with a browser user agent, `recentServers` parsed from the RSC payload | **188** `createdAt` occurrences on the page, **108** distinct recent cards, newest `2026-11-06T08:46:04.639Z` (**alalanet**), **2** cards above the evening stamp |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included | **15** numbers, `#6832` to `#6846`: **12** arrivals, **2** listing updates (`remoet-mcp`, `mcp-gotolstoy`), and `#6845` a 58-server monorepo already covered by the catalogued TheLuckyStrike suite |
| Official MCP registry API | search on every unledgered slug | **65 of 100** unledgered slugs resolved to a name, description, website and publication date |
| Cross-reference | compact-token pass against the catalog index, the guide tree, the last-sweep ledger and 40 recent sweep pages | **115** of the 215 additions matched an existing heading, guide directory or prior disposition. The **100** that did not were resolved in the registry before any of them was judged |
| Tracked listings | direct probes | mcpservers.org canonical still carries `/servers/corpusiq-io`; Glama **200** on `/mcp/connectors/io.corpusiq/multi-source-mcp`; the official registry now carries **four** active versions of `io.corpusiq/multi-source-mcp`; mcp.so still does not list us (all four direct slugs **404**); Smithery's registry API answered **500** twice and was not re-attempted |

## New Servers Catalogued

### [semlayer MCP - A Metric Layer Inferred From the Warehouse](/hermes/mcp/servers/external/semlayer-mcp/)

Local stdio server, `semlayer` **0.7.0b2** on PyPI, registered as `dev.semlayer/mcp` and published `2026-11-05T02:24:10Z`, Fair Source under FSL-1.1-ALv2 with the format spec Apache-2.0. Pointed at DuckDB, PostgreSQL, Snowflake or BigQuery, it profiles every column, discovers the foreign keys nobody declared, decodes the status columns, and writes the result as a portable YAML layer carrying `confidence`, `provenance` and `lifecycle` on every claim, then serves **21** tools over MCP.

It was driven, not quoted. A six-table DuckDB fixture was built with the traps that make warehouse answers wrong - a status code decoded through a separate dimension, an order header a line table fans out, an SCD2 customer master, a legacy twin of the order table, and an aggregate that only reconciles when cancellations are excluded. `semlayer infer duckdb:store.db --no-llm` produced **6** tables, **25** columns, `valid=True` and **4** review items with no API key and no model call. The server then answered `initialize` as protocol **2025-06-18** / `semlayer` **1.30.0**, listed **21** tools, and six were called.

The measurement that earns the entry: the inferred metric `total_tot_amt_completed` compiles to `SELECT SUM(ord_hdr.tot_amt) ... WHERE (sts_cd = 'C')` and returns **240,857.05** on the fixture, while the unfiltered twin of the same measure returns **378,881.81** - **138,024.76** apart on a 300-order table, with the fixture's own aggregate table summing to the filtered figure and confirming which one the business means. `check_sql` refuses the fan-out query with `fanout_aggregate` and a stated fix, and returns `ok: true` on the clean one. `run_sql` refused without a session connection rather than guessing, and said why.

It earns a guide on a mechanism gap rather than a name: **Dataddo** and the sheets-into-PostgreSQL entry both carry a semantic layer, and both need someone - or the vendor - to declare it. semlayer infers it from statistics with a provenance trail per claim, needs no account, and adds a deterministic SQL linter that is the piece actually stopping the two silent errors. Limits recorded: beta, best on messy warehouses by the vendor's own published negative result, Anthropic-only LLM today, dbt as the only exporter, no hosted service, and a DuckDB storage-version trap hit in this session (a file written by duckdb 2.x is unreadable by the pinned 1.5.x build).

## Held, With the Class Named

The window's arrivals were overwhelmingly rotated versions of classes this catalog already answers. Held on **geo-niche accounting** (DokladBot, Taokeh, Kvickd, Amore Fortnox, Mighty, Zeno, Grand Livre, Nextesy, Pohoda, firmy.ai) with BeeL already carrying Spanish VeriFactu invoicing: **ContaCeret** (`contaceret-es-conector-ia`), the Spanish SME accounting connector with VeriFactu invoices, quarterly models, bank balances and per-company read-only keys - a real thin spot for bookkeeping depth, but the French double-entry entry (Grand Livre) was held on this same class, so the reversal test is a driven session showing per-company read scoping that Grand Livre and BeeL do not offer. Held on **deposit and mortgage benchmarks** (MonitorBankRates, which already ranks HMDA lenders and reads a daily mortgage rate): **SafeRate**. Held on **Google Ads / GA4 / Search Console analytics** (GSCPAP's 38 tools, plus Hitech and Torvex): **Metrinel**, and this wave carried two more in the same slice, **mowteng** and **sonnivasquez/gsc-mcp**. Held on **property data** (PropRaven over 191.3M parcels, Placestack, Hercules, DFX, Korzy): **GetParcelData**. Held on **SEC and EDGAR** (nine surfaces): **alphayou**. Held on **legal research** (LEGAION, aka-recht, Specter Cite, EmentAI): **Jurisprudencias.ai** and **lexgraph**. Held on **B2B prospecting and enrichment** (Hilead, Leadbay, Vibe Prospecting, Sorzio, the MailTester trio): **AskBond**. Held on **help desk** (HelpWell): **rinhelp**. Held on **call analytics** (Callflow, the VoIP class): **loopvoice**. Held on **stock research saturation** (fAlpha, BDE, Altair, ValuEdge): **Gold-Silver Analytics**, junior-mining research. Held on **research papers** (papernex, rivul, Paperzilla): **Arca Life Sciences**. Held on **media generation** (RoomLab, Motion Reel, SFXReel, AdMake): **Masonry**, **Tevyon**, **Kreavo**, **Revline**, **ChatCut**, **Viralance**, **VIVID** and **Montik**. Held on **social scheduling** (post2all, Micm): **PersonaXpand**. Held on **social data** (Kaption, the Reddit and Threads scrapers, the Apify-actor hold): **tgden**, a Telegram catalogue and demand surface. Held **thin by inspection** rather than by class: **Kennmarq** (read-only documents about C2PA marking, no marking API), **KeepMD EOB Decoder** (consumer medical-bill explanation, the medical-bill-check class already held), **falzmarke** (German DIN 5008 letter rendering, document class), **Spacepal** (macOS Spaces), **Ferret** (household inventory), **FlyItalyADSB** (aviation), **WineAuction** (wine pricing), **Portproof** (proxy vendor, the IPRoyal rule), **onlyfakefacts**, **onlinealarmkur**, **mostexpensivewatches**, **truelook**, **stashhh**, **kenko**, **eldertongue**, **modellens**, **statelode**, **dash-gitsu**, **docstar**, **ahook**, **robodebut**, **draftkingsapi**, **feegate**, **optionclaws**, **wellspent**, **expressnumber**, **onesimpleapi**, **pdfshift**, **sitejar**, **sundaeui**, **spritulus**, **3dvalley**, **drawdy**, **fixmeadrink**, **fluentoo**, **countrymanager**, **anylocale** and **wptaskify**. And `#6845` is TheLuckyStrike's 58-server monorepo, covered by the catalogued suite; `#6841` and `#6842` are listing updates rather than submissions.

## Core Listing Check

- **mcpservers.org** - `/servers/corpusiq-io` still present in the canonical; the detail page remains unreadable behind the same 403.
- **Glama** - **200** on `/mcp/connectors/io.corpusiq/multi-source-mcp`.
- **Official MCP registry** - **four** active versions now: `1.0.0` published `2026-05-25`, `1.0.1` on `2026-10-22`, `1.0.2` on `2026-10-23`, and **`1.0.3`** on `2026-10-24`, all with the `https://mcp2.corpusiq.io/mcp` remote. The **30+ versus 40+ description drift that earlier sweeps flagged is closed**: the active records now read "One governed MCP endpoint for 40+ business systems."
- **mcp.so** - not listed. All four direct slugs (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) returned **404**.
- **Smithery** - the registry API returned **500** twice; not confirmed this pass, and a server error is never a delisting.

## Counts

- Canonical: **19,728** against **19,513**, **+215** / **-0**.
- Additions ledgered by crossref: **115** of **215**; unledgered **100**; registry-resolved **65**.
- mcp.so: **108** distinct cards, newest `2026-11-06T08:46:04.639Z`, **2** above the previous stamp.
- Submission window: `#6832` to `#6846`, **15** numbers, **12** arrivals.
- Guide tree at this pass, counted on the checkout rather than carried forward: **1,107** server directories and **144** single-file guides directly under `external/`.
- Endpoint probes: **1** driven end to end (semlayer, MCP stdio, 21 tools, 6 calls), **1** refused (the ContaCeret demo host answered **405** to a JSON-RPC POST, the app host did not answer at all).
