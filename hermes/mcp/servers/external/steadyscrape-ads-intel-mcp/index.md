---
title: "SteadyScrape Ads Intel MCP - Competitor Ad Libraries"
description: "Four read-only tools over Google's Ads Transparency Center and TikTok's Top Ads library, priced per ad in the buyer's own Apify account."
category: "Marketing"
stars: "n/a (vendor-hosted; runs on Apify Actors)"
added: 2026-11-23
source: "A canonical mcpservers.org arrival at /servers/steadyscrape/ads-intel-mcp stamped 2026-11-24T00:21Z; keyless initialize and tools/list on https://mcp.steadyscrape.dev/ads/mcp answering 200 as steadyscrape-ads-intel 0.1.0 with four tools; a find_google_advertisers call refused 401 -32001 'Sign in with Apify to use this tool.'; the protected-resource document at https://mcp.steadyscrape.dev/.well-known/oauth-protected-resource/ads/mcp and the Apify authorization-server document, both read 2026-11-24; the vendor page https://mcp.steadyscrape.dev/ads"
relevance: "★★★"
tags: [competitive-intelligence, advertising, google-ads, tiktok-ads, ad-transparency, apify, oauth, remote-mcp, marketing]
last_updated: "2026-11-23"
---

# SteadyScrape Ads Intel MCP

**Every competitor's ad library is already public. The work is not finding the ads, it is asking a question of them in the same breath as the rest of the research.** SteadyScrape Ads Intel puts Google's Ads Transparency Center and TikTok's Creative Center behind four read-only tools, and prices the answer per ad rather than per seat: an advertiser search is three tenths of a cent per account and a thousandth of a dollar per ad.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.steadyscrape.dev/ads/mcp
Server name: steadyscrape-ads-intel 0.1.0
Auth:        OAuth 2.1 against Apify, scope full_api_access
Billing:     per advertiser account and per ad, at Apify Store list price
```

## What was measured

The handshake is open and the calls are not, the same split the vendor's SEO server uses:

```
initialize  -> 200  {"name":"steadyscrape-ads-intel","title":"SteadyScrape Ads Intel","version":"0.1.0"}
tools/list  -> 200  4 tools
tools/call  -> 401  {"jsonrpc":"2.0","error":{"code":-32001,
                    "message":"Sign in with Apify to use this tool."}}
```

`find_google_advertisers` with `{"names": ["Notion"]}` was the call that refused. The protected-resource document at `/.well-known/oauth-protected-resource/ads/mcp` answers **200** with `resource` set to `https://mcp.steadyscrape.dev/ads/mcp`, `authorization_servers: ["https://console-backend.apify.com"]` and `scopes_supported: ["full_api_access"]`, and the issuer's RFC 8414 document offers authorization code, refresh and device grants with PKCE **S256**.

## The four tools

| Tool | Returns | Price |
| --- | --- | --- |
| `find_google_advertisers` | advertiser accounts matching 1-5 company names: name, advertiser ID, verification, country, approximate ad count, related domains | $0.003 per advertiser account |
| `google_advertiser_ads` | ads a company has run on Google Search, YouTube, Shopping, Maps and Play: format, first and last shown, days running, still running, preview image, Transparency Center link | $0.001 per ad |
| `tiktok_top_ads` | top-performing ads from Creative Center's public Top Ads library: caption, brand when shown, CTR and likes as published, video links | $0.0008 per ad, + $0.0012 for details |
| `get_results` | the result of a run that took longer than about two minutes | free |

Parameters: `find_google_advertisers(names, region, max_per_name)`, `google_advertiser_ads(targets, region, platform, ad_format, last_shown_within_days, date_from, date_to, limit)`, `tiktok_top_ads(countries, period_days, industries, objectives, languages, include_details, limit)`, `get_results(run_id)`.

The caps are set per call and they are the part to read before planning a sweep: at most **40 Google ads per target**, **3 targets per call**, **5 names per advertiser search**, **5 countries and 50 ads per TikTok call**, three time windows (7, 30 or 180 days) for TikTok, and **60 tool calls per minute per account**. A full competitor set of three domains at 40 ads each is **$0.12**, plus three advertiser searches at **$0.009**; a TikTok category pull of 50 ads is **$0.04**. Calls usually answer in **5 to 30 seconds**, and the vendor states that searches finding nothing are not billed for results.

## What it does not do

The vendor is unusually precise about the boundary and it is worth repeating without decoration: these tools **read public ad-library data only**. They do not create, buy, serve, place or target ads, and they return no sponsored content. There is no spend figure, no impression count, no audience, no bid and no conversion anywhere in the surface, because those are not in the public libraries either. Anyone planning to use this to estimate a competitor's media budget is estimating from ad counts and run lengths, and should say so out loud.

One behaviour recorded from the vendor's own documentation rather than observed: a **domain** lookup can return other advertisers Google associates with that domain, while an **advertiser ID** returns only that account's ads. That asymmetry is the difference between a clean count and a count that includes resellers, partners and unrelated businesses sharing a shell domain, so a comparison across competitors should be run on advertiser IDs.

## The billing account is the real permission

`full_api_access` on the Apify account is the only scope offered. The tool set is harmless, but the token is not scoped to it: the same session that reads public ad libraries can run every other Actor in the account. Connect a dedicated Apify account, or accept that the assistant holds a key to the whole surface. This is the second server in the catalogue whose permission boundary lives in the account rather than the token, and the pattern is worth recognising because a client's consent screen will not show it.

## How to connect

1. Add `https://mcp.steadyscrape.dev/ads/mcp` as a remote Streamable HTTP server. In Claude Code: `claude mcp add --transport http steadyscrape-ads https://mcp.steadyscrape.dev/ads/mcp`, then `/mcp`.
2. Sign in with the Apify account to be billed.
3. Ask for one advertiser by name first (`find_google_advertisers`), take the advertiser ID it returns, and drive `google_advertiser_ads` from the ID rather than the domain.
4. Set `last_shown_within_days` and `platform` on the first ad pull. Without them the call spends its budget on the oldest ads in the archive.

## What this guide can and cannot certify

Measured: the endpoint, both handshake methods, the refusal with its code, the protected-resource document, the four tool names with their schemas and annotations, the published prices, caps and latencies, and the stated boundary of read-only public-library access. Not measured: any response body, because every call requires an Apify session, and therefore no ad record, date or count in this guide is an observation of a real competitor.

## Verdict

**Three stars.** This is the cheapest honest way to ask what a competitor is running, and the marketing around ad-intel tools usually promises more than the public libraries contain; this one does not. What it lacks is proof: the guide can certify the price, the schema and the gate, and the first paying reader is the one who finds out whether an advertiser search on their own brand returns the account they know exists.
