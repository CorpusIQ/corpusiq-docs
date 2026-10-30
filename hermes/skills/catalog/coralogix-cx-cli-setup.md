---
title: "Coralogix cx CLI - Observability Agent Skills Setup"
description: "coralogix/cx-cli: 58.2K combined installs across 32 indexed listings. Official skills for Coralogix logs, spans, metrics, alerts, and RUM."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/coralogix-cx-cli-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "observability", "coralogix", "cli"]
---

# Coralogix cx CLI - Setup Guide

**Source:** [coralogix/cx-cli](https://www.skills.sh/coralogix/cx-cli) via skills.sh - 58.2K combined installs across 32 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [coralogix/cx-cli](https://github.com/coralogix/cx-cli) - 233 stars, Apache-2.0, branch master, last pushed 2026-10-29; 19 end-user skill directories under `skills/<name>/SKILL.md` (`cx-telemetry-querying`, `cx-alerts`, `cx-dashboards`, `cx-slos` and others), a shared reference folder at `skills/shared/`, and 4 contributor-only development skills under `.claude/skills/` (`add-command`, `add-skill`, `create-pr`, `run-tests`)

**Category:** Observability and production telemetry querying from the terminal, packaged as a Rust CLI plus a bundled agent skill suite

**Quality Tier:** 🟡 Beta - official Coralogix repository, Apache-2.0, actively developed Rust CLI, but two Snyk Warns (cx-telemetry-querying, coralogix-docs) in the sampled six and a suite that is still on 0.x skill metadata

Coralogix maintains `cx` as its own command line client for the Coralogix observability platform: logs, spans, metrics, RUM, dashboards, alerts, SLOs, cases, cost and retention controls, IAM and data pipeline rules. The repository is not a skill collection that happens to ship a CLI. It is a CLI that ships 19 skill files so a coding agent can drive every one of its 29 top-level commands without memorising DataPrime or PromQL syntax. The README puts the surface at 33 commands across 11 domains, and `CLAUDE.md` lists the same tree grouped as Query, Observe, AI, Detect & Respond, Notifications, Data Pipeline, Cost & Storage, Integrations, Access, Agent and Local.

Two design choices make the suite interesting for agents. First, `cx init` is a single onboarding command that creates a profile, signs you in through the browser with OAuth, installs the agent skills and optionally installs shell completions, so a fresh machine reaches "agent can query production" in one run. Second, the CLI is built for machine consumption rather than for a human reading a table: `cx schema` dumps the entire command tree as JSON so an agent can self-discover capabilities, and `-o toon` returns a token-optimised encoding that renames `metadata`, `labels` and `userData` to `$m`, `$l` and `$d`, strips noisy metadata fields, and spills oversized DataPrime result sets to a temp file instead of the context window.

## Installation

The repository documents three routes. The CLI first, because the skills are useless without it:

```bash
brew install coralogix/tap/cx
```

Cross-platform install script, or Cargo if you already have Rust:

```bash
curl -fsSL https://get.coralogix.dev/cli | sh
cargo install coralogix-cli
```

The README carries a security advisory from October 2026 about compromised intermediate certificate authorities at eMudhra, an industry-wide event rather than a Coralogix one, and asks for `cx` v0.1.28 or later out of caution. Pin at or above that version. Then one onboarding run, which installs the skills as part of setup:

```bash
cx init
```

`cx init` is prompt-free when you spell it out, which is what CI and agent harnesses should use:

```bash
cx init --url https://myteam.app.eu2.coralogix.com --api-key $CX_API_KEY --global-skills
```

To install or update the skills on their own, without going through onboarding:

```bash
cx skills install --global
cx skills install --local --agent claude-code --agent cursor
cx skills install --interactive
```

`cx skills` is a local command with no credentials and no API calls, and `install` is its only subcommand. The CLI wraps the `skills` installer, so the same suite is reachable without `cx` at all:

```bash
npx skills add coralogix/cx-cli/skills                         # all skills
npx skills add coralogix/cx-cli/skills --skill cx-telemetry-querying --skill cx-alerts
npx skills add coralogix/cx-cli/skills -g                      # global
npx skills add coralogix/cx-cli/skills -a claude-code -g -y    # a specific agent, unattended
```

The last form is the skills CLI convention for this layout, and `skills/README.md` in the repository documents it alongside the `cx skills install` path. Node.js is required either way, and a failed skills install never blocks the CLI: inside `cx init` it downgrades to a warning.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| cx-telemetry-querying | 5,090 | Gateway for telemetry investigation: logs, spans, metrics and RUM through DataPrime or PromQL, loading pillar-specific reference files per query type before it writes a query. |
| cx-search-dashboard | 4,173 | Find existing dashboards and widgets by natural-language description or by the fields they query, so an agent checks for a dashboard before building a duplicate. |
| coralogix-docs | 4,019 | Search and fetch official Coralogix product documentation with `cx docs search` and `cx docs fetch`, for how the platform works rather than what the tenant is doing. |
| cx-cli | 3,846 | Cross-cutting behaviour that applies to every `cx` invocation, including update notifications, so the agent stops guessing at version drift. |
| cx-alerts | 3,827 | List, inspect, create, delete, enable, disable and suppress Coralogix alert definitions with the `cx alerts` commands. |
| cx-observability-setup | 3,641 | Onboard a service: saved views and view folders, notification connectors and presets, webhooks and automation actions, integrations and extensions. |
| cx-data-pipeline | 3,608 | Parsing rules, enrichments and custom enrichment tables, Events2Metrics definitions and Prometheus recording rule groups. |
| cx-cost-optimization | 3,579 | Usage and consumption analysis, TCO policies, retention tiers, archive storage and why a bill moved, all from `cx usage`, `cx tco` and `cx retentions`. |
| cx-olly | 3,577 | Talk to Olly, the Coralogix Observability Agent: chat, follow-up questions and retrieval of generated artifacts such as charts and reports. |
| cx-dashboards | 3,519 | Build and deploy a dashboard for a service: discover telemetry, verify every PromQL and DataPrime query live, emit importable JSON, then create or replace it. |
| cx-platform-admin | 3,448 | Access and security work: API keys, roles, scopes, users, groups, IP access rules and audits of who can reach production. |
| cx-cases | 3,206 | Triage Coralogix Cases: acknowledge, assign, resolve, close, re-prioritise, and read the event timeline or notification deliveries. |
| cx-infra | 2,869 | Infrastructure resources: resource types, filterable attributes, lists, health and configuration changes, plus raw per-resource data. |
| cx-slos | 2,758 | List and inspect SLO definitions, check targets and error budgets, and create, update or delete SLOs from JSON. |
| cx-service-catalog | 2,727 | Service Catalog APM entities: services, databases, operations, JVMs and Kubernetes pods, with schema, entity lists and aggregated or timeseries data. |
| cx-ai-center | 2,498 | GenAI application and agent telemetry: behaviour, prompts and responses, quality, guardrails, token cost, evaluations and AI Center configuration. |
| cx-incident-management | 787 | Indexed on skills.sh with no matching directory in the current tree, so there is no SKILL.md to inspect on master; for incident work today the documented path is cx-cases for triage plus cx-alerts for firing alert definitions. |

The remaining 15 indexed listings range from 5 to 421 installs.

## Why This Matters for Hermes Agents

Most observability integrations reach an agent through an MCP server, and that server's tool schemas sit in context on every turn whether or not the agent touches them. This suite takes the other route: one binary on `PATH`, 19 short markdown skills that teach the agent which subcommands to compose, and a `cx schema` call that returns the whole command tree as JSON only when the agent asks for it. For a profile that already carries a lot of tool schemas, that is the cheapest possible way to add production telemetry.

The skill boundaries are drawn by investigation intent rather than by API namespace, and that is what makes routing work. `cx-telemetry-querying` is a gateway that loads a pillar reference (`skills/shared/logs-querying.md`, `metrics-querying.md`, `spans-querying.md`, `rum-querying.md`, `dataprime-reference.md`, `promql-guidelines.md`) before writing a query, so a vague "why is checkout slow" does not turn into a guessed DataPrime expression. `coralogix-docs` is deliberately scoped to product documentation and says so, which keeps documentation lookups from being answered with invented tenant data.

Multi-profile fan-out is the feature that changes what an agent can do rather than how fast it does it. A profile is one region or endpoint plus credentials and a default output format, `-p` selects one explicitly, and a single invocation can run across profiles, which covers the multi-team or multi-region case that the Coralogix UI only exposes one tab at a time. On top of that, `toon` output and the 100 KiB spill threshold (`max_dataprime_direct_output_size`, default `102400` bytes) mean a wide log query returns a file path instead of flooding the transcript.

The governance controls are unusually concrete for a vendor CLI. `read_only = true` in `~/.cx/config.toml`, or `--read-only` per invocation, blocks every write with a named error, and only local commands (`profiles`, `cleanup`, `completions`) are exempt. `allow_risky_commands` gates writes on `iam` and `archive`, and `olly_enabled` turns Olly off. An agent running unattended should be given a read-only profile rather than a prompt telling it to be careful.

## Usage

| You say | What happens |
|---|---|
| "Why is checkout slow in the last hour?" | cx-telemetry-querying loads the pillar references it needs, runs an error rate and latency query through `cx logs` or `cx metrics query`, and reports the shape of the slowdown instead of a raw dump. |
| "Ask Olly why error rates spiked" | cx-olly sends the question with `cx olly ask --agent-to-agent-mode`, then follows up and pulls any chart or report Olly generated. |
| "Is there already a dashboard for the payment service?" | cx-search-dashboard searches dashboards by description and by queried field, and reports matches before cx-dashboards is allowed to build anything new. |
| "Add Coralogix RUM to my React app" | cx-rum-setup creates the RUM key, installs the browser SDK, writes the `CoralogixRum.init` call and verifies that events arrive, rather than stopping at the snippet. |
| "Which services use the most CPU this week?" | cx-profiling pulls top CPU and memory services, filters by pod or label, and can reach a flame graph or hot function list for one service. |
| "Can we cut our log bill without losing errors?" | cx-cost-optimization reads usage and consumption, lists TCO policies and retention tiers, and proposes changes against actual billing units. |
| "Who has access to production?" | cx-platform-admin lists API keys, roles, scopes, users and groups, and reports IP access rules for the account. |

## Verification

Each raw SKILL.md path cited in this guide returned 200 on branch `master` when the guide was written on 2026-10-29:

```bash
for p in skills/cx-telemetry-querying/SKILL.md \
         skills/coralogix-docs/SKILL.md \
         skills/cx-alerts/SKILL.md \
         .claude/skills/add-skill/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/coralogix/cx-cli/master/$p"
done
```

Expect four `200` lines. Review a skill before install with the same URL, for example `https://raw.githubusercontent.com/coralogix/cx-cli/master/skills/cx-telemetry-querying/SKILL.md`: the frontmatter carries `name`, a description written as trigger phrases, and a `metadata.version`, and the body names the exact `cx` subcommands the agent is expected to run. Read those subcommand lists against `cx --help` on the installed binary, because the skill tells the agent to compose commands and a renamed subcommand fails at run time rather than at load time.

After install, confirm the files landed where the agent looks, then confirm the binary resolves and the profile works:

```bash
ls -1 skills/*/SKILL.md | wc -l                     # 19 in the repository tree
ls -1 ~/.claude/skills/ 2>/dev/null | head          # global install target
cx --version
cx profiles list
cx schema | head -40
```

`cx --version` should report v0.1.28 or later for the certificate advisory noted in Installation. The real end-to-end check is a live query: `cx logs 'source logs | limit 10'` returning rows means the profile, endpoint and credentials are all correct, and `cx schema` returning JSON means the agent can discover the command tree without reading documentation.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cx-telemetry-querying | Pass | Pass | Warn |
| cx-search-dashboard | Pass | Pass | Pass |
| coralogix-docs | Pass | Pass | Warn |
| cx-cli | Pass | Pass | Pass |
| cx-alerts | Pass | Pass | Pass |
| dataprime | Pass | Pass | Pass |

Nothing in the sampled six fails, and two of the six carry a Snyk Warn: `cx-telemetry-querying`, the gateway every investigation flows through, and `coralogix-docs`. In practice a warn means Snyk flagged something it did not classify as a failure, and the pack does not include the rule code or finding text, so open the security page for `cx-telemetry-querying` on skills.sh and read the entry before installing on a host that holds production credentials.

The larger risk is not in the markdown. The skills instruct an agent to run a CLI that holds a live Coralogix API key and can write to alerts, dashboards, SLOs, parsing rules, IAM and archive storage. `cx init` leaves `allow_risky_commands` and `olly_enabled` on from the start, and the OAuth login grants the CLI whatever team scopes you approve, so scope the login narrowly, set `read_only = true` or pass `--read-only` for unattended agents, and treat any skill that offers to "create" or "delete" as a write operation that needs a human in the loop.

## Limitations

- Snapshot data, verified 2026-10-29: 58,206 combined installs across 32 indexed listings; 233 GitHub stars; Apache-2.0; last pushed 2026-10-29. Counts drift over time.
- The listing count and the tree disagree in a way that matters. skills.sh indexes 32 listings but the repository holds 23 skill directories: 19 end-user skills under `skills/` and 4 contributor-only skills under `.claude/skills/`. The extra listings are older unprefixed duplicates such as `query-logs`, `dataprime`, `rum` and `metrics-query`, each with 5 to 22 installs, plus `cx-incident-management` with 787 installs, which has no directory and no SKILL.md on master (the raw path returns 404), so prefer the `cx-` prefixed names that still exist in the tree.
- `.claude/skills/` holds contributor tooling, not product skills. `add-command`, `add-skill`, `create-pr` and `run-tests` are marked `internal: true` and exist to help someone develop the repository; installing them gives an agent instructions for editing a codebase it will never see.
- The install examples are ahead of the shipping counts. `skills/README.md` shows an example summary line reading "Installed 14 cx agent skills" while the tree contains 19 end-user skill directories, and `cx-coding-agents` carries `internal: true`, so which skills a given release installs is worth checking with `--interactive` rather than assuming the README number.
- Skills are markdown instructions, not a sandbox. They name real `cx` subcommands, they will happily tell an agent to create or delete platform objects, and the only enforcement is the CLI's own `--read-only` and `allow_risky_commands` settings.
- The suite is on 0.x skill metadata (`metadata.version` of `0.1.0` on most skills, `0.2.1` on `cx-dashboards`), and both the CLI and the skills move quickly, so pin a CLI version if you depend on exact flag behaviour.

## Related

- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup)
- [Langfuse Agent Skills - LLM Observability Setup](/hermes/skills/catalog/langfuse-agent-skills-setup)
- [Sentry Dev Skill - Official Sentry CLI Setup](/hermes/skills/catalog/sentry-dev-skills-setup)
- [ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read `cx schema` instead of the skill when a command fails. It emits the whole command tree as JSON from the installed binary, which is the only source that matches the version on disk.
- Set the profile default output format to `toon` for agent work and keep one `text` profile for reading by eye. `-o toon` renames `metadata`, `labels` and `userData` to `$m`, `$l` and `$d`, and spills result sets over `max_dataprime_direct_output_size` (default `102400` bytes) to a temp file path, which is far cheaper than a 50,000 line log dump in context.
- Give unattended agents `read_only = true` in `~/.cx/config.toml` rather than a prompt instruction. Writes then fail with a named error naming the flag, env var and config key, and the agent can report a clean block instead of half-completing a change.
- Use `cx profiles` plus `-p` for multi-region work instead of re-running `cx init`. A profile is region, credentials and default output format, and fan-out across profiles happens in one invocation, which is the case the Coralogix UI handles one team tab at a time.
- Skip `.claude/skills/` when installing by hand. Those four skills teach an agent how to add commands and open pull requests in this repository, and they are marked internal for that reason.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
