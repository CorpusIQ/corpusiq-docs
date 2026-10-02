---
title: "SellerMate MCP - Amazon Ads Operations for AI Agents"
description: Live Amazon Advertising data and governed campaign actions for AI agents - wasted spend, ACOS, search term performance and true TACoS, with policy guardrails and admin approvals on every write
category: Marketing
stars: n/a (new listing)
added: 2026-09-03
source: "mcp.so GitHub issue #3913"
relevance: ★★★
tags: [amazon-ads, ecommerce, advertising, oauth, campaign-management, remote-mcp, pkey]
---

# SellerMate MCP

**Remote MCP server (SSE + Streamable HTTP, one URL) for live Amazon Advertising - plain-English answers on wasted spend, ACOS and TACoS, plus policy-checked campaign actions with admin approvals and a full audit trail.** Connect any MCP client to your Amazon Ads account through SellerMate, which holds the Amazon connection so you never touch Amazon Ads API credentials. Read-only by default; every write passes workspace guardrails (budget and bid floors, change-multiplier caps, per-currency limits) and can require a human admin approval. Used by 2,000+ brands and agencies in 20+ countries; 2026 Amazon Ads Partner Awards Technology Innovation finalist.

```
Server type: Remote (SSE + Streamable HTTP, same URL)
Auth: OAuth 2.1 + PKCE (browser sign-in, no API keys)
Endpoint: https://api.sellermate.ai/mcp/sse
Tools: 50+ (reporting, campaigns, targeting, negatives, automations, dayparting, DSP)
Pricing: Free on every plan
Category: Advertising / Amazon Ads
Built by: SellerMate.AI
```

## Why This Matters for Operators

Amazon Ads is where ecommerce operators either compound or bleed margin, and the numbers live in a console nobody enjoys opening. SellerMate's MCP puts the same live data inside the agent that is already writing your recap: ask "which search terms burned budget with zero orders in the last 30 days" and get the actual Search Query Performance rows. The write path is the differentiator: negate wasted terms, shift budgets to winners, and launch campaigns from chat, with every action policy-checked before it runs. The guardrails are server-enforced, not prompts - an agent cannot exceed the budget, bid or change-multiplier limits your workspace sets, and admin approval gates the sensitive moves.

**The grant is the security model.** OAuth 2.1 with PKCE means no API key to paste or rotate, account-level access control, and no Amazon Ads API credentials anywhere in the loop. Reads are read-only by default and the server caches nothing.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `get_search_term_performance` | Search terms with spend, clicks and orders - find budget burners |
| `add_negative_keywords` | Negate wasting terms (queued for approval) |
| `update_campaign` | Adjust budgets, bids and placements - policy-checked |
| `create_campaign` | Launch a campaign for a product |
| `get_sqp_report` | Search Query Performance trends |
| `create_dayparting` | Time-of-day budget rules to stop overnight overspend |

The full surface is 50+ tools across reporting, campaign management, targeting, negatives, automations, dayparting and DSP.

## Installation

```bash
claude mcp add --transport sse sellermate https://api.sellermate.ai/mcp/sse
```

The client opens a browser window for the SellerMate sign-in on first use. Desktop, Code, Cursor, VS Code, Windsurf and Gemini CLI all take the same URL. ChatGPT connects it as a custom connector. Claude users can also one-click add it from Claude's connector directory.

## Configuration

No keys. Sign in with a free SellerMate account connected to your Amazon account, approve the scopes, and set your workspace guardrails: budget and bid floors and ceilings, change-multiplier caps, per-currency limits, and which actions require admin approval. Every write is logged with the approving identity for the audit trail.

## Business Relevance

Amazon marketplace operators get the fastest path from "ACOS jumped last week" to a governed fix, without exporting reports or trusting an agent with unchecked write access. Agencies get per-brand workspaces and an audit trail their clients can inspect. True TACoS math (retail plus ads performance in one view) is the number operators actually need to judge ad efficiency.

## Integration with CorpusIQ

CorpusIQ's 40+ connectors give agents financial, commerce and marketing reads across QuickBooks, Shopify, Stripe, Google Ads and more. SellerMate adds the Amazon Ads depth: when a recap in CorpusIQ asks why margin moved, a SellerMate-connected agent can answer from live Amazon advertising data and stage governed fixes, complementing CorpusIQ's read-only visibility with policy-gated Amazon ad execution.

## Limitations

- Amazon Ads only - no Seller Central inventory or order tools (see the two-in-one Amazon Seller Central / Amazon Ads entry in the catalog)
- Admin approvals and guardrails are configured in the SellerMate workspace, not per-agent
- OAuth sign-in requires a browser on first connect

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [AdWhispr MCP - Meta Ads Research for Agents](/hermes/mcp/servers/external/adwhispr-mcp)
- [Apple Ads MCP - App Store Campaign Operations from Your Terminal](/hermes/mcp/servers/external/apple-ads-mcp)
- [Mercopilot MCP - Shopify & Google Ads Operating Bridge](/hermes/mcp/servers/external/mercopilot-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
