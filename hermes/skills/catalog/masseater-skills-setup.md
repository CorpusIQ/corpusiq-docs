---
title: "Masseater Skills - Engineering Judgment Suite"
description: "Masseater skills: 13.0K combined installs. Nine Japanese-language skills on measuring before guessing, writing prose humans read, and using what exists."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/masseater-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "engineering", "writing", "plugin"]
---

# Masseater Skills - Engineering Judgment Suite

**Source:** [masseater/skills](https://www.skills.sh/masseater/skills) via skills.sh - 13.0K combined installs across 10 indexed listings; new to this catalog in the Oct 24, 2026 evening sweep

**GitHub:** [masseater/skills](https://github.com/masseater/skills) - 2 stars, no LICENSE file, last pushed 2026-10-24, branch main, 10 skill directories under `skills/` plus a `.claude-plugin` manifest for plugin installs

**Category:** Engineering Practice / Writing Discipline

**Quality Tier:** 🟡 Beta - consistent, well argued skill bodies and clean auditor verdicts, but no license file, two stars, and every skill body is written in Japanese

Most skill collections answer "what tool do I use". This one answers "how do I work". Each skill is a short set of rules aimed at a failure mode the author kept hitting: deciding from a plausible guess instead of a measurement, adding a library without migrating the code that should use it, writing code that the repository already has, producing prose that reads like a machine assembled it. The bodies are structured the same way, starting from why the skill exists and what state it is trying to reach, then the rules themselves.

The scale is small and the install counts are not. Nine of the ten listings clear a thousand installs, which is unusual for a two-star repository and suggests the skills are being copied rather than browsed. That fits the content: these are portable working agreements rather than tool documentation, and the three that carry the most installs are the three most transferable rules in the set.

The one thing to decide before installing is language. Every `SKILL.md` is written in Japanese, including the section headings, so an English-first agent will load a skill whose rules it has to interpret rather than follow directly. That is a real cost and it is the reason this guide sits in Beta rather than Production.

## Installation

Two paths, both documented in the README.

As a Claude Code plugin:

```bash
claude plugin marketplace add masseater/skills
claude plugin install masseater-skills@masseater
```

Or from inside a Claude Code session:

```text
/plugin marketplace add masseater/skills
/plugin install masseater-skills@masseater
```

For any other agent that reads the Agent Skills format:

```bash
npx skills add masseater/skills
```

To apply the same set to everyone working in one repository, the README shows the project level form: add the marketplace and enable the plugin in that repository's `.claude/settings.json` under `extraKnownMarketplaces` and `enabledPlugins`.

Each skill directory is self contained, so copying a single `skills/<name>/` folder into your agent's skills directory gives the same result as the CLI without the rest of the set.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| measure-dont-guess | 1,619 | Decide the measurement that settles a hypothesis before implementing or fixing anything, then judge only on the result: production or production-identical conditions, unmeasured claims labelled as guesses. |
| integrate | 1,564 | Adopting a library or a new implementation approach properly: migrate the existing code and add the mechanical enforcement that makes everyone use the new path. |
| how-to-use-react | 1,564 | React 19.3 components, loaders and server work: where state lives, how async is structured, where concurrent UI APIs apply, and how prop shapes are decided. |
| skill-authoring | 1,438 | Writing, fixing and reviewing Agent Skills, deriving the body from why the skill is needed and the state it wants to reach rather than from a template. |
| humanity-and-humanness | 1,425 | Giving the agent a working model of how humans read, think and infer, for prose a person will read, for asking a user to decide, and for reading the intent behind feedback. |
| setup-template | 1,412 | Bringing a repository created from the author's TypeScript template back in line with it, including GitHub settings through `gh` and a completeness check on the migration. |
| poteto-principles | 1,364 | A principles list applied at the start of design, implementation, fixes, refactors, migrations, verification and documentation changes. |
| writing | 1,263 | Writing and polishing documentation, comments, commit messages, pull request bodies and articles, including the repair case where text reads as machine written or is hard to follow. |
| dont-it-yourself | 1,231 | Searching libraries, runtimes and the repository itself for what already exists, before writing a new helper, wrapper, tool or external API client. |

The remaining 1 indexed listing is setup-github (82 installs), a GitHub configuration companion to setup-template with no directory in the current tree. In the other direction, the tree carries a `blog-writing` skill that the install index does not list.

## Why This Matters for Hermes Agents

An autonomous agent fails in predictable ways, and almost none of them are knowledge failures. It guesses at a cause because guessing is faster than measuring. It adds a dependency and leaves the old call sites in place. It writes a helper that already exists three directories away. It produces a document that is accurate and unreadable.

This set is a checklist against exactly those four failures, which is why it is worth loading even though it teaches no tool. `measure-dont-guess` is the strongest of them: state the hypothesis and the threshold before you measure, measure in production or in a production-identical environment, label unmeasured claims as guesses, and when something cannot be measured, tell the user what is missing instead of proceeding on an assumption. That is a direct constraint on the behaviour that makes agents untrustworthy.

`dont-it-yourself` and `integrate` are complements. One stops the agent from writing code the repository already has, the other stops the agent from leaving a half migration behind after adopting something new, which is how codebases accumulate two ways of doing one thing.

The language cost is the honest limit. The rules are short and structured, but the agent reads Japanese and an English-speaking user cannot audit a skill they cannot read. Skim one body before installing the set, and if the language is a blocker for your workflow, take `measure-dont-guess` alone and restate the rule in your own `AGENTS.md`.

## Usage

| You say | What happens |
|---|---|
| "Why is this endpoint slow" | measure-dont-guess fixes the hypothesis and the threshold first, measures under production-like conditions, and reports the result as the only basis for a change. |
| "Add Zod validation to the API" | integrate wires the library, migrates the existing call sites and adds the enforcement that stops new code bypassing it. |
| "Write a date formatter" | dont-it-yourself checks the runtime, the libraries and the repository for something that already does it before any code is written. |
| "Write the PR description" | writing structures the body for a reviewer: what changed, why, and what to check, without the machine cadence. |
| "Draft a note to the client about the delay" | humanity-and-humanness models how the reader will interpret the message and what they need to decide before the wording is chosen. |
| "Turn this session into a reusable skill" | skill-authoring derives the body from the reason the skill exists and the outcome it should produce, then checks the structure. |
| "Review this component for state bugs" | how-to-use-react checks where state lives and how async is structured against React 19.3 patterns. |

## Verification

Confirm the layout on main before installing:

```bash
for p in skills/measure-dont-guess/SKILL.md \
         skills/writing/SKILL.md \
         skills/skill-authoring/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/masseater/skills/main/$p"
done
```

Read the two skills that will shape your agent's behaviour most before enabling them:

- https://raw.githubusercontent.com/masseater/skills/main/skills/measure-dont-guess/SKILL.md
- https://raw.githubusercontent.com/masseater/skills/main/skills/dont-it-yourself/SKILL.md

After install, `npx skills list` should show the skills that were written, and for the plugin path `claude plugin details masseater-skills@masseater` lists what the marketplace resolved. Confirm the manifest exists if you install as a plugin:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/masseater/skills/main/.claude-plugin/plugin.json
```

## Security

skills.sh verdicts for sampled skills (verified October 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| measure-dont-guess | Pass | Pass | Pass |
| integrate | Pass | Pass | Pass |
| how-to-use-react | Pass | Pass | Pass |
| skill-authoring | Pass | Pass | Pass |
| writing | Pass | Pass | Pass |

All five sampled listings pass all three auditors, which is what a set of instruction only skills should return: there is no executable code, no network call and no credential in the repository.

The audit that matters here is a reading one. These skills change how your agent behaves, not what it can run, so the review is whether you agree with the rules. `measure-dont-guess` forbids acting on unmeasured assumptions, which will make an agent slower and more annoying in exchange for being right more often. `dont-it-yourself` will push it to search before writing, which occasionally means it uses a dependency you did not want. Read before you install, and drop the skills whose rules you do not want enforced.

## Limitations

- Snapshot data, verified October 24, 2026: 12,962 combined installs across 10 indexed listings; 2 GitHub stars; no LICENSE file; last pushed 2026-10-24. Counts drift over time.
- No license file means no explicit grant. Reading and adapting the rules for internal use is the safe assumption; redistributing the text is a question for the author.
- Every skill body is written in Japanese, including headings. An English-first agent can still follow the structure but is interpreting rather than reading.
- The install index and the tree disagree in both directions: setup-github has 82 installs and no directory, while blog-writing has a directory and no listing.
- Two stars and one author. There is no community review behind these rules beyond the install counts.
- `setup-template` is written against one specific TypeScript template and its README says to confirm the procedure with the user before applying it to another repository.

## Related

- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup)
- [Humanizer Setup](/hermes/skills/catalog/humanizer-setup)
- [Avoid AI Writing - AI-Pattern Audit & Rewrite Setup](/hermes/skills/catalog/avoid-ai-writing-setup)

## Pro Tips

- Install `measure-dont-guess` on its own first. It changes agent behaviour the most and it is the easiest of the set to judge after a week of use.
- Pair `writing` with a house style document. The skill carries the structure and the anti machine-cadence rules, not your product vocabulary.
- Use `integrate` at the moment you adopt a dependency, not after. The migration half is what the skill exists for and it is hardest to apply retroactively.
- Drop `setup-template` if you do not use the author's template. It is the most repository specific skill in the set.
- Keep the plugin manifest path in mind when sharing: `.claude-plugin/plugin.json` plus `skills/` is what makes a one command install possible for a team.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
