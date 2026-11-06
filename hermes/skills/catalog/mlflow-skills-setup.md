---
title: "MLflow Skills - Tracing, Evaluation and LLMOps"
description: "mlflow/skills on skills.sh: 10.8K combined installs across 21 listings; MLflow tracing, trace analysis, GenAI evaluation and SageMaker backend setup."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mlflow-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "mlflow", "llmops", "evaluation"]
---

# MLflow Skills - Setup Guide

**Source:** [mlflow/skills](https://www.skills.sh/mlflow/skills) via skills.sh - 10.8K combined installs across 21 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 89 stars, Apache-2.0 licence (LICENSE in the repo root), last pushed 2026-11-04, 10 SKILL.md directories at the repository root plus a .claude-plugin manifest, a hooks/ directory and a scenario test harness
**Category:** LLMOps for agents: MLflow tracing, evaluation, trace analysis and onboarding plus SageMaker deployment
**Quality Tier:** 🟡 Review - Apache-2.0 and a well-tested layout, but one sampled skill carries a Snyk Warn and the install index still lists eleven pre-refactor skill names that no longer have directories.

MLflow Skills is the MLflow project's own skill set for coding agents: ten skills at the repository root that give a coding agent working knowledge of MLflow tracing, evaluation and observability. It works with any agent that reads skills, including Claude Code, Cursor, Codex CLI, Gemini CLI and OpenCode, and the README's pitch is narrow and credible: add tracing to an app, explain why a trace failed, evaluate an agent and then improve it against that evaluation.

The structure is a dispatcher plus specialists. `mlflow-agent` routes a broad request to the right skill; `mlflow-onboarding` decides between the GenAI and classic ML paths; `mlflow-docs` searches the official documentation; `mlflow-sagemaker` connects to SageMaker Managed MLflow; and the five trace and evaluation skills cover instrumentation, retrieval, analysis, aggregate metrics and scorer design. There is also an optional `UserPromptSubmit` hook in `hooks/` that watches a prompt for MLflow patterns and surfaces the matching skill before the agent answers.

## Installation

Through the Agent Skills CLI:

```bash
npx skills add mlflow/skills
```

Directly from source:

```bash
git clone https://github.com/mlflow/skills.git
cp -r mlflow-skills/* ~/.claude/skills/
```

The README notes that you should change `~/.claude/skills/` to the right location for your agent, for example `~/.codex/skills/` for Codex. For team sharing, the project-level route clones into the repository instead:

```bash
cd your-project
git clone https://github.com/mlflow/skills.git .skills/mlflow
# Or as a submodule:
git submodule add https://github.com/mlflow/skills.git .skills/mlflow
```

The optional hook installs in two steps. Copy it somewhere permanent:

```bash
cp hooks/mlflow-suggest-hook.py ~/.claude/hooks/mlflow-suggest-hook.py
```

Then register it in `~/.claude/settings.json` under `hooks` as a `UserPromptSubmit` command running `python3 ~/.claude/hooks/mlflow-suggest-hook.py`. The README's example output is a one-line suggestion naming the skill, which is a convenience rather than a requirement: without the hook you name the skill yourself.

The one hard prerequisite is stated in the README's Requirements section: MLflow 3.8 or newer, with the instructions and code examples tested against that version.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| mlflow-onboarding | 1,161 | Determines the use case, GenAI agent or classic ML, and walks the matching quickstart, reusing an existing experiment when one is supplied |
| agent-evaluation | 1,062 | Evaluates or improves an existing agent's output quality with MLflow datasets, scorers and tracing, loading the tracing skill alongside |
| searching-mlflow-docs | 1,059 | Searches and retrieves the official MLflow documentation for features, APIs, integrations, tracing and tracking |
| instrumenting-with-mlflow-tracing | 1,056 | Adds or repairs tracing in Python and TypeScript apps: framework autologging, custom spans, backend setup and persisted-trace verification |
| analyzing-mlflow-trace | 1,012 | Explains a failing trace span by span: errors, unexpected output, quality issues and latency, without editing application code |
| retrieving-mlflow-traces | 991 | Finds a trace by ID or filters traces by run, session, user, status, time, tags, feedback and span fields |
| analyzing-mlflow-session | 966 | Multi-turn session diagnosis: ordered turns, the first incorrect answer, and how the error propagates across the conversation |
| querying-mlflow-metrics | 959 | Aggregate trace metrics from the tracking server: token usage, latency, trace counts and quality trends |
| mlflow-agent | 835 | The dispatcher: routes any broad MLflow request to the right sub-skill |

The remaining 12 indexed listings range from 35 to 394 installs. `sagemaker-mlflow` (394), `fix-agent-issue` (376), `build-a-scorer` (339) and `debug-agent` (232) sit at the top of that tail, and the eight listings that match current directory names, from `mlflow-evaluation` (49) down to `mlflow-sagemaker` (35), sit at the bottom.

The naming split is the thing to know before installing. The install index carries 21 names against 10 directories: the ten listings named `mlflow-*` match the directories in the current tree, while eleven names such as `agent-evaluation` and `analyzing-mlflow-trace` are pre-refactor labels with no directory in the current tree. Nine of those eleven still have history in the repository, and the two trace names, `analyzing-mlflow-trace` and `analyzing-mlflow-session`, have no directory in the current tree or in the commits the API exposes; both describe work that now lives under `mlflow-trace-analysis`.

## Why This Matters for Hermes Agents

An agent that cannot see what it did cannot debug itself. Tracing gives it spans, assessments and a persisted record; without that, "why did this answer come out wrong" is answered by re-reading the prompt and guessing. The instrumentation skill is the entry point that makes every later question answerable, which is why the evaluation skill tells the agent to load it alongside.

The evaluation skills are where this stops being observability and becomes a loop. `mlflow-agent-improvement` is explicit about the sequence: diagnose from traces, prove a regression test fails, implement the smallest fix, then verify it passes without breaking existing behaviour. That is a discipline an agent will otherwise skip in favour of a plausible patch, and encoding it as a skill is more durable than repeating it in a prompt.

The multi-turn analysis skills matter because most agent failures have nothing to do with a single call. An error in turn four often starts in turn two, and `analyzing-mlflow-session` describes exactly that shape: ordered turns, the first incorrect answer, then propagation. Aggregate metrics answer a different question again, which is whether quality and cost are trending in the right direction rather than whether one trace failed.

The repository is also honest about its own limits, which is worth knowing before trusting its verdicts. The README says the scenario harness runs a real agent against a real MLflow server, that merely mentioning an API or reporting success does not pass, and that live SageMaker, Databricks online monitoring and distributed tracing still need dedicated environments. A skill set that states what its tests do not cover is easier to reason about than one that claims a green run means production readiness.

## Usage

| You say | What happens |
|---|---|
| "Add MLflow tracing to my LangChain app" | instrumenting-with-mlflow-tracing detects the framework, adds the autolog call, configures the experiment and verifies traces are captured |
| "Why did this trace return the wrong answer" | analyzing-mlflow-trace walks the span tree, checks assessments, finds the failure point and suggests a fix |
| "Set up evaluation for my support agent" | agent-evaluation creates or reuses a dataset, picks scorers, runs the evaluation and analyses the results |
| "Show me token usage for the last seven days" | querying-mlflow-metrics pulls aggregate metrics and breaks down cost and latency trends |
| "I need to get started with MLflow" | mlflow-onboarding decides between the GenAI and classic ML paths and walks the matching quickstart |
| "Find the traces for this user that failed" | retrieving-mlflow-traces filters by user, status, tags and time and returns the matching trace IDs |
| "Connect to our SageMaker MLflow" | mlflow-sagemaker takes the ARN, verifies the connection and hands off to the other skills |

## Verification

Read the two skills that touch a real tracking server before installing them:

```bash
curl -fsSL https://raw.githubusercontent.com/mlflow/skills/main/mlflow-onboarding/SKILL.md | head -5
curl -fsSL https://raw.githubusercontent.com/mlflow/skills/main/mlflow-trace-analysis/SKILL.md | head -5
```

Both return 200 on the `main` branch, and both are at the repository root with no `skills/` prefix. The first should open with `name: mlflow-onboarding` and a description about determining the use case and guiding the quickstart. The second should describe analysing traces, agent failures and multi-turn chat sessions without editing application code.

Then install and confirm the ten skills landed:

```bash
npx skills add mlflow/skills
ls ~/.claude/skills/mlflow-onboarding ~/.claude/skills/mlflow-trace-analysis
```

Each directory should hold SKILL.md, and several also carry a `references/` folder: `mlflow-evaluation` ships scorer, dataset, judge-alignment and throughput references, and `mlflow-trace-analysis` ships trace-structure and session-analysis references. Those are the files the skill reads when a task gets past the basics.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| mlflow-onboarding | Pass | Pass | Pass |
| retrieving-mlflow-traces | Pass | Pass | Warn |
| fix-agent-issue | Pass | Pass | Pass |
| mlflow-trace-metrics | Pass | Pass | Pass |
| mlflow-sagemaker | Pass | Pass | Pass |

One Warn in the sample, on `retrieving-mlflow-traces`, the skill that queries a tracking server for traces by ID, user and time. The verdict is a reason to read its query construction before pointing it at a shared server, not a reason to avoid it.

Two operational surfaces are worth naming. The skills execute against a live MLflow backend, so a wrong experiment ID or tracking URI writes to the wrong place, and the SageMaker skill needs AWS credentials and an ARN. The optional hook edits `~/.claude/settings.json` and runs a Python script on every prompt, which is a real change to your agent environment; read `hooks/mlflow-suggest-hook.py` before registering it, and skip the hook if you would rather not have a per-prompt process.

## Limitations

- Snapshot data, verified 2026-11-06: 10,794 combined installs across 21 indexed listings; 89 GitHub stars; Apache-2.0; last pushed 2026-11-04. Counts drift over time.
- The install index outruns the tree. 21 listings map to 10 directories: eleven names are pre-refactor names, nine of which have directories in history and two of which, analyzing-mlflow-trace and analyzing-mlflow-session, never had one. Installing by the old names is not possible; install `mlflow-trace-analysis` for that work.
- MLflow 3.8 or newer is a hard requirement. The instructions and examples are tested against 3.8, and the test harness against 3.17.1, so advice written for one version can miss in another.
- The test harness is not a CI gate. Running the scenarios needs an authenticated `claude` CLI, Git, Node and npm, and `uv`; the README states the repository has no CI workflow that launches the paid Claude scenarios automatically.
- Discovery is a known weak point in that harness. The README says the dispatcher currently disables automatic invocation, so its required-loading check can expose a discovery limitation, which is a reason to name the skill explicitly when you need one.
- Versions of the older skills are gone from the tree. If you want to read what an old name did, you have to fetch its SKILL.md at a historical commit, which is a worse experience than reading the current documentation.

## Related

- [AI Research Skills - 100-Skill ML Research Library Setup](/hermes/skills/catalog/ai-research-skills-setup)
- [Databricks Agent Skills - Data & AI Platform Skills](/hermes/skills/catalog/databricks-agent-skills-setup)
- [LLM Code Skills - Cross-Tool Documentation Pack](/hermes/skills/catalog/llm-code-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `mlflow-onboarding` even if you think you know the setup. It picks the GenAI or classic ML track and reuses an existing experiment instead of creating a second one.
- Never ask for evaluation before tracing works. A dataset and a scorer over untraced code gives you numbers with no way to explain them.
- Ask for the failing span, not the failing trace. The analysis skill walks the tree to the specific child span; that detail is what makes a fix possible.
- Use `mlflow-agent-improvement` for the fix, not a bare patch request. The skill's four steps, diagnose, prove the regression, smallest fix, verify, are the part that keeps a repair from becoming a rewrite.
- Read `references/` inside `mlflow-evaluation` before designing scorers. Scorer design, judge alignment and dataset preparation each have their own file, and the top-level skill only summarises them.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
