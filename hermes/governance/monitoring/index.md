---
title: System Monitoring
description: Health monitoring for autonomous agent deployments. Drift detection, alerting, performance audits, system governance.
---

# System Monitoring

Autonomous agents need continuous health monitoring. When agents run 24/7 without human supervision, monitoring is the safety net.

## Monitoring Layers

```
Layer 1: Process Health
  ├─ Is the agent process running?
  ├─ CPU/Memory within bounds?
  └─ Any zombie processes?

Layer 2: Operational Health
  ├─ Are crons firing on schedule?
  ├─ Are emails being sent/received?
  ├─ Are API keys still valid?
  └─ Token usage within budget?

Layer 3: Quality Health
  ├─ Are outputs meeting quality thresholds?
  ├─ Are responses going to the right channels?
  └─ Any silent failures detected?
```

## Key Metrics

| Metric | Check | Alert Threshold |
|--------|-------|-----------------|
| Cron completion rate | `cronjob list` success/fail ratio | < 95% |
| API token validity | Test auth endpoint | Expired or revoked |
| Disk usage | `df -h` | > 90% |
| Memory usage | `free -m` | > 90% |
| Email deliverability | SMTP test send | Bounce > 10% |
| LLM token burn | Session token counts | > $50/day |
| Session DB size | SQLite file size | > 1GB |
| Skill staleness | Last-updated timestamp | > 30 days |

## Drift Detection

CorpusIQ's metric spec system detects when two sources disagree:

```python
# Two sources should agree within 1%
metric_spec_resolve("leads_this_week")
# Returns: {value: 47, drift: {source_a: 47, source_b: 44, delta_pct: 6.4}}
# Flagged: 6.4% > 1% tolerance → investigate
```

## Alerting Channels

| Severity | Channel | Example |
|----------|---------|---------|
| Critical | Telegram Topic 2 (dev) + DM | API key expired |
| Warning | Telegram Topic 2 (dev) | Cron failure |
| Info | Logged to activity-log.jsonl | Daily stats |

## System Audit

Run `corpusiq-system-audit` skill to run a full six-category audit:
1. Configuration integrity
2. Connection health
3. Cron execution
4. Disk and memory
5. Token and cost
6. Skill freshness

## Self-Monitoring Patterns

```
cron: health-check (every 30m)
  → script: check_processes.sh
  → silent if healthy
  → alerts only on threshold breach

cron: drift-report (daily at 6 AM)
  → metric_spec_drift_report
  → reports discrepancies across data sources
  → silent if all within tolerance
```

## Dashboard Files

| File | Content |
|------|---------|
| `post-log.jsonl` | All outbound posts |
| `activity-log.jsonl` | All agent actions |
| `lead-pipeline.jsonl` | Lead state transitions |
| `email-monitor.log` | Inbound email processing |
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
