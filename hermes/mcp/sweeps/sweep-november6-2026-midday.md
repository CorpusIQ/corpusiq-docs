---
title: "MCP Server Discovery - November 6, 2026 (Midday Sweep)"
description: "Midday pass at a seven hour gap where the sitemap did not move at all and one hosted store connector was catalogued on its write envelope."
last_updated: 2026-11-06
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november6-2026-midday"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 6, 2026 (Midday Sweep)

## Summary

This pass fired on the **10:00 MST** tick, seven hours after the November 6 night read, and the canonical came back **set identical**: **19,733** server URLs against **19,733**, **zero additions and zero removals**. That is the third exact empty diff in two days and the first one this week where nothing had to be subtracted from an ingestion wave, because there was no wave to subtract.

With the sitemap flat, the window was carried by the two surfaces that move independently of it. mcp.so produced **188** timestamped entries on the homepage and **10** cards above the night stamp, the newest at `2026-11-06T16:09:36.927Z`, and the chatmcp/mcpso submission queue added **12** numbers from `#6847` to `#6858`, all arrivals, no listing updates. Every one of the **22** candidates was cross-referenced against the catalog index, the guide tree and the recent sweep pages, and **21** fell into a class this catalog already answers.

**One** server was catalogued: the hosted connector for a digital-product store platform, and the reason it earns the entry is not the platform. It is the envelope around the write tools, which refuses refunds, refuses deletions, refuses buyer email, creates everything unpublished, and rejects a storefront write when the page changed since the agent last read it. That is the pattern an operator wants before letting anything near a live shop.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| mcpservers.org twelve-sitemap canonical | all 14 sitemap documents fetched directly with plain urllib, locale prefixes stripped, set difference against the November 6 04:31 capture | **19,733** server URLs against **19,733**. **0** additions, **0** removals. The raw union read **76,408** URLs across the static, priority, `servers/1..10`, skills and remote documents, with **43,259** inline locale prefixes stripped before diffing |
| mcpservers.org `/all` | not read | Cloudflare answers **403** to a direct fetch and the reader proxy answers **401 03** bad IP reputation, the same standing condition every pass this week has recorded |
| mcp.so homepage | direct fetch with a browser user agent, `createdAt` and `slug`/`name` pairs parsed from the RSC payload | **188** `createdAt` occurrences, **138** distinct stamps, **204** slug/name pairs reducing to **170** distinct, newest `2026-11-06T16:09:36.927Z` (**apogee-ads**), **10** cards above the night stamp |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included in one call | **12** numbers, `#6847` to `#6858`, every one an arrival |
| Endpoint probes | keyless `initialize` against five candidate endpoints | **2** answering **200** (backlnk, plus the keyless `initialize` on the catalogued candidate was not driven), **2** answering **401** with a protected-resource document named in `WWW-Authenticate`, **1** answering **405** |
| Cross-reference | compact name and slug pass against the catalog index, the 1,107 guide directories, the previous sweep report and the recent sweep pages | **21** of **22** candidates matched an existing heading, a guide directory or prior disposition prose |
| Tracked listings | direct probes and the canonical itself | mcpservers.org canonical still carries `corpusiq-io`; Glama **200** on `/mcp/connectors/io.corpusiq/multi-source-mcp`; mcp.so still **404** on all four direct slugs; Smithery's registry API answered a server error and was not confirmed, which is never a delisting |

## New Servers Catalogued

### [Sellfy MCP - Store Operations Inside the Chat](/hermes/mcp/servers/external/sellfy-mcp/)

Hosted remote server at `https://api.sellfy.com/mcp`, Streamable HTTP, OAuth browser sign-in with two scopes (`mcp:read`, `mcp:write`) and no API keys to create. Included on every Sellfy plan and during the 14-day trial, launched **14 October 2026**, vendor-reported **75,000+ creators and businesses** and **$165M+** in creator earnings. **Documented, not driven**: a keyless `initialize` answers **401** naming its protected-resource document, and that document confirms the authorization server, header-only bearer method and the two scopes; the capability detail comes from the vendor's machine readable contract at `sellfy.com/mcp.md` and an agent-addressed setup file at `api.sellfy.com/agent-setup.md`.

It earns a guide on the write envelope rather than on the platform. Products, discounts, orders, customers, reviews, sales summaries, campaigns, storefront drafts and shipping profiles are all exposed, and the destructive half is deliberately absent: there is no tool to delete a product or a discount (a discount can only be expired), no refund or payout tool, no way to email a buyer (campaigns are drafts, tests go to the seller), new products are created unpublished with publishing a separate request, and storefront writes carry a revision check so a stale draft cannot overwrite a colleague's edit. The other four store connectors here either read a store or install locally with a token; this is the first hosted one that writes, which is why the limits are the story. Two details worth carrying: money arrives in minor units (1999 is 19.99), and the read tools see buyer names and addresses, which then travel to whichever model provider the merchant connected.

## Held, With the Class Named

The window was dense with rotations of classes already answered. Held on **technical SEO, AEO and GEO auditing**, which now carries Seo Audit Console, Geolint, CiteRank, Seomely, AEO Engine, AIO.GEO and MisarSEO among others: **BACKLNK**, a keyless endpoint answering **200** with six tools and fourteen checks (`llms-txt-validate`, `ai-crawler-access`, `entity-schema`, `indexability`, `hreflang`, `page-speed` and the rest) plus a `verify_fixes` step. The closed loop from check to fix to re-verify is genuinely the best mechanism in that class this month, and it is still a name in a class with seven owners, so it holds.

Held on the **geo-niche auction** class already owned by Subastech (Spanish judicial auctions): **Subastum**, the BOE Auction Portal and Social Security auction reader with OAuth scope `subastum.lectura`, total-cost-of-a-bid calculation and hammer-price statistics by city. The reversal test is a driven session showing that the state auction portal surface answers a question the judicial one cannot; two Spanish auction surfaces in one catalog is one too many until then.

Held on **company intelligence**, owned by Synorb, FinzData, SimilarLabs and Velarion: **Xcout Intel**, roughly **450,000 companies** across **115 countries** with funding rounds, investors, founders, executives, directors and financial history, each carrying the filing, website or article it came from. The provenance-per-claim is the closest thing in this window to how CorpusIQ answers, and Velarion already holds the class.

Held on **Search Console, Bing and GA4 analytics** (GSCPAP's 38 tools, Hitech, Torvex), where it is also a prior disposition in three consecutive sweeps: **GSC Magic**. Held on **consumer sports data** (SockOdds, ELDRICK, SquadCard, BetBank): **Odds-API.io**, 33 tools over 450+ bookmakers. Held on **app store and trends data** (Sonar ASO, AppSigma for store data; TrendPulse for Google Trends): **PastCharts**, free historical top charts across 30 App Store and 15 Google Play countries plus Google Trends back to November 2024. Held on **media generation** (RoomLab, Motion Reel, SFXReel, AdMake, Masonry, Tevyon, Revline): **Scenes**, a library of finished motion graphics scenes as HyperFrames code. Held on **anti-detect browser automation**, where Veilus already set the ruling: **chromeleon-mcp**, Windows only, no npm package. Held on the **crypto and trading** class (TTMT, the broker and bot cohort): **etrink**, cloud MetaTrader 5 terminals with bot hosting. Held on the **career** class: **Graphlog Career**. Held on **x402-paid security checks**, per the RE Data Refinery and Sentinel Shield precedents: **Nightshift Labs**, eighteen link, domain, DNS and signature pre-checks with per-call USDC pricing. Held on **AI-employee and team-brain** tools beside Cedric and Bidhelm: **Addness**, already dispositioned in an earlier sweep. Held on **social publishing and ads**, already dispositioned: **Apogee Ads**. Held on **travel eSIM** (SimoraGo, shibaSIM): **PuraSIM**. Held thin by inspection: **All My Ducks** (personal and household to-dos with promises), **GravityPort** (desktop asset library for AI-generated media), **ManaWG** (shared-flat expenses and cleaning rota), **Hutlists** (5,600 Alpine huts), **Movie Scene Map** (filming locations), and **Soundlink**, which answers **401** with a protected-resource document but publishes no description or capability anywhere this pass could read, so it is unjudged rather than refused.

## Core Listing Check

- **mcpservers.org** - `/servers/corpusiq-io` is still present in the freshly fetched twelve-sitemap canonical; the detail page answers the standing **403** to a direct fetch.
- **mcp.so** - not listed. All four direct slugs (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) answered **404**.
- **Glama** - **200** on `/mcp/connectors/io.corpusiq/multi-source-mcp`.
- **Smithery** - the registry API returned a server error rather than a result, so the listing is not confirmed this pass. A server error is never a delisting.
- **Official MCP registry** - four active versions of `io.corpusiq/multi-source-mcp` stand from the night read (`1.0.0` through **`1.0.3`**), with the 40+ business systems description in the active records.

## Counts

- Canonical: **19,733** against **19,733**, **+0** / **-0**. Ledger note: the night report's prose recorded **19,728** while its capture on disk carries **19,733** distinct server URLs, so the 19,728 figure is an earlier subset count; this pass diffs against the artifact, not the prose.
- Candidates evaluated: **22** (**10** from the mcp.so homepage, **12** from the submission queue). Catalogued **1**, held **21**.
- Guide tree: **1,107** directories before this pass, **1,108** after. **1,251** entries counting single-file guides before, **1,252** after.
