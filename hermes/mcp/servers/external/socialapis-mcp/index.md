---
title: "SocialAPIs MCP - Facebook and Instagram Data for Agents"
description: "47 read-only tools for Facebook and Instagram pages, posts, comments, Ads Library, Marketplace and reels, with a hosted endpoint or local npx install."
category: Marketing
stars: n/a (hosted platform, socialapis.io)
added: 2026-10-02
source: "mcp.so feed (socialapis-facebook-instagram-data)"
relevance: ★★★
tags: [marketing, social-media, facebook, instagram, ads-library, competitor-research, marketplace, scraping, remote-mcp]
---

# SocialAPIs MCP

**Facebook and Instagram data behind one API key, with no Facebook app review.** SocialAPIs exposes public Facebook and Instagram surfaces to an agent as 47 read-only tools: pages, posts, comments, groups, the Ads Library, Marketplace, profiles, reels, highlights and locations. There is no OAuth dance and no Meta developer app to register - you sign up, take a key, and point a client at the endpoint.

```
Server type: Remote (Streamable HTTP) or local (stdio via npx)
Auth: API key sent as an Authorization Bearer header (or x-api-token)
Endpoint: https://mcp.socialapis.io/mcp
Local package: @socialapis/mcp
Tools: 47 (all read-only)
Pricing: free tier of 200 calls per month; per-call credits shown in each tool response
Category: Marketing
Built by: SocialAPIsHub
```

## Why This Matters for Operators

The Facebook and Instagram surfaces that matter most for competitor and market work - the Ads Library, Marketplace pricing, page and post engagement, reel performance - are exactly the ones Meta makes hardest to reach programmatically. Getting them normally means a developer app, an app review, and a business verification. SocialAPIs strips that out: one key, one endpoint, structured JSON back.

Three operator workflows this unlocks:

- **Competitor ad research.** `facebook_ads_search` and `facebook_ads_archive_details` read the public Ads Library, so an agent can pull what competitors are actively running instead of what a keyword tool guesses they run.
- **Brand and page monitoring.** `facebook_get_page_posts`, `facebook_get_post_comments` and `instagram_get_profile_posts` give post cadence, engagement and comment volume - the raw signal for share-of-voice tracking.
- **Marketplace price tracking.** `facebook_marketplace_search` plus `facebook_marketplace_listing` and `facebook_marketplace_seller` cover listings, sellers and categories for resale and pricing work.

Every tool response carries a `meta` block with `creditsCharged` and `creditsRemaining`, so an agent can see the cost of each call it makes rather than discovering it on an invoice.

## Tools and Capabilities

All 47 tools are read-only. Beyond the Ads Library and Marketplace surfaces, the Facebook group covers page, post, video, reel, group and comment retrieval plus a set of `search_*` tools for pages, people, locations, posts and videos. The Instagram group covers profiles, posts, reels, highlights, audio-based reel lookup and location search.

Selected tool groups:

| Group | Representative tools | Purpose |
|---|---|---|
| Facebook pages and groups | `facebook_get_page_details`, `facebook_get_page_posts`, `facebook_get_group_posts` | Page and group content, videos and reels |
| Facebook posts and comments | `facebook_get_post_details`, `facebook_get_post_comments`, `facebook_get_comment_replies` | Post-level engagement and thread reading |
| Facebook Ads Library | `facebook_ads_search`, `facebook_ads_page_details`, `facebook_ads_keywords`, `facebook_ads_countries` | Active ad discovery and advertiser breakdowns |
| Facebook Marketplace | `facebook_marketplace_search`, `facebook_marketplace_listing`, `facebook_marketplace_seller`, `facebook_marketplace_categories` | Listing, seller and category data plus vehicles and rentals |
| Facebook search | `facebook_search_pages`, `facebook_search_people`, `facebook_search_locations`, `facebook_search_posts`, `facebook_search_videos` | Discovery across public surfaces |
| Facebook media and facts | `facebook_get_page_id`, `facebook_get_post_id`, `facebook_download_media` | ID resolution and media retrieval |
| Instagram profiles and posts | `instagram_get_profile_details`, `instagram_get_profile_posts`, `instagram_get_post_details` | Profile and post data |
| Instagram reels and highlights | `instagram_get_profile_reels`, `instagram_get_reels_by_audio`, `instagram_get_profile_highlights` | Reel performance and story highlight reading |
| Instagram discovery | `instagram_popular_search`, `instagram_get_location_posts`, `instagram_get_nearby_locations` | Popular queries and location-based content |

## Installation

Connect a remote-capable client to the hosted endpoint:

```
claude mcp add socialapis --transport http https://mcp.socialapis.io/mcp --header "Authorization: Bearer YOUR_API_KEY"
```

Clients that take a URL plus headers use this shape:

```json
{
  "mcpServers": {
    "socialapis": {
      "url": "https://mcp.socialapis.io/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

Tool listing works without a key, so a client can introspect the surface before you sign up. Tool calls require one.

## Configuration

The local stdio install runs the same 47 tools:

```json
{
  "mcpServers": {
    "socialapis": {
      "command": "npx",
      "args": ["-y", "@socialapis/mcp"],
      "env": { "SOCIALAPIS_API_KEY": "YOUR_API_KEY" }
    }
  }
}
```

The key can be passed as a command-line argument (`npx @socialapis/mcp YOUR_API_KEY`), through `SOCIALAPIS_API_KEY`, or via a `.env` file. `MCP_PROXY_URL` defaults to `https://mcp.socialapis.io` and `API_BASE_URL` to `https://api.socialapis.io` if you need to point at a different environment.

## See Also

- [Manifold MCP - Hosted Marketing Data for Agents](/hermes/mcp/servers/external/manifold-mcp/) - a broader marketing-data endpoint that also carries social and ad-library surfaces alongside SEO and AI visibility
- [MCP directory catalog](/hermes/mcp/servers/external/) - the full external server catalog

## FAQ

### Does SocialAPIs MCP need a Facebook developer account?

No. The server holds its own access to the public Facebook and Instagram surfaces, so you authenticate with a SocialAPIs API key instead of registering a Meta app or completing app review.

### Can an agent call the tools without an API key?

Tool listing works without a key, but any tool call needs one. A free key covers 200 calls per month and is issued from the SocialAPIs dashboard.

### Are any of the 47 tools write operations?

No. Every tool is read-only, covering retrieval and search across pages, posts, comments, groups, the Ads Library, Marketplace, profiles, reels, highlights and locations.
