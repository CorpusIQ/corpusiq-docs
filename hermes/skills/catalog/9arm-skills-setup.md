---
title: "9arm Skills - Thai Dev Agent Suite"
description: "thananon/9arm-skills: 24.4K combined installs. Six practitioner skills for debugging, post-mortems, review, management posts and long-task control."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/9arm-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "debugging", "code review", "engineering workflow"]
---

# 9arm Skills - Setup Guide

**Source:** [thananon/9arm-skills](https://www.skills.sh/thananon/9arm-skills) via skills.sh - 24.4K combined installs across 6 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [thananon/9arm-skills](https://github.com/thananon/9arm-skills) - 3,244 stars, no LICENSE file, branch main, last pushed 2026-06-14; 6 `SKILL.md` files, four under `skills/engineering/` and two under `skills/productivity/`, each directory holding only its `SKILL.md`

**Category:** General software engineering skills from a practitioner portfolio: planning, review and delivery

**Quality Tier:** 🟡 Yellow - `qwen-agent` is flagged by all three scanners (Gen Agent Trust Hub, Socket and Snyk), `management-talk` carries a Snyk warn, and the repository ships no LICENSE file

This is one practitioner's working kit rather than a product. The README opens with a single line, "Agent skills loaded by Claude Code", and the six skills inside are the ones its author uses daily: a debugging discipline, a post-mortem template, an outsider review, a management translation layer, a long-task watchdog, and a delegation wrapper that pushes menial work to a cheap model. Nothing here is a framework and nothing claims to be complete.

The bucket layout says as much. Skills live under `skills/` in named buckets, and the README distinguishes the shippable ones from the personal, in-progress and deprecated folders that are not promoted. Today only `engineering/` and `productivity/` carry skills, `misc/` is empty, and the repository's own `CLAUDE.md` requires every shippable skill to have both a README entry and an entry in `.claude-plugin/plugin.json`, which is why the six listings line up exactly with the six directories in the tree.

## Installation

The README's recommended route works across agents through the skills CLI:

```bash
npx skills add thananon/9arm-skills
```

The alternative is the author's own dev loop, which symlinks every shippable skill into `~/.claude/skills/`:

```bash
./scripts/link-skills.sh
```

The same folder also ships `scripts/list-skills.sh`, which prints every `SKILL.md` in the repository and is the quickest way to see what a clone actually contains. Both scripts assume Claude Code paths, so neither is the right route for a Hermes profile. The directory copy is, and it has to handle the bucket folders because the skills are one level deeper than the usual layout:

```bash
git clone --depth 1 https://github.com/thananon/9arm-skills.git /tmp/9arm-skills
cp -r /tmp/9arm-skills/skills/engineering/. ~/.hermes/profiles/corpusiq/skills/
cp -r /tmp/9arm-skills/skills/productivity/. ~/.hermes/profiles/corpusiq/skills/
```

The copy flattens `engineering/` and `productivity/` into one directory, which is harmless here because the buckets are organisational rather than functional, and no skill references another by bucket path. `qwen-agent` needs something extra: it drives the `claude-9arm` command, a shell alias that runs `claude` against a Qwen model through the author's own gateway. Without that command the skill can describe the delegation but not perform it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| scrutinize | 5,233 | An outsider review of a plan, PR, diff or design doc: questions whether the change should exist, traces the real code path rather than the diff, and verifies the change does what it claims, with every call carrying its rationale. |
| debug-mantra | 4,912 | A four-step debugging discipline (reproduce, trace the fail path, falsify the hypothesis, cross-reference every breadcrumb), recited at the start of a debugging session and applied in order before any fix. |
| post-mortem | 4,719 | Writing the canonical engineering record of a fixed bug: root cause, mechanism, fix, validation and how it slipped through, and it refuses to draft without a reliable repro, a known cause and a validated fix. |
| management-talk | 4,649 | Rewriting engineer-to-engineer content for engineering leadership and shaping it for the channel, whether that is a JIRA comment, a Slack post, an async standup line, an email or meeting talking-points. |
| qwenchance | 2,472 | Keeping a long task on track: breaking out of looping thinking, bounding internal reasoning, watching the context budget and triggering a clean handoff before the window fills. |
| qwen-agent | 2,434 | Delegating menial, well-scoped coding work (bulk renames, formatting, boilerplate, log condensing, test scaffolding) to a Qwen-backed subagent through the `claude-9arm` command instead of spending the main model's budget. |

All 6 indexed listings appear in the table above; none of them falls below the threshold.

## Why This Matters for Hermes Agents

Most skill packs here add domain knowledge. This one adds discipline at the points where agent sessions actually fail: debugging without a method, closing a bug without a record, reviewing a diff without standing outside it, and running a long task until the context window collapses. Each skill is written as an operating stance with triggers, not as a summary of best practice.

`debug-mantra` is the clearest example. It instructs the agent to recite a four-line mantra at the start of any debugging session and then apply the steps in order before proposing a fix, which is a cheap intervention against the most common failure mode in coding agents: jumping to a plausible fix for a symptom nobody traced.

`post-mortem` composes with it deliberately. The README and the skill body both say the finished post-mortem can be handed to `management-talk` for the leadership version, which means the engineering truth and the executive summary stay separate artifacts instead of one blurred document. That pairing is rare in this catalogue and it is the reason the pack is worth installing whole.

`qwenchance` addresses the failure that costs the most money. It watches for repeated steps, re-reads of the same file, circular second-guessing and context exhaustion, and it triggers a handoff instead of waiting for the window to fill. For any profile running scheduled multi-step work, that is a guardrail rather than a convenience.

## Usage

| You say | What happens |
|---|---|
| "This endpoint returns 500 for one customer, find it" | `debug-mantra` recites the mantra, reproduces the failure, traces the fail path, falsifies its first hypothesis and cross-references the logs before touching code. |
| "Write up the root cause for the bug we just fixed" | `post-mortem` checks that there is a repro, a known cause and a validated fix, then writes the engineering record in that order. |
| "Review this PR before I merge it" | `scrutinize` asks whether the change should exist at all, reads the code path instead of the diff, and reports concise findings with rationale. |
| "Turn this into a status update for my VP" | `management-talk` rewrites the engineering content for a leadership audience and formats it for the channel you name. |
| "You are going in circles, reset" | `qwenchance` breaks the loop, bounds the reasoning, and proposes a handoff summary that captures what is settled. |
| "Rename this across the repo, it is mechanical" | `qwen-agent` scopes the task and hands it to the Qwen-backed subagent through `claude-9arm`, keeping the main conversation for judgement work. |
| "Close this bug out properly" | `post-mortem` writes the record, then `management-talk` produces the leadership summary from it. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} scrutinize\n" \
  https://raw.githubusercontent.com/thananon/9arm-skills/main/skills/engineering/scrutinize/SKILL.md
```

Expect `200`. The nested path matters: there is no `skills/scrutinize/SKILL.md`, so a URL built from the skill name alone will 404. After the copy lands, confirm the six skills and their frontmatter:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/{scrutinize,debug-mantra,post-mortem,management-talk,qwenchance,qwen-agent}/ | wc -l
head -4 ~/.hermes/profiles/corpusiq/skills/scrutinize/SKILL.md
```

The count should print 6 and the header should show `name: scrutinize` with a description that names the review trigger. If the count is short, the copy of one of the two bucket folders did not land.

## Security

Two of the five sampled skills carry warns, and one of them is flagged everywhere: `qwen-agent` is warned by Gen Agent Trust Hub, Socket and Snyk, and `management-talk` carries a Snyk warn. `scrutinize`, `debug-mantra` and `qwenchance` are clean across all three scanners.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| scrutinize | Pass | Pass | Pass |
| debug-mantra | Pass | Pass | Pass |
| management-talk | Pass | Pass | Warn |
| qwenchance | Pass | Pass | Pass |
| qwen-agent | Warn | Warn | Warn |

The file surface is as small as it gets: six `SKILL.md` files, one per directory, with no bundled scripts, references or assets. The repository carries two shell scripts, `link-skills.sh` and `list-skills.sh`, and only the first changes anything, since it creates symlinks into `~/.claude/skills`. If you use it, read the header first, because it refuses to run when the destination is already a symlink into the repository and will otherwise write into your home directory rather than the profile.

The real caveat is licensing rather than code. There is no LICENSE file anywhere in the repository, so the terms for reusing these skills are unstated, and the sensible default is to install them for personal use in one profile rather than to redistribute or vendor them into anything published.

`qwen-agent` also deserves a second look before deployment. It is the only skill that shells out to an external command, and that command routes prompts through a third-party gateway to a Qwen model, so anything delegated left the local conversation. Keep secrets out of delegation requests and reserve the skill for mechanical work on code already in the repository.

## Limitations

- Snapshot data, verified 2026-10-31: 24,419 combined installs across 6 indexed listings; 3,244 GitHub stars; no LICENSE file; last pushed 2026-06-14. Counts drift over time.
- There is no LICENSE file in the repository, and the README says nothing about terms, so redistribution is unresolved. Install into a profile for use, and treat copying the skill text into published material as a licensing question.
- `qwen-agent` depends on `claude-9arm`, a shell alias that routes `claude` to a Qwen model through the author's own gateway. That alias is not in the repository, so the skill is inert on a profile without it.
- The repository is four months behind the snapshot date, with its last push on 2026-06-14 against a 2026-10-31 install count, so the counts are cumulative figures rather than a signal of recent activity.
- The bucket layout means the copy route has to name `skills/engineering/` and `skills/productivity/` explicitly. A copy of `skills/` alone produces a directory of buckets rather than a directory of skills, and the agent will not find them.
- Coverage is one practitioner's workflow, not a curriculum. There is no Go, Python, TypeScript or infrastructure skill here, so pair it with a language pack rather than expecting it to cover engineering generally.
- `post-mortem` refuses to draft without a reliable repro, a known cause and a validated fix. That is a feature, but it means the skill will push back on the exact moment a team usually wants a write-up.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Asyraf Hussin Skills - Clean Code Suite](/hermes/skills/catalog/asyrafhussin-agent-skills-setup)
- [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all six. The pack is small by design and the value is in the pairings: `debug-mantra` produces the material `post-mortem` needs, and the post-mortem is what `management-talk` rewrites for leadership.
- Keep `qwenchance` in every long-running profile even if you skip the rest. The loop and context-budget checks are cheap to load and they address the failure that wastes the most budget.
- Do not point `qwen-agent` at anything that needs this conversation's context. The skill's own description says so, and its boundary is architecture, design, debugging judgement and security-sensitive edits.
- Run `scripts/list-skills.sh` after a clone instead of trusting the README. The repository is organised in buckets that can hold drafts, and the script is the authoritative list of what ships.
- Treat the missing licence as a signal about scope: read these skills as one engineer's opinionated practice, copy them for your own profile, and do not republish the text.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
