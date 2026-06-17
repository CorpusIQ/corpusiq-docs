---
title: Cron Design Best Practices for Hermes Agent — Reliable Scheduled Automation
description: Production-grade cron design for Hermes Agent scheduled automation. Idempotency, error handling with retry/backoff, rate limiting, monitoring, delivery targets, and anti-patterns. Build crons that don't fail silently.
category: best-practices
tags: [hermes-agent, cron-design, scheduled-automation, idempotency, error-handling, monitoring, rate-limiting]
last_updated: 2026-06-16
---

# Cron Design Best Practices — Reliable Scheduled Automation

Scheduled automation is one of Hermes Agent's most powerful features, but poorly designed crons are the fastest path to operational pain. These cron design best practices cover idempotency, error handling, rate limiting, monitoring, and the anti-patterns that keep your scheduled tasks reliable and safe in production.

## Overview

Crons are the heartbeat of autonomous Hermes Agent operation. They handle email monitoring, data synchronization, report generation, and operational checks — running on schedules from every 5 minutes to once per month. Following [Hermes Agent best practices](/hermes/best-practices/) for cron design prevents silent failures, resource exhaustion, and alert fatigue.

## How It Works

A well-designed Hermes Agent cron follows this pattern:

```
SCHEDULE → DATA COLLECTION → PROCESSING → VALIDATION → OUTPUT → LOGGING
                                                         ↓
                                                    ERROR → RETRY → DEAD-LETTER → ALERT
```

## The Cardinal Rule: Idempotency

Every cron should be safe to run multiple times with the same inputs. Cron schedulers can drift, containers can restart, and manual re-runs happen during debugging. If your cron writes to a database, use upsert semantics. If it sends notifications, track sent status. If it generates reports, use deterministic filenames.

A good litmus test: could you run this cron three times back-to-back without breaking anything?

## Error Handling: Fail Loudly, Recover Gracefully

**Retry with backoff.** Transient failures (network timeouts, rate limits) should retry with exponential backoff. Cap at 3-5 attempts with jitter.

**Dead-letter queue.** After all retries exhausted, route failed work to a dead-letter queue or structured log. Never silently discard work.

**Alert on persistent failure.** If your cron fails for more than N consecutive runs, trigger an alert through [Slack](/hermes/integrations/slack-github.md), email, or PagerDuty.

**Partial success handling.** Handle individual failures within a batch without aborting the entire batch. Log failed records and continue processing.

## Rate Limiting and Delivery Targets

Define explicit throughput targets. Implement token-bucket or sliding-window rate limiting. Maintain separate rate-limit budgets per API integration.

**Delivery windows matter.** If your cron takes 4 minutes to complete, don't schedule it every 5 minutes — that leaves only 1 minute of slack. Schedule at 2-3x the expected runtime to prevent overlap.

## Monitoring and Observability

Every cron should emit:

- **Start/end timestamps** with duration — track runtime drift
- **Record counts** — items read, written, failed
- **Error counts** by type
- **Last successful run timestamp** — your canary

**Heartbeat monitoring:** A separate lightweight check every 15-30 minutes verifies the last successful run is within the expected window.

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Fix |
|---|---|---|
| **God Cron** | One failure cascades everything | Split into single-responsibility crons |
| Hardcoded timestamps | DST/timezone bugs | Always UTC, always timezone-aware |
| Unbounded queries | Million-row timeouts | Always paginate/LIMIT |
| Missing dry-run mode | Can't test safely | Add `--dry-run` flag |
| Console output as logging | Ephemeral, unsearchable | Structured persistent logging |

## Delivery Target Patterns

- **Real-time needs:** Use event-driven architecture, not polling crons
- **Near-real-time:** Every 5 minutes — acceptable for most ecommerce
- **Hourly:** Good for dashboards, cache warming
- **Daily:** Batch windows for exports, reconciliation
- **Weekly/monthly:** Run during low-traffic with explicit retry windows

## Benefits

- **Zero silent failures**: Alerting on persistent failure catches issues before users notice
- **Predictable costs**: Rate limiting prevents API overage charges
- **Easy debugging**: Structured logs with timestamps and record counts
- **Safe testing**: Dry-run mode lets you verify changes before deployment

## FAQ

### What makes a cron job idempotent in Hermes Agent?
A cron is idempotent if running it multiple times with the same inputs produces the same result. Use upsert database operations, deduplication keys on notifications, and deterministic file naming for reports.

### How many times should a failed cron retry?
Retry 3-5 times with exponential backoff and jitter. After all retries are exhausted, route to a dead-letter queue — never silently discard work. Alert after 3 consecutive failures.

### How do I monitor cron job health?
Track start/end timestamps, record counts processed, error counts by type, and last successful run timestamp. Run a separate heartbeat check every 15-30 minutes to catch stale crons.

## Related Pages

- [Best Practices Overview](/hermes/best-practices/) — All best practices guides
- [Model Selection](model-selection.md) — Use the right model for each cron
- [Security](security.md) — Credential management for scheduled tasks
- [Setup Guides](/hermes/setup/) — Run crons on [cloud VPS](/hermes/setup/cloud-vps.md) or [Raspberry Pi](/hermes/setup/raspberry-pi.md)
- [Blueprints](/hermes/blueprints/) — End-to-end cron-anchored workflows

---

*The best cron is one you can explain to a teammate in 30 seconds.*

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What makes a Hermes Agent cron job idempotent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A cron is idempotent if running it multiple times with the same inputs produces the same result. Use upsert database operations, deduplication keys on notifications, and deterministic file naming for reports."
      }
    },
    {
      "@type": "Question",
      "name": "How many times should a failed Hermes Agent cron retry?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Retry 3-5 times with exponential backoff and jitter. After all retries are exhausted, route to a dead-letter queue — never silently discard work. Alert a human after 3 consecutive failures."
      }
    },
    {
      "@type": "Question",
      "name": "How do I monitor Hermes Agent cron job health?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Track start/end timestamps, record counts processed, error counts by type, and last successful run timestamp. Run a separate heartbeat check every 15-30 minutes to catch stale crons before users notice."
      }
    }
  ]
}
</script>
