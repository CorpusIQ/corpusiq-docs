---
title: "Sonar ASO MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Official Sonar MCP server with 25 App Store Optimization tools for AI agents - keyword research, rank tracking, review mining and revenue estimates"
category: Marketing
stars: n/a (new listing)
added: 2026-08-18
source: mcp.so homepage
relevance: ★★
tags: [aso, app-store, google-play, keyword-research, rank-tracking, reviews, revenue-estimates, marketing]
---

# Sonar ASO MCP

**The official Sonar MCP server — App Store Optimization tools for AI agents: look up apps, research keywords with difficulty and popularity scores, audit ASO metadata, mine reviews, estimate revenue, and run daily rank tracking across the iOS App Store and Google Play.** Stateless tools run free without a key (30 requests/day); workspace tracking and write tools unlock with an API key. Data is real Apple and Google store data, not estimates.

```
Server type: stdio via npm
Auth: Optional SONAR_API_KEY (aso_ prefix); free mode without a key
Install: npx -y @sonarapp/mcp
Tools: 25 (10 stateless read, 8 workspace read, 7 write)
Pricing: Free mode (rate-limited); prepaid credits from $10; Indie $19/mo; Agency $99/mo
Category: Marketing / ASO
Built by: Sonar (trysonar.app, repo: trysonar/mcp)
```

## Why This Matters for Operators

App revenue is decided by keyword positions nobody checks daily because the checking is tedious. Sonar's MCP puts live store data inside the agent, so the loop closes in chat: research keywords the app can actually rank for, audit the listing, track positions daily, mine competitor complaints, and size niches with revenue estimates — both stores, all countries, on one plan.

**The free tier is real.** Five stateless tools work without any key: `sonar_app_search`, `sonar_app_lookup`, `sonar_app_aso_score`, `sonar_app_extract_keywords`, and `sonar_keyword_suggestions` share 30 requests/day per IP, and `sonar_keyword_metrics` gets 5 keywords/day. Prepaid API credits start at $10 (1,000 credits) with 50 free on signup — built for agents and scripts, no subscription.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `sonar_app_lookup` | App metadata by store ID |
| `sonar_app_search` | Search apps by keyword, store ranking order |
| `sonar_app_aso_score` | 0-100 ASO audit with itemized checks |
| `sonar_app_extract_keywords` | Extract target keywords from a listing |
| `sonar_app_reviews` | Fetch reviews with rating filters and sorting |
| `sonar_app_revenue` | Monthly revenue estimate with methodology |
| `sonar_keyword_search` | Keyword research: difficulty, popularity, related terms |
| `sonar_keyword_metrics` | Difficulty + popularity, single or bulk |
| `sonar_keyword_suggestions` | Live store autocomplete suggestions |
| `sonar_top_charts` | Top free/paid/grossing with day-over-day movement |
| `sonar_list_apps` / `sonar_get_app` | Tracked apps with snapshot history (Indie plan) |
| `sonar_app_rankings` / `sonar_keyword_rankings` | Daily rank history for apps and keywords |
| `sonar_competitor_keywords` / `sonar_competitor_landscape` | Competitor keyword gap analysis + AI briefs |
| `sonar_track_keywords` / `sonar_scan_competitor` | Start tracking and run discovery scans (write) |

Workspace reads need an Indie plan (trial counts) with a `read`-scope key; write tools need the `write` scope — the server enforces both and returns a 403 explaining what to fix.

## Installation

```bash
claude mcp add sonar -e SONAR_API_KEY=aso_your_key_here -- npx -y @sonarapp/mcp
```

```json
{
  "mcpServers": {
    "sonar": {
      "command": "npx",
      "args": ["-y", "@sonarapp/mcp"],
      "env": {
        "SONAR_API_KEY": "aso_your_key_here"
      }
    }
  }
}
```

## Configuration

| Variable | Required | Default | Description |
|---|---|---|---|
| `SONAR_API_KEY` | no | — | Sonar API key (`aso_...`); free mode without it |
| `SONAR_API_URL` | no | `https://trysonar.app` | Override for self-hosting or staging |

Keys come from trysonar.app/developers. Credit packs: 1 credit per stateless call, 10 per keyword research call, 1 per app ID for bulk revenue. Credits never expire.

## Business Relevance

- **Indie developers** get enterprise-grade ASO research (Sensor Tower/AppTweak class) at $19/month
- **Growth operators** automate weekly listing audits and keyword gap analysis inside the agent
- **Agencies** run 50 apps and 10,000 keywords with white-label client reports on the Agency plan
- **Pre-launch teams** size niches with revenue estimates before committing build time

## Integration with CorpusIQ

CorpusIQ has no app-store connector — its 40+ connectors cover web analytics, commerce, ads, and finance. Sonar fills the ASO gap: keyword positions, store listings, reviews, and app revenue on both stores.

The composed workflow: Sonar's MCP answers "where do we rank and what do competitors own on the stores," while CorpusIQ answers "what happens after install — sessions, conversions, revenue, ad spend" from GA4, Shopify, and ad connectors. Store performance and downstream monetization finally sit in the same agent session.

## Limitations

- Early-stage package: npm downloads ~760/month, repo at 0 stars (Aug 2026)
- Free mode is rate-limited (30 requests/day/IP, 5 keyword metrics/day)
- Workspace tracking and writes require the Indie plan or an active trial
- Data covers iOS App Store and Google Play only — no third-party Android stores
