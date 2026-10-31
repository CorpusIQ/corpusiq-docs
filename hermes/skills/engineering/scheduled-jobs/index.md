---
title: "scheduled-jobs - CorpusIQ Docs"
description: Operate, debug, and verify recurring agent work  --  daily audits, inbox monitors, watchdogs, no-agent scripts. Covers the one-gateway host model, profile timezone semantics, no-agent script rules, and the discipline that keeps cron from rotting silently.
canonical: "https://www.corpusiq.io/docs/hermes/skills/engineering/scheduled-jobs/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Scheduled Jobs (Hermes Cron)

Operate and debug a Hermes agent's recurring work  --  the daily audit email, support-inbox monitor, agent-to-agent watchdogs, vendor sync jobs, end-of-day digests. All of it runs on Hermes cron and the rules here apply to every job in that family.

## Canonical tooling  --  use it, don't hand-edit jobs.json

Profile-local cron management belongs to two scripts:

| Tool | Purpose |
|---|---|
| `scripts/cron_job_manager.py` | add / list / show / enable / disable / remove / validate. Auto-backups `jobs.json` before every write. Refuses duplicate names, duplicate (script, profile) pairs, and jobs whose scripts don't exist at the resolved path. |
| `scripts/cron_health_watchdog.py` (a recurring job in itself) | Scans profile jobs only. Alerts the team by email (our fleet retired Telegram delivery) with 24h dedup on sustained outages. Silent unless something needs attention. Exits 0 on its own internal failures (no flaky-watchdog noise). |

**Rule:** NEVER write directly to `~/.hermes/cron/jobs.json` or the profile equivalent. Hand-edits lose the auto-backup, bypass the duplicate-name guard, and silently break the in-memory state of the running cron daemon.

## Profile timezone, not UTC

This is the single biggest source of confusion in cron scheduling. A job's schedule expression is read in **your profile's timezone** (`timezone:` in `config.yaml`), which defaults to the host's local time. If your dev box is in Arizona (GMT-7 year-round, no DST) and you write `0 13 * * *` expecting 1 PM UTC, the job fires at 1 PM Arizona time (20:00 UTC).

Pin a zone per job when the profile zone is not the one you mean:

```bash
hermes cron create "0 9 * * 1-5" --timezone America/New_York "US market open brief"
```

The expression is then that zone's wall clock and stays put across that zone's DST changes. Confirm via `next_run_at` in the job's status output: it shows the resolved next-fire-time in UTC, so you can compare it against your intent.

For a job that should fire at 9 AM Arizona / 16:00 UTC, write `0 9 * * *` and confirm `next_run_at` resolves to 16:00 UTC on the next day matching the day-of-week constraint.

## One host gateway, per-profile job stores

Hermes runs **one gateway per host**, and that single gateway serves every profile. Per-profile gateways are no longer a supported topology: each one is a supervisor unit, a scheduler and a set of duplicated bot tokens waiting to collide.

The job definitions themselves stay per profile:

- The default profile's cron: `~/.hermes/cron/jobs.json`
- A named profile's cron: `~/.hermes/profiles/<name>/cron/jobs.json`

If you inherited a host with several profile gateways running, converge it rather than deleting units by hand:

```bash
hermes gateway migrate --dry-run    # prints the plan and any blockers
hermes gateway migrate              # stop + uninstall secondary gateways, restart the host gateway
```

Verify afterwards with `hermes gateway list`: one entry running, the rest shown as not running because the host gateway serves them. A job reporting "dead" is usually a job whose profile the gateway is not serving, not a broken schedule.

## The "no_agent" cron pattern

Some jobs don't need an LLM at all  --  they're just scripts that produce a notification when they detect something. Examples:

- Watchdog: memory > 90%, send Telegram alert
- API poller: fetch a status endpoint, alert if degraded
- Build monitor: check CI, post to Slack on failure

For these, create the job in no-agent mode. The cron daemon executes the script directly without spinning up an agent loop:

```bash
hermes cron create "every 5m" \
  --no-agent \
  --script memory-watchdog.sh \
  --deliver telegram \
  --name "memory-watchdog"
```

- Stdout from the script becomes the message body
- **Empty stdout = silent** (the watchdog pattern  --  only notify when there's something to notify about)
- Non-zero exit code or a timeout triggers an error alert (so a broken watchdog can't fail silently)
- `{"wakeAgent": false}` on the last line is the same silent-tick gate LLM jobs use

`--script` is always a **file**, never a command line: `--script "echo hi"` is refused at creation. The resolved path must stay inside `$HERMES_HOME/scripts/`, so write the logic into a script there and pass the filename. Script subprocesses get a sanitized environment - Hermes-managed provider credentials are not inherited, so a script that needs a token must declare it in the profile `config.yaml` and define the value in that profile's `.env`.

When to use no-agent mode:
- Recurring script-only pings where the script itself produces the exact message text
- Memory/disk/GPU watchdogs, threshold alerts, heartbeats
- CI notifications, API pollers with a fixed output shape

When to use the default (LLM-driven):
- Anything that needs reasoning  --  summarize a feed, draft a daily briefing, pick interesting items, rephrase data for a human
- Conditional logic based on content

## In-prompt curl is a trap (use a script instead)

When you're writing a job's prompt and you want it to send a Telegram or Slack message, the natural instinct is to embed a `curl` invocation in the prompt body. **Don't.** Hermes' tool-approval layer may block the in-prompt curl, AND the ticker UX (the "agent is working..." indicator) gets killed when an unapproved tool fires.

Pattern: write a small script (`scripts/post_to_<channel>.sh`) that takes a message as `$1` and handles the curl. Reference the script from the prompt. The script runs through normal `terminal()` invocation, no approval gate, no ticker disruption.

## Reinstalling the gateway

If a Hermes update or a moved `HERMES_HOME` leaves the host gateway broken, reinstall it rather than starting a second one:

```bash
# Will prompt twice for confirmation
printf "Y\nY\n" | sudo hermes gateway install --system
```

`--system` installs a Linux system-level service that starts at boot; `--force` reinstalls over an existing unit, and `--force-unit-path` repoints a unit that still pins another `HERMES_HOME`. One host gateway serves every profile, so run this once - do not repeat it per profile.

## Status discipline

Every job should write its last result to a status file (`scripts/<job>_status.json` or similar) AND log to your standard log path. The cron daemon tracks `last_status` per job, but that's a coarse "ok / error"  --  the status file is where the operator looks when they need to diagnose "why did this job report ok but the email never arrived?"

Pattern: structure the status file as `{"timestamp": ..., "summary": ..., "details": {...}}`. The watchdog skill (above) reads these files and surfaces anomalies before they compound.

## Drift detection

A recurring problem with crontabs: jobs that USED to work but silently degraded  --  the API they call moved endpoints, the script's dependencies got upgraded, the auth token expired. The watchdog catches the loudest failures, but the subtle ones (job runs, exits 0, produces wrong output) need active drift detection.

For any job whose output has a known shape, write a tiny assertion at the end of the script:

```python
result = do_the_work()
assert isinstance(result, dict)
assert "summary" in result
assert len(result["items"]) > 0  # if you expect items every run
```

A failing assertion exits non-zero, the cron watchdog surfaces it, you get a real signal.

## Related

- [api-development](../api-development/)  --  when your cron job hits a Cloud Run API, the deploy-verification patterns apply
- [honcho-memory-usage](../honcho-memory-usage/)  --  for cron jobs that need cross-session memory

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills)  --  133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
