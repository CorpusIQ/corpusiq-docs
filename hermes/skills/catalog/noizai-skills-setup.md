---
title: "Noiz AI Skills - Voice and Speech for Agents"
description: "noizai/skills: 15.3K combined installs. Ten voice skills for text to speech, cloning, dubbing, sound effects, music and transcription."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/noizai-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "voice", "text to speech", "audio"]
---

# Noiz AI Skills - Setup Guide

**Source:** [noizai/skills](https://www.skills.sh/noizai/skills) via skills.sh - 15.3K combined installs across 10 indexed listings; first seen 2026-11-02 (morning sweep)

**GitHub:** [NoizAI/skills](https://github.com/NoizAI/skills) - 532 stars, no license and no `LICENSE` file anywhere in the tree, branch main, last pushed 2026-09-28; 10 `SKILL.md` directories under `skills/`, most with a `scripts/` folder of Python or shell entry points

**Category:** Voice for agents: text to speech, voice cloning and speech-to-text through the Noiz AI API

**Quality Tier:** 🟡 Beta - 532 stars and 15.3K installs across ten skills, but three of the five sampled listings carry a warning and the repository has no license at all

NoizAI publishes this as the central repository for giving a bot a voice, in the repository's own words a set of skills to "human" vibe-talking. Ten skills ship, and they cover the round trip: text to speech, expressive character voice, voice cloning from a person's own recordings, video translation and dubbing, a daily news podcast, sound effects, songs with vocals, music videos, transcription, and a template for writing new skills.

The interesting design choice is what sits behind each skill. Most of them carry real scripts rather than prompt-only instructions: `tts/scripts/tts.py` handles synthesis, timeline rendering and subtitle conversion, `characteristic-voice/scripts/speak.sh` wraps preset speaking styles, `speech-to-text/scripts/stt.py` transcribes, and `sound-fx`, `text-to-music`, `music-video` and `video-translation` each ship their own entry point. An agent gets a program to call, not a description of how to call an API.

Two backends are documented. The Noiz API is the recommended one, and it is where the emotion control, speed control and reference-audio cloning live. Kokoro is the local fallback, selected per call with `--backend kokoro`, which trades those features for running on the machine. The README's own framing is local-first: the skills run on your hardware and keep text and assets there, which is a meaningful claim for anything that transcribes a meeting.

## Installation

The README's commands use the skills CLI, with `--full-depth` because the skills sit one folder deeper than the default scan:

```bash
npx skills add NoizAI/skills --list --full-depth
npx skills add NoizAI/skills --full-depth --skill tts -y
npx skills add NoizAI/skills
```

The first lists what is available, the second installs one skill, the third installs the set. The README's fourth variant is for working inside the repository itself:

```bash
npx skills add . --list --full-depth
```

Nothing in the repository mentions Hermes. The skills are Markdown plus scripts, so a profile skills directory takes the same tree, but the commands inside them assume the repository layout, which means `skills/tts/scripts/` has to stay where the skill expects it:

```bash
git clone https://github.com/NoizAI/skills.git /tmp/noiz-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -R /tmp/noiz-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

The API key is documented through a `tts.sh` helper, and that path does not exist in this snapshot, so it is worth knowing before you chase the error. The tree ships `skills/tts/scripts/tts.py`, whose own header says it replaces the shell script, and its error messages print the exact command to run. Either of these works from the clone root:

```bash
python3 skills/tts/scripts/tts.py config --set-api-key YOUR_KEY
export NOIZ_API_KEY=YOUR_KEY
```

The key is written to `~/.config/noiz/api_key`, with a non-destructive migration from the older `~/.noiz_api_key`, and every script reads the environment variable first. Get a key from developers.noiz.ai.

`music-video` needs ffmpeg. Its code mode also needs Node, Google Chrome and git, while its hybrid mode reads only local stills and clips and calls no image or video generation API.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| tts | 4,306 | Text to speech on Kokoro or Noiz: simple mode, timeline-aligned rendering, precise duration control and reference-audio voice cloning, with subtitle-ready output. |
| characteristic-voice | 2,783 | Companion-like speech through fillers, emotional tuning and preset styles: goodnight, morning, comfort, celebrate and chat, each with its own speed and emotion. |
| chat-with-anyone | 2,091 | Talking with a real person or a fictional character in their own voice: finds their speech online, extracts a clean reference sample, then replies in that voice. |
| video-translation | 2,051 | Translating and dubbing a video into another language, replacing the original audio with TTS while the picture stays untouched. |
| daily-news-caster | 1,898 | Fetching current news and rendering a dual-host conversational podcast script plus the audio file. |
| template-skill | 1,550 | The reusable template for authoring new skills: clear triggers, workflow and I/O contracts, with a Chinese version alongside it. |
| sound-fx | 376 | Sound effects from a text description: animals, ambience, cartoon and sci-fi, 1 to 30 seconds, WAV, MP3 or FLAC output. |
| speech-to-text | 192 | Transcription from audio or video with speaker identification, timestamps for captions and multilingual output. |
| text-to-music | 20 | A full song with vocals from a description and lyrics, or a cover of an existing song in a new style, two variants per request as MP3. |
| music-video | 18 | A 24fps music video from an existing song, built as p5.js animation or assembled from local stills and clips. |

No indexed listings fall below the threshold; all 10 appear above.

The README's skills table documents eight of the ten. `template-skill` and `speech-to-text` are in the tree with full `SKILL.md` files and are absent from that table, so the table is a subset rather than the inventory. The distribution is steep: the top four listings hold most of the installs, and the two music skills sit at 20 and 18.

## Why This Matters for Hermes Agents

Voice is usually the part of an agent pipeline that gets bolted on last and works worst. The pattern this pack supports is the opposite: a script per capability, called like any other tool. `tts.py` takes text and writes audio; `stt.py` takes audio and writes a transcript with timestamps; `speak.sh` applies a named preset; `t2m.py` and `sfx.py` take a description and return a file. That is a shape an agent can plan around, retry and verify, because every step leaves a file behind.

The character work is the differentiator. Plain TTS reads a sentence; a comfort preset at 0.8 speed with softer emotion sounds like a person who noticed you were having a day. Fillers, emotional weighting and preset styles are the difference between a voice assistant and a companion, and they are exposed as flags rather than as prompt instructions.

The transcript path matters for anything with recordings. Speaker identification and caption timestamps are what turn a call recording into something an agent can index, and having it in the same pack as the speech synthesis means a voice loop can be closed without a second vendor.

The caveats are real. Cloning a voice is a consent question before it is a technical one, and `chat-with-anyone` is explicitly built to find someone's speech online and imitate it. The API features need a key and a paid account; only the Kokoro path is free and local. And the repository carries no license, so the terms you are accepting are the ones in the Noiz service terms, not an open source grant.

## Usage

| You say | What happens |
|---|---|
| "Read this article out loud as a voiceover" | tts converts the text on Kokoro or Noiz, writes the audio file, and can align it to a subtitle timeline or hold a target duration. |
| "Say this like you are comforting me" | characteristic-voice applies the comfort preset, lowering speed and softening emotion, then speaks through `speak.sh`. |
| "Turn this week's news into a two-host podcast" | daily-news-caster fetches current stories, writes a conversational script for two hosts and renders the audio. |
| "Dub this video into Spanish" | video-translation transcribes, translates, maps voices per segment and replaces the audio track while keeping the video intact. |
| "Make a door-slamming sound effect, two seconds" | sound-fx generates the effect from the description and writes it as WAV, MP3 or FLAC. |
| "Transcribe this interview with speaker labels" | speech-to-text produces a transcript with speaker identification and timestamps that can feed captions. |
| "Write a lo-fi song about coffee and sing it" | text-to-music writes lyrics if you have none, generates the song with vocals and returns two variants. |

## Verification

The raw paths below returned 200 on branch main when this guide was written on 2026-11-02:

```bash
for p in tts characteristic-voice speech-to-text; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/NoizAI/skills/main/skills/$p/SKILL.md"
done
```

After a clone, count the skills and check that the script the docs name is the script that ships:

```bash
git clone --depth 1 https://github.com/NoizAI/skills.git /tmp/noiz-skills
find /tmp/noiz-skills/skills -name SKILL.md | wc -l
ls /tmp/noiz-skills/skills/tts/scripts
ls ~/.config/noiz/api_key || echo "no API key stored"
```

The count should be 10. The third command prints `tts.py`, `noiz_tts.py`, `render_timeline.py`, `text_to_srt.py` and `test_tts.py`; there is no `tts.sh`, which is why the README's key command fails as written. The last line tells you whether a key is already on disk before you debug a synthesis error that is really an auth error.

Once a key is present, the README's own quick check exercises the preset engine directly:

```bash
bash /tmp/noiz-skills/skills/characteristic-voice/scripts/speak.sh \
  --preset comfort -t "Hmm... I'm right here." -o comfort.wav
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tts | Pass | Pass | Pass |
| chat-with-anyone | Pass | Warn | Warn |
| template-skill | Pass | Pass | Pass |
| speech-to-text | Pass | Pass | Warn |
| music-video | Warn | Pass | Warn |

Only two of the five sampled listings pass all three auditors. `chat-with-anyone` carries a Socket warning and a Snyk warning, `speech-to-text` carries a Snyk warning while passing the first two, and `music-video` has the only Gen Agent Trust Hub warning in the sample alongside a Snyk warning. The two that are flagged hardest are the two that handle other people's audio, one by scraping a voice sample online and one by ingesting recordings, which is where a reader should look first.

The disk surface is code, not prose. The tree holds 12 Python files, two shell scripts, four MP4 demos and a GitHub workflow, spread across eight skills with a `scripts/` folder. Every script calls the same base URL and reads `NOIZ_API_KEY` from the environment or from a key file under the home directory, so an install gains both network egress and a credential path.

Two risks are specific to this domain. Voice cloning is a likeness and consent issue before it is a technical one, and `chat-with-anyone` is designed to locate a real person's speech and reproduce it; nothing in the repository states a consent policy. And transcription means audio that may contain other people leaves the machine when the Noiz backend is used, even though the README's local-first framing is accurate only for the Kokoro path and for the hybrid music video mode.

There is no `LICENSE` file in the repository root, and no per-skill license file either. Treat the code as source-available under the vendor's service terms rather than as open source you can redistribute.

## Limitations

- Snapshot data, verified 2026-11-02: 15,285 combined installs across 10 indexed listings; 532 GitHub stars; no license; last pushed 2026-09-28. Counts drift over time.
- No license anywhere in the tree, neither at the root nor per skill. The code is source-available at best, and redistribution is a question for the vendor.
- The docs and the tree disagree on one path: the README and two `SKILL.md` files call `skills/tts/scripts/tts.sh`, which is not in the snapshot. The working entry point is `skills/tts/scripts/tts.py`, which describes itself as the replacement.
- The README's own skills table lists eight of the ten listings. `template-skill` and `speech-to-text` exist in the tree but not in that table.
- The Noiz API key is needed for emotion control, cloning and the paid features, and the free local path is Kokoro only. `music-video` needs ffmpeg, and its code mode also wants Node, Chrome and git.
- `chat-with-anyone` finds a real person's speech online and clones it. There is no consent rule in the repository, so the policy has to come from you.

## Related

- [Vapi Skills - Voice AI Agent Building Setup](/hermes/skills/catalog/vapi-skills-setup)
- [QwenCloud AI Skills - Multimodal Suite Setup](/hermes/skills/catalog/qwencloud-ai-setup)
- [ByteDance MediaKit CLI - Video Processing Setup](/hermes/skills/catalog/mediakit-cli-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Set `NOIZ_API_KEY` in the environment rather than relying on the documented `tts.sh config` command. The script that command names is not in the tree, and every entry point reads the environment variable first.
- Use a preset before you tune parameters. The five named styles in `speak.sh` already pair a speed with an emotion, and starting from a preset produces a better result than dialling emotion weights from scratch.
- Keep Kokoro for drafts and the Noiz backend for delivery. The local backend is free and fast enough to iterate on wording, and the API is where the emotion control and cloning quality live.
- Check durations before you render a long script. The tts skill supports timeline-aligned rendering and precise duration control, which is cheaper than re-rendering a five minute voiceover because the last line overran.
- Decide your cloning policy before you install `chat-with-anyone`. The skill will find and imitate a real person's speech, and the only guardrail is the one you write.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
