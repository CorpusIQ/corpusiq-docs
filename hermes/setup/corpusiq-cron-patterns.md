---
title: "Running CorpusIQ Cron Jobs — Autonomous Business Monitoring"
description: "Patterns for running CorpusIQ cron jobs with Hermes Agent — daily KPI reports, AR aging alerts, anomaly detection, and multi-client agency reporting."
---

# Running CorpusIQ Cron Jobs — Autonomous Business Monitoring

CorpusIQ connects business data to Hermes Agent. Combine with cron jobs for autonomous monitoring.

## Pattern: Daily KPI Report

```bash
# Crontab: 0 8 * * * (8 AM daily)
hermes run "Query Stripe MRR, QuickBooks cash position, HubSpot pipeline. Email summary to ceo@company.com"
```

## Pattern: AR Aging Alert

```bash
# Crontab: 0 9 * * MON (Monday 9 AM)
python3 token_refresh_guard.py && hermes run "
  Query QuickBooks for all overdue invoices. 
  Sort by amount and days overdue. 
  Email the top 10 to finance@company.com with subject 'Weekly AR Alert'
"
```

## Pattern: Anomaly Detection

```bash
# Crontab: 0 */6 * * * (every 6 hours)
python3 token_refresh_guard.py && hermes run "
  Check Stripe for:
  - Failed payments in last 6 hours
  - Unusual churn pattern (>2 standard deviations from 30-day average)
  - Revenue outside expected range
  Alert on Telegram if any anomalies found.
"
```

## Pattern: Multi-Client Agency Report

```bash
# Crontab: 0 7 * * * (7 AM daily)
python3 token_refresh_guard.py && hermes run "
  For each client connected:
  - Query their ad platform ROAS
  - Check their email campaign performance  
  - Verify their revenue vs target
  Generate a morning briefing with flags for underperforming clients.
"
```

## Token Refresh Guard

Always prefix CorpusIQ cron tasks with the token guard. The JWT expires hourly.

Download the guard script:
```bash
curl -O https://raw.githubusercontent.com/CorpusIQ/corpusiq-docs/main/hermes/scripts/token_refresh_guard.py
chmod +x token_refresh_guard.py
```

## Rate Limits

- Stripe: 100 req/sec (read-only, no practical limit)
- QuickBooks: 500 req/day per app (batch queries where possible)
- HubSpot: 100 req/10sec (burst OK, sustained <10/sec)

---

*More patterns: [corpusiq.io/docs](https://www.corpusiq.io/docs)*
