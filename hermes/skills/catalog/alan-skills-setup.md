---
title: "Alan Skills - Plan, Test and Review PRs"
description: "supatest-ai/alan-skills on skills.sh: 6.4K combined installs across 6 listings; plans, PR review and browser-tested feature reports for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/alan-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "testing", "planning"]
---

# Alan Skills - Setup Guide

**Source:** [supatest-ai/alan-skills](https://www.skills.sh/supatest-ai/alan-skills) via skills.sh - 6.4K combined installs across 6 indexed listings; first seen 2026-11-07 (Nov 7, 2026 morning sweep)
**GitHub:** 0 stars, Apache-2.0, branch `main`, last pushed 2026-07-28, 3 SKILL.md directories (`skills/alan-plan`, `skills/alan-review-pr`, `skills/alan-test-feature`)
**Category:** Delivery workflow for agents: implementation planning, feature testing and pull-request review passes from a software factory agent
**Quality Tier:** 🟡 Yellow - two of five sampled skills are clean, the testing skill draws a Socket warn plus a Snyk fail, and the repository has no stars and no pushes since July.

Alan is Supatest's software factory agent, and this repository is the public mirror of the workflows it runs internally: write a plan, write a PRD, create the PR, review the PR, check CI, test the feature. The skills are short and procedural. Each one names the MCP tools it needs, the order to call them, and the artifact it must produce before finishing.

Three of those skills carry almost all of the installs, and they form a loop rather than a suite: plan the work, test the feature end to end, review the pull request. The testing skill is the most opinionated of the three. It scopes coverage with the user, builds an explicit strategy, drives a real browser through `agent-browser`, and treats screenshots, video and a structured report as mandatory rather than optional.

## Installation

The README's one-command route. Note that the commands name `supatest-ai/aiden-skills`, an older repository path; the current repository is `supatest-ai/alan-skills`, and the drift is covered under Limitations rather than silently corrected here:

```bash
npx skills add supatest-ai/aiden-skills
npx skills add supatest-ai/aiden-skills --skill alan-test-feature
npx skills add supatest-ai/aiden-skills --list
```

The first line installs every skill, the second takes one, the third lists the repository without installing. The README says the `npx skills` CLI detects your installed agent (Claude Code, Codex, Cursor, Gemini, OpenCode) and writes to the right path.

For a pinned install, the README documents git tags:

```bash
npx skills add supatest-ai/aiden-skills@v0.1.0
```

If you would rather place files yourself, clone the repository and copy the skill directories into your agent's skills location. The README's table:

| Agent | Path |
|---|---|
| Claude Code | `~/.claude/skills/<name>/` |
| Codex CLI | `~/.codex/skills/<name>/` |
| Gemini CLI | `~/.gemini/skills/` or `~/.agents/skills/<name>/` |
| OpenCode | `~/.config/opencode/skills/<name>/` (also reads `~/.claude/skills/`) |
| Cross-agent | `~/.agents/skills/<name>/` |

Two runtime dependencies sit outside the skills. Several skills call Alan's MCP server (`mcp__alan__*`) to persist plans, documents, test reports and GitHub operations; without it the bodies still read as workflow guides, but persistence steps need adapting. The testing skill also needs `agent-browser`, which its own `SKILL.md` describes as a Vercel Labs CLI tool rather than a skill or an MCP tool, installed with `npm install -g agent-browser && agent-browser install`.

## What It Provides

Three listings clear the 500-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| alan-test-feature | 1,797 | Scope coverage, build a testing strategy, drive the feature in a real browser with `agent-browser`, capture screenshots and video, upload to S3, then write a structured test report |
| alan-plan | 1,797 | Build an implementation plan through codebase analysis and a one-question-at-a-time interview, then persist it as a plan artifact in Alan |
| alan-review-pr | 1,796 | Review a GitHub pull request for security, correctness and performance, then post inline comments through Alan's GitHub MCP tools |

The remaining 3 indexed listings range from 324 to 326 installs.

Those three tail listings are `aiden-plan`, `aiden-test-feature` and `aiden-review-pr`, and their install counts sit close enough together to look like one cohort rather than three independent skills. The names match the older `aiden-skills` path the README still uses, and no directories with those names exist in the current tree; the three `alan-*` directories are the live copies.

The README documents more skills than the index tracks: `alan-prd` for a Product Requirements Document, `alan-document` for structured artifacts with mermaid diagrams, `alan-create-pr` for pushing a branch and opening a PR, and `alan-check-ci` for CI status. None of those four carries an install count on skills.sh, and none has a directory in the current tree, so treat them as documented intent rather than shipped code.

## Why This Matters for Hermes Agents

The loop these skills encode is the one agents are worst at finishing. A model will happily write code, skip the plan, call the work done, and never look at the PR it just opened. `alan-plan` forces the interview before the code, `alan-test-feature` forces the browser pass and the artifact, and `alan-review-pr` forces a review with inline comments rather than a summary nobody can act on.

The testing skill is the most transferable piece even without Alan. It refuses to consider a feature tested without screenshots, video and a written report, and it starts by checking that `agent-browser` is installed rather than assuming. That habit, verify the harness before trusting the result, is the same one that keeps a Hermes agent from reporting a passing test suite it never ran.

The review skill is a useful counterweight to model agreeableness. Its job is security, correctness and performance, with findings posted as inline comments, which is a different output shape from a prose review and much harder to fake.

The persistence through MCP is the part to weigh. If your agent already has GitHub access and a place to write artifacts, the workflow bodies are the value and the MCP calls are optional scaffolding. If you run Alan, they are the reason the skills exist.

## Usage

| You say | What happens |
|---|---|
| "Plan this feature before I write any code" | `alan-plan` analyses the codebase, interviews you one question at a time and persists the plan as an artifact |
| "Test the new checkout flow and send me proof" | `alan-test-feature` scopes coverage, starts the dev server, drives the flow with `agent-browser`, captures screenshots and video, then writes the structured report |
| "Review PR 412 for security and performance" | `alan-review-pr` reads the diff through the GitHub MCP tools and posts inline comments on the lines it flags |
| "Is the harness even installed?" | The testing skill checks for `agent-browser` first and stops with the install command if it is missing, instead of running a browser that is not there |
| "Pin these skills so they stop changing" | The README's tag route installs a fixed release, for example `@v0.1.0`, instead of tracking `main` |
| "Where do these files go for Codex?" | The manual table maps each agent to its skills path, including the cross-agent `~/.agents/skills/<name>/` location |

## Verification

Read the testing skill before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/supatest-ai/alan-skills/main/skills/alan-test-feature/SKILL.md | head -40
```

It should open with the description quoted in the pack above, then a task section that lists the phases, the environment variables the skill reads (`ALAN_TASK_ID`, `ALAN_SESSION_ID`) and the `agent-browser` check with its install command. The plan skill is at the same shape, `skills/alan-plan/SKILL.md` (also 200).

After install, confirm the directories arrived, for example:

```bash
ls ~/.claude/skills
```

You should see `alan-plan`, `alan-review-pr` and `alan-test-feature`. Then confirm the browser harness the testing skill depends on:

```bash
command -v agent-browser
```

If that prints nothing, install it before running the testing skill. If you install through the README's `npx skills` route, check where the CLI actually wrote the files rather than assuming a path, because the README lists five different agent locations.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| alan-test-feature | Pass | Warn | Fail |
| alan-plan | Pass | Pass | Pass |
| aiden-plan | Pass | Pass | Pass |
| aiden-test-feature | Pass | Pass | Fail |
| aiden-review-pr | Pass | Pass | Warn |

The skill surface is markdown: `SKILL.md` bodies that tell the agent which MCP tool to call and in what order. Nothing in the skill path installs a service on its own, and the licence is Apache-2.0 with a LICENSE file in the repository root.

The testing skill is the one to read before trusting it. It carries a Socket warn and a Snyk fail, and it is also the skill with the widest blast radius: it starts a dev server, drives a browser against your app, captures screenshots and video of whatever is on screen, and uploads those artifacts to S3. Run it against test data and a throwaway account, and check what bucket and credentials the upload step resolves to in your environment. The review skill (`aiden-review-pr`, Snyk warn) is the other flagged one, and the MCP dependency means its GitHub token scope defines what it can touch.

## Limitations

- Snapshot data, verified 2026-11-07: 6,365 combined installs across 6 indexed listings; 0 GitHub stars; Apache-2.0; last pushed 2026-07-28. Counts drift over time.
- The repository has three names in play. skills.sh indexes it as `supatest-ai/alan-skills`, the README's install commands still say `supatest-ai/aiden-skills`, and GitHub redirects the repository to `tryalan-ai/alan-skills`. The commands here are the README's, kept verbatim; if a future redirect lands a 404, use the current canonical name.
- The tree is smaller than the README. Seven skills are documented, three directories exist, and four (`alan-prd`, `alan-document`, `alan-create-pr`, `alan-check-ci`) have neither a directory nor an install count.
- The six indexed listings map onto three live directories. The three `aiden-*` listings carry 324 to 326 installs each and look like the older name for the same three skills, not additional capability.
- Persistence needs Alan's MCP server (`mcp__alan__*`). Without it the plans, reports and inline comments have nowhere to go, and the workflow has to be re-pointed at your own tools.
- The testing skill needs `agent-browser` installed separately, plus network access for the S3 upload. Neither ships with the skill, and a missing harness stops the workflow rather than degrading it.
- Quiet repository: zero stars and no pushes since 2026-07-28, so the skills have had little outside review and no maintenance signal.

## Related

- [Spec Kit Skills - Specify, Plan, Implement](/hermes/skills/catalog/speckit-agent-skills-setup)
- [Writing Plans Subagent Development Setup](/hermes/skills/catalog/writing-plans-subagent-development-setup)
- [Multi-Agent Review - Adversarial Code Review Setup](/hermes/skills/catalog/multi-agent-review-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `alan-plan`. The plan artifact is what the review and testing skills read later, so skipping it leaves the other two working without context.
- Run the testing skill against a disposable branch and seeded data. It captures real screens and uploads them, so point it at an environment you are happy to see in a bucket.
- Check the harness before the feature. `command -v agent-browser` costs a second and turns a confusing browser failure into an obvious install step.
- Copy the workflow, not the tool calls. The phase order in `alan-test-feature` (scope, strategy, run, capture, report) works with any browser automation you already have.
- Keep the Apache-2.0 LICENSE with any copy you redistribute. The repository ships it in the root, and the skill bodies are the licensed material.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
