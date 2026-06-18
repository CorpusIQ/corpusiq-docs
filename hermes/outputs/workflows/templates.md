---
title: Hermes Cron Templates — 12 Copy-Paste Workflows for Autonomous Agents
description: "Ready-to-deploy cron templates for Hermes Agent: email triage, report generation, data sync, anomaly detection, SLA monitoring, and more. Copy, adapt, deploy in minutes."
category: Outputs
tags:
  - cron-templates
  - workflow-automation
  - hermes-crons
  - autonomous-agents
  - deployment-blueprints
last_updated: 2026-06-16
---

# Copy-Paste Cron Templates — 12 Ready-to-Deploy Autonomous Workflows

This is a **grab-bag of cron + skill templates** you can copy, adapt, and deploy in minutes. Each template includes the cron schedule, the skill it calls, what data sources it uses, and what it produces. Replace the placeholder values with your own tool names, channels, and thresholds.

## Overview

**Stop starting from scratch.** These 12 templates cover the most common automation patterns — email monitoring, report generation, data sync, anomaly detection, and platform-specific integrations. Each template has been production-tested on a [24/7 Hermes deployment](/hermes/) running 38 crons.

> **See also:** [Cron Scheduling Guide](/hermes/governance/scheduling/) · [Outputs Overview](/hermes/outputs/) · [Agent Library](/hermes/agents/)

## How to Use These Templates

1. **Copy the YAML block** into `~/.hermes/cron/` (or your profile's cron directory)
2. **Create the corresponding skill file** in `~/.hermes/skills/`
3. **Adjust the schedule, thresholds, and alert destinations** for your environment
4. **Test with a single manual run** before enabling the cron
5. **Monitor for a week**, tune thresholds, then add more

## Email Monitoring Templates

### Support Inbox Triage
```yaml
- name: support-inbox-triage
  schedule: "*/5 * * * *"  # Every 5 minutes
  skill: email-triage
  description: Classifies incoming support emails and routes to appropriate queues
  alert_channel: "#support-triage"
```

**What it does:** Monitors Gmail/Outlook for new messages, classifies by topic (billing, technical, account, feature request), checks sender against CRM for priority tier, assigns priority, posts triage summary to Slack. **Data sources:** Email connector, CRM connector, Slack connector.

### Invoice Arrival Monitor
```yaml
- name: vendor-invoice-monitor
  schedule: "0 9,15 * * *"  # Twice daily at 9 AM and 3 PM
  skill: invoice-processor
  description: Detects vendor invoice emails and logs them for processing
```

**What it does:** Scans email for invoice patterns, extracts vendor/amount/due date/invoice number, logs to accounting system, alerts finance team. **Data sources:** Email connector, Google Drive (Sheets) or QuickBooks connector.

### Lead Alert Monitor
```yaml
- name: lead-notification-watch
  schedule: "*/10 * * * *"  # Every 10 minutes
  skill: lead-alert
  description: Monitors email for high-intent lead signals and routes to sales
```

**What it does:** Watches for demo requests, contact forms, pricing inquiries, trial signups. Enriches with CRM data, scores urgency, posts to sales channel. **Data sources:** Email connector, CRM connector, Slack connector.

## Report Generation Templates

### Daily Executive Summary
```yaml
- name: daily-exec-summary
  schedule: "0 7 * * 1-5"  # Weekdays at 7 AM
  skill: daily-exec-brief
  description: Compiles key metrics into a morning executive summary
  output: slack
```

**What it does:** Pulls yesterday's revenue (Stripe/QuickBooks), new customers (CRM), web traffic (GA4), support tickets, and key alerts into a concise morning post. **Data sources:** Stripe, QuickBooks, CRM, GA4, Email connectors.

### Weekly Business Review
```yaml
- name: weekly-business-review
  schedule: "0 8 * * 1"  # Monday at 8 AM
  skill: weekly-review
  description: Generates comprehensive weekly business review with trends
```

**What it does:** Deeper weekly report with WoW comparisons, trend data, top-line and departmental metrics, pipeline changes, and all Hermes alerts from the past week. **Data sources:** All active connectors.

### Monthly Close Report
```yaml
- name: monthly-close-package
  schedule: "0 7 1 * *"  # 1st of each month at 7 AM
  skill: monthly-close
  description: Compiles month-end financial and operational metrics
```

**What it does:** Revenue reconciliation (CRM vs. billing vs. accounting), MRR waterfall, customer count changes, pipeline created vs. closed, expense summary. **Data sources:** CRM, Stripe, QuickBooks, Database connectors.

## Data Sync Templates

### CRM-to-Billing Sync Check
```yaml
- name: crm-billing-sync
  schedule: "0 */6 * * *"  # Every 6 hours
  skill: crm-billing-reconciliation
  description: Identifies discrepancies between CRM deals and billing system records
```

**What it does:** Cross-references closed-won CRM deals against active billing subscriptions. Flags CRM deals with no subscription, subscriptions with no CRM deal, plan/amount mismatches. **Data sources:** CRM connector, Stripe connector.

### Database-to-Analytics Validation
```yaml
- name: db-analytics-validation
  schedule: "0 8 * * *"  # Daily at 8 AM
  skill: data-consistency-check
  description: Validates that key metrics match between production database and analytics
```

**What it does:** Runs identical metric queries against production database and analytics platform (GA4, PostHog). Compares user counts, event volumes, conversions. Flags discrepancies beyond tolerance. **Data sources:** Database connector, GA4 connector, PostHog connector.

## Alerting Templates

### Anomaly Detection
```yaml
- name: metric-anomaly-detection
  schedule: "0 */2 * * *"  # Every 2 hours
  skill: anomaly-detector
  description: Compares current metrics against historical baselines and alerts on deviations
```

**What it does:** Pulls current metrics (signups, revenue, page views, API errors), compares against 7-day rolling average and same-day-last-week, alerts when deviation exceeds thresholds. **Data sources:** Database, Stripe, GA4 connectors.

### SLA Breach Warning
```yaml
- name: sla-breach-warning
  schedule: "*/10 * * * *"  # Every 10 minutes
  skill: sla-monitor
  description: Checks all open tickets against SLA targets with escalating alerts
```

**What it does:** Queries ticketing for open items, calculates time open against SLA targets, escalates at 50%/75%/90% thresholds with post-breach post-mortem draft. **Data sources:** CRM connector, email connector, Slack connector.

### System Health Check
```yaml
- name: system-health-check
  schedule: "*/5 * * * *"  # Every 5 minutes
  skill: health-check
  description: Pings critical endpoints and alerts on failures
```

**What it does:** HTTP health checks against critical endpoints, database connectivity checks, upstream dependency checks. Escalates through on-call channels if failures persist. **Data sources:** Web extraction/HTTP checks, database connector.

## Integration-Specific Templates

### Stripe Revenue Monitor
```yaml
- name: stripe-revenue-monitor
  schedule: "0 7,13,19 * * *"  # Three times daily
  skill: stripe-revenue-pulse
  description: Tracks daily revenue, new subscriptions, churn, and failed charges
```
**Data sources:** Stripe connector — charges, subscriptions, customers.

### GA4 Traffic Anomaly
```yaml
- name: ga4-traffic-watch
  schedule: "0 */3 * * *"  # Every 3 hours
  skill: traffic-anomaly
  description: Detects unusual traffic patterns that may indicate issues or opportunities
```
**Data sources:** GA4 connector — current traffic vs. baseline.

### CRM Pipeline Health
```yaml
- name: crm-pipeline-health
  schedule: "0 8 * * 1-5"  # Weekdays at 8 AM
  skill: pipeline-health-check
  description: Daily pipeline health report with deal movement and hygiene issues
```
**Data sources:** CRM connector — deals, activities, contacts.

## Template Customization Guide

| Placeholder | Examples |
|-------------|----------|
| `alert_channel` | `"#revops-alerts"`, `"#support-triage"`, `"@channel"` |
| `skill` name | Your skill filename in `~/.hermes/skills/` |
| Schedule expression | Standard cron syntax |
| Threshold values | Start generous (fewer false positives), tighten over time |

## Quick-Start: Your First Three Crons

Deploy these three crons today:

1. **Daily pulse** (report) — One morning summary replacing dashboard checks
2. **Anomaly detection** (alert) — One metric that tells you when something is wrong before customers do
3. **Health check** (monitor) — One endpoint or system that must stay up

**Three crons. One hour of setup.** You'll know within a week what to automate next.

## FAQ

### What are Hermes cron templates?

Hermes cron templates are **ready-to-deploy YAML configurations** that define scheduled autonomous agent tasks. Each template includes the cron schedule, which skill to execute, what data sources to query, and where to deliver the output. They're designed to be copied, customized with your values, and deployed in minutes.

### How do I install these cron templates?

Copy the YAML block into `~/.hermes/cron/` (or your profile's cron directory), create the corresponding skill file in `~/.hermes/skills/`, adjust thresholds and alert channels, test with a single manual run, then enable. Full steps in [How to Use These Templates](#how-to-use-these-templates).

### Which template should I deploy first?

Start with the **Daily Executive Summary** (report generation) to replace your morning dashboard check, then **Anomaly Detection** (alerting) to catch issues before customers report them, then **System Health Check** (monitoring) to ensure critical endpoints stay up.

### Do these templates work with any MCP connector?

Yes. The templates use standard Hermes skill references. Replace the `skill` name with your actual skill filename, and ensure your connectors are authenticated via `hermes setup connectors`. The [CorpusIQ MCP connectors](/hermes/mcp/connectors/) provide 37+ business tool integrations through a single OAuth flow.

### How do I customize thresholds and schedules?

Edit the YAML `schedule` field with standard cron expressions, and adjust threshold values in your skill file. Start with **generous thresholds** (fewer false positives), monitor for a week, then tighten as you build confidence in the automation.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What are Hermes cron templates?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hermes cron templates are ready-to-deploy YAML configurations defining scheduled autonomous agent tasks with cron schedules, skills, data sources, and output destinations."
      }
    },
    {
      "@type": "Question",
      "name": "How do I install these cron templates?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Copy the YAML into ~/.hermes/cron/, create the skill file in ~/.hermes/skills/, adjust thresholds, test manually, then enable."
      }
    },
    {
      "@type": "Question",
      "name": "Which template should I deploy first?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Start with Daily Executive Summary (report), then Anomaly Detection (alerting), then System Health Check (monitoring) — three crons covering the essential patterns."
      }
    },
    {
      "@type": "Question",
      "name": "Do these templates work with any MCP connector?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Templates use standard Hermes skill references. Replace skill names with your actual filenames and authenticate connectors via hermes setup connectors."
      }
    },
    {
      "@type": "Question",
      "name": "How do I customize thresholds and schedules?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Edit the YAML schedule field with standard cron expressions. Start with generous thresholds, monitor for a week, then tighten as confidence builds."
      }
    }
  ]
}
</script>

## Related Pages

- [Outputs Overview — Industry Case Studies](/hermes/outputs/)
- [Cron Scheduling Guide — 38 Production Crons](/hermes/governance/scheduling/)
- [Agent Library — 9 Role Configurations](/hermes/agents/)
- [CorpusIQ MCP Connectors — 37+ Business Tools](/hermes/mcp/connectors/)
- [Architecture — 6-Layer Production Model](/hermes/architecture/)


*From the [Hermes Case Studies](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/outputs/case-studies) — real-world agent deployments. Powered by [CorpusIQ](https://www.corpusiq.io).*


*From the [Hermes Case Studies](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/outputs/case-studies) — real-world agent deployments. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
