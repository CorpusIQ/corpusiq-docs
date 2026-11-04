---
title: "AI Native Camp 2 - Builder Skills Collection"
description: "ai-native-camp/camp-2 on skills.sh: 16.6K combined installs across 12 listings; a Korean-language Claude Code cohort curriculum shipped as skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ai-native-camp-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "curriculum", "session tooling"]
---

# AI Native Camp 2 - Setup Guide

**Source:** [ai-native-camp/camp-2](https://www.skills.sh/ai-native-camp/camp-2) via skills.sh - 16.6K combined installs across 12 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 19 stars, no licence (the repository has no LICENSE file), last pushed 2026-03-22, 12 SKILL.md directories under .claude/skills/
**Category:** Builder curriculum for agents: AI-native product work, prototyping and shipping loops from the Camp 2 cohort
**Quality Tier:** 🟡 Yellow: day1-onboarding draws a Gen Agent Trust Hub Fail, and the repository ships no LICENSE file, so there is no stated reuse grant

Camp 2 is the second cohort of AI Native Camp, a seven-day Claude Code intensive for non-developers taught in Korean. What earns it a catalog entry is the delivery model rather than the syllabus: the curriculum is shipped as skills, so running a day lesson teaches that day inside the agent instead of in slides. The README puts it plainly, that the curriculum is the skills themselves.

The repository holds 12 skills in `.claude/skills/`. Four are the day lessons, one is a deliberately trivial test skill for day one, and seven are the tooling the later days build or lean on: `session-wrap`, `history-insight`, `session-analyzer`, `content-digest`, `fetch-tweet`, `team-assemble` and `compound`. The README states the prerequisites (a Claude Pro, Max, Teams or Enterprise account, 4GB of RAM, and no Node.js needed if you use the native installer) and says to start with `/day1-onboarding`.

## Installation

The camp-install line is one command, and it installs every curriculum skill:

```bash
npx skills add ai-native-camp/camp-2 --agent claude-code --yes
```

Then start the curriculum from inside Claude Code:

```text
/day1-onboarding
```

If Claude Code is not installed yet, the README's native installer needs no Node.js:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows takes a PowerShell one-liner (`irm https://claude.ai/install.ps1 | iex`) or a CMD variant, both listed in the README. Once `claude` starts and greets you, the account handshake is done and the skills are ready.

For Hermes, copy the `.claude/skills/<name>` directories you want into the profile skills directory. The day lessons reference each other by name in their bodies, so copy the whole set if you intend to follow the curriculum in order.

## What It Provides

Four day lessons, one test skill and seven pieces of session tooling.

| Skill | Installs | Use For |
|---|---|---|
| day1-onboarding | 1,566 | Day one walkthrough of seven features: memory, skills, MCP, subagents, agent teams, hooks, plugins |
| day3-clarify | 1,484 | Clarifies vague requirements, writes a PRD, creates a skill and opens a first GitHub PR |
| day2-mcp-and-context-sync | 1,477 | MCP deep dive, then builds a context-sync skill hands on |
| day4-wrap-and-analyze | 1,476 | Builds session-wrap, then analyses sessions with history-insight and session-analyzer |
| day1-test-skill | 1,469 | A minimal skill run as /day1-test-skill to show how skill execution feels |
| session-wrap | 1,327 | End-of-session closeout: what was done, what to commit, what was learned |
| history-insight | 1,323 | Captures and reviews Claude Code session history as a source for summaries |
| fetch-tweet | 1,318 | Reads, translates or analyses an X post; usable as a dependency by other skills |
| content-digest | 1,307 | Digests a YouTube video, X post, web page or PDF into study notes |
| session-analyzer | 1,289 | Post-hoc analysis of a session log to check whether a skill actually executed |
| team-assemble | 1,287 | Decomposes a task into specialist roles run in parallel through TeamCreate |
| compound | 1,283 | Accumulates insights from work into structured documents so the knowledge base compounds |

All 12 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

The day lessons are a worked example of teaching a workflow rather than documenting one. Each is a skill that asks questions and drives exercises, which is the same shape a Hermes agent needs when it onboards a new operator.

The closing loop is the transferable part. `session-wrap` ends a session with a summary and a commit plan, `history-insight` pulls the transcript back as evidence, and `session-analyzer` checks after the fact whether a skill actually ran. That trio is a small verification harness, and the idea ports to any agent that leaves work behind.

`team-assemble` shows the decomposition pattern for parallel specialist work. It splits a task into roles and runs them through TeamCreate, which is the same fan-out shape as a subagent dispatch with a named role per branch.

`content-digest` is a clean ingestion front end: one entry point over YouTube transcripts, X posts, pages and PDFs, and it calls `fetch-tweet` for X instead of duplicating the logic. That kind of dependency between skills is worth copying.

The caveat is language. The skill bodies and their trigger phrases are Korean, so an English-only workflow will read them but may not match the triggers without rewriting them.

## Usage

| You say | What happens |
|---|---|
| "Day 1" | day1-onboarding walks the seven core Claude Code features with hands-on exercises |
| "Day 2, MCP and context sync" | day2-mcp-and-context-sync explains MCP, then builds a context-sync skill with you |
| "Clarify this requirement and open my first PR" | day3-clarify tightens the requirement, then the PRD and GitHub steps follow |
| "Wrap up this session" | session-wrap summarises the work and proposes what to commit |
| "Did that skill actually run?" | session-analyzer reads the session log and checks the skill execution |
| "Digest this video and this tweet" | content-digest transcribes and summarises both, calling fetch-tweet for the post |
| "Assemble a specialist team for this task" | team-assemble splits the task into roles and runs them in parallel |

## Verification

Confirm the skills landed in the agent skills directory:

```bash
ls ~/.claude/skills
```

Then fetch one raw file before installing. This path is `.claude/skills/session-wrap/SKILL.md` on branch main and returned 200 when this guide was written; the dot-prefixed directory is part of the path:

```bash
curl -fsSL https://raw.githubusercontent.com/ai-native-camp/camp-2/main/.claude/skills/session-wrap/SKILL.md | head -20
```

Frontmatter with a name and a description confirms the listing is backed by a real file. `.claude/skills/day1-onboarding/SKILL.md` is the other one worth checking, since it is the entry point the README names. The install index is at https://www.skills.sh/ai-native-camp/camp-2.

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| day1-onboarding | Fail | Pass | Pass |
| day4-wrap-and-analyze | Pass | Warn | Warn |
| history-insight | Warn | Pass | Pass |
| session-analyzer | Warn | Pass | Pass |
| compound | Pass | Pass | Pass |

`day1-onboarding` is the only Fail in the sample, and it is also the first skill the README tells you to run. Read its body before running it against a machine that holds real project files. The repository also ships no LICENSE file, so there is no stated grant to copy, modify or redistribute the skill text; ask the author before reusing it in a product.

## Limitations

- No licence. The repository has no LICENSE file, so the default is all rights reserved rather than a permissive grant. Read the skills as curriculum material and get permission before redistributing or shipping them inside a product.
- Snapshot data, verified November 4, 2026: 16,606 combined installs across 12 indexed listings; 19 GitHub stars; no licence; last pushed 2026-03-22. Counts drift over time.
- The install counts sit between 1,283 and 1,566 against 19 GitHub stars, which reads like one cohort installing the whole set at once. Treat the counts as reach inside the camp, not as independent adoption or quality ranking.
- The skills and their trigger phrases are Korean. An English prompt may not fire them, and translating the triggers changes what the lesson matches on.
- Last push was 2026-03-22, so the curriculum is pinned to how Claude Code looked in early 2026. Features it teaches may have moved since.
- `day1-test-skill` exists only to demonstrate skill execution on day one. Outside the lesson it does nothing useful, and its install count is not a signal of value.

## Related

- [Agentic Awesome Skills - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the day lessons in order. Each one assumes the skill you built the day before exists, and `day4-wrap-and-analyze` builds on `session-wrap` directly.
- Read the Korean trigger phrases before rewriting them. The day skills key off cohort vocabulary, and a blunt translation can collide with your other skills.
- Take `session-wrap` and `session-analyzer` even if you skip the rest. They are the two that pay off outside a classroom.
- Keep `fetch-tweet` if you install `content-digest`. The digest skill calls it for X links rather than reimplementing the fetch.
- Copy the directories, not the text. The lessons reference sibling skills by name, so a loose paste of one SKILL.md breaks the chain.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
