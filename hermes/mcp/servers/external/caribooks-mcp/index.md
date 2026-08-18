---
title: "Caribooks MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Hosted MCP server connecting QuickBooks Online Canada and US companies to Claude, ChatGPT and any MCP client with 160+ read and write tools"
category: Finance & Accounting
stars: n/a (new listing)
added: 2026-08-18
source: mcp.so GitHub issues
relevance: ★★★
tags: [quickbooks, accounting, bookkeeping, invoicing, oauth, remote-mcp, canada, write-access]
---

# Caribooks MCP

**Hosted MCP server (Streamable HTTP, OAuth 2.1) that connects QuickBooks Online to Claude, ChatGPT, and any MCP client — 160+ tools covering the whole ledger, with a write path for invoices, payments, bills, and journal entries.** Built for QuickBooks Online Canada, which Intuit's official Claude connector skips (it is US-only and sales-side). No developer keys, nothing to install: sign in, connect one or more companies through Intuit's OAuth flow, add the server URL to the assistant, and ask or delegate in English or French.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with dynamic client registration (Intuit sign-in, no developer keys)
Endpoint: https://caribooks.com/api/mcp
Tools: 160+ (read + opt-in write per company)
Pricing: CA$39 per company/month (CA$29 from 10 companies); free 14-day trial, no card
Category: Finance & Accounting
Built by: Caribooks (caribooks.com, hosted in Canada)
```

## Why This Matters for Operators

Bookkeeping is where AI delegation makes the most visible difference to a small business: the work is real, repetitive, and directly financial. Caribooks turns the assistant from a Q&A surface into a working bookkeeping clerk — it reads profit and loss, aged receivables, and the general ledger, and it creates invoices, records payments, files expenses, and posts journal entries when you flip write access on per company. Every delete requires confirmation, and no write happens until you enable it company by company.

**The data model is pass-through.** Caribooks stores none of your accounting data: only your account email, company names, and the Intuit tokens (AES-256 encrypted, AWS Montréal region). Ledger data flows encrypted from QuickBooks to your assistant and stops there. Anthropic excludes connector data from training on all plans, and OpenAI does not train on Business, Enterprise, or Edu — with a settings toggle for personal accounts.

## Tools & Capabilities

| Tool area | What it does |
|---|---|
| Profit and loss | Current P&L on demand |
| Balance sheet | Positions, assets, liabilities |
| Aged receivables / payables | Overdue buckets with customer context |
| Trial balance / cash flow | Bookkeeping integrity and cash positions |
| General ledger detail | Line-level entry inspection |
| Search | Customers, invoices, expenses, entries |
| Invoices | Create and update invoices |
| Payments | Record incoming payments |
| Estimates | Draft estimates |
| Vendor bills | Enter bills and pay them |
| Expenses | File and categorize expenses |
| Journal entries | Post entries directly |
| Master data | Create customers, vendors, and items |
| Credit memos / refunds | Issue credit memos and refunds |

Reads answer questions; writes do the work. The demo flow on the site is representative: "Which invoices are overdue? Politely chase the ones past 30 days" produces a per-customer table, drafted reminders tuned per customer, and a send step.

## Installation

1. Sign up at caribooks.com (free 14-day trial, no card).
2. Connect QuickBooks Online companies with the standard Intuit authorization.
3. Copy the prefilled install link into Claude or ChatGPT (or add the MCP URL to any client).

```json
{
  "mcpServers": {
    "caribooks": {
      "type": "http",
      "url": "https://caribooks.com/api/mcp"
    }
  }
}
```

## Configuration

Write access is off by default and enabled per company from the Caribooks dashboard. Deletes always require confirmation. Tokens can be revoked at any time from either side — the connection is just an Intuit access key, never your QuickBooks password. Works alongside other connectors (Gmail, Outlook, Calendar) in the same assistant.

## Business Relevance

- **Canadian operators** get the only full-ledger QBO connector that covers Canada today, bilingual in English and French
- **Solo operators** delegate invoice creation, expense filing, and payment recording without hiring a bookkeeper
- **Accounts receivable** gets the overdue-chase workflow: identify, draft tuned reminders, send
- **Multi-company operators** manage several QuickBooks companies from one assistant, at CA$29/company from 10 companies
- **Compliance-conscious firms** get pass-through data handling with no ledger data stored by the vendor

## Integration with CorpusIQ

CorpusIQ's QuickBooks connector is the read-only analytics layer — profit and loss, invoices, AR aging, and payments pulled into multi-source business views alongside GA4, Stripe, and ad spend. Caribooks adds what the CorpusIQ connector deliberately does not: a write path into the books and full Canadian coverage.

The composed workflow: CorpusIQ answers "what is the financial picture and who owes us money" across sources, and Caribooks executes the follow-through — drafting the invoice, recording the payment, or posting the entry — from the same conversation. Read-only reporting and gated writes stay on separate surfaces, which is the safer split.

## Limitations

- QuickBooks Online only — no QuickBooks Desktop or Xero
- Brand new listing (submitted Aug 16, 2026); no long track record yet
- Commercial — CA$39 per company per month after trial
- Write path requires deliberate per-company opt-in
- Hosted service — no self-host option; token custody rests with Caribooks (encrypted, Canada)
