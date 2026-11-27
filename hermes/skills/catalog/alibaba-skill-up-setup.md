---
title: "Alibaba Skill-Up - Skill Evaluation and Evolution"
description: "alibaba/skill-up: 1.4K combined installs. Evaluate and evolve agent skills with the skill-up CLI and skill-upper workflow."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/alibaba-skill-up-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "skill evaluation", "evals", "go cli"]
---

# Alibaba Skill-Up - Setup Guide

**Source:** [alibaba/skill-up](https://www.skills.sh/alibaba/skill-up) via skills.sh - 1.4K combined installs across 3 indexed listings; first documented 2026-11-27 (morning sweep)

**GitHub:** [alibaba/skill-up](https://github.com/alibaba/skill-up) - 1,526 stars, Apache-2.0, branch main, last pushed 2026-11-27; the skill-upper skill is the canonical source under skills/skill-upper/, the code-stats example under examples/code-stats/, and plugin bundles under plugins/codex-skill-up/ and plugins/dsh-skill-up/

**Category:** Skill evaluation and evolution: declarative evals with the skill-up CLI and the skill-upper conversation workflow

**Quality Tier:** 🟠 Orange - the skill-upper listing carries a Gen Agent Trust Hub Fail and a Snyk Fail, although the other two listings pass all three auditors

skill-up is a Go CLI published by Alibaba for evaluating Agent Skills, agents and their workspaces. It runs declarative cases against an agent engine, grades the response and the workspace changes, and produces reports locally or in CI. The repository's own skill, skill-upper, closes the loop: it lets an agent capture and review skill observations, create and run evals, diagnose failures, repair or expand the case suite, and rerun skill-up through conversation.

The index lists three skills. skill-upper is the workflow skill with nearly all the installs; todo-manager and code-stats are a fixture and an example shipped inside the repository rather than standalone distributable skills. skill-up supports Qoder CLI, Claude Code and Codex as built-in engines, custom engines via local commands or HTTP services, multi-turn conversations with user simulation, and Anthropic evals.json import.

## Installation

The README installs skill-upper through skills.sh for Codex or Claude Code:

```bash
# Codex, global install
npx skills add https://github.com/alibaba/skill-up/tree/main/skills/skill-upper -g -a codex -y

# Claude Code, global install
npx skills add https://github.com/alibaba/skill-up/tree/main/skills/skill-upper -g -a claude-code -y
```

You normally do not need to install skill-up first; skill-upper checks for the CLI when it runs and guides the agent through installation if needed. To install the CLI directly and hand-write eval files instead:

```bash
curl -fsSL https://raw.githubusercontent.com/alibaba/skill-up/main/install.sh | bash
```

Once the skill is loaded, point it at a project that contains a SKILL.md and ask it to evaluate, for example with the README's prompt: "Use skill-upper to evaluate this Skill. Read SKILL.md, identify its most important behaviors, create realistic eval cases with appropriate judges, validate the configuration, and run skill-up."

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| skill-upper | 1,372 | Capture and review skill observations; create, run, diagnose and iteratively improve skill evals with the skill-up CLI. |
| todo-manager | 1 | A Chinese-language todo fixture skill inside skill-upper's eval fixtures, used to exercise the eval harness rather than a standalone skill. |
| code-stats | 1 | Analyze code files and report line counts, file counts by extension and total size. |

All 3 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Skill evaluation turns "the skill works" into a repeatable, observable claim. skill-up gives declarative cases, three judge types (rule-based, script and agent-judge), and structured reports, so a skill's behaviour is checked the same way every time. skill-upper is the piece that matters for an agent that maintains its own skills: it closes the improvement loop through conversation, interpreting a failed report, repairing or adding cases, and rerunning skill-up. The with/without comparison is the measurement that isolates a skill's effect, running the same cases with and without the skill. Multi-engine support means one skill can be tested across Claude Code, Codex and Qoder CLI rather than tied to a single client. It imports Anthropic evals.json, which eases migration from an existing eval setup. For builders, the eval suite is declarative YAML you can commit next to the skill, so regressions run in CI through the bundled GitHub Action.

## Usage

| You say | What happens |
|---|---|
| "Use skill-upper to evaluate this Skill." | Reads SKILL.md, creates eval cases with appropriate judges, validates config, runs skill-up, and summarizes the highest-impact failures. |
| "Use skill-upper to improve this Skill from the latest results." | Compares the original and candidate, adds regression coverage, and applies only evidence-supported changes. |
| "Run this eval without the skill" | Sets skills: [] and runs agent-only cases to baseline the engine on its own. |
| "Import my Anthropic evals.json" | skill-up import converts evals.json to the YAML layout. |
| "Validate my eval config" | skill-up validate checks eval.yaml and case files. |
| "Run evals in CI on every pull request" | The alibaba/skill-up GitHub Action runs the same skill across engines. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/alibaba/skill-up/main/skills/skill-upper/SKILL.md
```

After installing the CLI, confirm it is on the path:

```bash
skill-up --version
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| skill-upper | Fail | Pass | Fail |
| todo-manager | Pass | Pass | Pass |
| code-stats | Pass | Pass | Pass |

skill-upper fails the Gen Agent Trust Hub and Snyk while the two fixture skills pass all three. The repository is a large Go codebase (664 files in the tree) plus a CLI installed by a shell script, so the audit surface is real executable code rather than Markdown-only skills. The CLI drives agent engines and can change workspace contents, so run evaluations against an isolated workspace when the skill under test is not one you trust.

## Limitations

- Snapshot data, verified 2026-11-27: 1,374 combined installs across 3 indexed listings; 1,526 GitHub stars; Apache-2.0; last pushed 2026-11-27. Counts drift over time.
- todo-manager and code-stats are a fixture and an example inside the repository, not standalone skills; both sit at 1 install each and nearly all indexed usage is skill-upper.
- skill-upper fails both the Gen Agent Trust Hub and Snyk audits. The failure reasons are not published beside the verdicts, so check the security pages on skills.sh before production use.
- The skill-up CLI is a compiled Go tool downloaded by the install script, so the security review covers a real codebase, not just skill Markdown.
- The skill-upper evaluation workflow drives agent engines and can mutate the workspace; run it against an isolated workspace when evaluating untrusted skills.

## Related

- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup)
- [Skill Vetting Setup](/hermes/skills/catalog/skill-vetting-setup)
- [ClawHub Skill Vetting - Security Scanner Setup](/hermes/skills/catalog/clawhub-skill-vetting-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install skill-upper only; it checks for the skill-up CLI when it runs and guides installation if the binary is missing.
- Commit the eval suite (eval.yaml plus cases/*.yaml) next to the skill so regressions run in CI on every pull request.
- Prove a skill's value with the with/without comparison instead of asserting it.
- Start from skill-upper's conversation flow, then hand-write eval.yaml only when you need fine control over judges and fixtures.
- Review the observation capture before enabling the Codex or DSH plugin; observations are approval-gated regression cases.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
