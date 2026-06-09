---
title: Social Media Automation
description: Automated cross-platform social media operations. X, Reddit, Discord, LinkedIn, TikTok, Instagram posting and monitoring.
---

# Social Media Automation

CorpusIQ agents manage presence across X, Reddit, Discord, HN, LinkedIn, TikTok, and Instagram via automated posting and community engagement.

## Platform Architecture

```
                    ┌─ X/Twitter (xurl CLI + Upload-Post API)
                    ├─ Reddit (PRAW OAuth)
Content Pipeline ───┼─ Discord (native API)
                    ├─ LinkedIn (API + Playwright fallback)
                    ├─ TikTok/Instagram (Postiz CLI → manual post)
                    └─ HN (Playwright browser automation)
```

## Cross-Platform Posting

Via [Postiz CLI](https://postiz.com):

```bash
postiz post \
  --platforms twitter,reddit,linkedin \
  --content "How operators think about data pipelines" \
  --media /path/to/image.png \
  --schedule "2026-06-10T14:00:00Z"
```

## Platform-Specific Setup

### X/Twitter
```bash
# Post via xurl CLI
xurl tweet "Five patterns we see in operator onboarding" --media screenshot.png

# Post via Upload-Post API (for media)
curl -X POST https://upload-post.api/posts \
  -H "Authorization: Bearer $API_KEY" \
  -d '{"text": "...", "media": "..."}'
```

### Reddit (PRAW)
```python
import praw
reddit = praw.Reddit(
    client_id="...",
    client_secret="...",
    user_agent="CorpusIQ/1.0"
)
reddit.subreddit("dataengineering").submit(
    title="How we handle schema evolution at scale",
    selftext="..."
)
```

### Discord
```python
# Send to specific channel
await channel.send("New feature deployed: ...")
```

## Content Rotation

Daily rotating content across 5 avatars:
| Avatar | Platform | Content Type |
|--------|----------|-------------|
| Technical | X, Reddit, HN | Infrastructure, architecture |
| Operator | X, LinkedIn | Pain points, solutions |
| Product | X, Discord | Feature updates, roadmap |
| Growth | LinkedIn, X | Results, playbooks |
| Human | TikTok, Instagram | Behind the scenes |

## Rate Limiting & Anti-Bot

| Platform | Rate Limit | Pivot Strategy |
|----------|-----------|----------------|
| Reddit | Subreddit-specific | Detect 429 → move to Discord |
| X | 500 posts/3h | Stagger posting times |
| LinkedIn | 100 requests/day | API first, Playwright fallback |
| HN | Aggressive anti-bot | Playwright with stealth |

## Monitoring

Crons check for:
- New mentions across all platforms
- Community questions without responses
- Competitor mentions
- Trending topics in our space

## Help-First Doctrine

All UGC content must:
1. Answer a real operator problem FIRST
2. Mention CorpusIQ only if relevant
3. Link to useful resources
4. Never sell, always help

---

*← [Video](/hermes/content-ops/video/) | [Engagement](/hermes/content-ops/engagement/) →*
*↑ [Content Ops](/hermes/content-ops/)*
