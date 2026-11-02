---
title: "Karpathy Guidelines - Coding Discipline Skill"
description: "multica-ai/andrej-karpathy-skills: 43.9K combined installs. One skill that turns Karpathy's notes on LLM coding into four rules for editing code."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/karpathy-guidelines-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "coding discipline", "code review", "prompting"]
---

# Karpathy Guidelines - Setup Guide

**Source:** [multica-ai/andrej-karpathy-skills](https://www.skills.sh/multica-ai/andrej-karpathy-skills) via skills.sh - 43.9K combined installs across 1 indexed listing; first seen 2026-11-02 (morning sweep)

**GitHub:** [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) - 228,252 stars, no license file in the repository, branch main, last pushed 2026-04-20; 1 `SKILL.md` at `skills/karpathy-guidelines/SKILL.md`, plus a root `CLAUDE.md`, a committed Cursor rule and a plugin manifest

**Category:** Coding discipline for agents: four principles against wrong assumptions, overcomplication and orthogonal edits

**Quality Tier:** 🟡 Yellow - a clean audit and 228,252 stars, but the repository ships no license file and its own install commands point at an upstream owner path

The repository takes the three complaints Andrej Karpathy made about LLM coding and reduces them to four principles in one short file. The complaints were that models run with wrong assumptions instead of surfacing them, that they bloat code and APIs, and that they rewrite comments and code they do not understand as a side effect. The answer is a single behavioural document: think before coding, simplicity first, surgical changes, and goal-driven execution, each with a test the model can apply to itself. It is 67 lines as a skill and 65 as `CLAUDE.md`, and the two carry the same four sections.

Distribution is the unusual part. The same text ships three ways: as `CLAUDE.md` for Claude Code projects, as `.cursor/rules/karpathy-guidelines.mdc` with `alwaysApply: true` for Cursor, and as an Agent Skill at `skills/karpathy-guidelines/SKILL.md` with the frontmatter a skills runtime routes on. A 522-line `EXAMPLES.md` shows each principle as a wrong implementation followed by the corrected one, with an anti-pattern summary at the end. Nine files in the repository, all of them text, and nothing to execute.

## Installation

The README documents two routes, and neither is the skills CLI. Option A is the Claude Code plugin, which makes the guidelines available across projects:

```text
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

Option B is the file itself, per project. This is the route that works for any agent that reads a root instruction file:

```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

To add it to a project that already has one, append rather than overwrite:

```bash
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

For Cursor the rule is committed with `alwaysApply: true`, so opening the repository as a workspace is enough; `CURSOR.md` explains copying the rule into another project.

The README names no `npx skills add` command, so the skill installs through the generic skills.sh CLI path, which writes it into the agent's skills directory:

```bash
npx skills add multica-ai/andrej-karpathy-skills
```

For a Hermes profile, install with the CLI above or copy the folder, since the repository names Claude Code, Cursor and any root-instruction reader and nothing Hermes-specific:

```bash
git clone --depth 1 https://github.com/multica-ai/andrej-karpathy-skills.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -R andrej-karpathy-skills/skills/karpathy-guidelines ~/.hermes/profiles/corpusiq/skills/
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| karpathy-guidelines | 43,921 | Four behavioural rules for code work, each with a self-test: state assumptions and stop when confused before writing anything, minimum code with nothing speculative, touch only what the request requires and clean up only your own orphans, and turn each task into a plan where every step names how it is verified. |

No indexed listings fall below the threshold; the single listing above is the whole index.

The four principles map to the three complaints one for one. Think Before Coding covers wrong assumptions, hidden confusion and missing tradeoffs: state assumptions explicitly, present multiple interpretations instead of picking one silently, push back when a simpler approach exists, and stop when something is unclear. Simplicity First covers overcomplication: no features beyond what was asked, no abstractions for single-use code, no flexibility nobody requested, and if 200 lines could be 50, rewrite it. Surgical Changes covers the orthogonal edit: do not improve adjacent code, do not refactor what is not broken, match the existing style, mention dead code instead of deleting it, and remove only the imports and variables your own change orphaned. Goal-Driven Execution covers leverage: "Add validation" becomes "write tests for invalid inputs, then make them pass", and a multi-step task gets a numbered plan with a verify line per step.

## Why This Matters for Hermes Agents

Most agent failures on real repositories are not capability failures, they are scope failures. The diff arrives larger than the request, a helper nobody asked for is introduced, a comment is rewritten on the way past, and the reviewer has to reconstruct which lines were actually intended. These four rules put the boundary in writing, and the two tests they give the model are checkable from inside the diff: would a senior engineer call this overcomplicated, and does every changed line trace to the request.

The second half is about honesty. An agent that does not know whether "export the data" means all rows or a page, and writes the code anyway, has converted an ambiguity into a bug. Think Before Coding turns that into a question, which is cheaper to answer than a reverted commit. For an unattended Hermes run the same rule is what stops a plausible assumption from becoming an executed plan.

Goal-Driven Execution is the principle that fits how modern agents actually work. A weak goal such as "make it work" needs a human in the loop at every step; a criterion such as "the test reproduces the bug and then passes" lets the agent iterate on its own and stop when it is done. That is the difference between an agent you supervise turn by turn and one you can hand a ticket.

It is also cheap to adopt. There is no runtime, no dependency and no configuration: the skill is 67 lines of Markdown, so it can sit alongside any other skill in a profile without competing for context, and `EXAMPLES.md` gives the operator a worked reference for reviewing what the agent produced.

## Usage

| You say | What happens |
|---|---|
| "Add validation to the signup form" | The agent restates the criteria as "write tests for invalid inputs, then make them pass" and works to that, instead of adding validation it guessed at and calling it done. |
| "Fix the login bug" | It writes or finds a test that reproduces the failure first, then fixes until the test passes, so the fix has evidence behind it. |
| "Refactor the config loader" | It records that the tests pass before the change and confirms they pass after, and it does not take the opportunity to tidy the neighbouring modules. |
| "Add a retry to the payment call" | It states the assumption it is making (which errors retry, how many times) or asks, rather than choosing silently. |
| "Add pagination to the users endpoint" | On a request with an ambiguity it presents the interpretations, for example cursor versus offset, instead of picking one and running with it. |
| "This module feels bloated" | It applies the simplicity test to its own change, drops speculative options and single-use abstractions, and rewrites a 200-line construction that could be 50. |
| "Review this diff" | It checks the diff against the four rules: assumptions surfaced, no unrequested features, no orthogonal edits, and a stated way to verify the result. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/multica-ai/andrej-karpathy-skills/main/skills/karpathy-guidelines/SKILL.md
```

After installing, confirm the skill is the one the runtime routes on, and that a copy did not land twice:

```bash
git clone --depth 1 https://github.com/multica-ai/andrej-karpathy-skills.git /tmp/karpathy-skills
find /tmp/karpathy-skills -name SKILL.md | wc -l
head -4 /tmp/karpathy-skills/skills/karpathy-guidelines/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/karpathy-guidelines
```

The count should print 1, and `head` should show the `name: karpathy-guidelines` line and the description the agent reads when deciding to load it. The last command should list a single `SKILL.md`.

The three distributions should carry the same four sections. This check confirms it before you trust one copy over another:

```bash
grep -c '^## ' /tmp/karpathy-skills/CLAUDE.md
grep -c '^## ' /tmp/karpathy-skills/skills/karpathy-guidelines/SKILL.md
```

Both should print 4, which is the four principles and nothing else.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| karpathy-guidelines | Pass | Pass | Pass |

The one sampled listing passes all three auditors, so there is no Warn or Fail to report. The installation is nine text files and nothing else: no install script, no postinstall hook, no executable, no network call at load time. The `curl` in the README's option B writes a Markdown file into the current project, which is worth reading before you run it, because it overwrites `CLAUDE.md` in place if one already exists, and the append form is the safe one for an existing project.

The repository has no license file, so there is no explicit grant to redistribute or reuse the text even though the README, the skill frontmatter (`license: MIT`) and the plugin manifest all state MIT. Treat that as a claim rather than a licensed artifact until a `LICENSE` file appears, and do not republish the text from a Hermes profile without deciding that for yourself.

The content risk is the ordinary one for behavioural prompts: these instructions change how the agent works on every task in the scope where they are installed. They bias toward caution, which costs turns on small jobs, so read the file before you put it in a global skills directory.

## Limitations

- Snapshot data, verified 2026-11-02: 43,921 combined installs across 1 indexed listing; 228,252 GitHub stars; no license file; last pushed 2026-04-20. Counts drift over time.
- No `LICENSE` file exists in the repository, while the README says MIT, the skill says `license: MIT` and the plugin manifest sets `"license": "MIT"`. Cite both positions and treat reuse as source-available rather than licensed.
- The README's install commands name `forrestchang/andrej-karpathy-skills`, which is not the repository the skills.sh listing indexes, and the plugin manifest still credits `forrestchang` as owner. The generic `npx skills add multica-ai/andrej-karpathy-skills` path is the one that matches this listing.
- One skill of 67 lines and nothing else: no scripts, no tests, no version history since 2026-04-20. The 228,252 stars are out of all proportion to nine files, so read the star count as attention rather than as evidence of maintenance.
- The pack states its own tradeoff: the guidelines bias toward caution over speed, and trivial tasks such as a typo fix do not need the full rigour. Installed globally, they will add questions to small jobs.

## Related

- [Agent Architect - Agent System Design Setup](/hermes/skills/catalog/agent-architect-setup)
- [Agent Skill Creator - Skill Generation and Templating Setup](/hermes/skills/catalog/agent-skill-creator-setup)
- [Advanced Skill Creator - Custom Skill Generation Setup](/hermes/skills/catalog/advanced-skill-creator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install it per project rather than globally at first. The guidelines change how every task in scope is approached, and a week of one repository tells you whether the extra questions are worth the turns.
- Keep the two tests in your review checklist. "Would a senior engineer say this is overcomplicated" and "does every changed line trace to the request" are the whole value of the file compressed into two questions you can ask of any diff.
- If you already maintain a `CLAUDE.md` or an `AGENTS.md`, append rather than replace, and merge the project-specific rules underneath. The README's own example adds a "Project-Specific Guidelines" section for exactly this.
- Read `EXAMPLES.md` once yourself before trusting the agent with it. The four worked examples show the failure and the correction side by side, which is a faster calibration than reading the rules alone.
- Pair it with a skill that supplies the verification, not one that duplicates the discipline. The rules say a step must name how it is checked; a testing skill is what makes that check real.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
