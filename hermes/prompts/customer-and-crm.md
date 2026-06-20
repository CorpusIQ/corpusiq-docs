# Customer and CRM prompts

For **HubSpot** and **LeadConnector** (GoHighLevel) pipelines. Add **Email**
and **Calendar** to get engagement context, **QuickBooks** to tie deals to
invoiced revenue.

---

### "How healthy is my sales pipeline?"

**What this does:** Pipeline review — deal velocity, stalled
opportunities, contact engagement gaps, forecast accuracy.
**Connectors used:** HubSpot or LeadConnector, Email, Calendar,
QuickBooks, Shopify.
**Behind the scenes:** `crm-pipeline-health` skill.
**Sample answer shape:** Stage-by-stage pipeline health with stalled-deal
list and forecast confidence note.

---

### "Which deals are stuck?"

**What this does:** Ranks open deals by days-since-last-activity. Surfaces
ones with no email/calendar touch.
**Connectors used:** HubSpot, Email, Calendar.
**Behind the scenes:** `crm-pipeline-health`.
**Sample answer shape:** Deal list with amount, stage, days idle, last
contact.

---

### "Score every customer by health."

**What this does:** Account-by-account health scoring — usage, billing,
engagement, support signals. Identifies healthy / at-risk / critical.
**Connectors used:** HubSpot, GA4 (or PostHog), Email, QuickBooks.
**Behind the scenes:** `customer-health-scorecard` skill.
**Sample answer shape:** Ranked list with health score, top driver,
and recommended action per account.

---

### "Which customers are about to churn?"

**What this does:** Surfaces at-risk accounts before cancellation —
declining engagement, failed payments, support escalations.
**Connectors used:** HubSpot, Email, QuickBooks, Klaviyo (if available).
**Behind the scenes:** `churn-prevention` skill.
**Sample answer shape:** At-risk account list with risk signals and a
suggested save play.

---

### "Find the contact record for Jane at Acme."

**What this does:** Searches your CRM for a person.
**Connectors used:** HubSpot or LeadConnector.
**Behind the scenes:** `search_hubspot_contacts` or
`search_leadconnector_contacts`.
**Sample answer shape:** Matching contacts with email, phone, company,
and last-activity.

---

### "Prep me for my call with Acme."

**What this does:** Pulls everything CorpusIQ has on a specific account
— CRM deal, recent emails, past meetings, invoice/payment history,
support threads.
**Connectors used:** HubSpot, Email, Calendar, QuickBooks.
**Behind the scenes:** `sales-call-prep-brief` skill.
**Sample answer shape:** A pre-call brief — relationship state, open
items, last touchpoint, suggested talking points.

---

### "Prepare a QBR deck for [customer name]."

**What this does:** Builds a quarterly business review brief — usage
metrics, wins, open issues, expansion angles.
**Connectors used:** HubSpot, GA4 or PostHog, Email.
**Behind the scenes:** `qbr-prep-assembler` skill.
**Sample answer shape:** Structured QBR sections populated from the
account's actuals.

---

### "How are bookings going? What's the meeting-to-close rate?"

**What this does:** Analyzes the booked-meeting funnel — bookings,
no-shows, demos completed, demo-to-deal rate.
**Connectors used:** Calendly, HubSpot, Calendar.
**Behind the scenes:** `meeting-funnel-analyst` skill.
**Sample answer shape:** Funnel from booked → showed → converted with
conversion rate per stage.

---

### "List my most engaged customer contacts this month."

**What this does:** Cross-references CRM with email and calendar
activity.
**Connectors used:** HubSpot, Email, Calendar.
**Behind the scenes:** Pipeline + engagement join.
**Sample answer shape:** Contact list ranked by touchpoint count.

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
