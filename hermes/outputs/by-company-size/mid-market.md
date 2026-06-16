# Hermes Agent for Mid-Market: Multi-Team Orchestration

Mid-market companies (50-500 employees) face a distinct automation challenge: they have the team size to specialize by function, but not the headcount to build dedicated internal tools for every department. Marketing, sales, customer success, finance, and operations each have their own tools and data — and those tools don't talk to each other. Hermes Agent provides the cross-department orchestration layer without requiring an engineering team to build and maintain custom integrations.

## The Mid-Market Automation Landscape

Unlike startups (where one person does everything) or enterprises (where dedicated platforms and teams exist for each function), mid-market companies need automation that:

- Works across departments without requiring a central data engineering team
- Respects existing tool choices (no rip-and-replace)
- Scales from 50 to 500 employees without architectural rewrites
- Supports approval workflows for sensitive operations

Hermes meets these needs with profile-based isolation, MCP connectors for every major SaaS tool, and cron-driven skills that can be owned by departmental power users.

## Departmental Agent Patterns

Each department gets its own Hermes profile with dedicated skills, cron schedules, and alerting channels. Operations or IT can manage the profiles centrally while department leads configure their own skills.

### Marketing Operations

```yaml
# Marketing profile: ~/.hermes/profiles/marketing/cron/campaign-monitor.yaml
- name: campaign-performance-daily
  schedule: "0 8 * * *"
  skill: marketing-daily-pulse
  description: Aggregates campaign metrics across ad platforms, email, and web analytics

- name: lead-handoff-monitor
  schedule: "0 */3 * * *"  # Every 3 hours
  skill: lead-handoff
  description: Ensures MQLs are being picked up by sales within SLA

- name: ad-spend-anomaly
  schedule: "0 7,13,19 * * *"
  skill: spend-anomaly-detection
  description: Detects unusual cost-per-click or spend spikes across ad accounts

- name: weekly-marketing-report
  schedule: "0 7 * * 1"
  skill: marketing-weekly-report
  description: Channel performance, CAC trends, and campaign ROI for leadership
```

The marketing profile connects to Google Ads, Meta Ads, LinkedIn Ads, Klaviyo/Mailchimp, GA4, and the CRM. It monitors spend against budget, flags anomaly patterns (a campaign suddenly spending 3x normal without corresponding conversion lift), and tracks the lead-to-opportunity handoff to ensure marketing-sourced leads aren't being dropped.

### Sales Operations

```yaml
# Sales profile: ~/.hermes/profiles/sales/cron/pipeline-monitor.yaml
- name: pipeline-hygiene-daily
  schedule: "0 7 * * 1-5"
  skill: pipeline-cleanup
  description: Flags stale deals, missing data, and pipeline inconsistencies

- name: weekly-forecast
  schedule: "0 16 * * 5"  # Friday 4 PM
  skill: forecast-compiler
  description: Compiles weighted pipeline forecast for weekly review

- name: deal-risk-monitor
  schedule: "0 8,14 * * *"
  skill: deal-risk-alert
  description: Identifies at-risk deals based on inactivity and stage duration

- name: commission-preview
  schedule: "0 8 25 * *"  # 25th of each month
  skill: commission-estimate
  description: Provides estimated commissions for current month-to-date
```

The sales profile connects to the CRM (HubSpot, Close, LeadConnector), calendar systems for activity tracking, and email for communication monitoring. Deal risk detection looks at multiple signals: no logged activity in 7+ days, deal aging past average cycle time for its stage, contact going dark (no email responses), or decision-maker changes detected through LinkedIn.

### Finance Operations

```yaml
# Finance profile: ~/.hermes/profiles/finance/cron/reconciliation.yaml
- name: daily-revenue-reconciliation
  schedule: "0 7 * * *"
  skill: revenue-reconcile
  description: Matches CRM closed-won against billing system and accounting

- name: ar-aging-alert
  schedule: "0 8 * * 1-5"
  skill: ar-collections
  description: Monitors accounts receivable aging and flags past-due accounts

- name: monthly-close-checklist
  schedule: "0 7 1 * *"
  skill: close-checklist
  description: Verifies all revenue entries, accruals, and reconciliations for month-end
```

### Customer Success Operations

```yaml
# CS profile: ~/.hermes/profiles/cs/cron/health-monitor.yaml
- name: customer-health-daily
  schedule: "0 7 * * *"
  skill: health-score-update
  description: Updates customer health scores based on product usage, support tickets, and engagement

- name: churn-risk-alert
  schedule: "0 9 * * *"
  skill: churn-risk-detection
  description: Flags accounts showing churn signals for CSM intervention

- name: qbr-prep
  schedule: "0 7 * * 1"
  skill: qbr-prep
  description: Compiles account summaries for upcoming quarterly business reviews
```

## Approval Workflows for Sensitive Operations

Mid-market companies need controls. Not every automation should act autonomously — some should propose and wait for approval.

Hermes supports this through notification-and-confirmation patterns:

1. **Skill executes and produces a recommendation** (e.g., "Refund $450 to customer X for duplicate charge")
2. **Recommendation routes to Slack with approve/deny buttons** or to email for reply-based confirmation
3. **Approved actions execute in a follow-up skill run**
4. **All approvals are logged** for audit trail

Key workflows that benefit from approval gates:
- Refunds above a threshold
- Contract or pricing changes
- Data deletion requests
- Access permission changes
- Commission adjustments

## Shared Infrastructure Patterns

While departments own their profiles, certain infrastructure should be centralized:

**Shared secrets management:** Database credentials, API keys, and service account tokens stored securely and referenced by all profiles.

**Cross-department alerts channel:** A `#hermes-alerts` Slack channel where critical cross-functional alerts surface (e.g., "Billing system reports 50 failed charges in the last hour").

**Central monitoring:** An operations Hermes profile that monitors that all other profiles' crons are running successfully and alerts on skill failures.

**Shared data sources:** The company database, CRM, and billing system are connected across multiple profiles. Use read-only credentials scoped to each profile's needs.

## Scaling from 50 to 500 Employees

Your Hermes deployment evolves with your company:

| Stage | Profiles | Crons | Pattern |
|-------|----------|-------|---------|
| 50 employees | 2-3 profiles | 10-15 crons | Department leads configure skills |
| 100 employees | 4-5 profiles | 20-30 crons | Dedicated ops person manages Hermes |
| 200 employees | 5-7 profiles | 40-60 crons | RevOps/Data team owns Hermes configuration |
| 500+ employees | Per-team profiles | 80+ crons | Enterprise patterns begin to apply |

## Governance Without Bureaucracy

The key to mid-market success with Hermes: enable departmental autonomy while maintaining visibility. Let marketing build their own campaign monitors, but ensure IT can see all running crons. Let sales build their own pipeline alerts, but ensure finance can verify revenue reconciliation independently.

A weekly Hermes governance review — 30 minutes — covers:
- New skills deployed this week
- Skill failure rate and resolution
- Data quality issues surfaced
- Upcoming connector or API changes that might affect crons

## Getting Started

1. **Pick your highest-pain cross-department gap first.** Likely candidates: lead handoff (marketing → sales), revenue reconciliation (sales → finance), or customer handoff (sales → CS).
2. **Create two profiles:** one for the primary department, one for operations monitoring.
3. **Build three crons:** the cross-department gap filler, a daily pulse for each department, and a failure monitor.
4. **Route everything to Slack.** Mid-market teams live in Slack. Every alert, report, and approval should surface there.
5. **Add approval gates before automated actions.** Build trust with monitoring before enabling autonomous action.

The outcome: each department operates with startup-like efficiency while maintaining the coordination and controls a multi-team organization requires.
