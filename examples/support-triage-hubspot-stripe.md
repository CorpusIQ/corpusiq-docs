---
title: "Support Triage with HubSpot and Stripe - CorpusIQ Docs"
description: "Cross-source support triage example: find open HubSpot tickets from customers with past-due Stripe invoices, prioritize by revenue at risk, and answer in seconds."
---
# Example: Support Triage with HubSpot + Stripe

This example shows how CorpusIQ combines CRM and billing data so support teams
can find the customers that matter most: open tickets from accounts with
past-due invoices or a high lifetime value.

No exports, no joining CSVs, no waiting on engineering. One question gets a
ranked answer from your actual tools.

## Prerequisites

1. A CorpusIQ account (free trial at [corpusiq.io](https://corpusiq.io))
2. These connectors connected:
   - **HubSpot** - for tickets, contacts, and companies
   - **Stripe** - for invoices, subscriptions, and payment status

## The Problem

Support queues are full of tickets, but not all tickets are equal. A bug report
from a customer with three open invoices is a bigger deal than the same bug
from a trial account. Figuring out which is which usually means opening two
apps and comparing spreadsheets.

With CorpusIQ, the comparison happens inside the answer.

## Step 1: Find Tickets from Past-Due Accounts

Ask in plain language:

```
Show me open HubSpot tickets from customers with past-due Stripe invoices.
Sort by invoice amount, highest first.
```

CorpusIQ queries HubSpot for open tickets, resolves each contact to their
company, then checks Stripe for invoice status. The answer comes back ranked:

```
Open tickets from past-due accounts (5):

1. Acme Corp - "API rate limit errors" (open 3d) - invoice $1,240 past due
2. Bluebird Retail - "Missing orders in dashboard" (open 1d) - invoice $860 past due
3. Northwind Supply - "Webhook not firing" (open 6d) - invoice $450 past due
4. Lakeside Foods - "Login issues" (open 2d) - invoice $210 past due
5. Fern & Co - "Export broken" (open 4d) - invoice $95 past due
```

## Step 2: Prioritize by Revenue at Risk

Refine the same question to focus on the accounts that matter:

```
Of my open HubSpot tickets, which customers have a Stripe subscription above
$500 per month AND an open ticket older than 2 days?
```

This surfaces the accounts where churn would hurt most, so a manager can route
the senior support rep to those tickets first.

## Step 3: Check Billing History Before Replying

Before replying to a sensitive ticket, pull the customer's full picture:

```
What is Acme Corp's payment history with us? Have any invoices failed recently?
```

CorpusIQ reads Stripe invoice and payment-failure data and summarizes it, so
the reply can acknowledge the customer's situation instead of asking them to
repeat it.

## Why This Works

Cross-source questions are the default in support, not the exception. The
information exists in both systems already. CorpusIQ just removes the manual
join:

- HubSpot knows the ticket and the customer
- Stripe knows the money and the risk
- The answer combines both in one step

## Next Steps

- Try the same pattern with **Shopify** (order history) and **Zendesk** or
  **Intercom** tickets to rank refund requests by order value
- See the [recipes/](../recipes/README.md) directory for more query patterns
- Read [CorpusIQ for Customer Support](/ai-for-customer-support) for the
  full support workflow guide
