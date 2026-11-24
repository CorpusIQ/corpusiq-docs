---
title: "rar-skills (robsonrung) - Agent Engineering Skills Setup"
description: "robsonrung/rar-skills - 4.8K combined installs across 96 listings: engineering skills that plan, implement, review and deliver coding work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rar-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "software engineering", "coding agents"]
---

# rar-skills (robsonrung) - Agent Engineering Skills Setup

**Source:** [robsonrung/rar-skills](https://www.skills.sh/robsonrung/rar-skills) via skills.sh - 4.8K combined installs across 96 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [robsonrung/rar-skills](https://github.com/robsonrung/rar-skills) - 2 stars, MIT, main branch, last pushed Nov 19, 2026; skills live under skills/<domain>/ with one SKILL.md each, and engineering skills sit one level deeper under skills/engineering/<group>/<name>/.
**Category:** Software Engineering and Coding Agents
**Quality Tier:** 🟡 Yellow - two of the 20 sampled skills carry a Warn cell: full-review (Snyk) and ui-ux-pro-max (Gen Agent Trust Hub); the other 18 pass all three scanners.

rar-skills is a library of engineering skills for coding agents, one SKILL.md per skill with its own references and scripts. The publisher ships no repository description, so this guide is drawn from the README, which frames the suite as the full feature lifecycle: plan a feature, implement it task by task with independent review, then deliver it. All 96 indexed listings install as one collection in the Agent Skills format.

The shared layer is the useful part. Shared contracts, model routing and runner scripts live in skills/shared/, which installs beside the skills, and each skill owns its own rules. The listings are grouped into workflow, engine, gates, lenses, practice, review, delivery, model seats, extras and visualization domains, with engineering skills nested one level deeper than the rest.

## Installation

Install the whole collection:

```bash
npx skills@latest add robsonrung/rar-skills --skill '*'
```

From a local checkout, run the bundled install script:

```bash
git clone https://github.com/robsonrung/rar-skills.git ../rar-skills
bash ../rar-skills/scripts/install-skills.sh /path/to/project
```

The script installs into .agents/skills/ and .claude/skills/; --layout picks one target, and --copy copies instead of symlinking. Check the environment the suite expects:

```bash
bash ../rar-skills/scripts/check-environment.sh
```

If a host hides a skill, tell the agent to read .agents/skills/<name>/SKILL.md and follow it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| models-consensus | 94 | running a read-only council of independent model opinions and returning one recommendation |
| skill-expert | 89 | creating, auditing or improving SKILL.md workflows and their supporting resources |
| full-review | 89 | reviewing code or requirements with evidence-backed findings and a verdict |
| brainstorm | 89 | exploring an uncertain idea and recommending whether to build, defer, reduce scope or reject it |
| clean-code | 88 | refactoring existing code with behavior-preserving Clean Code practices |
| frontend-design | 86 | frontend and UI design decisions |
| coding-design-plan | 85 | planning the implementation shape of one approved coding task |
| to-tasks | 84 | turning an approved PRD into canonical task drafts and an approved dependency queue |
| design-gate | 84 | selecting design lenses for a planned slice and returning a proceed-or-revise verdict |
| test-lens | 83 | judging test value and choosing what to test or mock |
| data-systems-coding-lens | 83 | reviewing risks in persistent state and asynchronous data paths |
| security-gate | 82 | identifying security decisions and classifying slices for deep or standard review |
| coding-review-simplify | 82 | reviewing code with a focus on simplifying it |
| implement-and-review | 81 | implementing one approved task with independent review until the acceptance contract passes |
| architecture-lens | 78 | deciding system shape and architecture trade-offs |
| gemini-runner | 77 | running a task through the Gemini model seat |
| codex-runner | 76 | running a task through the Codex model seat |
| ui-ux-pro-max | 76 | UI and UX design |
| summarize | 75 | summarizing completed work |
| claude-runner | 75 | running a task through the Claude model seat |
| safe-incremental-coding | 73 | building characterization tests before a risky change to untested legacy code |
| domain-driven-design | 73 | reviewing domain boundaries, business language, aggregates and domain events |
| explain-architecture | 70 | explaining system architecture |

The remaining 73 indexed listings range from 11 to 69 installs.

## Why This Matters for Hermes Agents

An agent asked to take a feature from idea to merged pull request usually skips the design decision and jumps to code, then discovers the shape was wrong after the work is done. rar-skills closes that gap by forcing the lifecycle in order: brainstorm the idea, settle the decisions through interview-me, write the PRD, split it into tasks, then implement each task through implement-and-review, which brings in an independent model as reviewer and keeps iterating until an acceptance contract passes. The gates and lenses are the highest-leverage pieces for a builder, because design-gate and security-gate front-load the decisions that are most expensive to reverse, and the lenses for architecture, data systems and domain-driven design catch the mistakes that general knowledge makes quietly.

The runner seats and the shared model routing are what make the suite scale across a fleet: tasks can be dispatched to a specific model, and the shared contracts keep every skill reading and writing the same work state. For an operator, the delivery skills open-pr, session-handoff and capture-learning turn a finished change into a merged pull request plus a record the next session can pick up, so handoffs stop losing context.

## Usage

| You say | What happens |
|---|---|
| Take this idea and tell me if we should build it | Uses brainstorm to weigh build, defer, reduce scope or reject |
| Turn the approved PRD into a work plan | Uses to-tasks to draft canonical tasks and an approved dependency queue |
| Implement this task and make sure it is correct | Uses implement-and-review to code, then have an independent model review until acceptance passes |
| Review this PR before it merges | Uses full-review to return evidence-backed findings and a verdict |
| Something about the data layer looks risky | Uses data-systems-coding-lens to review persistent state and async paths |
| Refactor this messy code without changing behavior | Uses clean-code for behavior-preserving refactoring |
| Give me a second opinion before I commit | Uses models-consensus to run a council of independent model opinions |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/robsonrung/rar-skills/main/README.md | head -40
```

Confirm the models-consensus skill body is present before planning work:

```bash
curl -sL https://raw.githubusercontent.com/robsonrung/rar-skills/main/skills/engineering/workflow/models-consensus/SKILL.md | head -30
```

Confirm the review skill body is present before a deep review:

```bash
curl -sL https://raw.githubusercontent.com/robsonrung/rar-skills/main/skills/engineering/review/full-review/SKILL.md | head -30
```

Confirm the shared contracts are present before relying on model routing:

```bash
curl -sL https://raw.githubusercontent.com/robsonrung/rar-skills/main/skills/shared/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| models-consensus | Pass | Pass | Pass |
| skill-expert | Pass | Pass | Pass |
| full-review | Pass | Pass | Warn |
| brainstorm | Pass | Pass | Pass |
| clean-code | Pass | Pass | Pass |
| frontend-design | Pass | Pass | Pass |
| coding-design-plan | Pass | Pass | Pass |
| to-tasks | Pass | Pass | Pass |
| design-gate | Pass | Pass | Pass |
| test-lens | Pass | Pass | Pass |
| data-systems-coding-lens | Pass | Pass | Pass |
| security-gate | Pass | Pass | Pass |
| coding-review-simplify | Pass | Pass | Pass |
| implement-and-review | Pass | Pass | Pass |
| architecture-lens | Pass | Pass | Pass |
| gemini-runner | Pass | Pass | Pass |
| codex-runner | Pass | Pass | Pass |
| ui-ux-pro-max | Warn | Pass | Pass |
| summarize | Pass | Pass | Pass |
| claude-runner | Pass | Pass | Pass |

full-review carries a Snyk Warn cell and ui-ux-pro-max carries a Gen Agent Trust Hub Warn cell; the other 18 sampled listings pass all three scanners. The 76 listings outside the sample carry no verdict cells in this guide.

## Limitations

- Snapshot data, verified Nov 23, 2026: 4,834 combined installs across 96 indexed listings; 2 GitHub stars; MIT licence; last pushed Nov 19, 2026. Counts drift over time.
- Install counts form a flat band rather than a ranking: the 23 listings shown in the table sit between 70 and 94 installs, and the full 96 span only 11 to 94, because the collection is installed as a set and no single skill dominates usage.
- The publisher ships no repository description, so the collection summary above comes from the README rather than a publisher statement.
- Several high-install listings have no counterpart in the current tree: frontend-design, coding-review-simplify, ui-ux-pro-max, summarize, explain-architecture and the per-model runner seats gemini-runner, codex-runner and claude-runner. The tree instead ships design-ui, simplify-changes and three generic seats (cli-runner, muse-runner, pi-runner), so those table cells are name-level only.
- 76 of the 96 listings were outside the verdict sample and carry no security cells in this guide.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup](/hermes/skills/catalog/dot-skills-setup)
- [Skill From Masters - Domain Expert Methodology Suite Setup](/hermes/skills/catalog/skill-from-masters-setup)
- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup)
- [AI Dev Standards Skills - Design Setup](/hermes/skills/catalog/ai-dev-standards-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the shared layer first: the gates, lenses and runners depend on skills/shared/ contracts and routing.
- Run design-gate and security-gate before implementation; they are cheap relative to reversing a wrong design after code exists.
- Pair implement-and-review with a reviewer on a different model so the review is independent rather than self-confirming.
- Ask for the PRD and task queue before code; to-prd and to-tasks make the dependency order explicit.
- Keep capture-learning and session-handoff enabled so finished work leaves a record the next session can load.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
