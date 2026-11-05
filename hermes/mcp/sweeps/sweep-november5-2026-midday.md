---
title: "MCP Server Discovery - November 5, 2026 (Midday Sweep)"
description: "Midday pass where the sitemap and the feed both stood still and the submission queue carried the window: one parcel-and-grid siting server catalogued."
last_updated: 2026-11-05
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november5-2026-midday"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 5, 2026 (Midday Sweep)

## Summary

This pass fired on the **10:00 MST** tick, seven hours after the **03:00 MST night** read, and both named discovery surfaces were flat. The twelve-sitemap canonical returned **19,513** server URLs, the same count as the 04:31 MST capture, with **2** additions and **2** removals and both removals pairing exactly with an addition whose namespace prefix had been dropped. The mcp.so homepage parsed to **172** cards whose newest timestamp `2026-11-05T06:47:30Z` is the night pass's own stamp, so no card was new. mcpservers.org `/all` refused every read for the second consecutive pass (**403** direct, **401 03** bad IP reputation through the reader proxy).

That left the submission queue as the whole window: **36** items from `#6773` to `#6808`, read with bodies in one authenticated call, **21** of them a single author's utility fleet. **One** server was catalogued, a parcel-level site-feasibility surface with a utility and grid layer the catalog did not have.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| mcpservers.org twelve-sitemap canonical | 14 sitemaps fetched directly with plain urllib, **43,181** inline locale prefixes stripped, set difference against the 04:31 MST capture | **19,513** server URLs against **19,513**, **2** additions and **2** removals, both removals a namespace-prefix flip of the addition beside it. Zero genuine change |
| mcpservers.org `/all` | direct fetch with a browser user agent, then the reader proxy | **403** Cloudflare on the direct read, **401 03** bad IP reputation on the reader. Not read |
| mcp.so homepage | direct fetch with a browser user agent, `recentServers` parsed by `createdAt` | **172** cards, newest `2026-11-05T06:47:30Z`, **zero** above the night stamp |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included, one call | **36** issues in the window `#6773` to `#6808`, **21** of them one author's fleet |
| Official MCP registry API | `search` on the catalogued candidate | resolved `co.korzy/korzy` **1.0.0**, published `2026-11-05T13:41:35Z`, remote `https://api.korzy.co/mcp` |
| Vendor surface for the candidate | docs, authentication, pricing, datasets and `openapi.json` | `korzy.co/docs/mcp/` **200** (16 tools), `docs/authentication/` **200**, `pricing/` **200**, `datasets/` **200**, `openapi.json` **200** (**193,888** bytes, **34** routes with `x-korzy-credits`), keyless `initialize` **401** |

## New Servers Catalogued

### Korzy MCP - Parcel, Utility and Grid Siting Data

Relevance: HIGH. **Endpoint verified as gated** (keyless `initialize` returns **401** `Sign in or provide a valid Korzy credential`), so the tool surface is documented rather than driven.

Korzy registers as `co.korzy/korzy` **1.0.0** at `https://api.korzy.co/mcp` and publishes **16** tools. The entry exists because of what sits around the parcel rather than the parcel itself:

- `get_site_context` returns **water and sewer service areas** for a point, the treatment plants that serve it, and nearby data-center projects.
- `get_utility_record` reads one water, sewer, treatment, gas or fiber record with standardised attributes.
- `get_transfer_capacity` returns **total and available transfer capability in MW** for a regional grid interface and date.
- `get_power_plant` returns a plant and its generators; `get_plant_energy_history` adds generation, fuel, outages and inventory.
- `get_environment_context` returns mapped flood and wetland layers plus nearby cleanup sites; `get_parcel_terrain` runs slope and elevation across a parcel.
- `get_data_center` returns one project with capacity evidence and a dated timeline.
- `search_parcels`, `get_parcel`, `get_logistics_context` and `get_regional_energy` complete the read surface.

The commercial terms were read from the vendor's own spec rather than quoted from a marketing page: the OpenAPI document carries an `x-korzy-credits` block on all **34** routes, so a parcel or address lookup costs **1** credit, a point context **2** with a **1 to 10** range priced per ten records, `include_owner=true` doubles the parcel and site calls, utility and project records cost **1**, and the energy reads cost **50** with coal receipts at **10**. Plans are **$49** a month (or **$490** a year) at 3,000 credits with extra at **$16** per 1,000, and **$199** a month (or **$1,990** a year) with unlimited seats.

Limits recorded in the guide: United States only, point and address lookups with area search still to come, no free tier (the endpoint answers **402** `subscription_required` with no active plan even though three summary tools cost zero credits), and the `mcp:read` and `api:read` scopes are separate with **403** outside a key's scope.

## Read and Held

The window was dominated by one author. **21** submissions from `mambalabsdev` (**#6782** to **#6802**) cover an email verifier, a whois lookup, a Substack scraper, a Reddit thread scraper, a Threads keyword search, an ATS jobs feed, a LinkedIn jobs feed, a Product Hunt launches feed, recent funding rounds, an app-store review monitor, an AI answer visibility tracker and six list-builder tools. Each lands in a class already carried here, so the fleet is held as one line under the single-author rule.

Individually evaluated and held, each with the class that answers it:

| Submission | What it is | Held on |
| --- | --- | --- |
| `#6807` JaKonto | Danish accounting over e-conomic, Dinero and Billy; keyless `initialize` **200** as `jakonto`, five read-only tools | geo-niche accounting (DokladBot, Taokeh, Kvickd, Amore Fortnox, Mighty, Zeno, Grand Livre, Nextesy, Pohoda) |
| `#6805` getwork.dev | employer ATS job feeds, no auth | jobs data (ATS Jobs, CareJobs.Now, Applystead, RobotTraining.jobs) |
| `#6804` Stackurity | software inventory with CVE, CISA KEV and EPSS posture | security review (VulX Watch, TrustScan, kosa8) |
| `#6780` Growth Radar | Google and AI search audit on a keyless free server | visibility saturation (geolint, LogNorm, Tracetify, Sorank, HiBot, Serpel) |
| `#6774` Shipbook | mobile and server log debugging | observability |
| `#6777` EZO Watcher | self-hosted monitoring the agent configures and proves | monitoring (Cronitor, Runheed, uptrack) |
| `#6773` Desktop Steward | scoped file access on a local Mac or Windows machine | local files and agent infrastructure |
| `#6781` EXTREMELY agency | controls a local fleet of agents | agent orchestration |
| `#6775` OMX for Hyperliquid | perpetuals execution with pre-trade limits | trading and agent payments |
| `#6803` Solana Alpha x402 | pay-per-call Solana market data over x402 | trading and agent payments (FiatDock, CoinVello, SnapEX Pay) |
| `#6779` RoomLab | 19 property-photo rendering tools | media generation |
| `#6778` Feedough Prompt Generator | prompt construction tool | prompt tooling, no operator data |
| `#6776` Piratex | Russian-language Reels and TikTok trends | single-market creator vertical |
| `#6808` DataXAPI | pay-per-call social data across Douyin, Xiaohongshu, TikTok, WeChat, X | scraping and social data (LurkAPI, Scrape.ly, Apify-actor hold) |

## Core Listing Check

- **mcpservers.org**: LISTED. `/servers/corpusiq-io` is present in the twelve-sitemap canonical; the detail page itself answers **403** to a direct read, which is the platform block and not a delisting.
- **Glama**: LISTED. `https://glama.ai/mcp/connectors/io.corpusiq/multi-source-mcp` returns **200**, title **CorpusIQ - MCP Connector**, canonical on the connectors route, description reading 40+ business systems.
- **Official MCP registry**: `io.corpusiq/multi-source-mcp` with the `https://mcp2.corpusiq.io/mcp` remote. The description still reads 30+ business systems against a catalog that now states 40+, which is metadata drift to correct at the next publish.
- **Smithery**: not confirmed this pass. The registry API answered `{"error":"An unexpected error occurred"}` on two calls and the Smithery server listing returned **308** then **404** on the redirect, which is a routing change and never a delisting signal.
- **mcp.so**: NOT LISTED. All four direct slug forms (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) return **404**, and the paid route stays declined under the no-payment rule, so it is not retried.

## Counts

Guide tree **1,102** directories before this pass, **1,103** after; **1,246** entries counting single-file guides before, **1,247** after.
