---
title: "Axonaut - CorpusIQ Docs"
description: "Query Axonaut from ChatGPT, Claude or Perplexity. Companies, quotations, invoices, expenses and CRM pipeline answered in plain English, read-only"
last_updated: "2026-11-10"
---
# Axonaut

## What it unlocks

Axonaut runs quotes, invoices, accounting, expenses and CRM for a lot of small businesses in France. The connector brings those records into the conversation you already have with your AI assistant, so a question that used to take three exports and a spreadsheet comes back as one answer with the record cited.

## Before you connect

- An Axonaut account with access to the records you want to query.
- An Axonaut API key. Copy it in Axonaut under Paramètres → API.
- About 2 minutes.

## How to connect

1. In Axonaut, open Paramètres → API and copy your API key.
2. Open your CorpusIQ dashboard and click Connections.
3. Find Axonaut and click Connect.
4. Paste the API key and save. CorpusIQ verifies the connection.

You'll see Axonaut change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see

- Companies, contacts and suppliers.
- Quotations and invoices, with line items and status.
- Payments recorded against invoices.
- CRM opportunities and events.
- Expenses and accounting entries.
- Products, contracts, employees and users.
- Custom fields configured in your Axonaut account.

Read-only. CorpusIQ never creates or edits quotations, invoices or payments, never changes companies, contacts or opportunities, never records an expense and never posts an accounting entry.

## Long lists

Axonaut returns a whole collection per resource. CorpusIQ pages that collection and hands the assistant one window at a time, together with the total record count and a `has_more` flag, so it can tell you when more records exist instead of quietly showing you a truncated list.

## Questions you can ask

- "Which invoices are still unpaid this month?"
- "What quotations are waiting on a customer signature?"
- "Show me open opportunities by stage."
- "What did we spend with each supplier last quarter?"
- "Which contracts renew in the next 60 days?"
- "How does invoiced revenue this month compare to last month?"

## Troubleshooting

- "Authentication failed" - copy the key again from Paramètres → API. A trailing space in the pasted key is the usual cause.
- A section looks empty - the API key belongs to an Axonaut user, and that user's permissions decide which records the key can read.
- A list stops at a round number - ask for the next page. The response carries `has_more`, so the assistant knows there is more.

## See also

- [QuickBooks](quickbooks.md) - accounting and invoicing questions for your books.
- [Odoo](odoo.md) - ERP and CRM records across modules in one query.
- [HubSpot](hubspot.md) - CRM pipeline and deal reporting.
- [Connector directory](../connectors.md) - all 40+ CorpusIQ connectors in one place.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
