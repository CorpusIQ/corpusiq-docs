---
title: "Arize Phoenix Skills - LLM Observability for Agents"
description: "arize-ai/phoenix on skills.sh: 5.5K combined installs; tracing, evals, error analysis and CLI workflows for the self-hosted Phoenix server."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/arize-phoenix-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "llm observability", "evaluation", "tracing"]
---

# Arize Phoenix Skills - Setup Guide

**Source:** [arize-ai/phoenix](https://www.skills.sh/arize-ai/phoenix) via skills.sh - 5,516 combined installs across 8 indexed listings; first seen 2026-11-08 (Nov 8 2026 morning sweep, first documentation)
**GitHub:** 12,201 stars, Elastic License 2.0 at the repo root, last pushed 2026-11-07, 56 SKILL.md directories at the time of the snapshot, of which 5 are the public product skills
**Category:** LLM observability for agents: tracing, evals, error analysis and CLI workflows on the open-source Phoenix server
**Quality Tier:** 🟡 Use With Care - a serious project with 12,201 stars and active commits, but the repo root is Elastic License 2.0 rather than an OSI licence, Snyk warns on two of five sampled skills, and only 8 of 56 skill directories are indexed.

Phoenix is an observability server for LLM applications: it ingests OpenInference spans over OTLP, groups them into traces and sessions, holds datasets and experiments, stores prompt versions, and hosts annotation queues. The five public skills in this repo teach an agent to operate that server properly instead of guessing at the REST API: the `px` CLI for reading and annotating, instrumentation for sending traces, an evaluator workflow, an error analysis method, and a Harbor plugin for agent benchmarks.

The important structural fact for anyone installing these is that the repository is not a skills collection with a product attached. It is a product whose own engineering workflow is stored as skills. Of the 56 SKILL.md directories, 33 live in `.agents/skills/` and are maintainer-facing: docs gap audits, release notes, Storybook, Playwright test conventions, TypeScript package docs. Others are copies that `make skills` writes into the Codex plugin, the MCP server and PXI. Only `skills/` holds the five shipped to users, and only those five carry install numbers.

The five are uneven in weight. `phoenix-evals` is the largest by reference surface, a task-indexed front door into dozens of files covering Python and TypeScript evaluators, datasets, experiments, synthetic data, pytest and vitest CI gates, span filters and judge validation. `phoenix-tracing` is the instrumentation manual: OpenInference conventions, nine span kinds with their attributes, project and session organisation, production batching and masking. `phoenix-cli` is the terminal interface. `phoenix-error-analysis` is a method rather than an API. `phoenix-harbor` wires Phoenix into Harbor agent evaluations.

Do not confuse this with `arize-ai/arize-skills`, which the catalog documents separately. That repository is the vendor's set of skills for the `ax` command line tool; this one is the Phoenix server repository, where the skills drive `px` and the Phoenix REST and GraphQL APIs. Different CLI, different install, different counts.

## Installation

The skills install through the standard CLI, and the repository documents that command in its own package READMEs:

```bash
npx skills add Arize-ai/phoenix
npx skills add Arize-ai/phoenix --skill phoenix-tracing
```

The skills are only useful against a running server. Phoenix self-hosts, and the README's local path is two commands:

```bash
pip install arize-phoenix
phoenix serve
```

`uvx arize-phoenix serve` does the same with no install. The server listens on `localhost:6006` by default. The `phoenix-cli` skill then reads three environment variables:

```bash
export PHOENIX_ENDPOINT=http://localhost:6006
export PHOENIX_PROJECT=my-project
export PHOENIX_API_KEY=your-api-key   # only if auth is enabled
```

For instrumentation there is a setup command rather than hand-written code. From an agent, the skill is emphatic that it must run headless:

```bash
px setup --no-input --endpoint http://localhost:6006 --project my-app --format raw
```

Codex users get a plugin that bundles all five skills plus a launcher for the remote MCP server:

```bash
codex plugin marketplace add .
codex plugin add arize-phoenix@arize-phoenix
```

## What It Provides

The table threshold for this pack is zero, so all eight indexed listings appear below. No rows fall below the threshold and there is no tail.

| Skill | Installs | Use For |
|---|---|---|
| phoenix-cli | 1,771 | Terminal access to traces, spans, sessions, datasets, experiments, prompts and annotation configs, plus raw GraphQL |
| phoenix-tracing | 1,736 | OpenInference instrumentation in Python and TypeScript, custom spans, span kinds, production masking and batching |
| phoenix-evals | 1,674 | Code and LLM-as-judge evaluators over traces or dataframes, experiments, CI gates, judge validation against human labels |
| phoenix-error-analysis | 111 | Reading sampled traces and coding them into annotation dimensions that feed eval design and fix priority |
| phoenix-harbor | 85 | Recording Harbor agent evaluations as Phoenix datasets, experiments, runs and ATIF traces |
| agent-browser | 77 | Browser automation helper indexed under this repo, with no matching directory in the repository tree |
| gh-stack | 59 | Stacked branches and split PRs through the `gh` CLI extension, a GitHub-authored skill vendored here |
| test-integration | 3 | Integration test conventions for work inside the Phoenix repository itself |

The pair with real weight is `phoenix-cli` and `phoenix-evals`. The CLI skill defines a noun-verb surface modelled on `gh`: `px trace list`, `px trace get <id>`, `px trace annotate`, `px span annotate`, `px session get`, `px dataset list`, `px experiment get`, `px prompt-versions list`, `px annotation-config create`, and `px api graphql <query>` for anything the surface does not cover. Two details in it are better than average documentation: every delete is gated behind `PHOENIX_CLI_DANGEROUSLY_ENABLE_DELETES=true` and a confirmation prompt, and `--format raw --no-progress` is prescribed whenever output is piped to `jq`.

`px setup` is the onboarding path and its exit codes are documented as a contract. Missing inputs exit 3 with remediation text, a cancel exits 2, and a run whose trace wait times out exits 6, not 0. That last one matters: configuration and edits are real, but tracing is unconfirmed, and the skill tells the agent to report that as a failure rather than accept the hand-off agent's own summary. The `--format raw` payload includes `tracesVerified`, which is set only when the API saw a trace arrive.

`phoenix-error-analysis` is the one worth reading even if you install nothing. It runs open coding, where each sampled trace, span or session gets a specific written note stored on the server and mirrored to `.px/coding/<identifier>.jsonl`, followed by axial coding, which groups those notes into a few narrow one-dimension annotations with small label sets and counts. It forces an explicit choice of unit before recording, because the failure being hunted may only exist across turns and therefore across traces: session for context loss and goal drift, span for exceptions and malformed output, trace for one-shot classifiers. Dimensions that were not grounded in notes are named as the anti-pattern the workflow exists to prevent.

## Why This Matters for Hermes Agents

An agent that instruments its own work needs somewhere to put the evidence. Phoenix is a reasonable destination because it is self-hosted, speaks OpenTelemetry through OpenInference, and exposes a CLI that produces machine-readable output. The skills close the gap between having a server and using it: without them an agent will invent REST calls, and with them it has the actual command surface and the documented failure codes.

The error analysis method transfers to any agent debugging loop, Phoenix or not. The distinction between open coding and axial coding is the same distinction between generating hypotheses and committing to a measurement, and the insistence that notes be recorded rather than summarised in chat is what stops a diagnosis from evaporating when the context window turns over. If you run multi-agent systems and need to know why a trajectory failed, that is the shape of the work.

For evaluation work the value is the ordering the `phoenix-evals` skill enforces: code-based checks first, an LLM judge only for nuance, and the judge validated against human labels before its scores are trusted. That is a direct antidote to the common failure of shipping a judge prompt that is never checked against anything.

One caveat for Hermes specifically: these skills assume a terminal. `phoenix-cli` declares the `agents` target only, leaving out `mcp` and `pxi` because it needs a shell, so the harness has to allow command execution for the CLI workflows to function.

## Usage

| You say | What happens |
|---|---|
| "What failed in the last 200 traces of this agent?" | Error analysis samples, writes notes per trace, then groups them into counted dimensions |
| "Find every trace where the retrieval step threw" | The CLI lists spans, filters on the failure, and returns ids you can annotate |
| "Build me an evaluator for answer relevance" | Evals picks code-based checks first, then a judge prompt, then a validation run against labels |
| "Compare the last two experiment runs on this dataset" | `px experiment get` reads both runs and the experiments references walk through the comparison |
| "Instrument this FastAPI app and confirm traces arrive" | `px setup --no-input --instrument --agent claude --yolo` writes the files and reports `tracesVerified` |
| "Our chatbot keeps losing context across turns" | The method picks session as the unit, not trace, before recording anything |
| "Record this Harbor benchmark in Phoenix" | The Harbor plugin writes datasets, experiments, runs and ATIF traces |

## Verification

Read the CLI skill before installing anything. This path returned 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/arize-ai/phoenix/main/skills/phoenix-cli/SKILL.md | head -40
```

It should open with frontmatter naming `phoenix-cli`, version 3.5.0, `license: Apache-2.0`, a compatibility line about Node and `@arizeai/phoenix-cli`, and `targets: "agents"`, followed by the invocation block showing `px <resource> <action>` and the `npx` equivalent.

After install, check the server before trusting the skills:

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:6006
npx @arizeai/phoenix-cli project list
npx @arizeai/phoenix-cli trace list --format raw --no-progress
```

The first command should print 200 once `phoenix serve` is up. The second should list projects, including the one `px setup` created. The third should return JSON rather than an error, which confirms the endpoint, the project and the output format all line up.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| phoenix-cli | Pass | Pass | Warn |
| phoenix-evals | Pass | Pass | Pass |
| phoenix-harbor | Pass | Pass | Pass |
| gh-stack | Pass | Pass | Warn |
| test-integration | Pass | Pass | Pass |

The two Snyk warnings land on the two skills that execute destructive commands, and that is structural rather than a packaging accident. `phoenix-cli` can delete traces, spans, sessions, datasets, experiments, prompts and annotation configs, which is exactly what an observability CLI is for. The mitigation is real and documented: deletes require `PHOENIX_CLI_DANGEROUSLY_ENABLE_DELETES=true` plus confirmation, and without the variable the command exits without deleting. Do not export that variable in an environment where an agent runs unattended.

`gh-stack` drives `gh` to rewrite branches and rewrite or reorder pull requests, so its blast radius is your git history on the remote. Treat a stacked-PR skill the way you would treat a force-push.

The bigger governance question is licence, not scanner verdicts. The repository root ships an Elastic License 2.0 file, while individual skills declare `license: Apache-2.0` in frontmatter and the Codex plugin manifest also says Apache-2.0. ELv2 permits internal use, modification and distribution but forbids providing the software to others as a managed service. If you plan to host Phoenix for customers, read the root licence, not the per-skill line.

## Limitations

- Snapshot data, verified 2026-11-08: 5,516 combined installs across 8 indexed listings; 12,201 stars; last pushed 2026-11-07; 56 SKILL.md directories. Counts drift.
- Indexed listings and skill directories do not match, in both directions. Eight listings are indexed against 56 directories. Five of the listings are the public skills in `skills/`; `gh-stack` is a GitHub-authored skill vendored from `github/gh-stack` according to `skills-lock.json`; and `agent-browser` is indexed with no `agent-browser` directory anywhere in the repository tree. Of the 56 directories, 33 are in `.agents/skills/` and aimed at people working on Phoenix itself.
- The repository root is Elastic License 2.0, not MIT or Apache-2.0, despite per-skill and plugin-manifest claims of Apache-2.0. This is the single fact to check before any commercial hosting plan.
- A Phoenix server is mandatory. `phoenix-evals` needs the `phoenix` and `openai` Python packages or `@arizeai/phoenix-client` on the TypeScript side, and `phoenix-harbor` pins Python 3.12 or newer, Harbor 0.21.0 or newer, the `harbor` extra of `arize-phoenix-client`, and Phoenix server 15.0 or newer.
- The Codex plugin is stricter than the skills: it needs Node plus Phoenix 19.0.0 or later, because it bridges to `<PHOENIX_ENDPOINT>/mcp`. The Harbor plugin's live OpenTelemetry path is deferred; it accepts `atif` or `null` trace modes only.
- `px setup` assumes a clean git repository, and an unattended instrument run needs `--yolo` or it stalls waiting for an approval that never comes.
- I could not verify the hosted Arize AX path, PXI, or the MCP server end to end, because those need a deployed instance and credentials. Only the raw skill paths above were confirmed to return 200.

## Related

- [Arize Skills - LLM Observability and Evaluation Setup](/hermes/skills/catalog/arize-skills-setup)
- [Eval Skills - AI Evaluation Workflows for Agents](/hermes/skills/catalog/hamelsmu-evals-skills-setup)
- [AI Evals Skills - Product-Specific Evaluations](/hermes/skills/catalog/ai-evals-skills-setup)

## Pro Tips

- Install the skills after the server, not before. `phoenix-cli` is only meaningful once `PHOENIX_ENDPOINT` resolves, and an agent that meets a connection error first tends to start improvising around the tool.
- Run `px setup --no-input --format raw` and read `tracesVerified` yourself. A run that exits 6 has written real configuration with unconfirmed tracing, and the hand-off agent's summary is not a substitute for that field.
- Pick the analysis unit before the first note. Trace, span and session produce different findings from the same data, and session-level failures such as context loss are invisible at trace level.
- Keep the `.px/coding/` sidecars in the repo or an artefact store. They are the record of what was observed, and they are what makes an annotation run reviewable and revertible later.
- Gate deletes out of unattended environments. Leaving `PHOENIX_CLI_DANGEROUSLY_ENABLE_DELETES` unset is the documented kill switch for `px trace delete`, `px dataset delete` and the rest.
- Prefer code-based evaluators and validate any judge before scaling it. Judge scores that were never checked against human labels are the most expensive kind of noise in an eval dashboard.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
