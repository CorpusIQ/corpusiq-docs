---
title: scheduled-jobs
description: Operate, debug, and verify recurring agent work — daily audits, inbox monitors, watchdogs, no-agent scripts. Covers the profile vs default-profile split, server-local time semantics, and the discipline that keeps cron from rotting silently.
---

# Scheduled Jobs (Hermes Cron)

Operate and debug a Hermes agent's recurring work — the daily audit email, support-inbox monitor, agent-to-agent watchdogs, vendor sync jobs, end-of-day digests. All of it runs on Hermes cron and the rules here apply to every job in that family.

## Canonical tooling — use it, don't hand-edit jobs.json

Profile-local cron management belongs to two scripts:

| Tool | Purpose |
|---|---|
| `scripts/cron_job_manager.py` | add / list / show / enable / disable / remove / validate. Auto-backups `jobs.json` before every write. Refuses duplicate names, duplicate (script, profile) pairs, and jobs whose scripts don't exist at the resolved path. |
| `scripts/cron_health_watchdog.py` (a recurring job in itself) | Scans profile jobs only. Alerts to your team's status channel via Telegram or Slack with 24h dedup on sustained outages. Silent unless something needs attention. Exits 0 on its own internal failures (no flaky-watchdog noise). |

**Rule:** NEVER write directly to `~/.hermes/cron/jobs.json` or the profile equivalent. Hand-edits lose the auto-backup, bypass the duplicate-name guard, and silently break the in-memory state of the running cron daemon.

## Server-local time, not UTC

This is the single biggest source of confusion in cron scheduling. Hermes cron evaluates schedule expressions in **server-local time**, not UTC. If your dev box is in Arizona (GMT-7 year-round, no DST) and you write `0 13 * * *` expecting 1 PM UTC, the job will fire at 1 PM Arizona time (which is 20:00 UTC).

Confirm via `next_run_at` in the job's status output — it shows the resolved next-fire-time in UTC, so you can compare against your intent.

For a job that should fire at 9 AM Arizona / 16:00 UTC, write `0 9 * * *` and confirm `next_run_at` resolves to 16:00 UTC on the next day matching the day-of-week constraint.

## The profile vs default-profile split

If your Hermes installation has multiple profiles (e.g. `default` + a named profile per workstream), each profile has its OWN `jobs.json` and its OWN cron daemon. Confusing them is a common failure mode:

- The default profile's cron: `~/.hermes/cron/jobs.json`, managed by `hermes -p default gateway`
- A named profile's cron: `~/.hermes/profiles/<name>/cron/jobs.json`, managed by `hermes -p <name> gateway`

**Important:** if you only see one of the two gateways running and you reinstall, you may orphan jobs from the other. Two gateways is the normal state. Verify both are running before assuming a job is dead.

## The "no_agent" cron pattern

Some jobs don't need an LLM at all — they're just scripts that produce a notification when they detect something. Examples:

- Watchdog: memory > 90%, send Telegram alert
- API poller: fetch a status endpoint, alert if degraded
- Build monitor: check CI, post to Slack on failure

For these, set `no_agent: true` in the job definition. The cron daemon will execute the script directly without spinning up an agent loop:

- Stdout from the script becomes the message body
- **Empty stdout = silent** (the watchdog pattern — only notify when there's something to notify about)
- Non-zero exit code triggers an error alert (so a broken watchdog can't fail silently)

When to use `no_agent: true`:
- Recurring script-only pings where the script itself produces the exact message text
- Memory/disk/GPU watchdogs, threshold alerts, heartbeats
- CI notifications, API pollers with a fixed output shape

When to use the default (LLM-driven):
- Anything that needs reasoning — summarize a feed, draft a daily briefing, pick interesting items, rephrase data for a human
- Conditional logic based on content

## In-prompt curl is a trap (use a script instead)

When you're writing a job's prompt and you want it to send a Telegram or Slack message, the natural instinct is to embed a `curl` invocation in the prompt body. **Don't.** Hermes' tool-approval layer may block the in-prompt curl, AND the ticker UX (the "agent is working..." indicator) gets killed when an unapproved tool fires.

Pattern: write a small script (`scripts/post_to_<channel>.sh`) that takes a message as `$1` and handles the curl. Reference the script from the prompt. The script runs through normal `terminal()` invocation, no approval gate, no ticker disruption.

## Reinstalling the gateway

If you ever need to fully reinstall the Hermes cron gateway (e.g. after a system update broke something):

```bash
# Will prompt twice for confirmation
printf "Y\nY\n" | sudo hermes -p default gateway install --system
```

For a named profile, replace `default` with the profile name. Verify both gateways are still running afterwards.

## Status discipline

Every job should write its last result to a status file (`scripts/<job>_status.json` or similar) AND log to your standard log path. The cron daemon tracks `last_status` per job, but that's a coarse "ok / error" — the status file is where the operator looks when they need to diagnose "why did this job report ok but the email never arrived?"

Pattern: structure the status file as `{"timestamp": ..., "summary": ..., "details": {...}}`. The watchdog skill (above) reads these files and surfaces anomalies before they compound.

## Drift detection

A recurring problem with crontabs: jobs that USED to work but silently degraded — the API they call moved endpoints, the script's dependencies got upgraded, the auth token expired. The watchdog catches the loudest failures, but the subtle ones (job runs, exits 0, produces wrong output) need active drift detection.

For any job whose output has a known shape, write a tiny assertion at the end of the script:

```python
result = do_the_work()
assert isinstance(result, dict)
assert "summary" in result
assert len(result["items"]) > 0  # if you expect items every run
```

A failing assertion exits non-zero, the cron watchdog surfaces it, you get a real signal.

## Related

- [api-development](../api-development/) — when your cron job hits a Cloud Run API, the deploy-verification patterns apply
- [honcho-memory-usage](../honcho-memory-usage/) — for cron jobs that need cross-session memory


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*
