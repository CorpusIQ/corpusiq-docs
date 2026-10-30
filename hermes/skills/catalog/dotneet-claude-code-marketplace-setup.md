---
title: "Dotneet Claude Code Marketplace - Plugin Collection Setup"
description: "dotneet/claude-code-marketplace: 12.9K combined installs. Claude Code plugins for React code review, prompt improvement and agent handoff."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dotneet-claude-code-marketplace-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "prompt engineering", "claude code"]
---

# Dotneet Claude Code Marketplace - Setup Guide

**Source:** [dotneet/claude-code-marketplace](https://www.skills.sh/dotneet/claude-code-marketplace) via skills.sh - 12.9K combined installs across 10 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [dotneet/claude-code-marketplace](https://github.com/dotneet/claude-code-marketplace) - 3 stars, no license file (the GitHub API also reports no license), branch main, last pushed 2026-01-23; 10 `SKILL.md` files in one layout, `<plugin>/skills/<name>/SKILL.md`, across six plugin directories (agent-call with three skills, agent-session, google, prompt, research with two and review-tool with two), beside the root catalog `.claude-plugin/marketplace.json`, a per-plugin `.claude-plugin/plugin.json`, `CLAUDE.md` and `.claude/docs/`

**Category:** Mixed plugin marketplace: code review, prompt improvement and UI helpers

**Quality Tier:** 🟡 Beta - 1 sampled FAIL verdict(s) in the security table; review before install. Covers ten small skills: one TypeScript and React 19 reviewer, one prompt rewriter, and eight helpers for agent delegation, research lookups, calendar access and agent rule suggestions.

The repository is a personal Claude Code marketplace published by Shinji Yamada under the `dotneet` handle, described in its own README as "a collection of plugins and skills for Claude Code". Six plugins are registered in `.claude-plugin/marketplace.json`, `agent-call`, `agent-session`, `research`, `review-tool`, `google` and `prompt`, holding ten skills between them, and the install counts are lopsided: `typescript-react-reviewer` alone carries 8,966 of the 12,917 combined installs while the other nine sit between 402 and 512. The README's plugin table names only four of the six, so the catalog and the documentation disagree on the size of the suite.

What the skills actually are is uneven, and that is the useful thing to know before installing. Three of them are delegation wrappers that check for a local binary with `which` and then pipe a task into `claude -p`, `codex exec` or `cursor-agent`; `suggest-agent-rules` is a session-history analyser with three bundled shell tools; `google-calendar` and `perplexity-search` are real API clients with their own scripts; and the two review skills are long prose-rubric documents backed by reference files. There is no license file in the checkout, which matters more than the install count for anyone planning to redistribute a copy.

## Installation

The README documents one route, the Claude Code plugin marketplace, and it names four of the six registered plugins:

```text
/plugin marketplace add dotneet/claude-code-marketplace
/plugin install review-tool@dotneet-marketplace
/plugin install agent-call@dotneet-marketplace
/plugin install agent-session@dotneet-marketplace
/plugin install research@dotneet-marketplace
```

The two remaining plugins, `google` and `prompt`, are registered in `.claude-plugin/marketplace.json` but have no install line in the README. Confirm the name in that file before running a command of the same shape, `/plugin install google@dotneet-marketplace` or `/plugin install prompt@dotneet-marketplace`, because this guide follows the catalog rather than a documented command there.

There is no skills CLI path anywhere in the README or in the ten `SKILL.md` files: no `npx skills add`, no install section per skill, and no Hermes target among the hosts the repository knows about. The durable route for this profile is a directory copy out of a clone:

```bash
cp -R review-tool/skills/typescript-react-reviewer ~/.hermes/profiles/corpusiq/skills/typescript-react-reviewer
cp -R prompt/skills/prompt-improver ~/.hermes/profiles/corpusiq/skills/prompt-improver
```

Copy the whole directory rather than the markdown. `typescript-react-reviewer` ships `references/antipatterns.md`, `references/checklist.md` and `references/react19-patterns.md` next to its `SKILL.md`, `prompt-improver` ships `references/claude.md` and `references/codex.md`, `code-modularization-evaluator` ships three reference files, `perplexity-search` ships `scripts/perplexity_api.py` plus a reference, `google-calendar` ships `scripts/` with two Python clients and a requirements file, and `suggest-agent-rules` ships `tools/` with three shell analysers. A lone `SKILL.md` leaves the agent citing a rubric it cannot open or running a script that is not there.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| typescript-react-reviewer | 8,966 | Reviewing TypeScript and React 19 code and PRs against a three-level rubric: critical block-merge issues (derived state in `useEffect`, missing cleanup, direct state mutation, `key={index}`, `useFormStatus` beside its form, a Promise created in render with `use()`), high-priority problems (dependency arrays, `any` props, missing Error Boundaries) and architecture notes, with reference files for antipatterns, a checklist and React 19 patterns. |
| prompt-improver | 512 | Rewriting a prompt or an agent-instruction document into a verifiable one: classifies task type, complexity and risk, scores eight dimensions (verifiability, specificity, context, scope, outcome, constraints, context economy, execution preference), detects anti-patterns such as vague instructions and missing verification commands, then returns a fixed output format with issues, missing questions, a verification plan and the improved prompt, applying the extra Claude and Codex techniques in its reference files. |

The remaining 8 indexed listings range from 402 to 460 installs.

## Why This Matters for Hermes Agents

The React reviewer is the part worth the install. It is not a style guide: it carries a merge-blocking tier that names the React 19 traps an agent gets wrong most often, including `useFormStatus` in the same component as the form and a Promise created during render with `use()`, and it points at three reference files that a reviewer pass can actually open. For a profile that reviews generated frontend code, that is a usable rubric rather than an opinion.

`prompt-improver` is the second useful piece, and its target is wider than the name suggests. The skill treats an instruction document, a plan file or an `AGENTS.md` as an improvement target, reports what is missing, and returns a revised draft, which makes it a reviewer for the very file that governs an agent's behaviour. Its output contract is fixed, so the result can be diffed across runs instead of drifting.

The delegation trio is the least portable part. Each of the three is roughly thirty lines: check for the binary, then pipe a heredoc at it, with a note to raise the Bash tool timeout because the task may take a long time. That is a clean illustration of the hand-off pattern and a poor thing to drop into an unattended profile, since the flags involved are `--dangerously-skip-permissions` for Claude and `--sandbox danger-full-access` for Codex.

Everything else is a thin client: Context7 and Perplexity over their APIs, Google Calendar and Tasks over OAuth, and a session-log analyser that reads `~/.claude/projects` or `~/.codex/sessions`. Read each `SKILL.md` before you rely on it, because the quality of the ten files varies far more than the install counts suggest.

## Usage

| You say | What happens |
|---|---|
| "Review this PR for React 19 problems" | `typescript-react-reviewer` works the priority tiers in order, flags derived state in `useEffect`, missing cleanup, direct state mutation and `key={index}` in dynamic lists as block-merge issues, then reads `references/react19-patterns.md` for hook-specific guidance before writing the review. |
| "Improve this prompt: add tests for foo.py" | `prompt-improver` classifies the task, lists the anti-patterns it found (no verification command, ambiguous deliverable, missing file paths), asks the questions that would make the prompt workable, and returns an improved prompt with a concrete command to run. |
| "Is this module too coupled to that service?" | `code-modularization-evaluator` scores the coupling on integration strength (intrusive, functional, model, contract), distance and volatility, identifies the connascence type, and returns refactoring options rather than a score. |
| "Look up how Next.js App Router middleware works now" | `context7` resolves the library ID through the Context7 API, fetches version-specific documentation for the query, and answers with code examples and documentation URLs, provided `CONTEXT7_API_KEY` is set. |
| "Research what changed in the React 19 release" | `perplexity-search` picks one of four modes (ask, research, reason, search) and runs `scripts/perplexity_api.py` against the matching sonar model, then presents results with sources; it needs `PERPLEXITY_API_KEY`. |
| "What is on my calendar Thursday and which tasks are due?" | `google-calendar` drives the bundled `gcal` client: list events in an RFC3339 window, then list tasks from a task list, using the token at `~/.config/google-calendar/token.json` or an alternate account passed with `--token`. |
| "What rules should this repo's agent follow?" | `suggest-agent-rules` runs `tools/list-sessions.sh` and `tools/extract-patterns.sh` over the project's Claude Code or Codex session logs, combines repeated corrections with the repository's README, CI and test layout, and proposes verifiable agent rules. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} reviewer\n" \
  https://raw.githubusercontent.com/dotneet/claude-code-marketplace/main/review-tool/skills/typescript-react-reviewer/SKILL.md
curl -sL -o /dev/null -w "%{http_code} improver\n" \
  https://raw.githubusercontent.com/dotneet/claude-code-marketplace/main/prompt/skills/prompt-improver/SKILL.md
```

Expect `200` twice. Read one before installing: the reviewer's frontmatter description is the routing contract, listing the trigger phrases (code review requests, PR reviews, React architecture evaluation, code smells, type-safety checks, `useEffect` abuse), and a copy with a trimmed description stops being selected for the requests it was written for.

After a copy lands in the profile, confirm the frontmatter and the shape of the directory:

```bash
head -3 ~/.hermes/profiles/corpusiq/skills/typescript-react-reviewer/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/prompt-improver/
```

A good copy shows `name:` and `description:` in the first three lines, and the directory listing shows `SKILL.md`, `README.md` and `references/` for `prompt-improver`, with `claude.md` and `codex.md` inside `references/`. The same listing for `typescript-react-reviewer` should show `SKILL.md` and three files under `references/`; if the references are missing, the skill can still describe its rubric but cannot read the patterns it points at.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| typescript-react-reviewer | Pass | Pass | Pass |
| prompt-improver | Pass | Pass | Pass |
| code-modularization-evaluator | Pass | Pass | Pass |
| perplexity-search | Pass | Pass | Warn |
| call-claude | Fail | Pass | Warn |

One FAIL appears in the sampled five, on `call-claude`, and the pack records the verdict rather than the finding behind it, so read that entry on skills.sh before installing `agent-call`. The skill itself explains the verdict: it shells out with `claude -p --dangerously-skip-permissions`, which hands a task to another agent with permission prompts disabled, and its Codex sibling uses `codex exec --sandbox danger-full-access` and its Cursor sibling defaults to `--model=composer-1`. Those are deliberate design choices for an interactive developer and a poor default for a cron or a subagent that runs without a person watching.

The rest of the write surface is small and credential-bearing rather than destructive. `google-calendar` reads and writes calendar events and tasks through an OAuth client whose credentials sit at `~/.config/google-calendar/credentials.json` and whose token sits beside it, `perplexity-search` bills against `PERPLEXITY_API_KEY`, `context7` sends `CONTEXT7_API_KEY` as a bearer header, and `suggest-agent-rules` reads full session transcripts from `~/.claude/projects` or `~/.codex/sessions`, which can contain anything that was ever pasted into a prompt. Keep the keys in the environment rather than in the prompt, and point the session analyser at one project at a time.

## Limitations

- Snapshot data, verified 2026-10-30: 12,917 combined installs across 10 indexed listings; 3 GitHub stars; no license file (GitHub API reports None); last pushed 2026-01-23. Counts drift over time.
- There is no license file in the repository and the GitHub API returns no license, so no permission is granted by default. Redistributing a copy, vendoring it into a product or publishing a modified version needs the author's permission first; treat this as all rights reserved until you have it.
- The catalog and the README disagree on the size of the suite. `.claude-plugin/marketplace.json` registers six plugins and `CLAUDE.md` lists five, while the README's plugin table and its install block name four; `google-calendar` and `prompt-improver` appear only in the manifest and the maintainer notes, so their install command is inferred from the documented pattern rather than quoted.
- There is no skills CLI install path: no `npx skills add` in the README, no install section in any of the ten `SKILL.md` files, and no generated Hermes adapter. Outside Claude Code the only route is a directory copy, which also means updates are a re-copy rather than an upgrade command.
- Six of the ten skills are inert without a live dependency: `perplexity-search` needs `PERPLEXITY_API_KEY`, `context7` needs `CONTEXT7_API_KEY`, `google-calendar` needs a Google Cloud OAuth desktop client, and the three `call-*` skills need `claude`, `codex` or `cursor-agent` on `PATH`. The skills check for the missing piece and stop, so a failed install usually looks like a skill that declines to act.
- Install counts do not rank these skills. `typescript-react-reviewer` alone accounts for 8,966 of the 12,917 combined installs, and the other nine sit between 402 and 512, which is closer to publication noise than adoption signal. One more wrinkle: `suggest-agent-rules` is written in Japanese while the other nine skills are in English, so its instructions need translation or a bilingual reader before you rely on its output format.

## Related

- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup)
- [Subagent-Driven Development - Multi-Agent Task Dispatch Setup](/hermes/skills/catalog/subagent-driven-development-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy whole directories. Seven of the ten skills carry `references/`, `scripts/` or `tools/` next to `SKILL.md`, and the review rubric is useless without the three reference files it keeps pointing at.
- Install `typescript-react-reviewer` on its own first. It is the only skill here with a large install base, and pairing it with a real PR review tells you more than installing all ten and guessing which one fired.
- Point `prompt-improver` at your own `AGENTS.md` before pointing it at a user request. The skill treats an instruction document as an improvement target and returns a revised draft, which is the cheapest audit of an agent's operating rules you will get from this repository.
- Do not install `agent-call` into any profile that runs unattended. The three skills invoke other agents with permission prompts or sandboxing disabled, so either keep them out of cron jobs and subagents or replace the flags with your own wrapper.
- Read `references/react19-patterns.md` before trusting a Review pass on React 19 code. The merge-blocking list is React 19 specific (`use`, `useActionState`, `useOptimistic`, `useFormStatus`), and a model working from older training data will miss exactly those cases unless the reference is in context.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
