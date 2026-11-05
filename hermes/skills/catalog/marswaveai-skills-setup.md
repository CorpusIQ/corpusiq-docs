---
title: "Marswave Skills - Voice, TTS and Slides Setup"
description: "marswaveai/skills on skills.sh: 13.0K combined installs across 20 listings; ListenHub voice, TTS, ASR, podcast, slides and image generation skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/marswaveai-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "text to speech", "media generation", "podcast"]
---

# Marswave Skills - Setup Guide

**Source:** [marswaveai/skills](https://www.skills.sh/marswaveai/skills) via skills.sh - 13.0K combined installs across 20 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 82 stars, MIT licence, last pushed 2026-11-03, 19 SKILL.md directories at the repository root, one per skill
**Category:** Voice and media production for agents: text to speech, transcription, podcast and explainer video, slides, music, images and avatars through ListenHub
**Quality Tier:** 🟡 Beta - Gen Agent Trust Hub Fail on tts; MIT; 82 stars.

MarsWave publishes 19 skills that turn a prompt into audio or video. Most of them are thin, opinionated wrappers over the hosted ListenHub API: text to speech, speech to text, podcast episodes, explainer videos, slide decks, music, images and video. Two of them are routers: `listenhub` and `listenhub-cli` read the request and pick the skill that should handle it, which is how a single "make a podcast" phrase reaches the right endpoint without the user naming a skill.

The remaining skills split by medium. `cola-avatar-pack` is the odd one out: a local generator for pixel-art avatars, profile cards, emoji GIFs and meme stickers that runs on Python and Pillow rather than the hosted API. Trigger phrases in the skill descriptions are written in both English and Chinese, so routing works for either language.

## Installation

The README documents one install line for the whole collection:

```bash
npx skills add marswaveai/skills
```

Updates go through the same CLI, followed by an agent restart:

```bash
npx skills update -g
```

The ListenHub skills need the CLI installed and authenticated before they can generate anything:

```bash
npm install -g @marswave/listenhub-cli
```

```bash
listenhub auth login
```

`content-parser` and `creator` additionally require a ListenHub API key, created from the settings page at listenhub.ai. `cola-avatar-pack` needs Python 3.10 or newer and Pillow, and is documented in its own SKILL.md. The README also gives a git route for contributors, `git pull origin main` inside a clone.

## What It Provides

Twelve of the 20 indexed listings meet the 500-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| listenhub | 1,558 | Intent router that maps podcast, explainer, slides, TTS, image and video requests to the matching skill |
| tts | 1,432 | Text-to-speech and voice narration, including read-aloud requests in English and Chinese |
| asr | 1,317 | Local speech recognition that transcribes audio files to text |
| image-gen | 1,206 | AI image generation from text prompts |
| podcast | 1,203 | Podcast episodes from a topic, URL or text, in solo, dialogue or debate form |
| explainer | 1,145 | Narrated explainer videos with AI-generated visuals |
| content-parser | 1,132 | Extracting page content from a URL so another skill can use it as source material, needs an API key |
| music | 709 | Generating, remixing, extending and stem-splitting AI music through Mureka, plus lyric recognition |
| creator | 695 | Platform-ready content packages for WeChat, Xiaohongshu and spoken-word formats, needs an API key |
| listenhub-cli | 601 | CLI authentication and setup routing for the ListenHub commands |
| slides | 578 | Slide decks from a topic, URL or text with AI visuals |
| cola-avatar-pack | 546 | Pixel-art avatars, profile cards, emoji GIFs and meme stickers through Pillow |

The remaining 8 indexed listings range from 8 to 336 installs, covering the narrower generation and transcription variants.

## Why This Matters for Hermes Agents

Media is where agents most often hand-wave. Asked for a podcast, a model will describe an episode instead of producing an audio file, because text is the only output it controls. These skills close that gap: the generation call, the waiting, and the saved file all happen inside the skill.

The router design is the transferable idea. `listenhub` and `listenhub-cli` exist only to dispatch by intent, so a large surface stays reachable through one trigger phrase and the user never has to remember a skill name.

`asr` is the useful companion. Local transcription lets an agent check what a generated narration actually says, which turns a one-way generation step into a loop the agent can verify.

Bilingual triggers are a practical detail worth copying. Every skill description lists English and Chinese phrasing, so the same pack routes correctly for teams working in either language rather than needing a translated fork.

The dependency to plan for is the account. Most of this pack is a client for a paid hosted service, so the agent is only as capable as the authenticated session it runs under, and cron or sandboxed runs need their own credentials.

## Usage

| You say | What happens |
|---|---|
| "read this paragraph aloud" | tts renders narration and returns the audio file |
| "transcribe this recording" | asr runs local speech recognition and writes the text out |
| "make a podcast about vector databases" | podcast writes and renders a solo or dialogue episode |
| "turn this URL into an explainer video" | content-parser extracts the page, then explainer builds a narrated video |
| "make slides from this article" | slides builds a deck with AI-generated visuals |
| "generate a soundtrack and split the stems" | music generates the track, extends it and returns separated stems |
| "draw an avatar for my profile" | cola-avatar-pack produces a pixel-art avatar and an emoji set |

## Verification

Fetch a raw skill file to confirm the tree still matches what skills.sh indexed. This path is `tts/SKILL.md` on branch `main` and it returned 200 on November 4, 2026:

```bash
curl -fsSL https://raw.githubusercontent.com/marswaveai/skills/main/tts/SKILL.md | head -20
```

A response opening with `name: tts` in the frontmatter confirms the content is live. After the install, the skills land as directories in the agent skills directory the CLI prompts for, so list that directory and look for the skill names above.

Then confirm the service side, which is where these skills actually fail:

```bash
listenhub auth login
```

A completed login means the hosted generation calls have a session to use. If the agent runs under a scheduler or a container, repeat the login there rather than reusing your interactive session.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| listenhub | Pass | Pass | Pass |
| tts | Fail | Pass | Pass |
| asr | Pass | Pass | Pass |
| slides | Pass | Pass | Pass |

Gen Agent Trust Hub fails `tts`, the second most installed skill in the suite, while Socket and Snyk pass it. The other three sampled skills pass all three auditors. Read `tts/SKILL.md` before enabling it, and scope the ListenHub credentials to a single workspace so a failed skill cannot reach more than its own account.

## Limitations

- Snapshot data, verified 2026-11-04: 12,967 combined installs across 20 indexed listings; 82 GitHub stars; MIT licence; last pushed 2026-11-03. Counts drift over time.
- Gen Agent Trust Hub fails `tts` in the sampled set. That is the most serious verdict in this pack and it is not offset by a clean Socket or Snyk result.
- The install index carries 20 listings against 19 skill directories in the repository, so one listing has no one-to-one directory match in the current tree.
- Most skills call the hosted ListenHub API. They need the CLI plus `listenhub auth login`, and `content-parser` and `creator` also need an API key.
- `cola-avatar-pack` is the only skill that runs locally, and it requires Python 3.10 or newer with Pillow installed.
- Trigger phrases are bilingual, but parts of the README and several skill bodies are Chinese only, so plan for translation if the team does not read Chinese.

## Related

- [ByteDance MediaKit CLI - Video Processing Setup](/hermes/skills/catalog/mediakit-cli-skills-setup)
- [MiniMax H3 Skills - AI Video Prompt Writing & Generation](/hermes/skills/catalog/minimax-h3-skills-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the `listenhub` router when you do not know which skill fits. It picks from the intent instead of making you name a skill.
- Authenticate in the environment the agent runs in. A login in your shell does nothing for a scheduled job in another container.
- Feed `content-parser` output into `explainer` or `slides` rather than pasting text. The skills chain, and the parser keeps the source structure.
- Run `asr` on a generated narration before publishing. Hearing the transcript is cheaper than listening to the file.
- Schedule `npx skills update -g` and restart the agent afterwards, which is what the README asks for after an update.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
