---
title: "PostHog Instrumentation Skill - Analytics and Feature Flags"
description: "posthog/posthog-for-claude on skills.sh: 2.2K combined installs; one archived skill that edits code to add PostHog events and feature flags."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/posthog-instrumentation-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "posthog", "product analytics", "feature flags", "instrumentation"]
---

# PostHog Instrumentation Skill - Setup Guide

**Source:** [posthog/posthog-for-claude](https://www.skills.sh/posthog/posthog-for-claude) via skills.sh - 2.2K combined installs across 1 indexed listing (2,219 exact); first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 13 stars, no licence declared at the repository level, `main` branch, last pushed 2026-03-05, repository archived, 1 `SKILL.md` at `skills/posthog-instrumentation/` beside 13 slash commands under `commands/`, one subagent under `agents/`, and a `.mcp.json` wiring the PostHog MCP server at `https://mcp.posthog.com/mcp`, 18 files in total
**Category:** Product analytics and instrumentation: event capture, user identification, feature flags and HogQL queries inside an existing codebase
**Quality Tier:** 🟡 Experimental - Pass on all three scanners, but the repository is archived, has no licence declared, and its last push predates the current PostHog SDKs.

This repository is the official PostHog plugin for Claude Code, and its README is now a redirect: it states that the repo has moved to [PostHog/ai-plugin](https://github.com/PostHog/ai-plugin) and that this one is deprecated. GitHub agrees, with `archived: true` and a last push of 2026-03-05. It still carries 2,219 installs on skills.sh against 13 GitHub stars, which is the usual pattern for a package that gets pulled by a CLI rather than found by browsing.

What it contains is small and specific. `skills/posthog-instrumentation/SKILL.md` is 70 lines: a three-step workflow (identify the framework, check for existing PostHog setup, add the appropriate instrumentation), code patterns for JavaScript and TypeScript, Python and React, and four naming and rollout rules. Around it sit 13 command files, one per PostHog surface (flags, experiments, surveys, insights, logs, errors, dashboards, actions, docs, query, search, llm-analytics, workspace), and a single `error-analyzer` agent that prioritizes errors by user impact. The commands are MCP clients rather than skills: `commands/flags.md` calls `feature-flag-get-all` and `create-feature-flag`, and `commands/query.md` calls `query-generate-hogql-from-question` and `query-run`.

## Installation

The README gives one command for the plugin package:

```bash
claude plugin install posthog
```

The skills CLI route installs the skill itself, and its command names the skill explicitly:

```bash
npx skills add https://github.com/posthog/posthog-for-claude --skill posthog-instrumentation
```

A manual install is a clone plus a copy of the one skill directory. The skill lives under `skills/` in this repository, so a bare clone into the skills directory would leave `SKILL.md` two levels too deep:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/posthog/posthog-for-claude /tmp/posthog-for-claude
cp -r /tmp/posthog-for-claude/skills/posthog-instrumentation ~/.claude/skills/
```

The copy also sets the indexed name, because the directory basename becomes the skill name. This skill's frontmatter declares the same string, `posthog-instrumentation`, so the copied directory and the skill name agree.

The plugin package and the CLI route install different things, and the difference is worth knowing before you pick. The plugin carries the `commands/` slash commands, the `agents/error-analyzer.md` subagent and the `.mcp.json` server declaration, none of which the `--skill posthog-instrumentation` flag asks for. If you want the management commands, take the plugin.

For a current install, the successor repository is the better target: the README points at `PostHog/ai-plugin`, and this guide documents this repository because that is the listing the install index carries.

## What It Provides

The threshold for this guide is zero installs, so the single indexed listing appears:

| Skill | Installs | Use For |
|---|---|---|
| posthog-instrumentation | 2,219 | Detecting a project's framework, checking for an existing PostHog setup, then adding event capture, user identification and feature flag checks to source files, with consistent snake_case event naming |

One row clears the zero-install threshold, and no rows fall below it.

The skill's own body is deliberately thin, which is the honest way to describe it: three framework pattern blocks and four best-practice bullets, with no reference directory and no per-framework guide behind it. The heavier material in the repository is the command set. Each of the 13 command files is a short procedure over PostHog MCP tools: `flags.md` walks list, inspect, create, update and delete with a confirmation step before deletion; `query.md` carries HogQL notes (the `events`, `persons`, `sessions` and `groups` tables, and `properties.$property_name` for event properties) and converts a natural language question to HogQL before running it; `error-analyzer.md` fetches errors in parallel and ranks them by users affected before occurrence count.

## Why This Matters for Hermes Agents

Instrumentation is the part of analytics that agents are actually asked to do, and it is the part that goes wrong quietly. A model told to "add analytics" will invent an event taxonomy, place `capture` calls on the wrong side of an async boundary, and mix naming conventions across files. This skill's three steps are the correct order of operations: detect the framework, check what is already installed, then instrument. That second step is the one that matters most, because a codebase with `posthog-js` already initialized will end up with two clients and duplicated events if the agent skips the check.

The use of feature flags is the second reason to have it. The skill pairs `isFeatureEnabled` in code with the flag commands on the management side, which is the shape of a gradual rollout: create the flag, gate the code, then ramp. An agent with only the SDK will write a flag check against a key that was never created, and the branch silently never runs.

The counterweight is real. This file is 70 lines, its patterns were last touched before 2026-03-05, and it has no mechanism for knowing what changed in `posthog-js` or `posthog-python` since then. Use it as a checklist for procedure and for naming discipline, and take the call signatures from the SDK documentation rather than from the snippet.

## Usage

| You say | What happens |
|---|---|
| "Add PostHog to this Next.js app" | Runs the three steps: identifies the framework, looks for an existing PostHog client before adding another, then adds the provider and capture calls from the JavaScript and TypeScript patterns |
| "Track when a user completes checkout" | Adds a capture call with a snake_case event name and properties, following the skill's rule to include relevant properties rather than a bare event |
| "Put the new dashboard behind a flag" | Adds an `isFeatureEnabled` check at the render path, and the `flags` command creates the matching flag in PostHog with a rollout percentage, so the code and the flag exist together |
| "Identify users as soon as they log in" | Adds the identify call with the user id and profile properties at the login handler, which is the skill's "identify users early in their session" rule made concrete |
| "Review recent errors and tell me what to fix first" | The bundled `error-analyzer` agent lists errors, pulls details, groups them by root cause, and ranks critical against high and medium by users affected |
| "How many users signed up last week?" | The `query` command turns the question into HogQL, runs it, and returns the number, using the events and persons tables the command file documents |

## Verification

The skill sits one level down in a `skills/` directory, so the raw path carries both segments. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/posthog/posthog-for-claude/main/skills/posthog-instrumentation/SKILL.md | head -6
```

It should open with frontmatter holding `name: posthog-instrumentation` and a description that starts `Automatically add PostHog analytics instrumentation to code`, and below the delimiter you should see `# PostHog Instrumentation Skill` and a `## When to Use` list. There is no `version`, `license` or `homepage` field in this frontmatter.

Because the repository is archived, confirming that the file has not moved is a cheap sanity check before a plugin install:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/posthog/posthog-for-claude/main/README.md
```

A 200 from that URL should return the redirect notice pointing at `PostHog/ai-plugin`. If it returns something else, the listing and the repository have diverged.

After a manual clone, confirm the skill landed as a directory containing `SKILL.md` rather than as nested files:

```bash
test -f ~/.claude/skills/posthog-instrumentation/SKILL.md && echo ok
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| posthog-instrumentation | Pass | Pass | Pass |

All three scanners return Pass, and the package is defensible on that axis: 18 files, no installer, no shell script, no network client of its own. The only executable surface is the `.mcp.json` declaration, which points the client at `https://mcp.posthog.com/mcp` and takes an override from `POSTHOG_MCP_URL`.

The verdict does not cover the thing that matters most here, which is that this skill works by editing your source files. Its workflow is "add appropriate instrumentation", so the agent writes imports, client initialization, capture calls and flag checks into whichever files it decides are relevant, and it does so with the permissions of the session. Treat it as a code change: run it on a branch, read the diff, and check that event names and properties match a taxonomy you chose rather than one the model invented. The scanners cannot score a skill that produces edits rather than executes commands.

Credentials are the other exposure. The Python pattern in `SKILL.md` initializes the client with `api_key='<ph_project_api_key>'` inline, so an agent following it literally can paste a project key into a file that gets committed, and `posthog.identify(userId, { email })` deliberately ships user identifiers and properties the same way. Pass the key through an environment variable and keep it out of the diff.

Two operational notes. The `query` and `flags` commands call PostHog's MCP server, which means the questions you ask and the project data they return leave your machine. Scope whatever credential you give that server to the single project it needs, and keep the server URL override in `POSTHOG_MCP_URL` pointed at a host you trust. And because the repository is archived, nothing here will be patched: if a command file or the MCP wiring turns out to be unsafe, the fix is a move to `PostHog/ai-plugin`, not an update.

## Limitations

- Snapshot data, verified 2026-11-09: 2,219 combined installs across 1 indexed listing; 13 GitHub stars; no licence declared; last pushed 2026-03-05. Counts drift over time.
- The repository is archived and its README declares it deprecated in favour of `PostHog/ai-plugin`. There is no LICENSE file in the tree and GitHub reports no licence, so no licence is declared at the repository level even though `.claude-plugin/plugin.json` carries a `license: MIT` field. Read that as an intent statement in a manifest, not as a grant.
- The last push was 2026-03-05, roughly eight months before this snapshot. The skill has no version field, no dependency declaration and no way to know what changed in `posthog-js`, `posthog-python` or the React bindings since then, so its three code patterns describe the API shape as of that date. Verify each signature against current SDK docs before shipping it into a codebase.
- Coverage is three stacks: JavaScript and TypeScript, Python, and React. Vue, Svelte, Flutter, Go, Ruby, PHP and the mobile SDKs are not addressed, and an agent asked to instrument one of those will improvise.
- One skill directory, one publish date against 2,219 installs: the number is a pull signal from the CLI and the plugin registry, with no second listing to cross-check it.
- The command set depends on a PostHog MCP server being configured in the client. Without it the 13 commands have nothing to call, and the `npx skills` route does not install those commands in the first place.

## Related

- [Amplitude Agent Skills - Product Analytics Setup](/hermes/skills/catalog/amplitude-agent-skills-setup)
- [ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the "check for existing PostHog setup" step yourself before letting the agent edit anything. One `grep -r "posthog" --include=*.ts` costs a second and prevents a second client, a duplicated pageview stream and a confusing fortnight of double counts.
- Write the event taxonomy before the code. The skill recommends snake_case and properties, but it will invent names per file if you do not hand it a list, and renaming events after a week of data loses the history.
- Keep the identify call at the authentication boundary, not in a component. The skill's "identify early" rule is right, and the login handler is the only place that reliably runs once per session.
- Take the call signatures from the SDK docs and the procedural order from this skill. The file has not changed since 2026-03-05, so its value is the three-step workflow and its naming rules, not the exact arguments.
- If you only want the management side, install the successor plugin instead. `PostHog/ai-plugin` is where the commands and MCP wiring are maintained; this repository is archived and will not receive fixes.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
