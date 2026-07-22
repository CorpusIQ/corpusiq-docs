---
title: FreshBooks MCP Server Integration Guide
description: Accounting automation for AI agents — manage clients, invoices, expenses, and payments through FreshBooks MCP. Connect your accounting to Hermes Agent.
category: mcp
tags: [mcp, freshbooks, accounting, invoicing, expenses, payments, small-business, hermes-agent]
last_updated: 2026-07-21
---

# FreshBooks MCP — Accounting Automation for Hermes Agent

FreshBooks MCP connects your AI agent directly to FreshBooks accounting — manage clients, create and send invoices, track expenses, and record payments without touching the FreshBooks dashboard.

## What It Does

FreshBooks MCP brings small-business accounting into the agent workflow:

- **Client management** — List, search, create, and update clients
- **Invoice operations** — Create, send, and track invoices with line items
- **Expense tracking** — Log expenses with categories, attachments, and tax info
- **Payment recording** — Record payments against invoices, track outstanding balances
- **Reports access** — Pull profit & loss, expense reports, and invoice aging

## Quick Setup

### Prerequisites
- **FreshBooks account:** Sign up at [freshbooks.com](https://www.freshbooks.com)
- **FreshBooks API credentials:** Generate from FreshBooks Developer dashboard
- **Node.js 18+** on your machine

### Add to Hermes Agent

```bash
# Clone and configure
git clone https://github.com/codeChap/mcp-server-freshbooks
cd mcp-server-freshbooks
npm install
```

```json
{
  "mcpServers": {
    "freshbooks": {
      "command": "node",
      "args": ["path/to/mcp-server-freshbooks/index.js"],
      "env": {
        "FRESHBOOKS_CLIENT_ID": "your_client_id",
        "FRESHBOOKS_CLIENT_SECRET": "your_client_secret",
        "FRESHBOOKS_REDIRECT_URI": "http://localhost:3000/callback",
        "FRESHBOOKS_ACCOUNT_ID": "your_account_id"
      }
    }
  }
}
```

## Key Capabilities

| Tool | Description |
|------|-------------|
| `list_clients` | List all clients with search and filter |
| `get_client` | Get client details by ID |
| `create_client` | Create a new client with contact info |
| `create_invoice` | Create an invoice with line items, taxes, and due dates |
| `send_invoice` | Send an invoice to the client via email |
| `list_invoices` | List invoices with status filters (draft, sent, paid, overdue) |
| `create_expense` | Log an expense with category, amount, and receipt attachment |
| `list_expenses` | List expenses with date range and category filters |
| `record_payment` | Record a payment against one or more invoices |
| `get_profit_loss` | Pull profit & loss report for a date range |

## Use Cases for Business Operators

### 1. Automated Client Invoicing
Have your agent generate and send invoices based on completed work:

```
Agent prompt: "We just finished the website redesign for Acme Corp.
Create a FreshBooks invoice for $4,500 — 50% deposit already paid.
Line items: Design ($2,000), Development ($2,000), Project Management ($500).
Send to billing@acmecorp.com with net-30 terms."
```

### 2. Expense Reconciliation
Feed receipts to your agent for automatic logging:

```
Agent prompt: "I have 15 receipts from my business trip. Extract the amounts,
categorize them (travel, meals, software, office), and log each
as a FreshBooks expense against the correct client project."
```

### 3. Cash Flow Monitoring
Get real-time financial visibility:

```
Agent prompt: "What's my cash position? Show me all outstanding invoices
over 30 days, total unbilled work, and upcoming expenses for the next 2 weeks.
Flag any clients who are 60+ days past due."
```

### 4. Tax Preparation
Pull categorized financials for tax season:

```
Agent prompt: "Pull my full-year 2026 P&L broken down by category.
Export all expenses with receipts for my CPA. Flag any large
uncategorized transactions."
```

## Integration with CorpusIQ

FreshBooks MCP + CorpusIQ = complete financial operations:

1. **CorpusIQ Stripe connector** → auto-record payments against FreshBooks invoices
2. **CorpusIQ email connector** → find vendor invoices for expense creation
3. **AI agent** → reconcile Stripe payouts, bank feeds, and FreshBooks in one pass
4. **CorpusIQ Gmail connector** → auto-attach emailed receipts to expenses

This replaces the manual "export CSV from Stripe, import to FreshBooks, match by hand" workflow with an agent that does it in seconds.

## Pricing

- **FreshBooks MCP:** Open source (MIT), free
- **FreshBooks:** Plans start at $19/month (Lite), $33/month (Plus), $60/month (Premium)
- **API access:** Available on Plus plan and above

## Limitations

- OAuth2 flow requires browser interaction for initial setup
- FreshBooks API rate limits apply (typically 100 requests/minute)
- Multi-currency requires Plus plan or higher

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*
