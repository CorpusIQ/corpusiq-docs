---
title: "MCP Server Discovery - October 26, 2026 (Midday Sweep)"
description: "A frozen listing and three finds that answered for themselves: keyless print-on-demand supplier prices, live GPU stock, and EV charging rows that cite."
last_updated: 2026-10-26
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october26-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 26, 2026 (Midday Sweep)

Seven hours after the morning pass, the listing had not moved at all. mcpservers.org served 17,522 servers at the 13:32Z reader stamp, the same page-one order as the morning read, and 119 slugs were read across pages 1 to 4. Breadth work on a frozen surface is repetition, which is why this pass spent its weight on the three places a delta still lands: the submission window, the cards that no earlier ledger had dispositioned, and the endpoints themselves.

The feed is worth a note on method. The reader proxy returned the sponsor rails and nothing else this cycle, so the 30 cards were read from the raw page with a browser user agent and a regex on the hydration payload. The newest card was already inside the morning dispositions, and the only two fresh timestamps were a media card from 16:17Z and a payment-card comparison surface from October 24 that the feed's position made look newer than it was.

## What Was Catalogued

Three entries earned guides, and each was driven rather than described.

[POD Benchmark MCP](/hermes/mcp/servers/external/podbenchmark-mcp/) is ten tools at `https://podbenchmark.com/api/mcp` with no auth at all, read-only at 120 requests per minute per IP. Two calls executed without a key: `list_suppliers` returned seven print-on-demand suppliers with Printful, Printify, Gelato, CustomCat, Prodigi, Inkthreadable and Fourthwall, the last two typed `direct` rather than marketplace, and `list_categories` returned destination US in USD with Apparel at 1,971 products of which 1,722 carry a price across six suppliers from $11.33, T-Shirts at 457 from $12.08 and Hoodies at 277 from $12.08. The comparison itself is `compare_product` on a canonical product id with a destination and currency, `get_product_options` for one size or colour, and `resolve_supplier_link`, which takes a pasted supplier URL from any of the seven and returns the normalized product. That last tool is what makes a fair comparison possible without a shared product identifier, and it is also the reason this entry reverses the August 26 hold on `BestPrintOnDemand`: the earlier candidate was a site-published price table, this one is a procurement surface.

[GPU Finder MCP](/hermes/mcp/servers/external/gpufinder-mcp/) answers keyless on both handshake methods, `initialize` returning `gpufinder` version `a6` and `tools/list` returning eight tools, with tool execution behind a free key of 60 operations a month. The interesting schema is `list_providers`, which carries each provider's **egress cost per GB and free egress allowance** beside its price range, and `get_market_snapshot`, which separates the cheapest listed offer from the cheapest offer actually observed in stock. `get_data_status` reports each provider's last success, consecutive failures and last error, and the site's own table shows one provider 30 hours stale beside another marked out of stock. Vendor numbers: 33 providers, 24 availability APIs, 96 models, data collected 43 minutes before the read, and 8x H100 quoted from $15.46/hr at Vast to $186.61/hr at Azure. This closes the FastGPU hold, whose reason was an endpoint nobody could verify from public pages.

[ChargingNear.me MCP](/hermes/mcp/servers/external/chargingnear-mcp/) is six read-only tools at `https://chargingnear.me/api/mcp`, keyless, over the US Department of Energy station records under CC-BY-4.0, and its own initialize instructions are a constraint rather than marketing: read-only access, cite `citation_url` when you use a result. Three calls were executed. `get_city_charging_stats` for `scottsdale-az` returned 179 stations, 16 DC fast and 162 Level 2 with the network mix. `get_state_charging_stats` for `arizona` returned 1,760 stations across 100 cities, 232 DC fast and 1,465 Level 2, ten networks named. `search_stations` returned real site records with per-level port counts, `J1772COMBO` connectors, access hours and a citation URL on every row.

## What Was Held

Of the 22 issues filed between `#6155` and `#6176` with no gaps: `simulator-use` and `Breakpane` as coding-agent infrastructure; `Objective Trust` and `369 Meter` as agent-payment plumbing; `Apparent` against the app-data class carried by `AppSigma`; `Flipvo Agent Tools` on dense overlap with the screening, carrier and licence classes the catalog already carries; the `mambalabsdev` quintet once as a vendor fleet this catalog has classed three times over; `FastAF` beside the scraping-vendor holds; `AuraStream` against the saturated market-data class; `Ashare` as publishing infrastructure; `AgentPad` as crypto; `BinaSmart` on geography; `backlink-guard` as SEO tooling; `HypeFox` inside the held media class; `LibrePass` as telecom retail; `AI Architectures` as a construction vertical; and `Staygreen` beside `Watchcron` as developer observability.

On the listing, `comparecloudcosts` held against the catalogued `Opencloudcosts` and the FinOps dispositions, `getaiso` against the AI-visibility class this window already carries through `CitedBy`, `geolint`, `LogNorm` and `Cite42`, and the remainder resolved to consumer verticals, site builders, media generation, agent security, communications surfaces and German-language assistants. Two cards served a 404 shell through the reader proxy and are recorded as such rather than as findings.

## Directory Status Re-Verified

- mcpservers.org: CorpusIQ listed at `/servers/corpusiq-io`, HTTP 200.
- Smithery: listed as `Cprusiq` with `unlisted` false.
- Glama: listed, but the public route moved. `https://glama.ai/mcp/servers/io.corpusiq%2Fmulti-source-mcp` now 301s to a search query, and the live page is `https://glama.ai/mcp/connectors/io.corpusiq/multi-source-mcp`, which returns HTTP 200 titled CorpusIQ - MCP Connector and invites the author to claim ownership by verifying the domain.
- mcp.so: absent on all four slug forms, all 404.

Sources: mcpservers.org `/all` pages 1 to 4 through the r.jina.ai reader proxy (13:32Z stamp, 119 slugs), mcp.so `/feed` page 1 from the raw page with a browser user agent (30 cards), the chatmcp/mcpso issue window `#6155` to `#6176` over the authenticated GitHub API, live JSON-RPC sessions on three endpoints with five executed tool calls, the Glama search page and connector route, the Smithery registry JSON and the vendor sites for GPU Finder and POD Benchmark.

Catalog 995 to 998 servers, guides 1,143 to 1,146.
