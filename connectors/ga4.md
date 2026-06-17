# GA4 — Google Analytics 4

Connect GA4 to CorpusIQ and ask plain-English questions about your website traffic, conversions, acquisition sources, and revenue — without leaving Claude or ChatGPT.

## What it unlocks

- **Traffic analysis** — sessions, users, pageviews by channel, device, country
- **Acquisition breakdown** — which channels drive the most engaged visitors
- **Conversion tracking** — goal completions, events, funnel performance
- **Revenue reporting** — ecommerce purchase revenue, ROAS from GA4's perspective
- **Real-time data** — active users right now, top pages in the last 30 minutes
- **Cross-source analysis** — GA4 traffic vs Google Ads spend vs Shopify revenue in one answer

## Example prompts

```
What were my top 5 traffic sources this week and which had the best conversion rate?
```

```
How many new users signed up in the last 7 days and where did they come from?
```

```
Compare organic vs paid traffic performance over the last 30 days.
```

```
What pages have the highest bounce rate this month?
```

```
Show me real-time active users right now broken down by device.
```

## How to connect

1. Go to **corpusiq.io** → Settings → Connectors
2. Click **Google Analytics 4**
3. Sign in with the Google account that has access to your GA4 property
4. Select the GA4 property you want to connect
5. Done — CorpusIQ is read-only and never modifies your Analytics data

## What data CorpusIQ can see

| Data | Available |
|------|-----------|
| Sessions, users, pageviews | ✅ |
| Traffic sources / channels | ✅ |
| Conversion events | ✅ |
| Ecommerce revenue | ✅ |
| Real-time active users | ✅ |
| Individual user PII | ❌ Never |
| Raw event stream | ❌ Aggregated only |

## Cross-source power queries

GA4 becomes most powerful when combined with other connectors:

```
My Google Ads spend was $12,000 this month. What revenue did GA4 attribute to paid search?
```

```
Which acquisition channel has the lowest CAC when I combine GA4 conversion data with my ad spend?
```

```
Did the email campaign I sent Tuesday cause a traffic spike? Compare Klaviyo send time to GA4 sessions.
```

---

*CorpusIQ is read-only. We never write to or modify your Google Analytics data.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
