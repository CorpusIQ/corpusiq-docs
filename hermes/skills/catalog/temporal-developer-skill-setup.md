---
title: "Temporal Developer Skill - Durable Execution"
description: "temporalio/skill-temporal-developer on skills.sh: 5.0K combined installs; one skill for Temporal workflows, activities, workers and durable execution."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/temporal-developer-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "temporal", "durable execution", "workflows", "background jobs"]
---

# Temporal Developer Skill - Setup Guide

**Source:** [temporalio/skill-temporal-developer](https://www.skills.sh/temporalio/skill-temporal-developer) via skills.sh - 5,014 installs across 1 indexed listing (5.0K combined); first seen 2026-11-08 (Nov 8, 2026 evening sweep)
**GitHub:** 236 stars, MIT via LICENSE, `main` branch, last pushed 2026-11-05, 1 SKILL.md at the repository root with a `references/` tree beside it
**Category:** Backend and workflows: durable execution, Temporal workflows, activities, retries and worker patterns across eight SDK languages
**Quality Tier:** 🟢 Production - official Temporal repository, MIT license, Pass on all three scanners, and a reference tree that covers eight SDK languages.

Temporal is a durable execution platform: workflows are replayed from an event history after a crash, which is why a workflow function may not read the clock, roll a random number or call an API directly. This repository is the official Temporal skill for that problem, and it is a routing document rather than a tutorial. `SKILL.md` is 115 lines. It names the eight supported SDKs, states what is out of scope, and hands the agent a reference file to read for the actual task, under `references/core/` for language-neutral guidance and `references/{language}/` for the SDK-specific counterpart.

The adoption numbers are unusual for a skill this shape. 5,014 installs against 236 stars means the skill is being pulled by the skills CLI and by the plugin wrappers rather than found on GitHub, and the newest commit, 2026-11-05, added PHP SDK support with eleven reference files, so coverage of the eight languages is not uniform and is still moving.

## Installation

The README offers two routes: a plugin wrapper per agent, or the standalone skill. The plugin route is the one it recommends, because it "provides a simple way to install and receive future updates". The three wrappers are separate repositories:

- **Claude Code**: [temporalio/claude-temporal-plugin](https://github.com/temporalio/claude-temporal-plugin)
- **Cursor**: [temporalio/cursor-temporal-plugin](https://github.com/temporalio/cursor-temporal-plugin)
- **OpenAI Codex**: [temporalio/codex-temporal-plugin](https://github.com/temporalio/codex-temporal-plugin)

Each wrapper carries its own installation instructions, which this guide does not restate because they are versioned independently of the skill itself.

The standalone route supports all major coding agents through the skills CLI:

```bash
npx skills add temporalio/skill-temporal-developer
```

Then follow the prompts. For a manual clone, the README gives one line each for Claude Code and Codex.

Claude:

```bash
mkdir -p ~/.claude/skills && git clone https://github.com/temporalio/skill-temporal-developer ~/.claude/skills/temporal-developer
```

Codex:

```bash
mkdir -p ~/.agents/skills && git clone https://github.com/temporalio/skill-temporal-developer ~/.agents/skills/temporal-developer
```

Both commands end by naming the clone directory `temporal-developer`, and that part is not cosmetic. This repository has no `skills/` subdirectory: `SKILL.md` and `references/` sit at the root, so the clone directory becomes the skill directory and its basename becomes the name the client indexes. The README does not give a manual clone line for Cursor, so Cursor installs through the plugin repository.

## What It Provides

The threshold for this guide is zero installs, so the single indexed listing appears below:

| Skill | Installs | Use For |
|---|---|---|
| temporal-developer | 5,014 | Building and debugging Temporal workflows, activities and workers across eight SDK languages, with the determinism, versioning, retry and job queue patterns that the platform requires |

One row clears the threshold, and since the threshold is zero no rows fall below it.

The design is progressive disclosure, and it is the reason a 115-line body is enough. The body splits the task into language selection, core architecture, a determinism section explaining history replay, and a reference index. The core index lists sixteen files under `references/core/`, including determinism, patterns, gotchas, versioning, standalone activities, priority and fairness, random streams, troubleshooting, an error reference, interactive workflows, dev management, Docker Compose, CLI workflow commands, job queue and AI patterns. Each has a per-language counterpart where the SDK differs, and the language directories range from eighteen files for Python to a single file for Rust.

Two positions in the body are worth quoting because an agent gets both wrong by default. The first is that the job queue answer is a standalone activity: when a developer asks for background jobs, a work queue, or whether Temporal can replace Celery, Sidekiq, BullMQ or SQS plus workers, the skill builds it with a standalone activity rather than a workflow wrapping one activity, and it states that PHP and Rust have no standalone activity support and need the fallback guide. The second is that Temporal task queues are the routing mechanism workers poll, not a queue that producers push jobs into, and the skill warns against answering a job queue question by describing task queues.

The references carry the operational detail: a workflow diagnosis decision tree that starts from status and branches on whether a worker is running, whether it is on the correct task queue, whether the code is stale, and whether the workflow is waiting for a signal; a non-determinism tree that separates intentional changes from accidental ones; a versioning guide with three approaches and a table mapping change size to approach; and an integrations catalog for third-party frameworks such as Spring Boot, Spring AI, the OpenAI Agents SDK and Google ADK.

## Why This Matters for Hermes Agents

Hermes runs long tasks that must survive a restart, and Temporal is the reference implementation of that problem. The overlap is direct: retries that duplicate side effects, work that resumes after a process dies, and code that has to be replayed rather than re-executed. The skill's gotchas reference opens with non-idempotent activities, which is the same failure an agent produces when it retries an email send or a payment call without a key.

The second fit is that this skill is written as decisions rather than prose. The troubleshooting and determinism references are trees with a check at each node, which is the form an instruction survives in a long context. An agent asked to debug a stuck workflow will follow "is a worker running, is it on the right task queue, is the code stale, is it waiting for a signal" in order, where a general explanation of durable execution gives it nothing to do.

The third is the correction it applies to confident answers. Temporal looks like a job queue and is not one; workflows look like ordinary functions and are not; a changed activity name looks harmless and breaks every running workflow. Each of those is a place where a model without the skill produces a plausible, wrong answer, and the skill contains an explicit refutation for each.

The honest counterweight: this skill writes and debugs application code, it does not operate the cluster. Operational CLI work, serverless workers, and first-time Cloud setup live in `temporalio/skill-temporal-ops`, `temporalio/skill-temporal-serverless` and `temporalio/skill-temporal-cloud-setup`, three separate repositories that this install does not include. Installing this one alone leaves the agent able to build a workflow and unable to administer the namespace it runs in.

## Usage

| You say | What happens |
|---|---|
| "My workflow throws NondeterminismError after a deploy" | Splits intentional from accidental change, then routes to the patching API for in-flight production workflows or terminate and restart for local development, from the determinism and versioning references |
| "A workflow is stuck in RUNNING and nothing moves" | Walks the troubleshooting tree in order: worker running, correct task queue, stale code, pending signal or timer, then `temporal workflow show --workflow-id <id>` to read WorkflowTaskFailed |
| "Design retries for an activity that calls a flaky API" | Keeps the retry policy and timeouts in the activity, keeps the workflow deterministic, and requires an idempotency key built from the workflow ID or activity ID |
| "I need to change a running workflow's code" | Chooses between the patching API, workflow type versioning and worker versioning, using the table that maps change size and workflow lifetime to approach |
| "This workflow runs for months and the history is huge" | Recommends continue-as-new, and for worker versioning pairs it with the behaviour that lets the new run start on the target version |
| "Start a local Temporal server" | Checks whether `temporal` is installed first, follows the CLI installation guide if not, then runs `temporal server start-dev` with the gRPC port on 7233 and the web UI on 8233 |
| "Can Temporal replace Celery for background jobs" | Answers with a standalone activity rather than a workflow wrapping one activity, and notes that PHP and Rust have no standalone activity support |

## Verification

The skill sits at the repository root, so there is no `skills/` segment in the raw path. This URL returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/temporalio/skill-temporal-developer/main/SKILL.md | head -6
```

It should open with YAML frontmatter holding `name: temporal-developer` and a long `description` that lists the eight languages together with the trigger phrases the skill activates on, such as `temporal server start-dev` and `temporal workflow signal`. Below the closing delimiter you should see `# Skill: temporal-developer`. There is no `license`, `version` or `homepage` field in this frontmatter, so those are not part of the check.

The references have to arrive with it, because the body is a router:

```bash
curl -fsSL https://raw.githubusercontent.com/temporalio/skill-temporal-developer/main/references/core/troubleshooting.md | head -5
```

That should return the troubleshooting heading and the start of the workflow diagnosis decision tree. A 404 here means the relative links in the body no longer resolve and every deep reference has moved.

After a manual clone, confirm the skill landed in the directory the client reads, not one level above it:

```bash
test -f ~/.claude/skills/temporal-developer/SKILL.md && echo ok
```

## Security

skills.sh verdicts for the single indexed skill (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| temporal-developer | Pass | Pass | Pass |

The skill is Markdown and reference files, with no installer, no scripts and no network calls of its own. All three scanners returning Pass reflects that absence of executable payload, not an audit of the workflows an agent will write with it.

The surface that matters is the code the skill describes. A Temporal application holds database credentials, keys for whatever its activities call, and the authority to mutate external systems once per attempt, which is exactly what a retry multiplies. Audit activity code the way you would audit a web handler, and keep credentials in the worker environment rather than in files an agent is editing.

The dev server is the other loose end. The skill documents `temporal server start-dev` as suitable for development and testing only, and it should stay on localhost: 7233 is the gRPC frontend that workers and clients connect to, and 8233 is the web UI. Keep both on loopback and do not open either beyond the machine.

One behaviour is worth knowing before install. The skill instructs the agent to draft a GitHub issue when a reference is wrong or a concept is proving hard to use, and to ask the user to file it, explicitly not to file autonomously. That is the right default, and it means feedback needs a human in the loop.

## Limitations

- Snapshot data, verified 2026-11-08: 5,014 combined installs across 1 indexed listing; 236 GitHub stars; MIT license; last pushed 2026-11-05. Counts drift over time.
- The skill sits at the repository root, so a manual clone has to land in the directory the client expects (`~/.claude/skills/temporal-developer` or `~/.agents/skills/temporal-developer`). Cloning into a directory with a different name changes the skill name the client shows, and there is no `skills/` path to fall back on.
- The plugin wrapper repositories are separate and versioned independently, and their install steps are not covered here. A plugin install and an npx install can sit on different skill versions at the same time.
- 5,014 installs against 236 stars is a distribution signal, not an evaluation one: the CLI and the plugin wrappers both count, and with one indexed listing there is no second source to cross-check the number.
- Language coverage is uneven and the skill says so itself. Rust is Public Preview with a single reference file, PHP and Rust have no standalone activity support, AI patterns exist for Python only, and named random streams exist for Go and TypeScript.
- The repository has no release tags and no version field in `SKILL.md`, so a pin means pinning a commit hash, and the troubleshooting and versioning references move with `main`.

## Related

- [III Workers Hermes Bridge - Setup Guide](/hermes/skills/catalog/iii-workers-hermes-setup)
- [Cron Design Workflow - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/cron-design-workflow-setup)
- [OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read the reference the body names, not the body alone. The 115 lines are a router, and an agent that answers from them will generalise across eight SDKs and be wrong about the one in use.
- Make the agent state the SDK language before it answers anything. Language selection is the first branch, and every core reference has a per-language counterpart under `references/{language}/`.
- For a failed workflow after a deploy, decide first whether the change was intentional. The determinism tree splits patching for in-flight production workflows from terminate and restart for local development, and taking the wrong branch discards state you needed.
- Start every stuck workflow investigation with the task queue, not the code. Most of the troubleshooting tree is downstream of whether a worker is polling the queue the workflow was started on.
- Give every activity an idempotency key built from the workflow ID and activity ID. Retries and worker failures make at-least-once the normal case, and this is the gotcha that costs money when it is missed.
- Prefer the CLI dev server over Docker Compose unless you need containers. The skill's own guidance defaults to `temporal server start-dev` and asks you to check the server management criteria before reaching for Compose.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
