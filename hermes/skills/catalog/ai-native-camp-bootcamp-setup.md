---
title: "AI Native Camp 1 - Korean Claude Code Curriculum"
description: "ai-native-camp/camp-1 on skills.sh: 10.1K combined installs across 9 listings; a Korean 7-day Claude Code camp shipped as skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ai-native-camp-bootcamp-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "curriculum", "onboarding"]
---

# AI Native Camp 1 - Setup Guide

**Source:** [ai-native-camp/camp-1](https://www.skills.sh/ai-native-camp/camp-1) via skills.sh - 10.1K combined installs across 9 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 242 stars, no licence (the repository has no LICENSE file), last pushed 2026-03-04, 7 `SKILL.md` files in the tree, five under `.agents/skills/` and the same five plus two more under `.claude/skills/`
**Category:** Builder curriculum for agents: a seven-day Claude Code course for non-developers, taught day by day as skills rather than slides
**Quality Tier:** 🟡 Yellow - two of the three sampled skills draw Socket and Snyk Warns, and the repository ships no LICENSE file, so there is no stated grant to reuse the material.

This is the first AI Native Camp cohort, and it is a different repository from the one this catalog documents as AI Native Camp 2. The camp-2 guide covers `ai-native-camp/camp-2`. This repository is `ai-native-camp/camp-1`, the earlier cohort, and its README title is the Korean form of AI Native Camp followed by the counter for cohort one. The two share a teaching model and a vocabulary, not a file tree, so the skill names and install counts in the two guides are not interchangeable.

The README describes a seven-day intensive for non-developers, run 2026-02-14 to 2026-02-21 with Sunday off, hosted at Naver D2SF. Its claim is in the delivery: the curriculum is the skills. A learner runs `/day1-onboarding` and the agent teaches, asks questions and drives the exercise, and each day's lesson builds on the skill the learner made the day before.

## Installation

One command installs the whole curriculum into Claude Code:

```bash
npx skills add ai-native-camp/camp-1 --agent claude-code --yes
```

A single day can be installed on its own, which is the documented pattern for learners who join late:

```bash
npx skills add ai-native-camp/camp-1 --skill day1-onboarding --agent claude-code --yes
npx skills add ai-native-camp/camp-1 --skill day4-wrap-and-analyze --agent claude-code --yes
```

The README then says to start from inside Claude Code with the slash command that matches the day, for example `/day1-onboarding` or `/day5-fetch-and-digest`.

Note the layout before you copy anything to Hermes. The five core lessons exist twice, once under `.agents/skills/<name>/` and once under `.claude/skills/<name>/`, and the last two skills, `day6-prd-submit` and `my-fetch-tweet`, appear only under `.claude/skills/`. The day lessons load their content from a `references/` folder of block files, so a copy that takes only `SKILL.md` breaks the lesson halfway through. Copy whole directories, include `references/`, and pick one of the two trees rather than merging them.

## What It Provides

Nine indexed listings, all above the reporting threshold:

| Skill | Installs | Use For |
|---|---|---|
| day1-onboarding | 1,732 | Day one over seven core features: CLAUDE.md, skills, MCP, subagents, Agent Teams, hooks and plugins, each block explained then practised |
| day2-create-context-sync-skill | 1,645 | Building a personal context-sync skill: tool selection, MCP or API connection, parallel collection and one merged output document |
| day2-supplement-mcp | 1,642 | A Day 2 supplement on MCP: concepts, adding a server, the `/mcp` command, popular servers and plugin-provided MCP |
| day4-wrap-and-analyze | 1,477 | Building a session-wrap skill by hand, then analysing sessions with history-insight and session-analyzer |
| day5-fetch-and-digest | 1,402 | Building fetch-tweet, fetch-youtube and content-digest, then wiring the three into one ingestion flow |
| day6-prd-submit | 1,326 | Writing a PRD from a template, validating the required format, then walking a GitHub pull request submission |
| my-fetch-tweet | 840 | Fetching an X post through the FxEmbed API and returning a summary, three insights and a full translation |
| day1-test-skill | 67 | Indexed listing with no matching directory in the current tree, so there is no local skill file to read before install |
| my-context-sync | 9 | Indexed listing with no matching directory in the current tree, while the Day 2 lesson builds a context sync skill by hand |

No indexed listings fall below the threshold; all 9 appear above.

The teaching mechanism is the notable part, and it is written into every lesson as a STOP PROTOCOL. Each block runs over two turns. In the first turn the agent reads the EXPLAIN section, explains the feature and gives the exercise, then stops and ends its turn without asking anything. The learner goes and does the exercise, comes back, and only then does the agent read the QUIZ section, ask questions with the user-question tool, give feedback and offer the next block. The protocol names the specific failures it forbids, including asking a quiz before the learner has tried the exercise.

## Why This Matters for Hermes Agents

An agent that teaches has to resist finishing the exercise for the learner, and the two-turn protocol here is the clearest written rule for that. Explain, hand over, stop, then check. Any Hermes skill that onboards a new operator, walks a client through a setup or runs a training session can borrow the structure directly, because the hard part is not the content, it is knowing when to stop talking.

The second pattern is skills that build skills. Day 2 has the learner build a context-sync skill, Day 4 builds session-wrap, Day 5 builds three ingestion skills. The lesson is the process, and the artefact persists after the camp. That is a better onboarding shape than a document, because the learner ends with working tooling rather than notes.

Third, the closing loop is reusable. `day4-wrap-and-analyze` builds a session wrap, then uses history-insight and session-analyzer to check what happened in the session. That trio is a small verification harness, and it ports to any agent that leaves work behind.

The Day 6 lesson is the only one that touches the outside world. It writes a PRD, validates its format, and then walks a real pull request through `git` and the `gh` CLI, which is also where the security consideration sits.

## Usage

| You say | What happens |
|---|---|
| "Day 1" or "start the camp" | `day1-onboarding` runs the onboarding lesson block by block, explaining a feature, stopping while you try it, then quizzing |
| "Day 2, teach me MCP" | `day2-supplement-mcp` covers concepts, server install, the `/mcp` command and plugin MCP before the hands-on block |
| "Build my own context sync skill" | `day2-create-context-sync-skill` walks tool choice, connection, parallel collection and output format, ending with a working skill |
| "Wrap this session and tell me what to keep" | `day4-wrap-and-analyze` has you build the wrap skill, then analyses the session with the two companion skills |
| "Make a fetch and digest skill" | `day5-fetch-and-digest` builds fetch-tweet, fetch-youtube and content-digest, then joins them into one flow |
| "Submit my PRD as a pull request" | `day6-prd-submit` drafts the PRD, checks the required format and guides the git and gh steps |
| "Summarise and translate this X post" | `my-fetch-tweet` pulls the post through the FxEmbed API and returns a summary, three insights and a translation |

## Verification

Read the entry lesson before installing. This path returned HTTP 200 on `main` when this guide was written, and the dot-prefixed directory is part of it:

```bash
curl -fsSL https://raw.githubusercontent.com/ai-native-camp/camp-1/main/.agents/skills/day1-onboarding/SKILL.md | head -12
```

It should open with `name: day1-onboarding` and a Korean description naming Day 1 and onboarding. The second check is the skill that sits only in the other tree, which proves both layouts are live:

```bash
curl -fsSL https://raw.githubusercontent.com/ai-native-camp/camp-1/main/.claude/skills/day6-prd-submit/SKILL.md | head -12
```

After install, confirm seven directories landed in the skills directory your agent uses, and that each day lesson arrived with its `references/` folder. Then run `/day1-onboarding` and check that the agent stops after the first exercise instead of continuing to the quiz. If it does not stop, the lesson body did not load and the agent is improvising.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| day1-onboarding | Pass | Pass | Pass |
| day2-create-context-sync-skill | Pass | Warn | Warn |
| day2-supplement-mcp | Pass | Warn | Warn |

Two of the three sampled skills draw a Warn from Socket and Snyk, and the two are the Day 2 pair that connect the agent to external services. Read them before running them, since installing an MCP server is exactly the step where an agent can add reach you did not intend.

The repository ships no LICENSE file. Under default copyright that means all rights reserved, so there is no stated grant to copy, modify or redistribute the skill text. Read it as curriculum material, and ask the author before you reuse it inside a product.

Two data notes. `my-fetch-tweet` sends post URLs to `api.fxtwitter.com`, a third-party public API, so the URLs you feed it leave your machine. `day6-prd-submit` assumes `git` and an authenticated `gh` CLI and pushes a branch to a repository you have write access to, which means the lesson can put a real PR in front of a real team.

## Limitations

- Snapshot data, verified 2026-11-07: 10,140 combined installs across 9 indexed listings; 242 GitHub stars; no licence (no LICENSE file); last pushed 2026-03-04. Counts drift over time.
- No licence. There is no LICENSE file, so the default is all rights reserved rather than a permissive grant. Treat the skills as course material and get permission before shipping them inside a product.
- The whole curriculum is in Korean, bodies and trigger phrases alike. An English prompt will usually miss the triggers, and translating them changes what the lesson matches on.
- Nine indexed listings against seven files in the tree. `day1-test-skill` (67 installs) and `my-context-sync` (9) have no matching directory, so there is nothing to read before installing those two.
- The course is incomplete by design. The README's curriculum table shows Day 3 and Day 7 as coming soon, and the repository stops at Day 6, so a learner finishes without the graduation lesson the README promises.
- Last push is 2026-03-04, so the lessons describe Claude Code as it stood in early 2026, including the Agent Teams and plugin features from that period.
- Installs cluster tightly between 840 and 1,732 for the seven lessons, with a two-listing tail at 67 and 9. That shape reads as one cohort installing the set, not as independent adoption, so the counts are reach inside the camp rather than a quality ranking.
- Do not mix this repository with camp-2. The catalog's AI Native Camp 2 guide covers `ai-native-camp/camp-2`, a later cohort with different skills and different counts.

## Related

- [AI Native Camp 2 - Builder Skills Collection](/hermes/skills/catalog/ai-native-camp-skills-setup)
- [Context Engineering Skills Setup](/hermes/skills/catalog/context-engineering-skills-setup)
- [Claude Scholar - Research Pipeline for Agents](/hermes/skills/catalog/claude-scholar-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the days in order. Day 4 wraps the session tooling Day 2 introduced, and Day 5's digest skill assumes the fetch pattern from the Day 2 lesson.
- Copy directories, not files. Every day lesson reads block files from `references/`, and a lone `SKILL.md` produces a lesson that stops at the first block.
- Watch the first turn of `/day1-onboarding` closely. If the agent asks a quiz question before you have tried the exercise, the STOP PROTOCOL did not load and the rest of the lesson will be improvised.
- Take `day4-wrap-and-analyze` even if you skip the camp. The session wrap and session analysis pattern works outside a classroom, and it is the one artefact that survives the course.
- Read `day6-prd-submit` before running it in a real repository. It pushes a branch and opens a pull request, so point it at a scratch repository the first time.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
