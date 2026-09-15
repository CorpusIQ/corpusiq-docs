---
title: AMZ Vault MCP - Amazon Seller Central and Ads for Agents
description: Hosted MCP for Amazon Seller Central and Amazon Ads. 100+ read and staged-write tools cover P&L, settlement waterfalls, inventory health, brand analytics, keyword intelligence and PPC at every grain, with every change reviewed as a diff before anything reaches Amazon. OAuth 2.1, 14-day free trial.
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★★
tags: [amazon-seller, amazon-ads, ppc, profitability, inventory, brand-analytics, e-commerce, remote-mcp]
---

# AMZ Vault MCP - Amazon Seller Central and Ads for Agents

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - a hosted connector that puts a full Amazon seller's operating picture in front of an AI agent: true settlement-based profitability, PPC performance at every grain, inventory and forecasting, brand analytics, keyword intelligence and safe, approval-gated changes. Every write is staged as a reviewable diff and nothing reaches Amazon until the operator confirms. Built by AMZ Vault (amz-vault.com) on top of the official Selling Partner API and Amazon Ads API through the seller's own authorized connection.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with dynamic client registration (sign in with your AMZ Vault account)
Endpoint: https://www.amz-vault.com/mcp
Tools: 100+ (read plus staged write, grouped by domain)
Pricing: 14-day free trial, no card required, then paid plans
Category: Commerce & E-Commerce
Built by: AMZ Vault (amz-vault.com)
```

## Why This Matters for Operators

Amazon sellers juggle three separate reporting surfaces - Seller Central, the Ads console and their own spreadsheets - none of which agree on the same number. AMZ Vault collapses that into one account-level P&L: the settlement waterfall (revenue to refunds to COGS to fees to ad spend to net profit) computed from real settlement data rather than dashboard approximations, plus per-ASIN margin rows that roll up to TACoS and true contribution margin.

**The safety model is what makes it agent-usable: there is no autopilot. Every mutation - bids, budgets, campaigns, listings, negatives, COGS - goes through a staged write that renders a full diff first, and only `confirm_staged_changes` executes it.** The agent proposes, the human approves, and the approval inbox for automation rules is itself a first-class surface the agent can read. The tool catalog openly documents which tools read Amazon data and which merely stage proposals.

The read surface is unusually deep: raw row-level queries over the PPC data warehouse, search-term harvesting candidates, negation candidates, dayparting schedules, new-to-brand metrics, brand search query performance and a 12-month per-ASIN unit forecast with seasonality diagnostics.

## Tools & Capabilities

| Family | Tools | What they do |
|---|---|---|
| Account & discovery | `account_report`, `account_sellers`, `account_profiles`, `account_management_guide` | One-call account overview with period cards and settlement waterfall; list seller connections and ad profiles; the brand and PPC decision framework |
| Data warehouse | `data_describe`, `data_query`, `data_freshness` | Catalog and query every warehouse dataset with column projection and filters, plus per-dataset freshness caveats |
| P&L / profitability | `pnl_summary`, `pnl_breakdown`, `pnl_by_asin`, `pnl_settlement_audit`, `pnl_refunds`, `pnl_expenses`, `pnl_mcf_summary`, `pnl_sb_attribution`, `pnl_period_cards` | Settlement-basis account waterfall, per-ASIN margins and TACoS, fee audits, refund components, custom operating expenses, Multi-Channel Fulfillment totals |
| Products & inventory | `product_library`, `product_cogs`, `inventory_health`, `product_fee_preview` | Product catalog with breakeven ACoS targets, landed costs, FBA inventory with restock recommendations, Amazon fee previews |
| Brand analytics | `brand_sqp`, `brand_search_catalog`, `brand_top_search_terms`, `brand_market_basket`, `brand_repeat_purchase` | Search Query Performance funnels, marketplace top terms with click shares, bought-with pairs, repeat-purchase loyalty |
| Keyword intelligence | `keyword_finder` | Reverse-ASIN keyword lookup merged from first-party data |
| PPC - read | `ppc_product_report`, `ppc_campaigns`, `ppc_keywords`, `ppc_search_terms`, `ppc_ad_groups`, `ppc_query`, `ppc_describe` + 20 more | Full-fidelity row-level queries over every PPC dataset, campaign and ad-group performance, bid recommendations, harvesting and negation candidates, dayparting analytics |
| Automation | `automation_activity`, `automation_rules`, `automation_aoe_status`, `automation_dayparting`, `automation_minmax_results`, `automation_scheduled_tasks` | The approval inbox for rule automation, Adaptive Optimization Engine status, MinMax budget analysis results |
| A+ content | `aplus_document` | Fetch live A+ content documents including the full content module list |
| Staged writes | `stage_bid_changes`, `stage_budget_changes`, `stage_campaign_create`, `stage_campaign_update`, `stage_negatives`, `stage_listing_update`, `stage_cogs_update`, `stage_automation_rule` + 20 more | Propose every mutation as a diff; only `confirm_staged_changes` executes, `cancel_staged_changes` aborts, `staged_changes_pending` lists open proposals |

The full tool list is served live from the endpoint; the table above follows the vendor's published catalog.

## Installation

```bash
claude mcp add --transport http amz-vault https://www.amz-vault.com/mcp
```

Create an AMZ Vault account, connect your Amazon account (14-day free trial, no card), then add the URL in Claude or any MCP client. OAuth 2.1 with dynamic client registration means no API keys to create, copy or leak - the client opens the AMZ Vault consent screen and every call runs under that connection.

## Configuration

```json
{
  "mcpServers": {
    "amz-vault": {
      "type": "http",
      "url": "https://www.amz-vault.com/mcp"
    }
  }
}
```

Auth is browser OAuth on first connect. Writes are staged server-side: the agent submits a proposal, the operator reviews the diff in the client, and confirmation is explicit.

## Business Relevance

- **Amazon sellers** get one settlement-basis P&L instead of reconciling three dashboards, with per-ASIN breakeven ACoS and margin targets
- **PPC managers** read row-level ad data, pull harvesting and negation candidates, and stage bid or budget changes as diffs instead of editing the console blind
- **Agencies** bridge multiple seller connections and ad profiles under one token with per-account scoping
- **Operators running automation** get an approval inbox that keeps every rule change human-confirmed

## Integration with CorpusIQ

AMZ Vault complements CorpusIQ's read-only business connectors by adding the Amazon marketplace execution layer. CorpusIQ already serves Shopify, QuickBooks, Stripe and GA4; an operator adding AMZ Vault gets Amazon Seller Central and Ads on top, closing the gap between marketplace performance and the rest of the books. A composed workflow: pull revenue and COGS from CorpusIQ's QuickBooks connector, pull ad spend and sales from AMZ Vault's PPC read tools, reconcile the two in one agent session, then stage the bid changes that close the gap - with the human confirming before anything is sent to Amazon.

## Limitations

- Brand new listing (September 2026) - no long track record, no public source code (the repo is a registry listing only)
- Hosted only - data flows through amz-vault.com under the seller's own Amazon authorization
- Free trial is 14 days; ongoing pricing requires a paid AMZ Vault plan
- Read depth is exceptional but writes are deliberately staged-only, which adds a confirmation step to every change
- Amazon API throttling and data-freshness caveats apply to the underlying datasets

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
