---
title: Customer Lifecycle Automation Blueprint — Onboarding to Win-Back with Hermes Agent
description: Multi-stage Hermes Agent customer lifecycle blueprint. Automate onboarding, engagement monitoring, churn detection, retention campaigns, and win-back. CRM, email marketing, and analytics orchestrated through cron-driven workflows.
category: blueprints
tags: [hermes-agent, blueprint, customer-lifecycle, onboarding, retention, churn-prevention, crm-automation]
last_updated: 2026-06-16
---

# Customer Lifecycle Automation Blueprint — Onboarding to Win-Back

## Lifecycle Stages

```
ONBOARDING → ENGAGEMENT → RETENTION → WIN-BACK
  (Days 0-30)  (Days 31-90)  (Day 91+)  (Churned)
```

Each stage has its own cron schedule, triggers, and automated actions. The pipeline is designed to move customers smoothly from acquisition to advocacy — and to detect and intervene when they drift toward churn.

## Architecture Overview

```
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │   CRM    │    │  Email   │    │ Analytics│    │  Tasks   │
  │ Contacts │    │Marketing │    │Behavioral│    │+ Calendar│
  └────┬─────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘
       │               │               │               │
       └───────────────┴───────┬───────┴───────────────┘
                               │
                     ┌─────────▼─────────┐
                     │ Lifecycle Engine  │
                     │ - Stage detection │
                     │ - Action triggers │
                     │ - Health scoring  │
                     └─────────┬─────────┘
                               │
                     ┌─────────▼─────────┐
                     │  Hermes Agent     │
                     │  - Cron scheduler │
                     │  - Multi-source   │
                     └───────────────────┘
```

## Stage 1: Onboarding (Days 0–30)

**Goal:** Get new customers to their first meaningful value milestone within 30 days.

### Triggers and Detection
- **New customer detection:** Monitor CRM for new contacts tagged "customer" or deals moved to "closed-won." Run every 4 hours.
- **Cron:** `0 */4 * * *` — checks for new customers to onboard.

### Automated Actions

**Welcome Sequence (Day 0):**
1. Add customer to onboarding email sequence in email marketing platform
2. Create CRM task for account manager: "Schedule onboarding call within 3 business days"
3. Post welcome notification to internal Slack channel `#new-customers`

**Day 3 Health Check:**
1. Check if customer has logged in (analytics) or completed key setup action
2. If no activity detected: escalate to account manager with a "hand-hold" alert
3. If active: send congratulatory email highlighting what they've accomplished

**Day 7 Milestone Review:**
1. Query analytics for: login count, features used, time spent, configuration completeness
2. Score onboarding health (0–100):
   ```
   health_score = (login_count × 5) 
                + (features_configured × 15) 
                + (has_invited_team ? 30 : 0)
                + (has_imported_data ? 25 : 0)
   ```
3. If score < 50: flag for intervention. Schedule additional training session.
4. If score >= 70: move to "onboarded" stage and trigger engagement workflow.

**Day 14 and Day 30 Check-Ins:**
1. Send automated check-in email: "How's it going? Here's what other customers achieved by now."
2. Surface most-used features and suggest under-utilized ones relevant to their use case
3. Schedule 30-day business review call for customers above a revenue threshold

### Onboarding Completion Criteria
A customer graduates from onboarding when:
- Health score >= 70
- At least one key workflow is operational
- At least [N] team members are active (for team products)

**Cron:** `0 8 * * *` — daily onboarding health sweep.

## Stage 2: Engagement (Days 31–90)

**Goal:** Deepen product usage, expand to more team members, and establish recurring value.

### Triggers and Detection
- Customers who graduated from onboarding (health score >= 70)
- Active daily or weekly users
- Customers showing feature expansion signals

**Cron:** `0 9 * * 1,3,5` — engagement pulse check on Monday, Wednesday, Friday.

### Automated Actions

**Feature Adoption Campaign:**
1. Weekly: identify the top 3 features used by the customer's industry peers but not by them
2. Queue a personalized email suggesting each feature with a use case relevant to their business
3. Track click-through on feature suggestion emails — clicks indicate interest worth following up on

**Usage Deepening Triggers:**
| Signal | Action |
|---|---|
| Usage plateaus for 2 weeks | Send "power user tips" email with advanced workflows |
| Single user for > 30 days | Suggest team invite feature; offer admin training |
| Integration not configured | Send integration setup guide with step-by-step instructions |
| Support ticket opened | Follow up 48 hours after resolution: "Still good?" |

**Advocacy Identification:**
Customers who meet these criteria are flagged as potential advocates:
- NPS score of 9 or 10
- Usage in top 25th percentile
- Have referred others or expressed willingness

When identified:
1. Add to "advocates" segment in CRM
2. Send case study invitation
3. Invite to beta program for new features
4. Create task for Customer Success to nurture the relationship

**Monthly Business Review Automation:**
1. First of each month: generate a one-page account health summary
2. Include: usage trends, feature adoption, support ticket history, upcoming renewals
3. Push to CRM as a note on the account
4. Draft quarterly business review presentation for accounts above threshold

**Cron:** `0 7 1 * *` — monthly account health reports.

## Stage 3: Retention (Day 91+)

**Goal:** Prevent churn by detecting early warning signals and intervening proactively.

### Triggers and Detection
All active customers beyond 90 days are in the retention stage. The focus shifts from growth to monitoring.

**Churn Risk Model:**
```
risk_score = (login_decline × 20)       # Login frequency dropped > 30%
           + (feature_shrink × 15)      # Features used decreased
           + (support_spike × 10)       # Support tickets up > 50%
           + (nps_drop × 20)            # NPS decreased by > 2 points
           + (no_advocate_behavior × 5) # No referral/advocacy signals
           + (contract_near_end × 15)   # Within 60 days of renewal
```

Risk categories:
- **0–30:** Healthy — standard engagement workflow
- **31–50:** At Risk — initiate retention playbook
- **51+:** Critical — executive escalation

**Cron:** `0 7 * * 1-5` — daily churn risk sweep.

### Retention Playbook

**At Risk (31–50):**
1. Notify account manager with risk score breakdown — which specific signals triggered the alert
2. Schedule a check-in call within 5 business days
3. Send curated content addressing the specific area of concern (e.g., if feature usage dropped, send training material for the dropped features)
4. Offer an extended trial of a premium feature relevant to their use case
5. Create a 14-day monitoring plan — if score doesn't improve, escalate

**Critical (51+):**
1. Immediate notification to account manager, their manager, and customer success leadership
2. Executive sponsor assigned if account is above revenue threshold
3. Generate a "save plan" with specific recommendations based on what degraded
4. Schedule emergency check-in within 48 hours
5. Prepare concession options (discount, extended terms, services credits) for the conversation

### Renewal Management
For subscription businesses, renewal automation kicks in 90 days before contract end:

**90 Days Out:**
- Account health review generated
- Renewal forecast added to CRM pipeline
- Customer success manager notified

**60 Days Out:**
- Automated renewal reminder email to customer
- Usage summary attached: "Here's the value you got this year"

**30 Days Out:**
- If no renewal conversation scheduled, escalate
- Generate renewal proposal with pricing and terms

**Cron:** `0 8 * * *` — renewal pipeline sweep.

## Stage 4: Win-Back (Post-Churn)

**Goal:** Re-engage churned customers when the timing is right.

### Triggers
- Customer status changes to "churned" or "cancelled" in CRM
- Subscription ends without renewal

### Win-Back Cadence

**Immediate (Day 0):**
1. Send cancellation confirmation with exit survey (why did you leave?)
2. Log churn reason in CRM for cohort analysis
3. Remove from active engagement workflows

**30 Days Post-Churn:**
1. Send "we miss you" email with product updates since they left
2. Offer a return incentive (1 month free, discounted annual plan)
3. Only send if they haven't unsubscribed from marketing emails

**90 Days Post-Churn:**
1. Check if they've signed up for a competitor (monitor analytics for competitor-related searches)
2. Send case study from their industry showing success with your product
3. If major new features shipped that address their exit reason, highlight those

**180 Days Post-Churn:**
1. Final re-engagement attempt: "A lot has changed — here's what's new"
2. If no response, move to archival nurture (quarterly newsletter only)

**Cron:** `0 10 * * 1` — weekly churned customer sweep.

## Full Cron Schedule

| Time | Stage | Task | Cron |
|---|---|---|---|
| Every 4 hours | Onboarding | New customer detection | `0 */4 * * *` |
| 08:00 daily | Onboarding | Health score sweep | `0 8 * * *` |
| 09:00 MWF | Engagement | Usage pulse check | `0 9 * * 1,3,5` |
| 07:00 1st of month | Engagement | Monthly account reports | `0 7 1 * *` |
| 07:00 weekdays | Retention | Churn risk sweep | `0 7 * * 1-5` |
| 08:00 daily | Retention | Renewal pipeline | `0 8 * * *` |
| 10:00 Mondays | Win-Back | Churned customer sweep | `0 10 * * 1` |

## Implementation Notes

### Stage Transitions
Customers should only be in one lifecycle stage at a time. Implement a state machine with clear transition rules. Stage changes should be logged with timestamps for cohort analysis.

### Over-Communication Risk
The biggest risk in lifecycle automation is overwhelming customers with too many touches. Implement a communication throttle:
- Maximum [N] automated emails per customer per week
- Minimum [X] days between automated touches
- Suppression list: customers who've asked for less communication

### Data Quality
Lifecycle automation is only as good as the data feeding it. Weekly reconciliation: do your CRM, email platform, and analytics agree on who's active? Discrepancies lead to customers getting the wrong stage treatment.

### Extending
- Add **SMS** to the win-back sequence for opted-in customers
- Connect to **Slack** for real-time critical churn alerts
- Integrate with **product analytics** (PostHog, Mixpanel) for deeper behavioral signals
- Add **NPS surveys** at key lifecycle transitions (end of onboarding, 6-month mark, renewal)


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
