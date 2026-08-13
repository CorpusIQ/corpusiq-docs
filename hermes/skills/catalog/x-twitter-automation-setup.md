---
title: X/Twitter Automation Setup Guide
description: Design safe X/Twitter automation workflows for tweet search, reply reads, monitoring, posting, and agent-operated social media actions. From cosmicstack-labs/mercury-agent-skills (364⭐).
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/x-twitter-automation-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# X/Twitter Automation — Setup Guide

**Source:** [cosmicstack-labs/mercury-agent-skills](https://github.com/cosmicstack-labs/mercury-agent-skills) (364 ⭐)
**Skill:** `x-twitter-automation` — 10 installs (skills.sh)
**Category:** Social Media & Automation

## Installation

```bash
npx skills add cosmicstack-labs/mercury-agent-skills --skill x-twitter-automation
```

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.8+ |
| X/Twitter API credentials | OAuth 1.0a or API v2 Bearer token |
| xurl CLI | Hermes-native Twitter tool (bundled) |
| Rate limit awareness | X API: 1500 tweets/month (free), 500k (basic) |

## Capabilities

| Capability | Trigger | Description |
|-----------|---------|-------------|
| Tweet search | `search Twitter for {query}` | Search recent tweets by keyword, hashtag, or user |
| Reply monitoring | `check replies to {tweet}` | Read and analyze replies to specific tweets |
| Safe posting | `post to X` | Post tweets with rate-limit awareness and safety checks |
| Feed monitoring | `monitor Twitter timeline` | Track home timeline or list feeds for engagement opportunities |
| Agent-operated actions | `automate Twitter {action}` | Orchestrate multi-step Twitter workflows from Hermes Agent |

## CLI / Command Reference

```bash
# Install the skill
npx skills add cosmicstack-labs/mercury-agent-skills --skill x-twitter-automation

# Search tweets
hermes run x-twitter-automation --action search --query "hermes agent"

# Post a tweet (with safety checks)
hermes run x-twitter-automation --action post --content "Check out how Hermes Agent..."

# Monitor replies
hermes run x-twitter-automation --action replies --tweet-id 123456789
```

## CorpusIQ Use Cases

1. **Help-first engagement** — Search for operators asking about AI tooling, business automation, or growth challenges; reply helpfully without pitching
2. **Competitor monitoring** — Track mentions of competing platforms to understand positioning and gaps
3. **Content distribution** — Post UGC content, product updates, and thought leadership on schedule
4. **Lead discovery** — Find founders/operators discussing pain points that CorpusIQ solves
5. **Brand monitoring** — Track @corpusiq mentions and relevant industry conversations

## Safety Rules (Hard Constraints)

- **Never spam** — Rate limit: max 5 automated replies per hour
- **Help-first only** — All automated replies must solve a real problem before mentioning CorpusIQ
- **No bot-like behavior** — Randomize timing, vary response templates, stay human
- **Respect blocks/mutes** — Honor user boundaries; never re-engage blocked accounts
- **API limits** — Back off automatically when approaching rate limits

## Troubleshooting

| Issue | Solution |
|-------|----------|
| 401 Unauthorized | Verify Twitter API credentials in Hermes config |
| 429 Rate Limited | Skill auto-backs off; reduce query frequency |
| Posts not appearing | Check xurl configuration: `hermes config get twitter` |
| Content safety block | Review against help-first rules; remove sales language |

## Related Skills

- [twitter-gtm-find-skill](/hermes/skills/catalog/twitter-gtm-find-skill-setup/) — GTM/DevRel job scraping from X/Twitter
- [autonomous-helpful-presence-mining](/hermes/skills/) — CorpusIQ's help-first community engagement framework
- [corpusiq-social-cadence-engine](/hermes/skills/) — All-platform posting and engagement schedule

## Verification

```bash
# Verify installation
hermes skills list | grep x-twitter-automation

# Test search (dry-run)
hermes run x-twitter-automation --action search --query "test" --dry-run
```

---

*Catalog guide created July 30, 2026. Skill source: cosmicstack-labs/mercury-agent-skills.*
