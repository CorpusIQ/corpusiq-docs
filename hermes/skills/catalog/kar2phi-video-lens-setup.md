---
title: "Video Lens - YouTube Link Summarizer Skill Setup"
description: "kar2phi/video-lens - 3.2K combined installs: paste a YouTube link and get a summary, key points, and a timestamped outline beside the video"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/kar2phi-video-lens-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "youtube", "video summarizer", "transcript"]
---

# Video Lens - Setup Guide

**Source:** [kar2phi/video-lens](https://www.skills.sh/kar2phi/video-lens) via skills.sh - 3.2K combined installs across 3 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [kar2phi/video-lens](https://github.com/kar2phi/video-lens) - 142 stars, MIT license, last pushed Nov 20, 2026, main branch; three skills at skills/video-lens/SKILL.md, skills/video-lens-gallery/SKILL.md, and skills/video-lens-recs/SKILL.md.
**Category:** Video Summarization (YouTube)
**Quality Tier:** 🟡 Yellow - 6 Pass, 3 Warn, and 0 Fail across 3 sampled skills; each clears Gen Agent Trust Hub and Socket with a Warn on Snyk.

video-lens is a three-skill suite from kar2phi that turns a YouTube link into a readable report for coding agents. The core skill, video-lens, fetches a transcript and writes an executive summary, a takeaway, numbered key points, and a timestamped outline, then opens them beside the playing video in the browser. Two companion skills round out the workflow: video-lens-gallery opens or rebuilds the library of saved summaries, and video-lens-recs recommends videos worth watching, ranked with reasons and skipping anything already watched or summarised.

The notable part is scope discipline: this is a YouTube-link reader, not a video editor. It reads captions, generates a text report, files it in a local gallery, and surfaces recommendations; it does not cut, caption, or republish video. Reports are stored under ~/Downloads/video-lens/reports/, and sharing is opt-in via an unlisted link.

## Installation

Install all three skills with the skills CLI, picking all three when prompted:

```bash
npx skills add kar2phi/video-lens
```

On the first video, video-lens checks what is missing and asks before installing anything. Its Python packages go into the skill's own folder (~/.local/share/video-lens/venv), not system Python. The same setup can be run by hand:

```bash
python3 ~/.agents/skills/video-lens/scripts/setup.py transcript-api yt-dlp
# Optional, Apple Silicon: transcribe videos that have no captions
python3 ~/.agents/skills/video-lens/scripts/setup.py mlx-whisper && brew install ffmpeg
```

Adjust the path to where your agent keeps skills (~/.claude/skills/... for Claude Code). Add --upgrade when YouTube breaks an older release.

## What It Provides

skills.sh publishes a per-skill install count for each of the three indexed listings.

| Skill | Installs | Use For |
|---|---|---|
| video-lens | 2,198 | Fetch a YouTube transcript and generate a summary, key points, and a timestamped topic list as an HTML report |
| video-lens-gallery | 744 | Open or rebuild the gallery index of saved video summaries |
| video-lens-recs | 271 | Recommend YouTube videos worth watching on a topic, ranked with reasons |

No indexed listings fall below the 200-install threshold; all 3 appear above.

## Why This Matters for Hermes Agents

YouTube is a common research input for agents, and a link is far easier to pass than a video file. video-lens closes the gap by reading YouTube captions directly, so no audio download is needed for the common case. When captions are missing or blocked, it asks before falling back to local Whisper transcription, which keeps the cost and privacy profile predictable. The report format is structured rather than freeform: a summary, a takeaway, numbered key points, and a timestamped outline that jumps to the video on click. For an agent that maintains notes over time, the gallery turns one-off summaries into a searchable library, and recommendations feed the next watch decision. The trade-off is scope: it is a reader and organiser, so anything beyond summarising, filing, and recommending is out of bounds.

## Usage

| You say | What happens |
|---|---|
| Summarize this video, then paste a YouTube URL | Fetches the transcript and opens a report with summary, key points, and timestamped outline |
| /video-lens <url> in Spanish, focus on the pricing part | Generates the report in Spanish with focus on the pricing section |
| /video-lens-gallery | Opens the searchable gallery of every saved report |
| /video-lens-recs what's new in Rust this week | Recommends videos with reasons, skipping already-watched items |
| share this report | Creates an unlisted link on video-lens.org; unshare revokes it |
| This video has no captions | Asks before downloading audio and transcribing locally with Whisper |

## Verification

Confirm the README and the three skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/kar2phi/video-lens/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/kar2phi/video-lens/main/skills/video-lens/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/kar2phi/video-lens/main/skills/video-lens-gallery/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/kar2phi/video-lens/main/skills/video-lens-recs/SKILL.md | head -40
```

All four URLs return 200. After installing, confirm the three skill folders exist in your agent's skills directory and review each SKILL.md before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| video-lens | Pass | Pass | Warn |
| video-lens-gallery | Pass | Pass | Warn |
| video-lens-recs | Pass | Pass | Warn |

Across the 3 sampled skills there are 6 Pass, 3 Warn, and 0 Fail cells; every skill clears Gen Agent Trust Hub and Socket with a Warn on Snyk.

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,213 combined installs across 3 indexed listings; 142 GitHub stars; MIT license; last pushed Nov 20, 2026. Counts drift over time.
- This is a YouTube-link reader, not a general video editor; it does not cut, caption, or republish video.
- Local transcription (the captions fallback) requires mlx-whisper and ffmpeg on Apple Silicon; Windows support is best effort.
- YouTube Shorts are not supported.
- Reports and the gallery live on the local machine; nothing is uploaded unless the user asks to share, which publishes an unlisted link.

## Related

[YouTube Skills - Transcript API Suite for Agents](/hermes/skills/catalog/youtube-skills-setup) | [YouTube Clipper - AI Chaptering and Bilingual Cuts](/hermes/skills/catalog/youtube-clipper-skill-setup) | [Claude Video Watch Skill - Agent Video Input Setup](/hermes/skills/catalog/claude-video-watch-skill-setup) | [Herk Edit Kit - AI Video Editing Setup](/hermes/skills/catalog/herk-edit-kit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Pass the URL first and let the skill fetch captions; you do not need to download the video yourself.
- Keep the default venv path (~/.local/share/video-lens/venv) so the skill's packages never leak into system Python.
- Use the gallery to search saved reports instead of re-summarising the same video.
- Re-run setup.py with --upgrade when YouTube changes and an older release breaks.
- For videos without captions, expect a slower first run as Whisper downloads its model locally.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
