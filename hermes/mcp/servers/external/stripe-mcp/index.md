---
title: Stripe MCP Server ★★★ Official
description: "Setup and usage guide for Stripe MCP Server ★★★ Official. Part of the Hermes resource directory."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/stripe-mcp/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# Stripe MCP Server ★★★ Official

**Source:** mcpservers.org · **Last updated:** July 26, 2026 (evening sweep)  
**GitHub:** [stripe/agent-toolkit](https://github.com/stripe/agent-toolkit) ⭐ 1,700+  
**Endpoint:** `https://mcp.stripe.com` (Streamable HTTP)  
**Auth:** OAuth 2.0 (Stripe account required)  
**Category:** Payments & Billing / Finance

---

## Overview

The **official Stripe MCP server** gives AI agents direct, authenticated access to Stripe's billing infrastructure — customers, payments, subscriptions, refunds, invoices, and more. It's part of Stripe's broader `agent-toolkit` monorepo which includes SDKs for integrating Stripe billing into AI-powered applications.

This is a landmark MCP server: the first major payment processor to ship an official MCP endpoint, opening the door for AI agents to autonomously manage billing workflows.

## Key Capabilities

- **Customers** — Create, read, update, delete Stripe customer records
- **Payments & Payment Intents** — Create, confirm, capture, cancel payments
- **Subscriptions** — Manage recurring billing, trial periods, upgrades, cancellations
- **Refunds** — Issue full or partial refunds
- **Invoices** — Create, send, void, and mark invoices as paid
- **Products & Prices** — Define and manage your product catalog and pricing tiers
- **Billing Portal** — Generate customer portal sessions

## Companion SDKs (Same Repo)

| SDK | Purpose |
|-----|---------|
| `@stripe/ai-sdk` | Billing integration with Vercel AI SDK — usage-based billing, metering, subscriptions |
| `@stripe/token-meter` | Track LLM token consumption (OpenAI, Anthropic, Gemini) for pay-per-use billing |
| **Stripe MCP** | Direct agent access to Stripe resources via Model Context Protocol |

## Integration

### 1. Claude Desktop

```json
{
  "mcpServers": {
    "stripe": {
      "type": "http",
      "url": "https://mcp.stripe.com",
      "auth": "oauth"
    }
  }
}
```

### 2. Hermes Agent (config.yaml)

```yaml
mcp:
  servers:
    stripe:
      type: http
      url: https://mcp.stripe.com
      auth: oauth
```

### 3. Cursor / VS Code

Connect via the MCP client using the Streamable HTTP URL `https://mcp.stripe.com` with OAuth.

## Authentication Flow

1. Configure the MCP client with `https://mcp.stripe.com`
2. The client initiates OAuth 2.0 — you'll be redirected to Stripe to authorize
3. Grant access to the Stripe account(s) you want the agent to manage
4. The agent receives a scoped token — permissions are defined by your Stripe account's API key restrictions

**⚠️ Recommendation:** Use a restricted API key with only the permissions your agent needs. Never grant full admin access unless required.

## Business Operator Use Cases

1. **Subscription Health Dashboard** — Agent monitors churn signals (failed payments, expiring trials) and surfaces at-risk accounts
2. **Automated Refund Processing** — Agent handles refund requests against your policy rules, only escalating edge cases
3. **Invoice Reconciliation** — Agent cross-references Stripe invoices against your accounting system
4. **Usage-Based Billing** — Pair with `@stripe/token-meter` for AI-product consumption billing
5. **Revenue Analytics** — Agent queries MRR, churn rate, LTV directly from Stripe data

## Pricing

- **Stripe MCP server:** Free (part of Stripe platform)
- **Standard Stripe fees apply** for any payment processing (2.9% + $0.30 per transaction, etc.)
- No additional MCP-specific charges

## Security Considerations

- Uses Stripe's OAuth 2.0 — industry-standard authentication
- Scoped API key support — limit what your agent can access
- All operations auditable in Stripe Dashboard
- ⚠️ Write operations (refunds, cancellations) should be gated behind human approval for production use

## Verdict

★★★★★ — Landmark MCP server. The first major payment processor to ship an official MCP endpoint. Essential for any business operator who wants AI agents to manage billing, subscriptions, and payment operations. The companion SDKs (`@stripe/ai-sdk`, `@stripe/token-meter`) make this a comprehensive billing toolkit for AI-powered products.
