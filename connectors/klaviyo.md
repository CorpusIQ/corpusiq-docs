# Klaviyo

## What it unlocks
For ecommerce brands, Klaviyo is where email and SMS revenue actually gets attributed. Connecting it lets CorpusIQ pull campaign performance, flow revenue, abandoned cart recovery, list health, and predictive analytics — and combine them with Shopify and GA4 to answer the only question that matters: how much revenue did email actually drive this month?

## Before you connect
- A Klaviyo account with admin access
- A Klaviyo private API key (Account → Settings → API keys)
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find Klaviyo.
2. Click Connect.
3. <!-- screenshot: Klaviyo API key form in CorpusIQ -->
4. In a second tab, go to Klaviyo → Account → Settings → API keys and create a private API key with read scopes on Campaigns, Flows, Lists, Segments, Profiles, Metrics, Forms, and Events.
5. Copy the key and paste it into the CorpusIQ form.
6. Click Save.

You'll see Klaviyo change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Campaigns and per-campaign metrics (opens, clicks, revenue, conversions)
- Top campaigns ranked by any metric
- Flows, flow performance, and time-series flow data
- Abandoned cart flow performance — revenue recovered and conversion rate
- Email and SMS metric summaries
- Conversion metrics — conversions, revenue, conversion rate
- Lists, list growth, and current size
- Segments and segment performance
- Profile counts and profile growth over time
- Subscription health — active, unsubscribed, bounced, suppressed
- Predictive analytics — CLV, churn risk, purchase probability
- Forms and form performance, including top-performing forms
- Raw metrics catalog, custom metric aggregates, and recent events

CorpusIQ never sends campaigns, edits flows, or modifies profiles.

## Questions you can ask
- "How much revenue did my Klaviyo flows generate last month?"
- "Which campaigns had the highest revenue per recipient?"
- "How's my abandoned cart flow performing?"
- "How fast is my email list growing?"
- "Compare email-driven revenue to my paid ad revenue by day."

## Troubleshooting
- **"403 Forbidden"** — Your private key is missing scopes. Recreate it and tick every read scope listed above.
- **No campaigns returned** — Klaviyo separates email and SMS channels. If you only run SMS, switch the channel filter when asking.
- **Predictive analytics empty** — Predictive CLV needs a minimum order history. New accounts may not have it populated for weeks.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
