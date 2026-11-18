---
title: "Creative Writing Skills - Fiction Agent Suite Setup"
description: "haowjy/creative-writing-skills: 19.5K combined installs across 58 listings; skills for writing novels, short stories, and serial fiction."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/creative-writing-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "creative writing", "fiction", "novel"]
---

# Creative Writing Skills - Setup Guide

**Source:** [haowjy/creative-writing-skills](https://www.skills.sh/haowjy/creative-writing-skills) via skills.sh - 19.5K combined installs across 58 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 593 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-16. Skills ship in `skills/` with generated `plugin/claude`, `plugin/cursor`, and `plugin/opencode` copies, alongside a set of writer, critic, and knowledge agents.
**Category:** Creative writing / fiction production
**Quality Tier:** 🟠 Orange - 57 Pass, 2 Warn and 1 Fail (Snyk) across the 20 sampled listings.

The suite writes novels, short stories, and serial fiction with agents that keep the author's voice and track continuity. Muse is the author-facing partner: it talks, plans, and drafts in your voice, then spawns critics and knowledge capture. Specialized agents handle each mode of work (writer, critic, brainstormer, outliner, character-sim, reader-sim, style-creator, continuity-checker), while shared skills carry the craft methodology.

Install lands as a Claude Code or Cowork plugin, on meridian-cli, or as Claude.ai marketplace skills. Run project-setup once before writing: it interviews you and writes `AGENTS.md`, the `kb/` layout, and the style files every agent reads.

## Installation

On meridian-cli, add and sync the repo:

```bash
meridian mars add haowjy/creative-writing-skills
meridian mars sync
```

Then run `meridian` to start a session with muse; first-run setup runs the bootstrap automatically.

Claude Code and Cowork share the same plugin format:

```bash
/plugin marketplace add haowjy/creative-writing-skills
/plugin install creative-writing-skills@creative-writing-skills
```

Start muse as the session agent, then run the one-time project setup:

```bash
claude --agent creative-writing-skills:muse
```

```text
/creative-writing-skills:project-setup
```

On Claude.ai, add the marketplace (sidebar, Customize, Personal plugins, +, Create plugins, Add marketplace, Add from repository, enter `haowjy/creative-writing-skills`) or upload the `.skill` files from the latest release. Then turn on `creative-writing-muse` in a chat and describe what you want to write.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| writing-principles | 1,186 | What fiction readers want (reader reward channels) and the ways LLM training damages prose; load when drafting, critiquing, or diagnosing a flat passage. |
| creative-writing-craft | 941 | Put fiction on the page or judge how it reads: production modes, prose technique, scene mechanics, style analysis, and genre craft. |
| llm-writing | 815 | Write commit messages, PRs, changelog entries, docs, READMEs, AGENTS.md, and prompts in plain words, stripping default LLM phrasing. |
| writing-staffing | 791 | Decide which agent takes which lane, which skills it loads, and which model runs it before handing off story work. |
| story-review | 781 | Diagnose a draft: editorial review, developmental edit, line edit, copyedit, proofreading, and reader-signal synthesis. |
| story-planning | 771 | Plan before prose: creative direction, brainstorming, outlining, and story architecture. |
| reader-sim | 638 | Read a draft as a specified first-time reader and report the moment-by-moment reading experience. |
| character-sim | 615 | Speak as a character: in-character conversation, voice discovery, and relationship pressure tests. |
| project-setup | 612 | One-time guided setup that interviews the author, then writes AGENTS.md, the kb/ layout, and style files. |
| story-memory | 611 | Preserve and retrieve durable story state: fact extraction, context scoping, reference writing, and issue tracking. |
| intent-modeling | 586 | Separate what a person said from what they meant before acting on their instructions. |
| shared-dao | 581 | Resolve one name per concept when a term has two names or meanings, or before coining a new one. |
| creative-writing-muse | 574 | Work with one creative partner that talks, plans, drafts in your voice, critiques, and revises across a project. |
| creative-research | 560 | Ground a story in fact: historical detail, cultural texture, and domain accuracy, returned as a sourced report. |
| grill-with-docs | 556 | Indexed listing with no counterpart in the current tree; the current grill skill stress-tests a plan or direction with the author. |
| creative-writing-modes | 537 | Indexed listing; the production-modes guidance was folded into creative-writing-craft as its prose-modes resource. |
| kb-management | 531 | Indexed listing; knowledge-base upkeep now runs through the kb-lead agent and the story-memory skill. |
| prose-writing | 491 | Indexed listing; prose-writing guidance now lives as a resource under creative-writing-craft, not a standalone skill. |
| story-architecture | 477 | Indexed listing; story-architecture guidance now lives as a resource under story-planning, not a standalone skill. |
| information-hierarchy | 456 | Decide what a reader or user sees first, what sits behind a click, and what to cut on any surface. |

The remaining 38 indexed listings range from 4 to 443 installs.

## Why This Matters for Hermes Agents

The suite models fiction work as a division of labor: muse owns the conversation, and focused workers take the passes that need their own context. A durable knowledge base under `kb/` holds characters, world, timeline, canon, and issues, so each session picks up accurate context instead of re-deriving it.

project-setup is the gating step: it writes `AGENTS.md` and style files from your own prose samples, so agents draft in your voice rather than a default one. reader-sim and critic give two different kinds of feedback, an experiential reader response versus a craft diagnosis, and muse brings you what is still open after two critique rounds instead of resolving it silently.

The suite also covers non-fiction surfaces: llm-writing disciplines commit messages, docs, and READMEs, and information-hierarchy orders what a reader sees first on a screen, a report, or a reply.

## Usage

| You say | What happens |
|---|---|
| "claude --agent creative-writing-skills:muse" | Starts a session with muse, the author-facing partner that drafts and spawns critics. |
| "/creative-writing-skills:project-setup" | Interviews you about the project and writes AGENTS.md, the kb/ layout, and style files. |
| "Brainstorm plot options without committing" | Fans out brainstormers for creative variety before anything is decided. |
| "Write this scene in my voice" | Drafts from your style files so the prose matches your existing voice. |
| "Critique this chapter" | Runs critic lanes and, after two rounds, brings back what is still open for you to decide. |
| "Check the timeline for contradictions" | Runs continuity-checker against established canon. |
| "Read this as a first-time reader" | Runs reader-sim for a moment-by-moment experiential read. |

## Verification

Probe two skills on the `main` branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/haowjy/creative-writing-skills/main/skills/writing-principles/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/haowjy/creative-writing-skills/main/skills/creative-writing-craft/SKILL.md
```

Then add the repo on meridian-cli and confirm the plugin registered:

```bash
meridian mars add haowjy/creative-writing-skills
meridian mars sync
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| writing-principles | Pass | Pass | Pass |
| creative-writing-craft | Pass | Pass | Pass |
| llm-writing | Pass | Pass | Pass |
| writing-staffing | Pass | Pass | Pass |
| story-review | Pass | Pass | Pass |
| story-planning | Pass | Pass | Warn |
| reader-sim | Pass | Pass | Pass |
| character-sim | Pass | Pass | Pass |
| project-setup | Pass | Pass | Fail |
| story-memory | Pass | Pass | Pass |
| intent-modeling | Pass | Pass | Pass |
| shared-dao | Pass | Pass | Pass |
| creative-writing-muse | Pass | Pass | Pass |
| creative-research | Pass | Pass | Warn |
| grill-with-docs | Pass | Pass | Pass |
| creative-writing-modes | Pass | Pass | Pass |
| kb-management | Pass | Pass | Pass |
| prose-writing | Pass | Pass | Pass |
| story-architecture | Pass | Pass | Pass |
| information-hierarchy | Pass | Pass | Pass |

The sample covers 20 of the 58 indexed listings. The single Fail is a Snyk flag on project-setup; the two Warn cells are Snyk flags on story-planning and creative-research. All other sampled cells pass.

## Limitations

- Snapshot data, verified 2026-11-17: 19,508 combined installs across 58 indexed listings; 593 GitHub stars; Apache-2.0; last pushed 2026-11-16. Counts drift over time.
- Five indexed listings (grill-with-docs, creative-writing-modes, kb-management, prose-writing, story-architecture) carry install counts but have no matching skill directory in the current tree; their guidance was folded into other skills' resources or agents, and the table notes this per row.
- project-setup carries a Snyk Fail in the skills.sh sample; review that skill's page before relying on it in a production pipeline.
- The plugin format targets Claude Code, Cowork, and meridian-cli; plain Claude.ai chat runs skills only, with the agents greyed out.
- The writing-sync skill (Google Drive sync) is present in the tree at 57 installs and does not appear in the install table.

## Related

- [Anti-Slop - AI Copywriting Quality Skill](/hermes/skills/catalog/anti-slop-setup)
- [Claude Blog - AI Blog Writing and SEO Plugin Setup](/hermes/skills/catalog/claude-blog-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run project-setup once before writing anything; it writes the AGENTS.md, kb/ layout, and style files every agent reads, and skipping it makes them guess your conventions.
- Add a few prose samples so style-creator can capture your voice; drafts match it better than a default voice.
- Let muse own the verdict after two critique rounds rather than hand-editing each critic's notes.
- Use reader-sim for pivotal scenes where the experiential read matters more than craft critique.
- The plugin/ trees are generated; rebuild with `mars build plugin` only if you edit a source skill in skills/.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
