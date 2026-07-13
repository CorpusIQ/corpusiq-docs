# Recipe: Replace Your Morning Dashboard Check With One Question

**Time to value:** 5 minutes setup.
**Connectors needed:** Any 3 of your daily-check tools. GA4, Stripe, Shopify, Klaviyo, Meta Ads, QuickBooks.
**Skill level:** Operator. No code.

## The problem

Every morning you check the same five dashboards. GA4 for traffic. Stripe for revenue. Klaviyo for email. Meta Ads for spend. Shopify for orders.

Each one takes 2 minutes to load, find the right report, set the date range, and read the numbers. That is 10 minutes every morning. 50 minutes a week. Over 40 hours a year just looking at dashboards.

And half the time you see a number that makes you log into a second tool to verify it. Now you are at 20 minutes.

## What you will ask your AI

After connecting your tools:

"Good morning. Show me yesterday's traffic from GA4, revenue from Stripe, email sends from Klaviyo, ad spend from Meta Ads, and orders from Shopify. Flag anything that changed more than 20 percent from the day before."

Your AI queries all five tools, pulls the numbers, compares against the previous day, and delivers a morning briefing with anomalies flagged. Source cited for every number.

## Setup

1. Connect your daily-check tools in CorpusIQ
2. Read-only OAuth for all. Your AI reads data, never modifies.
3. Ask your morning question.

## Example briefing

Ask your AI:

"Morning briefing for July 13. Show me GA4 sessions, Stripe net revenue, Klaviyo campaign sends, Meta Ads spend, and Shopify order count. Compare each against July 12. Flag anything outside normal range."

Your AI returns something like:

- GA4 sessions: 2,847 (up 12% from yesterday)
- Stripe net revenue: $14,230 (up 8%)
- Klaviyo campaign sends: 18,400 (normal)
- Meta Ads spend: $342 (down 15% — flag)
- Shopify orders: 47 (up 4%)

The Meta Ads drop gets flagged. You investigate. Turns out a campaign exhausted its budget overnight. You catch it at 8 AM instead of discovering it at the weekly review. You fix it in 30 seconds.

## Why this matters

You did not learn anything from those dashboards you could not have learned from one question. But you spent 40 hours a year pulling the numbers manually.

One question. All your tools. Morning briefing done in 15 seconds.

---

**Contributed by:** CorpusIQ Growth Agent
**Connectors used:** `ga4`, `stripe`, `klaviyo`, `meta_ads`, `shopify`, `quickbooks`
