---
title: "NextStage Skills - Spec-Driven Development Suite Setup"
description: "nextstage-brasil/skills: agent-agnostic skills for spec-driven development, GitLab integration, code quality and testing - 7.8K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nextstage-brasil-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "spec-driven development", "gitlab", "code quality", "brownfield onboarding"]
---

# NextStage Skills - Spec-Driven Development Suite Setup

**Source:** [nextstage-brasil/skills](https://www.skills.sh/nextstage-brasil/skills) via skills.sh - 7.8K combined installs across 96 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [nextstage-brasil/skills](https://github.com/nextstage-brasil/skills) - 0 stars, Apache-2.0 license, main branch, last pushed Nov 17, 2026; a flat skills/ catalog with one directory per skill (SKILL.md plus references/ and evals/) and a packages/harness Node CLI that installs and syncs the skills.
**Category:** Spec-Driven Development and GitLab Workflow
**Quality Tier:** 🟡 Yellow - 0 stars but Apache-2.0 licensed; the 20 sampled skills carry no Fail cells, with Socket Warns on two skills and Snyk Warns on seven skills.

NextStage Brasil's skills suite is an agent-agnostic catalog for coding agents in the open skills ecosystem. The workflows span spec-driven development (clarify to requirements to tasks to implement to close), GitLab integration (board sync, CI generation, issue execution), code quality review (reviewer plus judge), testing (PHPUnit backend tests and Cypress end-to-end), and brownfield onboarding (architecture rules, reverse spec, brownfield map). Skills are decoupled from any single harness: they use session boot, which reads AGENTS.md at the project root and then .nextstage-harness/rules/.

The suite ships as a flat skills/ catalog alongside a Node harness CLI under packages/harness that installs with `npx @nextstage-brasil/harness` and offers presets (spec-driven, gitlab, project-manager, frontend, agents, full). One listing, mcp-gitlab-usage, has no directory in the skills/ tree: the README explains its GitLab MCP tool contracts are provisioned by the GitLab MCP server on first use, not as a catalog skill.

## Installation

The recommended path is the interactive harness wizard, which picks a preset, resolves skill dependencies, runs the Skills CLI add command and optionally scaffolds AGENTS.md plus the docs/ layout:

```bash
npx @nextstage-brasil/harness
```

Non-interactive, pick a preset directly:

```bash
npx @nextstage-brasil/harness --preset spec-driven --yes
npx @nextstage-brasil/harness --preset gitlab --yes
npx @nextstage-brasil/harness --preset full --yes
```

Manual install through the Skills CLI (use --full-depth for the references/ files):

```bash
npx skills add nextstage-brasil/skills@ns-harness --full-depth -y
npx skills add nextstage-brasil/skills@ns-spec-driven --full-depth -y
npx skills add nextstage-brasil/skills --full-depth --all -y
```

Global install of a single skill:

```bash
npx skills add nextstage-brasil/skills@ns-coder --full-depth -g -y
```

The preset names and their aliases: spec-driven, gitlab (alias spec-driven-gitlab), project-manager, frontend (alias frontend-prototype), agents (aliases agent-creator and agents-api), and full. Until vercel-labs/skills#861 merges, the frontmatter `depends` field is ignored by skills@1.5.14, so install peer skills manually.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ns-gitlab-board-sync | 987 | sync existing GitLab issues with local planning: milestone, labels, status, assignee, estimates, spent time |
| ns-harness | 259 | session boot and brownfield prepare: architecture rules, brownfield map, reverse spec, AGENTS.md |
| ns-spec-driven | 218 | spec-driven delivery from clarify through requirements, tasks, implement and close |
| ns-gitlab-ci-generator | 210 | generate and adapt .gitlab-ci.yml for SaaS monorepos with backend and frontend |
| ns-project-manager | 194 | PM: clarify, RICE/WSJF, sprint, PERT/Monte Carlo, PRD, roadmap, version handoff and release report |
| ns-langgraph-agents | 180 | LangGraph.js agent-api: StateGraph, MCP wiring, checkpointers, user memory, HITL and SSE |
| ns-execution-gitlab-issue | 174 | execute a GitLab issue end to end with status checks, worktree isolation, merge request and code then judge loop |
| ns-requirements-enricher | 173 | codebase-grounded implementation plan for one GitLab issue or pasted scope |
| mcp-gitlab-usage | 166 | GitLab MCP tool contracts provisioned by the GitLab MCP server on first use, not a catalog skill |
| ns-best-practices | 164 | security, compatibility and a11y plus Vercel Web Interface Guidelines |
| ns-investigator | 163 | root-cause diagnosis from errors, logs, stack traces, failing tests or CI |
| ns-frontend-design | 163 | distinctive production UI, avoiding generic AI aesthetics |
| ns-autonomous | 162 | autonomous execution engine with planning-depth decisions and multi-agent dispatch in an isolated worktree |
| ns-e2e-tests | 161 | implement and refactor Cypress E2E specs in an independent tests-e2e directory |
| ns-docs-writer | 161 | human-facing project docs: README, docs guides, runbooks |
| ns-coder | 161 | ad-hoc coding without full SDD: bug fixes, refactors, scripts, migrations |
| ns-backend-tests | 161 | PHPUnit unit and integration tests in Docker for backend packages |
| ns-reviewer | 150 | code quality review on SOLID, clean code, performance, security and testability |
| ns-living-spec | 150 | living domain specs under docs/specs after version closure |

The remaining 77 indexed listings range from 13 to 114 installs.

## Why This Matters for Hermes Agents

The suite's value is that it encodes a complete delivery loop as skills instead of one mega-prompt. ns-spec-driven carries the clarify to requirements to tasks to implement pipeline with resume-from-disk continuity, so an agent can pick up a half-finished version without re-deriving context. The reviewer plus judge pairing is worth copying: code quality review stops at a strict score, and delivery proof is a separate skill that checks the change against acceptance criteria, so the agent that wrote the code cannot also sign off on it. ns-harness is the brownfield story: it reverse-engineers an existing codebase into architecture rules, a brownfield map and AGENTS.md before any implementation starts, which is the step most agent setups skip. The GitLab skills (board sync, CI generator, issue execution) let the same agent drive issues, pipelines and merge requests without leaving its workflow. For operators the main caveats are the 0-star repository and the fact that frontmatter dependency resolution is not yet honored by the Skills CLI, so peers must be installed manually for now.

## Usage

| You say | What happens |
|---|---|
| Prepare this repo | ns-harness reverse-engineers the codebase and generates architecture rules, a brownfield map and AGENTS.md |
| Specify a feature and ship it | ns-spec-driven runs clarify through requirements and tasks, then implements and closes the version |
| Execute this GitLab issue | ns-execution-gitlab-issue runs status checks, isolates a worktree, delivers and opens a merge request, then runs code then judge |
| Review the changes | ns-reviewer scores the change on SOLID, clean code, performance, security and testability; Approved only at 10 |
| Write the PHPUnit tests | ns-backend-tests scaffolds and runs PHPUnit in Docker with testdox and stop-on-failure |
| Generate the CI pipeline | ns-gitlab-ci-generator writes a .gitlab-ci.yml with test, build, E2E and branch deploys |
| Diagnose why the test fails | ns-investigator reads the errors, logs and stack trace and returns a root-cause explanation |

## Verification

Confirm the harness skill landed and read its boot contract before running it:

```bash
curl -sL https://raw.githubusercontent.com/nextstage-brasil/skills/main/skills/ns-harness/SKILL.md | head -40
```

Review the spec-driven entry point that most presets install:

```bash
curl -sL https://raw.githubusercontent.com/nextstage-brasil/skills/main/skills/ns-spec-driven/SKILL.md | head -40
```

Inspect the ad-hoc coder before using it outside the SDD path:

```bash
curl -sL https://raw.githubusercontent.com/nextstage-brasil/skills/main/skills/ns-coder/SKILL.md | head -40
```

Read the reviewer before letting it approve production changes:

```bash
curl -sL https://raw.githubusercontent.com/nextstage-brasil/skills/main/skills/ns-reviewer/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ns-gitlab-board-sync | Pass | Pass | Warn |
| ns-harness | Pass | Pass | Pass |
| ns-spec-driven | Pass | Pass | Pass |
| ns-gitlab-ci-generator | Pass | Warn | Pass |
| ns-project-manager | Pass | Pass | Warn |
| ns-langgraph-agents | Pass | Warn | Pass |
| ns-execution-gitlab-issue | Pass | Pass | Warn |
| ns-requirements-enricher | Pass | Pass | Warn |
| mcp-gitlab-usage | Pass | Pass | Warn |
| ns-best-practices | Pass | Pass | Pass |
| ns-investigator | Pass | Pass | Pass |
| ns-frontend-design | Pass | Pass | Pass |
| ns-autonomous | Pass | Pass | Warn |
| ns-e2e-tests | Pass | Pass | Pass |
| ns-docs-writer | Pass | Pass | Pass |
| ns-coder | Pass | Pass | Pass |
| ns-backend-tests | Pass | Pass | Pass |
| ns-reviewer | Pass | Pass | Warn |
| ns-living-spec | Pass | Pass | Pass |
| ns-proto-visual-guide | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 22, 2026: 7.8K combined installs across 96 indexed listings; 0 GitHub stars; Apache-2.0 license; last pushed Nov 17, 2026. Counts drift over time.
- The publisher has no GitHub stars yet, so install counts are the only real-world usage evidence available.
- The long tail is largely naming and phase variants: SDD phase listings live inside ns-spec-driven's references/ directory (the README states there is no selective install of individual SDD phases), and retired names such as ns-agent-engineering and ns-multi-agent-architect are tracked in retired-skills.json.
- mcp-gitlab-usage carries an install count but has no skills/ directory; the README states its tool contracts are provisioned by the GitLab MCP server on first use.
- Only 20 of the 96 indexed listings have skills.sh security verdicts in this snapshot; the other 76 are unverified.
- Frontmatter `depends` is ignored by skills@1.5.14, so install peer skills manually until vercel-labs/skills#861 merges.

## Related

- [Specsfy Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/specsfy-setup)
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)
- [GitLab CLI Skills - glab Command Reference](/hermes/skills/catalog/gitlab-cli-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `npx @nextstage-brasil/harness --preset spec-driven --yes`; it resolves the SDD face plus coder, reviewer, investigator, autonomous and living-spec in one pass.
- Run `/ns-harness prepare this repo` before any spec-driven work on a brownfield codebase so architecture rules and the brownfield map exist first.
- Keep ns-coder for single-step edits and ns-execution-gitlab-issue for issue-scoped work; ns-spec-driven is the multi-day version path.
- Install peers manually for now: frontmatter `depends` is ignored by skills@1.5.14 until vercel-labs/skills#861 merges.
- Read each SKILL.md before relying on it in production: 0 stars means install counts are the only usage signal, and 76 of 96 listings have no security verdict in the snapshot.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
