# Recipe: Cross-Source Revenue Audit

**Time to value:** 5 minutes setup, instant answers after that.
**Connectors needed:** Stripe, QuickBooks, Shopify (any 2 of 3 works)
**Skill level:** Operator. No code required.

## The problem

You have revenue in Stripe. Orders in Shopify. Invoices in QuickBooks. These numbers should match. They rarely do.

Reconciling them means exporting CSV files from three platforms, loading them into Excel, running VLOOKUPs, and spending 30 minutes to confirm what you already suspected: $2,300 is missing somewhere.

## What you'll ask your AI

After connecting your tools through CorpusIQ, you ask questions like:

- "What's my actual collected revenue this month across Stripe and Shopify? Compare against QuickBooks invoices."
- "Show me Stripe charges from last week that don't have matching QuickBooks invoices."
- "Which Shopify orders from yesterday are still pending in Stripe?"

Your AI queries all three tools live and gives you the answer with sources cited. No exports, no spreadsheets, no VLOOKUPs.

## Setup

1. Connect Stripe, QuickBooks, and Shopify in your CorpusIQ dashboard (corpusiq.io/connectors)
2. Each connection uses read-only OAuth. Your AI can read data, never write or spend.
3. That's it. No API keys to manage. No code to write.

## Example: Find unmatched Stripe charges

Ask your AI:

> "List Stripe charges from July 1-7 over $100. For each one, check if there's a matching QuickBooks invoice by amount and customer email. Show me the ones without matches."

Your AI queries Stripe's charges endpoint, QuickBooks' invoice endpoint, cross-references by amount and email, and returns only the unmatched items. Source citations for every number.

## Why this matters

The alternative is exporting CSV files from three platforms, merging them manually, and hoping your formulas are right. Most operators do this once a month. Some do it once a quarter. Many never do it at all and just hope the numbers are close enough.

One question. All your tools. Source cited. Done.

---

**Contributed by:** CorpusIQ Growth Agent
**Related recipe:** [Shopify-QuickBooks Reconciliation](./shopify-quickbooks-reconciliation.md)
**Connectors used:** `stripe`, `quickbooks`, `shopify`
