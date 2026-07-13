# Recipe: True ROAS Across Meta Ads and Shopify

**Time to value:** 5 minutes setup.
**Connectors needed:** Meta Ads, Shopify.
**Skill level:** Operator. No code.

## The problem

Meta Ads tells you one ROAS number. Shopify tells you another. Neither accounts for returns, discounts, or shipping costs. Your actual ROAS is somewhere between them and you won't know until you export both datasets and merge them in a spreadsheet.

Most operators never do this. They report the Meta Ads ROAS because it's the bigger number.

## What you'll ask your AI

After connecting Meta Ads and Shopify:

- "For each Meta Ads campaign this week, show me the ad spend, the attributed Shopify revenue, and the actual revenue after returns. Calculate real ROAS."
- "Which campaigns have Meta-reported ROAS above 2.0 but actual ROAS below 1.5 after Shopify returns?"
- "Compare yesterday's ad spend per campaign against today's Shopify orders from those campaigns."

Your AI queries Meta Ads for spend and attributed conversions, Shopify for actual orders and returns, then calculates the number that matters: what you actually made after returns.

## Setup

1. Connect Meta Ads and Shopify through CorpusIQ
2. Read-only OAuth for both. Your AI can query data, never adjust budgets or modify orders.
3. Ask your first question.

## Example

Ask:

> "Show me my Meta Ads campaigns from this week. For each one: total spend, purchases reported by Meta, actual Shopify revenue from those purchases, returns, and real ROAS."

Your AI queries Meta Ads campaign insights, cross-references purchase event values with Shopify order data by timestamp, subtracts returns, and presents a table with the real numbers. Every column is source-cited.

## Why this matters

The difference between Meta-reported ROAS and actual ROAS is often 20 to 40 percent. Returns, canceled orders, and attribution gaps eat into what looks like profit.

If you are spending $10,000 a month on Meta Ads, a 30 percent ROAS gap means $3,000 a month you think you are making but aren't. One question catches that.

---

**Contributed by:** CorpusIQ Growth Agent
**Related recipe:** [Weekly Ad ROI Report](./weekly-ad-roi-report.md)
**Connectors used:** `meta_ads`, `shopify`
