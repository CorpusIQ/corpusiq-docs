---
title: "Khazix Skills - Agent Workflow Toolkit"
description: "kkkkhazix/khazix-skills on skills.sh: 15.1K combined installs across 9 listings; Chinese-language workflow skills for goals, research and writing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/khazix-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "agent workflow", "research", "writing"]
---

# Khazix Skills - Setup Guide

**Source:** [kkkkhazix/khazix-skills](https://www.skills.sh/kkkkhazix/khazix-skills) via skills.sh - 15.1K combined installs across 9 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 21,933 stars, MIT licence, last pushed 2026-11-03, 6 SKILL.md directories at the repository root
**Category:** Agent workflow for builders: planning, research, writing and delivery skills wired for Claude Code and Hermes
**Quality Tier:** 🟡 Yellow: skill-manager and github-to-skills both draw a Gen Agent Trust Hub Fail, storage-analyzer draws Warns from all three scanners, and three of the 9 indexed listings have no directory in the tree

Khazix Skills is the working set of a Chinese AI writer and builder, published as six MIT licensed skills at the repository root. The install index is wider than the tree: it carries 9 listings, while the tree holds 6 SKILL.md directories. The three without a tree counterpart are skill-manager (295 installs), Skill Evolution Manager (289) and github-to-skills (260). The README says the repository maintains the six skills it documents, that it no longer distributes the older skill-manage and self-evolution manager set, and that names from older tutorials should not be read as current install directories.

The six live skills split into three kinds of work. `leader` turns a vague request into a goal brief an agent can run unattended, `neat-freak` closes a task by reconciling documentation and memory with what the code now does, and `hv-analysis` runs a two-axis research report. On the production side, `khazix-writer` writes long-form articles in the author's voice, `aihot` pulls daily AI news without an API key, and `storage-analyzer` analyses disk usage with a tiered cleanup report.

## Installation

The README's own route is conversational: you give the agent a tree URL for the skill you want, and it clones the directory into place. The pattern is the repository URL plus a skill name:

```text
https://github.com/KKKKhazix/khazix-skills/tree/main/<skill-name>
```

Swap the placeholder for a real directory such as `neat-freak`, `hv-analysis` or `khazix-writer`. The README is explicit that you should keep the whole skill directory, including `references/`, `scripts/`, `assets/` and `agents/` where present, because pasting `SKILL.md` alone keeps the method but loses the scripts and resources.

Claude Code can also install all six through the plugin directory:

```text
/plugin marketplace add KKKKhazix/khazix-skills
/plugin install khazix-skills@khazix-skills
```

Updates take two commands, and the README warns against keeping a plugin install and a hand-copied directory of the same skill at once:

```text
/plugin marketplace update khazix-skills
/plugin update khazix-skills@khazix-skills
```

Pinned versions and full download bundles are on the repository's Releases page. For Hermes, clone the six root directories into the profile skills directory and keep `scripts/` intact; three of the skills run local tooling rather than only producing text.

## What It Provides

Six live skills and three indexed listings with no directory in the tree.

| Skill | Installs | Use For |
|---|---|---|
| neat-freak | 3,432 | Closeout that aligns docs, CLAUDE.md and AGENTS.md, agent memory and residue with the code |
| khazix-writer | 3,173 | Long-form article writing in the author's voice, with style rules and a four-layer self-check |
| hv-analysis | 2,929 | Two-axis research: narrative history plus competitor comparison, crossed into a report |
| aihot | 2,552 | Daily AI news, hot events, timelines and keyword search with no API key |
| storage-analyzer | 1,634 | Read-only disk analysis with green, amber and red tiers and an interactive HTML report |
| leader | 536 | Turns one vague sentence into a goal brief with a whitelist, anti-cheat checks and resume points |
| skill-manager | 295 | No directory in the current tree; the index keeps the historical install count |
| Skill Evolution Manager | 289 | No directory in the current tree; the README says the older self-evolution set is no longer distributed |
| github-to-skills | 260 | No directory in the current tree; no replacement skill is documented |

All 9 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Most skill libraries are domain knowledge. This one is workflow, and it aims at the parts of a long session that rot: the goal at the start, the knowledge at the end, the research in the middle and the news feed in the background.

`leader` is the design worth studying. It inspects the codebase before writing anything, asks at most five questions, and produces a brief capped at 4,000 characters with an explicit whitelist, anti-cheat acceptance criteria and resume points, on the reasoning that a long-running agent will take whatever shortcut you left unstated. Copy that structure into any dispatch prompt.

`neat-freak` treats documentation drift as the failure mode rather than an afterthought. After a task it reconciles the README, `docs/`, `CLAUDE.md` and `AGENTS.md`, and the agent's own memory, with what the code now does, then audits whether the project rules were actually followed.

`hv-analysis` is a reusable research shape: one axis follows the subject from origin to now as narrative, the other compares it against contemporaries, and the cross of the two produces the judgement neither axis shows alone. It outputs 10,000 to 30,000 characters and a PDF by default.

`aihot` shows the right pattern for a news skill. The skill only asks and relays, while fetching, ranking and summarising happen on the service side, so it needs no API key and no update when the feed changes.

One caution: `storage-analyzer` can delete files through a local web service. Install it with the tier rules in view.

## Usage

| You say | What happens |
|---|---|
| "Write a goal brief for the agent so it can run this alone" | leader inspects the repo, asks up to five questions and writes a capped goal brief |
| "Run /neat before I close this session" | neat-freak aligns docs, rule files and agent memory with the code and audits rule compliance |
| "Research this company properly" | hv-analysis builds the history axis and the competitor axis, then crosses them into a report |
| "What happened in AI today?" | aihot pulls the daily digest and the current hottest events from aihot.news |
| "My disk is full, what can I delete?" | storage-analyzer scans read-only, tiers the findings and opens an HTML report |
| "Write this material up as a long article" | khazix-writer applies the author's voice rules and runs a four-layer self-check |
| "Install the writing skill" | the agent clones the khazix-writer directory with its references and scripts |

## Verification

Confirm the skills landed in the agent skills directory:

```bash
ls ~/.claude/skills
```

Then fetch one raw file before installing. This path is `neat-freak/SKILL.md` on branch main and returned 200 when this guide was written:

```bash
curl -fsSL https://raw.githubusercontent.com/kkkkhazix/khazix-skills/main/neat-freak/SKILL.md | head -20
```

Frontmatter with a name and a description confirms the listing is backed by a real file. `leader/SKILL.md` is the other path worth checking. The same probe shows the drift: `skill-manager/SKILL.md` and `github-to-skills/SKILL.md` return 404 on branch main, which matches the README's note that the older set is no longer distributed. The install index is at https://www.skills.sh/kkkkhazix/khazix-skills.

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| neat-freak | Pass | Pass | Pass |
| hv-analysis | Warn | Pass | Warn |
| storage-analyzer | Warn | Warn | Warn |
| skill-manager | Fail | Pass | Warn |
| github-to-skills | Fail | Pass | Warn |

`neat-freak` is the only skill in the sample that passes all three scanners, which is worth noting because it is also the one that edits documentation and rule files in your project. Both Fail verdicts land on listings with no directory in the current tree, and `storage-analyzer` carries a Warn from every scanner while shipping a local service that can delete files.

## Limitations

- Snapshot data, verified November 4, 2026: 15,100 combined installs across 9 indexed listings; 21,933 GitHub stars; MIT licence; last pushed 2026-11-03. Counts drift over time.
- The install index outruns the tree: 9 indexed listings against 6 SKILL.md directories. skill-manager (295), Skill Evolution Manager (289) and github-to-skills (260) have no directory on branch main, and the README says the older skill-manage and self-evolution manager set is no longer distributed.
- Two of the nine listings carry a Gen Agent Trust Hub Fail (skill-manager and github-to-skills) and only neat-freak passes all three scanners. Neither failing listing has a tree directory, so the flagged code is not necessarily what you would install, but re-check the security pages rather than assuming.
- All six live skills are written in Chinese, trigger phrases included. The repository links an English README, but the skill bodies themselves are not translated, so an English prompt may not fire a skill without editing its triggers.
- `hv-analysis` targets 10,000 to 30,000 characters and a PDF by default. That is a large spend for a question a shorter path could answer, and the report format is the point rather than the length.
- `storage-analyzer` supports macOS and Windows only. Its delete flow depends on a local service on 127.0.0.1 with a token, and the README says the service exits after 30 idle minutes.

## Related

- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Agentic Awesome Skills - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install six, not nine. The three listings without a tree directory cannot be cloned, whatever the install count says.
- Read `leader` even if you never run it. The goal-brief structure, with a whitelist and anti-cheat acceptance, is the most portable idea in the set.
- Keep the `scripts/` and `references/` folders. `storage-analyzer` and `neat-freak` both depend on local tooling that a bare `SKILL.md` does not carry.
- Run `neat-freak` at the end of a task rather than mid-way. It compares finished work against the docs, and a half-built tree gives it the wrong answer.
- Pick one install route per skill. The README warns that a plugin install plus a hand-copied directory of the same skill leads to version confusion.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
