---
title: Use CorpusIQ with Claude Code — Ask Business Questions from Your Terminal
description: Connect CorpusIQ to Claude Code via MCP. Ask revenue, orders, and margin questions against live Shopify, Stripe, and QuickBooks data. Source-cited answers in your terminal.
canonical: "https://www.corpusiq.io/docs/hermes/guides/corpusiq-claude-code/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Use CorpusIQ with Claude Code

Claude Code is Anthropic's agentic coding tool that runs in your terminal. You can use it to write code, manage repos, and run commands.

With the CorpusIQ MCP server, Claude Code can also answer business questions — from your actual data.

## Setup (2 minutes)

Add this to your Claude Code MCP config:

```json
{
  "mcpServers": {
    "corpusiq": {
      "type": "url",
      "url": "https://mcp2.corpusiq.io/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_CORPUSIQ_JWT"
      }
    }
  }
}
```

Get your JWT from the CorpusIQ dashboard at [corpusiq.io/dashboard](https://corpusiq.io).

## Connect Your Tools

Before Claude Code can answer business questions, connect your tools once:

1. Go to [corpusiq.io/dashboard](https://corpusiq.io)
2. Connect Shopify, Stripe, QuickBooks, GA4, Meta Ads — or any of the 40+ supported tools
3. Each connection uses read-only external-source retrieval with no write access; direct MCP does not retain raw customer files or full connector response payloads

## Ask Business Questions

Once connected, ask Claude Code questions in plain English:

```
> What was our revenue last month?

Claude Code calls CorpusIQ MCP → pulls from Stripe → cross-checks with Shopify → returns:

  June 2026 revenue: $247,382
  - Stripe: $238,150 (from 842 transactions)
  - Shopify (manual orders): $9,232 (from 34 orders)
  - Source: Stripe balance transaction list + Shopify order export
  - Discrepancy: $0 (reconciled)
```

```
> Which ad campaign drove the most sales last week?

Claude Code calls CorpusIQ → pulls from Meta Ads + GA4 → returns:

  Campaign "Summer Launch — AZ" drove $14,230 in attributed revenue
  - Ad spend: $3,120
  - ROAS: 4.56x
  - 142 attributed orders
  - Source: Meta Ads campaign report (Jul 21-27) + GA4 attribution
```

```
> What is our current margin by product line?
```

Claude Code calls CorpusIQ → pulls from QuickBooks + Shopify → returns margin breakdown.

## What Makes This Different

You could ask ChatGPT the same questions. But without CorpusIQ, ChatGPT guesses. It does not have access to your actual Stripe account, your actual Shopify orders, or your actual QuickBooks ledger.

With CorpusIQ as the MCP server, every AI you use — Claude Code, ChatGPT, Perplexity, Slack — inherits the same connections. Same data. Same answers. Every time.

## Supported Tools

Shopify. Stripe. QuickBooks. Google Analytics 4. Meta Ads. HubSpot. Klaviyo. Gmail. Google Drive. Dropbox. YouTube. Google Ads. eBay. Microsoft OneDrive. Outlook. And 25 more.

External-source retrieval tools are marked read-only; write-capable management/control-plane tools are separate. Direct MCP does not retain raw customer files or full connector response payloads; scoped operational logs may be retained for up to 30 days. Every answer cites its exact source.

## Get Started

[Connect your tools in 5 minutes](https://corpusiq.io)
