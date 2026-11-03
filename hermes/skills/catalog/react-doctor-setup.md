---
title: "React Doctor - React Codebase Diagnostics Setup"
description: "millionco/react-doctor: 28.2K combined installs. Seventeen agent skills around a deterministic React scanner that grades codebase health."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/react-doctor-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "react", "diagnostics", "linting", "code quality"]
---

# React Doctor - Setup Guide

**Source:** [millionco/react-doctor](https://www.skills.sh/millionco/react-doctor) via skills.sh - 28.2K combined installs across 18 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [millionco/react-doctor](https://github.com/millionco/react-doctor) - 15,076 stars, a LICENSE file is present and its text is a Modified MIT (the GitHub licence field reads NOASSERTION), branch main, last pushed 2026-11-03; 17 skill directories in two trees, 13 under `.agents/skills/` and 4 under `skills/`, each holding a `SKILL.md`, inside a pnpm and turbo monorepo that also builds the CLI

**Category:** Deterministic React diagnostics for state and effects, performance, architecture, security, accessibility and bundle size, reported as a 0 to 100 health score

**Quality Tier:** 🟡 Yellow - Gen Agent Trust Hub fails the deslop listing and Snyk warns on react-doctor and improve-react, even though the repo ships a licence file and the sampled skills are Markdown wrappers around one CLI

React Doctor is published by Million Software and ships as two things at once: a deterministic scanner you run from a project root, and a set of agent skills that tell a coding agent when to run it and what to do with the result. The README states the premise plainly: "Your agent writes bad React. This catches it". The scanner reports issues in state and effects, performance, architecture, security, accessibility and maintainability, supports React projects built with Next.js, Vite, Astro, TanStack, React Native and Expo, and returns a 0 to 100 health score that an agent can compare before and after a change.

The 17 skills are split by audience, which matters more than the count. Four sit under `skills/` and are the ones a product team installs: `react-doctor` for the scan and triage loop, `improve-react` for a read-only whole-codebase audit, `improve-threejs` for React Three Fiber work, and `performance` for runtime traces. Thirteen sit under `.agents/skills/` and lean toward maintainer tooling for the React Doctor project itself: rule research, rule writing, rule validation, fuzzing, PR parity, benchmark audits and `ship`. Two further indexed listings, animation-best-practices and remotion-best-practices, appear on skills.sh but have no directory in the current checkout.

## Installation

The README documents the CLI route, and the scan and the skill install are separate steps:

```bash
# scan the current project
npx react-doctor@latest

# copy the bundled react-doctor skill into the agents the CLI finds
npx react-doctor@latest install

# scan every pull request in CI
npx react-doctor@latest ci install
```

`install` copies one packaged skill, not all 17. It looks for agent binaries on PATH (`claude`, `codex`, `cursor`, `droid`, `gemini`, `copilot`, `opencode`, `pi`) and writes the skill in copy mode, adding native hooks only for Claude Code and Cursor. Hermes is not in that list, so use the skills.sh CLI or a manual copy:

```bash
npx skills add millionco/react-doctor --skill react-doctor
npx skills add millionco/react-doctor --skill improve-react

git clone --depth 1 https://github.com/millionco/react-doctor.git /tmp/react-doctor
cp -r /tmp/react-doctor/skills/react-doctor ~/.hermes/profiles/corpusiq/skills/
```

Copy the whole directory. `skills/react-doctor/SKILL.md` is 77 lines and routes rule questions to `references/explain.md`; the `.agents/skills/react-doctor` copy is a shorter 56-line variant used by the project's own contributor loop.

Rules and scan settings live in `doctor.config.ts`. With `customRulesOnly: true`, explicit `rules` entries set to `warn` or `error` turn on selected ported rules, while other ported rules and the React Compiler plugin stay off. The CLI collects crash reports and anonymous usage data by default; `--no-telemetry` opts out.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| react-doctor | 20,438 | The main skill: scan, triage and clean up React diagnostics before committing, including the full `/doctor` triage workflow. |
| improve-react | 2,669 | A read-only whole-codebase audit that returns a prioritized plan other agents can execute. |
| deslop | 494 | Simplifying and refining recently modified code while keeping its behaviour. |
| rule-validate | 443 | Checking a new rule before merge: detector correctness, open-source hits, PR parity, changeset. |
| find-similar-functions | 434 | Finding existing JS/TS helpers with truffler before writing another one. |
| rule-research | 427 | Pinning down a rule contract and its evidence before implementation. |
| rule-writing | 421 | Implementing oxlint rules from a validated contract, with adversarial tests. |
| ship | 373 | Taking a branch from done to merge-ready: review, deslop, commit, PR, then babysit. |
| product-thinking | 361 | Checking a public-surface change against the CLI, score, config, JSON schema and Action. |
| writing-guidelines | 345 | Reviewing docs or prose against the project's writing guidelines. |
| improve-threejs | 328 | Three.js and React Three Fiber audits: frame loop, GPU leaks, scene graph, visual defects. |
| rde-eval | 314 | Running a local evals loop on an uncommitted rule change to collect false-positive evidence. |
| fuzz | 269 | Fuzzing rules for crashes, slowness and false positives with @react-doctor/fuzz. |
| performance | 213 | Diagnosing one slow interaction with traces, render outlines and Long Animation Frames. |
| animation-best-practices | 200 | An indexed listing for React animation guidance with no in-tree copy in this checkout. |
| run-parity | 193 | Comparing PR diagnostics against Vercel Sandbox and reporting added and removed findings. |
| benchmark-fp-fn-audit | 160 | An adversarial pass over benchmark output for false positives, false negatives and taxonomy gaps. |
| remotion-best-practices | 119 | An indexed listing for Remotion video guidance with no in-tree copy in this checkout. |

No indexed listings fall below the threshold; all 18 appear above.

The strongest part of `react-doctor` is its command contract. It documents `--verbose` for file and line output, `--scope changed` for issues introduced against the base branch, `--scope contextual` and `--scope lines` for narrower comparisons, `--score` to print only the number, and `design` for a focused UI audit. It also documents baseline mode: save a full `--json` scan, then pass `--baseline base-report.json` to report only new findings, with `--warning-exit-code 123` available for GitLab CI, where errors still return 1.

When the user types `/doctor`, the skill fetches the canonical triage playbook from react.doctor and follows every step: a scan, filter, triage, fix and validate loop that edits the working tree but never commits and never opens a PR. Per-rule prompts are fetched on demand from the same site.

## Why This Matters for Hermes Agents

A number beats an opinion. Most agent code review ends in prose that nobody can diff; this ends in a score an agent can compare across a commit boundary, and the skill states the rule explicitly: if the score dropped, fix the regressions before committing. That turns "I improved the code" into a check.

Baseline mode is what makes the tool livable in an older repository. Scan once, save the JSON, then gate only new findings. Without it, a codebase with hundreds of existing findings is unusable as a pre-commit hook, and agents learn to ignore the output.

Planning is separated from execution. `improve-react` is read-only and produces self-contained implementation plans for other agents or cheaper models, which is a clean handoff shape: one model audits, another applies. The same division of labour shows up in `ship`, which expects a finished branch rather than an investigation.

Install discipline matters more here than in a prose-only pack. Nine of the 13 skills under `.agents/skills/` exist to change React Doctor itself, so giving a product agent triggers like `rule-writing` or `run-parity` invites work nobody asked for. Install `react-doctor` plus `improve-react` and stop.

## Usage

| You say | What happens |
|---|---|
| "Did my last change make the score worse?" | Runs `npx react-doctor@latest --verbose --scope changed` and fixes regressions before the commit. |
| "/doctor" | Fetches the canonical local-triage playbook and runs scan, filter, triage, fix and validate over the working tree. |
| "Audit this codebase and tell me what to fix first" | `improve-react` surveys the repo with scan output as evidence and returns a prioritized audit plus plans, without editing source. |
| "This drag feels slow on the checkout page" | The `performance` skill records a DevTools trace, flashes render outlines, and reports interaction timing and long frames. |
| "Only flag what this branch introduced" | Saves a base report, then re-runs with `--baseline` so unrelated findings stay quiet. |
| "Why is this rule firing, and how do I turn it down?" | Runs `rules explain <rule>`, then the narrowest control into `doctor.config.*`: disable, set, category or ignore-tag. |
| "Ship this branch" | The `ship` skill reviews the diff against AGENTS.md, deslops, commits, opens a PR and follows it until mergeable. |

## Verification

The raw paths below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/millionco/react-doctor/main/skills/react-doctor/SKILL.md

curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/millionco/react-doctor/main/.agents/skills/react-doctor/SKILL.md
```

Then confirm both trees and the frontmatter after a clone:

```bash
git clone --depth 1 https://github.com/millionco/react-doctor.git /tmp/react-doctor
ls -d /tmp/react-doctor/skills/*/ | wc -l
ls -d /tmp/react-doctor/.agents/skills/*/ | wc -l
head -4 /tmp/react-doctor/skills/react-doctor/SKILL.md
```

The counts print 4 and 13, 17 in total, and `head` shows `name: react-doctor` with `version: "1.2.0"`. Finally read the number itself before trusting any comparison:

```bash
cd /path/to/react-app
npx react-doctor@latest --score
```

`--score` prints only the number; the file-and-line detail needs `--verbose`. When you need findings grouped by rule and file, save a full `--json` scan and diff against it with `--baseline`, which is also the cheapest way to see what one commit actually changed.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react-doctor | Pass | Pass | Warn |
| improve-react | Pass | Pass | Warn |
| deslop | Fail | Pass | Pass |

This suite is not prose only, and that is the main thing to weigh. The skills instruct the agent to run `npx react-doctor@latest`, which downloads and executes a package from npm with access to the project tree, and the performance path launches an isolated Chrome profile and records a DevTools trace of a real interaction. The skill text is explicit about the boundary: never ask for cookies or copy a browser profile, treat the trace as sensitive local application data, and never upload it without permission.

Two behaviours deserve a decision rather than a default. The CLI collects crash reports and anonymous usage data, and the README documents `--no-telemetry` as the opt-out. And `/doctor` fetches a Markdown playbook from react.doctor at runtime and follows it step by step, which puts remote instructions inside the agent loop; review or pin that content for repositories that handle credentials.

The licence is also not plain MIT. The LICENSE file calls itself a "Modified MIT License" and adds a permission requirement for two uses: training, fine-tuning or evaluating a model on the code, and reselling it as a paid hosted or managed product whose value derives from it. Reading, modifying and running it internally are unaffected.

## Limitations

- Snapshot data, verified 2026-11-03: 28,201 combined installs across 18 indexed listings; 15,076 GitHub stars; Modified MIT with a LICENSE file present; last pushed 2026-11-03. Counts drift over time.
- Two of the 18 indexed listings, animation-best-practices and remotion-best-practices, have no directory in the checkout, so what skills.sh counts is not exactly what the repository ships.
- Nine of the 13 skills under `.agents/skills/` target contributors to React Doctor itself, and their trigger descriptions read like ordinary review requests, which is how a product agent picks one up by mistake.
- The sampled verdicts are mixed: a Trust Hub fail on deslop and Snyk warns on two of three. The fail reasons are not visible in the pack, so check the security pages before installing into a production profile.
- `install` supports eight agent binaries and Hermes is not one of them, so the native installer path does not exist in this profile; use the skills.sh CLI or a copy.
- Rules change between releases (the repo keeps `docs/rule-retirements.md` and `docs/rule-candidates-backlog.md`), so a score comparison is only fair within one version.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup)
- [shadcn Improve - Codebase Audit to Plan Setup](/hermes/skills/catalog/shadcn-improve-setup)
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Gate on `--score` in a pre-commit hook and keep the full `--verbose` scan for a scheduled job; a full scan on every edit is wasted compute.
- Save one baseline JSON per release branch, then use `--baseline` so only new findings fail the build.
- Pass the same `textComponents`, `rawTextWrapperComponents` and `respectInlineDisables` settings to both scans; the skill says to regenerate the base report after changing them, and a mismatch silently changes the comparison.
- Install `react-doctor` and `improve-react` first. Add a maintainer skill only when you are actually changing a rule.
- For runtime work, measure a production build. The `performance` skill warns that development builds add framework work that distorts render timing.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
