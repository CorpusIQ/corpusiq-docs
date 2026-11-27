---
title: "ZRT AI Lab OpenCode Skills - Chinese Video Publisher Setup"
description: "zrt-ai-lab/opencode-skills - 3.7K combined installs: OpenCode skills for Chinese short-video production, image generation, and Feishu integration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/zrt-ai-lab-opencode-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "opencode", "video", "douyin", "wechat"]
---

# ZRT AI Lab OpenCode Skills - Setup Guide

**Source:** [zrt-ai-lab/opencode-skills](https://www.skills.sh/zrt-ai-lab/opencode-skills) via skills.sh - 3.7K combined installs across 30 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [zrt-ai-lab/opencode-skills](https://github.com/zrt-ai-lab/opencode-skills) - 305 stars, GitHub reports no license while the README states MIT, last pushed Jul 22, 2026, main branch; 30 skills in <skill-name>/SKILL.md directories with a README.md alongside most.
**Category:** OpenCode Video Editing and Chinese-Market Publishing
**Quality Tier:** 🟠 Orange - 20 of 30 listings sampled: 11 pass all three checks; searchnews carries three Warns and video-subtitle-remover carries one Fail (Gen Agent Trust Hub), which moves the suite to Orange.

zrt-ai-lab/opencode-skills is a 30-skill collection for OpenCode and OpenClaw spanning content creation, automated publishing, video editing, Feishu integration, development tooling, and agent orchestration. The suite's strongest cluster is Chinese-market short-video tooling: the videocut family (install, clip-oral, clip, subtitle, and self-update) drives a transcription-to-final-cut workflow, while auto-douyin and auto-weixin-video automate publishing to Douyin and WeChat Channels.

Skills install by copying each directory into ~/.opencode/skills/ (OpenCode) or ~/.openclaw/skills/ (OpenClaw), and several skills are OpenCode-specific in their paths and configuration. The README is written in Chinese and lists per-skill config requirements, including image and TTS API keys, Douyin and WeChat cookie scans, and Feishu app credentials.

## Installation

The README documents a manual copy install: place each skill directory into ~/.opencode/skills/ (OpenCode) or ~/.openclaw/skills/ (OpenClaw):

```bash
# copy a single skill
cp -r image-service ~/.opencode/skills/

# copy all skills
cp -r */ ~/.opencode/skills/
```

Runtime dependencies are listed per skill: Python 3.10+ for image, video, and data skills; Node.js 16+ for the Feishu skills; ffmpeg for video and videocut; Playwright for the Douyin and WeChat publishing skills.

## What It Provides

skills.sh publishes per-skill install counts for all 30 indexed listings. The 13 skills at or above 80 installs are tabled below; the remaining 17 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| videocut-subtitle | 539 | transcribe, dictionary-correct, review, and burn subtitles into video |
| auto-douyin | 520 | publish video to Douyin: cookie login, upload, topic tags, scheduled posting |
| videocut-clip | 310 | run confirmed FFmpeg cuts, looping until zero slip-ups, then generate subtitles |
| videocut-clip-oral | 238 | transcribe talking-head video and flag slip-ups into a review draft and deletion list |
| videocut-install | 212 | install dependencies, download the Whisper model, and verify the environment |
| auto-weixin-video | 201 | publish to WeChat Channels: upload, originality declaration, scheduling, collections |
| videocut-self-update | 135 | record user feedback and update the editing rules and methodology |
| video-creator | 133 | compose images plus audio into video with TTS, transitions, subtitles, outro, and BGM |
| image-service | 111 | generate and edit images across infographic, cover, long-image, slide, comic, article, XHS, and marketing scenes |
| log-analyzer | 94 | detect log type, extract entities, and run root-cause and alert analysis on 100M+ files |
| xhs-note-creator | 85 | Xiaohongshu (RED) note creation; no matching directory in the current tree (auto-redbook is the tree counterpart) |
| csv-data-summarizer | 83 | pandas-driven CSV statistics, visualization, and analysis report |
| story-to-scenes | 82 | split long text into scenes and batch-generate consistent, character-stable images |

The remaining 17 indexed listings range from 22 to 79 installs.

## Why This Matters for Hermes Agents

zrt-ai-lab/opencode-skills bundles a complete Chinese short-video production line into skills an agent can run end to end. The videocut family walks from environment install through slip-up detection, FFmpeg cutting, and subtitle burning, so a single agent can turn a raw talking-head recording into a finished, subtitled cut. The publishing pair (auto-douyin and auto-weixin-video) handles the fiddly parts: cookie login, upload, and scheduled posting to Douyin and WeChat Channels. Beyond video, image-service routes image generation across eight scenes, the Feishu skills cover Chinese workplace document and chat automation, and mcp-builder and skill-creator help an agent build its own tools. uni-agent adds a single API across ANP, MCP, A2A, and AITP for cross-protocol agent calls. The skills target the OpenCode and OpenClaw directories rather than the Claude Code layout, so builders on those runtimes get a turnkey fit.

## Usage

| You say | What happens |
|---|---|
| Add subtitles to this talking-head video | Runs the videocut flow to transcribe, dictionary-correct, review, and burn subtitles |
| Publish this video to Douyin tomorrow | Uses auto-douyin to scan a login cookie and schedule the upload with topic tags |
| Cut the slip-ups out of this recording | Uses videocut-clip-oral to flag slip-ups, then videocut-clip to run the FFmpeg cuts |
| Post this video to my WeChat Channels | Uses auto-weixin-video to upload with an originality declaration and scheduling |
| Generate a cover and long image for this article | Uses image-service scene routing for cover and long-image generation |
| Summarize this CSV file | Uses csv-data-summarizer to produce statistics, charts, and a report |
| Find the root cause in this log | Uses log-analyzer to detect the log type and extract key entities |

## Verification

Confirm the README and representative skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/zrt-ai-lab/opencode-skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/zrt-ai-lab/opencode-skills/main/videocut-subtitle/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/zrt-ai-lab/opencode-skills/main/auto-douyin/SKILL.md | head -40
```

All three URLs return 200. After installing, review each <skill-name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn and Fail verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| videocut-subtitle | Pass | Pass | Pass |
| auto-douyin | Pass | Warn | Pass |
| videocut-clip | Pass | Pass | Pass |
| videocut-clip-oral | Pass | Pass | Pass |
| videocut-install | Pass | Pass | Pass |
| auto-weixin-video | Pass | Pass | Pass |
| videocut-self-update | Pass | Pass | Pass |
| video-creator | Pass | Pass | Pass |
| image-service | Pass | Pass | Pass |
| log-analyzer | Pass | Pass | Pass |
| xhs-note-creator | Pass | Warn | Pass |
| csv-data-summarizer | Pass | Pass | Warn |
| story-to-scenes | Pass | Warn | Pass |
| deep-research | Pass | Pass | Warn |
| searchnews | Warn | Warn | Warn |
| video-subtitle-remover | Fail | Pass | Warn |
| smart-query | Pass | Warn | Pass |
| uni-agent | Pass | Warn | Warn |
| skill-creator | Pass | Pass | Pass |
| mcp-builder | Pass | Pass | Pass |

Across the 20 sampled skills there are 47 Pass, 12 Warn, and 1 Fail cells. 11 skills pass all three checks; searchnews carries three Warns and video-subtitle-remover carries one Fail (Gen Agent Trust Hub).

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,693 combined installs across 30 indexed listings; 305 GitHub stars; no license in GitHub metadata (README states MIT); last pushed Jul 22, 2026. Counts drift over time.
- The install index outruns the tree in one place: xhs-note-creator (85 installs) carries a skills.sh verdict but has no matching directory in the current tree; the tree's auto-redbook covers Xiaohongshu note creation.
- skills.sh sampled 20 of the 30 indexed listings; the other 10 carry no published verdict.
- The README and most SKILL.md descriptions are written in Chinese, so non-Chinese agents may need translation before driving the skills.
- GitHub metadata reports no license while the README states MIT; treat licensing as README-asserted until a LICENSE file lands in the repo.
- Several skills need configuration before use: image and TTS API keys, Douyin and WeChat cookie scans, Feishu app credentials, and SSH database access.

## Related

[rnskill Content Suite - Chinese AI Skills Setup](/hermes/skills/catalog/rnskill-setup) | [Huashu Skills - 22-Skill Content Production Pack](/hermes/skills/catalog/huashu-skills-setup) | [YouTube Clipper - AI Chaptering and Bilingual Cuts](/hermes/skills/catalog/youtube-clipper-skill-setup) | [OpenClaw XHS Setup - Xiaohongshu (RED) Integration](/hermes/skills/catalog/openclaw-xhs-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the videocut family in order: install, then clip-oral to flag slip-ups, clip to cut, and subtitle to burn.
- Re-check the security pages on skills.sh before relying on searchnews (three Warns) and video-subtitle-remover (one Fail).
- Install only the skills you need by copying single directories instead of cp -r */.
- Keep image and TTS API keys out of the repo; each configurable skill reads a local config file or environment variable.
- Confirm the xhs-note-creator path in the tree before relying on it, since the current tree ships auto-redbook instead.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
