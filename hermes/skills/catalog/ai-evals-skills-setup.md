---
title: "AI Evals Skills - Product-Specific Evaluations"
description: "ai-evals-course/evals-skills on skills.sh: 9.5K combined installs across 11 listings; nine skills for error analysis, judge prompts and eval audits."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ai-evals-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "ai evals", "llm testing", "error analysis"]
---

# AI Evals Skills - Setup Guide

**Source:** [ai-evals-course/evals-skills](https://www.skills.sh/ai-evals-course/evals-skills) via skills.sh - 9.5K combined installs across 11 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 1,716 stars, Apache-2.0, last pushed 2026-09-24, 9 SKILL.md directories, one per skill under `skills/`, with the Claude Code plugin manifest in `.claude-plugin/`
**Category:** Evaluation work for agents: eval audits, error discovery, synthetic data, RAG evaluation and evaluator validation
**Quality Tier:** 🟢 Green - all five sampled skills pass all three scanners, the licence is Apache-2.0, and the only executable part is a local review server the agent builds.

These skills come out of the AI Evals course, and the README is explicit about the target: skills that guide AI coding agents to build "product-specific" evals, not foundation model benchmarks. The authors describe them as guards against the mistakes they saw "helping 50+ companies and teaching thousands of students".

The set is small and opinionated, nine skills arranged around a single claim: you should not write evals until you have looked at your data. `evals-start` is the entry point and routes by situation. With traces but no analysis it sends you to `error-discovery`, which builds an annotation app and helps you sample. With an existing eval pipeline it sends you to `eval-audit`, which inspects the setup and recommends next steps. The remaining six skills cover the specific jobs that follow: code checks, judge prompts, judge validation, synthetic inputs, RAG evaluation and custom review interfaces.

## Installation

The README installs with the skills CLI, from the repository URL rather than the shorthand:

```bash
npx skills add https://github.com/ai-evals-course/evals-skills
```

One skill only:

```bash
npx skills add https://github.com/ai-evals-course/evals-skills --skill error-discovery
```

Updates are handled by the same CLI:

```bash
npx skills check
npx skills update
```

The repository also ships a Claude Code plugin at `.claude-plugin/`, named `evals`, authored by Shreya Shankar and Hamel Husain, version 0.3.1. Because the skills are plain `SKILL.md` folders, copying `skills/*` into any agent's skills directory also works, and each folder's `references/` files must come with it.

## What It Provides

Eight listings clear the threshold, which is most of the set:

| Skill | Installs | Use For |
|---|---|---|
| validate-evaluator | 1,184 | Calibrating an LLM judge against human labels with data splits, TPR/TNR and bias correction |
| write-judge-prompt | 1,180 | Designing LLM-as-judge evaluators for subjective criteria such as tone, faithfulness, relevance and completeness |
| error-discovery | 1,159 | Running error analysis on a dataset: review UI, diverse sampling, annotation monitoring and failure-mode organisation |
| eval-audit | 1,156 | Auditing an eval pipeline and surfacing missing error analysis, unvalidated judges and vanity metrics, with severity |
| generate-synthetic-data | 1,092 | Creating diverse synthetic test inputs by dimension-based tuple generation, when real data is sparse |
| evaluate-rag | 1,074 | Evaluating retrieval and generation quality in a RAG pipeline, including faithfulness and relevance |
| build-review-interface | 1,070 | Building a browser annotation interface tailored to your data for reviewing traces and collecting labels |
| evals-start | 882 | The entry point: reads your situation and routes to the skill that matches it |

The remaining 3 indexed listings range from 2 to 459 installs.

The routing logic is worth knowing before you install, because two of the eight are dispatch rather than work. `evals-start` exists for the case where the user does not know where to begin, and its frontmatter says not to use it when a more specific skill already matches. `eval-audit` is the diagnostic for an inherited pipeline, and its description names the specific faults it looks for: missing error analysis, unvalidated judges, vanity metrics.

`error-discovery` carries most of the method. Its `SKILL.md` describes five phases: read the dataset and infer the content type, design a visual encoding from what varies in the data using Gestalt principles, build a single-file HTML review app served by a Python standard-library server with no dependencies, cluster the data and pick a diverse initial sample, then run an interactive loop that monitors annotations and proposes new samples to increase coverage.

## Why This Matters for Hermes Agents

The default failure mode of an agent asked to "add evals" is to write assertions against cases it imagined, then report a passing suite. These skills invert that order. Error analysis comes first, from real traces, and the output is a set of observed failure modes rather than a plausible checklist.

The second failure the set addresses is the unvalidated judge. An LLM judge that has never been compared to human labels is a metric with unknown error, and `validate-evaluator` exists to measure that error with splits, true and false positive rates, and bias correction. That is the difference between a number you can act on and a number that flatters the last prompt change.

Third, the skills encode judgement about which evaluator to use. `write-code-eval` is for objective failure modes checkable with regex, schema validation or execution tests, and `write-judge-prompt` is for the ones that need interpretation. Agents tend to reach for the judge because it is easier to write, which is exactly backwards on cost and reliability.

For a Hermes agent working on a RAG product, `evaluate-rag` covers the split that matters: retrieval quality separately from generation faithfulness. Without that split, a bad answer is unattributable.

## Usage

| You say | What happens |
|---|---|
| "I have a JSONL of traces and no idea what is failing" | `evals-start` routes to `error-discovery`, which builds a review app, samples diverse traces and organises annotations into failure modes |
| "Audit our eval suite, I inherited it" | `eval-audit` inspects the pipeline and returns findings with severity, starting with whether error analysis ever happened |
| "Write an eval for tone" | `write-judge-prompt` designs a judge for the subjective criterion, with a rubric and the reasoning steps it should follow |
| "Is our judge any good?" | `validate-evaluator` compares judge output to human labels and reports TPR, TNR and bias correction |
| "We have no data yet, generate test inputs" | `generate-synthetic-data` builds dimension-based tuples so the inputs vary on the axes that matter |
| "Evaluate the retrieval half of our RAG" | `evaluate-rag` measures retrieval quality, then generation faithfulness and relevance, as separate results |
| "Build me a review UI for these traces" | `build-review-interface` produces a browser annotation interface shaped to your record structure |

## Verification

Read the entry skill before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/ai-evals-course/evals-skills/main/skills/eval-audit/SKILL.md | head -20
```

It should open with `name: eval-audit` and the description about auditing an eval pipeline, missing error analysis, unvalidated judges and vanity metrics.

After install, confirm nine folders landed rather than the eight you see in the table, since the ninth (`write-code-eval`) sits below the reporting threshold but is still part of the set:

```bash
ls .agents/skills | wc -l
```

The count should be 9. Then ask the agent "where should I start with evals" and check that it names `evals-start` before anything else.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| validate-evaluator | Pass | Pass | Pass |
| error-discovery | Pass | Pass | Pass |
| evaluate-rag | Pass | Pass | Pass |
| write-code-eval | Pass | Pass | Pass |
| error-analysis | Pass | Pass | Pass |

The skills are markdown, but two of them build software while you watch. `error-discovery` and `build-review-interface` have the agent write a local review application and serve it, and `error-discovery` documents the endpoints it exposes: `GET /` for the app, `GET` and `POST /api/annotations` for labels, plus JSON files on disk (`samples.json`, `annotations.json`, `graph.json`, `patterns.json`, `suggestions.json`). Read the generated server before you leave it running, and keep it on localhost.

The data is the bigger consideration. Error analysis means putting real traces in front of the model and into a local app, and production traces routinely contain user text, identifiers or prompts under NDA. Decide what may enter that loop before you point the skill at a dataset.

The licence is Apache-2.0, which adds an explicit patent grant that MIT does not, and there is a LICENSE file in the repository root.

## Limitations

- Snapshot data, verified 2026-11-06: 9,483 combined installs across 11 indexed listings; 1,716 GitHub stars; Apache-2.0; last pushed 2026-09-24. Counts drift over time.
- Listings outnumber directories. The repository tree holds nine `SKILL.md` folders while skills.sh shows eleven entries, so `start` (225 installs) and `error-analysis` (2) have no matching directory. Treat them as aliases and confirm what you get before relying on them.
- The method assumes an interactive session. `error-discovery` says outright that it is meant for interactive sessions only, so it does not fit a headless cron job.
- Validation needs human labels you must supply. `validate-evaluator` calibrates against human judgement, and without a labelled sample there is nothing to calibrate.
- The skills are opinionated about order. Skip error analysis and go straight to judge prompts, and the resulting suite measures what the agent guessed rather than what breaks.
- Last push is the oldest of the four guides in this wave. Nothing is archived and the method is stable, but the tooling advice is a month behind the Rstack set.

## Related

- [MLflow Skills - Tracing, Evaluation and LLMOps](/hermes/skills/catalog/mlflow-skills-setup)
- [AI Research Skills - 100-Skill ML Research Library Setup](/hermes/skills/catalog/ai-research-skills-setup)
- [Context Engineering Kit - Prompt and MCP Setup](/hermes/skills/catalog/context-engineering-kit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `evals-start` even if you think you know the answer. It costs one turn and prevents the common case of writing a judge for a failure mode nobody has observed.
- Bring traces, not a spec. `error-discovery` reads JSONL, CSV or JSON of real outputs; a description of the product gives it nothing to cluster.
- Run `validate-evaluator` before trusting any judge score. A judge without a TPR and TNR against human labels is an opinion formatted as a number.
- Keep the review app local and disposable. It is a working tool for one analysis session, so do not check the generated server into the product repository.
- Re-audit after a model or prompt change. `eval-audit` is cheap, and a pipeline that passed last quarter can be measuring the wrong thing now.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
