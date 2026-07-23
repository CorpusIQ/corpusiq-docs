---
title: Reddit Research API — Semantic Search & B2B Lead Discovery for Hermes Agents
description: Access Reddit's full data archive via reddapi.dev. Semantic search, trend analysis, and AI-powered B2B lead scoring. 2.8K + 1.3K installs across two skills. Zero Reddit rate limits.
---

# Reddit Research & Leads — Setup Guide

**Source:** [lignertys/reddit-research-skill](https://skills.sh/lignertys/reddit-research-skill) (4.1K+ combined installs)
**Category:** Research / Lead Generation
**Quality Tier:** 🟡 Beta

Two skills in one repo providing Reddit data access without Reddit's API rate limits. **reddapi** offers semantic search across millions of posts and comments, subreddit discovery, and trend analysis. **reddit-leads** uses AI-powered lead scoring (0-100) to find B2B prospects actively expressing buying intent across 50K+ subreddits.

Key advantage: This is a third-party service, not Reddit official — so there are **no rate limits, no daily quotas, and 24/7 availability**. 1024D vector search matches on meaning, not just keywords.

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **reddapi** | 2.8K | Semantic search, trend analysis, subreddit discovery |
| **reddit-leads** | 1.3K | AI-powered B2B lead discovery with intent scoring |

---

## Installation

```bash
npx skills add lignertys/reddit-research-skill --skill reddapi
npx skills add lignertys/reddit-research-skill --skill reddit-leads
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **API Key** | Sign up at [reddapi.dev](https://reddapi.dev) — Free: 3 searches/mo, Lite $19.9/mo (500 calls), Starter $49/mo (5K), Pro $99/mo (15K) |
| **Environment** | `export REDDAPI_API_KEY="your_key"` |

---

## Key Capabilities

### Semantic Search (reddapi)
Natural language search across millions of Reddit posts — no keyword matching, meaning-based:

```bash
# Market research
curl -X POST "https://reddapi.dev/api/v1/search/semantic" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" \
  -d '{"query": "best productivity tools for remote teams", "limit": 100}'

# Pain point discovery — "I wish there was an app that"
curl -X POST "https://reddapi.dev/api/v1/search/semantic" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" \
  -d '{"query": "I wish there was an app that", "limit": 100}'

# Competitor complaints
curl -X POST "https://reddapi.dev/api/v1/search/semantic" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" \
  -d '{"query": "COMPETITOR_NAME problems complaints", "limit": 200}'
```

### Trend Analysis (reddapi)
Discover trending topics with engagement metrics and sentiment:

```bash
curl "https://reddapi.dev/api/v1/trends" \
  -H "Authorization: Bearer $REDDAPI_API_KEY"
```

Response includes: `post_count`, `total_upvotes`, `avg_sentiment` (-1 to 1), `trending_keywords`, `growth_rate`.

### B2B Lead Discovery (reddit-leads)
AI scores every post 0-100 on buying intent with 5 lead type categories:

| Lead Type | Signal |
|---|---|
| **pain_point** | User describing a problem, looking for solution |
| **solution_request** | Actively asking "what tool should I use for X" |
| **complaint** | Frustrated with current tool — switching signal |
| **feature_request** | Wants something their tool doesn't have |
| **comparison** | Evaluating options — ready to buy |

### Subreddit Discovery (reddapi)

```bash
# List popular subreddits
curl "https://reddapi.dev/api/subreddits?limit=100" \
  -H "Authorization: Bearer $REDDAPI_API_KEY"

# Get specific subreddit info
curl "https://reddapi.dev/api/subreddits/programming" \
  -H "Authorization: Bearer $REDDAPI_API_KEY"
```

---

## Quick Start — Hermes Agent

```bash
# Set API key
export REDDAPI_API_KEY="your_key"

# Discover trending topics in SaaS
curl "https://reddapi.dev/api/v1/trends" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" | python3 -m json.tool | head -30

# Find leads for "AI business tools"
curl -s -X POST "https://reddapi.dev/api/v1/leads/search" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "AI business operations tools for SMB", "limit": 10}' | python3 -m json.tool
```

---

## Verification

```bash
# Test API key
curl -s "https://reddapi.dev/api/me" -H "Authorization: Bearer $REDDAPI_API_KEY"

# Run a quick search
curl -X POST "https://reddapi.dev/api/v1/search/semantic" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" \
  -d '{"query": "test", "limit": 1}' | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'OK: {d.get(\"total\",0)} results')"
```

---

## Notes

- **No Reddit API limits**: reddapi.dev is a third-party index — unlimited QPS, no daily quotas
- **Use cases for CorpusIQ**: Market research, competitive analysis, pain point discovery, B2B lead generation for business operators
- **Lead scoring**: 0-100 with industry auto-detection — filter for scores >70 for warmest prospects
- **Free tier**: 3 searches/month — sufficient for evaluation. Lite ($19.9/mo) for production use
- **Related skills**: reddit-praw-automation, help-first-community-engagement
