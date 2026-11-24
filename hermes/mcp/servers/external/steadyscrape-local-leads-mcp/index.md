---
title: "SteadyScrape Local Leads MCP - Businesses With No Site"
description: "Four read-only tools over Google Maps, Trustpilot and Tripadvisor with lead filters, a hard per-call charge cap and reviewer names removed."
category: "Marketing"
stars: "n/a (vendor-hosted; runs on Apify Actors)"
added: 2026-11-23
source: "A canonical mcpservers.org arrival at /servers/steadyscrape/local-leads-mcp stamped 2026-11-24T00:21Z; keyless initialize and tools/list on https://mcp.steadyscrape.dev/leads/mcp answering 200 as steadyscrape-local-leads 0.1.0 with four tools; a find_local_businesses call refused 401 -32001 'Sign in with Apify to use this tool.'; the protected-resource document at https://mcp.steadyscrape.dev/.well-known/oauth-protected-resource/leads/mcp and the Apify authorization-server document, both read 2026-11-24; the vendor page https://mcp.steadyscrape.dev/leads"
relevance: "★★★"
tags: [local-seo, lead-generation, google-maps, reviews, prospecting, apify, oauth, remote-mcp, marketing]
last_updated: "2026-11-23"
---

# SteadyScrape Local Leads MCP

**In local services the best prospect list is a filter, not a directory: businesses with no website, or an unclaimed profile, or a rating below four with more than fifty reviews.** Those are the rows a Google Maps search will not give you and a checklist will. SteadyScrape Local Leads exposes four read-only tools over Google Maps businesses and their reviews, with the lead filters as first-class parameters and a hard maximum charge on every call.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.steadyscrape.dev/leads/mcp
Server name: steadyscrape-local-leads 0.1.0
Auth:        OAuth 2.1 against Apify, scope full_api_access
Billing:     per business, per review and per report, at Apify Store list price
```

## What was measured

```
initialize  -> 200  {"name":"steadyscrape-local-leads","title":"SteadyScrape Local Leads","version":"0.1.0"}
tools/list  -> 200  4 tools
tools/call  -> 401  {"jsonrpc":"2.0","error":{"code":-32001,
                    "message":"Sign in with Apify to use this tool."}}
```

`find_local_businesses` with `{"categories": ["coffee shop"], "city": "Austin"}` was the call that refused, so the tool path is live behind the gate rather than absent from it. The protected-resource document at `/.well-known/oauth-protected-resource/leads/mcp` answers **200** with `resource` `https://mcp.steadyscrape.dev/leads/mcp`, `authorization_servers: ["https://console-backend.apify.com"]`, `scopes_supported: ["full_api_access"]` and `resource_documentation` pointing at the vendor's own page.

## The four tools

| Tool | Returns | Price |
| --- | --- | --- |
| `find_local_businesses` | businesses for 1-5 categories in a city, postal code, country or radius, with lead filters: name, category, address, coordinates, Maps link, place_id, website, claimed flag, rating, review count, status, first-seen date. **No phone numbers.** | $0.015 per run + $0.002 per business, $0.005 per business when a lead filter is used |
| `business_reviews` | recent reviews of 1-5 businesses from Google Maps, Trustpilot or Tripadvisor: rating, title, text, date, owner reply, plus rating stats and monthly trend. No reviewer names. | $0.0005 per Google review, $0.0004 Trustpilot, $0.001 Tripadvisor, + $0.005 per run |
| `review_summary` | complaint and praise themes with counts and excerpts, a summary, suggested actions, rating distribution and trend, for 1-3 businesses | $0.03 per business report + the reviews analysed + $0.005 per run |
| `get_results` | the result of a run that took longer than about two minutes | free |

`find_local_businesses` carries seventeen parameters and the filters are the product: `website`, `unclaimed_only`, `rating_below`, `min_rating`, `reviews_below`, `min_reviews`, `first_seen_within_days`, `business_status`, plus `city`, `postal_code`, `country_code`, `coordinates`, `radius_km`, `sort_by`, `include_hours` and `limit`. `business_reviews(targets, reviews_per_business, sort_by, google_location, language)` and `review_summary(targets, reviews_to_analyze, sort_by, google_location, language)` read the reviews. The caps are **50 businesses per call**, **100 reviews per call**, **3 businesses and 200 reviews each** for a summary, and **60 tool calls per minute per account**. Business search answers in **5 to 30 seconds**; review analysis takes **1 to 3 minutes** and hands back a `run_id` after about two.

## The privacy contract, in the vendor's own terms

This is the part of the surface that makes it usable for prospecting rather than a data-protection incident, and it is stated precisely enough to hold them to:

- The tools return **business facts only**. Phone numbers and free-text business descriptions are **removed**.
- **Reviewer names, profile links, avatars and photos are never returned**, and reviewer names are **masked inside review text**.

So the lead list is genuinely a list of businesses you can walk into, not a list of people you can cold-call, and the review corpus is quotable without republishing somebody's identity. Both restrictions cut against the usual pitch for a scraper and both are in the buyer's favour: a list of business names with no phone numbers is a list that does not need a consent basis per row.

Every call also sets a hard maximum charge for its run based on the limits asked for, and the vendor states that the maximum is what it says: at most 50 businesses or 100 reviews per call. A run cannot silently cost more than the limits imply.

## What a list actually costs

Worked from the published rates, because a per-business price is easy to read and hard to budget:

- **500 no-website businesses in one metro**, filtered, in ten calls of 50: ten runs at **$0.015** plus 500 businesses at **$0.005** = **$2.65**.
- **A review pull of 100 Google reviews** on three competitors: **$0.05** in reviews plus three runs at **$0.005** = **$0.065**.
- **Three competitor review summaries** at 200 reviews each, the expensive path: **$0.03 x 3** for the reports, **$0.0005 x 600** for the reviews analysed and **$0.005 x 3** for the runs = **$0.405**.

Against a data broker selling a local-business list at a few cents a row, this is not cheaper; it is *current*, filtered by facts the broker cannot see, and re-runnable next month for the price of one lunch.

## How to connect

1. Add `https://mcp.steadyscrape.dev/leads/mcp` as a remote Streamable HTTP server. In Claude Code: `claude mcp add --transport http steadyscrape-leads https://mcp.steadyscrape.dev/leads/mcp`, then `/mcp`.
2. Sign in with the Apify account to be billed, and know that the grant is `full_api_access` on that whole account.
3. Start narrow: one category, one city, `website` absent, `reviews_below` set, `limit` at 10. Confirm the rows against Maps by hand before scaling to 50.
4. Drive `review_summary` at one business before three. It is the slowest and the most expensive call, and it is the one that produces the sentence a salesperson actually uses.

## What this guide can and cannot certify

Measured: the endpoint, both handshake methods, the refusal and its code, the protected-resource document, the four tools with their parameters and annotations, the published prices, caps, latencies and privacy rules. Not measured: any returned row, because every call needs an Apify session. So no coverage claim in this entry is a count: how many Austin coffee shops carry no website is exactly the number a buyer would want and exactly the number this pass could not obtain.

## Verdict

**Three stars, and the highest operator value of the three SteadyScrape servers in this catalogue.** The filters are the product, the privacy rules are unusually explicit, the per-call ceiling is stated, and the whole surface costs about a dollar to test properly. What is missing is the only thing that cannot be read from outside: how complete the Maps coverage actually is in a given city on the day it is asked.
