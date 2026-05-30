# Recipe: HubSpot Deal Pipeline Correlated with Klaviyo Email Engagement

**Connectors:** hubspot, klaviyo
**Category:** pipeline
**Complexity:** multi-source

---

## Use Case

Revenue and marketing teams need to understand whether email engagement drives
or follows deal progression. This recipe correlates HubSpot deal stage movement
with Klaviyo email opens, clicks, and conversions for the same contacts over
a rolling 30-day window. It surfaces which deals have gone cold (no email
engagement), which contacts are actively engaging but haven't advanced in the
pipeline, and which email flows are generating the most deal movement.

---

## Prerequisites

- CorpusIQ connectors connected: hubspot, klaviyo
- Required scopes:
  - HubSpot: crm.objects.deals.read, crm.objects.contacts.read
  - Klaviyo: read-only (profiles, metrics, campaigns, flows)
- Frequency: weekly or on-demand
- Contacts must share email address between HubSpot and Klaviyo for matching

---

## Query

```
Correlate HubSpot deal pipeline with Klaviyo email engagement over the last 30 days.

From HubSpot: pull all open deals. For each deal give me: deal_id, deal_name,
deal_stage, amount, close_date, associated contact email(s), days in current stage.

From Klaviyo: for those same contact emails, pull email engagement over the last
30 days: total emails received, opens, clicks, and any conversion events
(placed_order or custom conversion metric if configured).

Join on contact email. For each deal show:
- Deal stage and amount
- Contact email engagement summary (opens, clicks, conversions)
- Days since last email open (if any)

Then give me three segments:
1. Hot — deal in late stage AND contact opened email in last 7 days
2. At Risk — deal has been in current stage 14+ days AND no email open in 14+ days
3. Engaged but stalled — contact has 3+ opens in last 14 days but deal hasn't advanced

Sort At Risk by deal amount descending.
```

---

## Sample Output

```
HubSpot × Klaviyo Pipeline Correlation — Apr 25 – May 25, 2025

HOT (8 deals)
Deal: Acme Corp Expansion — Stage: Proposal Sent — $42,000
  Contact: jane@acme.com — Opens: 6 | Clicks: 3 | Last open: 2 days ago

Deal: Beta Industries Q2 — Stage: Contract Review — $18,500
  Contact: ops@betaind.com — Opens: 4 | Clicks: 2 | Last open: 1 day ago

[... 6 more]

AT RISK (12 deals — $287,000 at risk)
Deal: Gamma Corp Platform — Stage: Demo Scheduled — $95,000 — 22 days in stage
  Contact: it@gammacorp.com — Opens: 0 | Last open: 31 days ago

Deal: Delta Retail Suite — Stage: Qualified — $61,000 — 18 days in stage
  Contact: buyer@deltaretail.com — Opens: 1 | Last open: 19 days ago

[... 10 more]

ENGAGED BUT STALLED (5 deals)
Deal: Epsilon Media — Stage: Qualified — $28,000 — 11 days in stage
  Contact: cmo@epsilonmedia.com — Opens: 9 | Clicks: 4 | Last open: 1 day ago
  → High engagement, deal not advancing. Consider direct outreach.

[... 4 more]
```

---

## Notes

- Matching is done by email address. Contacts must have the same email in both
  HubSpot and Klaviyo. Mismatches (e.g. work vs personal email) will cause
  contacts to appear with zero Klaviyo engagement even if they're active.
- Klaviyo "conversion" events depend on how your account defines conversions.
  By default CorpusIQ uses placed_order. If you use a custom conversion metric,
  specify it explicitly in the query.
- HubSpot deals with multiple associated contacts will show engagement for all
  associated emails. Specify "primary contact only" in the query if you want
  single-contact matching.
- "Days in stage" is calculated from the stage_timestamp on the deal record.
  Deals migrated from other CRMs may have inaccurate stage timestamps.

---

## Variations

- **By deal owner:** Add "group At Risk deals by HubSpot deal owner" to route
  follow-ups to the right rep
- **Flow breakdown:** Add "which Klaviyo flow or campaign generated each open"
  to see which sequences are working
- **Custom stages:** Replace stage names with your pipeline's actual stage names
  (e.g. "Discovery", "POC", "Legal Review")
- **Tighter window:** Change email engagement to 7-day window for higher-velocity sales cycles
