# Multi-source prompts — the moat

These prompts fire across **three or more connectors at once**. They're what
no single SaaS tool can give you, and they're the reason CorpusIQ exists.
The skills engine handles the orchestration — you just ask the question.

---

### "What's my true CAC and ROAS by channel?"

**Connectors used:** Google Ads, Meta Ads, TikTok, GA4, Shopify, QuickBooks.
**Behind the scenes:** `ad-spend-truth-report` skill.
**What this does:** The only attribution view that matters — joins every
ad platform's spend to actual revenue from Shopify/QuickBooks via GA4
sessions. Cuts through each platform's self-reported ROAS, which is
always optimistic.
**Sample answer shape:** Per-channel matrix: spend, attributed revenue,
conversions, CAC, ROAS, payback days, and a verdict.

---

### "Draft a board update for last quarter."

**Connectors used:** QuickBooks, Shopify, HubSpot, GA4, Drive.
**Behind the scenes:** `board-update-drafter`.
**Sample answer shape:** Investor-update format — financials, KPIs,
wins, risks, asks — populated with your actuals and matched to the tone
of prior updates if found in Drive.

---

### "Prepare me for a board meeting next week."

**Connectors used:** QuickBooks, Shopify, HubSpot, ad accounts, GA4.
**Behind the scenes:** `board-meeting-prep`.
**Sample answer shape:** The update + an appendix of anticipated tough
questions with backing data.

---

### "How healthy is my business right now?"

**Connectors used:** QuickBooks, Shopify, HubSpot, ad accounts, GA4,
Email, Calendar.
**Behind the scenes:** `executive-snapshot`.
**Sample answer shape:** Multi-section snapshot — cash, revenue, wins,
risks, focus list.

---

### "Run a full financial health check."

**Connectors used:** QuickBooks, Shopify, Email, Drive.
**Behind the scenes:** `financial-command-center`.
**Sample answer shape:** Cash, concentration risk, expense anomalies,
late-payment patterns, forecasts.

---

### "Run a full ecommerce business review."

**Connectors used:** Shopify, Google Ads, Meta Ads, TikTok, GA4,
QuickBooks.
**Behind the scenes:** `ecommerce-command-center`.
**Sample answer shape:** Cash, ads, inventory, LTV, CAC, refunds — the
whole store, one report.

---

### "Run a full email marketing review."

**Connectors used:** Klaviyo, ActiveCampaign, Mailchimp, GA4, Shopify.
**Behind the scenes:** `email-lifecycle-intel`.
**Sample answer shape:** Cross-tool email perf, list health, flow
revenue, attribution to ecommerce revenue.

---

### "How does email-driven revenue compare to my paid ads?"

**Connectors used:** Klaviyo, Google Ads, Meta Ads, Shopify, GA4.
**Behind the scenes:** `cross_source_email` correlation
(`correlate_email_vs_social_ads`,
`correlate_email_revenue_vs_ecommerce`).
**Sample answer shape:** Per-day comparison of email-attributed revenue
vs paid-attributed revenue.

---

### "Give me a unified channel attribution summary."

**Connectors used:** Klaviyo, Shopify, GA4, Meta Ads.
**Behind the scenes:** `get_channel_attribution_summary` cross-source
tool.
**Sample answer shape:** Per-channel revenue contribution rolled up
across email, SMS, paid, and organic.

---

### "Pull together everything I need to know about [customer name]."

**Connectors used:** HubSpot, Email, Calendar, QuickBooks, Shopify (if
they're also a buyer), Drive (for past proposals).
**Behind the scenes:** `sales-call-prep-brief`.
**Sample answer shape:** Account 360 — relationship history, deal
state, billing status, open items, suggested next move.

---

### "Score my customer portfolio by health."

**Connectors used:** HubSpot, QuickBooks, GA4 or product analytics,
Email.
**Behind the scenes:** `customer-health-scorecard`.
**Sample answer shape:** Every active account scored Healthy / At Risk /
Critical with the driving signal per account.

---

### "Reconcile my numbers — why don't Shopify revenue and QuickBooks
revenue match?"

**Connectors used:** Shopify, QuickBooks, ad accounts (sometimes).
**Behind the scenes:** `data-discrepancy-detector` skill.
**Sample answer shape:** Side-by-side metric comparison with the gaps
explained (refunds, fees, sync lag, etc.).


---
*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
