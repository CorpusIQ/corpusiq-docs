---
title: "GrowthBook Skills - Feature Flagging and Experimentation"
description: "growthbook/skills: 1.3K combined installs. GrowthBook's official agent skills for feature flagging, experimentation and product analytics."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/growthbook-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "feature flags", "experimentation", "product analytics"]
---

# GrowthBook Skills - Setup Guide

**Source:** [growthbook/skills](https://www.skills.sh/growthbook/skills) via skills.sh - 1.3K combined installs across 28 indexed listings; first seen Nov 28 2026 (morning sweep)

**GitHub:** [growthbook/skills](https://github.com/growthbook/skills) - 31 stars, MIT license, branch main, last pushed 2026-11-27; four domain skills under `skills/<name>/SKILL.md` with a `.claude-plugin/marketplace.json`, a `.cursor-plugin/plugin.json` and a bundled Node helper (`scripts/gb-call`).

**Category:** Agent skills reference - feature flagging, experimentation and product analytics for the GrowthBook platform

**Quality Tier:** 🟠 Orange - Snyk fails gb-setup and experiments; Warn cells land on feature-flags and analytics (Snyk) and flag-monitoring and flag-cleanup (Socket).

growthbook/skills is the official agent skills repository for GrowthBook, an open source feature flagging and experimentation platform. It packages GrowthBook's feature flagging, experimentation and product analytics workflows as Agent Skills for Claude Code, Cursor and other agentskills.io-compatible tools. The skills call the GrowthBook REST API directly through a bundled Node helper, so no MCP server is required.

The repo ships four skills, one per domain: gb-setup, feature-flags, experiments and analytics. Each is a router that loads a short index and reads only the workflow reference file matching the request, keeping the workflows out of context until they are needed. The 28 indexed listings on skills.sh include those four skills plus the workflow reference files indexed as separate listings. The suite is MIT licensed.

## Installation

The README installs the suite as a Claude Code plugin or through the skills CLI, then walks through API key setup. Node 18+ is required.

Claude Code:

```text
/plugin marketplace add growthbook/skills
/plugin install growthbook@growthbook-skills
```

Cursor, Codex, Warp, Zed and other agentskills.io-compatible agents:

```bash
npx skills add growthbook/skills
```

This installs the skills at project scope. Restart your agent if the skills do not appear immediately.

Configure credentials by running the setup skill:

```text
/growthbook:gb-setup
```

It walks through your API key and, for self-hosted installs, your API and app origins, then validates against the live API and writes `~/.config/growthbook/.env` with `chmod 600`. Every other skill reads that file automatically.

To prefer shell environment variables instead (the skills read env vars first and only consult the file when a var is unset):

```bash
export GB_API_KEY=<your-key>
export GB_API_URL=https://api.your-host
export GB_APP_URL=https://growthbook.your-host
```

Get a Personal Access Token from [app.growthbook.io/account/personal-access-tokens](https://app.growthbook.io/account/personal-access-tokens). The token is tied to your GrowthBook user, so flags and experiments the write skills create are attributed to you.

Verify with:

```text
/growthbook:feature-flags
```

Ask it to list your flags; if configuration is wrong, the error points back at `/growthbook:gb-setup`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gb-setup | 128 | Configure API credentials and the trusted app origin; writes ~/.config/growthbook/.env with chmod 600 and validates against the live API. |
| feature-flags | 85 | The full flag lifecycle: create, search, toggle, target, schedule, ramp, monitor, review, publish and archive flags through draft revisions. |
| experiments | 79 | Design, launch, analyze and stop A/B tests, and search or record durable Learnings across experiments. |
| analytics | 75 | Chart product data, build dashboards, manage the metric catalog and query the warehouse via the Product Analytics Explorer. |

The remaining 24 indexed listings range from 19 to 44 installs. These are the workflow reference files inside the four domain skills, indexed as separate listings on skills.sh.

## Why This Matters for Hermes Agents

This suite is a clean reference for the router pattern: instead of shipping one skill per task, each domain skill is a small router that loads an index and reads only the single workflow reference file matching the request. That keeps dozens of detailed playbooks out of context until an agent actually needs one, which is the discipline a Hermes builder wants when wiring a feature-rich domain into a router without bloating the context window.

The bundled helper is the other pattern worth copying. `scripts/gb-call` is a zero-dependency Node script that centralizes auth, base URL resolution, trusted app-origin handling and error reporting, so every workflow calls one small command instead of re-implementing API plumbing. Each skill directory carries a symlink to it so agents installed via `npx skills install` resolve it relative to the skill.

The security verdicts are a useful calibration too: an official vendor suite can still carry Snyk failures (here gb-setup and experiments), so even a publisher's own repository deserves a skills.sh scan before it enters a production profile.

Finally, the four-skill split maps cleanly onto GrowthBook's own product surface: setup, flags, experiments and analytics. A Hermes agent pointed at a GrowthBook workspace can let the domain routers route, the same way they route for Claude Code and Cursor.

## Usage

| You say | What happens |
|---|---|
| "Set up GrowthBook with my API key" | Uses gb-setup to write and validate credentials in ~/.config/growthbook/.env. |
| "Create a feature flag for the new pricing page" | Uses feature-flags, which reads its flag-create workflow to create the flag as a draft. |
| "Release this flag to 10% of users" | Uses feature-flags to add a rollout rule via flag-targeting, or a staged flag-ramp. |
| "What should we test next?" | Uses experiments to read the experiment-brainstorm workflow, grounded in past stopped-experiment history. |
| "Analyze the results of this A/B test" | Uses experiments to read experiment-analyze: trigger a snapshot, poll, then interpret SRM, lifts, CIs and guardrails. |
| "Chart daily active users by country" | Uses analytics to build a chart in the Product Analytics Explorer. |
| "How many orders did we get last week?" | Uses analytics to run an exploration or fall back to ad-hoc SQL against the warehouse. |

## Verification

Review a skill before installing by fetching its SKILL.md directly. The layout on branch main is `skills/<name>/SKILL.md`:

```bash
curl -sL https://raw.githubusercontent.com/growthbook/skills/main/skills/gb-setup/SKILL.md
```

After a clone, confirm the four skill directories and the plugin manifest:

```bash
git clone --depth 1 https://github.com/growthbook/skills.git /tmp/growthbook-skills
ls /tmp/growthbook-skills/skills/
cat /tmp/growthbook-skills/.claude-plugin/marketplace.json
```

The skills listing should show four directories (analytics, experiments, feature-flags, gb-setup). Each holds a SKILL.md router plus a `references/` directory of workflow files and a `scripts/gb-call` symlink.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gb-setup | Pass | Pass | Fail |
| feature-flags | Pass | Pass | Warn |
| experiments | Pass | Pass | Fail |
| analytics | Pass | Pass | Warn |
| flag-experiment | Pass | Pass | Pass |
| flag-graph | Pass | Pass | Pass |
| experiment-brainstorm | Pass | Pass | Warn |
| experiment-analyze | Pass | Pass | Warn |
| flag-search | Pass | Pass | Pass |
| flag-default-value | Pass | Pass | Pass |
| flag-create | Pass | Pass | Pass |
| flag-prerequisites | Pass | Pass | Pass |
| flag-monitoring | Pass | Warn | Pass |
| flag-cleanup | Pass | Warn | Pass |
| flag-toggle | Pass | Pass | Pass |
| flag-targeting | Pass | Pass | Pass |
| flag-review | Pass | Pass | Pass |
| flag-metadata | Pass | Pass | Pass |
| experiment-design | Pass | Pass | Pass |
| flag-schedule | Pass | Pass | Pass |

This guide is Orange because Snyk fails gb-setup and experiments. The Gen Agent Trust Hub passes all 20 sampled listings; 20 of the 28 indexed listings were sampled.

## Limitations

- Snapshot data, verified 2026-11-28: 1,302 combined installs across 28 indexed listings; 31 GitHub stars; MIT license; last pushed 2026-11-27. Counts drift over time.
- The install index outruns the repo: 28 indexed listings against four skills in the tree, with the workflow reference files indexed as separate listings.
- No bandit workflows yet: the skills target standard A/B tests and identify bandits to hand off to the GrowthBook UI rather than applying fixed-allocation guidance.
- No SDK code generation: flags and experiments are managed through the REST API, not the SDK.
- No silent retries or rate-limit backoff in the helper: GrowthBook is rate-limited at 60 rpm and gb-call surfaces 429s explicitly rather than retrying.
- No datasource creation, and metric analysis tuning inherits org defaults: connect datasources in the GrowthBook UI, and tune conversion windows, capping, priors and risk thresholds there.

## Related

- [LaunchDarkly Agent Skills - Feature Flags & AgentControl Setup](/hermes/skills/catalog/launchdarkly-agent-skills-setup)
- [PostHog Skills](/hermes/skills/catalog/posthog-analytics-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read a domain SKILL.md before installing: each of the four routers loads a short index and reads only the workflow reference file matching the request.
- Prefer environment variables in CI: the skills read env vars first and only consult ~/.config/growthbook/.env when a var is unset, so export GB_API_KEY for one-off overrides.
- Generate a dedicated Personal Access Token for the plugin rather than reusing a personal admin token, so it can be revoked independently.
- Note the helper guardrails: gb-call rejects whitespace and control characters in GB_API_KEY, and gb-setup refuses http:// URLs or URLs carrying a path, query, hash or credentials.
- Because Snyk fails gb-setup and experiments, re-check the skills.sh security pages before pulling the suite into a production profile.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
