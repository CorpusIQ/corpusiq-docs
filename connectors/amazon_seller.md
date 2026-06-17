# Amazon Seller

## What it unlocks
If you sell on Amazon, your real revenue picture is split across Shopify (your own store) and Seller Central (the marketplace). Connecting Amazon Seller lets CorpusIQ pull orders and inventory directly into the same view as your Shopify revenue, QuickBooks expenses, and ad spend — so the question "how is my business doing this month" actually includes Amazon.

## Before you connect
- An Amazon Seller Central account
- Admin permission to authorize third-party apps in Seller Central
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find Amazon Seller.
2. Click Connect.
3. Sign in to Seller Central when prompted and follow the standard Amazon SP-API authorization flow.
4. <!-- screenshot: Amazon Seller authorization consent screen -->
5. Approve read access to orders and inventory and you'll be redirected back to CorpusIQ.

You'll see Amazon Seller change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Orders, with status, totals, and financial details
- FBA inventory levels and stock counts
- Sales metrics derived from order history

CorpusIQ never creates listings, edits inventory, or refunds orders.

## Questions you can ask
- "How many Amazon orders did I get last week?"
- "What's my FBA inventory looking like right now?"
- "Compare my Amazon revenue to Shopify revenue this month."
- "Which products are running low on Amazon stock?"
- "Show me Amazon orders over $200 from the last 30 days."

## Troubleshooting
- **Authorization fails halfway through** — Make sure you're signed in as the primary Seller Central account, not a sub-user without app-authorization rights.
- **No orders returned** — Confirm the date range. Amazon SP-API only exposes orders from the marketplace region tied to your account.
- **Inventory empty** — If you don't use FBA, inventory will be empty by design. Use orders to track sell-through instead.

<!-- DOC-GAP: No internal SETUP doc exists. Setup steps inferred from registry + vendor public docs. Verify before publish. -->

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
