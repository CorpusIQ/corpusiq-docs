---
title: "API Direct MCP - CorpusIQ Docs"
description: Search public social, news, and local-business data across 13 platforms with 68 MCP tools and 60+ ready-made playbooks for lead-gen, recruiting, and due diligence. Pay-as-you-go per request.
category: Marketing
stars: n/a (new listing)
added: 2026-08-14
source: mcp.so
relevance: ★★★
tags: [social-media, data, search, linkedin, lead-gen, market-research, news, remote-mcp]
---

# API Direct MCP

**Remote MCP server (Streamable HTTP, API key)** — one endpoint for searching and reading public data across 13 platforms: LinkedIn, X/Twitter, Facebook, Reddit, YouTube, Instagram, Threads, TikTok, Truth Social, forums, news, web search, and Google Maps. Built by Josh Waller (apidirect.io). 68 tools plus 60+ ready-made skill playbooks that chain them into concrete outcomes — competitor conquest, just-funded outreach windows, layoff-wave recruiting, due-diligence dossiers. Pay-as-you-go per request, no subscription.

```
Server type: Remote (Streamable HTTP)
Auth: API key (also accepted as X-API-Key or Authorization header)
Endpoint: https://apidirect.io/mcp?token=YOUR_API_KEY
Tools: 68 (platform search, profile/post detail, skills layer, batch)
Pricing: Pay-as-you-go per request (typically $0.005–$0.006 per page on read endpoints); no subscription
Category: Data & Analytics (filed under Marketing)
Built by: API Direct (apidirect.io)
```

## Why This Matters for Operators

Public social and local-business data has always been valuable and always been painful to collect. Thirteen different platforms, thirteen different auth walls, rate limits, and scrapers that break whenever a site changes markup. The result is that lead-gen, competitive monitoring, and reputation work gets done manually, occasionally, or by tools that only cover one platform.

**API Direct collapses all thirteen into one API key and one MCP endpoint.** The agent asks for LinkedIn posts by founders at Series-A companies, X replies to a competitor's launch tweet, Google Maps reviews of a local acquisition target, or news coverage of a crisis — and gets back structured JSON with engagement metrics, sentiment options, and citations, all billed per request.

The differentiator is the skills layer. `list_skills` returns 60+ playbooks — expert recipes with the non-obvious filters already encoded (author title, company mentions, AI sentiment, freshness windows). `get_skill` returns a step-by-step recipe with the caller's inputs filled in. The agent stops improvising raw searches and starts running "competitor conquest," "churn intent," or "outage early warning" as a single outcome-shaped call.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_skills` / `get_skill` | Browse and run 60+ ready-made playbooks: lead-gen, recruiting, competitive intelligence, investing, PR/crisis, product insights, OSINT/due diligence |
| `search_linkedin` | Search LinkedIn posts with filters: author, author title, author company, mentions_company, mentions_member, industry; returns engagement metrics and optional AI sentiment |
| `linkedin_person_posts` / `linkedin_post_details` | Recent posts by a person or full detail for one post by URL |
| `linkedin_company_details` / `linkedin_company_posts` / `search_linkedin_companies` | Company page data, company posts, and keyword company search |
| `search_linkedin_jobs` / `linkedin_job_details` | Job listings with salary, location, industry, and experience level — usable as hiring/expansion/funding signals |
| `search_twitter` / `search_twitter_users` | Post and user search on X |
| `twitter_user_profile` / `twitter_user_tweets` / `twitter_user_followers` / `twitter_user_following` | Profile, timeline, and graph data for X accounts |
| `twitter_verified_followers` / `twitter_tweet_details` / `twitter_tweet_retweets` / `twitter_tweet_quotes` / `twitter_tweet_comments` | Verified-follower extraction and per-tweet engagement deep dives |
| `twitter_trends` | Current trending topics by location |
| `search_reddit` / `search_reddit_comments` / `search_reddit_users` | Post, comment, and user search across Reddit |
| `search_youtube` / `search_youtube_channels` / `get_youtube_comments` / `youtube_channel_details` / `youtube_video_details` | Video, channel, and comment data on YouTube |
| `search_instagram` / `search_instagram_users` / `instagram_user_profile` / `instagram_user_posts` / `instagram_post_details` | Post and profile data on Instagram, including reels and carousels |
| `search_threads` / `search_threads_users` / `threads_user_profile` / `threads_user_posts` | Threads post and profile data |
| `search_tiktok` / `search_tiktok_users` / `tiktok_user_profile` / `tiktok_video_details` | TikTok discovery with watermark-free playback URLs |
| `facebook_page_details` / `facebook_page_posts` / `facebook_page_photos` / `facebook_page_videos` / `facebook_page_reels` / `facebook_page_reviews` | Facebook page surface in full |
| `facebook_group_details` / `facebook_group_posts` / `facebook_post_comments` / `search_facebook_posts` / `search_facebook_pages` / `search_facebook_videos` / `search_facebook_events` / `search_facebook_locations` | Groups, comments, and location-scoped Facebook search |
| `search_forums` / `search_news` / `search_web` | Forum posts, thousands of news sources, and Google organic results with country/language targeting |
| `google_ai_mode` | Structured conversational replies from Google's AI Mode with citation links |
| `search_places` / `place_details` / `place_reviews` / `place_photos` | Google Maps local-business data: ratings, hours, reviews, photos, and contact scraping |
| `batch_requests` | Up to 100 API Direct requests in one concurrent call — free to invoke, each item billed at its endpoint's rate |

## Installation

```bash
claude mcp add api-direct --transport http "https://apidirect.io/mcp?token=YOUR_API_KEY"
```

Per-client walkthroughs are published on the mcp.so listing page; the endpoint is the same for every client. Sign up at apidirect.io to get an API key.

## Configuration

```json
{
  "mcpServers": {
    "api-direct": {
      "type": "http",
      "url": "https://apidirect.io/mcp?token=YOUR_API_KEY"
    }
  }
}
```

The key can alternatively be sent as an `X-API-Key` or `Authorization` header. Pay-as-you-go credit meter — no subscription required.

## Business Relevance

- **Founders and sales leads** get competitor-conquest lists, just-funded outreach windows, and local buying-intent capture without paying for a seat in a social-listening suite
- **Recruiters and hiring managers** source talent by title and company, intercept layoff waves, and verify candidate signal from public posts
- **Investors and deal sourcers** run due-diligence dossiers, adverse-media sweeps, and cross-platform identity resolution from one tool call
- **Marketing operators** monitor brand mentions, share of voice, and detractor radar across thirteen platforms, with AI sentiment on every result
- **Local-service operators** pull Google Maps ratings, reviews, and owner contact data for acquisition lists and reputation audits

## Integration with CorpusIQ

API Direct feeds the top of the funnel; CorpusIQ closes and measures it. A composed workflow: `get_skill` (local-buying-intent-capture) surfaces prospects talking about a pain point, `search_linkedin` and `search_twitter` resolve who they are and who they work for, then CorpusIQ's HubSpot connector records them as contacts with the social context attached, Klaviyo runs the nurture sequence, and GA4 + Stripe measure whether the social-sourced cohort actually converts. Every lead keeps its provenance — which post, which platform, which playbook — so attribution survives from first signal to first invoice.

For competitive intelligence, API Direct's market-map and pricing-objection playbooks complement CorpusIQ's Ahrefs and Semrush connectors: the SEO connectors show what a competitor ranks for, API Direct shows what their customers complain about in public.

## Limitations

- Brand new listing (Aug 2026) — no long track record yet
- Pay-as-you-go pricing means unbounded agents can burn credits; set spend caps before wiring it into autonomous workflows
- Data is public-only — no authenticated/private feeds, no DMs, no posting (read-only by design)
- Platform availability can shift as underlying sites change; individual endpoint coverage varies
- Live tool list is served from the endpoint — the 68-tool count and table above come from the published listing, verify after connecting

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
