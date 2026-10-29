---
title: "Running CorpusIQ Cron Jobs - Autonomous Business"
description: "Patterns for running CorpusIQ cron jobs with Hermes Agent - daily KPI reports, AR aging alerts, anomaly detection, and multi-client agency reporting."
canonical: "https://www.corpusiq.io/docs/hermes/setup/corpusiq-cron-patterns/"
robots: "index,follow"
last_updated: 2026-10-29
tags: ["hermes agent", "ai agent", "nous research"]

---

# Running CorpusIQ Cron Jobs - Autonomous Business Monitoring

CorpusIQ connects business data to Hermes Agent. Combine with cron jobs for autonomous monitoring.

## Pattern: Daily KPI Report

```bash
# Crontab: 0 8 * * * (8 AM daily)
hermes -z "Query Stripe MRR, QuickBooks cash position, HubSpot pipeline. Email summary to ceo@company.com"
```

## Pattern: AR Aging Alert

```bash
# Crontab: 0 9 * * MON (Monday 9 AM)
hermes -z "
  Query QuickBooks for all overdue invoices. 
  Sort by amount and days overdue. 
  Email the top 10 to finance@company.com with subject 'Weekly AR Alert'
"
```

## Pattern: Anomaly Detection

```bash
# Crontab: 0 */6 * * * (every 6 hours)
hermes -z "
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
hermes -z "
  For each client connected:
  - Query their ad platform ROAS
  - Check their email campaign performance  
  - Verify their revenue vs target
  Generate a morning briefing with flags for underperforming clients.
"
```

## Token Refresh Guard

A CorpusIQ JWT access token expires after 60 minutes, so any cron that runs less often than that needs a fresh credential before it starts.

The simplest setup is to let Hermes own the token. Register the server with OAuth instead of pasting a JWT into `config.yaml`:

```bash
hermes mcp add corpusiq --url https://mcp2.corpusiq.io/mcp --auth oauth
hermes mcp login corpusiq          # add --flow device for a headless host
hermes mcp test corpusiq
```

The server publishes OAuth 2.0 authorization-server and protected-resource metadata, so Hermes runs the flow once and keeps the credential in its own token store. Re-authenticate with `hermes mcp reauth corpusiq` when the 30-day refresh credential lapses.

If you keep the header-auth setup instead, refresh before the task and write the new access token into `config.yaml`:

```bash
curl -s -X POST https://mcp2.corpusiq.io/oauth/token \
  -d "grant_type=refresh_token&refresh_token=<saved_refresh_token>"
```

A wrapper script is the right place for that: refresh, patch `headers.Authorization`, then call `hermes -z "<task>"` in the same run.

## Rate Limits

- Stripe: 100 req/sec (read-only, no practical limit)
- QuickBooks: 500 req/day per app (batch queries where possible)
- HubSpot: 100 req/10sec (burst OK, sustained <10/sec)

---

*More patterns: [corpusiq.io/docs](https://www.corpusiq.io/docs)*
