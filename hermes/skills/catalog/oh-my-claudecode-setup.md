---
title: "Oh My ClaudeCode - Agent Workflow Suite Setup"
description: "yeachan-heo/oh-my-claudecode on skills.sh: 36.5K combined installs across 98 listings; planning, delegation and review skills for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/oh-my-claudecode-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "orchestration", "multi-agent"]
---

# Oh My ClaudeCode - Setup Guide

**Source:** [yeachan-heo/oh-my-claudecode](https://www.skills.sh/yeachan-heo/oh-my-claudecode) via skills.sh - 36.5K combined installs across 98 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 40,550 stars, MIT, last pushed 2026-11-03, 48 SKILL.md directories
**Category:** Agent orchestration: planning, parallel delegation, review, debugging and delivery skills for coding agents
**Quality Tier:** 🟡 Yellow: all five sampled skills pass Socket and Snyk, but ask-codex draws a Warn from Gen Agent Trust Hub

oh-my-claudecode (OmC) is a multi-agent orchestration layer for Claude Code, described in its README as "multi-agent orchestration for Claude Code. Zero learning curve." The repo ships 48 SKILL.md directories under skills/, while skills.sh indexes 98 listings for the same source, so the catalog is wider than the tree.

The suite is built around workflow verbs rather than reference material: plan, build, verify, release, cancel. Setup is done once through the plugin marketplace, and most daily use is a single command that expands into a delegated work loop.

## Installation

The documented path is the Claude Code plugin marketplace. Enter these one at a time, because pasting both lines at once fails:

```bash
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
```

```bash
/plugin install oh-my-claud
```

If you only want individual skills inside Hermes, clone the repo and copy the directories you need out of skills/ into your Hermes skills directory, then load them by directory name:

```bash
git clone https://github.com/Yeachan-Heo/oh-my-claudecode
```

Run the setup skill first if you want the suite configured for you rather than by hand:

```bash
cat skills/omc-setup/SKILL.md
```

## What It Provides

Twenty of the 98 indexed listings clear 795 installs. The table below reports every one of them at its exact count.

| Skill | Installs | Use For |
|---|---|---|
| ai-slop-cleaner | 1,618 | Stripping AI-sounding prose and filler from generated text |
| ralplan | 1,223 | Plan-first workflow before any edit |
| hud | 1,173 | Status display for a running session |
| deepinit | 1,058 | Deep project initialisation pass |
| autopilot | 1,039 | Unattended execution loop |
| deep-interview | 1,037 | Structured requirements interviewing |
| omc-setup | 1,026 | Installing and configuring the suite |
| ralph | 1,009 | Iterative build loop from a written spec |
| visual-verdict | 931 | Visual check of rendered output; not in the pack's visible tree sample |
| team | 916 | Parallel team-of-agents delegation |
| ultraqa | 902 | Extended QA sweep; not in the pack's visible tree sample |
| project-session-manager | 894 | Session state held across a project |
| cancel | 888 | Stopping a running workflow |
| omc-doctor | 869 | Diagnosing a broken install |
| skill | 865 | Creating and loading skills |
| release | 860 | Release preparation |
| external-context | 818 | Pulling outside context into the task |
| trace | 817 | Tracing execution paths |
| configure-notifications | 809 | Notification channel setup |
| omc-plan | 795 | Plan mode entry; not in the pack's visible tree sample |

The remaining 78 indexed listings range from 3 to 765 installs.

## Why This Matters for Hermes Agents

Hermes agents are good at single-turn tool calls and weak at long multi-step delivery unless something forces a plan, a check and a hand-off. OmC packages exactly that structure as prompt-level skills, so a Hermes builder can lift the workflow shape without adopting the Claude Code runtime.

The two most portable pieces are ralplan, which makes the agent write a plan before touching files, and ultraqa or verify, which forces a review pass before the agent claims success. Both map cleanly onto a Hermes loop that has a planning step and a verification step.

The ai-slop-cleaner skill is useful outside coding: it is a documented pass for removing filler and templated phrasing, which is the same problem public-facing copy has.

The team and ultrapilot skills show how the project splits work across parallel agents and merges results, which is a reasonable reference for anyone writing their own delegation prompts.

Treat the plugin install instructions as Claude Code specific. In Hermes you are copying prompt documents, not installing a runtime, and the cancel-* companions exist because those loops need an explicit stop.

## Usage

| You say | What happens |
|---|---|
| "Plan this refactor before you touch anything" | ralplan produces a written plan and holds edits until the plan is agreed |
| "Run the build loop until the tests pass" | ralph iterates against the spec, then reports the remaining failures |
| "Clean the AI tone out of this page" | ai-slop-cleaner rewrites filler and templated phrasing |
| "Interview me about the requirements first" | deep-interview asks the questions that change the design |
| "Have a team of agents review this module" | team splits the review across roles and consolidates findings |
| "Why is the install broken?" | omc-doctor checks configuration and reports what is missing |
| "Stop the running workflow" | cancel halts the active loop and returns control |

## Verification

Confirm the install location and the directory count first:

```bash
ls ~/.claude/skills | wc -l
```

Then read one raw skill file to confirm the content is what skills.sh indexed. This URL is built from the skills/omc-setup/SKILL.md path in the repo tree, on branch main:

```bash
curl -fsSL https://raw.githubusercontent.com/yeachan-heo/oh-my-claudecode/main/skills/omc-setup/SKILL.md | head -30
```

If the fetch returns frontmatter with a name and a description, the source is live and the guide's counts can be re-checked on the skills.sh page.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ai-slop-cleaner | Pass | Pass | Pass |
| skillify | Pass | Pass | Pass |
| minimal-prose-discipline | Pass | Pass | Pass |
| review | Pass | Pass | Pass |
| ask-codex | Warn | Pass | Pass |

## Limitations

- Snapshot data, verified November 3, 2026: 36,471 combined installs across 98 indexed listings; 40,550 GitHub stars; MIT; last pushed 2026-11-03. Counts drift over time.
- The documented install path is the Claude Code plugin marketplace. No Hermes installer is described in the pack, so copying directories by hand is the practical route.
- 98 indexed listings against 48 SKILL.md directories means the catalog and the tree do not map one to one; some listings have no directory in the visible tree sample.
- ask-codex carries a Gen Agent Trust Hub Warn, and several skills emit shell commands, so read a skill before letting it run.
- Install counts are dominated by workflow verbs and a prose cleaner. They say little about the quality of the cancel-* and configure-* companions at the bottom of the list.
- The republished documentation site and CLI reference are external, so version drift between the README and the skills is possible.

## Related

- [ClaudeKit Skills - Full Stack Agent Toolkit](/hermes/skills/catalog/claudekit-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Composio - Awesome Claude Skills (28-Skill Suite)](/hermes/skills/catalog/composiohq-awesome-claude-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install omc-setup first and let it write the configuration; hand-editing the plugin files is the common source of a broken install.
- Pair ralplan with verify. The plan alone does not stop an agent from declaring success early.
- Skip the cancel-* companions until you actually run long loops, then add the one you need so the agent has a stop word.
- Use ai-slop-cleaner as a final pass on any public copy generated inside the workflow, not as a first draft step.
- Check the skills directory count against the 48 in this guide after an upgrade, since listings get added faster than directories.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
