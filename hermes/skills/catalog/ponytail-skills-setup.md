---
title: "Ponytail Skills - Lazy Senior Dev Coding Setup"
description: "Ponytail: 321.6K combined installs. Six skills that make an agent write the smallest complete change, review code and track deferred shortcuts."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ponytail-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-23"
tags: ["hermes skill", "agent skill", "skill setup", "code quality", "yagni", "code review"]
---

# Ponytail Skills - Setup Guide

**Source:** [DietrichGebert/ponytail](https://www.skills.sh/dietrichgebert/ponytail) via skills.sh - 321.6K combined installs across 6 indexed listings; new to this catalog in the Oct 23, 2026 sweep

**GitHub:** [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) - 174,315 stars, MIT license, last pushed 2026-10-18, branch main, six skills under `skills/` mirrored into `.openclaw/skills/`

**Category:** Developer Tooling / Code Quality

**Quality Tier:** 🟢 Production - MIT, 174.3K stars, all six indexed listings pass Gen Agent Trust Hub, Socket and Snyk, CI test and publish workflows in the repo, pushed within a week of this snapshot

Ponytail is a coding mode for an agent, packaged as six skills. Its claim is narrow and testable: the best code is the code never written, so the agent should stop at the first option that fully works rather than build the most general one. The main skill installs a persistent session mode with three intensities, and five companion skills give the agent a review pass, a whole-repo audit, a deferred-shortcut ledger, a usage card and a savings scoreboard.

What makes it worth a catalog entry is the install base. 321.6K combined installs across six listings, on a repository that is nine months old, is the kind of adoption that usually means the mode is being used on real code rather than admired in a README. The rules are plain English instructions, not code, so anything an agent does with them is auditable by reading one file.

## Installation

The repository documents plugin routes for Claude Code and Codex. For Hermes, install the six skills from the repo's `skills/` directory:

```bash
# Hermes Agent, one skill at a time
hermes skills install DietrichGebert/ponytail/ponytail --yes
hermes skills install DietrichGebert/ponytail/ponytail-review --yes
hermes skills install DietrichGebert/ponytail/ponytail-audit --yes
hermes skills install DietrichGebert/ponytail/ponytail-debt --yes
hermes skills install DietrichGebert/ponytail/ponytail-gain --yes
hermes skills install DietrichGebert/ponytail/ponytail-help --yes
```

```text
# Claude Code, as two separate prompts
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

```bash
# Codex
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```

The README also offers an instruction-only route for agents without a plugin system: copy `AGENTS.md` into the project, or point the agent at `skills/ponytail/SKILL.md`. INSTALL.md carries the per-host steps for Copilot, Cursor, OpenCode and Gemini.

Install `ponytail` first. It is the mode itself; the other five are one-shot commands that are only useful once the mode is loaded. If a project only wants the review pass, `ponytail-review` and `ponytail-audit` work standalone.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ponytail | 102,473 | The mode itself. Lazy senior developer behavior for any coding task: smallest complete change, a solution stopped at the first rung that holds, and a reply a busy human reads once. Levels lite, full (default) and ultra, switched with `/ponytail lite`, `/ponytail full`, `/ponytail ultra`, or turned off with `stop ponytail`. |
| ponytail-review | 54,851 | Review of a change in fixed priority order: correct, safe, holds under load, tested, fast, lean. Reads the code the change touches rather than only the diff, and reports each finding in plain English. Triggers on "review this", "review my PR", "is this over-engineered". |
| ponytail-audit | 43,379 | Whole-repository audit as one ranked report: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or split. Changes nothing. Triggers on "audit this codebase", "find bloat". |
| ponytail-help | 40,993 | Reference card for the levels, skills and commands. One-shot display, writes nothing. |
| ponytail-debt | 40,904 | Debt ledger. Collects every `shortcut:` comment, and the older `ponytail:` form, with the ceiling and upgrade path each one names, so a deliberate deferral cannot quietly become permanent. |
| ponytail-gain | 38,998 | Savings scoreboard from the project's own benchmark: code, cost and speed. One-shot display, writes nothing. |

All 6 indexed listings clear the 38,000-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Over-engineering is the default failure of a coding agent, and it is invisible in review because the extra code looks like thoroughness. A Hermes agent asked for a date picker will reach for a library or build a calendar, when the repository already has an input component and the browser already ships a date picker. Ponytail replaces that instinct with an ordered ladder: does it need to exist, is it already here, does the standard library do it, is there a platform feature, is there an installed dependency, can it be one line, and only then write the minimum.

The mode also fixes a subtler problem: the scope of a change. The skill makes the agent list every place the edit must reach, callers, tests, fixtures, config and exports, before writing anything, and then insists the change be finished there. Being lazy about the solution while being complete about the change is the distinction most agents get backwards.

For Hermes specifically the five companion skills map cleanly onto work the agent already does with shell and git: a review pass before a commit, a repository audit before inheriting a codebase, and a `shortcut:` ledger that makes technical debt a file you can read instead of a memory you hope survives.

## Usage

| You say | What happens |
|---|---|
| "Add a date picker to the booking form" | The agent checks for an existing input component and a native platform picker, then follows the ladder. You get the smallest change that works plus one line naming what it skipped. |
| "Review the last commit before I merge" | ponytail-review runs the six-point order and reports findings, including whether every line added is needed. |
| "Audit this repo, I am taking it over" | ponytail-audit returns one ranked report covering correctness, safety, load behavior, untested risky code, slow paths and dead weight. |
| "Why is this service so big, what can I delete?" | The audit answers with a ranked delete, merge and split list rather than a refactor proposal. |
| "What did we defer, and is any of it about to bite?" | ponytail-debt lists every marked shortcut with its ceiling and upgrade path in one ledger. |
| "Use ponytail ultra for this refactor" | The mode also pushes back on parts of the request the need does not justify before building. |

## Verification

Confirm the install targets exist before installing, and read the rules yourself:

```bash
for s in ponytail ponytail-review ponytail-audit ponytail-debt ponytail-gain ponytail-help; do
  curl -sL -o /dev/null -w "%{http_code} $s\n" \
    "https://raw.githubusercontent.com/DietrichGebert/ponytail/main/skills/$s/SKILL.md"
done
```

The six files can also be read directly:

- https://raw.githubusercontent.com/DietrichGebert/ponytail/main/skills/ponytail/SKILL.md
- https://raw.githubusercontent.com/DietrichGebert/ponytail/main/skills/ponytail-review/SKILL.md
- https://raw.githubusercontent.com/DietrichGebert/ponytail/main/skills/ponytail-audit/SKILL.md

After installing, the first run should prove the mode is active rather than assume it: ask for a small feature in a repository you know, and check that the reply names what it skipped. A mode that answers without that line did not load.

## Security

skills.sh verdicts for sampled skills (verified October 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ponytail | Pass | Pass | Pass |
| ponytail-review | Pass | Pass | Pass |
| ponytail-audit | Pass | Pass | Pass |
| ponytail-debt | Pass | Pass | Pass |
| ponytail-gain | Pass | Pass | Pass |
| ponytail-help | Pass | Pass | Pass |

All six listings were sampled and all six pass all three auditors. The skills are instruction files: they tell the agent how to behave and ship no executable code of their own. The one behavior worth knowing about is local persistence. The mode is designed to stay on for a session until it is turned off, and the Claude Code band writes usage data to `~/.config/ponytail/band/` on the local machine. Nothing is uploaded by default.

## Limitations

- Snapshot data, verified October 23, 2026: 321,598 combined installs across 6 indexed listings; 174,315 GitHub stars; license MIT; last pushed 2026-10-18. Counts drift over time.
- The star count is extraordinary and should not be read as an audit result. The three auditor passes and the readable instruction files are the evidence; the stars are popularity.
- The benchmark numbers in the README are vendor-published: 39 tasks, one model, five runs each, measured by the skill's author. Treat the reported savings as a claim to reproduce, not a measurement you can inherit.
- The usage band that shows cost, tokens and agent time above the prompt is Claude Code only, needs version 2.1.290 or later, and does not appear in the VS Code chat panel, cloud sessions or `claude -p`. Hermes users get the skills without the band.
- This repository is the upstream project. The catalog also carries a Hermes port packaged by a third party as seven skills, which is a different repository with its own maintenance.
- A mode that stays on changes every coding task in the session. Turn it off before work where the most general solution is the correct one.

## Related

- [Hermes Ponytail Setup](/hermes/skills/catalog/hermes-ponytail-setup)
- [Caveman Skills - Agent Coding Workflow Suite Setup](/hermes/skills/catalog/caveman-skills-setup)
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup)

## Pro Tips

- Install `ponytail` and `ponytail-audit` first. The mode changes daily work and the audit is the skill that pays for itself on an unfamiliar repository.
- Use `lite` on client-facing work. It still names the smaller option without refusing to build what was asked.
- Pair the mode with `ponytail-debt` on a schedule. The ledger only works if someone reads it while the shortcut is still cheap to remove.
- Read `skills/ponytail/SKILL.md` once. It is about 3.5KB and every rule the agent follows is in that file, which makes disagreements about scope concrete.
- Keep the repository's own conventions above the mode. The skill says the shortest diff wins once you know everything it must touch, not the shortest diff that compiles.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
