---
title: "Lev Nikolaevich Skills - DevOps and Delivery Setup"
description: "levnikolaevich/claude-code-skills: 45.3K combined installs across 198 listings. MIT suite of 41 lifecycle skills, from discovery to deployment."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "devops", "code review", "claude code plugins"]
---

# Lev Nikolaevich Skills - Setup Guide

**Source:** [levnikolaevich/claude-code-skills](https://www.skills.sh/levnikolaevich/claude-code-skills) via skills.sh - 45.3K combined installs across 198 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [levnikolaevich/claude-code-skills](https://github.com/levnikolaevich/claude-code-skills) - 585 stars, MIT, branch master, last pushed 2026-10-26; 41 `SKILL.md` files, one per skill, under `plugins/<suite>/skills/ln-NN-<name>/` across nine plugin suites, beside `docs/`, `scripts/`, `templates/`, `SKILL_TEMPLATE.md`, `.claude-plugin/marketplace.json` and a per-suite `plugin.json`

**Category:** DevOps, delivery and engineering lifecycle skills shipped as Claude Code and Codex plugins

**Quality Tier:** 🟡 Yellow - MIT licensed and 41 real SKILL.md files in the tree, but two of five sampled listings carry Socket and Snyk Warn verdicts

The repository is published by Lev Nikolaevich as a self-hosted plugin marketplace, and the README titles it "Claude-Codex Skills" rather than by the GitHub slug. What it sells is a lifecycle, not a grab bag: nine plugin suites that each answer one question, from "is this idea worth building" through architecture, delivery planning, implementation, quality assurance and delivery, down to "why did this fail". Every skill is standalone, and each one is written as a contract that names what to check, what it may change, and how to report evidence and remaining gaps.

The structure is visible in the checkout. Skill directories are numbered by suite: `ln-11` to `ln-13` cover product discovery, `ln-21` to `ln-26` architecture, `ln-31` to `ln-33` delivery planning, `ln-41` to `ln-46` implementation, `ln-51` to `ln-57` quality assurance, `ln-61` to `ln-64` delivery, `ln-71` to `ln-72` operations, `ln-81` skill maintenance and `ln-91` to `ln-99` engineering foundations. Each suite ships an `evals/` directory of failure fixtures, which is unusual at this level of detail: the author tests the skills against bad outcomes, not just against happy paths.

## Installation

The README documents a marketplace install for Claude Code:

```text
/plugin marketplace add levnikolaevich/claude-code-skills
/plugin install implementation-suite@levnikolaevich-skills-marketplace
/reload-plugins
```

And the Codex equivalent:

```text
codex plugin marketplace add levnikolaevich/claude-code-skills
codex plugin add implementation-suite@levnikolaevich-skills-marketplace
```

Skills are invoked by their full namespaced name, `/implementation-suite:ln-41-surgical-change-implementer` in Claude Code or `$ln-41-surgical-change-implementer` in Codex, followed by the task.

Updates are a marketplace refresh rather than a reinstall:

```text
claude plugin marketplace update levnikolaevich-skills-marketplace
claude plugin update implementation-suite@levnikolaevich-skills-marketplace
```

Hermes has no plugin marketplace target, so the durable route is a directory copy. Every `SKILL.md` carries a `name` and a one-line `description` in its frontmatter, which is the pair a Hermes skills directory reads, so a suite copies in whole:

```bash
git clone https://github.com/levnikolaevich/claude-code-skills.git
cp -r claude-code-skills/plugins/implementation-suite/skills/* ~/.hermes/profiles/corpusiq/skills/
```

The checkout holds 41 skills across those nine suites, and that count is what you install. The skills.sh index lists 198 entries for the same owner and repository, so read the tree, not the index, when you are deciding what lands in a profile.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ln-100-documents-pipeline | 479 | Running a documentation pipeline that turns one scope into the page set it needs |
| ln-620-codebase-auditor | 449 | Broad read-only audit of codebase health, security and maintainability |
| ln-775-api-docs-generator | 432 | Generating API reference documentation from the implementation |
| ln-624-code-quality-auditor | 413 | Auditing code quality for maintainability cost and duplication |
| ln-782-test-runner | 412 | Running the test suite and reporting what actually executed |
| ln-634-test-coverage-auditor | 401 | Auditing coverage against the risks the code actually carries |
| ln-201-opportunity-discoverer | 398 | Finding product opportunities worth evaluating before committing to build |
| ln-200-scope-decomposer | 396 | Breaking a scoped intent into work items with clear boundaries |
| ln-761-secret-scanner | 395 | Scanning for committed secrets and leaked credentials |
| ln-631-test-business-logic-auditor | 395 | Auditing whether tests check real business rules rather than incidental behaviour |
| ln-730-devops-setup | 394 | Setting up DevOps plumbing: pipelines, hooks and environment wiring |
| ln-140-test-docs-creator | 394 | Writing the test documentation that sits beside the suite |
| ln-630-test-auditor | 389 | Auditing an existing test suite for risk coverage and oracle quality |
| ln-210-epic-coordinator | 387 | Coordinating an epic across its child stories and tasks |
| ln-773-cors-configurator | 386 | Configuring CORS policy across environments |
| ln-774-healthcheck-setup | 385 | Adding healthcheck endpoints and readiness probes |
| ln-742-precommit-setup | 385 | Installing pre-commit hooks that enforce project rules |
| ln-732-cicd-generator | 384 | Generating CI/CD pipeline configuration for the repo's stack |
| ln-700-project-bootstrap | 384 | Bootstrapping a project with the baseline structure and rules |
| ln-401-task-executor | 384 | Executing one approved task end to end |
| ln-115-devops-docs-creator | 384 | Creating the DevOps documentation set |
| ln-114-frontend-docs-creator | 384 | Creating frontend documentation |
| ln-113-backend-docs-creator | 384 | Creating backend documentation |

The remaining 175 indexed listings range from 35 to 383 installs.

A caveat that matters more here than for most guides: every one of those 23 names is absent from the checkout. The tree ships `ln-41-surgical-change-implementer` where the index lists a task executor, and the whole `ln-1xx`, `ln-2xx`, `ln-4xx`, `ln-6xx` and `ln-7xx` number ranges are missing from it, so the Use For cells above are a reading of the listing name plus the README's suite map, not a quote from a `SKILL.md` that exists in the tree today.

## Why This Matters for Hermes Agents

Most agent skill collections are collections of verbs: search the web, run the tests, write the file. This one is a collection of gates, and the gates are the part that transfers. Each `SKILL.md` opens with an execution contract that forces per-item status tracking: an item is `PENDING`, `PROVEN` with observed outcome evidence, `CLEARED` with evidence its condition is absent, or `UNPROVEN` with a stated gap. Reading a file, a zero exit code or a self-reported success is explicitly not proof.

That is the failure mode Hermes has most of, and it is worth installing the language even if you use only two or three of the skills. An agent that reports `PROVEN` only when it has an observed outcome is an agent whose summaries can be trusted without re-deriving them, and the contract spells out what to do when nobody can answer a question: report the exact question and apply the gap verdict rather than waiting or guessing.

The suites are also split by authority rather than by topic, which is how a multi-agent harness should be wired. Audit skills are read-only by construction, implementation skills carry a bounded write scope, and delivery skills require explicit authorization before they touch a remote. That makes a clean mapping onto a Hermes profile: the read-only auditors can be handed to a subagent with no approval prompts, while the publishers and deployment engineers sit behind an explicit decision.

Finally, the evals are a real artifact. Because each suite ships failure fixtures rather than only success fixtures, the repository tells you where the author expects the skill to be tempted, and that list is a good checklist for the parts of your own workflow to instrument first.

## Usage

| You say | What happens |
|---|---|
| "Is this feature request worth building?" | `ln-11-opportunity-evaluator` assesses demand, channels and economics before any build commitment, and writes to product docs only. |
| "Plan the change, then tell me what could go wrong" | `ln-31-delivery-plan-builder` builds a dependency-ordered plan read-only, then `ln-33-plan-reviewer` reports missing decisions, feasibility and risk before execution starts. |
| "Fix the cause, not the symptom" | `ln-41-surgical-change-implementer` makes one scoped change against existing contracts, marks each checklist item as proven or unproven, and reports the gaps at the end. |
| "Audit this codebase before we ship" | `ln-54-codebase-auditor` runs a broad read-only audit across security, delivery and maintainability, and explicitly refuses to turn detector matches into findings. |
| "Our tests pass but prove nothing" | `ln-55-test-suite-auditor` checks risk coverage, oracle reliability and maintenance value without editing the tests. |
| "Set up the lint and type gates" | `ln-46-quality-gate-engineer` configures and verifies the checks, and reports project compliance separately from enforcement. |
| "Publish the release" | `ln-62-release-publisher` prepares an explicitly requested tagged release and verifies it at the destination; it does not deploy an application. |

## Verification

Both raw paths below returned 200 on branch master when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} baseline\n" \
  https://raw.githubusercontent.com/levnikolaevich/claude-code-skills/master/plugins/architecture-suite/skills/ln-21-system-design-baseline-builder/SKILL.md
curl -sL -o /dev/null -w "%{http_code} documenter\n" \
  https://raw.githubusercontent.com/levnikolaevich/claude-code-skills/master/plugins/architecture-suite/skills/ln-22-current-architecture-documenter/SKILL.md
```

Expect `200` twice. The branch name is `master`, not `main`, and a `main` URL fails, which is the most common way to conclude wrongly that a repository is empty.

After the copy, confirm the frontmatter is what the loader expects:

```bash
head -4 ~/.hermes/profiles/corpusiq/skills/ln-41-surgical-change-implementer/SKILL.md
grep -l '^name: ' ~/.hermes/profiles/corpusiq/skills/*/SKILL.md | wc -l
```

A good copy shows `name:` and a single-line `description:` with no other frontmatter keys, since that is all these skills declare. `find` over the profile also confirms the count: 41 for the full repository, or however many suites you chose to copy.

## Security

Two of the five sampled listings carry a Warn verdict, so read this before enabling the write-capable skills: `ln-620-codebase-auditor` is Warn on both Socket and Snyk, and `ln-775-api-docs-generator` is Warn on Snyk. None of the sampled listings Fail. skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ln-100-documents-pipeline | Pass | Pass | Pass |
| ln-620-codebase-auditor | Pass | Warn | Warn |
| ln-775-api-docs-generator | Pass | Pass | Warn |
| ln-624-code-quality-auditor | Pass | Pass | Pass |
| ln-73-system-design-proposal-builder | Pass | Pass | Pass |

The good news is the surface. These skills are markdown instructions, not executables: the 41 `SKILL.md` files total 549,557 bytes, roughly 13 KB each, and the repository's only scripts are PowerShell helpers under `scripts/` for local eval runs, plus `fixture.sh` files inside each suite's `evals/`. There is no MCP server, no network client and no install hook. What a skill here can do is bounded by the tools your harness gives it, which means a read-only auditor is genuinely read-only only if the profile also withholds write tools from it.

The part worth reading carefully is the delivery and foundation suites, `ln-61` through `ln-64` and `ln-91` through `ln-99`. Those skills are written to commit, push, publish releases, prepare pipelines and establish authentication and authorization contracts, and they assume the harness enforces their authorization boundaries. Grant them to a profile with push rights and no approval gate and you have delegated publishing to a markdown file.

## Limitations

- Snapshot data, verified 2026-10-30: 45,336 combined installs across 198 indexed listings; 585 GitHub stars; MIT; last pushed 2026-10-26. Counts drift over time.
- The index outruns the tree by a wide margin and with different names. skills.sh carries 198 listings, the checkout holds 41 skill directories, and not one of the 23 listings above the install threshold matches a directory name in the tree. The numbers describe an index version this guide could not inspect.
- The counts are flat, not ranked. The top listing holds 479 installs out of 45,336 combined, and 175 listings sit between 35 and 383, so the suite's visibility is spread across many small entries rather than concentrated in a few popular skills.
- The install path is Claude Code and Codex only. There is no skills.sh CLI install, no Hermes plugin target, and the marketplace commands are the two clients the README names; on Hermes the install is a directory copy plus a restart.
- Every skill is long. Each `SKILL.md` is a full execution contract averaging about 13 KB, so loading three suites into a context costs real tokens before any work starts, and there is no index file that summarises them for routing.
- The evals are PowerShell-driven. `scripts/run-codex-evals.ps1` and its siblings target a Windows shell, so verifying the fixtures on Linux means reading them rather than running the runner.

## Related

- [PStack Skills - Engineering Discipline Suite Setup](/hermes/skills/catalog/pstack-setup)
- [Ship Shit Dev Skills - 14 Command Routers Setup](/hermes/skills/catalog/shipshitdev-skills-setup)
- [Melodic Software Claude Code Plugins - Marketplace Setup](/hermes/skills/catalog/melodic-claude-code-plugins-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy suites, not the repository. The profile loader reads every `SKILL.md` under its skills directory, so dropping all 41 in at once gives you 41 always-available descriptions to route against and a large context bill; start with `implementation-suite` and `quality-assurance-suite`.
- Prefix the directory names when you copy. `ln-41-surgical-change-implementer` is unambiguous on its own, but the nine suites share one numbering convention, and a flat copy into one skills directory loses the suite a skill belongs to.
- Keep the audit skills read-only at the harness level, not just in the prose. The contracts ask the model to stay read-only; withholding write and shell tools is what makes it true.
- Read the `evals/` fixture names before you trust a skill. They name the failure the author was worried about, which is the fastest way to see whether a skill covers the thing your workflow keeps getting wrong.
- Use `master` in every raw URL. The repository has no `main` branch, and a fetch that silently 404s against `main` reads like an empty repository rather than a wrong branch.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
