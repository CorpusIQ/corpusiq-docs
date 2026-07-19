---
title: "SocialBu MCP — Social Media Management for AI Agents"
description: "Connect any MCP-compatible AI assistant (Claude, ChatGPT, Cursor, Hermes) to SocialBu for social media posting, analytics, and scheduling across all major platforms. Operator-first social management."
category: mcp
tags: [mcp-server, social-media, marketing, automation, content-scheduling]
last_updated: 2026-07-18
---

# SocialBu MCP Server ★ New (July 18)

## Overview

SocialBu MCP gives AI agents direct access to SocialBu's social media management platform. Instead of logging into a dashboard, operators can ask their AI assistant to create posts, review schedules, check analytics, and manage social accounts across platforms — all through natural conversation. Built by the SocialBu team, this MCP server bridges the gap between AI assistants and operational social media workflows.

**Key advantage: Operators can manage their entire social presence through conversation with their AI agent — no dashboard required.**

## Key Features

- **Multi-platform posting**: Create and schedule posts across all major social platforms from any MCP client
- **Analytics access**: Pull engagement metrics, follower growth, and post performance data directly into AI conversations
- **Schedule management**: Review and modify content calendars through natural language
- **Account management**: Monitor account health, connected profiles, and publishing status

## Installation

```bash
# Clone the repository
git clone https://github.com/usamaejaz/socialbu-mcp.git
cd socialbu-mcp

# Install dependencies
npm install

# Build
npm run build
```

## Configuration

```json
{
  "mcpServers": {
    "socialbu": {
      "command": "node",
      "args": ["path/to/socialbu-mcp/build/index.js"],
      "env": {
        "SOCIALBU_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Business Relevance

- **Marketing operators**: Query post analytics and schedule content without switching contexts — stay in your AI conversation and manage social in real-time
- **Agency teams**: Give each team member an AI assistant that can view published content and suggest scheduling gaps — reduces dashboard training time
- **Founders and solopreneurs**: Manage social presence without learning another tool — ask your AI "what posted today and how did it perform"
- **Content teams**: Preview scheduled content, catch gaps in the calendar, and adjust publishing cadence through conversation

## Integration with CorpusIQ

SocialBu MCP pairs naturally with CorpusIQ's content strategy tools and Postiz publishing pipeline. Ask your AI agent to review SocialBu analytics alongside CorpusIQ's 37+ business connectors — cross-reference social performance with Google Analytics traffic, Shopify sales data, or HubSpot lead conversions to build a complete picture of content ROI.

For teams already using CorpusIQ's Postiz integration for automated posting, SocialBu MCP adds a conversational management layer — schedule posts, check analytics, and adjust strategy without leaving your AI workflow.

## Limitations

- **Repository maturity**: 0 stars, 0 forks as of July 2026 — early-stage project. API reliability not yet proven at scale
- **API key required**: Requires a SocialBu account and API key — not self-hosted
- **Platform coverage**: Limited to platforms SocialBu supports (primarily mainstream social networks)
- **No self-hosted option**: The server depends on SocialBu's cloud API — no offline or air-gapped deployment

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [Competitor Tracker MCP](/hermes/mcp/servers/external/competitor-tracker-mcp/)
- [Octolens MCP](/hermes/mcp/servers/external/octolens/)
