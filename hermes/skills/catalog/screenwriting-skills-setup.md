---
title: "Screenwriting Skills - Screenwriting and Dramaturgy Suite"
description: "jtydhr88/screenwriting-skills - 7.7K combined installs across 26 indexed listings: agent skills for screenwriting, television writing and dramaturgy."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/screenwriting-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "screenwriting", "dramaturgy", "television"]
---

# Screenwriting Skills - Setup Guide

**Source:** [jtydhr88/screenwriting-skills](https://www.skills.sh/jtydhr88/screenwriting-skills) via skills.sh - 7.7K combined installs across 26 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 2,091 stars, MIT license, `main` branch, last pushed 2026-10-03, `SKILL.md` files under `plugins/screenwriting/skills/<name>/`, with a `reference.md` beside most
**Category:** Creative writing - screenwriting, television writing and dramaturgy
**Quality Tier:** 🟢 Green - all twelve sampled skills pass the Gen Agent Trust Hub, Socket and Snyk.

screenwriting-skills is a collection of 26 agent skills for screenwriting, television writing and dramaturgy, distilled from 47 craft books and 23 volumes of published scripts, scores and plays across Chinese, American, British, Japanese and Korean sources. The skills follow the open agentskills.io standard and are shared by Claude Code and OpenAI Codex from a single source tree.

The skill bodies are written in Chinese because most sources are Chinese originals or translations, but output follows whatever language you ask in; a term table in sw-workflow maps the craft vocabulary back to its original English terms. Four layers organise the set: general dramaturgy, the medium layer (series and stage), tradition and trade, and master corpora such as Chekhov, Ozu, Succession and television case studies.

## Installation

Install as a plugin in Claude Code (recommended):

```
/plugin marketplace add jtydhr88/screenwriting-skills
/plugin install screenwriting@screenwriting-skills
```

Skills are then invoked as `/screenwriting:sw-dialogue`. Alternatively clone and copy the folders:

```bash
git clone https://github.com/jtydhr88/screenwriting-skills.git
cp -r screenwriting-skills/plugins/screenwriting/skills/* ~/.claude/skills/
```

For project scope, copy into `.claude/skills/` instead. For Codex, add the plugin with `codex plugin marketplace add jtydhr88/screenwriting-skills`, or copy the folders into `~/.agents/skills/` (all projects) or `.agents/skills/` (project). The same 26 skill files ship through both plugins with no duplication.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sw-scene-craft | 578 | Scene and sequence craft: value turns, beats, text and subtext, enter late leave early, suspense and props. |
| sw-story-structure | 577 | Structure: Field's paradigm, Save the Cat beats, McKee's act structure, midpoint and openings and endings. |
| sw-character-conflict | 457 | Character and conflict: Egri's three-dimensional character, McKee's dimensions and antagonism, Jung archetypes. |
| sw-dialogue | 440 | Dialogue: action-based lines, subtext, fixing on-the-nose or expository speech and giving each voice distinction. |
| sw-premise-theme | 413 | Premise, theme and logline: controlling idea, the desire-vs-misbelief third rail and subject selection. |
| sw-workflow | 404 | Project orchestrator: routes a project through stages, names the skill per stage and keeps state in a story-bible.md. |
| sw-sitcom-comedy | 361 | Half-hour comedy: premise-driven predicaments, joke mechanics and multi vs single camera formats. |
| sw-series-structure | 317 | Episode and season structure: acts, teasers, act outs, cliffhangers, A/B/C weaving and season shape. |
| sw-format-adaptation | 308 | Format and adaptation: spec rules, the Fountain output contract and Chinese and Japanese formats. |

The remaining 17 indexed listings range from 181 to 274 installs.

## Why This Matters for Hermes Agents

The set's backbone is sw-workflow, a meta-skill that adds no craft knowledge but routes a project through stages (premise to submission for a feature, engine to draft for a series), names which skill to invoke at each stage, and keeps all state in a story-bible.md so work resumes across sessions. For a long-running agent that is the missing glue: the individual craft skills fire well on their own, and sw-workflow sequences them.

The multilingual design is the other notable decision. The bodies are Chinese, but a term table restores the field's original English vocabulary (logline, act out, beat sheet, showrunner) so an agent answers in the language it was asked in. One source tree avoids the combinatorial cost of translated forks drifting apart.

The corpus work is unusual in depth: chekhov-dramaturgy reads seven full plays plus the one-acts as a method, succession-series-writing tabulates all four seasons of Succession across 39 shooting scripts, and the Chinese opera layer splits by vocal system (banqiang vs qupai) because each imposes different structure, format and lyric rules.

## Usage

| You say | What happens |
|---|---|
| "Break my series into acts" | sw-series-structure places act outs and cliffhangers on a four, five or six-act grid. |
| "My dialogue is all on the nose, fix this scene" | sw-dialogue plus sw-scene-craft rewrite the lines and the scene. |
| "Turn this novel into a 40-episode drama outline" | sw-chinese-series-practice and sw-series-engine-bible plan the adaptation. |
| "Set up a project and track where I am" | sw-workflow routes the stages and saves state to story-bible.md. |
| "Fix my saggy second act" | sw-story-structure or sw-truby-anatomy rebuilds the middle act organically. |
| "Write a sitcom episode" | sw-sitcom-comedy applies the predicament, joke and format rules. |
| "Help me run a writers room" | sw-writers-room covers breaking story, notes and the staff ladder. |

## Verification

Review the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/jtydhr88/screenwriting-skills/main/plugins/screenwriting/skills/sw-dialogue/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/jtydhr88/screenwriting-skills/main/plugins/screenwriting/skills/sw-workflow/SKILL.md | head -20
```

Skills live under `plugins/screenwriting/skills/<name>/`; confirm the path exists in the current tree before installing a specific one. Run `/skills` to list installed skills, or invoke one explicitly with `$sw-story-structure`.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sw-scene-craft | Pass | Pass | Pass |
| sw-story-structure | Pass | Pass | Pass |
| sw-character-conflict | Pass | Pass | Pass |
| sw-dialogue | Pass | Pass | Pass |
| sw-premise-theme | Pass | Pass | Pass |
| sw-workflow | Pass | Pass | Pass |
| sw-sitcom-comedy | Pass | Pass | Pass |
| sw-series-structure | Pass | Pass | Pass |
| sw-format-adaptation | Pass | Pass | Pass |
| sw-truby-anatomy | Pass | Pass | Pass |
| chekhov-dramaturgy | Pass | Pass | Pass |
| sw-writers-room | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 16, 2026: 7,716 combined installs across 26 indexed listings; 2,091 GitHub stars; MIT; last pushed 2026-10-03. Counts drift over time.
- Skill bodies are written in Chinese: you cannot audit the instruction files directly unless you read Chinese, only the agent's account of them. Output still follows your language.
- The security sample covers 12 of the 26 listings; the other 14 carry no skills.sh verdicts, so re-check them before production use.
- The MIT license covers the skills themselves only; quotations from the source books and scripts remain with their authors, translators and publishers (see the repo's NOTICE file).
- Stage coverage is partial: film and television are covered, while musical theatre and some opera traditions are planned rather than shipped.

## Related

- [Story Skills](/hermes/skills/catalog/story-skills-setup)
- [Playwriter](/hermes/skills/catalog/playwriter-setup)
- [Drama Skills](/hermes/skills/catalog/drama-skills-setup)
- [Oh Story ClaudeCode Skills](/hermes/skills/catalog/oh-story-claudecode-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Let sw-workflow sequence the other skills; it keeps project state in story-bible.md so work resumes across sessions.
- Ask in whatever language you want; the term table in sw-workflow restores the field's English vocabulary regardless of the source language.
- The same 26 SKILL.md files are read by both Claude Code and Codex from one source tree; install once for either.
- Keep quotations out of anything you ship: only the skills are MIT, the book and script excerpts are not.
- Reverse-engineer a show before writing one: sw-series-structure measures act lengths from published West Wing, Succession and Fleabag scripts.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
