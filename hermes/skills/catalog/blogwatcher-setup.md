---
title: "Blogwatcher — RSS/Atom Feed Monitoring for Hermes"
description: "Install and configure the blogwatcher-cli skill for RSS/Atom feed monitoring on Hermes Agent. Monitor blogs, news feeds, and content sources without API keys."
category: catalog
---

# Blogwatcher — RSS/Atom Feed Monitoring Setup Guide

Monitor blogs and RSS/Atom feeds directly from your Hermes agent. The `blogwatcher` skill wraps the `blogwatcher-cli` tool, enabling automated content discovery, trend monitoring, and competitive intelligence — all without API keys or third-party services.

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) via [skills.sh](https://www.skills.sh/nousresearch/hermes-agent/blogwatcher)

## Installation

```bash
npx skills add nousresearch/hermes-agent --skill blogwatcher
```

## Prerequisites

- Hermes Agent installed and running
- Node.js 18+ (for npx)
- No API keys required — blogwatcher-cli reads RSS/Atom feeds directly

## Configuration

The skill auto-discovers feeds. To add custom feeds:

```bash
# Add a feed to monitor
blogwatcher add https://example.com/feed.xml

# List monitored feeds
blogwatcher list

# Check for new posts since last poll
blogwatcher check
```

## Common Use Cases

### 1. Competitive Intelligence
Monitor competitor blogs and product updates:
```bash
blogwatcher add https://competitor.com/blog/feed.xml
blogwatcher add https://another-competitor.com/rss
```

### 2. Industry News Tracking
Stay on top of AI/ML papers, tech news, and industry announcements:
```bash
blogwatcher add https://blog.google/technology/ai/rss/
blogwatcher add https://openai.com/blog/rss.xml
blogwatcher add https://www.anthropic.com/blog/rss.xml
```

### 3. Content Discovery for Social Media
Find shareable content for automated social posting:
```bash
blogwatcher check --since 24h --format json | jq '.[].title'
```

## Integration with Hermes Cron Jobs

Create a cron job to check feeds daily:

```bash
hermes cron create \\
  --name "blogwatcher-daily-check" \\
  --schedule "0 8 * * *" \\
  --command "blogwatcher check --since 24h" \\
  --deliver telegram
```

## Limitations

- Only supports RSS 2.0 and Atom 1.0 formats
- No authentication for private feeds (use curl + auth headers as fallback)
- Rate-limited by source servers (respects `429` responses)
- No full-text extraction (headlines + summaries only)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `blogwatcher: command not found` | Install via npx first: `npx skills add nousresearch/hermes-agent --skill blogwatcher` |
| Feed returns empty | Check feed URL in browser — site may use JavaScript rendering |
| Feed times out | Source server may be blocking headless requests. Add `User-Agent` header |
