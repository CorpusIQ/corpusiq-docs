# How to Reconcile Meta Ads and Shopify Revenue: The Operator's Guide

If you run Facebook/Instagram ads for a Shopify store, you've seen this: Meta reports $10,000 in purchase conversion value. Shopify reports $8,200. They will never match. Here's why — and how to actually reconcile them.

## Why Meta and Shopify Numbers Never Agree

Meta and Shopify use fundamentally different attribution models:

| Platform | Attribution Model | What It Means |
|---|---|---|
| **Meta Ads** | 7-day click + 1-day view (default) | If someone saw your ad in the last 24 hours, then bought — Meta claims the sale. Even if they would have bought anyway. |
| **Shopify** | Last-click | Credits the last channel the customer clicked before buying. If they clicked a Google ad, Shopify credits Google — even if Meta's ad started the journey. |
| **Google Ads** | Data-driven attribution | Uses machine learning to distribute credit across touchpoints. |
| **Klaviyo** | Email assist | Attributes revenue to email flows and campaigns based on when emails were opened/clicked. |

**The result:** Multiple platforms all claiming credit for the same sale. If you add up platform-reported revenue, you'll often get 130-180% of your actual revenue.

## The Manual Reconciliation Method (What Most Operators Do)

Every Monday morning, thousands of operators do this:

1. Export Meta Ads data (campaign, ad set, spend, reported revenue)
2. Export Shopify orders (order ID, product, revenue, source)
3. Export Google Ads data
4. Open Excel/Google Sheets
5. Build a pivot table
6. Manually match transactions across platforms
7. Calculate true ROAS per product/SKU
8. Figure out which products are actually profitable

**Time spent:** 2-4 hours per week. **150+ hours per year.**

## The 3-Line Python Method

If you're comfortable with code, here's a lightweight reconciliation approach using our open-source package:

```python
from cross_source_roas import reconcile

table = reconcile("shopify_orders.csv", "meta_ads.csv")
print(table.summary())
```

Output:
```
              ad_spend  shopify_revenue  true_roas  platform_roas  gap
Signature Hoodie   $2,140          $6,820       3.19x          3.67x  +0.48x
Classic Tee        $1,260          $1,910       1.52x          1.79x  +0.27x
Logo Cap           $1,840          $1,120       0.61x          0.66x  +0.05x
```

**Time spent:** 14 seconds.

[Get cross-source-roas on GitHub →](https://github.com/Ben-Home/cross-source-roas)

## The Full-Stack Method (No Code Required)

For operators who want full reconciliation across ALL channels — including QuickBooks, Stripe, GA4, and Klaviyo — without writing code:

1. Connect your stack to CorpusIQ (60 seconds, 37+ connectors)
2. Ask: "Which product is burning ad spend?"
3. Get the answer in 14 seconds with true ROAS across every channel

CorpusIQ doesn't model attribution. It reconciles actual transaction data across platforms — matching orders to ad spend, factoring in email assist, and showing you the real numbers.

[Try CorpusIQ free →](https://corpusiq.io)

## Why True ROAS Matters

Platform ROAS is misleading because of attribution overlap:

- Meta might claim a 3.2x ROAS on a campaign
- But 30% of those "Meta-attributed" sales were actually driven by a Klaviyo email flow
- And 15% would have happened organically regardless of ads

**True ROAS** strips out the overlap. It answers: "If I turned off this ad, how much revenue would I actually lose?"

For the Logo Cap in the example above — true ROAS of 0.61x means you're losing $0.39 for every dollar spent. Platform ROAS of 0.66x masks some of the damage but the decision is the same: pause it.

## The Bottom Line

You have three options for reconciling Meta and Shopify:

1. **Manual (Excel):** Free but costs 150 hours/year. Error-prone.
2. **Open-source (cross-source-roas):** Free, takes 14 seconds, but only handles Meta + Shopify CSV reconciliation.
3. **Full-stack (CorpusIQ):** 37+ connectors, true cross-source reconciliation, AI-native. Free tier available.

Stop trusting platform ROAS. Start reconciling.

---

*Last updated: June 2026*
