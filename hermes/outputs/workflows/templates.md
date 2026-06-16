# Copy-Paste Cron Templates: Ready-to-Deploy Workflows

This page is a grab-bag of cron + skill templates you can copy, adapt, and deploy in minutes. Each template includes the cron schedule, the skill it calls, what data sources it uses, and what it produces. Replace the placeholder values with your own tool names, channels, and thresholds.

## How to Use These Templates

1. Copy the YAML block into `~/.hermes/cron/` (or your profile's cron directory)
2. Create the corresponding skill file in `~/.hermes/skills/`
3. Adjust the schedule, thresholds, and alert destinations for your environment
4. Test with a single manual run before enabling the cron
5. Monitor for a week, tune thresholds, then add more

## Email Monitoring Templates

### Support Inbox Triage

```yaml
- name: support-inbox-triage
  schedule: "*/5 * * * *"  # Every 5 minutes
  skill: email-triage
  description: Classifies incoming support emails and routes to appropriate queues
  alert_channel: "#support-triage"
```

**What the skill does:** Monitors Gmail/Outlook inboxes for new messages, classifies by topic (billing, technical, account, feature request, bug), checks sender against CRM for priority tier, assigns priority, and posts triage summary to Slack.

**Data sources:** Email connector (Gmail/Outlook), CRM connector (HubSpot/Close/LeadConnector), Slack connector.

### Invoice Arrival Monitor

```yaml
- name: vendor-invoice-monitor
  schedule: "0 9,15 * * *"  # Twice daily at 9 AM and 3 PM
  skill: invoice-processor
  description: Detects vendor invoice emails and logs them for processing
```

**What the skill does:** Scans email for invoice patterns (attachment with "invoice" in filename, subject lines matching vendor patterns), extracts key fields (vendor, amount, due date, invoice number), logs to accounting system or Google Sheet for approval, and alerts finance team of invoices needing attention.

**Data sources:** Email connector, Google Drive (Sheets) or QuickBooks connector, Slack connector.

### Lead Alert Monitor

```yaml
- name: lead-notification-watch
  schedule: "*/10 * * * *"  # Every 10 minutes
  skill: lead-alert
  description: Monitors email for high-intent lead signals and routes to sales
```

**What the skill does:** Watches for patterns like demo request confirmations, contact form submissions, pricing page inquiries, and trial signup notifications. Enriches with CRM data (existing contact? current customer?), scores urgency, and posts to the sales channel with context.

**Data sources:** Email connector, CRM connector, Slack connector.

## Report Generation Templates

### Daily Executive Summary

```yaml
- name: daily-exec-summary
  schedule: "0 7 * * 1-5"  # Weekdays at 7 AM
  skill: daily-exec-brief
  description: Compiles key metrics into a morning executive summary
  output: slack  # or email
```

**What the skill does:** Pulls yesterday's metrics across the business and compiles into a concise Slack post or email. Typical sections: revenue (from Stripe/QuickBooks), new customers (from CRM), website traffic and conversion (from GA4), support tickets opened/closed (from ticketing/email), key alerts triggered (from other Hermes skills).

**Data sources:** Stripe connector, QuickBooks connector, CRM connector, GA4 connector, email connector.

### Weekly Business Review

```yaml
- name: weekly-business-review
  schedule: "0 8 * * 1"  # Monday at 8 AM
  skill: weekly-review
  description: Generates comprehensive weekly business review with trends
```

**What the skill does:** A deeper weekly report with week-over-week comparisons, trend charts (as data, not images), top-line and departmental metrics, pipeline changes, and a summary of all Hermes alerts from the past week. Designed for the Monday leadership standup.

**Data sources:** All active connectors, aggregated across the week.

### Monthly Close Report

```yaml
- name: monthly-close-package
  schedule: "0 7 1 * *"  # 1st of each month at 7 AM
  skill: monthly-close
  description: Compiles month-end financial and operational metrics
```

**What the skill does:** Revenue reconciliation (CRM vs. billing vs. accounting), MRR waterfall, customer count changes, pipeline created vs. closed, expense summary, and key operational metrics. Saved as a date-stamped report in a shared Google Drive folder.

**Data sources:** CRM connector, Stripe connector, QuickBooks connector, database connector.

## Data Sync Templates

### CRM-to-Billing Sync Check

```yaml
- name: crm-billing-sync
  schedule: "0 */6 * * *"  # Every 6 hours
  skill: crm-billing-reconciliation
  description: Identifies discrepancies between CRM deals and billing system records
```

**What the skill does:** Cross-references closed-won deals in CRM against active subscriptions in billing. Flags: CRM deals with no corresponding subscription, subscriptions with no CRM deal, plan/amount mismatches, and customer status inconsistencies. Produces a reconciliation queue for RevOps.

**Data sources:** CRM connector (HubSpot/Close/LeadConnector), Stripe connector (or QuickBooks connector for non-SaaS).

### Database-to-Analytics Validation

```yaml
- name: db-analytics-validation
  schedule: "0 8 * * *"  # Daily at 8 AM
  skill: data-consistency-check
  description: Validates that key metrics match between production database and analytics
```

**What the skill does:** Runs the same metric queries against your production database (via PostgreSQL/MSSQL connector) and your analytics platform (GA4, PostHog). Compares user counts, event volumes, and conversion numbers. Flags discrepancies beyond configured tolerance for investigation.

**Data sources:** Database connector, GA4 connector, PostHog connector.

### Multi-Platform Listing Sync

```yaml
- name: listing-platform-sync
  schedule: "0 */4 * * *"  # Every 4 hours
  skill: listing-sync-verifier
  description: Ensures product/service listings are consistent across all platforms
```

**What the skill does:** For e-commerce or marketplace businesses: queries your source-of-truth (database, Shopify, Amazon Seller) and checks that listings on all platforms match — correct price, inventory status, description, images. Alerts on any discrepancy.

**Data sources:** Database connector, Shopify connector (if applicable), Amazon Seller connector (if applicable), web extraction for external platforms.

## Alerting Templates

### Anomaly Detection

```yaml
- name: metric-anomaly-detection
  schedule: "0 */2 * * *"  # Every 2 hours
  skill: anomaly-detector
  description: Compares current metrics against historical baselines and alerts on deviations
```

**What the skill does:** Pulls current-hour metrics (signups, revenue events, page views, API errors), compares against 7-day rolling average and same-day-last-week values, and alerts when any metric deviates beyond configured thresholds (e.g., signups drop 50% below baseline, error rate spikes 3x). Alerts include the metric, current value, expected range, and potential related events.

**Data sources:** Database connector, Stripe connector, GA4 connector.

### SLA Breach Warning

```yaml
- name: sla-breach-warning
  schedule: "*/10 * * * *"  # Every 10 minutes
  skill: sla-monitor
  description: Checks all open tickets against SLA targets with escalating alerts
```

**What the skill does:** Queries ticketing system or support inbox for open items, calculates time open against SLA targets, and escalates: at 50% SLA → gentle reminder to owner, at 75% → notification to team lead, at 90% → alert to manager, after breach → creates post-mortem draft.

**Data sources:** CRM connector (for ticket data), email connector, Slack connector.

### System Health Check

```yaml
- name: system-health-check
  schedule: "*/5 * * * *"  # Every 5 minutes
  skill: health-check
  description: Pings critical endpoints and alerts on failures
```

**What the skill does:** HTTP health checks against critical endpoints (API, website, auth service), database connectivity checks, and upstream dependency checks. Escalates through on-call channels if failures persist beyond configured retry windows.

**Data sources:** Web extraction or direct HTTP checks, database connector (connectivity test).

## Integration-Specific Templates

### Stripe Revenue Monitor

```yaml
- name: stripe-revenue-monitor
  schedule: "0 7,13,19 * * *"  # Three times daily
  skill: stripe-revenue-pulse
  description: Tracks daily revenue, new subscriptions, churn, and failed charges
```

**Data sources:** Stripe connector. Queries charges, subscriptions, customers.

### GA4 Traffic Anomaly

```yaml
- name: ga4-traffic-watch
  schedule: "0 */3 * * *"  # Every 3 hours
  skill: traffic-anomaly
  description: Detects unusual traffic patterns that may indicate issues or opportunities
```

**Data sources:** GA4 connector. Compares current traffic against baseline.

### CRM Pipeline Health

```yaml
- name: crm-pipeline-health
  schedule: "0 8 * * 1-5"  # Weekdays at 8 AM
  skill: pipeline-health-check
  description: Daily pipeline health report with deal movement and hygiene issues
```

**Data sources:** CRM connector. Queries deals, activities, contacts.

## Template Customization Guide

When adapting these templates, replace:

| Placeholder | Examples |
|-------------|----------|
| `alert_channel` | `"#revops-alerts"`, `"#support-triage"`, `"@channel"` |
| `skill` name | Your skill filename in `~/.hermes/skills/` |
| Schedule expression | Standard cron syntax. Common patterns above. |
| Threshold values | Start generous (fewer false positives), tighten over time |

## Quick-Start: Your First Three Crons

If you're new to Hermes, deploy these three crons today:

1. **Daily pulse** (report): One morning summary replacing your dashboard checks.
2. **Anomaly detection** (alert): One metric that will tell you when something is wrong before customers do.
3. **Health check** (monitor): One endpoint or system that must stay up.

That's it. Three crons. One hour of setup. You'll know within a week what to automate next.
