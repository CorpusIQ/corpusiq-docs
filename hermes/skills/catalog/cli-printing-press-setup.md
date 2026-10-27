---
title: "CLI Printing Press - Agent-Native CLI Generator Setup"
description: "CLI Printing Press: 62.3K combined installs. 20 skills that turn any API into a token-efficient Go CLI, an agent skill and an MCP server."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cli-printing-press-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "cli generation", "api tooling", "go"]
---

# CLI Printing Press - Setup Guide

**Source:** [mvanhorn/cli-printing-press](https://www.skills.sh/mvanhorn/cli-printing-press) via skills.sh - 62.3K combined installs across 20 indexed listings; new to this catalog in the Oct 22, 2026 sweep

**GitHub:** [mvanhorn/cli-printing-press](https://github.com/mvanhorn/cli-printing-press) - 4,847 stars, MIT license, last pushed 2026-10-22, branch main

**Category:** Developer Tooling / API and CLI Generation

**Quality Tier:** 🟡 Beta - MIT, 4,847 stars and pushed the same day as this snapshot, but Socket and Snyk return MEDIUM findings on the research and publish paths (W011 third-party content exposure, W009 direct money access)

CLI Printing Press is a research and generation suite for command line tools. Point it at an API and it studies the competing tools, absorbs their feature set, and writes a ship-ready Go CLI that is designed for AI agents first, with SQLite sync, offline search, and compound insight commands. The same run also produces an agent skill and an MCP server, so one integration lands in every surface an agent uses.

This guide covers installation from the repo README, the behavior of the 20 indexed skills, and how a Hermes agent can drive the suite without leaving the terminal. Installation counts come from the October 22, 2026 sweep of skills.sh.

## Installation

The README installer is downloaded to disk and then executed, rather than piped straight from the network into a shell:

```bash
# Binary plus all Printing Press skills (recommended)
curl -fsSL https://raw.githubusercontent.com/mvanhorn/cli-printing-press/main/scripts/install.sh -o install.sh
bash install.sh

# Skills only, or CLI only
bash install.sh --skills-only
bash install.sh --cli-only

# Install or refresh the skills for Codex instead
bash install.sh --skills-only --agent codex

# Verify
cli-printing-press --version
```

Requires Go 1.26.10 or newer, an agent that supports the skills format, and Node/npm for `npx`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| printing-press | 7,508 | Sets up a new integration, connector, or CLI binding for any API. Wraps or generates a ship-ready Go CLI from an OpenAPI, HAR, or Postman spec through a lean research, generate, build, shipcheck loop. Use when the user asks to build a CLI, wrap an API, add a connector, integrate with a service, or names an API by domain. |
| printing-press-publish | 6,809 | Publishes a generated CLI to the printing-press-library repo. |
| printing-press-polish | 6,758 | Polishes a generated CLI until it passes verification and is publish-ready. Runs diagnostics (dogfood, verify, scorecard, go vet, gosec), fixes verify failures, static-analysis findings, dead code, descriptions, README and MCP tool quality, reports the before and after delta, then offers to publish. |
| printing-press-retro | 6,453 | Runs a retrospective after a printed-CLI run and files findings to improve the Press. Trigger phrases include retro, retrospective, what went wrong, improve the press, post-mortem, lessons learned, and file a retro. Not for printed-CLI polish or a single-CLI fix. |
| printing-press-import | 6,435 | Brings a published CLI from the public library into the internal library so it matches a freshly generated copy: module path reverted, manuscripts placed alongside, ready for polish or emboss. Use when the public library has a CLI that is missing locally, or to recover a broken internal copy. |
| printing-press-reprint | 6,407 | Regenerates an existing printed CLI from scratch under the current Printing Press, carrying prior research, prior novel features, and post-publish hand patches forward as reconciliation context. Pulls the CLI from the public library when it is not local, recommends reuse versus redo of prior research based on age, then hands off to the writing pipeline. |
| printing-press-score | 6,341 | Scores a generated CLI against the Steinberger bar, and compares two CLIs side-by-side. |
| printing-press-output-review | 6,339 | Internal sub-skill: agentic review of a printed CLI's sampled command output for plausibility issues that rule-based checks cannot encode, such as substring-match relevance, format bugs, silent source drops and ranking failures. Invoked by the main printing-press skill at Phase 4.85 and by printing-press-polish during the diagnostic loop. Not for direct user invocation. |
| printing-press-amend | 5,419 | Amends a published CLI from one of two sources: dogfood mode mines the active Claude Code session transcript for friction such as missing flags, hand-rolled API payloads and silent-null returns; direct-input mode takes user asks such as renaming a command, adding commands or feeds, fixing a named bug, or sniffing the source site for new endpoints. Confirms scope, then plans and executes the change. |
| printing-press-catalog | 3,717 | No SKILL.md exists in the current tree for this indexed listing, so there is no documented behavior to summarize. |

The remaining 10 indexed listings range from 12 to 13 installs. They are pp-public-param-golden, pp-printing-press-rich, pp-printing-press-oauth2, pp-printing-press-golden, pp-learn-loop-example, ble-temperature-sensor, ble-session-appliance, ble-opaque-binary, ble-desk-lamp and pp-learn-disabled-example, and they sit far below the threshold for a table row.

## Why This Matters for Hermes Agents

Most agent tool use is expensive because the agent reads prose documentation and then hand-writes HTTP calls. Printing Press attacks that cost at the source: the generated artifact is a Go binary with narrow, discoverable commands, so a Hermes agent spends tokens on arguments instead of on payload construction. Offline search and SQLite sync mean repeated lookups do not require a network round trip per question, and compound insight commands return the joined answer directly rather than a raw record the agent must reassemble.

The suite also produces the MCP server and the agent skill in the same pass, which matters when a workflow has to run in more than one harness. A CLI built once can serve a shell-driven cron job, a Hermes skill invocation, and an MCP client without three separate integrations.

## Usage

After installation, the working loop is conversational. Ask the agent to build a CLI for a named API, or hand it an OpenAPI, HAR, or Postman spec, and the printing-press skill runs research, generation, build, and shipcheck before returning a binary.

- Ask for a CLI in plain language, for example "build a CLI for this API" with the spec attached.
- Run printing-press-polish on the result before publishing; it is the gate that turns a working binary into a publishable one.
- Use printing-press-score to compare a fresh CLI against an older one, or against the Steinberger bar.
- Use printing-press-amend for post-publish fixes, either mined from the session transcript or supplied directly.
- Use printing-press-import and printing-press-reprint to recover or refresh a CLI that has drifted from the library copy.

## Verification

The three anchor skills have SKILL.md files on main, so a cheap install check is to fetch each raw path and expect a 200:

```bash
for s in printing-press printing-press-publish printing-press-polish; do
  curl -sL -o /dev/null -w "%{http_code} $s\n" \
    "https://raw.githubusercontent.com/mvanhorn/cli-printing-press/main/skills/$s/SKILL.md"
done
```

The same paths can be read directly when a behavior question comes up:

- https://raw.githubusercontent.com/mvanhorn/cli-printing-press/main/skills/printing-press/SKILL.md
- https://raw.githubusercontent.com/mvanhorn/cli-printing-press/main/skills/printing-press-publish/SKILL.md
- https://raw.githubusercontent.com/mvanhorn/cli-printing-press/main/skills/printing-press-polish/SKILL.md

Finally, confirm the binary itself with `cli-printing-press --version` after the installer finishes.

## Security

Sampled verdicts from skills.sh, verified October 22, 2026:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| printing-press | Pass | Warn | Warn |
| printing-press-publish | Pass | Warn | Warn |
| printing-press-polish | Pass | Pass | Pass |
| printing-press-retro | Pass | Warn | Pass |
| printing-press-import | Pass | Warn | Warn |

The Snyk findings are the ones to read closely. printing-press returns risk MEDIUM with code W011 (third-party content exposure), printing-press-import returns MEDIUM W011, and printing-press-publish returns MEDIUM with W009 and W011, where W009 covers direct money access. In practice that means the research and publish paths touch untrusted third-party content and, for publish, a credentialed write path. Install into a workspace where the generated CLI is reviewed before it is given live credentials, and keep the publish step on a dedicated token rather than an account-wide one.

## Limitations

- Snapshot data, verified October 22, 2026: 62315 combined installs across 20 indexed listings; 4,847 GitHub stars; license MIT; last pushed 2026-10-22. Counts drift over time.
- The index and the tree do not line up. Seven indexed listings have no SKILL.md in the current tree: printing-press-catalog, pp-public-param-golden, pp-printing-press-rich, pp-printing-press-oauth2, pp-printing-press-golden, pp-learn-loop-example, pp-learn-disabled-example. printing-press-catalog is the notable one, because it is a table-row listing at 3,717 installs with nothing readable behind it.
- Quality gates are mixed rather than clean. Socket and Snyk both return Warn on printing-press and printing-press-publish, with MEDIUM findings on the research and publish paths as described above.
- The install path requires Go 1.26.10 or newer, and `npx` workflows require Node/npm, so the host has to carry a Go toolchain before any of this runs.
- The tier is Beta. The repo was pushed the same day as this snapshot, which is a sign of activity, not of stability.

## Related

- [Reason Machines DevTools Skills - Auto-Generated CLI Tool Skill Farm Setup](/hermes/skills/catalog/reason-machines-devtools-skills-setup)
- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)
- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup)
- [MCP Use Setup - Fullstack MCP Framework for Hermes](/hermes/skills/catalog/mcp-use-setup)

## Pro Tips

- Give the press a real spec when one exists. An OpenAPI or HAR file removes most of the guesswork in the research phase, and the shipped CLI is closer to complete on the first pass.
- Run polish before you benchmark anything. Score on an unpolished CLI measures the generator, not the design.
- Keep the installer on disk and read it once. The README form downloads `install.sh` and then runs it, so the review step is free and worth taking.
- Reuse the retro skill after a painful generation. Its findings are the only feedback path that improves the press rather than the single CLI.
- Treat the generated CLI as the integration point for cron and MCP use. The binary is cheaper to call than the API docs are to read.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
