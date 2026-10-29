---
title: "Unlazy - Completion Gates and Depth Tree Setup"
description: "Unlazy: 9.6K combined installs. A gate ledger and the Depth Tree method that make an agent's completion claim testable by runnable checks."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/unlazy-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "completion discipline", "verification", "task decomposition"]
---

# Unlazy - Setup Guide

**Source:** [leonxlnx/unlazy](https://www.skills.sh/leonxlnx/unlazy) via skills.sh - 9.6K combined installs across 1 indexed listing; snapshot 2026-10-29 (Oct 29 morning sweep)

**GitHub:** [leonxlnx/unlazy](https://github.com/leonxlnx/unlazy) - 4168 stars, MIT License, branch main, last pushed 2026-09-03; one skill at the repository root (`SKILL.md`) backed by a real tree: `references/` with six documents, `templates/` with three templates, `scripts/` with five zero-dependency Node tools, `tests/` with seven regression suites, `agents/openai.yaml`, a `SECURITY.md` threat model and a GitHub Actions workflow

**Category:** Agent completion discipline, gate ledgers and deep-task orchestration instruction sets

**Quality Tier:** 🟡 Beta - the publisher's own repository with a substantial test and CI story and no FAIL verdict, held at yellow by a Snyk warn on the listing, an unreleased version string, and a checker whose whole job is to execute shell code

Unlazy is the most literal answer to agent laziness in the current catalog: it does not argue that an agent should try harder, it makes the definition of done a file that a script can grade. The publisher is the individual maintainer behind the leonxlnx skills on skills.sh, whose public footprint is mostly the taste-skill family of design and frontend skills; unlazy is the same author's tooling skill rather than a design one, and it is the only listing under this name with installs. The repository is not a single markdown file. It ships a strict ledger parser, an advisory linter, a dispatch recorder, an optional Claude Code Stop hook, seven test suites and CI, which is why it reads as engineering documentation more than as a prompt.

The method has four moving parts. First, write the acceptance ledger before implementing: for solo work, copy `templates/gates-leaf.md` to `GATES.md` and state one observable outcome per gate, each with an indented `CHECK:` command and an `EXPECT:` success marker, or a manual gate with neither when no command can decide the outcome. Second, treat `CHECK:` as code: `scripts/gate-check.mjs --status` parses the ledger without executing anything, a normal run prints the resolved command, expectation, working directory, shell and `PATH` and leaves an unapproved oracle unexecuted, and `--approve` is the only mode that crosses into execution. Third, decompose with the Depth Tree in `references/method.md`: layer one is the requested task, splits happen only at real domain, component or verification boundaries, binary splits are optional, each leaf is one coherent deliverable with exact file ownership and its own ledger, and each branch carries integration gates. Fourth, work each leaf in four passes - implement completely, re-read as a domain expert, hunt correctness and evidence defects, then polish until a full pass finds nothing.

Around that sit three modes (solo, orchestrated, parallel) routed from `SKILL.md`, a verification hierarchy of leaf self-check, parent `--reverify`, branch integration and the optional Stop hook, and an honest failure path: a gate that cannot be met gets `ABANDON: <id> <reason>` and turns the run into a visible handoff that exits 1 with `HANDOFF REQUIRED` instead of a green report.

## Installation

The README documents the skills CLI for supported agents, with `-g` for a user-level install and `--all` for every detected agent:

```bash
npx skills add Leonxlnx/unlazy
```

The README also gives manual locations for Claude Code (`~/.claude/skills/unlazy`) and Codex CLI (`~/.codex/skills/unlazy`) and says to clone the repository into the relevant directory. Hermes loads a skill from a named directory, so the predictable route is a directory of that name under the profile, with the whole repository inside it, because `SKILL.md` refers to sibling `references/`, `templates/` and `scripts/` paths and the checker is invoked as `node <skill-dir>/scripts/gate-check.mjs`:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills
git clone https://github.com/leonxlnx/unlazy.git \
  ~/.hermes/profiles/corpusiq/skills/unlazy
```

If you want only the instructions and no enforceable checks, the root file alone is enough to install by hand, and the skill degrades to prose at that point:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/unlazy
curl -sL -o ~/.hermes/profiles/corpusiq/skills/unlazy/SKILL.md \
  https://raw.githubusercontent.com/leonxlnx/unlazy/main/SKILL.md
```

The checker and the optional hook need Node 16 or newer and use no third-party runtime packages, so there is nothing to install for them. The README states that the current source targets `2.1.0` and is not identified as a tagged GitHub release, so pin an exact commit when you need an immutable copy.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| unlazy | 9609 | Completion discipline for long or multi-part work: `GATES.md` with one observable outcome per gate and runnable `CHECK:` and `EXPECT:` pairs, strict parsing that rejects zero-gate or duplicate-id ledgers, `--status` inspection without execution, `--approve` consent, `--reverify` for returned work, the Depth Tree decomposition with per-leaf ledgers and branch integration gates, rolling dispatch with `OWNS:` leases, `gate-lint.mjs` for mechanically weak gates, and terminal `ABANDON:` handoffs that can never print as success. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Most agent failures on long work are not wrong code, they are confident reports about work that was never finished, and this skill is the only catalog entry that turns that claim into a file a script can grade. The `CHECK:` and `EXPECT:` pairing is the useful part for a Hermes builder: a gate is met only when the process exits zero and the expected marker appears in the combined output, so "done" stops being a matter of the agent's tone. The evidence rule closes the obvious loophole, because a checked runnable gate stores a versioned SHA-256 digest of its parsed `CHECK:`, `EXPECT:` and `CWD:` plus an output fingerprint, and evidence that is handwritten, missing or bound to a different definition is stale and unmet until the current definition passes.

The token accounting is where it gets interesting, because `references/token-economy.md` is explicit that the skill is not free. Command execution itself needs no model inference, but the agent still pays context for the command, the returned output, the failure interpretation and the evidence review. The design caps that spend rather than pretending it away: evidence keeps a digest and a byte count instead of raw output or a build log, `SKILL.md` stays limited to the core workflow with method, gate, orchestration and parallel references loaded only for the selected mode, and each leaf receives the shared contract and its own ledger instead of the driver's transcript. The same file also warns against the opposite mistake, telling you not to orchestrate a task that one focused session can implement and verify cleanly, and not to keep a whole build in one context merely to avoid subagent overhead.

The Stop hook deserves a precise reading. The hook itself calls no model, but a block causes another agent continuation, which does consume model work, so the six-block no-progress guard exists to stop a loop that pays per block. For Hermes users the portable pieces are the ledger format, the approval boundary and the four passes; the hook is Claude Code specific.

## Usage

| You say | What happens |
|---|---|
| "/unlazy tree 5 refactor the payment module and verify every migration path" | The skill rereads the request, inventories every independently omittable outcome in `PLAN.md`, builds a tree of leaves with owners and per-leaf ledgers, dispatches only leaves whose dependencies are verified, and re-runs each returned leaf's runnable gates with `--reverify`. |
| "gates" | Before any implementation, `GATES.md` is created from `templates/gates-leaf.md` with one observable outcome per gate, a `CHECK:` and `EXPECT:` for every runnable one, and an explicit handoff for any acceptance constraint that gets no gate. |
| "Show me what the ledger would run" | `node <skill-dir>/scripts/gate-check.mjs --status GATES.md` parses and reports state without executing anything; a normal run prints the resolved command, expectation, `CWD:`, shell and `PATH` and leaves a new oracle unexecuted. |
| "Approve the checks and run them" | `--approve` executes the reviewed oracle, and the gate is met only on exit zero plus an `EXPECT:` match, with automatic evidence bound to the parsed definition digest rather than a pasted log line. |
| "Is that leaf actually done?" | `--reverify` executes every runnable gate including ones already marked complete, and returns a gate to unmet when its oracle no longer passes, which is how a parent checks returned work instead of trusting it. |
| "G3 is impossible, the owner is gone" | Adding `ABANDON: G3 owner unavailable` keeps the gate visible and terminal: the checker prints `HANDOFF REQUIRED`, exits 1, and no parent `ALL MET` can promote an abandoned child. |
| "Is this gate ledger any good?" | `scripts/gate-lint.mjs` reads the ledger without executing it and warns on fixed-output emitters, success vocabulary that failure output also uses, activity titles rather than outcomes, and numbers that nothing measures, with `--strict` turning warnings into a failure. |

## Verification

The raw paths below returned 200 on branch main when this guide was written:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/leonxlnx/unlazy/main/SKILL.md
curl -sL -o /dev/null -w "%{http_code} references/gates.md\n" \
  https://raw.githubusercontent.com/leonxlnx/unlazy/main/references/gates.md
curl -sL -o /dev/null -w "%{http_code} scripts/gate-check.mjs\n" \
  https://raw.githubusercontent.com/leonxlnx/unlazy/main/scripts/gate-check.mjs
```

Read `SKILL.md` first, then `references/gates.md` for the strict format, and skim `SECURITY.md` before you let the checker run anything. After install, confirm the directory, the frontmatter name and the checker are all present, since a `SKILL.md` without `scripts/` is prose only:

```bash
ls ~/.hermes/profiles/corpusiq/skills/unlazy/ \
  ~/.hermes/profiles/corpusiq/skills/unlazy/scripts/gate-check.mjs
head -3 ~/.hermes/profiles/corpusiq/skills/unlazy/SKILL.md
node ~/.hermes/profiles/corpusiq/skills/unlazy/scripts/gate-check.mjs --help
```

If you cloned the repository rather than copying one file, the project's own regression command runs the seven suites and is the fastest way to confirm the tools work on your Node version:

```bash
cd ~/.hermes/profiles/corpusiq/skills/unlazy && npm test
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| unlazy | Pass | Pass | Warn W011 |

One listing was sampled. Gen Agent Trust Hub and Socket both pass it, and Snyk records a warning, code W011, rather than a fail; the pack carries the verdict but not the finding text, so read the finding on the skills.sh security page before production use. What the warning lands on is not ambiguous inside this repository: `scripts/gate-check.mjs` imports `spawn` from `node:child_process` and runs each `CHECK:` through a shell with the checker's permissions and inherited environment, so every ledger is a list of commands that may touch files, network, credentials and developer tools. Nothing here pipes curl to bash; installation is the skills CLI or a clone, and the only settings file the project writes is Claude Code's, through `scripts/install-hooks.mjs`, which is explicit, atomic, backs up an existing settings file and preserves unrelated hooks.

The repository's own boundary is review and approval, not sandboxing, and it says so in `SECURITY.md`. An approval record lives under `~/.unlazy/approved` and is bound to the absolute ledger and gate, the exact command and expectation, the resolved working directory and shell, the timeout, the output and regex limits, the platform and the full inherited `PATH`, so any change to those inputs requires approval again. Approval does not hash the scripts, fixtures or dependencies the command calls, and the definition digest is unkeyed, so it detects structural drift rather than tampering: anyone who can edit a ledger can forge canonical-looking evidence. Review inherited ledgers as source before running them, keep `.unlazy/`, `.unlazy-hook-state.json` and `.claude/settings.local.json` in your ignore rules, and prefer a disposable environment when the ledger came from somewhere you do not trust.

## Limitations

- Snapshot data, verified 2026-10-29: 9609 combined installs across 1 indexed listing; 4168 GitHub stars; MIT License; last pushed 2026-09-03. Counts drift over time.
- The version story is soft. `package.json` says `2.1.0` and the README says the current source targets that version but is not identified as a tagged GitHub release, so a clone gives you whatever main held that day; pin a commit if you need a fixed copy.
- The checker grades only the oracle you declared. `references/gates.md` states plainly that a gate titled "invoices reconcile" with `CHECK: node -e "console.log('ok')"` is syntactically valid and semantically useless, and nothing in the tool can tell that an English title and its command disagree.
- Approvals and evidence are structural, not cryptographic. Neither the approval record nor the definition digest hashes called scripts, fixtures or dependencies, so a changed dependency still runs under the old approval and existing evidence can look current until you run `--reverify`.
- The historical performance numbers are gone by the author's own choice: `references/token-economy.md` says earlier documentation gave exact token and effort ratios from a six-run comparison whose prompts, traces and scoring records are not in the repository, and `references/method.md` retires the v1 claim that each binary split multiplied effort. Treat the method as design history, not a benchmark.
- The name is only unique inside itself. The publisher query behind this snapshot returns 109 rows across all sources, of which exactly one is unlazy; the rest are other leonxlnx repositories and third-party republishes of the author's taste-skill under names such as `leonxlnx-taste-skill` and `taste-skill-leonxlnx`, so read install counts from the single listing and not from the publisher page.
- The Stop hook is Claude Code specific and is not installed by default; on Hermes it is a design reference, not a working enforcement layer.

## Related

- [Agent Architect - Agent System Design Setup](/hermes/skills/catalog/agent-architect-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with three gates, not thirty. A leaf ledger with one gate per real acceptance criterion plus one manual gate for the thing no command can see is enough, and `gate-lint.mjs` will tell you when the ledger has drifted toward activity titles.
- Make `EXPECT:` a success-only marker your script prints after every assertion passes, never a phrase that failure output also contains. The checker matches combined stdout and stderr, so an error message that happens to include the word "passed" is a false green.
- Treat `--status` as the review step and `--reverify` as the audit step. Status never executes; reverify re-runs everything including gates already ticked, which is the only way to catch a gate that was true an hour ago.
- Put the ledgers under version control with the code. `GATES.md` and any `.unlazy/<scope>/` tree are contracts, and the approval records deliberately live outside the repository, so a clone never inherits someone else's execution consent.
- Budget the tokens before you dispatch. Evidence is capped by design, but orchestration is not free: independent leaves need their own contracts and fresh contexts, so run a contained task in one session with a solo ledger and save the tree for work that genuinely splits at integration boundaries.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
