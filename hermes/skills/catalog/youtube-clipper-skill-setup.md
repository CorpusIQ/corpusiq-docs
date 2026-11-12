---
title: "YouTube Clipper - AI Chaptering and Bilingual Cuts"
description: "op7418 YouTube Clipper: 4.4K combined installs across 1 listing for AI chapter detection, segment cutting and burned-in bilingual subtitles"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/youtube-clipper-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "youtube", "video", "subtitles", "ffmpeg"]
---

# YouTube Clipper - Setup Guide

**Source:** [op7418/youtube-clipper-skill](https://www.skills.sh/op7418/youtube-clipper-skill) via skills.sh - 4.4K combined installs across 1 indexed listing; first seen Jan 22, 2026 (Nov 11, 2026 sweep)
**GitHub:** 2,307 stars, MIT license, `main` branch, last pushed 2026-01-22, 24 tracked files with a single `SKILL.md` at the repository root and an `install_as_skill.sh` script
**Category:** Video: chapter detection, clip extraction, bilingual subtitle translation and burning, repurposing copy
**Quality Tier:** 🟡 Established - 2,307 stars and MIT licensing with a working install script, held back by two Warn verdicts and an instruction body written in Chinese.

The workflow this skill encodes is the one a short-form operator does by hand: watch a long video, decide which ninety seconds are worth publishing, cut them, subtitle them in two languages, and write the caption. Here the agent does the finding and the cutting, and you approve the segments.

The chapter detection is the differentiator. Rather than splitting on timestamps, the skill asks the model what the video is about and where its arguments turn, which produces chapters at the two to five minute granularity a human would pick. Once chapters exist, selecting segments is a conversation instead of a scroll.

Subtitle work is the second part, and the README claims a specific efficiency: batch translation that cuts API calls by about 95 percent compared with translating segment by segment. The output is bilingual subtitles, then burned into the video with configurable styling. The final step generates platform-specific copy for Xiaohongshu, Douyin and WeChat, which tells you where the author publishes.

One fact should be stated before anyone installs this: the `SKILL.md` is written in Chinese, as are the usage examples. The models handle that fine, but a team expecting English instructions will be surprised, and the generated caption templates are shaped for Chinese platforms rather than for YouTube or LinkedIn.

## Installation

The README's recommended route is the skills CLI, pointed at the repository URL:

```bash
npx skills add https://github.com/op7418/Youtube-clipper-skill
```

The manual route runs the project's own installer, which also handles the Python dependencies and creates the configuration file:

```bash
git clone https://github.com/op7418/Youtube-clipper-skill.git
cd Youtube-clipper-skill
bash install_as_skill.sh
```

The script copies the files into the agent's skills directory, installs `yt-dlp`, `pysrt` and `python-dotenv`, checks the system dependencies and writes a `.env` file. Read it before running it, since it installs packages and writes outside the checkout.

Two system dependencies are not installed by the script and have to be present already. `yt-dlp` handles the download; FFmpeg built with `libass` handles the subtitle burn, and a FFmpeg without `libass` will fail at the last step rather than the first:

```bash
brew install yt-dlp ffmpeg-full
sudo apt install yt-dlp ffmpeg libass-dev
```

Python 3.8 or newer is required. The `.env` file the installer creates is where API keys for the translation step go, so check it after installation rather than assuming it is configured.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| youtube-clipper | 4,415 | Downloads a video and its subtitles, generates semantic chapters, cuts chosen segments, translates subtitles bilingually, burns them in and drafts platform copy. |

The single listing is the whole package, and no indexed listings fall below the threshold.

The skill body is one `SKILL.md` plus the scripts it calls. The repository is 24 files, which is small for the amount of work described because the heavy lifting belongs to `yt-dlp` and FFmpeg. The `install_as_skill.sh` path is the documented one, and the README states that `npx skills` installs to the agent skills directory directly.

## Why This Matters for Hermes Agents

Repurposing a long video is a sequence of small judgment calls, and agents are bad at sequences they did not invent. This skill supplies the sequence, and more importantly it supplies the pause: chapters first, then your selection, then cutting. An agent that goes straight to cutting produces clips that start mid-sentence.

The bilingual subtitle path is the part with the most practical value for a global audience. Burning subtitles is what makes a clip watchable without sound, and a burned subtitle cannot be turned off or mistranslated downstream. The 95 percent API reduction claim is about batching: translate the subtitle file as one document rather than as hundreds of separate calls.

The dependency chain is the honest cost. This is not a prompt. It is a small pipeline that needs Python, `yt-dlp` and an FFmpeg with libass, and every one of those can fail independently. Budget an hour for the first install and treat failures as environment problems before assuming the skill is wrong.

The platform copy step deserves a caveat for anyone outside China: the templates target Xiaohongshu, Douyin and WeChat. They are a starting point for those platforms and a poor fit elsewhere, so ask for a rewrite in your own voice rather than publishing the generated caption directly.

## Usage

| You say | What happens |
|---|---|
| "Download this video and chapter it" | Pulls the video and subtitles, then returns semantic chapters at a few minutes each rather than fixed intervals. |
| "Cut the segment about pricing and give me a vertical version" | Extracts the segment with frame-accurate timing through FFmpeg and reframes it. |
| "Make a bilingual subtitle track for this clip" | Translates the subtitle file as one batch and produces a two-language track. |
| "Burn the subtitles in" | Hardcodes the bilingual track with the styling from the configuration. |
| "Write the caption for this clip" | Drafts platform-shaped copy from the chapter content. |
| "Which five minutes of this hour-long talk are worth posting?" | Reads the chapters and ranks segments by how self-contained they are. |
| "Translate this to English and Chinese" | Runs the batch translator over the existing subtitle file without re-downloading the video. |

## Verification

The `SKILL.md` sits at the repository root. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/op7418/Youtube-clipper-skill/main/SKILL.md | head -6
```

If the frontmatter and instructions come back in Chinese, that is the file, not an encoding problem. Confirm the two system binaries before blaming the skill:

```bash
yt-dlp --version
ffmpeg -hide_banner -filters 2>/dev/null | grep -w ass
```

The second command should list the `ass` filter, which is what a `libass`-enabled build provides. After installation, check that the `.env` file exists in the skill directory and holds whatever key the translation step needs.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| youtube-clipper | Warn | Pass | Warn |

Two of the three scanners return Warn. Read that as a signal about the shape of the skill rather than about the author: it downloads arbitrary URLs, runs FFmpeg subprocesses, writes files and reads environment variables for API keys. A scanner sees network egress plus subprocess execution plus credential access, and it warns.

The practical consequences belong in your own hands. The `.env` file holds a translation API key, so do not commit it. The download step takes a URL from the conversation, which means an injected instruction can point it at any host; keep the URL explicit. And the install script runs package installs as your user.

## Limitations

- Snapshot data, verified 2026-11-11: 4,415 combined installs across 1 indexed listing; 2,307 GitHub stars; MIT; last pushed 2026-01-22. Counts drift over time.
- The `SKILL.md` and the usage documentation are written in Chinese, and the caption templates target Xiaohongshu, Douyin and WeChat rather than YouTube, LinkedIn or X.
- Last pushed in January 2026, the oldest source in this batch. YouTube's own surfaces change, and `yt-dlp` may need updating independently of the skill.
- The dependency chain is real: Python 3.8+, `yt-dlp`, and an FFmpeg built with `libass`. A stock FFmpeg without `libass` fails at the burn step.
- Two of three scanners Warn, and the install script performs package installs and writes a configuration file.
- Translation quality depends entirely on the API behind the `.env` key, and the skill does not evaluate it. A subtitle is burned into the pixels, so a bad translation is not recoverable from the output.
- Downloading third-party video has terms attached. This guide describes the tool, not the right to redistribute what it produces.

## Related

- [YouTube Content - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/youtube-content-setup)
- [YouTube Skills - Transcript API Suite for Agents](/hermes/skills/catalog/youtube-skills-setup)
- [OpenMontage Video Production Skills - Setup Guide](/hermes/skills/catalog/openmontage-video-skills-setup)

## Pro Tips

- Chapter before you cut, always. The chapter list is cheap to review and the cut is expensive to redo.
- Install `ffmpeg-full` rather than plain FFmpeg on macOS, and check for the `ass` filter before the first burn instead of after.
- Ask for chapters as text first, save the selection, then run one cut. Re-running the analysis for each attempt is the main time sink.
- Ask for a caption rewrite in your own voice. The generated copy is platform-shaped for Chinese apps and reads as translated marketing elsewhere.
- Update `yt-dlp` separately with `pip install -U yt-dlp` when a download fails. It breaks before the skill does.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
