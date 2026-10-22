---
title: "Privatrak MCP - Product Analytics With Undo"
description: "Privatrak answers traffic and funnel questions with the counts behind them, and can build features, funnels and dashboards from chat."
category: Analytics
stars: n/a (no public repo)
added: 2026-10-21
source: "mcp.so /feed page 1 (card posted 2026-10-21T06:51:31Z)"
relevance: ★★
tags: [web-analytics, product-analytics, funnels, dashboards, cookieless, click-tracking, remote-mcp, oauth]
---

# Privatrak MCP

**Most analytics connectors read. This one writes, and every change it makes lands in a run the operator can undo in one step, which is what makes it safe to let an agent configure tracking.**

```
Server type: Remote (Streamable HTTP) at https://api.privatrak.com/mcp
Auth: OAuth (choose the projects the connection can see, and whether it may read or also write); API keys for headless agents
Live check: POST initialize returned HTTP 401 {"error":"missing API key ...","error_code":"auth_invalid_token"} (unauthenticated probe, this sweep)
Tools: 44 (overview, pages, sources, campaigns, features, insights, funnels and trends, journeys, clicked elements, click problems, setup runs, docs search)
Pricing: Free $0 (10,000 events a month), Starter $19/mo, Pro $79/mo, Enterprise custom
Vendor: Privatrak (privatrak.com)
```

## Why This Matters for Operators

The usual failure of analytics is not missing data, it is a number with no basis. A dashboard says conversion fell 12 percent and the operator has to trust it, because the count behind the percentage is two clicks away and the comparison period may be incomplete. An agent answering the same question is worse: a language model will produce a confident sentence from no data at all if nothing forces it to compute.

Privatrak's answer is that answers carry the counts behind every percentage, and a period that would compare against incomplete data is flagged rather than guessed. That one design choice is what makes it safe to put in front of an operator who is going to act on the answer.

The second half is the write surface. The gap between "the funnel shows a drop" and "the funnel is now instrumented so we can see the drop" is normally a developer ticket. Privatrak lets the assistant create feature rules that name what people click without touching code, build and check funnels before saving them, create dashboards and charts, and mark click problems fixed or ignored.

## What It Actually Does

The 44 tools group into read and write. On the read side: overview metrics, pages, sources, campaigns, insights queries, funnels and trends, user journeys, clicked elements, click problems, and a search over Privatrak's own documentation.

On the write side: feature rules, funnels built and validated before saving, dashboards and their charts, and click problem status. Every write is recorded in a run, and a run can be undone in one step from the assistant or from Settings, AI assistant changes. If a person edited something after the assistant did, the undo leaves that change alone and reverts the rest, which is the detail that makes undo safe to use rather than a rollback that destroys human work.

The connection model is per-project and per-capability: the operator picks which projects the connection may see and whether it may only read or also make changes. That is the right shape for an agent, because the risky capability is opt-in at connect time rather than granted by default.

The product itself is cookieless with no personal data and no consent banner, which removes the compliance question that normally blocks analytics instrumentation in the EU.

## Installation

```bash
claude mcp add privatrak --transport http https://api.privatrak.com/mcp
```

Sign in through OAuth and choose read-only or read-and-write at consent time. Setups for Claude, Cursor and Codex are published at privatrak.com/docs/ai-assistant.

## Configuration

```json
{
  "mcpServers": {
    "privatrak": {
      "type": "http",
      "url": "https://api.privatrak.com/mcp"
    }
  }
}
```

For headless agents, send an API key instead of the OAuth flow.

## Business Relevance

- **Growth and marketing leads** ask where traffic came from, which campaign worked, and where people drop between product page and checkout, and get counts rather than vibes.
- **Product managers** instrument a funnel from the conversation instead of filing a ticket.
- **Founders without a data team** get funnel and dashboard setup through the assistant, on a free plan up to 10,000 events a month.
- **Compliance-conscious operators** keep analytics without a cookie banner, because the product is cookieless and stores no personal data.
- **Agencies** create read-only connections per client project, which is the scoping a multi-client agency needs.

## Integration with CorpusIQ

This is the product-analytics half that a Google Analytics connector cannot reach. GA4 reports sessions, events and conversions on the site; Privatrak reports what people clicked and where the funnel actually broke, with the click context attached. Ask CorpusIQ to reconcile the two: GA4 for acquisition, Privatrak for the in-product drop, and the disagreement between them is usually the tracking gap worth fixing.

Pair it with the Shopify or Stripe connector for revenue and the Search Console connector for intent, and the funnel question becomes end to end: which query, which landing page, which step, which amount. Because Privatrak can write, the composed workflow can also close the loop, instrumenting the step the numbers say is missing rather than waiting for a sprint.

## Limitations

- New listing with no independent track record.
- The class has carry-over: Cookie Free Analytics covers the read-only cookieless view, Clamp Analytics covers traffic, funnels and cohorts, and the GA4 server covers Google's own numbers. What Privatrak adds is the write surface with undo, and it should be evaluated on that basis.
- Write access has to be granted at connection time; a read-only connection cannot instrument anything.
- Free plan is capped at 10,000 events a month, one project, one member and 30-day retention, so it evaluates rather than runs a business.
- Flows history is limited on paid tiers (last 90 days) and data retention tops out per plan.

## FAQ

### Can the agent break our tracking setup?

Every change lands in a run that can be undone in one step, and an undo leaves later human edits untouched. Combined with the read-or-write choice at connect time, the failure mode is a revertible run rather than a broken configuration.

### Why not just use the Google Analytics connector?

GA4 answers what happened on the site. It does not tell you which button people clicked, which funnel step silently broke, or what to change. Privatrak answers those and can make the change, so the two are complementary rather than alternatives.

### Does it need a cookie banner?

No. The product is cookieless and stores no personal data, so the consent banner requirement that normally applies to analytics does not arise.

### How much does it cost to evaluate?

The free plan is $0 with 10,000 events a month and no card. Starter is $19 a month for 100,000 events, Pro is $79 a month for a million.

## See Also

- [Cookie Free Analytics MCP - Cookieless GDPR-First Web](/hermes/mcp/servers/external/cookiefreeanalytics-mcp)
- [Jitsu MCP](/hermes/mcp/servers/external/jitsu)
- [Google Analytics MCP](/hermes/mcp/servers/external/google-analytics-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
