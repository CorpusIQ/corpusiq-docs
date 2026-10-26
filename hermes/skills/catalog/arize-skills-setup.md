---
title: "Arize Skills - LLM Observability and Evaluation Setup"
description: "Arize official skills: 38.8K combined installs. Eighteen ax CLI skills for tracing, datasets, experiments, evaluators and compliance audits."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/arize-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "llm observability", "evaluation"]
---

# Arize Skills - Setup Guide

Arize publishes 18 skills that teach a coding agent to do observability work on an LLM application: add tracing, export and debug traces, build datasets, run experiments, create LLM-as-judge evaluators, annotate spans, manage Prompt Hub templates, migrate off a competing platform, and audit a system against compliance frameworks. Every skill drives the `ax` CLI rather than inventing API calls.

The repo is the vendor's own, under MIT, at version 1.2.0. It ships an installer for macOS, Linux and Windows, a pytest suite that exercises the health checks and migration paths, CI validation for skill structure and links, and release-please versioning.

**Source:** [arize-ai/arize-skills](https://www.skills.sh/arize-ai/arize-skills) via skills.sh - 38.8K combined installs across 18 indexed listings; first seen Mar 10, 2026
**GitHub:** [Arize-ai/arize-skills](https://github.com/Arize-ai/arize-skills) (67 stars; MIT; branch main, pushed 2026-10-22; layout `skills/arize-<area>/SKILL.md` for all 18 skills, with supporting `references/` and, for the migration skills, `scripts/migrate_vendor_traces.py`)
**Category:** AI Observability / LLM Evaluation
**Quality Tier:** 🟢 Production - official Arize repo under MIT, all 18 indexed listings resolve to a real skill directory, a pytest suite plus CI skill validation, versioned releases at 1.2.0, and sampled verdicts Pass except a Snyk warn on arize-trace

## Installation

```bash
# Install every skill non-interactively, which is what the README's own prompt does
npx skills add Arize-ai/arize-skills --skill "*" --yes

# Or run the interactive wizard and pick skills, agent and scope
npx skills add Arize-ai/arize-skills
```

```bash
# Prerequisite: the ax CLI, plus one authenticated profile
uv tool install arize-ax-cli
ax profiles create --api-key YOUR_API_KEY
export ARIZE_SPACE="my-workspace"

# Or skip profiles and use environment variables directly
export ARIZE_API_KEY="your-api-key"
```

```bash
# Git clone path, which also installs the ax CLI if it is missing
git clone https://github.com/Arize-ai/arize-skills.git
cd arize-skills
./install.sh --project ~/my-project
```

```bash
# Already on ax v0.39.0 or newer: install through the CLI instead of npx
ax skills install --agent claude-code --yes
```

Install order matters: most SKILL.md files declare `compatibility: Requires the ax CLI and a configured Arize profile`, and a handful pin `ax` 0.39.0 or newer. `ARIZE_SPACE` (a space name or base64 ID from `ax spaces list -o json`) is the second required value, and the evaluator skill also needs an AI integration configured so a judge model can be called.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| arize-instrumentation | 3,443 | Add Arize AX tracing to an app for the first time: detect the stack, route to the matching integration doc, wire auto-instrumentation after confirmation, verify traces land |
| arize-prompt-optimization | 3,283 | Improve a prompt from production evidence: extract prompts from spans, gather eval and annotation signal, run a data-driven optimization loop |
| arize-trace | 3,226 | Export and inspect existing traces, spans and sessions by ID, and root-cause runtime errors, latency and behaviour regressions |
| arize-experiment | 3,112 | Create, run and analyse experiments against datasets, export runs, and compare model versions or prompts |
| arize-dataset | 3,110 | Dataset and example CRUD, append examples, export data, build golden sets from files |
| arize-evaluator | 3,082 | Create LLM-as-judge and code evaluators, score spans or experiments, map columns, trigger runs, and set up continuous monitoring |
| arize-link | 3,048 | Generate deep links to projects, traces, spans, sessions, datasets, experiments, labeling queues and evaluators in the Arize UI |
| arize-ai-provider-integration | 3,016 | Create and manage stored LLM provider credentials for OpenAI, Anthropic, Azure OpenAI, Bedrock, Vertex, Gemini, NVIDIA NIM, Fireworks and Together |
| arize-annotation | 2,994 | Define annotation configs (categorical, continuous, freeform) and queues, then apply human labels to spans via the Python SDK |
| arize-compliance-audit | 2,645 | Scan an agent for gaps against EU AI Act, GPAI Code of Practice, GDPR, NIST AI RMF, Colorado AI Act, HIPAA and ISO 42001, and produce a remediation checklist |
| arize-admin | 2,363 | Enterprise admin: users, organizations, spaces, projects, roles, role bindings, resource restrictions and API keys, including SAML/SSO role mapping |
| arize-prompts | 2,289 | Prompt Hub workflows with ax prompts: author or import templates, save, label and promote, edit, duplicate, delete |
| arize-span-routing | 1,200 | Send each agent's or tenant's Python spans to the correct space and project with OpenTelemetry routing (register_with_routing, set_routing_context) |
| arize-instrumentation-health | 1,000 | Audit existing instrumentation with deterministic checks: orphaned, uncategorized or duplicate spans, flat structure, blank root I/O, unset status, missing token counts |

The remaining 4 indexed listings range from 177 to 469 installs: arize-phoenix-migration (469), which imports Phoenix project traces into Arize AX, and three vendor migrations at arize-migrate-langsmith (178), arize-migrate-braintrust (177) and arize-migrate-langfuse (177), each covering OTLP trace import, dataset import, prompt and evaluator recreate, and an optional live cutover.

## Why This Matters for Hermes Agents

An LLM application fails quietly. The request returns, the user is unhappy, and nothing in the logs explains why. Tracing is the only way to see the prompt, the retrieval, the tool calls and the cost of one request. `arize-instrumentation` turns that from a research project into a two-phase procedure the agent can execute and then verify, and `arize-trace` turns an exported span into a readable story about where a request went wrong.

The ax CLI is the friction point these skills remove. Flags, JSON output shapes, space and project resolution, pagination and column mapping are all documented in the SKILL.md files, so the agent stops guessing `--space` semantics or inventing a filter syntax. Where a real trap exists the skill says so, for example that `ax spaces list` paginates and can silently omit the target space.

There is also a genuine evaluation loop here, not just a dashboard. Datasets feed experiments, experiments are scored by evaluators, annotations add human judgement, and `arize-prompt-optimization` uses all three as evidence to change a prompt. That is the workflow most agent builders describe and rarely wire end to end.

The health check is the piece worth installing even if you touch nothing else. `arize-instrumentation-health` runs deterministic checks over a bounded span sample and returns a ranked report, which answers the specific question of why eval scores or cost dashboards show zero: the spans are orphaned, flat, or missing token counts.

## Usage

| You say | What happens |
|---|---|
| "Add tracing to this app" | Loads arize-instrumentation, detects the framework, applies the matching integration doc after confirmation, then verifies a trace landed in the project |
| "Why is this request slow?" | Loads arize-trace, exports the trace, and reports where latency sits across spans, tools and model calls |
| "Build a golden dataset from our last 200 production traces" | Loads arize-dataset, exports spans and creates a dataset of examples ready for experiments |
| "Compare prompt v3 against v4" | Loads arize-experiment with the dataset, runs both, then arize-evaluator scores them and the results are compared |
| "Why do my token and cost charts show zero?" | Loads arize-instrumentation-health, runs the deterministic checks, and ranks the instrumentation defects that break token accounting |
| "We need a HIPAA and EU AI Act gap check" | Loads arize-compliance-audit, scans the codebase and instrumentation coverage, and returns a framework-by-framework remediation checklist |
| "Onboard the new data team into its own space" | Loads arize-admin, creates the space, role bindings and service key, and confirms before any destructive operation |

## Verification

Confirm what the skills CLI installed, and that the CLI the skills call is present:

```bash
npx skills list | grep -i arize
ax --version && ax profiles show
```

Read the skills before installing. The five URLs below returned 200 with `curl -s -o /dev/null -w "%{http_code}"` when checked on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/Arize-ai/arize-skills/main/README.md
curl -sL https://raw.githubusercontent.com/Arize-ai/arize-skills/main/skills/arize-instrumentation/SKILL.md
curl -sL https://raw.githubusercontent.com/Arize-ai/arize-skills/main/skills/arize-trace/SKILL.md
curl -sL https://raw.githubusercontent.com/Arize-ai/arize-skills/main/skills/arize-admin/SKILL.md
curl -sL https://raw.githubusercontent.com/Arize-ai/arize-skills/main/skills/arize-instrumentation-health/SKILL.md
```

The repo is capitalised `Arize-ai` in the GitHub owner path and lowercase `arize-ai` on skills.sh, so use `Arize-ai/arize-skills` in install commands and raw URLs, and `arize-ai/arize-skills` on the skills.sh pages.

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| arize-instrumentation | Pass | Pass | Pass |
| arize-trace | Pass | Pass | Warn |
| arize-admin | Pass | Pass | Pass |

No SKILL.md in the repo declares an `allowed-tools` field, so the skills inherit whatever your host agent already permits and nothing here escalates it. What they do have is an API key: every skill authenticates to Arize through `ax`, using either a stored profile or `ARIZE_API_KEY` plus `ARIZE_SPACE` in the environment, and the README recommends the profile so the key is not exported into every session.

Three behaviours deserve review before production use. First, `arize-instrumentation` edits application source to add tracing, which is a code change, done after user confirmation by design. Second, `arize-admin` carries destructive `ax` commands behind `--force`: users, organizations, spaces, projects, roles, role bindings, resource restrictions and API keys, where `ax spaces delete` and `ax projects delete` also destroy the traces and datasets inside them. The SKILL.md states a rule to never run a `--force` destructive command without confirming with the user first, and that rule is the only thing standing between a misread prompt and an irreversible delete. Third, the three `arize-migrate-*` skills ship `scripts/migrate_vendor_traces.py`, which reads source-vendor credentials (`LANGSMITH_API_KEY`, `BRAINTRUST_API_KEY` or `LANGFUSE_*`) and posts OTLP data to Arize, so those credentials enter the same process that holds your Arize key.

Two further notes from the README. `arize-compliance-audit` is guidance only and does not constitute legal advice or a complete compliance assessment. And the repo's own test harness runs Claude Code in `bypassPermissions` mode, which the README says is only safe with a deny list for destructive shell commands; that harness is a maintainer tool, not part of the installed skills.

## Limitations

- The skills are a thin, high-quality layer over `ax`. They need the CLI installed and an Arize account with an API key and space, so without credentials they can only explain what to do.
- `arize-evaluator` and anything that calls a judge model need an AI integration configured first. The SKILL.md compatibility line says so; a session without one will stop at the setup step.
- `arize-instrumentation-health` has a directory and 1,000 installs but is absent from the README's Available Skills table, which lists 17 of the 18 skills.
- Admin work needs org-admin privileges, and the deletes are irreversible. `ax spaces delete` and `ax projects delete` take their traces, datasets and evaluations with them.
- `arize-compliance-audit` maps code patterns to published frameworks. It is explicitly not legal advice and cannot know your contractual or jurisdictional obligations.
- 67 GitHub stars is modest for the install volume, so the install counts and the vendor ownership are the stronger signals here.
- Snapshot data, verified Oct 26, 2026: 38,812 combined installs across 18 indexed listings; 67 GitHub stars; MIT; last pushed 2026-10-22. Counts drift over time.

## Related

- [Langfuse Agent Skills - LLM Observability Setup](/hermes/skills/catalog/langfuse-agent-skills-setup) - the same observability job on a different platform, and the source side of arize-migrate-langfuse.
- [LangSmith Skills - LLM Evaluation & Tracing Setup](/hermes/skills/catalog/langsmith-skills-setup) - evaluation and tracing workflows, useful for comparison or migration planning.
- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup) - infrastructure and application monitoring alongside LLM-level tracing.
- [Hermes Labyrinth - Observability Dashboard Plugin for Hermes Agent](/hermes/skills/catalog/hermes-labyrinth-observability-setup) - observability for the agent runtime itself, not the app it is instrumenting.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Create an `ax` profile once instead of exporting `ARIZE_API_KEY` everywhere. The README recommends it, and it keeps the key out of every shell and every agent session.
- Set `ARIZE_SPACE` before the first instrumentation run. Nearly every skill needs a space, and the skills will stop to resolve one mid-task if it is missing.
- Start with arize-instrumentation and then arize-instrumentation-health as a pair. Instrumenting without the health audit leaves the empty-span and missing-token failures to be discovered by a dashboard nobody trusts.
- Keep arize-admin out of always-on installs. It is the only skill group with irreversible deletes, so scope it to an admin session with the key that can perform them.
- Run the compliance skill as a gap-finder, not a sign-off. Its own README says it cannot account for your legal obligations, and the output is a checklist to take to a lawyer or compliance owner.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*