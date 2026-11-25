---
title: "rnskill Content Suite - Chinese AI Skills Setup"
description: "pluviobyte/rnskill - 12.1K combined installs: Chinese-language agent skills for short-form video, Xiaohongshu content, subtitles, covers and avatars."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rnskill-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "content creation", "video production", "xiaohongshu", "chinese"]
---

# rnskill Content Suite - Setup Guide

**Source:** [pluviobyte/rnskill](https://www.skills.sh/pluviobyte/rnskill) via skills.sh - 12.1K combined installs across 62 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [Pluviobyte/rnskill](https://github.com/Pluviobyte/rnskill) - 1,768 stars, NOASSERTION license field (README states CC BY-NC 4.0), last pushed Sep 21, 2026, main branch; 61 top-level skill directories under skills/<name>/SKILL.md plus nested skill collections.
**Category:** AI Content Creation (Video / Image / Article)
**Quality Tier:** 🟡 Yellow - 10 of 15 sampled skills pass all three checks; three carry a Snyk Warn and two were not parsed.

pluviobyte/rnskill is a Chinese-language AI agent skills collection maintained by Xuetawuyun for Codex, Claude Code and other agents that read SKILL.md. The 62 indexed listings span short-form video production (topic planning, script rewriting, hooks, titles, subtitles, talking-head cuts, motion graphics and reference replication), Xiaohongshu and Douyin content, digital avatars, TTS voice cloning, and a 22-skill business diagnostics toolkit, plus a smaller coding set.

The skills.sh index lists 62 listings at 12.1K combined installs, while the README counts 61 top-level skill directories (including compatibility aliases). Several indexed listings live in nested directories or under aliases, so the install index does not map one-to-one onto the tree.

## Installation

Claude Code plugin marketplace:

```bash
claude plugin marketplace add Pluviobyte/rnskill
claude plugin install ra-人话@rnskill
```

Generic install for Codex and Claude Code:

```bash
npx -y skills add Pluviobyte/rnskill -g --all
npx -y skills add Pluviobyte/rnskill --skill ra-人话
```

Manual install copies a skill directory into the agent's skills folder:

```bash
# Codex
mkdir -p <project>/.agents/skills
cp -R skills/ra-人话 <project>/.agents/skills/ra-人话
```

## What It Provides

skills.sh publishes per-skill descriptions for all 62 indexed listings; most map to a skills/<name>/ directory in the current tree, while a few live in nested directories or under aliases.

| Skill | Installs | Use For |
|---|---|---|
| ra-人话 | 1,284 | Chinese AI/tech writing de-AI editor for posts, threads and drafts |
| chengfeng-videocut-skills:剪口播 | 592 | talking-head video cut: transcribe, detect speech errors, review, FCPXML export |
| rn-motion-director | 271 | motion-first AI video director for topic-to-video creation |
| rn-replica-qc | 267 | analyze, recreate, align and verify reference-video motion |
| rn-dark-saas-video | 266 | dark cinematic SaaS and product motion videos |
| rn-bw-text-opener | 257 | black-background white-text opening animations |
| rn-motion-replica | 239 | build an original motion replica with reusable templates |
| editorial-collage-motion | 215 | halftone paper collage motion from a reference image or description |
| ra-hook | 213 | short-video hook type selection and writing (7 hook types) |
| dbs-ai-check | 212 | scans copy for AI-generated writing patterns |
| ra-audio-to-subtitles | 209 | word-timestamp subtitles from Volcengine Doubao ASR |
| ra-video-title | 207 | generates 8-12 theme-first two-part video titles |
| skill-captions | 206 | render, validate and burn production subtitles |
| ra-video-production-director | 205 | end-to-end video production orchestration |
| ra-local-talking-head-cut | 204 | local talking-head rough cut editing |
| video-use | 203 | conversational video editing: transcribe, cut, color, captions |
| dbs-hook | 203 | diagnoses a video opening, pairs with ra-hook |
| xhs-article-to-images | 202 | Markdown article to Xiaohongshu 3:4 image sets |
| heygen-digital-avatar | 200 | HeyGen Digital Twin generation and composition |

The remaining 43 indexed listings range from 1 to 199 installs.

## Why This Matters for Hermes Agents

This suite is a working example of an agent-driven short-form video pipeline: the author reports growing a Douyin account by 2,000 followers and landing a first paid brand deal on under 10 hours of total time using these skills with Codex, HyperFrames, HeyGen and IndexTTS2. For a builder running Hermes agents on content work, the skills map a whole production flow: topic selection, script rewriting, hooks and titles, subtitle rendering, cover generation, motion graphics and reference replication. The dbs sub-suite adds 22 business diagnostics skills for planning, benchmarking and decision-making, licensed CC BY-NC 4.0 from a third-party project. The collection is large (62 indexed listings), so it is cheap to browse but worth reviewing per skill before relying on it. Most sampled skills pass all three checks, with a handful of Snyk warnings and two unparsed listings in the sample. The main caveats are the non-English documentation and the NOASSERTION license field.

## Usage

| You say | What happens |
|---|---|
| Make this Chinese draft sound human | Uses ra-人话 to strip AI-flavored phrasing |
| Cut the filler from this talking-head video | Uses ra-local-talking-head-cut or chengfeng-videocut-skills:剪口播 |
| Give me a title for this finished video | Uses ra-video-title for two-part title options |
| Match this reference video with a motion piece | Uses rn-motion-replica then rn-replica-qc to verify alignment |
| Burn clean captions onto this cut | Uses skill-captions with ra-audio-to-subtitles timestamps |
| Design a short hook for the first five seconds | Uses ra-hook to pick a hook type and draft the opening |
| Turn this Markdown post into Xiaohongshu images | Uses xhs-article-to-images for 3:4 image sets |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/Pluviobyte/rnskill/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/Pluviobyte/rnskill/main/skills/rn-motion-director/SKILL.md | head -40
```

Both URLs return 200. The default branch is main. After installing, review each skills/<name>/SKILL.md before relying on it; several skills bundle their own scripts and assets.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ra-人话 | not parsed | not parsed | not parsed |
| chengfeng-videocut-skills:剪口播 | not parsed | not parsed | not parsed |
| rn-motion-director | Pass | Pass | Pass |
| rn-replica-qc | Pass | Pass | Pass |
| rn-dark-saas-video | Pass | Pass | Pass |
| rn-bw-text-opener | Pass | Pass | Pass |
| rn-motion-replica | Pass | Pass | Warn |
| editorial-collage-motion | Pass | Pass | Pass |
| ra-hook | Pass | Pass | Pass |
| dbs-ai-check | Pass | Pass | Pass |
| ra-audio-to-subtitles | Pass | Pass | Pass |
| ra-video-title | Pass | Pass | Pass |
| skill-captions | Pass | Pass | Pass |
| ra-video-production-director | Pass | Pass | Warn |
| ra-local-talking-head-cut | Pass | Pass | Warn |

15 of 62 listings were sampled: 10 pass all three checks, rn-motion-replica, ra-video-production-director and ra-local-talking-head-cut carry a Snyk Warn, and the two Chinese-named listings returned not parsed.

## Limitations

- Snapshot data, verified Nov 25, 2026: 12,134 combined installs across 62 indexed listings; 1,768 GitHub stars; NOASSERTION license field (README states CC BY-NC 4.0); last pushed Sep 21, 2026. Counts drift over time.
- The README counts 61 top-level skill directories (including compatibility aliases) against 62 indexed listings, and several listings live in nested directories or under aliases, so the install index does not map one-to-one onto the tree.
- GitHub reports the license as NOASSERTION; the README states CC BY-NC 4.0 with per-skill exceptions, and the dbs sub-suite is CC BY-NC 4.0 from a third-party project while some skills keep MIT or AGPL-3.0.
- Documentation and most skill bodies are in Chinese, which may affect non-Chinese agents.
- Several skills bundle scripts that call external services (Volcengine, HeyGen, yt-dlp and TikHub), so review each skill's scripts and API-key handling before use.

## Related

[Meitu Skills - AI Image and Video Suite](/hermes/skills/catalog/meitu-skills-setup) | [Ootto Content Skills - Instagram Reels Factory Setup](/hermes/skills/catalog/ootto-content-skills-setup) | [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole collection with npx -y skills add Pluviobyte/rnskill -g --all, or pull a single skill with --skill.
- Review each skills/<name>/SKILL.md before relying on it; many skills bundle their own scripts and API-key expectations.
- Pair ra-audio-to-subtitles with skill-captions, and ra-hook with dbs-hook, since the README documents them as working pairs.
- The dbs sub-suite (22 skills) is a third-party CC BY-NC 4.0 toolkit adapted for content quality checks; read the attribution notes before redistribution.
- Keep the default branch main in mind for raw GitHub URLs.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
