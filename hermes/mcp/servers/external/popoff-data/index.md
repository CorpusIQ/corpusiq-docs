---
title: "PopOff Data MCP - Reality-TV Social Analytics for AI Agents"
description: "Hosted PopOff Data MCP server for reality-TV social analytics: Instagram and TikTok follower time series at roughly 30-minute resolution, cast follow/unfollow graphs, engagement rates, trend detections, and citation-ready season CSV exports across shows like Love Island, The Traitors, and Real Housewives. API-key remote HTTP, 12 tools."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-08-25
source: "mcp.so GitHub issue #3754"
relevance: ★★
tags: [mcp-server, social-analytics, entertainment, instagram, tiktok, influencer]
---

# PopOff Data MCP

**The paid analytics layer for reality-TV social data.** PopOff.tv tracks Instagram and TikTok follower growth for reality TV cast members; the PopOff Data product exposes that dataset to AI agents over MCP. Agents get follower time series at roughly 30-minute resolution, cast follow/unfollow graphs, engagement rates, trend detections, and citation-ready season CSV exports - for every tracked show and season, including ended-season archives.

```
Server type: Remote Streamable HTTP (hosted)
Endpoint: https://popoff.tv/mcp
Auth: API key (popoff_sk_...) as a bearer Authorization header or x-api-key header; OAuth access tokens also accepted
Tools: 12 (list_shows, get_show, list_episodes, get_cast, get_contestant, get_follower_history, get_follow_graph, get_follow_events, get_trend_events, get_engagement, export_season_csv, get_usage)
Registry: tv.popoff/data
Pricing: $79/month flat with 5,000 calls included, then $0.02 per call; REST and MCP share one meter
```

## Why This Matters for Operators

Reality-TV talent is a sponsorship and audience market: brands, agencies, and talent managers price cast members by follower trajectory, not snapshot counts. PopOff's 30-minute-resolution time series and Follow Watch graphs turn that pricing from guesswork into a query. Season CSV exports are built for citation, so an analyst can hand a producer or client a file with provenance instead of a screenshot. The same key drives the REST API at popoff.tv/v1, so non-agent workflows can read the identical dataset.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `list_shows` | List tracked reality shows and seasons |
| `get_show` | Detail for one show or season, including archive status |
| `list_episodes` | Episodes for a season |
| `get_cast` | Cast members for a show or season |
| `get_contestant` | Profile for one cast member |
| `get_follower_history` | Instagram/TikTok follower time series at ~30-minute resolution |
| `get_follow_graph` | Cast follow/unfollow relationships (Follow Watch) |
| `get_follow_events` | Individual follow and unfollow events |
| `get_trend_events` | Detected follower-growth trend events |
| `get_engagement` | Engagement rates for a cast member |
| `export_season_csv` | Citation-ready CSV export for a full season |
| `get_usage` | Call usage against the subscription meter |

The server also exposes the full API reference as a readable resource and ships two prompt templates (season_social_report, contestant_deep_dive).

## Installation

Subscribe at popoff.tv/data; the API key is issued immediately after checkout. Then register the endpoint with the key attached:

```shell
claude mcp add --transport http popoff https://popoff.tv/mcp
```

Store the key in the client's credential store and send it as the authorization header; the same key also works on the REST API at https://popoff.tv/v1.

## Configuration

- One key covers both REST and MCP; calls from both meter into a single shared pool.
- Airing and upcoming seasons remain free on the public JSON API (popoff.tv/api/docs); the Data API adds ended-season archives and premium metrics.
- Every Data subscription includes consumer Premium access on the site; media licensing and custom data deals go through the contact form.

## Business Relevance

- **Sponsorship valuation:** price cast partnerships from follower trajectories, not follower counts.
- **Audience intelligence:** growth windows and trend events for campaign timing.
- **Editorial research:** follow-graph dynamics and engagement for entertainment publications.
- **Data licensing:** citation-ready CSVs for client deliverables.

## Integration with CorpusIQ

PopOff exports pair with CorpusIQ connectors for the campaign side of entertainment marketing: join follower data with GA4 or Meta Ads performance, budget sponsorship spends in QuickBooks, and keep cast shortlists in Airtable or Notion so social evidence and commercial decisions share one workspace.

## Limitations

- Paid subscription required ($79/month, 5,000 calls, then $0.02 per call).
- Reality-TV niche: value concentrates in talent, sponsorship, and entertainment-media workflows.
- Hosted service with no public repo; anonymous probes return 401 (endpoint liveness verified).
- Tool list comes from the vendor's submission and docs pages; exact names were not enumerable without a key.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Social Glass MCP - Cultural Intelligence for Brand and Research Teams](/hermes/mcp/servers/external/social-glass-mcp)
