---
title: "Feedier — Customer Insights MCP for AI Agents"
description: "Connect AI agents to customer feedback and survey data through Feedier's MCP server. Get clear, reliable, and actionable customer insights with AI."
source: help.feedier.com
stars: 0
language: N/A (Hosted SaaS)
transport: Streamable HTTP
auth: OAuth
category: Business Operations
last_updated: 2026-07-21
---

# Feedier — Customer Insights MCP for AI Agents

**Customer feedback and survey platform with MCP integration.** Feedier lets AI agents access customer insights — surveys, NPS scores, feedback analytics — through a single MCP endpoint. Operators can ask their AI agent about customer sentiment without leaving their workflow.

## What It Does for Operators

- **Customer feedback access** — Query survey responses, NPS scores, and customer sentiment through MCP tools
- **AI-powered insights** — Feedier's AI analyzes feedback and surfaces trends your agent can query
- **Real-time data** — Streamable HTTP endpoint provides fresh feedback data on every query
- **Actionable intelligence** — Not just raw data — categorized, scored, and trended feedback

## Installation

```bash
# No installation — hosted endpoint
# Connect your Feedier account via OAuth
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "feedier": {
      "type": "url",
      "url": "https://help.feedier.com/en/articles/14999846-feedier-mcp"
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `get_survey_responses` | Retrieve customer survey responses with filters |
| `get_nps_score` | Current NPS score with trend data |
| `analyze_sentiment` | AI-powered sentiment analysis of feedback |
| `list_feedback_categories` | Categorized feedback by topic/theme |
| `get_customer_journey_feedback` | Feedback tied to specific journey touchpoints |

*Note: Tool names are approximate. Full documentation at help.feedier.com.*

## Operator Use Cases

1. **Customer Success Teams** — Ask AI agents "What are our top 3 customer complaints this week?" and get data-backed answers
2. **Product Managers** — Query feature-specific feedback to prioritize roadmap items
3. **Marketing Teams** — Surface testimonials and positive feedback for campaigns
4. **Executive Dashboards** — Agent-driven reporting on customer health metrics

## CorpusIQ Angle

Feedier fills the customer feedback gap in CorpusIQ's data ecosystem. While CorpusIQ connects financial and operational data (QuickBooks, Stripe, Shopify), Feedier adds the customer voice. Operators can cross-reference revenue data with customer satisfaction — identifying which revenue segments have the happiest (or angriest) customers.

## Limitations

- Requires active Feedier subscription
- MCP integration is new (July 2026) — API may evolve
- Full tool documentation not yet available publicly
- Limited to Feedier survey/feedback data (not a general survey tool)
