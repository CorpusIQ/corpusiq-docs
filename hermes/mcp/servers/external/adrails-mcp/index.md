---
title: "Adrails MCP - Ad Spend Reconciled to Real Revenue"
description: "Meta and Google Ads for a Shopify store, read next to Stripe, Klaviyo and PostHog revenue, with every change filed for human approval first."
category: Marketing
stars: n/a (new listing)
added: 2026-10-22
source: "mcp.so /feed + chatmcp/mcpso issues (October 22, 2026 evening sweep)"
relevance: ★★★
tags: [ads, meta-ads, google-ads, shopify, ecommerce, revenue, attribution, oauth, remote-mcp, approval-control]
---

# Adrails MCP

**Ad management for Meta Ads and Google Ads where the ad numbers sit next to the store's own revenue.** Agents read campaigns and the business data connected to the same workspace, explain performance against it, and prepare changes that a person approves in the browser before anything reaches Meta or Google.

```
Server type: Remote (Streamable HTTP at https://adrails.ai/api/mcp)
Auth: OAuth 2.1 (PKCE, dynamic client registration), six scopes
Protocol: 2025-11-25 per the vendor server card at /.well-known/mcp/server-card.json
Tools: 69 published - 49 agent tools plus 20 for accounts, integrations, campaign drafts, automations, Knowledge and job status
Business sources read beside ad spend: Shopify, Stripe, Klaviyo, Triple Whale, PostHog, RevenueCat, Google Drive
Change control: proposals only, 30% budget cap per change, campaigns created paused, approvals re-read the platform first
Pricing: Preview free (10 credits, once), Starter $49/mo, Growth $149/mo, Scale $399/mo
Built by: TBSS Labs, LLC (adrails.ai), not affiliated with Meta Platforms or Google
```

## Why This Matters for Operators

Ad platforms report on themselves. The number a dashboard calls revenue is the platform's own attribution of it, and the store's revenue lives somewhere else, in another currency of meaning: net of refunds, net of failed payments, net of the subscriptions that never renewed.

Adrails puts those two ledgers in one workspace and lets the agent read them together. **`store_revenue` returns gross, refunded and net sales kept apart, in each store's own currency, never converted**, and `business_review` accepts an explanation only when every number quotes its source word for word, from the person's own statement or from a tool result in that connection's history. That is a provenance rule enforced inside the tool, not a disclaimer in documentation.

The second half is change control, and it is the reason this entry exists rather than being another ads console. Every advertising change is a proposal with an expiry and an approval link. Nothing is applied by the agent.

## Tools & Capabilities

The vendor publishes all 69 tools with inputs, per-operation permission, role requirement and error contract at `adrails.ai/docs/mcp/tools`. `tools/list` returns only the tools the connection's permissions and your role allow, so the surface you see is the surface you can use.

| Area | Representative tools | Access |
|---|---|---|
| Reporting | `reporting_overview`, `performance_period`, `performance_diagnose`, `metrics_daily`, `metric_compare`, `portfolio_review` | read |
| Money and pacing | `budget_recommend` (latest two complete seven-day windows in the account timezone, and it suggests no amount), `planning_calculate`, `business_review`, `changes_review`, `findings_review` | read |
| Store and billing data | `store_revenue`, `store_orders`, `store_customers`, `store_products`, `saas_performance` | read |
| Creative | `creative_insights`, `creative_market_evidence`, `creative_review`, `drive_folder`, `site_brief`, `launch_brief` | read |
| Build and target | `campaigns_setup`, `campaigns_structure`, `google_ads_library`, `google_keyword_planner`, `targeting_options`, `audience_estimate`, `campaigns_create_draft`, `campaigns_launch` | proposal |
| Change | `campaigns_pause`, `campaigns_set_status`, `campaigns_change_budget`, `campaigns_split_test`, `actions_recent`, `actions_undo` | proposal |

Three access shapes are declared per tool: **read** changes nothing, **change** acts at once inside Adrails' own rules and needs an `idempotencyKey`, and **proposal for approval** prepares one exact advertising change and returns a link. Rule-engine findings arrive with their evidence, snapshot date, campaign objective, currency, budget owner and a classification across creative, targeting, tracking, fatigue and health.

## Installation

```bash
claude mcp add --transport http adrails https://adrails.ai/api/mcp
```

Any OAuth-capable MCP client works: the sign-in creates a connection scoped to the permissions you grant, and each call is checked again against your current role in the workspace rather than the role you held when you connected.

## Configuration and Safety

- **An approval is not a tool call.** A proposal comes back with `status: awaiting_approval`, an `actionId`, a field-by-field `preview`, an `expiresAt` and `approvalUrl` at `adrails.ai/oauth/actions/<actionId>`. Any current owner or admin of the workspace can open it, signed in as themselves. On approval Adrails reads the platform again and applies the exact change once, or blocks it if the entity changed in the meantime.
- **Proposals expire.** 24 hours for one prepared over MCP, 30 minutes for in-app chat. An expired proposal is not retried silently.
- **Budget moves are capped at 30% per change**, an increase needs measured spend and results, and a bulk change applies to at most 40 entities on one account with a result per entity.
- **What Adrails creates starts paused**, including campaigns built from a complete launch brief after approval.
- **Idempotency is enforced**, not advisory: the same key with the same arguments returns the first result, the same key with different arguments is refused, and a call cut off mid-flight keeps its key blocked until `jobs_status` is checked.
- **Errors arrive as tool results** with `isError: true` and a sentence, so the model can correct the call instead of failing the conversation.
- **Limits:** 60 calls a minute per token, 10 changes and proposals a minute per token, 180 a minute per person and 600 per workspace; a result over 256,000 bytes is refused whole with no partial figures, and a request is capped at 1 MB.
- **Credits:** MCP tool calls cost 0 credits on every plan. Your client's own inference cost is separate.

## Business Relevance

- **Ecommerce operators** see ad spend beside net store revenue for the same dates instead of two dashboards that disagree on the definition of a sale.
- **Marketing leads** get findings with evidence and a snapshot date, then a prepared change with a named approver, a cap and an expiry.
- **Owners and admins** keep a hard stop on spend: the agent prepares, a person approves in the browser, and the platform is re-read before the write.
- **Agencies and fractional CMOs** work across many ad accounts with unlimited accounts and team members on every paid plan, and no percentage of ad spend.

## Integration with CorpusIQ

CorpusIQ answers the cross-source question with citations from the connectors you already own - Stripe, Shopify, QuickBooks, Klaviyo, Google Ads - and Adrails is the ad-side workspace that can act on the answer. Use CorpusIQ to establish the number that is true across systems (revenue, refunds, acquisition cost, pacing), then hand the campaign work to Adrails, where the write still needs a person's approval. Two different jobs: one produces a figure you can defend, the other changes spend without letting the model touch the account.

## Limitations

- **No tool call was made in this sweep.** Every tool needs an OAuth connection to an Adrails workspace with at least one connected ad account, and that account is not something this catalog creates. The entry rests on the live 401, the protected-resource metadata, the vendor server card and the published 69-tool reference, and the absent execution is named here rather than implied.
- Ad platforms are Meta Ads and Google Ads only; TikTok, LinkedIn and Microsoft are not offered.
- Meta campaign creation from a draft is narrower than the platform: one website ad set and one image ad per draft, standard Sales, Leads or Traffic objectives, an image already uploaded to the account.
- The analysis language set is `fr` and `en`.
- Candidate response shapes are English or French prose plus `structuredContent.result`; there is no artifact or chart renderer over MCP.
- Built and operated by a single vendor (TBSS Labs, LLC, Dubai), so continuity is a supplier risk worth naming for teams that would run spend through it.

## FAQ

### Does an agent ever change ad spend on its own?

No. Pausing, status changes, budget changes, drafts and launches are all proposals. They return an approval link and expire, and nothing reaches Meta or Google Ads before an owner or admin approves in the browser.

### How much can one budget change move?

At most 30% in a single change, and an increase requires measured spend and results behind it. Bulk selection is capped at 40 entities on one account, each with its own result.

### Does it reconcile ad spend with revenue from other systems?

The workspace connects Shopify, Stripe, Klaviyo, Triple Whale, PostHog, RevenueCat and Google Drive. `store_revenue` reports gross, refunded and net sales separately in each store's currency without conversion, and `business_review` only accepts figures that quote their source verbatim.

### What does it cost?

Preview is free with 10 credits once. Starter is $49 a month with 200 credits, Growth $149 with 700 and Scale $399 with 2,000. Unlimited ad accounts and team members on every paid plan, every connector included, no percentage of ad spend, and MCP tool calls cost no credits.

### Can I try it without connecting a live ad account?

Not usefully. The tools act on a connected workspace, so the trial path is the Preview plan with a real ad account; there is no read-only demo endpoint published.
