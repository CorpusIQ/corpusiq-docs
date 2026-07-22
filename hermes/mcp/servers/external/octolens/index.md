---
title: "Octolens MCP — Integration Guide"
description: "Connect AI agents to Octolens for brand monitoring across 15+ platforms. AI-filtered mentions, sentiment scoring, and social listening directly in your AI workflows."
category: mcp
tags: [mcp-server, social-listening, brand-monitoring, marketing, analytics]
last_updated: 2026-07-18
---

# Octolens MCP — Integration Guide

**Source:** mcp.so listing (remote MCP server)  
**Author:** Octolens  
**Endpoint:** `https://app.octolens.com/api/mcp/v2`  
**Transport:** Streamable HTTP  
**Auth:** OAuth  
**Docs:** [octolens.com/docs/mcp/v2/overview](https://octolens.com/docs/mcp/v2/overview)  
**Website:** [octolens.com/mcp](https://octolens.com/mcp)

## What It Does

Octolens is one API for every brand mention across the internet — and this MCP server puts it directly into your AI agent's hands.

Coverage spans **15+ platforms:** Reddit, X (Twitter), LinkedIn, Hacker News, YouTube, Bluesky, GitHub, Stack Overflow, dev communities, podcasts, newsletters, news, Product Hunt, Medium, and TikTok.

Every mention is AI-filtered for relevance and scored for sentiment before it reaches your agent. Companies like Vercel, PostHog, and Prisma use Octolens to catch conversations across the web.

The MCP server enables:
- **Support agents** that know what users complain about in real time
- **Research agents** with real voice-of-customer data for product decisions
- **Marketing agents** that pull social proof on demand without manual searching
- **SQL queries** over your entire mention history — no dashboard, no CSV export

## Setup

### Prerequisites

- An Octolens account at [octolens.com](https://octolens.com)
- One or more brand monitoring topics configured in your Octolens dashboard

### MCP Client Configuration

Add this to your MCP client's server configuration:

```json
{
  "mcpServers": {
    "remote-server": {
      "type": "http",
      "url": "https://app.octolens.com/api/mcp/v2"
    }
  }
}
```

For Claude Code:
```bash
claude mcp add octolens https://app.octolens.com/api/mcp/v2
```

### OAuth Flow

On first connection, your MCP client opens a browser window for OAuth authorization. Once authorized, credentials are reused for future sessions. No API key management required.

## Use Cases for Business Operators

- **Brand monitoring:** "What did people say about us on Hacker News this week?"
- **Competitive intelligence:** "Summarize competitor mentions on Reddit from the last 30 days"
- **Customer support triage:** "Are there any unresolved complaints about our API on Stack Overflow?"
- **Content sourcing:** "Pull the top 5 positive testimonials from LinkedIn for our case studies page"
- **Trend detection:** "What topics are trending in our community across platforms?"
- **SQL-powered analytics:** Run complex queries over months of mention data — filter by platform, sentiment, date range, keyword

## Operator Relevance ★★★

Octolens MCP is directly relevant to CorpusIQ's target audience of business operators and marketers. Brand monitoring is a core operational need, and Octolens is the first MCP-native solution that makes social listening conversational rather than dashboard-driven. Instead of logging into yet another SaaS tool, operators can ask their AI assistant directly and get structured, filtered results.

For marketing operators: social proof, competitor tracking, content sourcing.  
For product operators: voice-of-customer, feature request tracking, community health.  
For support operators: issue detection, sentiment trends, platform-specific monitoring.

## See Also

- External MCP Server Catalog(/hermes/mcp/servers/external/)
- Competitor Tracker MCP(/hermes/mcp/servers/external/competitor-tracker-mcp/) — competitor website change monitoring
- AI Visibility Analytics MCP(/hermes/mcp/servers/external/ai-visibility-analytics/) — brand presence tracking across AI providers
