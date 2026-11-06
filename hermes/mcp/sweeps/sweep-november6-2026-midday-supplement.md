---
title: "MCP Server Discovery - November 6, 2026 (Midday Supplement)"
description: "Supplement pass where /all answered for the first time in a week with 28 unledgered slugs, and one label-stream connector was catalogued on its limits."
last_updated: 2026-11-06
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november6-2026-midday-supplement"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 6, 2026 (Midday Supplement)

## Summary

This pass fired on the **11:00 MST** tick, one hour after the midday sweep, and the value was not in a wave of new servers. It was in a surface that had refused every read for a week. **mcpservers.org `/all` returned 200** and handed over its newest **30** slugs, **28** of which had never been dispositioned in this ledger. The sitemap was flat, so none of them was an arrival: they were the page-1 residents of several earlier waves that this catalog had simply never read, because `/all` was answering **403** direct and **401 03 bad IP reputation** through the reader proxy on almost every pass since November 4.

The other two surfaces behaved as expected at a short interval. The twelve-sitemap canonical came back **set identical** at **19,727** server URLs against the 10:00 capture, all 14 documents fetched fresh, **0** additions and **0** removals. The mcp.so homepage put exactly **one** card above the midday stamp, `2026-11-06T16:54:40.494Z`, on both the plain and the cache-busted read, and the submission queue added three numbers, `#6859` to `#6861`.

**One server was catalogued**, and it did not come from the queue or the feed. It came from the `/all` cohort, which is the argument for reading that page even when it refuses.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| mcpservers.org `/all` | direct fetch, browser user agent, **200** | **30** slugs, **28** unledgered on a first slug pass. Every one dispositioned below |
| mcpservers.org twelve-sitemap canonical | all 14 documents, plain urllib, locale prefixes stripped, diffed against the 10:00 capture | **19,727** server URLs against **19,727**. **0** additions, **0** removals |
| mcp.so homepage | direct fetch plus a cache-busted second read | **204** `createdAt` occurrences, **167** distinct stamps, newest `2026-11-06T16:54:40.494Z` (**patentref**) on both reads, **one** card above the midday stamp |
| chatmcp/mcpso submission window | authenticated `gh api`, three issues | `#6859` ROVE Snow Forecast, `#6860` ndekoui, `#6861` Sanctionlistcheck.com, all arrivals |
| Official MCP registry | `registry.modelcontextprotocol.io` searches per candidate | Resolved `io.github.patentref/patentref-mcp` **0.4.0**, `com.sanctionlistcheck/sanctionlistcheck` **1.0.0**, `com.rove-ski/snow-forecast` **1.0.0** and **1.0.1**, plus twelve `/all` cohort names |
| Endpoint probes | keyless `initialize` | `https://mcp.zplflow.io/v1/mcp` and `/v1/mcp/` both **401 UNAUTHORIZED** with no `WWW-Authenticate`, confirming a static-key surface rather than OAuth |

## The surface that came back

`/all` answering again changes what a supplement pass is worth. Its 30 slots overlapped the feed almost not at all, and the cohort split cleanly into three kinds:

- **Already catalogued, read under a product spelling:** `loadoptimizer-mcp` and `fixragent-mcp` both have guides.
- **Prior dispositions in prose:** backlnk (BACKLNK), Motion Reel, Revline, Merit Ukrainian Law, Ava Advisor. Each was held in an earlier sweep with its class named, and none has changed since.
- **Genuinely unread:** 24 slugs that had never appeared in this ledger under any spelling, including the one that earned the guide.

## New Servers Catalogued

### [ZplFlow MCP - Thermal Label Streams for Agents](/hermes/mcp/servers/external/zplflow-mcp/)

Hosted remote server at `https://mcp.zplflow.io/v1/mcp/`, Streamable HTTP in stateless mode, operated by MTech S.r.l. in Italy. **10 MCP tools** over an asynchronous conversion engine, API key auth with per-key scopes, token pricing where one standard label is one token: ZPL to PDF is 1 token per page, PDF to ZPL is 3 at 203 DPI and 4 at 300 DPI, flat regardless of the output size budget. Free tier carries **6,000 tokens** with no card and a 30-day full platform trial, then EUR 9 for 15,000 up to EUR 800 for 3,000,000.

**Documented, not driven.** A keyless `initialize` answers **401** with `{"error_code":"UNAUTHORIZED","message":"missing authorization header"}` and no protected-resource document, because the credential is a static key rather than a browser sign-in. The tool list, scopes, limits and prices are read from the vendor's own integrator documentation.

It earns a guide because it is the first surface in this catalog that touches the **label stream** rather than the business system behind it. LoadOptimizer decides what fits, PackIndex prices the packaging, Container Tracking follows the box, and ProShip creates shipments with PDF labels for one regional carrier set. Nothing else converts between PDF and ZPL, applies programmable transformations before a label reaches a printer, or runs a print run as a batch. The 24 pipeline transformers cover `add_text`, `add_barcode`, `add_qrcode`, `add_datamatrix`, `replace_barcode_value`, `regex_replace`, `add_timestamp`, `format_date` and the geometric set, which is the layer that makes a PDF from an accounting system acceptable to a Zebra printer and the layer that injects GS1-128 compliance into a barcode an ERP produced without it.

The limits are the story, the same way the write envelope was the story for Sellfy. Conversions travel through the asynchronous engine even though the vendor ships a sub-200ms synchronous REST route, because that route is marked not exposed as a public MCP tool. `listPipelines` and `getPipeline` are the only pipeline tools, so an agent can read the label recipes and cannot rewrite them. Upload URLs expire in **15 minutes** and results in **1 hour**, so a workflow that stalls has to start over. And the commercial behaviour worth naming is dynamic over-budget scaling: exceeding the monthly allowance does not stop the line, it bills overage per 1,000 tokens, which is an operational guarantee with a bill attached.

## Held, With the Class Named

From the submission queue and the feed, four arrivals, all held:

- **PatentRef** (`io.github.patentref/patentref-mcp` **0.4.0**, stdio, PATENTREF_API_KEY, US grants from 1976 over a PatentsView-compatible API, `search_patents`, `similar_patents`, `build_facts`, `search_disclosures`) on the patent and IP research class already carried by Patsnap's 170-jurisdiction search and by LegalCode. Claim trees are the differentiator in the tagline and are not exposed as a tool in the listing, so the surface is a US-only slice of a class with an owner.
- **Sanctionlistcheck.com** (`com.sanctionlistcheck/sanctionlistcheck` **1.0.0**, remote, Bearer key by email, 100 free credits, 1 credit per screened name, `screen_names`, `get_record`, `list_sources`, `get_balance`, ten official lists) on the sanctions-screening class owned by ScreenVerity, QoreNext Trade Screening and Atlas Verified. A wider list set is a capability improvement inside that class, not a new class, which is the BACKLNK ruling applied again.
- **ndekoui** (`dev.ndekocode.ui/ndekoui`, keyless, 7 tools over a React component catalogue) as developer tooling for coding agents.
- **ROVE Snow Forecast** (`com.rove-ski/snow-forecast` **1.0.1**, OAuth or free Bearer key, 9 read-only tools over 667 ski resorts) as a consumer skiing vertical, outside the operator scope this catalog serves.

The 28-slug cohort, dispositioned as one list because the sitemap proved none of them was an arrival: **backlnk** technical SEO and GEO audits (Seo Audit Console, Geolint, CiteRank, Seomely, AEO Engine, AIO.GEO, MisarSEO); **loadoptimizer** and **fixragent** already catalogued; **motionreel**, **revline**, **spritulus**, **viralance** and **flavo** media generation; **merit-legal** Merit Ukrainian Law, held; **ava-fund** Ava Advisor, held; **seller-labs-amazon** Amazon seller and ads class; **changedetection-io** monitoring beside Cronitor, Runheed and uptrack; **countrymanager** app store reviews by country beside Sonar ASO and AppSigma; **anylocale** app localisation; **synchronicity-labs** lipsync and dubbing; **statelode** task layer for coding agents; **ryumoon-x402** x402-paid data tools; **ahook** agent webhooks; **oreondev** Harbor registry, DevOps; **yuryev89** Cisco Webex messaging; **mselcukozturk** Hevy to WHOOP, personal fitness; **centralcommand-io** crypto perpetuals and backtests; **firenook-dev** local Firebase emulators; **switchfrog-com** WebMCP agent detection; **helprange** document share and data-room analytics; **henokey09** and **aptekaonline** thin or single-market; **zplflow** catalogued.

Two of those deserve a record for the next pass rather than a silent skip. **HelpRange** is the nearest thing this catalog has to data-room engagement analytics: OAuth, hosted at `https://www.helprange.com/mcp`, and it answers who opened a document and which page held them, which is a question an operator raising money or sending a board pack asks by hand today. **Switchfrog** turns a site's own user workflows into WebMCP actions and reports which agents use them, which is the closest commercial surface to the agentic-web work this documentation set covers. Both held on thin public detail rather than on class, and both are worth a driven session when an account is available.

## Core Listing Check

- **mcpservers.org** - `/servers/corpusiq-io` is still present in the freshly fetched canonical. The detail page answers the standing **403**.
- **mcp.so** - still not listed. All four direct slugs remain **404**.
- **Glama** - **200** on `/mcp/connectors/io.corpusiq/multi-source-mcp`.
- **Official MCP registry** - **1.0.3** stands as the newest active `io.corpusiq/multi-source-mcp` record.

## Counts

- Canonical: **19,727** against **19,727**, **+0** / **-0**. Counted from the artifact on disk rather than carried forward from prose, after the same prose-versus-artifact gap the midday pass recorded.
- `/all`: **30** slugs, **28** unledgered on a first pass, **24** never read in this ledger under any spelling.
- Candidates evaluated: **32** (**28** from `/all`, **1** from the mcp.so feed, **3** from the submission queue). Catalogued **1**, held **31**.
- Guide tree: **1,108** directories before this pass, **1,109** after. **1,252** entries counting single-file guides before, **1,253** after.
