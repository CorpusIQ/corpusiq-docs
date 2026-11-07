---
title: "PUA Skill - Drive and Pushback for Agents"
description: "tanweai/pua on skills.sh: 19.2K combined installs; a high-agency persona that forces root-cause debugging, evidence and pushback over partial answers."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pua-agent-drive-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "agent behaviour", "debugging", "high agency"]
---

# PUA Skill - Setup Guide

**Source:** [tanweai/pua](https://www.skills.sh/tanweai/pua) via skills.sh - 19.2K combined installs across 34 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 19,812 stars, no licence file in the repo root, last pushed 2026-09-09, 46 SKILL.md directories in per-runtime trees (skills/, hermes/, codex/, kimi/, chatgpt/, codebuddy/, .trae/skills/, pi/package/skills/)
**Category:** Agent behaviour for agents: a review persona that forces root-cause work, evidence and pushback instead of partial answers
**Quality Tier:** 🟡 Review - clean scanner verdicts across every sampled skill and a very large star count, held back by having no licence file and by a README that mixes an unproven productivity claim into the methodology.

This is a behaviour skill, not a capability skill. It does not add tools or endpoints; it adds a persona and a set of rules for what the agent is allowed to do when a task is failing. The framing is corporate performance management: the Chinese edition uses big-tech performance-review rhetoric, the English edition uses a Performance Improvement Plan, and both sit on top of the same three mechanisms the README names: rhetoric that makes giving up feel expensive, a debugging methodology that makes giving up unnecessary, and a proactivity rule that replaces waiting with searching.

The trigger design is the part worth respecting. Every skill in the set carries an explicit list of conditions: a task that has failed twice or more, the same approach being tweaked repeatedly, an imminent "I cannot", a suggestion that the user do it manually, a claim that the environment is at fault without verification, passive waiting, or visible user frustration. The frontmatter also states the negative case, that normal first-attempt work and a known fix mid-flight are not triggers. A persona that fires on everything is a tax; this one is designed to stay quiet.

The repository supports a wide runtime list (Claude Code, Codex CLI, Cursor, Kiro, CodeBuddy, OpenClaw, Antigravity, OpenCode, pi, Trae, VSCode Copilot) and, unusually for this catalog, ships a `hermes/` tree with `pua`, `pua-en` and `pua-ja` ready to copy into a Hermes profile.

## Installation

The general route is the skills CLI, and the English edition is the one the English README installs:

```bash
npx skills add tanweai/pua --skill pua-en
```

The README adds that a session which does not pick the skill up immediately needs a restart of the AI tool. For Claude Code there is a plugin route:

```bash
claude plugin marketplace add tanweai/pua
claude plugin install pua@pua-skills
```

Updating through the plugin needs the marketplace cache refreshed first, or you get the cached version:

```bash
claude plugin marketplace update
claude plugin update pua@pua-skills
```

For Hermes, skip the CLI entirely. The repository carries the runtime tree already:

```bash
git clone https://github.com/tanweai/pua /tmp/pua
cp -r /tmp/pua/hermes/pua-en ~/.hermes/profiles/<profile>/skills/
```

That copies the English skill into the profile's skills directory as `pua-en`, where Hermes discovers it at session start. The Chinese edition is `hermes/pua`, and Japanese is `hermes/pua-ja`.

Other runtimes have their own trees in the same checkout. Trae installs with an explicit agent flag:

```bash
npx skills add tanweai/pua --skill pua-trae -a trae -y
```

`pua-trae` is instruction-only by design, with no hooks and no agents, so it behaves the same way in a runtime that has no hook API. The `codex/` tree is the largest of the mirrors and holds the sub-command variants (`pua-on`, `pua-off`, `pua-loop`, `pua-kpi`, `pua-team-status`, `pua-teardown-all`, `pua-survey`, `pua-reap-orphans`), which the README documents through the Codex install guide rather than in the main body.

## What It Provides

Thirty-four indexed listings, thirteen of them above the threshold:

| Skill | Installs | Use For |
|---|---|---|
| pua-en | 2,929 | The English PIP persona: forces exhaustive problem solving with Western big-tech performance rhetoric and structured debugging |
| pua-ja | 1,840 | Japanese edition of the same persona and the same evidence rules |
| p9 | 1,823 | P9 tech lead mode: writes task prompts, manages P8 agent teams, and does not write code itself |
| p10 | 1,820 | P10 CTO mode: strategic direction, org topology and management of P9 teams |
| pua-loop | 1,818 | Guided iterative development with recurring checks, completion evidence and explicit pause or abort markers |
| p7 | 1,809 | P7 senior engineer mode: solution-driven execution under supervision, with a three-question self-review before completion |
| yes | 1,756 | The encouragement variant: same evidence-first behaviour, with the narrator supporting instead of pressing |
| shot | 1,732 | Compact all-in-one version of the persona, meant to be injected into a sub-agent or a short session |
| mama | 1,700 | Maternal-nagging coaching register over the same structured troubleshooting rules |
| pua-trae | 1,061 | Trae-optimized edition for npx skills installs, instruction only, no hooks or agents |
| ding | 389 | Ding-style workplace reminder register, drawn from the inside-DingTalk essay genre |
| pua-debugging | 249 | A debugging-only pass; the listing has no matching SKILL.md in the cloned repository tree |
| high-agency | 101 | A high-agency behaviour pass; also listed on skills.sh without a matching SKILL.md in the tree |

The remaining 21 indexed listings range from 1 to 44 installs.

The tail is almost entirely sub-command and variant skills: `loop` (44), the alias set at 8 to 9 installs each (`pua-on`, `pua-off`, `pua-offline`, `pua-p7`, `pua-p9`, `pua-p10`, `pua-pro`, `pua-mama`, `pua-yes`, `pua-kpi`, `pua-flavor`, `pua-cancel-loop`, `pua-survey`, `pua-team-status`, `pua-teardown-all`, `pua-reap-orphans`), the translated debugging editions at 2 to 4, and `sb-leader` at 1. They exist because the plugin exposes sub-commands, and installing them separately is not the intended path.

## Why This Matters for Hermes Agents

The useful idea here is that giving up is a behaviour with a signature, and a signature can be detected. The repository's hooks make that concrete: `failure-detector.sh` runs after Bash tool use, and its own comment states the rule precisely. A non-zero exit status is a confirmed tool observation, never task acceptance, never task failure, and never a reason to infer the model's reasoning. Successful tools stay silent and do not reset the pressure state, because an `ls` is not proof the user's task is finished.

That distinction matters more than the rhetoric. Agents fail softly: they run a command, see success, and report the job done without checking the actual artifact. A rule that says a successful tool call is not evidence of completion is exactly the correction, and it is the same rule this catalog applies to its own work.

The level skills turn the persona into an orchestration model. `p7`, `p9` and `p10` are not motivational registers; they are an explicit hierarchy. P9 writes task prompts and manages P8 agents without writing code, P10 sets direction and org topology, P7 executes under supervision and self-reviews before claiming completion. For a Hermes setup that spawns sub-agents, that is a ready-made division of responsibility with a written contract for what each level may do.

The variant skills are cheaper than they look. `shot` exists to be injected into a sub-agent that gets no hooks and no context, which is the realistic constraint when you delegate. `pua-trae` is instruction-only, so it works where hooks do not. Choosing the variant that matches your runtime is the whole installation decision.

The caveats are the honest part, and the README states them itself: not all models passed the compatibility evaluation, and a productivity increase was not established by it. This is a well-engineered prompt, not a measured intervention.

## Usage

| You say | What happens |
|---|---|
| "Third failure on this test. Stop guessing." | The failure threshold is met, the persona escalates to the hard pass and the seven-point checklist runs before any further edit |
| "Do not tell me to do it manually, find the actual cause" | Manual workarounds are refused and the agent has to read logs, source and configuration until it can name a cause |
| "You have not verified anything, prove it works" | Completion requires evidence: a run, an exit code, a read-back, not a description of what should happen |
| "Put yourself on a PIP for this task" | The PIP framing is applied deliberately to a single task rather than left on as a permanent tone |
| "Coordinate these four agents on the migration" | P9 mode writes the task prompts and manages the team, and does not write the code itself |
| "Switch to the encouraging register" | The yes variant keeps the evidence rules and changes only the narrator |
| "Turn this off for the rest of the session" | The off variant disables the persona so a normal task does not carry the pressure overhead |

## Verification

Read the exact skill you intend to install. Both paths returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/tanweai/pua/main/skills/pua-en/SKILL.md | head -12
curl -fsSL https://raw.githubusercontent.com/tanweai/pua/main/hermes/pua-en/SKILL.md | head -12
```

The frontmatter should name `pua-en`, carry the four trigger conditions and the negative case, and the body should open with the PIP framing rather than with setup instructions.

After copying into a Hermes profile, confirm the file and the discovery path:

```bash
ls ~/.hermes/profiles/<profile>/skills/pua-en/SKILL.md
head -4 ~/.hermes/profiles/<profile>/skills/pua-en/SKILL.md
```

Hermes reads skills from the profile's `skills/` directory at session start, so the file has to be in place before the session begins. If you copied it mid-session, start a new one rather than assuming it loaded.

Then test the trigger rather than the prose. Ask for something that has already failed twice and watch whether the agent changes method. A skill that produces the rhetoric but not the checklist has been installed and not adopted.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pua-en | Pass | Pass | Pass |
| mama | Pass | Pass | Pass |
| pua-yes | Pass | Pass | Pass |
| pua-p10 | Pass | Pass | Pass |
| sb-leader | Pass | Pass | Pass |

Five sampled skills, five clean verdicts on all three scanners, which is the best security picture in this batch. The content is instruction markdown plus shell hooks, and the hooks file states that all hooks are local-only with no telemetry and no network requests, which matches what the scripts do: read the hook payload, read or write a local state file, print a reminder.

The hooks are still the surface to read. They run on `UserPromptSubmit`, `PostToolUse`, `PostToolUseFailure` and `PreCompact`, they invoke bash scripts with a five-second timeout, and `runtime-state.py` keeps state between turns. That is modest and local, and it is also code that executes on every prompt, so read the four scripts before enabling the plugin.

There are lifecycle commands in the Codex tree named for tearing down teams and reaping orphans (`pua-teardown-all`, `pua-reap-orphans`, `pua-survey`). If you run a multi-agent setup, know what they target before any agent is allowed to call them, because a teardown aimed at the wrong runtime state ends work that was not yours to end.

The licensing is the real gap. There is no LICENSE file in the repository root. The `pua-en` frontmatter and `plugin.json` both declare MIT, so the intent is clear, but a declaration inside a file is weaker than a licence text, and redistribution inside a product is the case where that difference matters.

The remaining consideration is tone. The persona is designed to make the model argue with itself, and the same register can leak into messages written for humans. If the agent drafts customer-facing prose, keep this persona out of that session or scope it to the debugging task.

## Limitations

- Snapshot data, verified 2026-11-06: 19,212 combined installs across 34 indexed listings; 19,812 GitHub stars; no licence file in the repo root; last pushed 2026-09-09. Counts drift over time.
- The productivity claim is unproven by the project's own account. The README states that not all models passed its compatibility evaluation and that a productivity increase has not been established by it.
- Two listings, `pua-debugging` and `high-agency`, have no matching SKILL.md in the cloned tree, so their content cannot be read before install from the repository alone.
- The English documentation is a translation of a Chinese-first project. Some of the register is culturally specific, and the Ding-style skill in particular assumes familiarity with Chinese workplace writing.
- Twenty-one of the 34 listings are sub-command variants at 44 installs or fewer. Installing them individually is not the intended path, and their counts say nothing about adoption.
- It is a tone, not a gate. Nothing here blocks a merge or fails a build; the persona changes what the agent does next, and a model that ignores instructions will ignore this one too.

## Related

- [Superpowers - Agentic Skills Framework & Development](/hermes/skills/catalog/superpowers-setup)
- [Context Engineering Kit - Prompt and MCP Setup](/hermes/skills/catalog/context-engineering-kit-setup)
- [Multi-Agent Review - Adversarial Code Review Setup](/hermes/skills/catalog/multi-agent-review-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `shot` into sub-agents and the full skill into the parent. Delegated agents rarely get hooks, and the compact version is the one that survives that constraint.
- Keep the negative case in view. If the persona fires on first attempts, the session gets slower and louder for no gain, and the fix is to name the task as normal rather than to argue with the model.
- Scope it to debugging sessions. A permanent performance-review register is exhausting in a research or writing session and it does not improve either.
- When you use P9 or P10 mode, require the task prompts as an artifact. The level skills are only useful if the decomposition is written down where the sub-agents can read it.
- Read `failure-detector.sh` before trusting the escalation. Its rule that a zero exit status is not completion evidence is the most transferable idea in the repository, and it is worth copying into your own agent instructions even if you never install the skill.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
