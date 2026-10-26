---
title: "Numbers Look Stale - CorpusIQ Docs"
description: "The answer is not empty, it is old. Why a connected source can return numbers that lag behind what the vendor shows, and how to read the delay correctly."
last_updated: "2026-10-19"
---
# The number is there, but it is older than you expected

This is different from an empty answer. The connector works, data comes
back, and nothing errors. The problem is the value: you know you closed
three deals this morning and the answer says two.

Almost every case is one of the five below.

## Cause 1: The source itself lags

CorpusIQ does not hold a copy of your business data. Each question is
resolved against the vendor at the moment you ask, so the age of the
number is the age of the vendor's own reporting.

Reporting software is rarely live. Advertising platforms settle
conversions for hours. Analytics platforms finalize a day after it ends.
Payment data posts as it happens.

| Source | Typical lag | What that means for you |
|--------|-------------|-------------------------|
| Shopify, Stripe, HubSpot, Klaviyo | Seconds to a couple of minutes | Safe to ask about today |
| QuickBooks | A few minutes | Safe to ask about today |
| Google Ads | Three to six hours | Yesterday's spend is reliable by morning |
| Meta Ads | Six to twelve hours | Conversions settle late, sometimes the next day |
| GA4 | One to two days | "Today" in GA4 usually means yesterday |
| Search Console | Weekly refresh | Treat it as a trend, not a live count |

If the number you expected falls inside one of those windows, the
answer is correct for the data that exists.

## Cause 2: You are comparing two sources with different clocks

The most common version of this: ads report a sale, the store reports
the sale, the two do not match. They never will at the same timestamp,
because the platforms attribute at different speeds and on different
calendars.

Ask for the comparison over a range that has had time to settle. Last
week reconciles. The last hour does not.

## Cause 3: You asked a question that closes the period too early

"Revenue today" asked at 9am is a partial day. "Spend this month" on
the 3rd is three days. Neither is stale, both are incomplete.

Phrase the window the way you would report it: "last full week", "the
month of September", "yesterday compared with the same day last week".

## Cause 4: The connector authenticated a different account than the one you are looking at

The status is green, the data is real, but it belongs to another
property, store, or ad account. The tell is a value that is stable but
wrong by a consistent factor, or a total that matches a secondary
account.

Disconnect, reconnect, and read the account name on the vendor consent
screen before approving. Use a browser session where only the intended
account is signed in.

## Cause 5: The metric definition is not the one you have in mind

"Revenue" is not one number. Gross versus net of refunds and tax.
Including shipping or not. Attributed revenue versus collected revenue.
Two dashboards can both be right and disagree.

If a number has been argued about before, write the definition down
once with Metric Specs and every later answer resolves the same way.
See [Metric Specs](../how-it-works/metric-specs.md).

## How to confirm in one step

Ask the same question through the vendor's own interface, restricted to
the same date range. If the two match, the data is current and the
expectation was off. If they differ, note the source, the question, the
range, and both values, and send that to support.

## FAQ

### Why does CorpusIQ not cache results to make answers faster?

Because a cached answer is a stale answer with no warning attached.
Every question is resolved against the source at the moment you ask, so
two questions thirty seconds apart both read live data. The trade is
latency for accuracy, and accuracy is the point.

### Is yesterday's data complete?

For most commerce and CRM sources, yes. For advertising and analytics
sources, usually, but the settlement window can run into the following
day. Check the same figure once more the next morning before you make a
decision on it.

### Why do two sources disagree on the same sale?

Attribution. The ad platform credits the click, the store credits the
order, and each counts at its own speed on its own calendar. Use one
source as the record of truth per metric rather than averaging them.

### Can I get a warning when a source is behind?

Ask the AI to show the most recent timestamp the source returned for
that entity. That gives you the data's own clock instead of your
assumption about it.

## Related

- [Connector shows no data](connector-shows-no-data.md) - when the answer
  is empty rather than old.
- [Rate limits and quotas](../how-it-works/rate-limits-and-quotas.md) -
  the full per-connector latency and limit tables.
- [Error codes reference](error-codes-reference.md) - when something
  actually failed.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
