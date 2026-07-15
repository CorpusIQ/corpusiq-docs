---
title: "XActions MCP — X/Twitter Automation Without API Fees"
description: "Integration guide for nirholas/xactions. Complete X/Twitter automation via MCP: scrapers, posting, analytics, growth tools. No API fees."
category: mcp
tags: [mcp-server, twitter, x, social-media, automation, hermes-agent]
last_updated: 2026-07-15
mcp_server: nirholas/xactions
stars: 384
source: mcpservers.org
---

# XActions MCP — X/Twitter Automation Without API Fees

**Repository:** [nirholas/xactions](https://github.com/nirholas/xactions)
**Stars:** 384 ★
**Category:** Social Media / Automation
**License:** MIT
**Last Updated:** 2026-07-14

## What It Does

Complete X/Twitter automation toolkit operating through web scraping (no API fees). Includes MCP server for AI agents (Claude, GPT, Hermes), CLI tools, and browser scripts. Covers the full growth workflow: scraping, posting, analytics, auto-follow, auto-like, commenting, and unfollow management.

### Tools Provided

| Tool | Description |
|------|-------------|
| `post_tweet` | Post a tweet (text + media) |
| `search_tweets` | Search Twitter by keyword, hashtag, user |
| `get_user_profile` | Fetch profile data by username |
| `get_user_tweets` | Get recent tweets from a user |
| `get_trending` | Get trending topics by location |
| `follow_user` | Follow a user |
| `unfollow_user` | Unfollow a user |
| `like_tweet` | Like a tweet by ID |
| `retweet` | Retweet a tweet |
| `get_notifications` | Fetch recent notifications |
| `get_analytics` | Profile analytics (followers, engagement) |
| `auto_unfollow_non_followers` | Bulk unfollow those who don't follow back |

## Comparison: XActions vs xurl CLI vs Postiz

| Feature | XActions MCP | xurl CLI | Postiz |
|---------|-------------|----------|--------|
| **Method** | Web scraping | X API v2 | API |
| **API cost** | Free | $100/mo Basic | Varies |
| **Risk** | Account flagging risk | Safe (official API) | Safe |
| **Posting** | Yes | Yes | Yes |
| **Scheduling** | No | No | Yes |
| **Analytics** | Basic | Good | Full |
| **Multi-platform** | X only | X only | X + LinkedIn + Instagram |
| **Best for** | Growth hacking, low budget | Reliable posting | Professional management |

**Verdict:** XActions is a growth-hacking tool — use for research, competitor analysis, and bulk operations where API costs would be prohibitive. For production posting, xurl or Postiz remain safer choices due to official API compliance.

## Setup for Hermes Agent

### Prerequisites

- Node.js 18+
- Python 3.10+ (for some scraper components)
- X/Twitter account credentials

### Step 1: Clone and Install

```bash
cd ~/mcp-servers
git clone https://github.com/nirholas/xactions.git
cd xactions
npm install
```

### Step 2: Configure Auth

XActions uses cookie-based authentication (extracted from browser session):

```bash
# Option A: Export cookies from your browser
# (Chrome: use "EditThisCookie" extension, export as JSON)
# Save to ~/.xactions/cookies.json

# Option B: Use credentials directly (less reliable)
export X_USERNAME="your-username"
export X_PASSWORD="your-password"
export X_EMAIL="your-email@example.com"
```

### Step 3: Register with Hermes

```bash
hermes mcp add xactions -- node ~/mcp-servers/xactions/mcp-server/dist/index.js
```

Or via `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  xactions:
    command: node
    args:
      - /home/hermes/mcp-servers/xactions/mcp-server/dist/index.js
    env:
      X_COOKIES_PATH: /home/hermes/.xactions/cookies.json
```

### Step 4: Verify

```bash
hermes mcp list | grep xactions
```

## Use Cases

1. **Competitor monitoring:** Track competitor tweet frequency, engagement, and topics
2. **Community growth:** Auto-follow users in target niches, engage with relevant content
3. **Trend research:** Pull trending topics by geo for content ideation
4. **Audience analysis:** Analyze follower demographics and engagement patterns
5. **Bulk operations:** Unfollow non-reciprocators, clean up following list

## Risk Warnings

**IMPORTANT:** XActions operates via web scraping, which violates X/Twitter's Terms of Service. Risks include:

- **Account suspension:** X actively detects and bans scraping-based automation
- **Rate limiting:** Aggressive scraping triggers IP blocks
- **Legal exposure:** ToS violation could result in legal action (rare but possible)
- **Detection vectors:** X monitors request patterns, timing, and browser fingerprints

### Mitigation Strategies

- Use a dedicated growth account (never your main brand account)
- Add random delays between actions (3-15 second range)
- Limit daily actions (under 100 follows/unfollows per day)
- Rotate user agents and browser profiles
- Use residential proxy IPs (not datacenter IPs)
- Monitor account health daily — stop at first warning

**Internal note:** CorpusIQ's main X account (@corpusiq) should NEVER use XActions. Reserve for growth/experimental accounts only.

## Limitations

- No scheduling or queuing — real-time execution only
- Cookie sessions expire (typically 7-30 days) — requires re-authentication
- X UI changes can break scrapers without warning
- No DM support
- Media uploads are less reliable than text-only tweets
- Rate detection is probabilistic — cannot guarantee safety

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `Login failed` | Cookies expired — re-export from browser |
| `Rate limited` | Reduce action frequency, rotate IP |
| `Tweet not posting` | Check for X UI changes; update to latest version |
| `Scraper returning empty` | X may have changed page structure — check repo issues |

## Related Guides

- [OpenTweet MCP](/hermes/mcp/servers/external/opentweet-mcp/) — Alternative Twitter MCP server
- [CorpusIQ Social Cadence Engine](/hermes/mcp/servers/external/) — Multi-platform posting schedule
- [Cross-Platform Commenting Engine](/hermes/mcp/servers/external/) — Automated engagement across platforms
