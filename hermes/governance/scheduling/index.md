---
title: Cron Scheduling
description: Cron job management for autonomous agents. Scheduling patterns, delivery channels, chain jobs, monitoring.
---

# Cron Scheduling

Cron jobs are the heartbeat of autonomous agents — recurring tasks that run without human intervention.

## Job Types

| Type | Pattern | Example |
|------|--------|---------|
| Monitoring | Poll external sources | Check for new MCP servers every 3h |
| Reporting | Generate and deliver summaries | Daily 6 PM growth report |
| Watchdog | Alert on threshold breaches | Disk usage > 90% → alert |
| Pipeline | Multi-step data processing | Scrape → analyze → publish |
| Heartbeat | Health check self-reporting | "I'm alive" ping every 30m |

## Scheduling Patterns

```
Common schedules for autonomous agents:

0 4,12,20 * * *     Every 8 hours (3x/day) - Monitoring
0 6-22/4 * * *      Every 4 hours (5x/day) - Content rotation
*/30 * * * *         Every 30 minutes - Email checks
0 18 * * *           Daily at 6 PM - Reports
0 9 * * 1            Every Monday - Weekly recap
```

## Delivery Channels

Jobs can deliver results to:

| Channel | Use Case |
|---------|----------|
| `telegram:chat_id:topic_id` | Team notifications, reports |
| `discord:#channel` | Community alerts |
| `local` | Save results to file for downstream processing |
| `all` | Fan-out to every connected channel |

## Chain Jobs

Jobs can chain by injecting output from one as context to another:

```yaml
job-a:  # Data collection
  schedule: "*/30 * * * *"
  action: "Scrape social media for mentions"

job-b:  # Analysis
  schedule: "*/30 * * * *"
  context_from: ["job-a"]
  action: "Analyze collected mentions, identify leads"
```

## CorpusIQ Active Crons (24 total)

| Category | Count | Examples |
|----------|-------|----------|
| DGX Spark | 21 | Email monitoring, lead capture, content rotation, daily reports |
| Mac Mini M4 | 4 | GitHub PR monitoring, browser-based tasks |

## Best Practices

1. **Stagger monitoring crons** — don't run all checks at the same time
2. **Silent when nothing found** — only report on actionable findings
3. **Watchdog pattern for critical alerts** — script checks threshold, only outputs when breached
4. **Delivery to correct topic** — operational alerts to ops topic, growth to growth topic
5. **Use `context_from` for pipelines** — don't re-scrape in every step

## Self-Healing

Crons can monitor themselves:
- Heartbeat crons that report "still alive"
- Watchdog crons that check other cron outputs
- Drift detection crons that verify data freshness

---

*← [Email Ops](/hermes/governance/email/) | [Monitoring](/hermes/governance/monitoring/) →*
*↑ [Governance](/hermes/governance/)*
