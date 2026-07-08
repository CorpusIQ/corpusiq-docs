# How to Query Business Data in Natural Language

You know SQL? Most operators don't. They know their business. They know the questions. But the gap between "how are we doing this quarter?" and `SELECT SUM(amount) FROM charges WHERE created > '2026-01-01'` is a data analyst who costs $120K/year.

Here's how to close that gap.

## The natural language revolution

LLMs can translate plain English into structured queries. "Show me revenue by month" becomes `SELECT date_trunc('month', created), SUM(amount)...` automatically. You never see the SQL. You just get the answer.

This isn't theoretical. It's how every MCP query works:

1. You ask: "Which products sold best last month?"
2. The AI translates it into a Shopify API call
3. The data comes back live
4. The AI formats it as an answer

You never write a query. You never see an API. You just ask and get answers.

## What you can ask

| Instead of | Ask |
|-----------|-----|
| "Export QuickBooks P&L, pivot by month, filter by department" | "What's our P&L by department this quarter?" |
| "Export Shopify orders, filter by date, VLOOKUP customer email" | "Which customers haven't ordered in 60 days?" |
| "Pull HubSpot deals, filter by close date, calculate total" | "What's our pipeline value closing this month?" |
| "Pull Stripe charges, calculate MRR, compare to last month" | "What's our MRR trend over the last 6 months?" |
| "Export Meta Ads + Google Ads, combine, calculate blended ROAS" | "What's our blended ROAS this week?" |

## The tools that make it work

Natural language querying requires two things: a model that understands your question, and connectors that can answer it. MCP provides both:

```json
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp",
      "transport": "streamable-http"
    }
  }
}
```

Connect QuickBooks. Connect Stripe. Connect Shopify. Connect HubSpot. Now you can ask anything in plain English and get answers from live data.

## The shift

When you stop needing a data analyst to answer basic questions, two things happen:

1. You ask more questions. When each answer takes 15 seconds instead of 45 minutes, curiosity becomes cheap.

2. Your questions get better. You stop asking "what happened?" and start asking "why did this happen, and what should I do about it?"

That second shift is where the money is.

---

*CorpusIQ: Natural language queries across 37+ business tools. Read-only. 5-minute setup. [corpusiq.io](https://www.corpusiq.io)*
