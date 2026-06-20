# Marketing and ROAS prompts

The hard questions: is your ad spend working, what's your true CAC, where
should the next dollar go. Powered by **Google Ads + Meta Ads + GA4 +
QuickBooks/Shopify** cross-source analysis.

---

### "What's my true CAC and ROAS by channel?"

**What this does:** Combines ad spend (Google Ads, Meta, TikTok) with
revenue (Shopify, QuickBooks) and traffic (GA4) to calculate **blended
ROAS**, **MER**, **CAC**, and **payback window per channel**. This is
the report your agency probably doesn't give you straight.
**Connectors used:** Google Ads, Meta Ads, TikTok (if running), Shopify,
GA4.
**Behind the scenes:** `ad-spend-truth-report` skill.
**Sample answer shape:** A per-channel breakdown with spend,
attributed revenue, conversions, CAC, ROAS, and a verdict per channel.

---

### "Are my ads actually working?"

**What this does:** Same engine as above, framed as a yes/no answer with
the evidence.
**Connectors used:** Google Ads, Meta Ads, Shopify, GA4.
**Behind the scenes:** `ad-spend-truth-report`.
**Sample answer shape:** Verdict per channel with the metrics that drove
it.

---

### "Compare Google Ads spend to GA4 sessions and revenue."

**What this does:** Cross-source correlation — does spend translate to
traffic, and traffic to revenue, on a day-by-day basis?
**Connectors used:** Google Ads, GA4.
**Behind the scenes:** `correlate_ads_spend_vs_ga4_revenue` and
`correlate_ads_spend_vs_ga4_sessions` cross-source tools.
**Sample answer shape:** Daily spend vs sessions vs revenue, with a
ROAS line at the bottom.

---

### "Which Google Ads campaigns are wasting money?"

**What this does:** Ranks campaigns by spend efficiency. CorpusIQ does
not invent a "waste" threshold — it surfaces high-spend / low-conversion
campaigns so you can judge.
**Connectors used:** Google Ads.
**Behind the scenes:** `list_google_ads_campaigns` +
`get_google_ads_campaign_performance`.
**Sample answer shape:** Campaign table sorted by spend with conversions,
CTR, CPC, and conversion rate.

---

### "What search terms are people actually using to find my ads?"

**What this does:** Pulls the Google Ads search terms report — the queries
your keywords matched on. Reveals negative-keyword opportunities.
**Connectors used:** Google Ads.
**Behind the scenes:** `get_google_ads_search_terms`.
**Sample answer shape:** Top search terms with impressions, clicks, cost,
and conversions.

---

### "Show me my Meta Ads performance for the last 30 days."

**What this does:** Account-level Meta (Facebook + Instagram) summary —
spend, impressions, reach, frequency, CPM, CPC, conversions.
**Connectors used:** Meta Ads.
**Behind the scenes:** `get_facebook_account_insights`.
**Sample answer shape:** Headline metrics table for the window.

---

### "Which Meta campaigns drove the most ROAS?"

**What this does:** Per-campaign breakdown ranked by return.
**Connectors used:** Meta Ads.
**Behind the scenes:** `list_facebook_campaigns` +
`get_facebook_campaign_insights`.
**Sample answer shape:** Campaign list sorted by ROAS.

---

### "Which demographics are converting on my ads?"

**What this does:** Age/gender breakdown for Meta and Google Ads.
**Connectors used:** Meta Ads, Google Ads.
**Behind the scenes:** `get_facebook_age_gender_insights` +
`get_google_ads_age_gender_performance`.
**Sample answer shape:** Age-gender grid with spend and conversions.

---

### "How's my TikTok content performing?"

**What this does:** TikTok organic — followers, top videos, total views
and engagement.
**Connectors used:** TikTok.
**Behind the scenes:** `get_tiktok_account_analytics`,
`get_tiktok_video_analytics`.
**Sample answer shape:** Account totals and a top-10 video list.

---

### "Where's my best traffic coming from?"

**What this does:** GA4 acquisition report — channels, sources, mediums
sorted by sessions and conversions.
**Connectors used:** GA4.
**Behind the scenes:** `run_ga4_report`.
**Sample answer shape:** Source/medium table with sessions, users,
engagement, conversions.

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
