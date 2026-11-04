---
title: "Drama Skills - AI Short Drama Production Suite"
description: "zenstory-ai/drama-skills: 23.6K installs across 12 listings; twelve skills from novel analysis and storyboards to video prompts and a finished cut."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/drama-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "short drama", "video production"]
---

# Drama Skills - Setup Guide

**Source:** [zenstory-ai/drama-skills](https://www.skills.sh/zenstory-ai/drama-skills) via skills.sh - 23.6K combined installs across 12 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 3,764 stars, MIT, last pushed 2026-11-04, 13 SKILL.md directories (12 of them indexed)
**Category:** Short-form drama for agents: story beats, shot lists, character continuity and episode packaging for serialized AI video
**Quality Tier:** 🟡 Yellow: short-drama-produce draws a Snyk Warn, and the production step spends money on external media APIs once you confirm a job

Drama Skills is the production line of a working motion-comic studio, published as skills. Eleven production skills run the chain from source novel to finished cut: novel analysis, adaptation development, episode script, visual assets, image prompts, storyboard, video prompts, confirmed production, editing and review. A twelfth, maintainer-only skill curates the know-how behind the set.

The organising idea is that creative decisions live in files, not in the conversation. Each episode carries its own script, visual design, storyboard, image-prompt and video-prompt documents, plus a cut list when a film is assembled. A continuity lock written as one phrase is pasted unchanged into every affected prompt, and a checker verifies declared references before generation.

## Installation

The README's install line is one command, and `-g` installs for every directory rather than the current one:

```bash
npx skills add zenstory-ai/drama-skills -y -g
```

Dropping `-g` scopes the install to the current project. To update, the README says to run the same command again.

Prerequisites are stated plainly: an agent that supports the Agent Skill spec (Claude Code, Codex or similar), `npx` on the terminal, Python 3.9 or newer for the bundled scripts, and `ffmpeg` plus `ffprobe` on PATH if you intend to cut a film.

Skills can also be linked individually from a clone, which is the route to take when you only want one capability:

```bash
git clone https://github.com/zenstory-ai/drama-skills.git && cd drama-skills
```

```bash
mkdir -p "$HOME/.claude/skills"
for skill in skills/*; do
  ln -s "$PWD/$skill" "$HOME/.claude/skills/$(basename "$skill")"
done
```

Invocation differs by runtime: Claude Code uses `/short-drama`, Codex uses `$short-drama`, and plain language works everywhere.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| short-drama-storyboard | 2,274 | Shots, boundaries and frozen keyframe prompts from script and visual design |
| short-drama-write | 2,251 | Episode script with causal beats and the project's production dialect |
| short-drama-video-prompts | 2,200 | Copyable video prompts: action, performance, camera, sound, start and end states |
| short-drama | 2,175 | Project init, five-document routing, Look Development and the local Dashboard |
| short-drama-review | 2,154 | Review of source analysis, script, assets, prompts and storyboards |
| short-drama-develop | 2,151 | Adaptation plan, story engine, episode map and director brief |
| short-drama-image-prompts | 2,143 | Lookdev style frames, reference prompts and scoped edit prompts |
| short-drama-assets | 2,140 | Character, location and prop settings with continuity decisions |
| short-drama-novel-analyze | 2,070 | Chapter index, per-chapter function extraction and episode candidates |
| short-drama-produce | 2,031 | Previews a bounded media job, waits for explicit confirmation, then executes |
| short-drama-edit | 1,961 | Cut list with in and out points, subtitles and loudness, rendered to film |
| short-drama-knowhow | 8 | Maintainer-only know-how curation; not for normal creative work |

No indexed listings fall below the threshold; all 12 listings appear above.

## Why This Matters for Hermes Agents

Serialized AI video breaks on continuity, not on prompt wording. This suite answers that with a naming and reference discipline the agent can check: `IMG-*` for images that exist, `PLAN-*` for planned shots, `REF-*` for references actually inspected, and continuity locks that must appear verbatim in every affected prompt.

The confirmation gate is the most reusable pattern in the pack. Production is a separate skill from prompt writing, it prints the exact count, content, parameters and adapter for a batch, and it refuses to treat an earlier acceptance or a preview as consent for a new paid job. For any Hermes workflow that spends money on an external API, that shape is worth copying.

Provider neutrality is the third piece. Prompts, storyboards and scripts stay in plain Markdown, credentials stay outside the project, and the generation adapters are optional profiles rather than a core dependency, so swapping a model does not rewrite the project.

The suite also models the boundary between measuring and judging. The check and measurement scripts report facts only and pass no verdict, and the review skill writes findings without editing the source files it reviewed.

## Usage

| You say | What happens |
|---|---|
| "Use $short-drama to init a vertical 9:16 short-drama project" | Creates the project skeleton, routes the five documents and opens the Dashboard |
| "Use $short-drama-novel-analyze to triage novel.txt" | Builds a chapter index, per-chapter functions and an adaptation value call |
| "Use $short-drama-develop to build the episode map" | Produces adaptation plan, story engine, episode map and director brief |
| "Use $short-drama-write to write EP001" | Writes a performable episode script with causal beats |
| "Use $short-drama-storyboard to author EP001's storyboard" | Shots, coverage, boundaries and frozen keyframe prompts |
| "Use $short-drama-video-prompts to write EP001's prompts for MiniMax H3" | Binds existing character, location and prop images as references, lists what is missing |
| "Use $short-drama-produce to preview EP001's job" | Prints the batch for review and executes only after you confirm |
| "Use $short-drama-edit to cut EP001 into a film" | Records why each in and out point sits where it does, then renders |

## Verification

Fetch one raw skill file to confirm the tree matches what skills.sh indexed. The path is skills/short-drama/SKILL.md on branch main, and it returned 200 on November 4, 2026:

```bash
curl -fsSL https://raw.githubusercontent.com/zenstory-ai/drama-skills/main/skills/short-drama/SKILL.md | head -20
```

A response with `name: short-drama` and a Chinese description confirms the file is live. Confirm the runtime prerequisites before the first production run:

```bash
python3 --version
```

```bash
ffmpeg -version | head -1
```

Python below 3.9 or a missing ffmpeg will surface later, inside the edit step, where the error is harder to read.

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| short-drama-storyboard | Pass | Pass | Pass |
| short-drama | Pass | Pass | Pass |
| short-drama-image-prompts | Pass | Pass | Pass |
| short-drama-produce | Pass | Pass | Warn |
| short-drama-knowhow | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified November 4, 2026: 23,558 combined installs across 12 indexed listings; 3,764 GitHub stars; MIT; last pushed 2026-11-04. Counts drift over time.
- The repo carries 13 skill directories against 12 indexed listings: short-drama-breakdown has a directory and a README entry, but no install count in the index.
- The primary README and the skill bodies are Chinese-first. An English README (README_EN.md) covers the workflow, and the install and invocation rules are the same.
- Production spends real money. Adapters are included for Seedance, GPT Image 2, MiniMax H3 video and MiniMax Music, and generation is billed by the provider you point it at.
- Cutting a film needs ffmpeg and ffprobe on PATH, and the scripts need Python 3.9 or newer.
- short-drama-produce carries a Snyk Warn in the sampled set; it is the skill that calls external media APIs.

## Related

- [ai-video-generation - AI Video Production (196K installs)](/hermes/skills/catalog/ai-video-generation-setup)
- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the triage skill before the full analysis on any long source. It answers whether the novel is worth adapting in one pass instead of after a chapter-by-chapter extraction.
- Keep the five project documents in the repo and let the agent read them back. The whole continuity story depends on files, not on chat history.
- Ask for the preview every time, and read the parameters. The production skill shows exactly what it will send and for how many shots.
- Write the continuity lock once and paste it unchanged. Paraphrasing it in one prompt is the failure mode the checker is built to catch.
- Treat the review skill as read-only. It writes findings and revision requirements; applying them belongs to the skill that owns the file.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
