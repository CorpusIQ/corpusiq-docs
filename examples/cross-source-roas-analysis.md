# Example: Cross-Source ROAS Analysis with Shopify + Meta Ads + Google Ads

This example shows how to use CorpusIQ to calculate true Return on Ad Spend by connecting Shopify revenue data with Meta Ads and Google Ads spend data.

Real ROAS in one question. No spreadsheets, no manual data pulls.

## Prerequisites

1. A CorpusIQ account (free trial at [corpusiq.io](https://corpusiq.io))
2. These connectors connected:
   - **Shopify** — for revenue, orders, and customer data
   - **Meta Ads** (Facebook/Instagram) — for ad spend and campaign data
   - **Google Ads** — for ad spend and campaign data
3. CorpusIQ added to your AI tool (Claude Desktop, ChatGPT, or Cursor)

## What We're Building

Instead of exporting CSVs from three platforms and building a spreadsheet, you ask one question and get the answer:

> "What was my ROAS last month, broken down by Meta Ads and Google Ads, using revenue data from Shopify?"

## Step 1: Connect Your Data Sources

Log into [corpusiq.io](https://corpusiq.io) and connect:
- **Shopify:** Click "Connect Shopify" → authorize via OAuth → done in 30 seconds
- **Meta Ads:** Click "Connect Meta Ads" → select your ad account → authorize
- **Google Ads:** Click "Connect Google Ads" → select your Google Ads account → authorize

All three connectors should show as "Connected" (green) in your dashboard.

## Step 2: Ask the ROAS Question

Open Claude Desktop (or your preferred AI tool with CorpusIQ connected) and ask:

```
What was my ROAS last month? I want it broken down by Meta Ads and Google Ads.
Use actual revenue from Shopify and ad spend from each platform.
```

## Step 3: What Happens

CorpusIQ runs three queries in parallel:

1. **Shopify:** `SELECT SUM(total_price) FROM orders WHERE created_at >= '2026-06-01' AND created_at < '2026-07-01' AND financial_status = 'paid'`
2. **Meta Ads:** `SELECT campaign_name, SUM(spend) FROM ad_insights WHERE date_start >= '2026-06-01' AND date_stop < '2026-07-01' GROUP BY campaign_name`
3. **Google Ads:** `SELECT campaign_name, SUM(cost_micros)/1000000 FROM campaign WHERE segments.date >= '2026-06-01' AND segments.date < '2026-07-01'`

Then it does the math:

```
Meta Ads ROAS = Shopify Revenue / Meta Spend = $45,200 / $12,800 = 3.53x
Google Ads ROAS = Shopify Revenue / Google Spend = $45,200 / $8,400 = 5.38x
Combined ROAS = $45,200 / $21,200 = 2.13x
```

If you have UTM tracking or campaign attribution set up, you can get even more granular.

## Step 4: Go Deeper

Follow-up questions you can ask:

- "Which Meta Ads campaign had the highest ROAS?"
- "Show me ROAS by week for the last quarter"
- "What's the customer acquisition cost (CAC) for customers who came through Google Ads vs Meta Ads?"
- "Which products generated the most revenue from paid traffic?"

Each of these triggers the same pattern: CorpusIQ queries the relevant connectors, joins the data intelligently, and your AI tool formats the answer.

## Why This Matters

Traditional ROAS analysis requires:
- Exporting Shopify orders to CSV
- Exporting Meta Ads data to CSV
- Exporting Google Ads data to CSV
- Building a spreadsheet with VLOOKUPs
- Manual updates every time you want to check

With CorpusIQ, it's one question. Every time. The data is always live.

## Next Steps

- Try the [QuickBooks + Shopify reconciliation example](../recipes/shopify-quickbooks-reconciliation.md)
- Learn about [cross-source queries](../how-it-works/mcp-architecture.md)
- Check out the [HubSpot + Klaviyo pipeline example](../recipes/hubspot-klaviyo-pipeline.md)
