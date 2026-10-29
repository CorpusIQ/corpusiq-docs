---
title: "incident.io CLI - Incident and On-Call API Setup"
description: "incidentio-cli by paymog: 9.3K combined installs. A TypeScript CLI built from incident.io's OpenAPI specs, plus a skill that teaches an agent to drive the API."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/incidentio-cli-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "incident.io", "on-call", "cli automation"]
---

# incident.io CLI - Setup Guide

**Source:** [paymog/incidentio-cli](https://www.skills.sh/paymog/incidentio-cli) via skills.sh - 9.3K combined installs across 1 indexed listing; snapshot 2026-10-29 (Oct 29 morning sweep)

**GitHub:** [paymog/incidentio-cli](https://github.com/paymog/incidentio-cli) - 0 stars, no LICENSE file at the repo root, branch main, last pushed 2026-07-21; one skill at `skills/incidentio-cli/SKILL.md`, backed by a real TypeScript CLI in `src/` (`cli.ts`, `auth/`, `http/`, `codegen/`, `commands/`), one test file and one release workflow

**Category:** Incident management, on-call and status page automation CLIs

**Quality Tier:** 🟡 Beta - a working CLI with a genuine OpenAPI codegen story, held back by a Snyk Fail (W007/W012), 0 GitHub stars, a single maintainer and no LICENSE file at the repository root

incident.io is an incident management platform, and unlike most SaaS tools it publishes a real public API behind Bearer keys. This repository is a command line client for that API, at version 0.6.0, from the individual GitHub account paymog. The interesting part is how the command surface is built. Public commands are not hand-written: a generator reads incident.io's per-tag OpenAPI specs, derives a two-token `<resource> <verb>` name for each operation, collapses the CRUD verb set, and resolves collisions. The SKILL.md names two of those collisions, `catalog-types update-type` against `update-type-schema`, and `heartbeat ping` against `ping-post`, which is the kind of detail that only shows up when someone actually ran the codegen.

The scale claim checks out against the tree. `src/commands/generated.ts` holds 179 public commands, `generated-internal.ts` holds 121 generated dashboard commands and `manual-internal.ts` holds 24 hand-curated ones, which is the "about 324 commands" the SKILL.md advertises, split as 179 public across 53 resources plus 145 internal. The skill itself is a single 29.7 KB file at `skills/incidentio-cli/SKILL.md`. It teaches the binary rather than replacing it: auth, the resource and verb grammar, the bracket query filters that the list endpoints expect, and the flags for path params, query params and request bodies.

Two auth modes are the part worth understanding before install. Most commands take an API key, resolved from `--api-key`, then `$INCIDENT_API_KEY`, then the stored credential, with the key kept at `~/.config/incidentio/creds.json` at mode 600. A second set of commands, marked with a cookie glyph in `incidentio list`, targets the dashboard's internal API at `app.incident.io/api/*`, where incident.io refuses API keys outright and the CLI instead replays an imported browser session. That split is where the security verdicts below come from, and it is why this guide treats the repo as useful but not yet something to switch on unattended.

## Installation

The README documents three install routes for the binary. Homebrew needs no Bun and pulls a prebuilt release artifact:

```bash
brew install paymog/tap/incidentio
```

With Bun present, install straight from GitHub:

```bash
bun install -g github:paymog/incidentio-cli
```

From source, which also gives you the codegen scripts:

```bash
git clone https://github.com/paymog/incidentio-cli
cd incidentio-cli
bun install
bun run build
```

The README also says you can skip the build entirely with `bun run src/cli.ts <command>`. The repo ships its own skill install instructions through the `skills` CLI:

```bash
npx skills add paymog/incidentio-cli --global --yes
```

That CLI writes to a Claude Code skill directory by default (`./.claude/skills/` locally, a global equivalent with `--global`). Hermes loads skills from named directories under its profile, so the predictable route is to create the directory and fetch the file:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/incidentio-cli
curl -sL -o ~/.hermes/profiles/corpusiq/skills/incidentio-cli/SKILL.md \
  https://raw.githubusercontent.com/paymog/incidentio-cli/main/skills/incidentio-cli/SKILL.md
```

Then authenticate once, and check that the binary and the key both behave:

```bash
incidentio auth set <api-key>
incidentio auth status
incidentio list incidents
```

For CI or a one-off call, skip `auth set` and export `INCIDENT_API_KEY` instead. Note that the skill is instructions only. It does not contain the CLI, so nothing works until the binary is on PATH and a key exists.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| incidentio-cli | 9298 | Driving the incident.io API from a shell or an agent: incidents (list, show, create, edit, import a postmortem document), actions, follow-ups, attachments, alerts and alert sources, alert routes including custom-field bindings and catalog navigation expressions, escalations and on-call schedules, catalog types and entries, custom fields, severities, users, teams, heartbeats, and status pages, with bracket query filters and JSON output built for `jq`. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Incident data is one of the few sources an agent can act on where the value is entirely in the freshness and the exact filter. "How many SEV1s did we have last month" is a question an agent can answer from this CLI without a human opening a dashboard, because the list endpoints accept bracket filters such as `status_category[one_of]=live`, `severity[gte]=<sev-id>` and `created_at[date_range]=2026-06-01~2026-06-30`, and the CLI prints pretty JSON that pipes straight into `jq`.

The two-token grammar is what makes this teachable to a model at all. `incidentio list` prints the authoritative command set, `incidentio list incidents` prints every verb for one resource, and the SKILL.md tells the agent to use those two commands instead of guessing a verb. A generated catalogue also means the agent does not have to learn a bespoke subcommand tree that drifts from the vendor's documentation, since the commands come from the vendor's own OpenAPI specs.

The write path is where it gets more interesting and more dangerous. `incidents create`, `alerts resolve`, `follow-ups create` and `alert-routes update` all mutate a shared system that other humans are watching during an outage, so an agent holding this skill needs a scoped key and a confirmation step, not a broad one. The API key's scopes are fixed at creation time, which is a helpful constraint: a read-only key fails loudly with 401 or 403 rather than silently succeeding.

Finally, the escape hatches are the real differentiator for an agent. `--raw` returns the unformatted body, and the `raw` command can hit any path that has not been codified, including internal dashboard endpoints when a cookie session is present. That is powerful for a research loop and entirely inappropriate for an unattended cron, which is the honest boundary to draw with this repository.

## Usage

| You say | What happens |
|---|---|
| "List our live incidents from the last week" | Runs `incidentio incidents list` with `--query 'status_category[one_of]=live'` and a `created_at[date_range]=<start>~<end>` filter computed from `date -u`, then returns the pretty JSON. |
| "Open a SEV2 incident for the checkout outage" | Builds `incidentio incidents create` with a `--body-json` payload carrying `name`, `severity_id` and `visibility`, then confirms with the returned incident id. |
| "Who is on call right now, and is anything escalating" | Runs `incidentio escalations list --query status=active`, then `incidentio escalation-paths list` to see which path and schedule each active escalation belongs to. |
| "Resolve the alert that came in from the payments source" | Looks the alert up with `incidentio alerts list` and `alerts show --id`, then calls `incidentio alerts resolve --id <id>`. |
| "Add a follow-up to that incident with the mitigation we used" | Calls `incidentio follow-ups create` with `incident_id` and `content` in the body, and can attach the external issue with `follow-ups connect-external-issue`. |
| "Is the nightly batch job still heartbeating" | Runs `incidentio heartbeat ping --alert-source-config-id <id>`, the GET ping the platform expects from a healthy job. |
| "Show me every verb the catalog-types resource supports" | Runs `incidentio list catalog-types`, which prints the verbs for that resource, including the collapsed names such as `update-type` and `update-type-schema`. |

## Verification

The raw path below returned 200 on the main branch when this guide was written, so the install command in it is the one to copy:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/paymog/incidentio-cli/main/skills/incidentio-cli/SKILL.md
```

You can also confirm the skill's central claim about its own size without installing anything, by counting the command entries the skill points at:

```bash
curl -sL https://raw.githubusercontent.com/paymog/incidentio-cli/main/src/commands/generated.ts \
  | grep -o '"[A-Z]*"' | wc -l
```

In the cloned tree that count is 179, against 121 generated and 24 hand-written internal commands, which matches the roughly 324 the SKILL.md documents. After installing, confirm the file landed under the Hermes profile and that the frontmatter name matches the directory:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/incidentio-cli/SKILL.md
head -3 ~/.hermes/profiles/corpusiq/skills/incidentio-cli/SKILL.md
```

The frontmatter name is `incidentio-cli`. If the binary is also on PATH, `incidentio auth status` and `incidentio list incidents` are the two commands that prove the install end to end.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| incidentio-cli | Pass | Warn | Fail W007/W012 |

One listing was sampled and it fails. Snyk returns W007 and W012, both high severity in Snyk's agent-scan issue-code reference, and Socket warns while Gen Agent Trust Hub passes. W007 covers insecure credential handling, meaning instructions that have the agent place secret values verbatim into its own output or context. W012 covers an unverifiable external dependency, meaning a skill whose prompts or code are controlled by something fetched at runtime. In this repository the W007 class is visible in the skill text itself: it tells the agent to run `incidentio auth set <api-key>` with a live key, to run `incidentio auth import '<paste curl>'` where the pasted cURL carries the dashboard's session cookies, and to export `INCIDENT_API_KEY` for CI. Every one of those puts a working credential in a chat transcript or a shell history. For W012, the flagged URL is not identified in the snapshot, and the SKILL.md's own external references point at the upstream repository and the platform's API docs, so read the skills.sh security page for the exact finding before trusting the pass on the other two auditors.

The dashboard mode deserves a plain warning. A cookie session is not a scoped API key, it is the ability to act as a logged-in user across the dashboard, including saved views, insights, policies and timelines, and it expires, so a stale one shows up as a 401 rather than as a permission error. Anyone who handles customer incidents for a living should not paste a production session cookie into an agent conversation, and should not give that agent a key with `incidents.create` unless the write path is gated by a human.

The installer itself is clean by the usual standard: Homebrew, a Bun global install from GitHub, or a source build, with no `curl | bash` hook and no postinstall script in `package.json`. The manual skill route fetches a markdown file and writes it to disk, which is inert. The risks here are the credentials the skill asks for and the dashboard session it replays, not a malicious installer.

Until those two findings are cleared or explained, the people who should not install this are: anyone who cannot create a narrow, revocable API key per agent, anyone whose incident.io workspace is production for a regulated customer set, and anyone who needs a license grant to vendor the CLI into an internal toolchain. For a read-only reporting agent on a scoped key, the risk is mostly ordinary supply chain risk, which is still non-trivial at 0 stars.

## Limitations

- Snapshot data, verified 2026-10-29: 9298 combined installs across 1 indexed listing; 0 GitHub stars; no license file at the repo root; last pushed 2026-07-21. Counts drift over time.
- There is no LICENSE file at the repository root and no license field in `package.json`. The repository is therefore unlicensed for redistribution purposes, even though the code is public, which matters before you copy it into an internal skills repository or ship a fork.
- Snyk fails the listing with W007 and W012 and Socket warns. The security section above explains the two classes, but the specific flagged URL for W012 is not in the snapshot, so the finding has to be read on skills.sh rather than inferred from the tree.
- The 0 star count against 9298 installs is the odd number in this pack. Installs and stars measure different things, and whoever is pulling this skill is not starring or forking the repository, so there is effectively no community review layer behind the code.
- Half the advertised surface only works through a replayed browser session, and the SKILL.md teaches that path directly. Those commands break on session expiry, grant more than a scoped key, and are the reason a reviewer should not treat this as a read-only integration.
- The skill is documentation for a binary, not the binary. Nothing in `skills/incidentio-cli/` runs on its own, there is no npm release to install (Homebrew, a Bun GitHub install, or a source build are the three routes), and the only test file, `src/commands/manual-internal.test.ts`, covers the hand-written internal command catalogue rather than the 300 generated commands.

## Related

- [Monitoring Expert - Observability & Monitoring Setup](/hermes/skills/catalog/monitoring-expert-setup)
- [Sentry AI Monitoring - Agent Error Tracking Setup](/hermes/skills/catalog/sentry-ai-monitoring-setup)
- [Linear Integration - Issue & Project Management Setup](/hermes/skills/catalog/linear-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the catalogue, not the docs. `incidentio list` and `incidentio list incidents` are generated from the same specs the commands are, so they cannot drift the way a hand-written reference does, and they cost one call each.
- Set the key's scopes at creation and assume they are permanent, because the SKILL.md says the scope set is fixed afterwards. A key with `incidents.create` is a write credential forever, so make a second read-only key for reporting loops.
- Push the filtering into the API. The bracket filters (`status[one_of]`, `severity[gte]`, `created_at[date_range]`, repeated `mode[one_of]`) are what keep a paginated list from turning into three round trips, and dates are ISO-8601 UTC, so compute them with `date -u`.
- Use `--body-file` for anything bigger than a few fields and `--set a.b=value` for one-off tweaks, rather than fighting shell quoting on a long `--body-json` string. The alert route payloads in the SKILL.md are the case where this saves real time.
- Regenerate rather than edit. `bun run codegen` refetches the per-tag specs and rebuilds `src/commands/generated.ts`, and `bun run codegen:har` rebuilds the internal catalogue, so a hand edit to a generated file disappears on the next release.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
