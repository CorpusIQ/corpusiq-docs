---
title: "AI Engineering from Scratch - Course Tutor Skills Setup"
description: "rohitg00/ai-engineering-from-scratch on skills.sh: 47.0K combined installs across 28 listings; skills that tutor a 542-lesson AI curriculum."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ai-engineering-from-scratch-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "ai engineering", "curriculum", "agent skills"]
---

# AI Engineering from Scratch - Setup Guide

**Source:** [rohitg00/ai-engineering-from-scratch](https://www.skills.sh/rohitg00/ai-engineering-from-scratch) via skills.sh - 47.0K combined installs across 28 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 77,600 stars, MIT, last pushed 2026-11-07, 48 SKILL.md files at this commit: 18 in `skills/`, an 18 directory mirror in `.claude/skills/`, and 12 more inside lesson and project outputs
**Category:** AI engineering education: a tutor led curriculum covering model internals, retrieval, agents and evaluation
**Quality Tier:** 🟡 Yellow - MIT with a LICENSE file in the root, but the first sampled skill returns a Snyk warn and the tutor reads lesson files over the network.

The repository is a curriculum first and a skill set second. It ships 542 lessons across 20 phases in four languages, from math foundations and model internals through retrieval pipelines, agent runtimes and evaluation. The skills are the teaching layer: they interview you, place you, then teach one lesson per session and quiz you at the end.

That makes this a different kind of install from a code skill library. Nothing here writes production code for you. The skills exist so an agent can run a structured course, keep state in a `LEARNING.md` file in your repository, and stream lessons from the project rather than reciting them from memory. The top five listings, from `start-learning` at 5,230 down to `course-guide` at 4,764, are all the tutor loop, which tells you what people actually install this for.

## Installation

The README installs with the skills CLI. Node and `npx` are required for the tutor, and `python3` for the runnable labs:

```bash
npx skills add rohitg00/ai-engineering-from-scratch
```

The installer asks for a host and a scope, and writes into that host's skills folder. The README is explicit that you should then confirm the host discovers that exact destination:

```bash
node --version
npx --version
python3 --version
```

Invocation belongs to the host, not to the portable `SKILL.md` format. In Codex the skill is `start-learning`, in Claude Code it is `/start-learning`, and other compatible hosts are asked by name:

| Host | Start the course | Start MCP | Start Agent Skills | Run a phase quiz |
|---|---|---|---|---|
| Codex | start-learning | learn-mcp | learn-agent-skills | check-understanding 13 |
| Claude Code | /start-learning | /learn-mcp | /learn-agent-skills | /check-understanding 13 |
| Other hosts | Use start-learning to begin the course | Use learn-mcp to start the MCP path | Use learn-agent-skills to start the Agent Skills path | Use check-understanding to quiz me on Phase 13 |

Hermes is not named in that table, but the "other compatible hosts" row is the documented behaviour: install the skills and ask for one by name. The tree keeps all 18 tutor skills as plain directories under `skills/`, which is the copy source if the installer does not know your host.

## What It Provides

Nineteen listings clear the 25-install threshold, which is most of the indexed set:

| Skill | Installs | Use For |
|---|---|---|
| start-learning | 5,230 | One time onboarding: interviews the learner, runs the placement quiz, writes a LEARNING.md study plan |
| find-your-level | 5,131 | Quiz that maps what you already know to a starting phase in the 20 phase curriculum |
| check-understanding | 5,131 | Phase quiz for one phase, triggered by "quiz me" or "do I know phase 3" |
| learn | 4,875 | Lesson tutor: reads LEARNING.md, teaches one lesson section by section, quizzes, records progress |
| course-guide | 4,764 | Topic router: give it a question or a bug and it points at the lessons that teach it |
| claude-certification | 3,948 | Tutor for the four Claude certification tracks, including preparation and onboarding |
| learn-mcp | 3,384 | Focused tutor for the MCP path: build, secure, debug, verify and operate MCP clients |
| learn-agent-skills | 3,381 | Tutor for the Agent Skills path: create, discover, invoke, secure, evaluate and package skills |
| mcpa-certification | 2,084 | Tutor and onboarding for the MCPA certification, with resume support |
| build-project | 1,878 | Project tutor that takes one stage per session: read, predict, write code, run it |
| isometric-explainer | 1,118 | Builds an interactive isometric page where each station stands for one step of a process |
| write-manual | 1,113 | Writes a long technical manual pinned to one version, with every claim traced to a source |
| blueprint-figure | 1,108 | Static SVG figures in the course visual language: nine figure kinds and fixed hue meanings |
| motion-figure | 1,106 | Figures that move or respond: SMIL animations, slider widgets, interactive mechanism diagrams |
| course-style | 1,104 | Shared visual and writing reference: colour tokens, font stacks, figure labels, card layout |
| learn-reverse-engineering | 1,060 | Tutor for the reverse engineering path: file formats, disassembly, control flow |
| lesson-screen | 364 | Opens a lesson screen beside the terminal with figures, code traces and clickable predictions |
| interview-prep | 199 | Mock interview coach: asks one question or incident scenario, then waits for your answer |
| skill-contract-reviewer | 40 | Validates a skill package and picks the right instruction, capability or lifecycle primitive |

The remaining 9 indexed listings range from 1 to 6 installs.

The install distribution is unusually honest. Two clusters: the tutor loop in the thousands, and the production skills in the low hundreds, with the build-your-own-skill examples at a single install each. The bottom cluster is course material rather than a product, and the guide treats it that way.

## Why This Matters for Hermes Agents

An agent is a good tutor and a poor teacher. Asked to explain retrieval augmented generation it will produce a confident lecture with gaps where the hard parts are. Asked to run lesson 12 of a fixed curriculum with a quiz at the end, it cannot skip ahead, and that difference is the whole value of this set.

The state file is the second good idea. `start-learning` writes a study plan to `LEARNING.md`, `learn` reads it each session and updates it as you finish lessons. That is a small piece of engineering that most agent workflows skip: durable progress outside the conversation, so a new session resumes instead of restarting.

The third is the router. `course-guide` takes a question or a bug you are fighting and points at the lessons that cover it, which turns a 542 lesson library into something you can search with a sentence. For a Hermes agent, that pattern generalises: any large document set benefits from a routing skill that maps a question to a file.

Two caveats for builders. The tutor streams lessons from the repository, so it needs network access and it is not a way to study offline. And the certification skills are study guides for third party exams, not guarantees, so treat the output as preparation material.

## Usage

| You say | What happens |
|---|---|
| "Where should I start with AI engineering?" | `start-learning` interviews you, runs the placement quiz and writes LEARNING.md with a starting phase |
| "Do I know phase 3 well enough to skip it?" | `check-understanding` quizzes that phase and reports what you got wrong |
| "Teach me the next lesson" | `learn` reads the study plan, fetches the next lesson, teaches it section by section and quizzes at the end |
| "I do not understand how attention works" | `course-guide` points at the exact lessons that cover attention and names the next command |
| "I want to prepare for the MCPA" | `mcpa-certification` opens the certification track and resumes where the study plan left off |
| "Build the embedding project stage 2" | `build-project` walks one stage: read the lesson, predict, write the code, run it, keep the result |
| "Quiz me for an AI engineering interview" | `interview-prep` asks one question or incident scenario and stops for your answer |

## Verification

Read the entry skill before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/skills/start-learning/SKILL.md | head -12
```

It should open with `name: start-learning`, a version line, and a description about one time onboarding that writes `LEARNING.md`.

After install, confirm the tutor set is complete. The `skills/` tree holds 18 directories:

```bash
ls skills | wc -l
```

Then ask the agent to use `start-learning` by name, as the README prescribes for hosts outside the table. If it starts a lecture instead of an interview, the skill did not load and the destination scope is the place to look.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07). This is a snapshot, so re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| start-learning | Pass | Pass | Warn |
| find-your-level | Pass | Pass | Pass |
| check-understanding | Pass | Pass | Pass |

The warn sits on the entry skill, which is the one that writes files. `start-learning` creates and updates `LEARNING.md` in your repository, and `learn` updates it as you progress, so the write scope is your working directory rather than a system path. Read the skill before running it in a repository you care about.

The lessons themselves are the content risk in a different sense. The curriculum teaches model internals, agent runtimes and evaluation, and the labs run real code with `python3`. That is ordinary development risk: read what a lesson asks you to execute before you execute it.

Nothing here needs credentials, and no skill in the sampled set calls a paid API. The network requirement is fetching lesson files from the repository.

The licence is MIT with a LICENSE file in the root, so forking the curriculum is allowed under the usual terms.

## Limitations

- Snapshot data, verified 2026-11-07: 47,043 combined installs across 28 indexed listings; 77,600 GitHub stars; MIT; last pushed 2026-11-07. Counts drift over time.
- The install index is wider than the tutor set. `skills/` holds 18 directories while the index lists 28, and `skill-contract-reviewer` (40 installs) lives only at `phases/13-tools-and-protocols/22-skills-and-agent-sdks/outputs/skill-contract-reviewer/SKILL.md`, not under `skills/`.
- Several listings are course artefacts rather than installable tutors. `release-review`, `release-publish`, `check-tests`, `orchard-release` and `orchard-review` sit at 1 install each and are example skills used inside the projects.
- The tutor streams lessons from the repository, so it needs network access. Offline study means copying lesson files yourself, which the README does not describe as a supported mode.
- The curriculum is under active development, last pushed the same day as this snapshot. Lesson numbering and phase contents can move, so a study plan written this month may need re-reading next month.
- Grading is self reported. The quizzes check your answers, but nothing verifies that you ran the labs, so progress in `LEARNING.md` reflects what the session claims.

## Related

- [AI Native Camp 2 - Builder Skills Collection](/hermes/skills/catalog/ai-native-camp-skills-setup)
- [Karpathy Guidelines - Coding Discipline Skill](/hermes/skills/catalog/karpathy-guidelines-setup)
- [AI Evals Skills - Product-Specific Evaluations](/hermes/skills/catalog/ai-evals-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `start-learning` once and commit `LEARNING.md`. The study plan is the state that makes the rest of the set useful across sessions.
- Use `check-understanding` before a phase, not after. Skipping a phase you already know is the fastest way through 542 lessons.
- Ask `course-guide` with the error message rather than the topic. It routes on the problem you actually have, which is usually narrower than the subject you name.
- Enrol in one certification track at a time. The four Claude tracks and MCPA share prerequisites, and running them together doubles the quiz load for the same material.
- Treat `build-project` as the real test. Reading a lesson takes minutes and keeping the project output is what the curriculum says you should have at the end.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
