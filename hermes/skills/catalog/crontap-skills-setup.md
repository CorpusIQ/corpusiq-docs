---
title: "CronTap Skills - Scheduled Job Setup"
description: "crontap/skills on skills.sh: 12.6K combined installs across 12 listings; schedule HTTP jobs, heartbeats and uptime monitors with retries."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/crontap-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "cron", "scheduling", "monitoring"]
---

# CronTap Skills - Setup Guide

**Source:** [crontap/skills](https://www.skills.sh/crontap/skills) via skills.sh - 12.6K combined installs across 12 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 1 star, MIT licence, last pushed 2026-09-16, 12 SKILL.md directories under skills/
**Category:** Scheduled HTTP work: cron and natural language schedules, timezones, retries and idempotency, dead-man heartbeats and uptime monitoring
**Quality Tier:** 🟢 Production - every sampled audit Pass; MIT; 1 star.

The README is one line: agent skills for managing scheduled HTTP jobs, uptime monitors and heartbeats with Crontap. The repo holds 12 SKILL.md directories, all prefixed `crontap-`, and the canonical source is maintained in the Crontap monorepo rather than here.

Each skill is narrow and operational. A schedule skill creates or updates a recurring HTTP request with cron syntax or plain English, a timezone and headers or JSON bodies. A retry skill covers backoff and idempotency. A heartbeat skill adds a dead-man's switch to a job that may stop running silently. Three skills exist to move an existing schedule: two migrate a Vercel Cron or GitHub Actions `schedule` trigger without moving the endpoint or the logs, and one puts a Supabase Edge Function on an external clock.

## Installation

The README installs the set with the skills CLI:

```bash
npx skills add Crontap/skills
```

That is the whole documented install. The skills then operate on a Crontap account, so the agent needs a working connection before any of the schedule, monitor or heartbeat skills can do real work. The quickstart skill declares `get_account_usage` and `list_timezones` among its tools and points at `https://crontap.com/mcp` as the connection guide.

If you would rather read before installing, the canonical copies live in the Crontap monorepo under `skills/`, and this repo is the synced distribution of them.

## What It Provides

Twelve listings, all above the 500 install threshold.

| Skill | Installs | Use For |
|---|---|---|
| crontap-supabase-edge-function-cron | 1,058 | Scheduling a protected Supabase Edge Function or HTTP-facing RPC through Crontap, with an external clock, retries, history and failure alerts |
| crontap-quickstart | 1,055 | Choosing between schedules, uptime monitors and heartbeats, inspecting account limits and verifying an IANA timezone before changing anything |
| crontap-replace-vercel-cron | 1,054 | Moving a Vercel Cron schedule to Crontap while keeping the protected HTTP route, timezone intent and a rollback path |
| crontap-uptime-monitor | 1,053 | Creating an uptime monitor, tuning its failure threshold, pausing it during deployments and inspecting probe evidence |
| crontap-retries-and-idempotency | 1,053 | Configuring retry policy with backoff and designing the endpoint so repeated requests do not duplicate side effects |
| crontap-heartbeat-for-cron | 1,053 | Adding a dead-man's-switch heartbeat to a recurring job, inspecting check-ins and rotating the secret token |
| crontap-ai-built-apps | 1,052 | Adding recurring HTTP work and liveness monitoring to apps built with Lovable, Bolt, Replit or v0 by exposing a protected endpoint |
| crontap-replace-github-actions-cron | 1,051 | Replacing a GitHub Actions schedule trigger with a Crontap dispatch while keeping the workflow, runner and logs on GitHub |
| crontap-recurring-agent-endpoint | 1,051 | Scheduling an endpoint that starts an application-owned agent workflow, then confirming completion with a heartbeat |
| crontap-natural-language-schedules | 1,051 | Translating plain English timing into a reviewed cron expression and concrete next runs, without creating a schedule |
| crontap-debug-failed-runs | 1,051 | Diagnosing a failed run from saved configuration and retained history, separating scheduler, network, timeout and endpoint failures |
| crontap-schedule-http-job | 1,050 | Creating, updating and verifying recurring HTTP requests with cron or plain English, timezones, headers and JSON bodies through MCP or REST |

No indexed listings fall below the threshold; all 12 appear above.

## Why This Matters for Hermes Agents

A scheduled job is the one part of an agent system that runs while nobody is watching, which makes it the part where silent failure hurts most. The set is built around that: heartbeat, retries and failed-run diagnosis cover three of the twelve skills, and each one assumes the failure mode of a job that stops, duplicates or times out rather than crashes loudly.

The timezone handling is a smaller but more common problem. Cron syntax carries no timezone, so a schedule written for one host drifts by an hour when deployed somewhere else, or silently skips a run on a daylight-saving boundary. The quickstart requires an IANA timezone check before a change, and the natural-language skill produces the next concrete run times so the operator can see the drift before it ships.

The migration skills are the practical entry point for existing systems. If a recurring job already lives in Vercel Cron or a GitHub Actions `schedule` trigger, the endpoint and its authentication already exist; the skill moves only the clock, which keeps the blast radius small.

The idempotency skill addresses the defect that agent-written endpoints most often carry: a handler that charges a card or sends a mail twice because it assumed one invocation. Retries make that assumption false.

For Hermes agents, the transferable idea is the split between the schedule, the check-in and the monitor. Naming them separately forces a decision about what "working" means for each job, instead of treating a 200 response as proof that the work happened.

## Usage

| You say | What happens |
|---|---|
| "Run this endpoint every weekday at 9am Phoenix time" | crontap-schedule-http-job creates the schedule with an explicit timezone and confirms the next runs |
| "Is 9am here the same as 9am in the config?" | crontap-natural-language-schedules shows the cron expression and the concrete next run times without creating anything |
| "Move our Vercel cron to something external" | crontap-replace-vercel-cron keeps the protected route and moves only the clock, with a rollback path |
| "Alert me if this nightly job stops running" | crontap-heartbeat-for-cron adds a dead-man's switch and shows how to rotate its token |
| "This job succeeded but the work happened twice" | crontap-retries-and-idempotency inspects the retry policy and the endpoint's side effects |
| "Watch this endpoint and tell me when it goes down" | crontap-uptime-monitor creates the probe, sets the failure threshold and shows the evidence |
| "Why did last night's run fail?" | crontap-debug-failed-runs separates scheduler, network, timeout and endpoint causes from the retained history |

## Verification

Fetch one skill file and confirm the frontmatter is intact (probed 2026-11-04, HTTP 200):

```bash
curl -fsSL https://raw.githubusercontent.com/crontap/skills/main/skills/crontap-quickstart/SKILL.md | head -12
```

The response should carry `name: crontap-quickstart`, the MIT licence line and the declared tool list. After `npx skills add`, confirm the files landed in the skill directory your harness uses, adjusting the path if it is not `~/.claude`:

```bash
find ~/.claude -name SKILL.md -path '*crontap*' | wc -l
```

Twelve files means the set is complete. Then ask the agent which Crontap resources it can see; if `get_account_usage` and `list_timezones` are unavailable, the account connection is missing rather than the skills.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| crontap-supabase-edge-function-cron | Pass | Pass | Pass |
| crontap-quickstart | Pass | Pass | Pass |
| crontap-replace-vercel-cron | Pass | Pass | Pass |
| crontap-ai-built-apps | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified 2026-11-04: 12,632 combined installs across 12 indexed listings; 1 GitHub star; MIT licence; last pushed 2026-09-16. Counts drift over time.
- The index and the tree agree here: 12 listings against 12 SKILL.md directories under skills/, so there is no hidden fixture or plugin tier inflating either count.
- The skills are clients for a hosted product. Without a Crontap account and a working MCP or REST connection they can describe a schedule but not create one.
- The canonical source is the Crontap monorepo, so this repo is a synced copy and may lag behind the upstream `skills/` directory.
- One GitHub star means very little independent review. The green tier reflects scanner verdicts on four sampled skills, not user reports or production history.
- Install counts sit between 1,050 and 1,058, which is far too tight to read as organic adoption; treat the total as an index artefact rather than a popularity signal.

## Related

- [Cron Design Workflow - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/cron-design-workflow-setup)
- [Supabase Server Skill - Edge Function Auth Setup](/hermes/skills/catalog/supabase-server-skills-setup)
- [Supabase Pentest Skills - 24-Skill Audit Suite](/hermes/skills/catalog/supabase-pentest-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the quickstart skill first on a new account. It checks limits and timezone before anything is created, which prevents the most common first mistake.
- Use natural-language-schedules as a dry run. It returns the cron expression and next runs without touching the account, so a wrong reading of "every other Tuesday" costs nothing.
- Add a heartbeat to any job whose absence is worse than its failure. A five-minute check that never fired is invisible without one.
- Design the endpoint to be idempotent before enabling retries. Retries turn a single bad assumption into duplicated side effects.
- Keep the old schedule until the migrated one has logged a few successful runs, then remove it. Both migration skills are written to preserve that rollback path.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
