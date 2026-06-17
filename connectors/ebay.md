# eBay

## What it unlocks
For eBay sellers, the financial truth sits inside Seller Hub — orders, transactions, fees, seller standards, traffic. Connecting eBay lets CorpusIQ fold marketplace revenue and seller health into the same answers as your other channels, so you can see your full business picture without bouncing between dashboards.

## Before you connect
- An eBay seller account
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find eBay.
2. Click Connect.
3. Sign in to eBay when the consent screen appears.
4. <!-- screenshot: eBay OAuth consent screen -->
5. Approve the requested seller scopes and you'll be returned to CorpusIQ.

You'll see eBay change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Orders with GMV, item counts, and fulfillment status
- Financial transactions (sales, credits, refunds, fees)
- Seller standards profile
- Customer service metrics, including INAD and INR rates
- Listing traffic reports
- Funds summary — settled, on hold, total balance
- Seller privileges and entitlements

CorpusIQ never lists items, edits listings, refunds buyers, or moves funds.

## Questions you can ask
- "What's my eBay GMV for the last 30 days?"
- "How are my seller standards trending?"
- "Show me eBay funds on hold right now."
- "Which listings got the most impressions last week?"
- "What's my refund rate on eBay this quarter?"

## Troubleshooting
- **"Missing finances scope"** — Disconnect and reconnect; the funds summary requires the `sell.finances` scope which is requested during OAuth.
- **Traffic report empty** — eBay's traffic data has a 24–48 hour lag. Check yesterday's date, not today's.
- **Standards profile blank** — New sellers don't have a standards profile yet; eBay requires a minimum order volume.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
