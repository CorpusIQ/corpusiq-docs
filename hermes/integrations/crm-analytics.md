---
title: CRM + Analytics Integration for Hermes Agent — Lead Scoring & Pipeline Forecasting
description: Connect CRM (HubSpot, Salesforce, Close) with analytics (GA4, PostHog) in Hermes Agent. Automated lead scoring, pipeline forecasting, marketing attribution with MCP server setup and cron-driven reporting patterns.
category: integrations
tags: [hermes-agent, integration, crm, analytics, hubspot, ga4, lead-scoring, pipeline-forecasting, attribution]
last_updated: 2026-06-16
---

# CRM + Analytics Integration — Lead Scoring & Pipeline Forecasting

## Architecture Overview

```
┌──────────┐     ┌──────────────┐     ┌───────────┐
│   CRM    │────▶│  Enrichment  │────▶│ Analytics │
│  (Deals, │     │   + Scoring  │     │ (Traffic, │
│  Contacts│     │              │     │  Events)  │
└──────────┘     └──────┬───────┘     └───────────┘
                        │
                  ┌─────▼──────┐
                  │  Hermes    │
                  │  Agent     │
                  └────────────┘
```

CRM provides the "who" (contacts, deals, pipeline stages). Analytics provides the "what" (behavior, engagement, conversion signals). The enrichment layer merges these into actionable intelligence.

## MCP Server Setup

### CRM Servers

**HubSpot MCP Server** — provides `list_hubspot_contacts`, `list_hubspot_deals`, `search_hubspot_contacts`, and company data. Configure with HubSpot private app token. Scopes needed: `crm.objects.contacts.read`, `crm.objects.deals.read`, `crm.objects.companies.read`.

**Close CRM MCP Server** — provides `close_list_leads`, `close_list_opportunities`, `close_list_activities`, and `close_search`. OAuth-based authentication. Ideal for sales-heavy organizations with activity tracking needs.

**LeadConnector MCP Server** — provides contact, opportunity, appointment, and conversation data. Suitable for agencies and service businesses using GoHighLevel.

### Analytics Servers

**GA4 MCP Server** — provides `run_report` with dimensions and metrics, `get_realtime` for live traffic. Configure with Google Analytics Data API scope. Use property IDs from your GA4 account.

**PostHog MCP Server** — provides `list_events`, `run_query` (HogQL), and `get_funnel` for product analytics. Personal API key authentication. Excellent for SaaS businesses tracking in-product behavior.

## Core Automation Scenarios

### 1. Lead Scoring Automation

**Goal:** Automatically score leads based on behavioral signals from analytics and firmographic data from CRM.

**Scoring Model:**
```
Score = (Page View Weight × Pages Visited) 
      + (Demo Request: +25)
      + (Pricing Page: +15)
      + (Case Study Download: +10)
      + (Email Open: +2 each)
      + (Company Size Bonus: Enterprise +10, Mid-Market +5)
      - (Bounce after 1 page: -5)
      - (No activity in 30 days: decay by 50%)
```

**Workflow:**
1. Daily: pull all contacts from CRM that aren't yet scored or need re-scoring
2. For each contact, query analytics for their behavioral events (page views, conversions, signups)
3. Compute the composite score using the weighted model above
4. Update CRM contact with score and score breakdown (what contributed)
5. Trigger alerts for contacts crossing threshold values (e.g., score > 70 → notify sales)

**Cron expression:** `0 2 * * *` — runs overnight when API load is lower.

### 2. Pipeline Forecasting

**Goal:** Generate forward-looking revenue forecasts by combining CRM pipeline data with historical conversion analytics.

**Workflow:**
1. Pull all open deals from CRM with: deal stage, amount, age-in-stage, owner, close date
2. Retrieve historical stage-conversion rates from analytics (what % of deals move from Stage A → Stage B)
3. Compute weighted pipeline value:
   ```
   Weighted Value = Sum(deal_amount × stage_probability) 
                    × velocity_adjustment(age_in_stage / avg_stage_duration)
   ```
4. Apply cohort adjustments: deals from [SOURCE A] convert 20% faster than [SOURCE B]
5. Generate forecast report with: best case, expected case (weighted), and worst case projections
6. Flag deals stuck in stage beyond 2× average duration — these need intervention

**Cron expression:** `0 6 * * 1` — weekly Monday morning forecast report.

### 3. Attribution Tracking

**Goal:** Connect marketing touchpoints (from analytics) to closed revenue (from CRM) for channel ROI.

**Workflow:**
1. Weekly: pull all deals closed in the last 7 days from CRM
2. For each closed deal, trace the contact's analytics journey:
   - First touch: which channel brought them initially
   - Last touch: which channel drove the conversion
   - Multi-touch: every touchpoint in between
3. Attribute revenue using configurable model (first-touch, last-touch, linear, time-decay)
4. Generate per-channel report:
   - Channel | Spend | Pipeline Generated | Closed Revenue | ROAS | CAC
5. Flag channels where ROAS is below target threshold

**Configurable attribution model:**
```yaml
attribution:
  model: "time_decay"  # or first_touch, last_touch, linear, u_shaped
  lookback_window_days: 90
  channels:
    - organic_search
    - paid_search
    - social_organic
    - social_paid
    - email
    - direct
    - referral
```

### 4. Churn Risk Detection

**Goal:** Identify accounts at risk of churning by combining CRM health signals with analytics engagement data.

**Workflow:**
1. Pull all active accounts/customers from CRM
2. For each, query analytics for engagement signals over the last 30 days:
   - Login frequency trend (declining?)
   - Feature usage breadth (narrowing?)
   - Support ticket volume (increasing?)
   - NPS or CSAT scores (dropping?)
3. Compute churn risk score using a weighted model
4. Categorize accounts: Healthy, At-Risk, Critical
5. For At-Risk and Critical accounts:
   - Create CRM task for account manager
   - Generate a health summary: what degraded, by how much, when it started
   - Suggest intervention: specific features to re-engage them on, unused capabilities

**Cron expression:** `0 7 * * 1,3,5` — runs Monday, Wednesday, Friday mornings.

## Cron Schedule Summary

| Task | Cron | Frequency |
|---|---|---|
| Lead scoring update | `0 2 * * *` | Daily, overnight |
| Pipeline forecast | `0 6 * * 1` | Weekly, Monday AM |
| Attribution report | `0 7 * * 1` | Weekly, Monday AM |
| Churn risk detection | `0 7 * * 1,3,5` | Mon/Wed/Fri AM |
| Data quality check | `0 3 * * 0` | Weekly, Sunday |

## Implementation Notes

### Data Quality First
CRM and analytics data drift apart. Start every automation with a data quality check:
- Do contact emails in CRM match identifiers in analytics? If not, cross-referencing breaks.
- Are deal stages consistently named and used? Normalize stage names before forecasting.
- Is analytics tracking comprehensive? Missing events create blind spots in scoring.

### Privacy Considerations
- Respect data residency requirements — don't merge EU CRM data with US analytics processing unless compliant.
- Honor unsubscribe and do-not-track signals from both systems.
- Log attribution data separately from PII — keep the pipeline analysis database isolated.

### Gradual Rollout
Start with non-critical reports (attribution, pipeline visibility). After 4 weeks of validated data, move to action-triggering automations (lead scoring alerts, churn tasks). This builds trust in the merged data before it drives decisions.

### Extending
- Add email marketing (Klaviyo, Mailchimp) to the attribution model for email-driven pipeline tracking.
- Connect Slack for real-time scoring alerts when high-value leads are detected.
- Wire in calendar data to track meeting-to-opportunity conversion rates.


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*
