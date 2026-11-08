---
title: "Eval Skills - AI Evaluation Workflows for Agents"
description: "hamelsmu/evals-skills on skills.sh: 6.0K combined installs across 7 listings; eval audits, error analysis, judge prompts and RAG evals for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hamelsmu-evals-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "ai evals", "llm judges", "error analysis"]
---

# Eval Skills - Setup Guide

**Source:** [hamelsmu/evals-skills](https://www.skills.sh/hamelsmu/evals-skills) via skills.sh - 6,048 combined installs across 7 indexed listings; first seen 2026-11-08 (Nov 8, 2026 morning sweep)
**GitHub:** 1,674 stars, MIT with a LICENSE file in the repo root, last pushed 2026-08-15, 7 SKILL.md directories under `skills/`, plus the Claude Code plugin manifest in `.claude-plugin/`
**Category:** AI evaluation for agents: error analysis, judge prompts, RAG evals, synthetic data and human review interfaces
**Quality Tier:** 🟢 Recommended - MIT licence, 1,674 stars, Pass on all three scanners for every sampled skill, and seven markdown-only skills with no executable install surface.

Seven skills arranged as a workflow rather than a menu. The README is written for the agent, not for you: it tells the agent to install the plugin and run the audit first, fan the audit's diagnostic areas out to parallel subagents, and then use whichever of the other six skills the audit recommends. That ordering is the substance of the set. `eval-audit` is the entry point, and it is written to refuse the common shortcut of recommending evaluators before anyone has read a trace.

The set comes out of the AI Evals course and encodes the mistakes the author reports seeing across 50+ companies: Likert-scale rubrics that no two annotators apply the same way, judges validated on the same examples they were prompted with, similarity scores used as the primary quality metric, and review interfaces that hand a domain expert a wall of raw JSON. Each skill is 96 to 215 lines of directives, about 1,110 lines total, with the reasoning deliberately stripped out. `meta-skill.md` states that rule plainly: write directives, not wisdom, because the agent already knows what JSON is and does not know your bias-correction formula.

One fact belongs at the top rather than in a footnote: the README marks this repository deprecated. The skills moved to `ai-evals-course/evals-skills`, a plugin called `evals` maintained by Shreya Shankar and Hamel Husain together. This guide measures the older single-author repository, and the catalog documents the successor separately.

## Installation

The README's primary path is the Claude Code plugin marketplace, in two commands run inside Claude Code:

```bash
# Step 1: Register the plugin repository
/plugin marketplace add hamelsmu/evals-skills

# Step 2: Install the plugin
/plugin install evals-skills@hamelsmu-evals-skills
```

Then restart Claude Code. The skills appear as `/evals-skills:<skill-name>`, for example `/evals-skills:error-analysis`. Upgrades go through the same namespace:

```bash
/plugin update evals-skills@hamelsmu-evals-skills
```

The README also documents the open Skills CLI, which is what a non-Claude harness uses:

```bash
npx skills add https://github.com/hamelsmu/evals-skills
npx skills add https://github.com/hamelsmu/evals-skills --skill eval-audit
npx skills check
npx skills update
```

Both forms come straight from the README and both still resolve. The deprecation notice in the same README points at the maintained fork, with its own install line:

```bash
npx skills add https://github.com/ai-evals-course/evals-skills
```

Take that redirect seriously if you are installing today rather than reading a snapshot: the copy here is the archived lineage, and the successor is the one that receives updates.

## What It Provides

The threshold for this guide is zero installs, so every indexed listing appears below and no rows are held back:

| Skill | Installs | Use For |
|---|---|---|
| eval-audit | 1,463 | Auditing an existing eval pipeline across six diagnostic areas and reporting findings by impact, each with a named fix |
| evaluate-rag | 849 | Separating retrieval failures from generation failures in a RAG pipeline, with Recall@k for retrieval and faithfulness and relevance for generation |
| write-judge-prompt | 833 | Building a binary Pass/Fail judge for one failure mode, with explicit definitions and few-shot examples drawn from labeled data |
| error-analysis | 798 | Reading roughly 100 traces, recording what went wrong, and growing failure categories from the notes instead of from a template |
| validate-evaluator | 737 | Calibrating a judge against human labels on train, dev and test splits, measured with TPR and TNR and corrected for bias |
| generate-synthetic-data | 722 | Building test inputs by dimension-based tuple generation when real traces are too sparse to sample |
| build-review-interface | 646 | Building a browser annotation page tailored to the domain, with Pass/Fail buttons, notes and keyboard shortcuts |

All 7 rows clear the threshold, and since the threshold is zero there is no tail. No rows fall below the threshold.

The install counts are the adoption signal, and they are close together: the spread between the top skill and the bottom is 817 installs. Everything here is fairly widely used, and `eval-audit` is the most used because the README tells people to start there.

What the skills actually contain is worth describing, because the useful parts are specific. `eval-audit` checks six areas and flags named anti-patterns in each: error analysis skipped in favour of evaluators, evaluators on Likert scales, judges that score holistically ("is this response helpful"), LLM judges used where regex or schema validation would do, ROUGE or BERTScore or cosine similarity as the primary generation metric, judges in production with no validation set, alignment measured as raw accuracy under class imbalance, few-shot examples drawn from the test split, outsourced annotators without domain expertise, reviewers shown only the final output, and error analysis that has not been re-run since the last model switch. Each finding carries a one or two sentence explanation and a fix that names a sibling skill. If there are no artifacts at all, the audit has a separate branch: do error analysis first, generate synthetic inputs only if there is no production data, and do not recommend dashboards.

`validate-evaluator` is the most quantitative of the set. It splits human-labeled data into train at 10 to 20 percent, dev at 40 to 45 percent and test at 40 to 45 percent, iterates on dev until TPR and TNR both clear 90 percent, accepts 80 percent as the floor, runs the test set exactly once, and then applies the Rogan-Gladen correction to production scores: theta = (p observed + TNR - 1) / (TPR + TNR - 1), clipped to the unit interval, with an explicit warning that it is invalid when TPR plus TNR minus one approaches zero. That formula is the reason to install the set rather than improvise. It is the difference between "the judge says 80 percent pass" and "the true pass rate is about 85 percent", and almost nobody derives it from memory.

## Why This Matters for Hermes Agents

Hermes agents write evaluators constantly and validate them almost never. Ask for a quality check on an extraction pipeline and you get a rubric out of ten with adjectives in it, scored by the same model that produced the output, on the same examples that were pasted into the prompt as guidance. The number that comes back is unfalsifiable, and it moves when the prompt is reworded even though the pipeline did not change. `eval-audit` exists to catch exactly that shape of pipeline, and its checks are written as greps over artifacts rather than as opinions.

The second fit is structural. These skills assume a harness that can spawn parallel subagents, which is the README's own instruction: investigate each diagnostic area in a separate subagent, then synthesise. That maps directly onto Hermes. Six read-only investigations can run concurrently because none of them writes anything, and the synthesis step has a report format already specified: problem title, status, one or two sentences, fix.

The third is the trace dependency. Every skill in the set either consumes traces or produces something that becomes one. Hermes already accumulates session transcripts, tool calls and connector responses, so the raw material is there in a way it often is not for a greenfield project. Pointing `error-analysis` at a folder of exported transcripts is a shorter path than standing up an observability stack first.

The set is also honest about its own ceiling. The README says these skills only encode mistakes that generalise across projects, and that skills grounded in your stack and data will outperform them. For an agent working on a specific pipeline, the right move is to run the audit, then write a local skill that carries the actual failure categories of that pipeline.

## Usage

| You say | What happens |
|---|---|
| "/evals-skills:eval-audit on my eval pipeline" | Walks the six diagnostic areas, inspects whatever artifacts exist, and returns findings ordered by impact with a fix per finding |
| "Run the audit with a subagent per area" | Fans the diagnostic areas out in parallel and synthesises one report, which is the README's recommended shape |
| "My judge scores 92 percent accuracy, is it good" | Flags raw accuracy under class imbalance and sends you to TPR and TNR on a held-out split |
| "We need evals for the support bot by Friday" | Refuses to design evaluators before error analysis and starts from a trace sample instead |
| "Write a judge for tone" | Produces one binary judge for one failure mode, with Pass/Fail definitions and few-shot examples, not a five-point scale |
| "We have no production traces yet" | Routes to dimension-based synthetic generation, 3 dimensions and 20 hand-checked tuples, then a separate conversion prompt per tuple |
| "Our RAG answer is wrong" | Splits retrieval from generation: Recall@k first, then faithfulness and relevance, and chunking grid search before generation tuning |

Invocation is a slash command in Claude Code and a plain request elsewhere. The skills also trigger on intent, because each description carries its own scoping clause, including the negative case: `eval-audit` explicitly says not to use it for building a new evaluator from scratch, which is what keeps it from swallowing the work of its siblings.

## Verification

Read the entry skill before installing anything. This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/hamelsmu/evals-skills/main/skills/eval-audit/SKILL.md | head -40
```

It should open with YAML frontmatter naming `eval-audit`, a folded description that includes the line "Audit an LLM eval pipeline and surface problems: missing error analysis, unvalidated judges, vanity metrics", and the explicit do-not-use clause routing to `error-analysis`, `write-judge-prompt` or `validate-evaluator`. Immediately under the frontmatter you should see the three step overview and then `## Prerequisites`, which states that access to traces and evaluator configs is required and that a run with no artifacts should skip to the "No Eval Infrastructure" section.

The README itself is worth a second curl, because it carries the deprecation notice and the marketplace name that the install command depends on:

```bash
curl -fsSL https://raw.githubusercontent.com/hamelsmu/evals-skills/main/README.md | head -20
```

That should print the `[!IMPORTANT]` block about the move to `ai-evals-course/evals-skills` before any other content. If your copy of the README does not show that block, you are reading a different repository than the one this guide measured.

After install, confirm the skills landed. The `npx` route writes one directory per skill into the agent's skills path, which for Claude Code is `~/.claude/skills`:

```bash
ls ~/.claude/skills | grep -i evals
```

You should see seven directories, one per skill, each holding a `SKILL.md`. The Claude Code plugin route does not use that path, so check it by typing `/evals-skills:` in the slash menu instead and confirming that the seven names complete. A cheap end-to-end check either way is to run the audit on a pipeline you already know is weak: if the report comes back with generic advice that could have been written without reading your artifacts, the skill loaded but the artifacts did not, and the anti-pattern list at the bottom of `eval-audit` names that failure directly.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| eval-audit | Pass | Pass | Pass |
| evaluate-rag | Pass | Pass | Pass |
| error-analysis | Pass | Pass | Pass |
| generate-synthetic-data | Pass | Pass | Pass |
| build-review-interface | Pass | Pass | Pass |

Five of the seven listings carry verdicts; `write-judge-prompt` and `validate-evaluator` were not in the sampled set, so their status is unmeasured rather than clean. Treat that as an absence of evidence.

What is being scanned matters here. Six of the skills are prose. The seventh, `build-review-interface`, instructs the agent to write an HTML page plus a local save endpoint, which means an agent acting on it produces executable code inside your working tree, with a Playwright test script beside it. The skill does not ship that code, so the scanners have nothing to inspect beyond the instructions. Review what the agent generates before it runs against real customer traces.

The data risk is larger than the code risk. Traces contain user inputs, retrieved documents and model outputs, often with personal data, and the whole method depends on exporting them to local files and, in the synthetic-data path, handing them to a model to generate more inputs. `error-analysis` asks for around 100 traces, and `write-judge-prompt` puts real labelled examples into a prompt. That is a data-handling decision, not a packaging one, and it should be made before install rather than during the first run.

The licence is MIT with a LICENSE file in the repo root, so reuse and modification are permitted with attribution.

## Limitations

- Snapshot data, verified 2026-11-08: 6,048 combined installs across 7 indexed listings, 1,674 GitHub stars, MIT, last pushed 2026-08-15. Counts drift, and the repository is archived lineage rather than active development.
- The upstream repository is deprecated by its own README. The maintained successor is `ai-evals-course/evals-skills`, owned by the course and co-maintained by Shreya Shankar and Hamel Husain. That is a different source, tracked in this catalog as a separate page, and installing from this repository pins you to the older copy.
- 7 indexed listings and 7 SKILL.md directories match exactly, so there is no drift between what skills.sh indexes and what the tree contains.
- Plugin version in `.claude-plugin/plugin.json` is 0.2.0. There is no changelog in the tree and no release tags to pin against, so an install today and an install next month may differ without notice.
- The audit needs eval artifacts to be useful: traces, evaluator configs, judge prompts or labelled data, either through an observability MCP server (Phoenix, Braintrust, LangSmith, Truesight or similar) or as local exports. Without them it degrades to a checklist, which its own anti-patterns call a failure.
- `validate-evaluator` wants roughly 50 Pass and 50 Fail human-labelled traces from a domain expert. That annotation budget is the real cost of the set, and no skill in it removes that work.
- The evidence is the maintainer's. The 50+ company claim, the course material and the method itself are the author's own reporting, not an independent benchmark.
- Two of the seven listings have no scanner verdicts, so their safety status could not be confirmed.

## Related

- [AI Evals Skills - Product-Specific Evaluations](/hermes/skills/catalog/ai-evals-skills-setup)
- [Arize Skills - LLM Observability and Evaluation Setup](/hermes/skills/catalog/arize-skills-setup)
- [Arize Phoenix Skills - LLM Observability for Agents](/hermes/skills/catalog/arize-phoenix-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `eval-audit` before installing the rest, and let it pick the next skill. Installing all seven and improvising an order defeats the one sequencing decision the set makes for you.
- Give the audit a path to artifacts, not a description of them. It is written to inspect files and MCP endpoints, and a prompt-only run is the checklist anti-pattern it names.
- Ask for the TPR and TNR numbers explicitly. A judge report without both is the finding, not the result, and the target is 90 percent on each rather than a single accuracy figure.
- Reuse the Rogan-Gladen correction outside this skill. Any time you quote a pass rate from a fallible judge, theta = (p observed + TNR - 1) / (TPR + TNR - 1) gives the number you should actually report.
- Keep the review interface out of the first sprint. `build-review-interface` says to add failure-mode tag buttons only after categories exist, and building the tagging UI first biases the labels toward the tags you guessed.
- Check the README's deprecation notice before pinning this into a pipeline. If the successor repo is the one being maintained, install that and keep this page as the method reference.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
