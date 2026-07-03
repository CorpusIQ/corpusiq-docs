---
title: "OpenTweet MCP — Twitter/X Management for AI Agents"
description: "Connect OpenTweet to Hermes Agent. Manage X (Twitter) accounts — post, search, engage, and analyze — directly from AI agents. Marketing automation for X/Twitter operators."
category: mcp
tags: [mcp-server, opentweet, twitter, x, social-media, marketing, posting, engagement]
last_updated: 2026-07-03
---

# OpenTweet MCP Server ★ New (July 3)

## Overview

OpenTweet MCP (`opentweet-io-twitter-mcp-server`) provides AI agents with full Twitter/X management capabilities. Post tweets, search content, analyze engagement, and manage your X presence — all through natural language. Built for marketers, social media managers, and operators who live on X.

**Key advantage**: X/Twitter management becomes agentic. Instead of scheduling posts in a dashboard, composing threads manually, and checking analytics separately, operators can manage their entire X presence through their AI agent.

## Key Features

- **Post management**: Compose, schedule, and publish tweets and threads
- **Search & discovery**: Search tweets by keyword, hashtag, or user with advanced filtering
- **Engagement analytics**: Track impressions, likes, retweets, replies, and follower growth
- **Timeline monitoring**: Monitor home timeline, lists, and saved searches
- **User analysis**: Analyze follower demographics, engagement patterns, and content performance
- **Draft & schedule**: Queue posts for optimal timing with content calendar integration
- **Hosted endpoint**: Remote MCP server at opentweet.io

## Installation

```bash
# Add to Hermes (remote endpoint)
hermes mcp add opentweet --url https://opentweet.io/twitter-mcp-server

# Authenticate (OAuth — connects your X account)
hermes mcp auth opentweet
```

## Manual Configuration

```json
{
  "mcpServers": {
    "opentweet": {
      "type": "sse",
      "url": "https://opentweet.io/twitter-mcp-server",
      "headers": {
        "Authorization": "Bearer ${OPENTWEET_API_KEY}"
      }
    }
  }
}
```

## Prerequisites

1. **OpenTweet Account**: Sign up at [opentweet.io](https://opentweet.io)
2. **X/Twitter Account**: Connect your X account via OAuth
3. **X API Access** (optional): For advanced analytics and higher rate limits

## Business Use Cases

1. **Content Scheduling**: "Draft a 5-tweet thread about our Q2 results, schedule it for Tuesday at 9 AM ET"
2. **Engagement Monitoring**: AI agent tracks replies to your tweets and drafts responses for review
3. **Competitive Analysis**: "Analyze the last 50 tweets from our top 3 competitors — what topics are they posting about?"
4. **Trend Surfing**: Agent monitors trending topics in your niche and suggests timely content angles
5. **Audience Insights**: "Show me which of my tweets got the most engagement this month and identify common themes"
6. **Hashtag Strategy**: Agent analyzes hashtag performance and recommends optimal hashtag combinations

## Business Relevance

X/Twitter remains the primary platform for tech operators, founders, and B2B marketers. Managing it effectively requires constant attention — drafting, scheduling, monitoring, engaging. OpenTweet MCP offloads the mechanical work to AI agents, letting operators focus on strategy and high-value replies. For agencies managing multiple client accounts, the agent can monitor and draft across accounts simultaneously.

## Limitations

- X API rate limits apply (varies by X API tier — Basic/Pro/Enterprise)
- DMs require elevated X API access (Pro tier minimum)
- Automated posting may trigger X's spam detection — human review recommended for high-volume accounts
- Analytics data limited to what X API exposes (no third-party data enrichment)
- X API access costs scale with usage — factor into budget for high-volume agents

## See Also

- CorpusIQ MCP — for cross-platform business data and social media analytics
- SEOforGPT MCP — for AI visibility and content optimization
- LinkedIn FastMCP — for LinkedIn professional network management
