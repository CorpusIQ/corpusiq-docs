---
title: "YouTube Agent Skills - Eleven Channel Skills"
description: "jakeschincariol/youtube-agent-skill - 12.2K combined installs across 11 indexed listings: eleven skills that script, package, edit and audit videos."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/youtube-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "youtube", "video", "content"]
---

# YouTube Agent Skills - Setup Guide

**Source:** [jakeschincariol/youtube-agent-skill](https://www.skills.sh/jakeschincariol/youtube-agent-skill) via skills.sh - 12.2K combined installs across 11 indexed listings; first seen Nov 15, 2026 (Nov 15 evening sweep)
**GitHub:** 6,060 stars, MIT license, `main` branch, last pushed 2026-09-16, eleven `SKILL.md` files under `skills/`
**Category:** YouTube channel production and content workflow
**Quality Tier:** 🟡 Yellow - four of the eleven sampled skills carry Snyk Warns.

This collection is eleven Claude skills that together run a YouTube channel: scripting, title and thumbnail packaging, editing, retention, Shorts, SEO, chapters, comments, weekly planning and a whole-channel audit. It is free and MIT-licensed, and it needs no signup, no API key and nothing to connect.

The skills are more than prompts. Six of them ship standalone Python tools that run on a clean Python 3 with no dependencies, and those tools are where the hook scoring, title linting, edit-list generation and retention reading happen. Nothing is published automatically: the skills write the copy and the cut list, and the human uploads.

## Installation

Clone and copy the skill folders into Claude Code, or use the plugin path:

```bash
git clone https://github.com/Jakeschincariol/youtube-agent-skill.git
cp -r youtube-agent-skill/skills/yt-* ~/.claude/skills/
```

```text
/plugin marketplace add Jakeschincariol/youtube-agent-skill
/plugin install youtube-agent
```

Project-local installation copies the same folders into a repo's `.claude/skills/`. Then spend ten minutes on `templates/voice.md`: copy it to `~/.claude/youtube/voice.md` and fill it in, or send Claude three of your own videos and ask it to write the file. Every skill reads that voice file.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| yt-script | 1,200 | One idea into a script: five hooks from 21 formulas, scored, then the spoken script with retention beats marked. |
| yt-retention | 1,161 | Reads the audience-retention export: hook leak, the cliffs, the slide, and what to change. |
| yt-package | 1,135 | Title and thumbnail linted as one pairing for truncation, duplication and vagueness. |
| yt-viral | 1,121 | What works in a niche, ranked by multiple over each channel's own median. |
| yt-shorts | 1,117 | Finds the Shorts already inside a long video, with a new first line written for each. |
| yt-seo | 1,101 | The description, the tags worth having, and the three queries the video should win. |
| yt-edit | 1,094 | A transcript into an edit decision list: dead air, filler cues and retakes with timecodes. |
| yt-chapters | 1,084 | Chapters from a transcript, validated against YouTube's own rules. |
| yt-audit | 1,078 | The whole channel reviewed, ending in one fix rather than twenty. |
| yt-plan | 1,074 | A week that fits the hours available: one anchor, one cheap video, three Shorts. |
| yt-comment | 1,061 | The comment section triaged into four piles, then replies in your voice, plus which to pin. |

No indexed listings fall below the threshold; all 11 appear above.

## Why This Matters for Hermes Agents

YouTube advice from general model training is generic: it will tell an agent to make good content without telling it how to read a retention export or lint a title and thumbnail as one unit. These skills carry the mechanics, and much of the mechanics lives in code rather than prose. Six of the eleven skills ship Python tools with no dependencies, so the hook scoring, title linting and edit-list steps are deterministic instead of vibes.

The publishing boundary matters more. This collection deliberately stops short of upload: every skill ends in a block you copy and a question, ship it or change it. For an agent that can reach the network, that boundary is the difference between drafting and posting, and it is the thing to preserve if you automate any part of this workflow.

The fine print is unusually honest for a content collection. The hook scorer is a heuristic calibrated against 74 real short-form hooks, not a predictor, and the viral finder reads public listings without ever logging in as you. An agent that repeats those caveats to a user is behaving better than one that presents them as certainty.

## Usage

| You say | What happens |
|---|---|
| "Turn this idea into a script" | Uses yt-script to score five hooks and write the spoken script with retention beats marked. |
| "Lint my title and thumbnail together" | Uses yt-package to check the pairing for truncation, duplication and vagueness. |
| "Where did people leave this video?" | Uses yt-retention on the retention export to find the hook leak, the cliffs and the slide. |
| "Find Shorts inside this long video" | Uses yt-shorts to locate the clips and write a new first line for each. |
| "Plan my week with four hours" | Uses yt-plan to build a week of one anchor, one cheap video and three Shorts. |
| "Audit my channel" | Uses yt-audit to review the whole channel and end on one fix instead of twenty. |

## Verification

Check the skill files and confirm the Python tools run on a clean Python 3:

```bash
curl -fsSL https://raw.githubusercontent.com/jakeschincariol/youtube-agent-skill/main/skills/yt-script/SKILL.md | head -30
curl -fsSL https://raw.githubusercontent.com/jakeschincariol/youtube-agent-skill/main/skills/yt-retention/SKILL.md | head -30
python3 skills/yt-script/hookscore.py --hook "one line"
```

The README's own smoke test is to install the collection and confirm `/yt-script` works before touching the other ten skills.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-15) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| yt-script | Pass | Pass | Pass |
| yt-retention | Pass | Pass | Pass |
| yt-package | Fail | Pass | Pass |
| yt-viral | Pass | Pass | Warn |
| yt-shorts | Pass | Pass | Warn |
| yt-seo | Pass | Pass | Pass |
| yt-edit | Pass | Pass | Pass |
| yt-chapters | Warn | Pass | Pass |
| yt-audit | Pass | Pass | Warn |
| yt-plan | Pass | Pass | Pass |
| yt-comment | Pass | Pass | Warn |

The skills are Markdown plus six dependency-free Python tools, and none of them publish. The four Snyk Warns sit on the viral, shorts, audit and comment skills, and the single Trust Hub Fail sits on yt-package.

## Limitations

- Snapshot data, verified 2026-11-15: 12,226 combined installs across 11 indexed listings; 6,060 GitHub stars; MIT; last pushed 2026-09-16. Counts drift over time.
- The hook scorer is a heuristic calibrated against 74 short-form hooks, not a predictor; a low score is a reason to look again and a high score is not a promise.
- The viral finder reads public listings only and never logs in as you; it judges the title you can see, not why a video got its views.
- Without Claude Code, pasting a single `SKILL.md` at the top of a chat runs it as a mode, but the six Python tools are lost, which removes most of the value of the script, retention and edit skills.
- Tags barely matter, and this collection says so instead of selling a tag generator.

## Related

- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)
- [Youtube Content Setup](/hermes/skills/catalog/youtube-content-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install via the plugin or copy the folders; the voice template matters more than which path you pick, because every skill reads `~/.claude/youtube/voice.md`.
- Treat a high hook score as a reason to keep going, not as proof a hook will land.
- Ask the agent to state the retention beats in a script before you record, not after.
- For a fresh channel, run yt-audit first and act on its single fix before touching any other skill.
- Never wire this into an auto-upload pipeline: it does not publish by design.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
