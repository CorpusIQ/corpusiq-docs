---
title: "Hermes Tweet — X/Twitter Automation Plugin for Hermes Agent"
description: "Install and configure the hermes-tweet plugin for native X/Twitter automation through Hermes Agent."
---

# Hermes Tweet Setup Guide

**Repo:** [Xquik-dev/hermes-tweet](https://github.com/Xquik-dev/hermes-tweet)
**Stars:** ⭐18 | **License:** MIT | **Language:** Python
**Install:** `npx skills add Xquik-dev/hermes-tweet -g -y`

## Overview

Hermes Tweet is a native Hermes Agent plugin for X/Twitter automation built on Xquik. It lets your Hermes agents post tweets, read timelines, search Twitter, and engage with content — all through the Hermes plugin system.

**Key capabilities:**
- Post tweets with media attachments
- Read home timeline and user timelines
- Search Twitter by keyword, hashtag, or user
- Reply, like, and retweet
- Rate-limit aware with automatic backoff

## Prerequisites

- Hermes Agent v0.15.0+
- Python 3.10+
- X/Twitter account with API access (via Xquik)

## Installation

```bash
# Via npx (recommended)
npx skills add Xquik-dev/hermes-tweet -g -y

# Via git clone + manual install
git clone https://github.com/Xquik-dev/hermes-tweet.git
cd hermes-tweet
pip install -e .
cp -r hermes_tweet ~/.hermes/plugins/
```

## Configuration

1. Get your Xquik API credentials from [xquik.dev](https://xquik.dev)
2. Add to your Hermes config:

```yaml
# ~/.hermes/config.yaml
plugins:
  hermes-tweet:
    api_key: ${XQUIK_API_KEY}
    api_secret: ${XQUIK_API_SECRET}
    access_token: ${XQUIK_ACCESS_TOKEN}
    access_secret: ${XQUIK_ACCESS_SECRET}
```

3. Set environment variables:
```bash
export XQUIK_API_KEY="your_key"
export XQUIK_API_SECRET="your_secret"
export XQUIK_ACCESS_TOKEN="your_token"
export XQUIK_ACCESS_SECRET="your_token_secret"
```

## Usage

The plugin auto-loads when Hermes starts if configured. Use these skill commands:

```python
# Post a tweet
hermes_tweet.post("Check out CorpusIQ for AI-powered business operations!")

# Read timeline
timeline = hermes_tweet.home_timeline(limit=20)

# Search
results = hermes_tweet.search("hermes agent", limit=10)

# Reply to a tweet
hermes_tweet.reply(tweet_id="1234567890", text="Great point!")
```

## Verification

```bash
# Test the plugin loads
hermes plugins list | grep hermes-tweet

# Run a quick smoke test
python3 -c "from hermes_tweet import TwitterPlugin; print('OK')"
```

## Pitfalls

- Rate limits: X API enforces 50 posts/24h per user. The plugin auto-throttles but monitor `remaining` headers.
- Xquik is NOT affiliated with X Corp — API behavior may differ from official X API v2.
- Media uploads require chunked upload for files >5MB.
- Auth tokens expire after 2 hours — the plugin handles refresh automatically.

## Related Skills

- [xurl CLI Setup](/hermes/skills/catalog/xurl-setup/)
- [X/Twitter Scraper Setup](/hermes/skills/catalog/x-twitter-scraper-setup/)
