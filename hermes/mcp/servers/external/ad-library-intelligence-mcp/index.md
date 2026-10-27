---
title: "Ad Library Intelligence MCP - Competitor Ads on Demand"
description: "Pull the actual ads a competitor runs on Meta, Google and LinkedIn, plus the ads.txt sellers behind a publisher, from one hosted endpoint with an API key."
category: Marketing / Ad Research
stars: n/a (free 50 calls, then $9 or $29 a month)
added: 2026-10-27
source: "live MCP probe on ad-library-intelligence.mcpize.run/mcp (initialize 401 Bearer token required) and the vendor listing at mcpize.com/mcp/ad-library-intelligence with its documented tool set, limits and pricing"
relevance: ★★★
tags: [competitor-ads, meta-ad-library, google-ads-transparency, linkedin-ads, ads-txt, creative-research, marketing]
last_updated: "2026-10-27"
---

# Ad Library Intelligence MCP

**Every competitor is already telling you what they are testing, in public, in the ad libraries - and the gap between knowing that and reading it has always been three scrapers and a spreadsheet.**

```
Server type: Remote (Streamable HTTP, hosted)
Endpoint:    https://ad-library-intelligence.mcpize.run/mcp
Transport:   JSON-RPC over POST
Auth:        Bearer API key issued by mcpize.com
Tools:       8, from the vendor's documented set
Pricing:     Free 50 calls a month, Pro $9 for 1,000, Business $29 for 5,000
Built by:    benthepythondev, published through mcpize
```

## Why This Matters for Operators

Meta, Google and LinkedIn all publish the ads that run on their networks. Practically nobody reads them, because each library has its own interface and none of them speaks to the others. The result is that competitive creative research is done once a year by an agency, from screenshots.

A server that returns the ads themselves - text, media, landing page, first and last date shown, and spend or reach where the platform publishes it - turns that into a weekly question: what is this competitor running now, and what changed since last month.

## What It Actually Does

`initialize` without a key returned HTTP 401 `{"jsonrpc":"2.0","error":{"code":-32603,"message":"Bearer token required"}}` - a JSON-RPC error rather than an HTML wall, which is the right shape for a client to surface.

| Tool | What comes back |
|---|---|
| `search_meta_ads` | Facebook and Instagram ads from the Meta Ad Library by keyword or Page id, with ad text, link, images, videos, platforms, start date, and spend and reach where Meta publishes them |
| `search_google_ads_transparency` | Ads from Google's Ads Transparency Center by domain, brand or advertiser id, with format, first and last day shown, and optional per-region impressions for EU ads |
| `search_linkedin_ads` | LinkedIn Ad Library ads by advertiser or keyword, with headline, text, media, optional landing page, impressions and targeting |
| `get_ads_txt` | Every authorised seller line of a publisher's `ads.txt` |
| `get_app_ads_txt` | The same for an app developer's `app-ads.txt` |
| `search_framer_marketplace`, `search_openverse_media`, `get_substack_posts` | Framer templates, openly licensed images and audio, and recent Substack posts |

Documented limits: at most 50 records and 10 domains or queries per call, and calls take 2 to 90 seconds depending on the library. Spend, reach and impressions exist only where the platforms publish them, which in practice means political and EU advertising.

## How It Is Contained

- **Public pages only.** Every tool reads what the platform already publishes; no account on the operator's side, no cookies, no logged-in session.
- **Metered, not subscription-trapped.** 50 calls a month free, then a flat monthly plan with an included call count, so the cost of a research routine is predictable before it runs.
- **Named limits in the tool contract.** 50 records per call is a hard ceiling, which stops one question from turning into an accidental crawl.
- **Failure is legible.** A missing key returns a JSON-RPC error with a message rather than a generic 401 page.

## Limitations Recorded

- No tool call was executed: the endpoint requires an mcpize-issued key, so the tool set comes from the vendor listing and the probe confirms only that the surface is live and gated.
- **Not in the official MCP registry.** The listing is on mcpize only, so there is no registry record to check versioning against.
- **Spend data is mostly political and EU.** For a typical commercial advertiser in the US, the value is the creative and the dates, not the budget.
- **Slow calls.** 2 to 90 seconds per call is long enough that an agent should be told to expect it rather than time out and retry.
- Around January 2027, the EU ad-library obligations widen, which will change what the Google and Meta tools can return for European advertisers - worth re-reading the listing before relying on the spend figures.

## FAQ

### Is this scraping?
It reads the public ad libraries through the publisher's own pages. There is no login, no cookie and no account on the operator's side.

### Can it tell me what a competitor spends?
Only where the platform publishes it, which is mostly political and EU advertising. For a commercial advertiser you get the creative, the landing page and the dates it has been running.

### What is the fastest useful question to ask it?
"Show me the ads HubSpot is running on LinkedIn right now" - the creative and the first-seen date together tell you both the message and how long they have kept paying for it.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Adspy MCP - paid ad library access](/hermes/mcp/servers/external/adspy-mcp/)
- [CorpusIQ connectors for advertising data](/hermes/mcp/)
