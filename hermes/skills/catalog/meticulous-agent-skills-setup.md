---
title: "Meticulous Agent Skills - Visual Regression Testing Setup"
description: "Setup guide for alwaysmeticulous/skills - 66.5K combined installs. Official Meticulous skills for reviewing visual diffs and fixing regressions."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/meticulous-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes skill", "agent skill", "skill setup", "visual regression testing", "frontend testing", "meticulous"]
---

# Meticulous Agent Skills - Setup Guide

**Source:** [alwaysmeticulous/skills](https://www.skills.sh/alwaysmeticulous/skills) via skills.sh - 66.5K combined installs across 23 indexed listings; first seen Oct 9, 2026 (evening sweep)
**GitHub:** [alwaysmeticulous/skills](https://github.com/alwaysmeticulous/skills) (10 stars, ISC license; very active - pushed Oct 9, 2026; 10 skills under `skills/`)
**Category:** Visual Regression Testing / Frontend QA / CI
**Quality Tier:** 🟢 Production - official Meticulous org (meticulous.ai visual regression platform), ISC license, very active (pushed Oct 9, 2026); 66.5K combined installs across 23 indexed listings; sampled verdicts Pass with two single-Warns

Meticulous is the automated visual regression testing platform for web frontends, and this repository is its official agent skills collection. Ten skills teach AI coding assistants (Cursor, Claude Code, and Codex among them) to use the platform: review test runs, investigate replays, debug visual diffs, and drive the full change-verification loop. The suite covers the whole workflow - run a test run after a frontend change, review the diffs against the PR description, classify each change as intended or unintended, and fix the diffs a reviewer has rejected - and it is very actively maintained; the repository was pushed the same day as this snapshot.

Around the core review loop sit specialized workflows: `meticulous-zero-diff-task` for work where the UI must not change at all (dependency upgrades, refactors, migrations), `meticulous-increase-coverage` for tracing under-covered code back to real UI actions and validating the fix with recorded sessions, `meticulous-simulate-and-diff` for session simulations against a live URL with pixel and HTML diffs against a base replay, and `meticulous-use-session-data` for downloading user flows and network mocks for local testing. The repository ships as a Claude Code plugin and a Codex plugin that both auto-connect the hosted Meticulous MCP server.

---

## Installation

```bash
# 1. Install/update the Meticulous CLI
npm install --global @alwaysmeticulous/cli@latest

# 2. Authenticate (opens a browser to sign in and pick a default project)
meticulous auth login

# 3. Install the skills into your project
npx skills add alwaysmeticulous/skills --skill "*" --agent claude-code --agent codex --agent cursor -y
```

Claude Code plugin (installs all skills and connects the hosted MCP server):

```text
/plugin marketplace add alwaysmeticulous/skills
/plugin install meticulous@meticulous
```

Then type `/mcp` and choose Authenticate for the Meticulous MCP server; login happens in your browser (skip this if you already authenticated with `meticulous auth login`).

Codex plugin:

```bash
codex plugin marketplace add alwaysmeticulous/skills
codex plugin add meticulous@meticulous
codex mcp login meticulous
```

Cursor users can install from the Cursor Marketplace (Customize → Plugins) once listed; the `npx skills` flow remains the recommended path for multi-agent setups. Full setup instructions live in the Meticulous docs at `app.meticulous.ai/docs/agents/setup`.

## What It Provides

The 10 skills documented in the repository README, with Oct 9, 2026 install counts:

| Skill | Installs | Use For |
|---|---|---|
| meticulous-cli | 8,117 | CLI overview: global options and available commands (supporting skill) |
| meticulous-cli-update | 8,073 | Check that the CLI and skills are installed and up to date, installing as needed; runs at the start of every other Meticulous skill (supporting skill) |
| meticulous-review | 8,066 | Review a completed test run: compare diffs against the PR description and flag likely regressions |
| meticulous-simulate-and-diff | 8,060 | Run a session simulation against a live URL: screenshot quick-check or pixel/HTML diff against a base replay |
| meticulous-iterative-dev | 8,049 | Iterative frontend development with per-step visual validation |
| meticulous-test | 8,028 | Run a test run after a frontend change, then hand off to classification of each visual change as intended or unintended |
| meticulous-use-session-data | 8,008 | Download structured session data (user flows and network mocks) for local testing |
| meticulous-fix | 4,020 | Fix visual diffs that were reviewed and rejected, following the review comments |
| meticulous-zero-diff-task | 3,994 | End-to-end tasks where no visual diffs are expected (upgrades, refactors, migrations); iterate until the diff is clean, then open a PR |
| meticulous-increase-coverage | 1,910 | Trace under-covered files to real UI actions, record sessions to cover them, validate with a coverage comparison, and propose `.meticulousignore` entries |

The remaining 13 indexed listings (between 5 and 28 installs each) have no counterpart in the repository's current `skills/` tree; names like `meticulous-cli-auth` and `meticulous-cli-schema` read as per-command or earlier alternate entries, so the 10 documented skills above are the ones to install.

## Why This Matters for Hermes Agents

Visual regressions are the failure mode coding agents are worst at: an agent can pass every unit test and still move a button two pixels, break a modal's stacking order, or wreck a layout at one breakpoint. Meticulous attacks that with recorded sessions replayed against every change, and these skills close the loop for agents by handing them the reviewer's workflow: run the tests, read the diffs against what the PR was supposed to change, and draw the line between intended and unintended. The zero-diff pattern is the most interesting primitive for builders - it encodes "the UI must not change" as an executable loop for dependency upgrades, refactors, and migrations, exactly the tasks where agents otherwise break visuals silently. The coverage skill goes further than testing: it traces under-covered code back to real UI actions, records sessions to exercise it, and proposes `.meticulousignore` entries for code that can never execute in a browser. The skills are plain markdown; the moving parts are the vendor's CLI and hosted MCP server. For teams with Meticulous in CI, this turns every agent session into a visual QA session without adding a second vendor. The main cost of entry is that the target project needs to be on the Meticulous platform.

## Usage

| You say | What happens |
|---|---|
| "I changed the checkout button - run the visual tests" | meticulous-test runs a Meticulous test run, then hands off to meticulous-review to classify each change |
| "Review the Meticulous results on this PR" | meticulous-review compares diffs against the PR description and flags probable regressions |
| "The diffs on this run are unintended - fix them" | meticulous-fix implements fixes for the rejected diffs, following the review comments |
| "Upgrade this dependency with zero visual change" | meticulous-zero-diff-task iterates against Meticulous until the diff is clean, then opens a PR |
| "Our coverage for this file is low - find the untested code" | meticulous-increase-coverage traces the file to a real UI action, records a session, and validates the coverage change |
| "Did this change break the signup flow?" | meticulous-simulate-and-diff simulates the session against a live URL and compares pixel and HTML diffs against a base replay |
| "I need the network mocks for this flow" | meticulous-use-session-data downloads user flows and network mocks for local testing |

## Verification

```bash
# Claude Code and skills-directory agents - check the skills landed
ls ~/.claude/skills/ | grep -i meticulous

# Review a skill's SKILL.md straight from GitHub before installing
curl -s https://raw.githubusercontent.com/alwaysmeticulous/skills/main/skills/meticulous-review/SKILL.md | head -20
```

Skills installed via the plugin are namespaced as `/meticulous:<skill-name>`; skills installed via `npx` land in the directory your agent scans.

## Security

skills.sh verdicts for sampled skills (verified Oct 9, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| meticulous-review | Pass | Pass | Warn |
| meticulous-test | Pass | Pass | Pass |
| meticulous-zero-diff-task | Pass | Warn | Pass |

Two of the three sampled skills carry a single Warn each (Snyk on meticulous-review, Socket on meticulous-zero-diff-task); the rest of the sample is clean. The skills drive the `@alwaysmeticulous/cli` npm package and the hosted MCP server at app.meticulous.ai, so the usual supply-chain and vendor-trust considerations apply.

## Limitations

- Works only where the target project uses Meticulous: the skills read test runs, diffs, and session data from the platform, and authentication is required (`meticulous auth login` or the MCP flow).
- The plugin path depends on the hosted MCP server at app.meticulous.ai; there is no offline mode for the auto-connect.
- The CLI and skills are under active development with frequent changes, which is why every Meticulous skill checks versions first via meticulous-cli-update.
- GitHub signals are thin (10 stars): trust rests on the official Meticulous org and the platform's own documentation rather than community history.
- The Cursor marketplace listing may lag the repository; `npx skills` stays the recommended cross-agent path.
- Snapshot data, verified Oct 9, 2026: 66.5K combined skills.sh installs across 23 indexed listings; 10 GitHub stars; ISC; last pushed Oct 9, 2026. Counts drift over time.

## Related

- [Limrun Skills - Cloud iOS & Android Simulator Setup](/hermes/skills/catalog/limrun-skills-setup) - cloud mobile simulators for testing app surfaces beyond the web
- [Modern Web Guidance - Google Chrome Agent Skill Setup](/hermes/skills/catalog/googlechrome-modern-web-guidance-setup) - platform guidance for writing the frontend code that Meticulous verifies
- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup) - accessibility auditing to complement visual regression coverage
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Drive the core loop in order: meticulous-test to run, meticulous-review to classify, meticulous-fix to repair. The handoffs are built in, so ask for the loop rather than a one-shot review.
- For refactors and dependency upgrades, say "the UI must not change" explicitly to trigger the zero-diff pattern - it iterates until the diff is clean instead of guessing when it is done.
- Keep the CLI current: the skills change frequently and check versions on every run, so a stale global CLI is the most common source of friction.
- Read `skills/meticulous-review/SKILL.md` before installing: the workflows are plain markdown and worth skimming to understand the classification rules.
- When increasing coverage, let the skill record a real session: synthetic clicks miss the paths that coverage tracing finds.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
