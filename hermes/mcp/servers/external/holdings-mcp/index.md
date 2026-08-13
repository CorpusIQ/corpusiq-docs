---
title: "Holdings MCP — Integration Guide"
description: "Agentic invoicing and payments — let your AI send invoices and take payment via card or ACH. Free. Holdings MCP server for Claude, ChatGPT, and Cursor."
category: mcp
tags: [mcp-server, invoicing, payments, finance-operations, accounts-receivable, hermes-agent]
last_updated: 2026-08-10
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/holdings-mcp/"
robots: "index,follow"

---

# Holdings MCP — Agentic Invoicing & Payments

**Rating:** ★★★ | **Category:** Finance & Commerce | **Transport:** stdio (npm) or Streamable HTTP (remote)

## What It Does

Holdings is agentic invoicing — software your AI can run. Connect Claude, ChatGPT, or Cursor, tell it who to bill, and it drafts the invoice, shows you a preview, and sends it the moment you confirm. Your client pays by card or ACH; you're told when the money lands. Free, no monthly fee — you pay standard payment-processing fees only when a client pays.

## Why Business Operators Need This

Invoicing is one of the highest-friction operational tasks for small businesses and freelancers. Holdings makes it a conversational action: "Send Acme the December retainer — $8,400, net 30." The agent drafts, you approve, the client pays. Every write is confirm-gated — a draft is created first, amounts are recomputed server-side, and nothing reaches a client until you explicitly confirm. This is the first MCP server to bridge the gap between AI agents and real payment collection.

**Competitive landscape:** No other MCP server handles invoicing and payment collection. Stripe MCP (catalogued earlier) handles payment infrastructure but not invoicing workflows. QuickBooks MCP (catalogued earlier) handles accounting but requires a QuickBooks subscription. Holdings is purpose-built for agentic invoicing with no monthly platform fee.

## Quick Start

### Connection Details

| Field | Value |
|-------|-------|
| **Transport (local)** | stdio via `npx -y @getholdings/mcp` |
| **Transport (remote)** | Streamable HTTP at `https://mcp.getholdings.com/mcp` |
| **Authentication** | API key (`HOLDINGS_API_KEY`) or Bearer token |
| **Pricing** | Free (no monthly fee; standard Stripe processing fees on payments) |
| **npm** | `@getholdings/mcp` |
| **GitHub** | `holdings-io/mcp` (0★, created Jul 28, 2026) |

### Option 1: Local (stdio) — Claude Desktop, Cursor, Cline, Windsurf

```json
{
  "mcpServers": {
    "holdings": {
      "command": "npx",
      "args": ["-y", "@getholdings/mcp"],
      "env": {
        "HOLDINGS_API_KEY": "hw_live_your_key_here"
      }
    }
  }
}
```

### Option 2: Remote (Streamable HTTP) — Any MCP Client

```json
{
  "mcpServers": {
    "holdings": {
      "transport": "http",
      "url": "https://mcp.getholdings.com/mcp",
      "headers": {
        "Authorization": "Bearer hw_live_your_key_here"
      }
    }
  }
}
```

### Claude Code

```bash
claude mcp add --transport http holdings https://mcp.getholdings.com/mcp \
  -H "Authorization: Bearer hw_live_your_key_here"
```

### Get an API Key

Create a free key in your Holdings workspace → **Settings → API keys**. No monthly fee.

## Key Tools

| Category | Capability | Description |
|----------|-----------|-------------|
| **Invoices** | Draft, preview, send, track | Create invoices with line items, preview before sending, track payment status |
| **Quotes** | Create, send, convert | Send estimates; turn accepted quotes into invoices |
| **Clients** | CRUD operations | Manage the people and businesses you bill |
| **Payments** | View status | See what's paid, outstanding, and overdue |

Every write operation is **confirm-gated**: a draft is created first, nothing reaches a client until you explicitly approve the send. Amounts are recomputed server-side — the agent can't override totals.

## Example Usage

### Send an Invoice

Ask your agent: *"Send Acme Corp the December retainer — $8,400, net 30."*

The agent drafts the invoice with line items, shows you a preview with the computed total, and waits for your confirmation before sending. Acme gets a payment link; you get notified when they pay.

### Convert a Quote to Invoice

Ask your agent: *"Turn the accepted Q4 proposal for GlobalTech into an invoice."*

The agent finds the quote, converts it to an invoice, and sends it — all in one conversation.

### Check Outstanding Payments

Ask your agent: *"Who still owes us money?"*

The agent lists all outstanding invoices with amounts, due dates, and client names.

### Set Up Recurring Invoices

Ask your agent: *"Set up a monthly $2,500 retainer invoice for DesignCo, starting January."*

The agent creates the recurring invoice template with monthly scheduling.

## Pricing

- **Platform fee:** Free (no monthly subscription)
- **Payment processing:** Standard Stripe fees (2.9% + $0.30 for cards; 0.8% cap for ACH)
- **No hidden costs:** Pay only when you get paid

## Repository & Resources

| Resource | URL |
|----------|-----|
| **GitHub** | [github.com/holdings-io/mcp](https://github.com/holdings-io/mcp) |
| **Website** | [getholdings.com/invoicing](https://getholdings.com/invoicing) |
| **npm** | [npmjs.com/package/@getholdings/mcp](https://www.npmjs.com/package/@getholdings/mcp) |
| **Smithery** | [smithery.ai/servers/holdings/invoicing](https://smithery.ai/servers/holdings/invoicing) |
| **MCP Registry** | `com.getholdings/mcp` |
| **MCP Endpoint** | `https://mcp.getholdings.com/mcp` |

## Verdict: ★★★ — Essential for Freelancers & Small Business Operators

Holdings is the first MCP server that makes invoicing and payment collection an agent-native capability. The confirm-gated design (draft → preview → confirm → send) is exactly right for financial operations — the agent does the work, but you stay in control. Free pricing with no monthly fee removes the adoption barrier entirely.

**Strengths:** Free (no monthly fee), confirm-gated writes prevent errors, dual transport (stdio + HTTP), card + ACH support, quotes-to-invoices conversion, recurring invoices, MCP Registry listed.

**Limitations:** Brand new (0 stars, created Jul 2026), built on Stripe (requires Stripe account), limited to invoicing/payments (no expense tracking, no accounting), US-focused payment methods.

**Best for:** Freelancers, small agencies, consultants, and service businesses who invoice clients regularly and want to do it from within their AI assistant.
