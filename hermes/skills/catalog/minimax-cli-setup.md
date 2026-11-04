---
title: "MiniMax CLI - Multimedia Generation for Agents"
description: "minimax-ai/cli: 32.4K combined installs. Official MiniMax command line for text, image, video, speech, music and vision from any agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/minimax-cli-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "multimedia", "video", "cli"]
---

# MiniMax CLI - Setup Guide

**Source:** [minimax-ai/cli](https://www.skills.sh/minimax-ai/cli) via skills.sh - 32.4K combined installs across 2 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 2,211 stars, no licence file, last pushed 2026-10-19, 2 SKILL.md directories
**Category:** Multimedia generation for agents: text, images, video and speech from the official MiniMax command line
**Quality Tier:** 🟡 Yellow - Snyk carries a Warn on mmx-cli and the repository ships no LICENSE file, even though the README badge claims MIT

MiniMax publishes this repository as the official command line for its AI platform, built for agents rather than for people typing at a prompt. Two skills are indexed. mmx-cli holds 32,330 of the 32,370 combined installs and mmx-h3-video holds 40, so the pack is effectively one skill plus a specialist video add-on. The binary installs from npm as mmx-cli and needs Node.js 18 or newer.

The surface is wide for a single tool. Text covers multi-turn chat, streaming, system prompts and JSON output. Image covers text to image with aspect ratio and batch controls. Video generation is asynchronous with progress tracking. Speech covers text to speech with more than 30 voices plus transcription to json, verbose_json, srt and vtt. Vision describes images, search queries the web through MiniMax, and both the Global region at api.minimax.io and the CN region at api.minimaxi.com are supported. Calls require a MiniMax Token Plan.

## Installation

The README gives two paths, one for agents and one for terminal use:

```bash
npx skills add MiniMax-AI/cli -y -g
npm install -g mmx-cli
```

Neither path mentions Hermes, and the skills are plain SKILL.md files sitting at skill/SKILL.md and skill/h3-video/SKILL.md, so a profile skills directory takes the same tree:

```bash
git clone --depth 1 https://github.com/minimax-ai/cli.git /tmp/mmx-cli
cp -R /tmp/mmx-cli/skill ~/.hermes/profiles/corpusiq/skills/mmx-cli
```

Authenticate before the first call. The interactive flow offers MiniMax OAuth or a pasted API key, and the non-interactive form takes the key directly:

```bash
mmx auth login
mmx auth login --api-key YOUR_KEY
mmx quota
```

mmx quota prints the remaining balance, which is the cheapest way to confirm the credential works before an image or video job spends credit. A Token Plan subscription is required, from platform.minimax.io for Global or platform.minimaxi.com for CN.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| mmx-cli | 32,330 | The main skill: text chat with streaming and JSON output, text to image with aspect ratio and batch controls, asynchronous video generation, speech synthesis with 30+ voices, transcription to json, verbose_json, srt and vtt, vision and web search, all from one Node.js binary at skill/SKILL.md. |
| mmx-h3-video | 40 | The separate H3 video directory at skill/h3-video/SKILL.md, kept beside the main skill rather than inside it; the README's video section documents the async generation and progress tracking it wraps. |

No indexed listings fall below the threshold; all 2 appear above.

The distribution is as lopsided as a two row pack can be. mmx-cli carries 32,330 installs and mmx-h3-video carries 40, so the second listing is an add-on for one video model, not a peer skill. Both directories exist in the tree and both are covered by the table.

## Why This Matters for Hermes Agents

Media generation is usually the point where an agent has to leave its own toolchain: one vendor for images, another for speech, a third for video, each with its own auth and its own output conventions. This pack collapses that into one binary with one credential and one region switch, which means a single install covers the four media types most agent tasks actually need.

The shape is friendly to automation. Every command writes a file or returns structured output, `--output json` makes the response parseable, and the text commands accept a messages file on stdin, so an agent can pipe a conversation in and get a completion out without shell quoting games. A run that leaves an artefact behind can be verified by checking the artefact, which is the property that separates a tool call from a promise.

Video is the interesting case because it is slow. Generation is asynchronous with progress tracking, so an agent can start a job, do other work and poll, instead of blocking a turn on a render. Speech adds transcription in four formats, which closes the loop: generate audio, transcribe it back, and compare against the script the agent wrote.

The dual region support matters more than it looks. Global and CN endpoints are separate hosts with separate accounts, and being able to point at either from the same binary avoids a second integration when a project has users on both sides. The cost surface is also visible in one place through mmx quota, which is what you want before an agent starts fanning out image jobs.

## Usage

| You say | What happens |
|---|---|
| "Write me a product description with MiniMax" | mmx text chat sends the message to MiniMax-M3.1-Flash by default, with --model or a saved default-text-model taking precedence, and prints the reply. |
| "Make three 16:9 hero images of a workshop bench" | mmx image generate takes the prompt with --n 3 and --aspect-ratio 16:9 and writes the batch to the working directory or to --out-dir. |
| "Generate a ten second clip of waves at sunset" | mmx video generate starts an async job and tracks progress until the clip is written. |
| "Narrate this paragraph in a warm voice" | mmx speech synthesize renders the text with a chosen voice and speed and writes the audio to --out. |
| "Transcribe this meeting into subtitles" | mmx speech transcribe reads the file and emits srt or vtt, or a json and verbose_json transcript. |
| "What is in this screenshot" | mmx vision describes the image passed on the command line. |
| "Check what is left on the plan before I batch this" | mmx quota reports the remaining Token Plan balance. |

## Verification

Check that both skill files resolve on branch main before copying anything:

```bash
for p in skill skill/h3-video; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/minimax-ai/cli/main/$p/SKILL.md"
done
```

The direct URL for the main skill is https://raw.githubusercontent.com/minimax-ai/cli/main/skill/SKILL.md and the video skill is at https://raw.githubusercontent.com/minimax-ai/cli/main/skill/h3-video/SKILL.md. Both should print 200. The README writes the owner as MiniMax-AI, which is the same repository; GitHub paths are case insensitive.

After the copy, confirm the tree landed and the binary is on PATH:

```bash
find ~/.hermes/profiles/corpusiq/skills/mmx-cli -name SKILL.md | wc -l
mmx --version
mmx quota
```

The count should be 2. If mmx is not found, the npm global install either failed or its bin directory is not on PATH; reinstall with npm install -g mmx-cli and check the npm prefix.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| mmx-cli | Pass | Pass | Warn |
| mmx-h3-video | Pass | Pass | Pass |

The sample is the whole pack, so there is nothing hidden below a threshold. mmx-h3-video passes all three auditors. mmx-cli passes Gen Agent Trust Hub and Socket and carries a Warn from Snyk, which is the one verdict to read before installing.

The install surface is a vendor CLI, not a folder of prompt files. Installing it globally means npm runs its package scripts on your host, and the tool then stores MiniMax credentials locally after mmx auth login. Every command in the README sends data to MiniMax: prompts, images, audio files and any text passed to transcription. Treat the machine as holding a live API credential and treat the outbound traffic as data leaving the machine, including any recording you transcribe.

There is no LICENSE file in the repository root. The README badge links to the MIT licence text, but a badge is not a grant, so the safe reading is that redistribution terms are unresolved until the file appears. If you need certainty, ask the vendor rather than assuming MIT.

## Limitations

- Snapshot data, verified November 3, 2026: 32,370 combined installs across 2 indexed listings; 2,211 GitHub stars; no licence file; last pushed 2026-10-19. Counts drift over time.
- No LICENSE file in the repository root, while the README badge claims MIT. Redistribution terms are unresolved until the file lands.
- A MiniMax Token Plan is required. Installing is free; text, image, video and speech calls spend plan credit, and video is the expensive one.
- Snyk warns on mmx-cli. The sample is two skills, one of which has 40 installs, so there is very little community evidence behind either verdict.
- The README is the only setup documentation in the snapshot and never mentions Hermes. The paths inside skill/SKILL.md assume the repository layout, so copy the skill directory intact rather than moving individual files.
- Node.js 18 or newer is required and the examples assume mmx is on PATH. Nothing in the pack covers Windows shells.

## Related

- [ai-video-generation - AI Video Production (196K installs)](/hermes/skills/catalog/ai-video-generation-setup)
- [Noiz AI Skills - Voice and Speech for Agents](/hermes/skills/catalog/noizai-skills-setup)
- [QwenCloud AI Skills - Multimodal Suite Setup](/hermes/skills/catalog/qwencloud-ai-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use --output json on text calls. MiniMax-M3.1-Flash is the default for text chat and text repl, and the JSON form saves parsing prose when an agent needs a field rather than a paragraph.
- Prefer the non-interactive login for anything automated. mmx auth login --api-key keeps the credential flow inside your secret handling instead of waiting on a browser prompt.
- Poll video rather than blocking. Generation is async with progress tracking, so start the job, write the result path down, and come back instead of holding a turn open.
- Ask for srt at synthesis time when you plan to caption. Transcription emits srt and vtt directly, which removes a separate conversion step in a video pipeline.
- Run mmx quota before a batch. Image and video fan-outs are where plan credit disappears, and the command is cheaper than discovering the limit halfway through.
- Copy the whole skill directory. skill/SKILL.md and skill/h3-video/SKILL.md assume the repository layout, so a partial copy breaks the relative paths they describe.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
