# Email and SMS marketing prompts

For Klaviyo, Mailchimp, Constant Contact, ActiveCampaign, and PostScript.
Klaviyo gets the most coverage because it has by far the richest API.

---

### "Which email campaign drove the most revenue last month?"

**What this does:** Ranks Klaviyo campaigns by attributed revenue.
**Connectors used:** Klaviyo.
**Behind the scenes:** `get_klaviyo_top_campaigns` with metric=revenue.
**Sample answer shape:** Top campaigns with sends, opens, clicks,
conversions, and revenue.

---

### "How healthy is my email program overall?"

**What this does:** Full email lifecycle analysis — performance,
list health, deliverability, flow revenue, attribution.
**Connectors used:** Klaviyo (primary), ActiveCampaign, Mailchimp, GA4
or Shopify for attribution.
**Behind the scenes:** `email-lifecycle-intel` skill.
**Sample answer shape:** Multi-section brief covering campaign perf,
flow perf, list health, deliverability concerns, and revenue
attribution.

---

### "How's my abandoned cart flow performing?"

**What this does:** Klaviyo abandoned cart flow — revenue recovered,
conversion rate, message-by-message breakdown.
**Connectors used:** Klaviyo.
**Behind the scenes:** `get_klaviyo_abandoned_cart_flows`.
**Sample answer shape:** Flow message breakdown with sends, opens,
clicks, conversions, attributed revenue.

---

### "Is my list growing or decaying?"

**What this does:** Subscriber growth, profile counts, subscription
health (active vs unsubscribed vs bounced vs suppressed).
**Connectors used:** Klaviyo.
**Behind the scenes:** `get_klaviyo_profile_growth` +
`get_klaviyo_subscription_health`.
**Sample answer shape:** Growth curve described in text plus health
breakdown.

---

### "Which Klaviyo segments are highest-value?"

**What this does:** Lists segments with size and performance signal.
**Connectors used:** Klaviyo.
**Behind the scenes:** `get_klaviyo_segments` +
`get_klaviyo_segment_performance` on top entries.
**Sample answer shape:** Segment list with size and engagement metric.

---

### "Who's at risk of churning based on predictive analytics?"

**What this does:** Surfaces Klaviyo's predicted CLV / churn-risk /
purchase-probability distribution.
**Connectors used:** Klaviyo.
**Behind the scenes:** `get_klaviyo_predictive_analytics`.
**Sample answer shape:** Distribution buckets with profile counts.

---

### "What's the recent SMS performance?"

**What this does:** Klaviyo SMS summary — recipients, deliveries, clicks,
revenue.
**Connectors used:** Klaviyo.
**Behind the scenes:** `get_klaviyo_sms_metrics_summary`.
**Sample answer shape:** Topline SMS metrics for the window.

---

### "Which Mailchimp campaigns had the best open rate?"

**What this does:** Ranks recent Mailchimp campaigns by open rate.
**Connectors used:** Mailchimp.
**Behind the scenes:** `get_mailchimp_campaigns` +
`get_mailchimp_campaign_report`.
**Sample answer shape:** Campaign list with open and click rates.

---

### "How many PostScript SMS subscribers do I have, and how fast is the
list growing?"

**What this does:** PostScript subscriber count and trend.
**Connectors used:** PostScript.
**Behind the scenes:** `get_postscript_subscribers` with date filters.
**Sample answer shape:** Total subscribers and new-subscriber trend.

---

### "Which signup forms are converting?"

**What this does:** Top-performing Klaviyo signup forms by submission
rate.
**Connectors used:** Klaviyo.
**Behind the scenes:** `get_klaviyo_top_performing_forms`.
**Sample answer shape:** Form list with views, submits, and submit rate.
