---
title: "SEO Performance Report (GA4 + Search Console)"
description: "Weekly SEO reporting across every site you run: biggest click movers, query opportunities, and GA4 landing-page checks in one cited answer."
---
# Recipe: SEO Performance Report (GA4 + Search Console)

**Connectors:** Google Workspace (Search Console + GA4)
**Category:** reporting
**Complexity:** simple

---

## Use Case

You run one or more websites and report on organic search. Once a week (or month), you want the same three answers without opening two Google tools and a spreadsheet: which pages gained or lost clicks, which queries are moving those pages, and whether the clicks that changed actually show up as sessions in GA4. This recipe turns that loop into one prompt run from your AI client of choice (ChatGPT, Claude, Claude Code, or any MCP client).

---

## Prerequisites

- CorpusIQ connected with the **Google Workspace** connector (one connection covers Search Console AND GA4)
- Search Console property accessible with your Google account (domain properties like `sc-domain:example.com` and URL-prefix properties both work)
- GA4 property ID (find it in GA4 under Admin, Property settings; it looks like `properties/123456789`)
- Frequency: weekly or monthly, on-demand

---

## Query

```
Compare Search Console performance for sc-domain:example.com, last 28 days
vs the previous 28 days. Give me:

1. The 10 pages with the biggest click increase and the 10 with the biggest click drop.
2. For the top 5 movers, the queries driving the change.
3. Then from GA4 (properties/123456789), sessions and engaged sessions for those
   same landing pages in the same window, so I can see which movement reached the site.
```

---

## Sample Output

```
Search Console - sc-domain:example.com - Sep 5 to Oct 2 vs Aug 8 to Sep 4

Top gainers (clicks)
  /guides/pricing-benchmarks   +412  (+61%)   queries: "saas pricing benchmark", "pricing page teardown"
  /blog/churn-metrics          +198  (+44%)   queries: "churn rate benchmark"
  ...

Top drops (clicks)
  /features/integrations       -287  (-38%)   queries: "hubspot integration" (position 6 -> 11)
  /pricing                     -96   (-12%)   queries: "crm pricing" (CTR 4.1% -> 2.6%)
  ...

GA4 (properties/123456789) - same landing pages, same window
  /guides/pricing-benchmarks   sessions +38%  engaged sessions +41%
  /features/integrations       sessions -22%  (matches the drop)
  ...
```

Every number is returned with its source (Search Console property or GA4 property) so you can verify before acting.

---

## Notes

- Search Console data lags 2 to 3 days; end your window 3 days before today for stable comparisons.
- Use full 28-day windows on both sides of the comparison; shorter windows swing hard on low-traffic sites.
- Domain properties must be passed as `sc-domain:example.com`. URL-prefix properties use the full `https://...` URL.
- GA4 and Search Console count differently (clicks vs sessions, different attribution). Expect them to disagree slightly; the recipe is about direction and magnitude, not exact parity.
- Everything is read-only. No writes touch your Google account.

---

## Variations

- **CTR opportunity hunt:** same connector, ask for queries with 500+ impressions, average position 4 to 12, and CTR under 2% - your fastest title/meta wins.
- **Content decay check:** pages that lost 30%+ clicks quarter over quarter, sorted by previous clicks.
- **New query discovery:** queries that appeared for the first time in the last 14 days with 50+ impressions.
- **Multi-site rollup:** run the same prompt per property and ask for a combined table comparing all sites.

## FAQ

### Why do Search Console clicks and GA4 sessions disagree?

They count different things. Search Console counts search-result clicks per query and page; GA4 counts sessions with its own attribution and filtering. Expect differences of 10 to 30 percent. Use Search Console for demand and queries, GA4 for on-site behavior, and never force the two into exact parity.

### How fresh is the data?

Search Console lags 2 to 3 days. GA4 is near real time but some reports settle for 24 to 48 hours. End your comparison windows at least 3 days back from today for stable numbers.

### Does this work for multiple properties?

Yes. Search Console works with domain properties (`sc-domain:example.com`) and URL-prefix properties, and each GA4 property is addressed by its `properties/123456789` ID. Run the recipe per property and ask for a combined rollup table.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
