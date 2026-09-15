---
title: "Buska MCP - Social Listening and Buying Signals for AI Agents"
description: "Remote social-listening MCP server that searches public conversations across 30+ platforms, returns AI-scored buying signals and qualifies leads against an ideal customer profile. OAuth 2.1, three documented tools, a 7-day free trial and plans from $49/month."
category: Sales & Outreach
stars: "n/a (new listing, Buska-io/buska-mcp)"
added: 2026-09-03
source: "mcpservers.org /all listing (buska-io/buska-mcp)"
relevance: ★★★
tags: [social-listening, lead-generation, buying-signals, sales, outreach]
---

# Buska MCP - Social Listening and Buying Signals for AI Agents

**Remote hosted MCP server (Streamable HTTP, OAuth 2.1)** - social listening built for lead generation, not brand reports. It searches public conversations across 30+ platforms in near real time, detects people actively asking for a product or service, and scores every mention 0-100 for buying intent and ICP fit.

## Spec Block

| Field | Value |
|---|---|
| Server name | buska-mcp |
| Repo | github.com/Buska-io/buska-mcp (docs, config examples and 6 agent skills) |
| Endpoint | https://api.buska.io/mcp |
| Transport | Streamable HTTP |
| Auth | OAuth 2.1 (browser login, no API key to paste) |
| Tools | search_mentions, get_signals, score_lead |
| Platforms | 30+ (Reddit, X, LinkedIn, Hacker News, YouTube, Quora, Bluesky, GitHub, Stack Overflow, G2, Product Hunt, TikTok, Instagram and more) |
| Plans | 7-day free trial (no card), then from $49/month |
| Registry | io.buska/buska |
| License | MIT (repo documentation) |

## Why This Matters for Operators

Most social listening tools count mentions; Buska finds buyers. The vendor's published study across 451,903 public posts found only 1.4% carried strong buying intent, Reddit produced 77% of the hot posts, and LinkedIn had the highest buyer density. An agent connected to Buska skips the noise: it asks for signals that are already scored, qualifies them against your ICP, and hands you the few conversations worth a reply.

## Tools & Capabilities (3 tools)

| Tool | Purpose | Key parameters |
|---|---|---|
| search_mentions | Live keyword search on one platform; returns posts with content, author, URL and engagement metrics | keyword, platform (19 enum values), limit 1-50 |
| get_signals | The qualified buying signals already detected for your configured keywords, with the AI score and its reasoning | keyword, intent (ACTIVE, COMPETITOR, PAIN, QUESTION, MENTION), minScore 1-10, since, limit 1-100 |
| score_lead | Score any lead or post for buying intent and ICP fit on demand | lead or post reference |

Six ready-made agent skills ship alongside: find-leads-in-public-conversations, daily-reply-shortlist, competitor-switch-alerts, qualify-leads-against-your-icp, surface-buying-objections, and fill-your-crm-from-social.

## Installation

```bash
claude mcp add --transport http buska "https://api.buska.io/mcp"
```

Works with Claude Code, Claude Desktop, claude.ai, ChatGPT, Cursor, Windsurf and any MCP client. One-click installs on Smithery and Cursor Directory; ready-made config snippets live in the repo's examples/ folder.

## Configuration

Nothing to run locally - the server is hosted. Sign in with OAuth 2.1 when the client prompts. Skills install via `npx skills add Buska-io/buska-mcp`. A REST alternative exists with an OpenAPI spec at buska.io/openapi.json.

## Business Relevance

For any operator running outbound or content-led growth: daily shortlists of scored buying signals with a suggested opener per lead, alerts when people complain about a competitor or shop for an alternative, real buyer objections mined for landing-page copy, and a pipeline that dedupes, qualifies and routes signals into a CRM. Buska never posts or replies on your behalf - skills draft replies and openers for human review.

## Integration with CorpusIQ

Scored signals pair directly with CorpusIQ's connector data: route qualified leads into the CRM, enrich them with company financials from QuickBooks or Shopify connectors before outreach, and use the objection vocabulary Buska surfaces to sharpen CorpusIQ reports and dashboard copy.

## Limitations

Brand new (repo created Sep 2, 2026, 0 stars). Public posts only - no private groups or DMs. Expect high precision but low volume: per the vendor's own study, roughly 1.4% of public posts carry strong buying intent. Paid plans start at $49/month after the 7-day trial.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CampaignStack MCP - Safe LinkedIn and Email Outreach](/docs/hermes/mcp/servers/external/campaignstack-mcp)
- [Xverum MCP - People Search Across 750M Professional Profiles](/docs/hermes/mcp/servers/external/xverum-mcp)
- [Apollo.io MCP - Integration Guide](/docs/hermes/mcp/servers/external/apollo-io-mcp)
