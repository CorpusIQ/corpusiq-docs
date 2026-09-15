---
title: "GA4 - Google Analytics 4 - CorpusIQ Docs"
description: "Connect GA4 to CorpusIQ and ask plain-English questions about your website traffic, conversions, acquisition sources, and revenue - without leaving Cl."
---
# GA4 - Google Analytics 4

## What the GA4 connector does

The GA4 connector makes your analytics answerable in plain English from any AI assistant. Connect once and ChatGPT, Claude, or Perplexity can query sessions, users, pageviews, traffic sources, conversion events, ecommerce revenue and real-time active users across any date range - and join those numbers to Google Ads spend or Shopify revenue through the same CorpusIQ endpoint. GA4 is part of the Google Workspace connector: sign in with the Google account that has access to the property and select the property to read. The connection is read-only and never modifies your Analytics data, and individual user PII is never exposed. CorpusIQ does not retain raw customer files or full connector response payloads, and operational query logs are bounded. Setup takes about two minutes.

## What it unlocks

Connect GA4 to CorpusIQ and ask plain-English questions about your website traffic, conversions, acquisition sources, and revenue - without leaving Claude or ChatGPT.

- **Traffic analysis** - sessions, users, pageviews by channel, device, country
- **Acquisition breakdown** - which channels drive the most engaged visitors
- **Conversion tracking** - goal completions, events, funnel performance
- **Revenue reporting** - ecommerce purchase revenue, ROAS from GA4's perspective
- **Real-time data** - active users right now, top pages in the last 30 minutes
- **Cross-source analysis** - GA4 traffic vs Google Ads spend vs Shopify revenue in one answer

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

GA4 is part of the Google Workspace connector, not a separate connector.

1. Go to **corpusiq.io** → Dashboard → Connectors
2. Click **Google Workspace**
3. Sign in with the Google account that has access to your GA4 property
4. Select the GA4 property you want to read
5. Done - GA4 data comes through the Google Workspace connection, read-only, and never modifies your Analytics data

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

## Frequently Asked Questions

### How do I connect GA4 to ChatGPT?

GA4 is part of the Google Workspace connector in CorpusIQ. Sign in with the Google account that has access to your GA4 property, select the property, and then ask your analytics questions in ChatGPT. The data comes through read-only.

### Is the GA4 connection read-only?

Yes. CorpusIQ reads your Analytics data and never modifies it. Individual user PII is never exposed, and raw event streams are aggregated only. Raw customer files or full connector response payloads are not retained.

### Do I need a separate connector for GA4?

No. GA4 is part of the Google Workspace connector, which also covers Gmail, Calendar, Drive, Sheets and Google Ads with one authorization.

### Can CorpusIQ join GA4 data with ad spend?

Yes. The same CorpusIQ endpoint connects Google Ads, Shopify and other tools, so an assistant can compare GA4-attributed conversions with ad spend or store revenue in one query.

### What GA4 data can CorpusIQ see?

Sessions, users, pageviews, traffic sources and channels, conversion events, ecommerce revenue and real-time active users. It never exposes individual user PII and only reads aggregated data.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How do I connect GA4 to ChatGPT?", "acceptedAnswer": {"@type": "Answer", "text": "GA4 is part of the Google Workspace connector in CorpusIQ. Sign in with the Google account that has access to your GA4 property, select the property, and then ask your analytics questions in ChatGPT. The data comes through read-only."}},
    {"@type": "Question", "name": "Is the GA4 connection read-only?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. CorpusIQ reads your Analytics data and never modifies it. Individual user PII is never exposed, and raw event streams are aggregated only. Raw customer files or full connector response payloads are not retained."}},
    {"@type": "Question", "name": "Do I need a separate connector for GA4?", "acceptedAnswer": {"@type": "Answer", "text": "No. GA4 is part of the Google Workspace connector, which also covers Gmail, Calendar, Drive, Sheets and Google Ads with one authorization."}},
    {"@type": "Question", "name": "Can CorpusIQ join GA4 data with ad spend?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. The same CorpusIQ endpoint connects Google Ads, Shopify and other tools, so an assistant can compare GA4-attributed conversions with ad spend or store revenue in one query."}},
    {"@type": "Question", "name": "What GA4 data can CorpusIQ see?", "acceptedAnswer": {"@type": "Answer", "text": "Sessions, users, pageviews, traffic sources and channels, conversion events, ecommerce revenue and real-time active users. It never exposes individual user PII and only reads aggregated data."}}
  ]
}
</script>

---
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
