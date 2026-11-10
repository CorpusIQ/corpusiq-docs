---
title: "PostHog Skills - 293 Product Analytics Agent Skills"
description: "posthog/skills on skills.sh: 10.1K combined installs; generated skills for instrumentation, flags, experiments, HogQL and LLM traces"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/posthog-analytics-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "posthog", "product analytics", "feature flags", "llm observability"]
---

# PostHog Skills - Setup Guide

**Source:** [posthog/skills](https://www.skills.sh/posthog/skills) via skills.sh - 10.1K combined installs across 20 indexed listings (10,120 exact); first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 79 stars, MIT license, `main` branch, last pushed 2026-11-09, 356 `SKILL.md` files among 2,305 blobs, skill directories at `skills/omnibus/<name>/`, README describing four collections (PostHog, team, community and `.meta` skills)
**Category:** Product analytics: instrumentation, session replay, feature flags, experiments, data warehouse and HogQL
**Quality Tier:** 🟡 Solid with caveats - MIT licensed and mostly Pass verdicts, but the sample carries five Socket and three Snyk Warnings, and the index lists 20 of 293 skills.

This is the official PostHog skills collection, and it is generated rather than hand-written: the README states that the PostHog skills are produced by [context-mill](https://github.com/PostHog/context-mill) and regenerated on each release. That explains both the size and the shape. The publisher page claims 293 skills, the skills.sh list renders 20 of them, and the tree carries 356 `SKILL.md` files, which is more than the publisher page claims. The GitHub description is candid about the state of the repository: PostHog skills, under construction.

The 20 indexed listings cluster into four jobs. Instrumentation skills edit a codebase to add capture, flags, logs, errors and LLM tracing. Query skills teach an agent to reach for typed runners and HogQL instead of guessing at SQL. Hygiene skills audit flags and experiments, and clean up the ones that are finished. The remaining listings are diagnostics: why a metric moved, why a recording is missing, which SDKs are stale, and how to read a trace. Most of them assume a PostHog MCP server is available, because the bodies call tools such as `posthog:query-trends` and `posthog:execute-sql` rather than an SDK directly.

## Installation

The skills CLI installs one listing at a time, and the listing pages name the skill explicitly:

```bash
npx skills add https://github.com/posthog/skills --skill querying-posthog-data
```

The README's preferred route is the Claude Code plugin marketplace, which installs a bundle rather than a single skill:

```
/plugin marketplace add PostHog/skills
/plugin install posthog-integration@posthog-skills
/plugin install posthog-feature-flags@posthog-skills
/plugin install posthog-all@posthog-skills
```

`/plugin search posthog` lists what the marketplace exposes if you would rather browse first. A manual install is a copy of the skill directory into the project's skills folder, which is the README's own example:

```bash
cp -r skills/team/customer-success/posthog-debugger .claude/skills/posthog-debugger
```

The two routes are not equivalent. `posthog-all` carries the bundle; `--skill <name>` installs exactly one directory and nothing that sits beside it in the tree. If you want the diagnostics as well as the instrumentation skills, take the bundle.

The skills are clients over PostHog's MCP tooling, so plan for that server or for direct API access alongside the install. A skill that expects `posthog:query-funnel` has nothing to call without it, and the failure is a plausible narrative rather than an error.

## What It Provides

The threshold for this guide is zero installs, so every indexed listing appears below:

| Skill | Installs | Use For |
|---|---|---|
| querying-posthog-data | 817 | Chooses typed query tools over SQL for trends, funnels, retention, paths and lifecycle, and documents HogQL schema, functions and governed metrics. |
| instrument-product-analytics | 774 | Adds product analytics event capture for new features or during PR review, including first-time SDK setup. |
| instrument-integration | 633 | Installs and initializes a PostHog SDK for a framework: package install, provider setup and base configuration. |
| instrument-feature-flags | 564 | Gates new functionality behind PostHog feature flags, with initial SDK setup when none exists. |
| instrument-llm-analytics | 544 | Adds AI observability tracing so LLM generations record token counts, latency and cost. |
| instrument-error-tracking | 528 | Captures exceptions with stack traces and source maps, and sets up the SDK when it is missing. |
| managing-subscriptions | 520 | Creates and schedules insight, dashboard and AI-prompt reports to email, Slack or Teams, with delivery history and pause or resume. |
| instrument-logs | 477 | Adds structured log capture through the OTLP exporter, with meaningful properties on each event. |
| diagnosing-sdk-health | 459 | Audits which PostHog SDKs a project runs, which are out of date and how to upgrade them. |
| exploring-autocapture-events | 457 | Explores $autocapture click data, finds CSS and data-attr selectors, checks uniqueness and builds actions from them. |
| cleaning-up-stale-feature-flags | 454 | Finds finished or abandoned flags and removes the code that checks them when the agent can edit the repo. |
| analyzing-experiment-session-replays | 451 | Compares session replays across experiment variants to explain the behavior differences behind the numbers. |
| auditing-experiments-flags | 450 | Audits experiments and feature flags for configuration errors, staleness and hygiene violations. |
| investigate-metric | 441 | Diagnoses why a metric moved by orchestrating breakdowns, actors, paths, retention and lifecycle queries. |
| skills-store | 435 | Lists, browses and loads shared team skills kept in the PostHog skills store. |
| exploring-llm-evaluations | 429 | Inspects and runs hog, llm_judge and sentiment evaluations against specific generations, with scheduled reports. |
| exploring-llm-traces | 429 | Debugs LLM and agent traces from a trace or session URL, checking tool use, context and token cost. |
| exploring-llm-clusters | 425 | Groups AI traffic into clusters, compares their behavior and computes cost and latency per cluster. |
| creating-experiments | 417 | Guides experiment creation from hypothesis through rollout, bucketing, analytics and a note of which choices were guesses. |
| diagnosing-missing-recordings | 416 | Explains why a session recording is missing: SDK signals, project settings, sampling, triggers, ad blockers and quota. |

All 20 indexed listings clear the zero-install threshold, and none fall outside the table. The page renders only 20 rows by design, so this is the full rendered set rather than the full repository.

Read the table top to bottom and the shape of the suite is clear: seven instrumentation skills, four query and metric-diagnosis skills, four AI observability skills, and a tail of flag hygiene, subscriptions and recording diagnostics. The instrumentation group is the part that changes your repository. Each of those skills carries the same instruction, which is to handle the case where PostHog is not installed yet, and that is the single most useful line in the collection for an agent working in an unfamiliar codebase.

## Why This Matters for Hermes Agents

Analytics work is where an agent can do visible damage without producing an error. An invented event name ships to production and never joins another event in a funnel. A second PostHog client initialized beside an existing one doubles every pageview. A HogQL query that reads `properties.utm_source` instead of `properties.$utm_source` returns empty and looks like a data problem rather than a syntax problem.

This collection treats those as procedure. `instrument-integration` installs the SDK before anything else, `instrument-product-analytics` places capture calls at the right boundary, and `querying-posthog-data` opens by telling the reader to use typed runners for standard analyses and to check `system.information_schema.metrics` for an approved definition before deriving a business measure. That last rule is the one that keeps an agent from inventing its own MRR formula.

The hygiene and diagnostic skills matter for the opposite reason: they remove work. A stale flag audit that ends in a code change, or a metric investigation that walks breakdowns, actors and retention before answering, is a multi-hour human task compressed into a procedure with a defined order.

The caveat is dependency. These are MCP client skills with generated bodies, so their tool names track the PostHog server rather than a stable SDK. When the server renames a tool, the skill text and the server disagree, and the agent will paper over the gap unless you check.

## Usage

| You say | What happens |
|---|---|
| "Add PostHog to this Next.js app" | Instrument integration installs the SDK, sets up the provider and base config, then product analytics adds capture calls at the meaningful user actions |
| "Put the new billing page behind a flag" | Instrument feature flags adds the flag check at the render path, while the flag itself is created in PostHog, a step the skill description does not cover |
| "Which feature flags can I remove?" | Stale flag cleanup lists fully rolled out and abandoned flags, then removes the code that checks them when the agent can edit the repository |
| "Why did signups drop last Tuesday?" | Metric investigation runs breakdowns, actors, paths and lifecycle queries, and reports the segment that moved rather than the aggregate |
| "Why is this session missing a replay?" | Recording diagnosis checks SDK signals, project settings, sampling, triggers, blockers and quota against that session ID |
| "Debug this LLM trace" | LLM traces reads the trace or session URL, checks which tools ran, what context was surfaced and what the call cost |
| "Are our experiments set up correctly?" | Experiment and flag audit checks configuration, staleness and best-practice violations across the project |

## Verification

Each listing resolves to a raw `SKILL.md` one directory below `skills/omnibus/`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/posthog/skills/main/skills/omnibus/querying-posthog-data/SKILL.md | head -5
```

It should open with frontmatter holding `name: querying-posthog-data`, a folded description that begins `Explains how to query PostHog data, defaulting to typed runners`, and below the delimiter a `# Querying data in PostHog` heading. Its bodies reference sibling `references/` files, so a directory with only `SKILL.md` is incomplete.

After an install, confirm the skill landed as a directory holding `SKILL.md`:

```bash
ls -d ~/.claude/skills/*/ | head -20
test -f ~/.claude/skills/querying-posthog-data/SKILL.md && echo ok
```

The plugin route keeps its bundle in the plugin directory, so use the `/plugin` listing for that install and the directory check for the CLI and manual routes.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| querying-posthog-data | Pass | Warn | Pass |
| instrument-product-analytics | Pass | Warn | Pass |
| instrument-integration | Pass | Warn | Pass |
| instrument-feature-flags | Pass | Pass | Pass |
| instrument-llm-analytics | Pass | Pass | Pass |
| instrument-error-tracking | Pass | Pass | Pass |
| managing-subscriptions | Pass | Pass | Pass |
| instrument-logs | Pass | Pass | Pass |
| diagnosing-sdk-health | Pass | Pass | Warn |
| exploring-autocapture-events | Pass | Pass | Pass |
| cleaning-up-stale-feature-flags | Pass | Pass | Pass |
| analyzing-experiment-session-replays | Pass | Pass | Pass |
| auditing-experiments-flags | Pass | Pass | Pass |
| investigate-metric | Pass | Pass | Pass |
| skills-store | Pass | Warn | Warn |
| exploring-llm-evaluations | Pass | Pass | Pass |
| exploring-llm-traces | Pass | Warn | Warn |
| exploring-llm-clusters | Pass | Pass | Pass |
| creating-experiments | Pass | Pass | Pass |
| diagnosing-missing-recordings | Pass | Pass | Pass |

Agent Trust Hub passes all 20 listings, Socket warns on 5 and Snyk on 3. The Socket warnings land on the three highest-installed skills (`querying-posthog-data`, `instrument-product-analytics`, `instrument-integration`) plus `skills-store` and `exploring-llm-traces`; the Snyk warnings are `diagnosing-sdk-health`, `skills-store` and `exploring-llm-traces`. No listing fails a scanner outright, which is why the tier is solid rather than experimental.

The scanner verdicts do not cover the two properties that matter most here. The first is that the instrumentation skills edit source files: they add imports, initialize clients, insert capture calls and write flag checks, all with the permissions of the session. Treat every instrumentation run as a code change, on a branch, with a read of the diff before merge.

The second is data egress. Query, diagnostic and AI observability skills send project questions to the PostHog MCP server, and traces and replays can contain customer identifiers, prompt text and model output. Scope the credential to one project, keep it out of the repository, and decide before the session whether that project's data is allowed to leave the machine in a prompt.

## Limitations

- Snapshot data, verified 2026-11-09: 10,120 combined installs across 20 indexed listings; 79 GitHub stars; MIT license; last pushed 2026-11-09. Counts drift over time.
- The skills.sh source page renders at most 20 listings, while the publisher page describes 293 skills and the tree carries 356 `SKILL.md` files. The install figures here cover a single rendered slice of a generated corpus, not the product.
- The repository describes itself as under construction. Skills are generated by context-mill and regenerated on release, so a skill's body can change without its name or install count changing.
- The README's four collections (PostHog, team, community and `.meta` skills) are broader than the index. Its own manual install example, `skills/team/customer-success/posthog-debugger`, is not among the rendered 20.
- Most listings assume a PostHog MCP server or API access. Without one, the skills describe procedures their tools cannot execute, and the agent will fill the gap with prose.
- The instrumentation skills produce real code changes in your repository and have no rollback of their own. The security scanners score the skill files, not the diff an agent writes while following them.

## Related

- [PostHog Instrumentation Skill - Analytics and Feature Flags](/hermes/skills/catalog/posthog-instrumentation-skill-setup)
- [Amplitude Agent Skills - Product Analytics Setup](/hermes/skills/catalog/amplitude-agent-skills-setup)
- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)

## Pro Tips

- Ask for the plan before the edit. "Which files would you touch to instrument checkout?" costs one turn and surfaces the double-init mistake before it lands in the diff.
- Start with `querying-posthog-data` even if your task is instrumentation. It carries the typed-runner list and the governed-metric rule, which is what stops an agent from writing raw SQL for a funnel that already has a tool.
- Install `posthog-all` rather than a single instrumentation skill. The hygiene and diagnostic skills are what you will want the following week, and the bundle is one command.
- Keep the flag audit and the flag cleanup as separate sessions. One reports, the other edits code, and mixing them means an agent decides which flags are stale and deletes the checks in the same pass.
- Check the MCP server's tool names before a long session. Generated skill bodies lag server changes, and a renamed tool turns a precise procedure into improvisation.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
