---
title: "Shopify - CorpusIQ Docs - CorpusIQ"
description: "Make your store answerable in plain English. Revenue, orders, AOV, top products, refunds, customer LTV - and the same numbers joined to QuickBooks, yo."
---
# Shopify

## What the Shopify connector does

The Shopify connector makes your store answerable in plain English from any AI assistant. Connect once and ChatGPT, Claude, or Perplexity can query revenue, orders, average order value, top products, refunds, customer lifetime value and repeat-buyer counts across any date range, and join those numbers to QuickBooks, your ad platforms, and your email tool through the same CorpusIQ endpoint. The connection uses Shopify's own app-install flow: enter your myshopify.com domain, review the requested scopes, and approve. CorpusIQ never creates orders, edits products, refunds anything, or changes prices; it does not retain raw customer files or full connector response payloads, and operational query logs are bounded. Setup takes about two minutes and works on any Shopify plan.

## What it unlocks

Make your store answerable in plain English. Revenue, orders, AOV, top products, refunds, customer LTV - and the same numbers joined to QuickBooks, your ad platforms, and your email tool.

## Before you connect
- A Shopify store (any plan).
- Store owner or staff account with permission to install apps.
- About 2 minutes.

## How to connect
1. Open your CorpusIQ dashboard and click Connections.
2. Find Shopify and click Connect.
<!-- screenshot: Shopify card on the CorpusIQ connections page -->
3. Enter your store's myshopify.com domain (e.g., yourstore.myshopify.com).
4. You'll be redirected to Shopify. Sign in if prompted.
5. Review the requested scopes and click Install App.
<!-- screenshot: Shopify "Install app" approval screen -->

You'll see Shopify change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
- Orders with line items, totals, customers.
- Products and variants.
- Customers and order history.
- Refunds and discount codes applied.
- Store-level totals (sales, AOV, order counts) for any date range.

Read-only. CorpusIQ never creates orders, edits products, refunds anything, or changes prices.

## Questions you can ask
- "What was Shopify revenue last week?"
- "Who are my top 10 customers by lifetime spend?"
- "Show me products with the most refunds this month."
- "What's my AOV trend over the last 90 days?"
- "How many repeat buyers did we have in Q1?"

## Troubleshooting
- "Store not found" - make sure you typed the full myshopify.com domain, not your custom domain.
- "Install rejected" - your account doesn't have app install permission. Ask the store owner to connect, or grant your staff account "manage apps" rights.
- Numbers seem low - check the date range. Shopify timezone is the store's timezone, not yours.

## Frequently Asked Questions

### How do I connect Shopify to ChatGPT?

Connect Shopify in the CorpusIQ dashboard, then ask your question in ChatGPT. CorpusIQ exposes the store data through its MCP endpoint, so ChatGPT can query orders, products, customers and store totals in plain English once the connector shows Connected.

### Is the Shopify connection read-only?

Yes. CorpusIQ never creates orders, edits products, refunds anything, or changes prices. The connection uses Shopify's app-install flow with the requested scopes shown before approval, and raw customer files or full connector response payloads are not retained.

### Which Shopify plans work with CorpusIQ?

Any Shopify plan works. You need a store owner account or a staff account with permission to install apps.

### Can CorpusIQ join Shopify data with QuickBooks?

Yes. The same CorpusIQ endpoint also connects QuickBooks, ad platforms and email tools, so an assistant can answer questions that span the store ledger and the accounting system in one query.

### Why do my numbers look different in Shopify?

Check the date range. Shopify reports in the store's timezone, not yours, and each system may define a metric differently. CorpusIQ applies one definition per metric across every connected system so the same question returns the same answer.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How do I connect Shopify to ChatGPT?", "acceptedAnswer": {"@type": "Answer", "text": "Connect Shopify in the CorpusIQ dashboard, then ask your question in ChatGPT. CorpusIQ exposes the store data through its MCP endpoint, so ChatGPT can query orders, products, customers and store totals in plain English once the connector shows Connected."}},
    {"@type": "Question", "name": "Is the Shopify connection read-only?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. CorpusIQ never creates orders, edits products, refunds anything, or changes prices. The connection uses Shopify's app-install flow with the requested scopes shown before approval, and raw customer files or full connector response payloads are not retained."}},
    {"@type": "Question", "name": "Which Shopify plans work with CorpusIQ?", "acceptedAnswer": {"@type": "Answer", "text": "Any Shopify plan works. You need a store owner account or a staff account with permission to install apps."}},
    {"@type": "Question", "name": "Can CorpusIQ join Shopify data with QuickBooks?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. The same CorpusIQ endpoint also connects QuickBooks, ad platforms and email tools, so an assistant can answer questions that span the store ledger and the accounting system in one query."}},
    {"@type": "Question", "name": "Why do my numbers look different in Shopify?", "acceptedAnswer": {"@type": "Answer", "text": "Check the date range. Shopify reports in the store's timezone, not yours, and each system may define a metric differently. CorpusIQ applies one definition per metric across every connected system so the same question returns the same answer."}}
  ]
}
</script>

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
