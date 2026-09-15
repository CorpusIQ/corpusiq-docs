---
title: "Checkout Page MCP - Stripe Payments, Subscriptions and Tickets for AI Agents"
description: "Hosted remote MCP server for the Checkout Page platform: 40 tools that let an AI assistant create checkout pages, events and tickets, bookings, lead-capture forms, customers, payments, subscriptions, invoices, coupons, tax rates and webhooks. Payments run on the merchant's own Stripe account, and OAuth sign-in means there are no API keys to copy."
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-09-15
source: "mcp.so feed (Sep 15 morning, submitted 2h before sweep) + vendor page at mcp.so/clients/checkout-page-mcp"
relevance: ★★★
tags: [checkout, payments, subscriptions, event-tickets, invoices, coupons, webhooks, stripe, oauth, remote-mcp]
---

# Checkout Page MCP

**Commerce operations from the chat window.** Checkout Page is a no-code checkout platform for businesses that sell on their own Stripe account: one-time products, subscriptions, event tickets, memberships and lead-capture forms. Its hosted MCP server gives an AI assistant direct access to the account, with 40 tools across pages, events, bookings, forms, customers, payments, subscriptions, invoices, coupons, tax rates, files and webhooks.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first connect)
Endpoint: https://mcp.checkoutpage.com
Tools: 40 (checkout pages, events and tickets, bookings, forms, customers, payments, subscriptions, invoices, coupons, tax rates, files, webhooks)
Pricing: Checkout Page plans from the dashboard; payments go directly to your own Stripe account
Category: Commerce & E-Commerce / Payments
Built by: Checkout Page (checkoutpage.com), docs at checkoutpage.com/docs/build/mcp
```

## Why This Matters for Operators

Checkout pages, event tickets and subscription plans are the last mile of revenue, but building them still means dashboard clicking: create the page, wire the price, add the coupon, find the customer, check the payment. That work is perfectly specifiable, which makes it agent work. The MCP server turns it into plain-language operations with the account's own permissions.

The Stripe relationship is the key detail: payments go straight to your Stripe account, so the agent is not a new payment rail, it is a new interface to the rail you already have. Read tools never change data, and write tools run with the same permissions as the dashboard, so the blast radius matches what a logged-in operator could already do.

## Tools & Capabilities

| Resource | Tools |
|---|---|
| Checkout pages | create, get, update |
| Events and tickets | create event, get event, update event, list tickets, update ticket |
| Bookings | create, get, list |
| Forms and submissions | create form, get form, update form, list submissions, get submission |
| Customers | list, get, update |
| Payments | list, get |
| Subscriptions | list, get, cancel, list subscription payments, get subscription payment |
| Invoices | list, get, regenerate |
| Coupons | create, list, update |
| Tax rates | create, list |
| Files | upload from a public URL |
| Webhooks | create, get, list, update, delete |

Read tools never change data. Write tools run with your own account permissions, the same as the dashboard.

## Installation

```bash
claude mcp add checkoutpage --transport http https://mcp.checkoutpage.com
```

Step-by-step guides for Claude, ChatGPT, Cursor, VS Code, Codex and Claude Code are published at checkoutpage.com/docs/build/mcp. The first connection opens a one-click Checkout Page sign-in in the browser.

## Configuration

```json
{
  "mcpServers": {
    "checkoutpage": {
      "type": "http",
      "url": "https://mcp.checkoutpage.com"
    }
  }
}
```

Authentication is OAuth, so there are no API keys to copy or rotate; access is managed and revoked from the Checkout Page account.

## Business Relevance

- **Course creators and event operators** get event creation with ticket types and booking counts asked in plain language.
- **E-commerce operators** get products, coupons, tax rates and payment summaries handled by the assistant, with the money still landing in their own Stripe account.
- **Agencies** get checkout pages and client webhooks provisioned from the chat window instead of the dashboard.
- **Support teams** get customer lookups, subscription state and invoice regeneration without handing out dashboard logins.

## Integration with CorpusIQ

Checkout Page and CorpusIQ meet at Stripe. CorpusIQ's Stripe connector reads the ledger: revenue, refunds, disputes, payouts. Checkout Page writes the top of the funnel: the pages, plans, coupons and tickets that generate the charges. A composed workflow runs both: the agent builds the Pricing Strategy Workshop checkout page with an early-bird coupon through Checkout Page, then reads the resulting revenue through CorpusIQ's Stripe connector in the same session, alongside QuickBooks for books and GA4 for the traffic that converted. The agent manages the commerce surface and the operator reads one reconciled view.

## Limitations

- Brand new: submitted to mcp.so hours before this guide; no public track record yet.
- Commercial platform: requires a Checkout Page account and its plans; the MCP server is not self-hostable.
- Write tools execute with account permissions immediately; there is no confirm-first gate described, so scope what the agent is asked to do.
- Stripe-only rails: no alternative payment processors behind the connector.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
