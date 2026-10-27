---
title: "MCP Server Discovery - October 21, 2026 (Midday Supplement)"
description: "One feed card posted past the midday cut plus three carried cards settled at the endpoint: Shopify speed and fees, influencer vetting."
last_updated: 2026-10-24
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october21-2026-midday-supplement/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 21, 2026 (Midday Supplement)

A supplement about an hour after the midday capture. The directories did not move inside the hour, so the delta came from two places: one feed card posted past the midday cut at 17:16Z, and three cards the midday report recorded as carried prior dispositions that had no ledger entry behind them. Every catalogued entry was settled by running the endpoint.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [Shopify Speed Check MCP](/hermes/mcp/servers/external/shopify-speed-check-mcp/) | Commerce and Retail | Free keyless remote server at `https://tools.skaidigital.com/mcp` from Skai Digital, a headless Shopify agency. Unauthenticated `POST initialize` returned HTTP 200 (`skai-shopify-tools` 1.0.0) and `tools/list` returned three tools. `check_shopify_store_speed` runs PageSpeed Insights on mobile and desktop with real-user Core Web Vitals, returns bottlenecks ranked and labels a headless estimate with its assumptions, in 10 to 90 seconds and cached 24 hours. `detect_shopify_store` reads the public page only and reports theme store or headless plus the theme name, verified on allbirds.com. `calculate_shopify_fees` prices Basic, Grow, Advanced and Plus with break-even sales between plans and the requirements only Plus covers: at $250,000 monthly GMV and an $85 average order it returned Advanced at $7,766 a month as the cheapest qualifying plan, Basic excluded on staff account limits, with break-evens at $30,000, $135,000 and $808,750. Gap named rather than closed: the speed class is here through GTmetrix and Sorank, no entry is Shopify-specific, and nothing attributed a slow storefront to the apps a merchant pays for. |
| [IQFluence MCP](/hermes/mcp/servers/external/iqfluence-mcp/) | Marketing | Influencer vetting and media planning at `https://mcp.iqfluence.io/mcp`, OAuth 2.1 in the browser or an API key for scripts. Unauthenticated `POST initialize` returned HTTP 401 `invalid_token`, and the authorization server metadata returns 200 with authorize, token, register and revoke endpoints, authorization_code and refresh_token grants and PKCE S256. Fifteen documented tools with a credit cost on each paid step: `search_influencers` over 455M profiles with the first three rows free, `unlock_search_results` at 0.02 credits an account, `get_influencer_report` at 1 credit with fake-follower signals and audience quality, `compare_influencers` and `audience_overlap` at 1 credit, `build_media_plan` at 1 credit per creator for expected views, engagements, CPM and cost per engagement, `get_contacts` at 0.04, post and hashtag reads at 0.02 a page, plus balance, campaigns and report lists. The assistant states each paid step and asks above 5 credits, a daily credit limit is settable per key, and requests are written to a history. Starter $199 for 300 credits, Pro $299 for 500, yearly at 20 percent off, top-ups $0.79. Gap named rather than closed: creator entries here reconcile payouts or publish, and the creator-finder class was held twice against thin scrapers. |

## Surface Results

- mcp.so `/feed` page 1 recaptured at 18:00Z: 30 cards, one posted inside the hour (Shopify Speed Check at 17:16Z). Three cards the midday report carried as prior dispositions (FERS, Zeptap, IQFluence) had no ledger entry, so all three were read to detail level and closed with a recorded reason.
- mcpservers.org `/all` pages 1 to 3 through the reader proxy: 89 slugs, unchanged inside the hour. Five served 404 shells (Mozarkai, Polign, Rollinggo AI, Lucyd Trade, Woven Video).
- No issue-window pass this cycle; the midday pass closed #5887 an hour earlier.

## Held This Cycle

FERS held as an engineering computation vertical with no operator data surface, and as a solver the hosted server builds and checks but does not run. Zeptap held as desktop and agent automation infrastructure on the ShadowCursor precedent, its bare-slug detail page a 404 which is the author-path class. Octobooks held against the bookkeeping class carried by Accountable and SuperBooks, with its read, propose and upload scopes recorded for a revisit if that class thins. Wine Labs held as a single vertical market data surface, BEON PASS as an access wallet, Agents Handbook as an agent-playbook knowledge surface. The fifteen username-shell cards are the sitemap-fresh-but-not-live class.

## Catalog Count

965 to 967 servers, 845 to 847 guides.
