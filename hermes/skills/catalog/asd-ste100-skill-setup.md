---
title: "ASD-STE100 Skill - Simplified Technical English"
description: "danyuchn/asd-ste100-skill on skills.sh: 9.4K combined installs; rewrites dense agent-facing English into ASD-STE100 Simplified Technical English."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/asd-ste100-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "simplified technical english", "controlled language", "prompt clarity"]
---

# ASD-STE100 Skill - Setup Guide

**Source:** [danyuchn/asd-ste100-skill](https://www.skills.sh/danyuchn/asd-ste100-skill) via skills.sh - 9.4K combined installs across 2 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 6,166 stars, MIT, last pushed 2026-11-07, a single SKILL.md at the repository root with references/, examples/ and scripts/ beside it
**Category:** Controlled English for agents: rewrites dense output into ASD-STE100 Simplified Technical English so steps cannot be misread
**Quality Tier:** 🟡 Review - MIT licence, 6,166 stars and clean Trust Hub and Socket verdicts, held to Review by a Snyk warning on the sampled skill and a second listing with no published verdicts.

ASD-STE100 is the controlled-language standard the aerospace and defense industry built so that aircraft maintenance instructions cannot be misread. The skill in this repository repurposes that discipline for a different reader: an AI agent parsing another agent's output, a tool description, an error message or an inter-agent instruction, with no human in the loop to ask "did you mean X or Y".

The clone is small and readable. `SKILL.md` is 139 lines and carries the stance, two rewrite modes, the structural and lexical rule tables, a six-item scan checklist, a six-step process and an output contract. Beside it sit `references/writing-rules.md`, two worked-example files under `examples/`, a stdlib-only linter at `scripts/ste-lint.py`, and a `.claude-plugin/` manifest pair.

The scoping is the interesting part. The skill encodes the rule categories of ASD-STE100 Issue 9 (January 2025): 53 writing rules across 9 sections, backed by a dictionary of roughly 900 approved words and roughly 1,200 words to avoid. It does not reproduce that dictionary, because ASD permits free reproduction only for eight listed categories of organisation and this project is in none of them. So the structural rules are applied as written, and the lexical rules are demoted to a direction of travel, stated as such in the output.

## Installation

The README's primary route is the skills CLI, run from the project root:

```bash
npx skills add danyuchn/asd-ste100-skill
```

The CLI sends anonymous install telemetry (skill name and timestamp, no personal or device information) to rank skills on the skills.sh leaderboard. `DISABLE_TELEMETRY=1` opts out. Update later with:

```bash
npx skills update
```

For a live checkout that tracks the repository with `git pull`, the README gives the clone route:

```bash
git clone https://github.com/danyuchn/asd-ste100-skill ~/.claude/skills/asd-ste100
```

That path makes the skill available in every Claude Code project rather than one. The repository also ships `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` declaring a single plugin named `asd-ste100`, so the marketplace route is available if your harness reads those manifests.

The linter has no install step and no dependencies, because it is standard-library Python only:

```bash
python3 scripts/ste-lint.py --selftest
```

## What It Provides

Two indexed listings carry the same skill, and only one clears the threshold:

| Skill | Installs | Use For |
|---|---|---|
| asd-ste100 | 9,157 | Rewriting tool descriptions, error messages, system prompts and inter-agent instructions into short, active, single-meaning English |
| Simplified Technical English (ASD-STE100) | 200 | The same rewrite job under the standard's full name; treat it as a duplicate label rather than a second implementation |

The remaining indexed listing sits at 200 installs, below the 500-install threshold.

What the top listing ships is a mode split worth knowing before you use it. Strict mode covers procedures, error messages, tool and function descriptions, inter-agent instructions and safety text, and enforces every rule including the length caps and one-word-one-meaning discipline. STE-flavored mode covers READMEs, PR descriptions, changelogs and explanatory prose: it keeps the sentence discipline, active voice, simple tenses, no phrasal verbs, no semicolons, no nominalization and no marketing adjectives, and drops the fixed-vocabulary lockdown because a strict rewrite of prose reads as a personality transplant rather than a clarification.

The linter is the part that makes the skill verifiable rather than advisory. It checks semicolons, a short list of soft phrasal verbs (spin up, reach out, dive into, kick off, circle back, touch base), nominalizations, marketing adjectives, passive voice, present-perfect forms including irregular participles, long sentences, synonym rotation and dangling conjunctions in supported list items. It does not check noun-cluster length, does not know phrasal verbs outside its list, and by design never flags hedges or modality. `--json` gives structured output, `--baseline N` tolerates N hard violations when adopting it on an existing document, and `--disable rule1,rule2` silences named rules.

## Why This Matters for Hermes Agents

Most ambiguity in an agent pipeline is authored, not inherited. A tool description written as "this may attempt to synchronize state and, if a conflict is detected, may resolve it depending on the strategy" gives a downstream model three readings and no way to ask which one was meant. The skill's rewrite of that sentence splits it into four sentences with one instruction each, which is the form a parser can act on.

The hedge rule is the one that protects you from silent damage. A rewrite that turns "the request may have failed" into "the request failed" is shorter, cleaner and a different claim, and a length-capped simplifier will do exactly that if nothing stops it. This skill names that failure in its own process notes, keeps the hedge, and prints a `Kept as-is:` line when it deliberately leaves a phrase unsimplified, so the trade-off is visible instead of hidden.

For Hermes specifically, the skill pairs with any pipeline where one agent writes the instruction and another executes it: subagent task briefs, MCP tool schemas, runbook steps, cron job prompts. Those strings are read exactly once, by a machine, with no back-channel. That is the same constraint the standard was built for, which is why the rules transfer at all.

The honest limit is stated in the README: this fixes the form of a text, not its substance. A paragraph with nothing to say comes out short, clean and still empty. It is also not a checker for an existing rewrite: the linter never compares an original against a simplified version, so nothing here proves that meaning survived. That check stays with you.

## Usage

| You say | What happens |
|---|---|
| "Disambiguate this tool description" | The skill picks Strict mode and returns the rewritten description with no preamble or change summary |
| "Rewrite this error message so an agent can't misparse it" | One instruction per sentence, active voice, no phrasal verbs, hedges preserved |
| "Apply ASD-STE100 to this instruction" | Strict mode with the length caps and one-word-one-meaning discipline enforced |
| "Show the diff" | Switches output to a before/after table naming the rule each row broke, plus a violation count |
| "Which rules did it break" | The same rule table, with a one-line note on anything deliberately left unsimplified |
| "Lint this README" | Runs `scripts/ste-lint.py` for a mechanical pass over the structural rules before any rewrite |
| "Reduce ambiguity in this output" | Infers the mode from the text type and rewrites, flagging lexical departures rather than claiming dictionary compliance |

## Verification

Read the skill before installing it. This path returned 200 on the repository's `master` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/danyuchn/asd-ste100-skill/master/SKILL.md | head -40
```

It should open with frontmatter naming `asd-ste100`, version 0.4.0, and a description that scopes the skill to text parsed without a human to resolve ambiguity and explicitly excludes creative and marketing copy.

After install, confirm the linter came with it and that it passes its own assertions. The default clone destination puts the skill at `~/.claude/skills/asd-ste100`:

```bash
ls ~/.claude/skills/asd-ste100/scripts
curl -fsSL https://raw.githubusercontent.com/danyuchn/asd-ste100-skill/master/scripts/ste-lint.py -o /tmp/ste-lint.py && python3 /tmp/ste-lint.py --selftest
```

The directory should hold `ste-lint.py` and nothing else, and `--selftest` should exit 0. The self-test asserts, among other things, that "may have failed" passes clean, which is the assertion that proves the linter is not quietly grading hedges.

One documented oddity is worth reproducing so it does not surprise you: the repository's own prose does not lint clean, because the rule tables quote the patterns they forbid and some sentences run long. The README's own command for it is:

```bash
python scripts/ste-lint.py --baseline 36 SKILL.md
```

A number far above or below 36 on a fresh clone means you are looking at a different revision.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| asd-ste100 | Pass | Pass | Warn |
| Simplified Technical English (ASD-STE100) | ? | ? | ? |

The install surface is markdown, a reference file, two example files and one Python script. There is no package manifest, no post-install hook and no network call in the rewrite path; the linter reads the file arguments you give it and prints findings. The `.claude-plugin` manifests are declarative JSON with no commands in them.

The single Snyk warning on the sampled skill is the reason this guide does not call the install clean. Check the skills.sh security page for the specific rule before you wire it into a pipeline that processes untrusted text, and remember that the input to this skill is often exactly that: error strings, logs and agent messages produced by something else.

The compliance caveat matters more than the scanner one. This is a clarity tool inspired by ASD-STE100, not a certified STE authoring tool, and the repository says so in its own boundaries section. Do not describe output as STE-compliant, and do not use it as the last check on real aircraft or defence documentation, where the official dictionary is the only valid reference.

## Limitations

- Snapshot data, verified 2026-11-06: 9,357 combined installs across 2 indexed listings; 6,166 GitHub stars; MIT; last pushed 2026-11-07. Counts drift over time.
- The dictionary is absent by design. The roughly 900 approved words and 1,200 words to avoid are not in the repository, so lexical rules are guidance rather than a checkable standard.
- The linter checks structural patterns only. It does not compare an original with a rewrite, verify that requirement strength stayed the same, or prove that meaning survived.
- Its own coverage is narrow by design: no noun-cluster length (that needs part-of-speech tagging), no phrasal verbs outside its short list, so "take off the panel" passes, and no hedge or modality findings at all.
- Wrong tool for persuasive text. STE is deliberately flat and literal, and applying it to marketing copy or creative writing removes the thing that made the text work.
- The second indexed listing has no published scanner verdicts, so there is no independent signal on it at all.

## Related

- [Avoid AI Writing - AI-Pattern Audit & Rewrite Setup](/hermes/skills/catalog/avoid-ai-writing-setup)
- [Academic Writing Skills - Paper Workflow](/hermes/skills/catalog/academic-writing-skills-setup)
- [Ghostwriter - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/ghostwriter-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the rule table when you are reviewing someone else's rewrite. The default output is the text alone, which is right for pasting into a tool description and useless for auditing one.
- Run the linter first and the rewrite second. The mechanical pass costs nothing and tells you which sentences are worth the model's attention.
- Watch the `Kept as-is:` line. It is the skill telling you where precision and brevity disagreed, and those are the sentences a human should read.
- Keep Strict mode for anything a machine executes and STE-flavored for anything a human reads. Mixing them is how a README ends up sounding like a maintenance manual.
- Point it at the tool schema, not the tool code. The description field is what the model actually parses, and it is usually the shortest, highest-leverage text in the integration.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
