---
title: "HasData MCP - Marketplace and Web Data Gateway for Agents"
description: "Hosted web-data gateway from HasData: one MCP endpoint exposes 57 connector APIs over real estate (Zillow, Redfin), hospitality (Airbnb, Booking), hiring (Indeed, Glassdoor), local business (Yelp, YellowPages), e-commerce (Shopify, Amazon, Walmart), social (YouTube, TikTok, Instagram, Facebook) and search data (Google SERP, Maps, Trends, Flights, Scholar). API key auth at mcp.hasdata.com/mcp, credit-priced."
category: Data & Analytics / Market Intelligence
stars: "n/a (hosted, no public repo)"
added: 2026-08-30
source: "mcpservers.org /all pages 1-3 (Aug 30 night sweep; deferred as catch-up Aug 29 midday)"
relevance: ★★
tags: [mcp-server, market-data, real-estate, hospitality, hiring, ecommerce, serp, scraping, api-key]
---

# HasData MCP

**One hosted endpoint, 57 marketplace and web-data connector APIs.** HasData is a web-scraping API provider, and its MCP gateway exposes the connector catalogue as MCP tools: Zillow and Redfin real estate, Airbnb and Booking stays, Indeed and Glassdoor hiring, Yelp and YellowPages local business, Shopify, Amazon and Walmart e-commerce, YouTube, TikTok, Instagram and Facebook social data, plus Google SERP, Maps, Trends, Flights, Images, Scholar and Travel. The gateway is the infrastructure; the DATA each connector carries decides what an operator can answer with it.

```
Server type: Hosted (Streamable HTTP)
Endpoint: https://mcp.hasdata.com/mcp (connector selection: https://mcp.hasdata.com/api/mcp?apis=amazon,shopify)
Auth: API key via the x-api-key header (HASDATA_API_KEY; create keys at app.hasdata.com/api-keys)
Tools: 57 connector APIs, exposed per the connectors you select
Docs: docs.hasdata.com/mcp-server
Pricing: HasData API credits, per-API pricing (app.hasdata.com/apis)
Built by: HasData (hasdata.com)
```

## Why This Matters for Operators

Market intelligence usually means stitching five scraping tools together. HasData's MCP puts the connector catalogue behind one authenticated endpoint, so an agent can answer "what are comparable three-bedroom listings asking in this ZIP" and "what do competitors charge on Booking" from the same session.

First, **real estate and hospitality data.** `zillow_listing` and `zillow_property` (plus `redfin_listing` and `redfin_property`) cover for-sale, for-rent and sold listings with full property details; `airbnb_listing`, `airbnb_property`, `booking_place` and `booking_search` cover stays by location and dates. Structured JSON out.

Second, **hiring and local-business intelligence.** `indeed_job`, `indeed_listing`, `glassdoor_job` and `glassdoor_listing` answer compensation and demand questions; `yelp_place`, `yelp_reviews`, `yellowpages_place` and `yellowpages_search` cover local market presence.

Third, **search and e-commerce surfaces.** The `google_serp_*` family (news, shopping, product, events, AI-mode and AI overview), `google_maps_search`, `google_trends_search`, `google_travel_flights` and `google_travel_hotels` give market-signal reads; `shopify_collections`, `shopify_products` and the `amazon_*` family cover competitor catalogues.

## Tool Groups (57 connector APIs)

| Domain | Tools |
|--------|-------|
| Real estate | `zillow_listing`, `zillow_property`, `redfin_listing`, `redfin_property` |
| Hospitality | `airbnb_listing`, `airbnb_property`, `booking_place`, `booking_search` |
| Hiring | `indeed_job`, `indeed_listing`, `glassdoor_job`, `glassdoor_listing` |
| Local business | `yelp_place`, `yelp_reviews`, `yellowpages_place`, `yellowpages_search` |
| E-commerce | `shopify_collections`, `shopify_products`, `amazon_product`, `amazon_reviews`, `amazon_search`, `amazon_seller`, `amazon_seller_products` |
| Search and trends | `google_serp` (news, product, shopping, events, AI mode), `google_maps_search`, `google_maps_reviews`, `google_trends_search`, `google_travel_flights`, `google_travel_hotels`, `bing_serp`, `duckduckgo_serp` |
| E-commerce (Walmart) | `walmart_product`, `walmart_reviews`, `walmart_search` |
| Social and media | `youtube_channel`, `youtube_search`, `youtube_transcript`, `youtube_video`, `tiktok_comments`, `tiktok_posts`, `tiktok_profile`, `tiktok_search`, `instagram_posts`, `instagram_profile`, `facebook_profile` |
| Search (more) | `google_flights_flights`, `google_images_images`, `google_scholar_cite`, `google_scholar_scholar` |
| Generic | `web_scraping` |

Tool names recovered from the vendor's official MCP docs page (docs.hasdata.com/mcp-server); the catalogue grows per connector - check the docs for the current list.

## Verification (Aug 30, 2026)

- Vendor docs: docs.hasdata.com/mcp-server documents the endpoint, the x-api-key auth header and per-connector tool names
- Listed on mcpservers.org under hasdata/zillow-mcp, hasdata/airbnb-mcp and hasdata/booking-mcp (and more)
- Recorded as a future catch-up candidate in the Aug 29 midday sweep and resolved by this sweep

## Verification Update (Sep 10, 2026 night sweep)

- HasData published five per-connector hosted MCP listings on mcp.so: YouTube MCP Server (search, video metadata, channel data, timestamped transcripts - no YouTube API key required), TikTok MCP Server (profiles, videos, comments, creator search), Instagram MCP Server (public profiles and post feeds), Zillow MCP Server and Google Search MCP Server (organic results, AI Overview, People Also Ask, news, shopping). Each carries its own GitHub repo (HasData/youtube-mcp, tiktok-mcp, instagram-mcp, zillow-mcp, google-search-mcp).
- Official docs table now lists 57 connector APIs including the new `youtube_*` (4 tools), `tiktok_comments`/`tiktok_search`, `facebook_profile`, `walmart_*` (3 tools), `google_flights`, `google_images` and `google_scholar` families - table above refreshed to match.
- Docs confirm `?apis=` parameter filtering (e.g. `?apis=google_maps_search,web_scraping` exposes 2 tools instead of 57) and OAuth sign-in alongside the `x-api-key` header.

## Notes and Caveats

- Credit-priced per API: each connector burns HasData API credits; set budget caps in the HasData console before handing a key to an agent
- No anonymous mode: every call needs an API key; the anonymous initialize is refused
- Reseller data terms: HasData scrapes third-party platforms - review their data-usage terms per connector before production use
- Key hygiene: keys are created at app.hasdata.com/api-keys and scoped to the account, not per-connector

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Google Maps Scraper MCP - Live Maps Data for AI Agents](/hermes/mcp/servers/external/google-maps-scraper-mcp/)
- [Crustdata MCP Integration Guide](/hermes/mcp/servers/external/crustdata/)
- [LiveDataLink MCP - Live Public Data for AI Agents](/hermes/mcp/servers/external/livedatalink-mcp/)
