---
title: "Darwin Skill - Autonomous Skill Optimization Setup"
description: "Huashu's darwin-skill: 11.1K installs on a single skill that grades and rewrites SKILL.md files with a 9-dimension rubric and a git ratchet."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/darwin-skill-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "optimization", "self-improvement"]
---

# Darwin Skill - Setup Guide

darwin.skill is one skill that treats other skills as something to be measured and improved, the way a training loop treats a model. The author, Huashu (alchaincyf), built it on Andrej Karpathy's autoresearch: read a SKILL.md, score it against a fixed rubric, make one targeted edit, re-score with independent judges, and keep the edit only if it wins. Failed edits are reverted with `git revert`, so the baseline can only move forward.

Version 2.0 rebuilt the scoring around two Microsoft Research papers, SkillLens (arXiv 2605.23899) for the rubric design and SkillOpt (arXiv 2605.23904) for validation-gated edits, and the SKILL.md now carries a 2.1 revision that replaces absolute-score comparison with a paired same-judge vote. It is a single Markdown file with supporting templates, references and a screenshot script, and it is the only listing in this repository.

**Source:** [alchaincyf/darwin-skill](https://www.skills.sh/alchaincyf/darwin-skill) via skills.sh - 11.1K combined installs across 1 indexed listing; first seen Apr 13, 2026
**GitHub:** [alchaincyf/darwin-skill](https://github.com/alchaincyf/darwin-skill) (6.6K stars; MIT License; branch master, pushed 2026-09-18; layout is a single `SKILL.md` at the repo root with no `skills/` directory, plus `references/`, `templates/`, `scripts/screenshot.mjs` and `test-prompts.json`)
**Category:** Agent Meta / Skill Quality Tooling
**Quality Tier:** 🟡 Beta - 6.6K stars, MIT licensed and 11.1K installs on a mature single skill, but two of three scanners return Warn because the skill edits files and drives git, the operational instructions are Chinese-first, and the rubric's own evidence puts LLM judge accuracy well below human review

## Installation

```bash
# Install the skill with the skills CLI
npx skills add alchaincyf/darwin-skill
```

```bash
# Manual path from the README: download the zip, then place SKILL.md here
mkdir -p ~/.claude/skills/darwin-skill
# unzip darwin-skill.zip and copy SKILL.md into that directory
```

There is no API key and no service to register. The hard prerequisite is a git repository to run the loop inside, because keep and revert decisions are git commits; the SKILL.md defines a fallback to timestamped `.bak` file copies when `git rev-parse` fails. Node is only needed for the optional result-card screenshot step (`node scripts/screenshot.mjs`), which also has an `npx playwright screenshot` fallback.

The README's own safety notes are part of the setup, not an afterthought: commit or stash local skill edits first, and review the checkpoint diff before each next round.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| darwin-skill | 11,143 | Grade a SKILL.md against a 9-dimension, 100-point rubric and run hill-climbing rounds that keep only judge-approved edits, with test prompts, git revert and human checkpoints |

No indexed listings fall below the threshold. This is a single-skill repository: the one listing resolves to `SKILL.md` at the repo root rather than a `skills/<name>/SKILL.md` directory.

The rubric it applies is worth stating, since it is what the skill actually sells. Six structure dimensions carry 59 points (frontmatter quality 7, workflow clarity 12, failure mechanism encoding 12, checkpoint design 6, actionable specificity 18, resource integration 4), two effectiveness dimensions carry 35 (architecture 12, live test performance 23), and a ninth meta dimension carries 6 for counter-examples and a high-risk action blacklist.

## Why This Matters for Hermes Agents

A skill library is the one part of an agent's behaviour that is edited by hand and almost never measured. Most skill review stops at structure: frontmatter present, steps numbered, paths that exist. darwin.skill adds the part that is missing, which is whether the skill still produces better output than the model would without it, by running test prompts with the skill and without it and comparing the two.

The mechanism that matters most for a Hermes agent is the refusal to let one model grade its own edit. The skill spawns independent judges on the edited and previous versions, takes an odd-number majority vote, and reverts through `git revert` instead of `git reset --hard`, which keeps the history auditable. That is the same shape as an approval gate: a change is either justified by evidence or removed.

It also fits the file-based model these agents already use. Skill directories are plain Markdown, so an optimization pass is a git branch plus a diff plus a score, which a human can review in a minute. Nothing is hidden in a database or a hosted service.

The honest limit is that the rubric is still an LLM judgement. The skill's own references report LLM-as-judge accuracy at 46.4 percent for raw scoring and 73.8 percent once the meta-skill dimensions are added, and the 2.1 revision exists precisely because absolute scores move by several points when only the judge changes. Treat the score as a triage ranking and the diff as the thing you actually approve.

## Usage

| You say | What happens |
|---|---|
| "Optimize all skills" | Runs the full cycle: branch `auto-optimize/YYYYMMDD-HHMM`, test prompts, baseline scoring, then the weakest skills first across up to 3 rounds each |
| "Optimize the emil-design-eng skill" | Limits scope to one skill and runs phases 0.5 to 2 only, skipping the suite-wide report |
| "Score my skills, do not change anything" | Stops after the baseline pass and returns the scoring card with the weakest dimension per skill |
| "Show the optimization history" | Reads `results.tsv` and reports past rounds, keep or revert status, dimension targeted and evaluation mode |
| "Why did this skill score 72?" | Breaks the score down by the 9 weighted dimensions and names the largest weighted gap |
| "Wait, I do not like that rewrite" | Reverts to the pre-optimization version of that skill at the checkpoint, before any further rounds run |
| "Give me a result card" | Fills `templates/result-card.html` in one of three themes and screenshots it to a PNG |

## Verification

List what the CLI installed and confirm the skill directory is present:

```bash
npx skills list | grep -i darwin
ls ~/.claude/skills/darwin-skill/
```

Read the skill before installing it. These URLs returned 200 with `curl -s -o /dev/null -w "%{http_code}"` on Oct 26, 2026 (the repo uses `master`, not `main`):

```bash
curl -sL https://raw.githubusercontent.com/alchaincyf/darwin-skill/master/SKILL.md
curl -sL https://raw.githubusercontent.com/alchaincyf/darwin-skill/master/README_EN.md
curl -sL https://raw.githubusercontent.com/alchaincyf/darwin-skill/master/test-prompts.json
curl -sL https://raw.githubusercontent.com/alchaincyf/darwin-skill/master/references/skilllens-evidence.md
```

The two artefacts the loop writes are easy to check after the first run: the branch `auto-optimize/<timestamp>` should exist, and `results.tsv` should have one row per round with an `eval_mode` column of `paired`, `full_test` or `dry_run`.

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| darwin-skill | Warn | Warn | Pass |

The two Warn verdicts are consistent with what the file asks an agent to do. This is one of the few skills whose job is to write to disk: it reads every `SKILL.md` in scope, edits them, creates a git branch, commits, and runs `git revert` when a round loses. It also invokes `node scripts/screenshot.mjs`, and its version self-check may run `git ls-remote origin HEAD` to compare local and remote commits, which is an outbound network call to the configured git remote.

There is no `allowed-tools` field, no bundled package, no API key and no telemetry. The mitigations are the ones the README states: run it inside a git repository you can throw away, commit or stash before the first round, and read each checkpoint diff before approving the next skill. The skill also enforces its own guardrails in text: no `git reset --hard`, no multiple dimensions per round, no optimizing beyond 150 percent of the original file size, and no silently swallowed exceptions.

Two behavioral details are worth knowing before you run it on a real library. It defaults to scanning `.claude/skills/*/SKILL.md`, so a Hermes profile's own `skills/` tree needs an explicit scope argument. And the version self-check writes a `.last-update-check` file into the skill directory on each run.

## Limitations

- One skill, not a suite. It optimizes existing SKILL.md files and cannot author a new skill, install one, or test behaviour in production traffic.
- Chinese-first documentation. `SKILL.md` and `README.md` are written in Chinese with English trigger words; `README_EN.md` is an overview, not a translation of the operational phases, so review the actual instructions before delegating a run.
- LLM-judged scores. The repo's own evidence section reports judge disagreement large enough that the author demoted absolute scores to triage only, so the score is directional and the human checkpoint is the real gate.
- Writes to the skill library. It edits files, commits and reverts inside a git repository, which is exactly why two scanners return Warn.
- Version skew in the docs. `SKILL.md` carries a 2.1 revision dated 2026-06-10 while both READMEs still describe 2.0, so the newest behaviour is documented only in the file the agent reads.
- Snapshot data, verified Oct 26, 2026: 11,143 combined installs across 1 indexed listing; 6.6K GitHub stars; MIT License; last pushed 2026-09-18. Counts drift over time.

## Related

- [Task Observer - Meta-Skill for Continuous Skill Improvement Setup](/hermes/skills/catalog/task-observer-setup) - a lighter meta-skill that watches a session for skill gaps instead of scoring files after the fact.
- [Hermes Dojo - Self-Improvement System Setup Guide](/hermes/skills/catalog/hermes-dojo-setup) - a broader self-improvement harness that pairs with a measured per-skill optimization loop.
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup) - run before granting an optimizer write access to a skill library, and again after it rewrites one.
- [Claude Skills Generator - Coding Setup](/hermes/skills/catalog/claude-skills-generator-setup) - the authoring side that darwin.skill assumes already exists.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with one skill, not the whole library. Scope the first run to the skill whose output you complain about most, and read the diff at the checkpoint before approving round two.
- Approve on the diff, not the score. The paired vote tells you a rewrite won; only the diff tells you why, and that is where a stray paragraph or a softened instruction shows up.
- Give it real test prompts. The live test dimension carries 23 of the 100 points, and a run with mostly `dry_run` rows is close to scoring an edit from imagination.
- Keep the run inside a scratch branch of the skill repo. The revert path is `git revert`, so an unrelated dirty tree turns a clean rollback into a conflict.
- Pair it with a security review of the skills it touches. An optimizer that rewrites instructions can just as easily widen a tool grant as tighten one.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
