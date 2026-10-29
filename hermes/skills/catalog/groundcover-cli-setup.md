---
title: "Groundcover CLI - Observability API Setup Guide"
description: "paymog/groundcover-cli: 9.6K combined installs. A Go CLI plus agent skill for Groundcover logs, traces, metrics and k8s queries."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/groundcover-cli-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "observability", "kubernetes", "cli tooling"]
---

# Groundcover CLI - Setup Guide

**Source:** [paymog/groundcover-cli](https://www.skills.sh/paymog/groundcover-cli) via skills.sh - 9.6K combined installs across 1 indexed listing; snapshot 2026-10-29 (Oct 29 morning sweep)

**GitHub:** [paymog/groundcover-cli](https://github.com/paymog/groundcover-cli) - 1 star, MIT License, branch main, last pushed 2026-08-18; the tree is a Go CLI (cmd/groundcover, internal/cli, internal/raw, internal/sdkcmd, internal/config, internal/credstore, internal/body, internal/output) with one skill at skills/groundcover-cli/SKILL.md, a goreleaser config and a test workflow that runs go test ./... on pull requests and pushes to main

**Category:** Observability queries, production triage and Groundcover API operations

**Quality Tier:** 🟡 Beta - single-maintainer Go CLI with real tests, a tagged goreleaser release pipeline and an unusually detailed 512-line skill file, but Gen Agent Trust Hub returns Fail on the one sampled listing and the repository has a single GitHub star, so it is not a green-tier install

groundcover-cli is Paymahn Moghadasian's Go client for the Groundcover observability platform, shipped with an agent skill that documents how to drive it. It uses the official `github.com/groundcover-com/groundcover-sdk-go` (pinned at v1.376.0 in go.mod, Cobra v1.10.1 for the command tree) wherever that SDK has a stable contract, and keeps HAR-derived raw commands for webapp endpoints the SDK does not expose. That split is deliberate and documented: SDK-backed commands are the first choice, and `groundcover raw ...` is the fallback for drilldowns, Prometheus passthrough, Grafana dashboards and billing or RBAC reads. Releases are built by goreleaser on version tags and the README documents a Homebrew tap, a `go install` path and a local build.

The other half of the repository is the skill at `skills/groundcover-cli/SKILL.md`, and it is the reason this listing is worth reading. It covers authentication in detail (a `gcsa_` service-account key of exactly 40 characters, with `gcik_` ingestion keys explicitly called out as the wrong type), stored profiles that keep the key in the OS keyring while metadata lands in `~/.config/groundcover/profiles.yaml`, and the precedence order between flags, environment and profiles. Past auth it carries request-body templates for logs, traces, metrics and k8s, a GCQL quick reference with the footguns marked, ten worked recipes, the dashboard preset layout rules, and a common-issues section written from observed API behaviour rather than from the docs.

## Installation

The README has no skills section, so the CLI is installed the way the README says and the skill is installed through skills.sh or by hand.

```bash
brew tap paymog/tap
brew install groundcover
```

The README notes the formula builds from source, so Homebrew installs a Go toolchain as a build dependency. The two alternatives are:

```bash
go install github.com/paymog/groundcover-cli/cmd/groundcover@latest
go build ./cmd/groundcover
```

For the skill itself, the site-wide skills.sh form is:

```bash
npx skills add paymog/groundcover-cli
```

Because Hermes loads skills from named directories and this one lives at `skills/groundcover-cli/`, the predictable route is to create the directory and fetch the file:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/groundcover-cli
curl -sL -o ~/.hermes/profiles/corpusiq/skills/groundcover-cli/SKILL.md \
  https://raw.githubusercontent.com/paymog/groundcover-cli/main/skills/groundcover-cli/SKILL.md
```

Then authenticate. The simplest setup is the environment, which the README recommends for CI:

```bash
export GROUNDCOVER_API_KEY=gcsa_...
export GROUNDCOVER_BACKEND_ID=groundcover
```

The key has to be a service-account key with the `gcsa_` prefix and exactly 40 characters, otherwise the CLI rejects it with `Invalid token prefix. Expected 'gcsa_'` or `Invalid token length (N, expected 40)`. Base URL defaults to `https://api.groundcover.com` and backend ID defaults to `groundcover`. For day-to-day use, `groundcover auth login` stores the key in the OS keyring and `groundcover auth list` shows which profile is the default.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| groundcover-cli | 9602 | Teaches an agent to drive the `groundcover` binary: SDK-backed CRUD for dashboards, monitors, silences, recurring silences, connected apps, notification routes, api keys, service accounts, ingestion keys, policies, synthetics, secrets, workflows, integrations and pipeline configs, plus raw HAR-derived commands for logs, traces, metrics, Prometheus passthrough, Grafana dashboards, k8s drilldowns and billing or RBAC reads, with auth rules, request-body templates, a GCQL reference, incident triage recipes and a common-issues log. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

An observability platform is one of the few places where an agent can answer a question nobody can answer from the repository, and Groundcover's API surface is wide enough that a model improvising requests will burn turns on 400s. This skill removes that guessing: it names the two surfaces, tells the agent to try the SDK command first, and gives `groundcover raw list <group>` as the discovery move when the SDK has no verb for the endpoint it needs.

The detail that makes it usable is the failure knowledge. The skill records that `logs search` returns a bare JSON array at the root with the human message inside `body` as a JSON string, that `metrics query` takes capitalised fields (`Promql`, `Start`, `End`, `Step`, `QueryType`) and silently ignores lowercase ones, and that an empty `query` returns a 500 with `pipeline cannot be nil`. Those are exactly the mistakes an agent makes on the first attempt.

It also covers the write side, which most observability skills skip. Dashboards carry their entire panel layout in a `.preset` JSON string, updates need `currentRevision` from a fresh `get` or the API fails with an opaque validation error, stat widgets only validate as flat top-level layout entries, and section colours are limited to a small palette. Monitors are YAML rather than JSON, and a successful update returns `{"status":202}` for an asynchronous apply, so the agent has to re-read to confirm.

For a Hermes profile, that turns a recurring class of request into a short, checkable loop: scope the window with `date -u`, search logs, pivot on trace IDs, check metrics for shape, then k8s if the question is whether the workload is running at all. The skill writes that order down as a numbered flow, which is a better default than letting each session rediscover it.

## Usage

| You say | What happens |
|---|---|
| "Why is api erroring in prod right now?" | Scope the last hour, then `groundcover logs search` with a GCQL filter on `service_name` and `level = "error"`, and print timestamp, pod, container and the parsed `body` for each hit. |
| "What is the p99 latency on api over the last 30 minutes?" | Builds a `metrics query` body with `histogram_quantile(0.99, ...)`, `QueryType: "range"` and `Step: "60"`, then reads the result series out of `.data.result`. |
| "Which pods are crashlooping?" | Runs `k8s workloads` with `gcqlFilter: "status != \"Running\""` and filters rows where `restarts > 0`, reporting name, namespace and status. |
| "Silence the ingest monitor for an hour while we deploy" | Looks the monitor up with `monitors list --query 'monitor_name = "ingest"'` (regex on that column returns 400) and creates a silence with `duration_seconds: 3600` and the deploy reason. |
| "Any Warning events in the prod namespace?" | `k8s events-search` over the requested window with `namespace = "prod" AND type = "Warning"`, which surfaces OOMKilled, FailedScheduling and BackOff churn. |
| "Search traces for slow requests, then show me their logs" | `traces search` on `duration_ms > 1000`, takes the top `trace_id` values and re-queries logs with `trace_id = "..."` for each one. |
| "Build me a dashboard deep link with the deployment variable pinned" | Reads the dashboard by `uuid`, parses `.preset` with `fromjson`, encodes the `variables` query parameter and returns an `app.groundcover.com/dashboards?viewId=...` link with every variable explicitly set. |

## Verification

The raw skill path returned 200 on the main branch when this guide was written:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/paymog/groundcover-cli/main/skills/groundcover-cli/SKILL.md
```

Confirm the file landed with its frontmatter intact, then confirm the binary can see credentials:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/groundcover-cli/SKILL.md
head -4 ~/.hermes/profiles/corpusiq/skills/groundcover-cli/SKILL.md
groundcover --help
groundcover auth status
```

The first line of the skill frontmatter must read `name: groundcover-cli`, and `auth status` should print the source it resolved (flag, environment or profile) rather than an empty key. A cheap end-to-end check that exercises auth without writing anything is `groundcover dashboards list`, which returns the dashboard collection for the tenant.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| groundcover-cli | Fail | Warn | Warn W011/W012 |

The single indexed listing, groundcover-cli, fails Gen Agent Trust Hub outright, with Socket at Warn and Snyk at Warn with codes W011 and W012. A FAIL from that auditor is not a stylistic note, and the reason it matters here is scope: installing this pair grants an agent a shell command wrapped around a `gcsa_` service-account key, and that key can read logs, traces, metrics, cluster inventory and Kubernetes events, and can also create, update and delete dashboards, monitors, silences, notification routes, connected apps, api keys, service accounts, policies, integrations, pipelines and workflows in a production tenant. Treat the install as a privileged operator, not a read-only integration.

Before running it, check three things on the skills.sh security pages rather than trusting this guide: what the Trust Hub report actually flags in the 512-line SKILL.md, what the two Snyk codes cover (the pack records W011 and W012 without a rule description, so read the report itself), and whether the key you export is scoped to the least privilege the task needs. Prefer a dedicated service account for the agent over a human key, keep the key in the OS keyring through `groundcover auth login` rather than a shell profile, and decide in advance whether the agent may delete anything at all.

One instruction in the skill deserves its own warning. To mint a Grafana token it tells you to run `sh -c "$(curl -fsSL https://groundcover.com/install.sh)"`, which is a curl-to-bash installer for Groundcover's official CLI. That installer drops a binary at `~/.groundcover/bin/groundcover` and prepends the directory to your PATH, which shadows the CLI this guide installs, and the skill's own advice is to invoke it by full path and then remove the PATH line. If you never need `raw grafana ...` commands, skip that installer entirely.

## Limitations

- Snapshot data, verified 2026-10-29: 9602 combined installs across 1 indexed listing; 1 GitHub star; MIT License; last pushed 2026-08-18. Counts drift over time.
- The distribution and the community do not match: one GitHub star against 9,602 installs on a single indexed listing, while the pack reports five owner rows across all sources, so there is no visible crowd of users filing issues to catch regressions for you.
- This reads as a one-person project. The LICENSE names Paymahn Moghadasian as the sole copyright holder, there is no contributor or governance file in the tree, and the only manifest is the Go module in go.mod plus go.sum, so a pause in maintenance means you pin a version or fork.
- The repository is CLI-first with a skill attached, not a skill collection. The README documents the binary and says nothing about skills, so all agent-facing guidance lives in the one SKILL.md and its install route is the manual directory plus curl shown above.
- The raw surface is HAR-derived: commands were captured from the Groundcover webapp, so they track webapp changes rather than SDK releases, and regenerating them needs a fresh capture through `go run ./scripts/generate-commands.go <har>`. Expect drift after a webapp release.
- Some behaviour is recorded as broken rather than fixed: the skill notes that `metrics query` returned `400 metricsQueryBadRequest` for instant bodies across every shape tried, and recommends a short range query as the workaround. The `monitors` endpoint speaks YAML while dashboards speak JSON, so a single agent needs both body formats.

## Related

- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup)
- [Monitoring Expert - Observability & Monitoring Setup](/hermes/skills/catalog/monitoring-expert-setup)
- [Sentry AI Monitoring - Agent Error Tracking Setup](/hermes/skills/catalog/sentry-ai-monitoring-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Create a dedicated service account for the agent and give it a policy that matches the job. The CLI can manage policies itself with `groundcover policies apply --body-file policy.json`, so the scope can be versioned next to the agent config.
- Keep `groundcover raw list` and `groundcover raw list <group>` in the agent's first moves. The raw tree is the only complete map of the API, and guessing an endpoint name wastes a turn every time.
- For log searches, always give a discriminating term plus a container or pod and a window of minutes, not hours. The skill records that broad queries hit `context deadline exceeded` and recommends `--timeout 120s` rather than a wider window.
- Never edit a dashboard in place. `get` the dashboard, edit `.preset` as a parsed object, re-serialise it to a string, and send it back with the `currentRevision` you just read, because the API fails opaquely when the revision is stale.
- Do not let the model invent request bodies. Hand it the templates from the skill and it will get the capitalised metric fields and the bare-array log response right on the first call.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
