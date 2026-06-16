# Cron Design Principles for Hermes

Scheduled automation is one of Hermes's most powerful features, but poorly designed crons are the fastest path to operational pain. This guide covers design principles that keep your scheduled tasks reliable, observable, and safe.

## The Cardinal Rule: Idempotency

Every cron should be safe to run multiple times with the same inputs. Cron schedulers can drift, containers can restart, and manual re-runs happen during debugging. If your cron writes to a database, use upsert semantics (`INSERT ... ON CONFLICT UPDATE`). If it sends notifications, track sent status to avoid duplicate alerts. If it generates reports, use deterministic filenames that naturally overwrite. A good litmus test: could you run this cron three times back-to-back without breaking anything or producing garbage data?

Idempotency applies to side effects too. A cron that reserves API rate-limit budget must release it on failure. A cron that locks rows must release locks even if the process crashes. Use database transactions with proper timeout and rollback, or implement a heartbeat-based lease system for distributed locks.

## Error Handling: Fail Loudly, Recover Gracefully

Crons that fail silently are worse than no cron at all — they create false confidence. Every cron should have a clear error-handling strategy:

**Retry with backoff.** Transient failures (network timeouts, rate limits, temporary API errors) should retry with exponential backoff. Cap retries at a reasonable maximum (3-5 attempts) and include jitter to avoid thundering-herd problems.

**Dead-letter queue.** After all retries are exhausted, route the failed work to a dead-letter queue or structured log. This preserves the payload for investigation and manual replay. Never silently discard work.

**Alert on persistent failure.** If your cron fails for more than N consecutive runs (or exceeds a time threshold without success), trigger an alert through your monitoring channel — Slack, email, or PagerDuty.

**Partial success handling.** If your cron processes a batch of records, handle individual failures without aborting the entire batch. Log failed records with their identifiers and continue processing the rest.

## Rate Limiting and Delivery Targets

Define explicit throughput targets. How many API calls per second can your cron make? What is the downstream system's tolerance? A cron that processes 10,000 records at 1,000 calls per second will either get rate-limited or overwhelm the target service.

Implement a token-bucket or sliding-window rate limiter. For crons that span multiple API integrations, maintain separate rate-limit budgets per service. Log actual vs. budgeted rates so you can tune over time.

**Delivery windows matter.** If your cron checks inventory and sends alerts, timing the window correctly is everything. A cron that runs every 5 minutes but takes 4 minutes to complete has only 1 minute of slack — any spike in data volume and it overlaps with the next run. Define a maximum expected runtime and schedule your cron at 2-3x that interval to prevent overlap.

## Monitoring and Observability

Every cron should emit:

- **Start/end timestamps with duration.** Track runtime drift over weeks.
- **Record counts processed.** Items read, items written, items failed.
- **Error counts by type.** Network errors vs. validation errors vs. upstream errors.
- **Last successful run timestamp.** This is your canary — if it goes stale, something is broken.

Store these as structured logs or metrics, not just stdout. A cron that runs at 3 AM and prints to a terminal you'll never check isn't monitored — it's a wish.

**Heartbeat monitoring.** Use a separate lightweight check (every 15-30 minutes) that verifies the last successful run timestamp is within the expected window. This catches stale crons before users notice.

## Anti-Patterns to Avoid

**The "God Cron."** One cron job that does inventory sync, pricing updates, report generation, and email notifications all in one script. When one step fails, everything fails. When you need to change one thing, you risk breaking everything. Split responsibilities into separate crons with clear ownership.

**Hardcoded timestamps.** Never use `datetime.now()` without timezone awareness. Never assume "midnight" means the same thing across DST boundaries. Always store and compare in UTC.

**Unbounded queries.** A cron that does `SELECT * FROM orders WHERE processed = false` with no LIMIT will eventually process a million rows and time out. Always paginate or limit.

**Missing dry-run mode.** Every cron should support a dry-run flag that logs what it would do without actually doing it. This is invaluable for testing changes and onboarding new operators.

**Console output as logging.** Stdout is ephemeral. Structured logging to a persistent store (database, log aggregation service, file with rotation) is the minimum viable approach.

## Delivery Target Patterns

Match your cron schedule to the business need, not to "every 15 minutes because that's the default":

- **Real-time needs** (order confirmations, fraud checks): event-driven architecture, not polling crons.
- **Near-real-time** (inventory sync every 5 minutes): acceptable for most ecommerce.
- **Hourly** (report pre-computation, cache warming): good for dashboards.
- **Daily** (data exports, reconciliation, cleanup): batch windows with clear completion signals.
- **Weekly/monthly** (analytics rollups, billing): run during low-traffic windows with explicit retry windows.

The best cron is one you can explain to a teammate in 30 seconds — what it does, when it runs, what happens if it fails, and how to re-run it.
