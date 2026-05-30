# Recipe: Weekly Ad ROI Report

**Connectors:** google-ads, meta-ads, ga4
**Category:** reporting
**Complexity:** multi-source

---

## Use Case

Every Monday morning, marketing and growth operators need a single view of last
week's advertising performance across paid channels. This recipe pulls spend and
conversion data from Google Ads and Meta Ads, then joins it with GA4 session
and revenue data to compute true blended ROI per channel. It answers:
"Where did we actually make money last week, and where did we burn it?"

---

## Prerequisites

- CorpusIQ connectors connected: google-ads, meta-ads, ga4
- Required scopes:
  - Google Ads: read access to campaigns, ad_groups, metrics
  - Meta Ads: ads_read, business_management
  - GA4: readonly
- Frequency: weekly (run Monday for the prior Mon–Sun window)

---

## Query

```
Pull last week's ad performance across all channels. For each channel (Google Ads
and Meta Ads), give me: total spend, impressions, clicks, conversions, and
cost-per-conversion. Then pull GA4 revenue attributed to paid traffic sources
for the same 7-day window. Calculate ROAS (revenue / spend) per channel.
Show me a ranked summary, highest ROAS first, with a total blended row at the bottom.

Date range: last 7 complete days (Mon through Sun).
```

---

## Sample Output

```
Weekly Ad ROI Report — May 19–25, 2025

Channel        Spend      Revenue    ROAS    Clicks   Conv.   CPC
---------------------------------------------------------------------------
Google Ads     $4,210     $18,945    4.50x   3,812    142     $1.10
Meta Ads       $3,890     $11,280    2.90x   5,104    98      $0.76
---------------------------------------------------------------------------
BLENDED        $8,100     $30,225    3.73x   8,916    240     $0.91

Notes:
- GA4 revenue uses last-click attribution
- Meta conversions from pixel events: Purchase
- Google conversions from: Checkout Complete goal
```

---

## Notes

- GA4 revenue attribution uses last-click by default. If you use data-driven
  attribution in GA4, note that numbers will differ from channel-reported conversions.
- Meta Ads reports conversions on a 7-day click / 1-day view window by default.
  Align your attribution window across connectors before comparing.
- If GA4 shows no paid traffic, verify UTM parameters are applied to all ad URLs.
- Time zones: ensure all three connectors are set to the same account timezone
  in CorpusIQ settings, or specify timezone explicitly in the query.

---

## Variations

- **By campaign:** Add "break down by campaign name" to get per-campaign ROAS
- **By device:** Add "split by device type" for mobile vs desktop breakdown
- **Month-to-date:** Change date range to "current month to date" for MTD pacing
- **Budget pacing:** Add "compare spend to monthly budget" if budgets are set in connectors
