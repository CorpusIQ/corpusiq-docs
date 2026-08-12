---
title: Cello MCP
description: Build and scale referral, partner, and affiliate programs from any MCP-compatible AI agent — live metrics, top referrer identification, churn alerts, and actionable recommendations
category: Marketing / Growth
stars: featured
added: 2026-08-11
source: mcp.so
relevance: ★★★
tags: [referrals, affiliates, partners, growth, saas, marketing, analytics]
---

# Cello MCP

**Remote MCP server (Streamable HTTP, OAuth) for Cello.** Connect AI agents to your referral, partner, and affiliate program data — ask which referrers drive the most revenue, identify partners at risk of churning, get recommendations to improve conversion, and pull program metrics against benchmarks.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in)
Endpoint: https://mcp.cello.so/mcp
Pricing: Free with Cello account
Category: Marketing / Growth / Referral Management
```

## Why This Matters for Operators

Referral programs drive 30% higher LTV than non-referred customers (SaaS Capital, 2026). But most operators check referral dashboards monthly at best — missing the window to re-engage partners before they churn. Cello MCP puts this data in your AI agent's context so you can:

1. **Ask "who should I reach out to today?"** — and get the top referrers ranked by revenue, not just volume
2. **Catch churn before it happens** — identify partners whose referral activity dropped 50%+ in the last 30 days
3. **Compare against benchmarks** — know if your 4.2% referral conversion rate is competitive
4. **Validate integration health** — confirm attribution is working correctly without opening a dashboard

For operators running any partner/referral/affiliate program, this is the first MCP server that puts program intelligence directly into your agent's tool set.

## Tools & Capabilities

| Capability | Description |
|---|---|
| **Live Program Metrics** | Revenue, conversion rates, active referrers, payout totals |
| **Top Referrer Identification** | Ranked by revenue, volume, conversion rate |
| **Churn Risk Detection** | Flag partners with declining activity patterns |
| **Benchmark Comparison** | Compare your program metrics against industry benchmarks |
| **Attribution Health** | Validate integration status, webhook delivery, and event tracking |
| **Actionable Recommendations** | Get specific suggestions to improve program conversion |
| **On-Demand Documentation** | Fetch setup guides and API docs in context |

## Configuration

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "cello": {
      "type": "streamableHttp",
      "url": "https://mcp.cello.so/mcp"
    }
  }
}
```

Or via Claude Code:
```
claude mcp add cello-mcp --transport http https://mcp.cello.so/mcp
```

First connection opens a browser for OAuth sign-in. Credentials are reused for subsequent sessions.

## Use Cases for Business Operators

- **Daily partner pulse:** "Which of my top 10 referrers haven't sent a referral in 2+ weeks?"
- **Program optimization:** "What's my referral-to-trial conversion rate and is it above SaaS benchmark?"
- **Attribution debugging:** "Is the webhook for Stripe payouts firing correctly for my last 5 referrals?"
- **Growth planning:** "What's the ROI on my referral program this quarter vs. paid acquisition?"
- **Partner outreach:** "Draft a re-engagement email for my top 3 dormant referrers"

## Verdict

★★★ **Catalogue immediately.** First MCP server dedicated to referral/affiliate program intelligence. The "ask in plain language" approach eliminates the dashboard-checking friction that causes most operators to under-manage their referral programs. For any business running a partner or affiliate program, this replaces the monthly dashboard login with an always-available AI agent that can proactively flag issues and opportunities.

## Additional Resources

- [Cello MCP Documentation](https://docs.cello.so/mcp/introduction)
- [Cello Homepage](https://cello.so/)
- MCP.so listing: `https://mcp.so/servers/cello-mcp`
