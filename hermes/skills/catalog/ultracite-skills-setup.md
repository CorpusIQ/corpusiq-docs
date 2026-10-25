---
title: "Ultracite - Zero-Config Lint Preset Setup"
description: "Ultracite skill: 11.1K combined installs. One skill that teaches an agent your lint and format setup, then runs check, fix, doctor and upgrade correctly."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ultracite-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "lint", "formatting", "typescript"]
---

# Ultracite - Zero-Config Lint Preset Setup

**Source:** [haydenbleasel/ultracite](https://www.skills.sh/haydenbleasel/ultracite) via skills.sh - 11.1K combined installs across 2 indexed listings; new to this catalog in the Oct 24, 2026 evening sweep

**GitHub:** [haydenbleasel/ultracite](https://github.com/haydenbleasel/ultracite) - 3,352 stars, MIT, last pushed 2026-10-24, branch main, one skill at `skills/ultracite/SKILL.md` in a 4,658 file monorepo

**Category:** Code Quality / Linting and Formatting

**Quality Tier:** 🟢 Production - mature MIT licensed project with an active release cadence, one narrow skill that changes no code by itself, and all three auditors passing

Ultracite is a linting and formatting preset for JavaScript and TypeScript that ships hundreds of rules behind one command. The pitch is that configuration is not a differentiated activity: pick a toolchain, run `ultracite init`, and get a ruleset that a model can also be held to. The project positions itself for agentic development specifically, which is why it ships a skill alongside the CLI.

The skill is the part that matters here. It teaches an agent to detect which of the three supported backends a repository uses by looking for `biome.json`, `eslint.config.*` or `oxlint.config.ts`, to run the right command with the right runner, to pass unknown flags through to the underlying linter, and to diagnose a broken setup with `ultracite doctor`. An agent that has this skill stops inventing ESLint configuration in a repository that uses Biome.

The repository supports three backends rather than one, and the skill names the current recommendation: Oxlint with Oxfmt for speed, Biome for an all-in-one binary, and ESLint with Prettier and Stylelint for the widest plugin ecosystem. That choice is made at `init` time and the skill reads it back from the files that decision produced.

## Installation

The skill is installed through the skills CLI:

```bash
npx skills add haydenbleasel/ultracite
```

The CLI can also install it during project setup, which is usually the cleaner path because the skill and the toolchain arrive together:

```bash
npx ultracite init --install-skill
```

`init` is interactive by default and asks for the formatter and linter, the framework, the editor and the agents, then writes the configuration. For non-interactive or CI use the CLI README documents the flags: `--linter <biome|eslint|oxlint>`, `--pm`, `--editors`, `--agents`, `--frameworks`, `--workspace-framework`, `--js-plugins`, `--type-aware`, `--install-skill`, `--skip-install` and `--yes`.

The runtime commands the skill drives:

```bash
npx ultracite check    # lint without writing changes
npx ultracite fix      # lint and auto-fix
npx ultracite doctor   # verify the setup and catch linter version mismatches
npx ultracite upgrade  # update Ultracite and reinstall the toolchain it supports
```

Use the runner that matches the project (`pnpm exec`, `bunx`, `yarn`); the skill is written to pick the installed Ultracite rather than downloading a second copy, and it notes that `pnpm dlx` and `yarn dlx` fetch the latest release instead.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ultracite | 11,051 | Detecting whether a project uses Ultracite and which backend it picked, then running `init`, `check`, `fix`, `doctor` or `upgrade` correctly and writing code that satisfies the project's ruleset. |

The remaining 1 indexed listing is remotion-best-practices (1 install), which has no directory in the current tree. A separate guide in this catalog covers a Remotion skill suite from a different publisher.

Beyond the commands, the skill carries the code standards the preset enforces, so an agent that would otherwise write in a generic style writes in the style the repository already validates. That includes naming, import ordering, nullable handling and the accessibility rules the preset enables.

## Why This Matters for Hermes Agents

Lint output is where an agent's confidence meets ground truth, and most agents waste that signal. They patch the file until the error text disappears, or they add a disable comment, or they run the wrong linter in a repository that standardized on a different one, and the resulting diff is a fight between a model's habits and a ruleset nobody explained to it.

A skill that knows the backend turns the same signal into a contract. The agent reads which toolchain the project uses before it writes, runs `check` rather than guessing at a command name, and when the setup itself is wrong it reaches for `doctor` instead of editing configuration blindly.

The second gain is in monorepos. Ultracite supports workspace-level framework mapping (`--workspace-framework apps/web=react`), so a repository can hold a React app, a library and a CLI with the right rules in each. An agent without that context applies one flat ruleset and produces plausible, wrong edits in the packages that differ.

The limit is that this is a young skill for a fast moving CLI. Read the SKILL.md once and confirm the flags against the CLI README for the version you installed before you let an agent run `upgrade` unattended.

## Usage

| You say | What happens |
|---|---|
| "Set up linting in this project" | Runs `ultracite init`, walks the interactive choices and writes the config for the backend, framework and agent you picked. |
| "Why is CI failing on lint" | Detects the backend, runs `ultracite check` with the same flags CI uses, and reports the real violations instead of a guess. |
| "Fix the lint errors" | Runs `ultracite fix`, and for anything unfixable it can hand the file to the Claude Code or Codex CLI with `--claude` or `--codex`, re-linting after each repair. |
| "The linter and the config disagree" | Runs `ultracite doctor`, which catches version mismatches between the installed toolchain and what the config expects. |
| "Add the React app to the monorepo rules" | Maps the workspace with `--workspace-framework` so the app gets framework-aware rules while the packages keep theirs. |
| "Upgrade Ultracite" | Runs `ultracite upgrade`, which updates the preset and reinstalls the linter versions it supports rather than leaving a mismatched pair. |
| "Write this component in the house style" | Applies the preset's rules for naming, imports, nullability and accessibility while writing, so the file passes `check` on the first run. |

## Verification

Confirm the skill path on main before installing:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/haydenbleasel/ultracite/main/skills/ultracite/SKILL.md
```

Read the skill body first, since it documents the detection order that determines everything else:

- https://raw.githubusercontent.com/haydenbleasel/ultracite/main/skills/ultracite/SKILL.md

After install, two checks: the skill appears in your agent's skills directory, and `npx ultracite doctor` reports the setup as healthy in a project that already has the preset. In a project without it, `npx ultracite init --skip-install` writes the configuration without touching dependencies, which is the reviewable way to see what the preset would change.

## Security

skills.sh verdicts for sampled skills (verified October 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ultracite | Pass | Pass | Pass |

The skill is instructions plus CLI invocations against a published npm package, so the trust question is the package rather than the skill. The CLI README links a Socket badge for the npm artifact, and the auditors pass on the listing.

Two things to watch operationally. `ultracite fix --claude` and `--codex` hand unfixable files to an external coding CLI that edits them; that is a second agent writing to your tree, so enable it deliberately. And `ultracite upgrade` changes installed tool versions in the project, which belongs in a reviewable commit rather than an unattended session.

## Limitations

- Snapshot data, verified October 24, 2026: 11,052 combined installs across 2 indexed listings; 3,352 GitHub stars; MIT; last pushed 2026-10-24. Counts drift over time.
- The second indexed listing, remotion-best-practices (1 install), has no counterpart in the current tree. This repository ships one skill.
- Three backends are supported and they are not interchangeable: a rule that exists in ESLint may not exist in Oxlint, and the skill cannot invent the difference.
- `init` is interactive by default. Unattended runs need the flag set spelled out, and defaults are not the same as your project's intent.
- The skill is one file with no references folder, so it stays short. Deep rule questions end at the preset's own documentation.
- `--install-skill` requires an `init` run, so projects that already configured Ultracite by hand need the skills CLI path instead.

## Related

- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup)
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)

## Pro Tips

- Run `npx ultracite doctor` before asking an agent to fix lint errors. A version mismatch looks like a rules problem and is not one.
- Install the skill with `--install-skill` during `init`, so the agent learns the toolchain you actually chose instead of the default.
- Pass the file list to `check` and `fix` when you want a scoped diff (`npx ultracite check src/app`); the whole-project run is the default for a reason, but it is slow on a monorepo.
- Keep `--claude` and `--codex` off in CI. They spawn an external agent that edits source, which is the opposite of a deterministic gate.
- Put `npx ultracite check` in the same place your tests run. The skill writes code to pass the rules; a gate that never runs them wastes that work.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
