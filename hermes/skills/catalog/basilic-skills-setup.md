---
title: "Basilic Skills - Slash Playbooks for Coding Agents"
description: "blockmatic-icebox/basilic-skills - 36.2K combined installs across 96 indexed listings: slash playbooks for coding agents from plan to ship."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/basilic-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "coding workflow", "slash commands"]
---

# Basilic Skills - Setup Guide

**Source:** [blockmatic-icebox/basilic-skills](https://www.skills.sh/blockmatic-icebox/basilic-skills) via skills.sh - 36.2K combined installs across 96 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 1 star, no LICENSE file (skills.sh reports NOASSERTION; the README ends with "MIT"), `main` branch, last pushed 2026-10-02, `SKILL.md` files under `skills/workflow/` (the workflow umbrella plus nested `w-<name>/` playbooks) and standalone skills such as `skills/technical-writing/`
**Category:** Coding workflow - slash-command playbooks for plan, build, ship
**Quality Tier:** 🟡 Yellow - sampled skills pass the Gen Agent Trust Hub, with a few Socket and Snyk warns and no fails.

Basilic is a suite of slash playbooks for coding agents, published by Blockmatic and indexed on skills.sh as blockmatic-icebox/basilic-skills. It packages a complete coding workflow as `/w-*` slash commands, plus a standalone `technical-writing` skill for MDX, README, and product markdown. Invoke them as `/w-plan`, `/w-build`, `/w-ship`, and the rest in any IDE or agent that can read a `SKILL.md`.

The playbooks install as one unit: `--skill workflow` unpacks all nested `/w-*` playbooks under `.agents/skills/workflow/`. That is why the playbook install counts sit in a flat band (most at 647) rather than accumulating individually: the count reflects one unit install, not 41 independent adoptions. The workflow spans lifecycle (plan, council, grill, wayfinder, build, retro), git (commit, push, pr, comments, git-repair, fix-push, ship, pr-loop), debug, CI (gha, vercel), quality (lint, test, tdd, unit, api-test, yolo), review and security, product and docs, and UI craft.

## Installation

From a consumer repo:

```sh
# install the full workflow pack (all nested /w-* playbooks)
npx skills@latest add blockmatic/basilic-skills --skill workflow

# standalone writing skill (MDX, README, product markdown)
npx skills@latest add blockmatic/basilic-skills --skill technical-writing
```

Interactive pick: `npx skills@latest add blockmatic/basilic-skills`. To list what is available, add `--list`. Do not pass `--all`: it also targets every harness (`-a '*'`), which writes extra trees such as eve's `agent/skills/` at the repo root.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| workflow | 849 | The packed unit that installs all /w-* playbooks under .agents/skills/workflow/. |
| w-review-plan | 649 | Review a plan's goals, assumptions, tasks, risks, and references. |
| w-yolo | 647 | Fix failing or requested local checks without publishing. |
| w-vercel | 647 | Retrieve Vercel build logs, analyze failures, and fix the local build. |
| w-v0 | 647 | Draft a Next.js and shadcn v0.dev prompt, then wait for OPEN, EDIT, or CANCEL. |
| w-unit | 647 | Add unit tests for the current change using the repo test skill and colocated files. |
| w-ui | 647 | Build or reshape UI with existing tokens, accessible interactions, and bounded verification. |
| w-test | 647 | Run the repository test scripts and fix failures until they pass. |
| w-tdd | 647 | Implement a requested increment with red-green-refactor. |
| w-ship | 647 | Implement the change, validate, commit, push, and create its PR. |
| w-shadcn | 647 | Install shadcn/w-ui primitives in the shared UI package with monorepo import paths. |
| w-security | 647 | Review the change or tree against repository security docs and existing checks. |
| w-roadmap | 647 | Diff the codebase against GitHub issues and matching docs without inventing a backlog. |
| w-review | 647 | Review a change for evidenced defects and risks without editing it. |
| w-retro | 647 | After finishing work, answer what you would do better next time. |
| w-release | 647 | Advisory review of release impact, changelog, and template contracts. |
| w-refactor | 647 | Refactor selected code while preserving behavior, then verify. |
| w-push | 647 | Validate and push the intended branch while preserving unrelated work. |
| w-pr | 647 | Create or update a reviewable pull request for the intended branch. |
| w-plan | 647 | Write an ordered plan without changing implementation. |
| w-perf | 647 | Measure bottlenecks with repository tools, then recommend or apply optimizations. |
| w-onboard | 647 | Get a new developer from clone to a running local app. |
| w-lint | 647 | Run project linters, apply the smallest fixes, and re-run until clean. |
| w-git-repair | 647 | Resolve common Git problems and conflicts with inspected commands. |
| w-gha | 647 | Retrieve GitHub Actions logs with gh, analyze failures, and fix CI errors locally. |
| w-form | 647 | Build a Next.js form using the app's existing mutation path, not a second stack. |
| w-fix-push | 647 | Fix reported issues, validate, then commit and push. |
| w-errors | 647 | Add error handling that matches existing repo error and logging packages. |
| w-docs | 647 | Document the current code or feature in the owning docs layer. |
| w-diagram | 647 | Produce a Mermaid diagram of the requested code, architecture, or data flow. |
| w-deslop | 647 | Remove AI-generated slop introduced on this branch relative to main. |
| w-debug | 647 | Diagnose a failure from evidence and verify the original scenario after a fix. |
| w-debug-browser | 647 | Reproduce and resolve an authorized browser issue using runtime evidence. |
| w-council | 647 | Explore a codebase with parallel agents, then hand off findings. |
| w-commit | 647 | Review and commit the task's intended changes using repository conventions. |
| w-comments | 647 | Process reviewer feedback, apply fixes, and draft replies without unsolicited commits. |
| w-coderabbit | 647 | Fetch CodeRabbit review comments, apply authorized fixes, and stop at local verification. |
| w-clarify | 647 | Resolve consequential missing requirements from inspected context. |
| w-build | 647 | Implement an agreed task incrementally and verify the result. |
| w-architecture | 647 | Plan an implementation structure; durable decisions belong in ADRs and architecture docs. |
| w-api-test | 647 | Add API tests that exercise public HTTP behavior against existing harnesses. |
| w-api-docs | 647 | Refresh API docs from the owning schema source, never editing generated OpenAPI by hand. |
| w-a11y | 647 | Audit UI against repository a11y docs and tests without inventing a WCAG level. |

The remaining 53 indexed listings range from 2 to 543 installs.

## Why This Matters for Hermes Agents

The suite splits one big coding job into single-writer slash commands, so an agent does not try to plan, build, review, and publish in one pass. `/w-plan` explores through `/w-council` before writing anything, which keeps exploration separate from the plan itself. The quality playbooks (`/w-test`, `/w-tdd`, `/w-unit`, `/w-lint`) enforce verification at each step rather than leaving it to the end. `/w-deslop` is unusual and directly useful: it removes AI-generated slop introduced on the current branch relative to main. The playbooks are tool-agnostic and read a `SKILL.md`, so they work in any harness that can load one. The single-writer discipline keeps git, TDD, lint, and publish sequential, which reduces the chance of two processes racing the same tree.

## Usage

| You say | What happens |
|---|---|
| "/w-plan this feature" | w-plan explores via w-council, then writes an ordered plan without changing implementation. |
| "/w-build" | w-build implements an agreed task incrementally and verifies the result. |
| "/w-ship the change" | w-ship implements, validates, commits, pushes, and opens the PR. |
| "/w-debug the failing check" | w-debug diagnoses from evidence and verifies the original scenario after the fix. |
| "/w-gha" | w-gha pulls GitHub Actions logs, analyzes failures, and fixes CI errors locally. |
| "/w-a11y" | w-a11y audits the UI against the repository's a11y docs and tests. |
| "/w-ui make this screen" | w-ui builds or reshapes UI with existing tokens and accessible interactions. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/blockmatic-icebox/basilic-skills/main/skills/workflow/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/blockmatic-icebox/basilic-skills/main/skills/workflow/w-plan/SKILL.md | head -20
npx skills@latest add blockmatic/basilic-skills --list
```

The workflow umbrella lives at `skills/workflow/SKILL.md` with nested playbooks at `skills/workflow/w-<name>/SKILL.md`; standalone skills live at `skills/<name>/SKILL.md`. Confirm the path exists in the current tree before installing a specific playbook.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| workflow | Pass | Warn | Warn |
| w-review-plan | Pass | Pass | Pass |
| w-yolo | Pass | Pass | Warn |
| w-vercel | Pass | Pass | Pass |
| w-v0 | Pass | Warn | Pass |
| w-unit | Pass | Pass | Pass |
| w-ui | Pass | Pass | Pass |
| w-test | Pass | Pass | Pass |
| w-tdd | Pass | Pass | Pass |
| w-ship | Pass | Pass | Pass |
| w-shadcn | Pass | Pass | Pass |
| w-security | Pass | Pass | Pass |

No sampled skill fails; three carry warns (workflow on Socket and Snyk, w-yolo on Snyk, w-v0 on Socket).

## Limitations

- Snapshot data, verified Nov 16, 2026: 36,217 combined installs across 96 indexed listings; 1 GitHub star; no LICENSE file (skills.sh reports NOASSERTION); last pushed 2026-10-02. Counts drift over time.
- The 41 /w-* playbooks share a flat 647-install count because they install as one unit; the count reflects that unit, not independent adoption.
- License mismatch: GitHub metadata reports no LICENSE file (NOASSERTION) while the README ends with "MIT". Treat the terms as unclear until a LICENSE file ships.
- The skills.sh listing uses blockmatic-icebox/basilic-skills while the README install command points at blockmatic/basilic-skills; both GitHub paths resolve today.
- Do not pass --all: it also targets every harness (-a '*'), writing extra trees such as eve's agent/skills/ at the repo root.
- 53 of the 96 indexed listings fall below 600 installs, mostly library and version-specific guides (tailwind-design-system-v4, next-v16, expo-*-v55, and others).

## Related

- [Claude Code Skills](/hermes/skills/catalog/claude-code-skills-setup)
- [Vercel Agent Skills](/hermes/skills/catalog/vercel-agent-skills-setup)
- [Sentimony Agentic Workflow](/hermes/skills/catalog/sentimony-agentic-workflow-setup)
- [Herman's Skill Playbook](/hermes/skills/catalog/herman-skill-playbook-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install with --skill workflow to get all /w-* playbooks in one unit; the flat install band across the playbooks is expected because they ship as one unit.
- Chain the playbooks in order (plan, build, test, ship); they assume one process touches the tree at a time.
- /w-plan ships references/plan-output.md and /w-pr-loop ships references/polling.md; read them before extending the workflow.
- Run node scripts/validate-catalog.mjs before pushing catalog changes; consumers refresh with npx skills@latest update.
- Keep the umbrella at skills/workflow/SKILL.md and set disable-model-invocation on each nested playbook, per the repo's contribute guide.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
