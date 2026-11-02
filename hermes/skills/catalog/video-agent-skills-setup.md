---
title: "Video Agent Skills - Video Production for Agents"
description: "melvynx/video-agent-skills: 7.8K combined installs. Thirteen Claude Code skills for scripting, editing, translating and publishing short-form video."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/video-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "video editing", "short-form video", "ffmpeg"]
---

# Video Agent Skills - Setup Guide

**Source:** [melvynx/video-agent-skills](https://www.skills.sh/melvynx/video-agent-skills) via skills.sh - 7.8K combined installs across 24 indexed listings; first seen 2026-11-01 (evening sweep)

**GitHub:** [Melvynx/video-agent-skills](https://github.com/Melvynx/video-agent-skills) - 86 stars, MIT with a `LICENSE` file in the root, branch main, last pushed 2026-10-22; 13 `SKILL.md` directories under `skills/`, one per skill, with `short-editing` carrying its own `engine/`, `references/` and `examples/` folders

**Category:** Short-form video production for coding agents: scripting, hook research, editing, translation and publishing

**Quality Tier:** 🟡 Beta - free and honestly documented with 86 stars, but two of the five sampled listings fail the Gen Agent Trust Hub scan and four carry a Snyk warning

The repository is published by Melvynx (Melvyn Malherbe) as the free base of the Editing IA Pro course at codelynx.dev, and it is MIT licensed. There is no app, no server and no subscription in the free pack: the skills are Markdown instructions that tell Claude Code how to do the work, and `short-editing` ships its own render engine built on Node, Chrome and ffmpeg, with whisper.cpp producing the word timings. Everything runs on the operator's machine, on macOS, Windows or Linux, and the README ships six real shorts made with it as examples.

The working state lives in one folder at the project root. `studio-setup` creates `video-agent/` and writes `voice.md`, `style.json` and the permission rules; `studio-script` writes a week of scripts into `scripts/`; recordings land in `takes/`; `short-editing` writes `edits/short-<slug>/output/short-<slug>.mp4` together with an `.srt` and the post copy. Three surfaces are optional and priced separately: Treg for Instagram audits and publishing, an ElevenLabs key for dubbing, and Codex for generated images.

## Installation

In a project folder, the README's command installs all 13 skills into `.claude/skills/`:

```bash
npx skills add Melvynx/video-agent-skills -a claude-code
```

Add `-g` to install them for every project, and run `npx skills update` to pull the latest version. Anyone who installed before October 2026 is told to remove the old names first:

```bash
npx skills remove video-setup video-script video-viral video-audit video-edit video-steal video-translate video-publish long-to-short-videos -y
npx skills add Melvynx/video-agent-skills -a claude-code
```

That cleanup list covers nine of the eleven legacy listings. `video-repurpose` and `video-human` are in neither the cleanup command nor the rename table, and neither has a current folder, so treat them as dead index rows rather than skills to install.

The manual route is a plain directory copy. The README documents it into `~/.claude/skills/` for a user-wide install; the same copy works against a Hermes profile skills directory, which is the route to use here because nothing in the repository mentions Hermes:

```bash
git clone https://github.com/Melvynx/video-agent-skills.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r video-agent-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

To update a manual install, run `git -C video-agent-skills pull` and copy again. Then open the agent and run `/studio-setup`: about 15 minutes, once.

Outside the skills CLI the pack needs Node 20 or newer, git, ffmpeg, yt-dlp with deno, and a Chrome or headless Chromium plus whisper.cpp that `engine/setup.mjs` installs on the first edit, about 0.6 GB once. `studio-setup` prints the install command for each on macOS, Windows and Linux. On claude.ai only `studio-script` works, because it needs no local tools; the rest require the machine.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| studio-script | 622 | A week of short-form scripts written from the creator's real week and `voice.md`, each on a concept proven by the niche's outliers, with 3 scored hooks from 22 formulas, a re-hook, timing at their pace and a humanize pass. Also `viral`, `hook <topic>` and `humanize <text>`. |
| short-editing | 622 | One raw take into a finished short: silences and retakes cut, the take at 1.15x, boards on the exact word, word-by-word captions, the comment CTA, voice at -14 LUFS, plus the `.srt` and the post copy, all rendered by the skill's own engine. |
| codex-images | 610 | Thumbnails, covers, end cards and stills generated with Codex's image tool on a ChatGPT plan, several in parallel, using the creator's photos as reference when the face matters. |
| studio-setup | 605 | First run: checks Node, ffmpeg, yt-dlp and git, creates `video-agent/`, writes `voice.md`, sets the default style, pre-approves the tool commands and optionally connects Treg, ElevenLabs and Codex. |
| editing | 589 | The entry point. Reads the request, routes it to the one skill that owns it, and continues a video already in progress instead of starting it over. |
| steal | 583 | Measuring another creator's editing style with ffmpeg (cuts per second, layouts, captions, the beat and its sound effects, face size, zooms) into a named style, then editing a test video and comparing frames before use. |
| insta-audit | 563 | Auditing an Instagram account through Treg: the last 30 to 50 reels with real stats, what over-performs against the account's own median, the first seconds of the best and worst, and 3 changes written to `audit.md`. |
| clips | 561 | One long video, podcast, webinar or livestream into finished shorts, each edited by `short-editing`, plus new scripts from the ideas too spread out to clip. |
| publish | 554 | Getting a finished video onto YouTube Shorts or long form, Instagram Reels and TikTok through Treg, with the light export, the cover, the caption and the title, and nothing sent before an explicit yes. |
| broll | 553 | The creator's own clips, screen recordings and photos scanned once with ffprobe and ffmpeg, tagged by Haiku sub-agents into a library one grep can search, then placed full screen on a short. |
| short-translate | 550 | Dubbing a take into another language with the creator's cloned voice through ElevenLabs and their own key, then handing it to `short-editing` for captions in the new language. The image stays the original. |
| vox | 505 | One photo into a 6 to 15 second paper-collage animation in the style of Vox explainer documentaries: halftone cut-out, Codex-generated paper layers, stop-motion moves, captured to MP4. |
| outliers | 505 | Competitor reels and TikToks at 3x their own account's median or more, sponsored posts dropped, ranked against a watchlist, with the 5 best rewritten as remake scripts in the creator's voice. |
| video-edit | 50 | Legacy name from before October 2026. The README maps it to `/short-editing`. |
| video-setup | 49 | Legacy name from before October 2026. The README maps it to `/studio-setup`. |
| video-script | 49 | Legacy name from before October 2026. The README maps it to `/studio-script`. |
| video-viral | 47 | Legacy name from before October 2026. The README maps it to `/studio-script viral`. |
| video-translate | 46 | Legacy name from before October 2026. The README maps it to `/short-translate`. |
| video-publish | 46 | Legacy name from before October 2026. The README maps it to `/publish`. |
| video-audit | 46 | Legacy name from before October 2026. The README maps it to `/insta-audit`. |
| long-to-short-videos | 46 | Legacy name from before October 2026. The README maps it to `/clips`. |
| video-steal | 32 | Legacy name from before October 2026. The README maps it to `/steal`. |
| video-repurpose | 2 | Legacy index row with no current folder and no line in the README's rename table. Read the count as history, not as a skill to install. |
| video-human | 2 | Legacy index row with no current folder and no line in the README's rename table. Read the count as history, not as a skill to install. |

All 24 indexed listings clear the 0-install threshold and appear in the table above; the smallest is 2 installs.

The index does not describe the tree. Eleven of the 24 rows are pre-October-2026 names, and nine of the eleven carry between 32 and 50 installs, which reads as installs that were never moved to the current names. Those eleven rows hold 415 installs between them, against 7,422 across the 13 skills that actually ship. The live set is the top 13 rows: editing, studio-setup, studio-script, short-editing, insta-audit, outliers, steal, broll, clips, short-translate, vox, publish and codex-images.

## Why This Matters for Hermes Agents

Video editing is the kind of task where an agent improvises badly and confidently: a plausible cut list, no word timings, captions guessed from the transcript, a render that has no safe zone. This pack pushes the decision into files. `voice.md` holds who the creator is and how they talk, `style.json` holds the look, `audit.md` and `swipe.md` hold what already worked, `log.md` keeps one line per script so topics do not repeat, and `short-editing` renders from one spec file per short, `source/spec.js`, through a deterministic canvas renderer rather than an ad hoc ffmpeg chain.

The cost model is unusually clear for a video tool. The core path is local and free: transcription is whisper.cpp on the machine, the render is Node plus Chrome plus ffmpeg, and no API is called for a normal edit. Paid surfaces are opt in and quoted first. Treg is free on your own accounts and about $0.001 a call on other accounts, with $1 of credit on signup, and the skills say the price before a paid call. ElevenLabs spends the operator's own plan, and Codex images spend the ChatGPT plan rather than an API key.

Guardrails are written into the pack instead of left to the prompt. `studio-setup` merges a short allow list into `.claude/settings.json` covering `yt-dlp`, `ffmpeg`, `ffprobe`, the engine's own `node` entry points and Treg's free read-only commands, and the README states never `Bash(*)`. Paid Treg calls always ask first, publishing and dubbing wait for an explicit yes, and keys live in `video-agent/.env`, never in a chat message or a commit. For an unattended Hermes run, that is the difference between a skill that can act and a skill that can spend.

The README also states its own limits, which is rare and useful. Auto captions mishear names and numbers and need a check, generated images can misspell text, translation has no lip-sync, and without Treg the research is YouTube only and publishing is a manual kit. An agent told these limits up front produces fewer confident wrong answers than one that is told the tool is magic.

## Usage

| You say | What happens |
|---|---|
| "Set up my editing studio and make the look mine" | studio-setup checks Node, ffmpeg, yt-dlp and git, creates `video-agent/`, writes `voice.md` from your own videos or a short interview, then runs the style onboarding (color, paper, fonts, captions, pace, Instagram CTA, real tool logos) previewed on your footage. |
| "Edit my last take into a short" | short-editing transcribes locally with word timings, cuts every silence and retake, speeds the take to 1.15x, lays boards on the exact word, adds captions and the comment CTA, and writes the mp4, the `.srt` and the post copy under `video-agent/edits/`. |
| "Write this week's scripts from what I actually did" | studio-script reads `voice.md`, `swipe.md` and `audit.md`, writes scripts from your real week, gives 3 scored hooks per script from 22 formulas, checks timing at your pace, and runs the humanize pass. |
| "What blew up for my competitors this month" | outliers ranks the watchlist's reels and TikToks against each account's own median at 3x or more, drops sponsored posts, and rewrites the 5 best as scripts in your voice. |
| "Cut this podcast into shorts" | clips finds the moments that stand alone, cuts each into a take and hands it to short-editing; the ideas too spread out to clip become new scripts instead. |
| "Publish it to Shorts, Reels and TikTok tomorrow at 9" | publish picks the export, cover, caption and title, shows the plan with the time, and posts through Treg only after your explicit yes; without Treg it hands you a ready-to-post kit. |
| "Edit the way this reel is edited" | steal measures the reference with ffmpeg, writes `video-agent/styles/<name>/`, edits a test video and compares it frame by frame with the original before you commit to the style. |

## Verification

The raw paths below are the ones to probe before installing. All four returned 200 on branch main when this guide was written on 2026-11-01:

```bash
for p in studio-setup studio-script short-editing publish; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/Melvynx/video-agent-skills/main/skills/$p/SKILL.md"
done
```

After a clone, confirm the count instead of trusting the index. The repository holds 13 skills against 24 listings, so a copy with 24 folders is a copy that installed the pre-October names:

```bash
git clone --depth 1 https://github.com/Melvynx/video-agent-skills.git /tmp/video-agent-skills
find /tmp/video-agent-skills/skills -name SKILL.md | wc -l
head -3 /tmp/video-agent-skills/skills/short-editing/SKILL.md
```

The first count should be 13. The second should print the `name:` and `description:` frontmatter of `short-editing`, which is what the agent actually routes on.

On the machine, verify the toolchain the first edit depends on. A missing `whisper.cpp` or Chrome shows up as a failed render minutes later rather than as an install error:

```bash
node -v && ffmpeg -version | head -1 && yt-dlp --version
ls .claude/skills | wc -l
```

Node should be 20 or newer and the skill count 13. The engine's own setup writes the Chrome build and whisper.cpp on the first edit, roughly 0.6 GB, so run one short before scheduling anything unattended.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| studio-script | Pass | Pass | Warn |
| insta-audit | Fail | Pass | Warn |
| outliers | Pass | Pass | Warn |
| video-publish | Fail | Pass | Warn |
| video-human | Pass | Pass | Pass |

Two of the five sampled listings fail the Gen Agent Trust Hub scan: `insta-audit` and `video-publish`. Both are also Snyk Warn. They are the two skills that operate an external account, one connecting Instagram and reading its stats, the other posting to YouTube, Instagram and TikTok through Treg, so the failures sit exactly where you would want to read the skill before running it. `studio-script` and `outliers` pass the first two auditors and still carry a Snyk warning.

What the install puts on disk is small in the code sense and large in the disk sense. Twelve of the 13 skill folders hold nothing but Markdown: a `SKILL.md`, a `references/` folder in seven of them, and one `README.md` in `vox`. The only repository script outside `skills/` is `sync-engine.mjs`. Nothing runs on clone. `short-editing` is the exception: it ships `engine/` with Node render modules, a `short.html` stage, font and template assets, and `setup.mjs`, which downloads a Chrome build and whisper.cpp on the first edit. Budget the 0.6 GB and read `engine/setup.mjs` before an unattended first run, because that is the script that fetches binaries.

The permission model is the part worth keeping. The allow list is narrow on purpose, paid Treg calls ask before spending, and publishing and dubbing stop for a yes. Keys belong in `video-agent/.env`, which is git-ignored, and the skills are told to keep them out of chat and out of commits. If you widen the allow list to `Bash(*)` to stop the prompts, you have removed the only thing that keeps a publishing skill from publishing.

Two content risks come with the domain. The research skills download other creators' reels through yt-dlp or Treg, and the README's rule is to only download and cut videos you own or have the rights to. Generated images and Vox layers come from Codex, so anything published from them carries the same text-rendering and likeness questions as any generated asset.

## Limitations

- Snapshot data, verified 2026-11-01: 7,837 combined installs across 24 indexed listings; 86 GitHub stars; MIT; last pushed 2026-10-22. Counts drift over time.
- The index lists 24 rows and the tree holds 13 skills. Eleven rows are pre-October-2026 names, holding 415 installs between them, and two of those, `video-repurpose` and `video-human`, have no current folder and no entry in the README's rename table.
- Two of the five sampled listings, `insta-audit` and `video-publish`, fail the Gen Agent Trust Hub scan, and four of the five carry a Snyk Warn. The sample is five skills out of 13, so the rest of the pack is unaudited by that sample.
- The core path is local but not weightless: Node 20 or newer, ffmpeg, yt-dlp with deno, and about 0.6 GB of Chrome and whisper.cpp that install on the first edit. On claude.ai only `studio-script` runs, since the others need the machine.
- One layout family is deliberate. Colors, paper, fonts, captions, pace and sound are configurable through `/studio-setup style`, but the split-screen paper layout is not, and the README points at the paid course for the review studio, the teleprompter recorder and the B-roll app.
- Quality limits are stated by the pack itself: auto captions mishear names and numbers, generated images can misspell text, dubbing has no lip-sync, and without Treg the competitor research is YouTube only and publishing is a manual kit.

## Related

- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)
- [ScrapeCreators Social Research Skills - Setup Guide](/hermes/skills/catalog/scrapecreators-social-research-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `studio-setup` before anything else, and let it write `voice.md` from your own videos rather than from a description of them. Every script skill reads that file first, and a thin `voice.md` produces scripts that sound like the tool.
- Do one short end to end before you schedule anything. The first edit is what installs Chrome and whisper.cpp, roughly 0.6 GB, and it is better to pay that cost while you are watching than inside a cron run.
- Keep the render deterministic by editing `source/spec.js`, not the engine. The renderer is driven by one spec per short, so a spec change is reviewable and an engine change is not.
- Measure a style with `steal` before copying one by eye. The skill compares its test render against the reference frame by frame, which is the only way to know the copy held after the render.
- Check captions on anything with names, numbers or tool names. The pack says auto captions mishear those, and a wrong number in a caption is the failure a viewer notices first.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
