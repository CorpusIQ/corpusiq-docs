---
title: "BibiGPT Skill - Video Summary for Agents Setup"
description: "jimmylv/bibigpt-skill: 2.1K combined installs across 4 listings, four agent skills fronting the hosted BibiGPT video and audio summarizer service."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jimmylv-bibigpt-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "video", "transcription", "mcp", "youtube"]
---

# BibiGPT Skill - Setup Guide

**Source:** [jimmylv/bibigpt-skill](https://www.skills.sh/jimmylv/bibigpt-skill) via skills.sh - 2.1K combined installs across 4 indexed listings; first seen Nov 13, 2026 (evening sweep)
**GitHub:** 141 stars, MIT licence, `main` branch, last pushed 2026-11-13, four SKILL.md files under `skills/<name>/SKILL.md`
**Category:** Video and audio summarization for agents: YouTube, Bilibili, podcasts and local files
**Quality Tier:** 🟠 Orange - all four sampled skills fail the Gen Agent Trust Hub, with Socket or Snyk warns on three.

This pack is a front end to BibiGPT, a paid third-party summarization service, not a self-contained summarizer. The four skills route requests to the hosted MCP server at `https://bibigpt.co/api/mcp` or to the `bibi` CLI, both of which need a BibiGPT account and sign-in (or an API key). Video URLs and file content you summarize are sent to BibiGPT's servers, so the data leaves your machine.

Read the security verdicts before anything else. All four sampled skills fail the Gen Agent Trust Hub, and three carry Socket or Snyk warns. That is the single most important fact about this pack, and it is repeated in Security below.

## Installation

The shortest path adds the hosted MCP server once, then asks for a summary in plain words. The first call opens a browser for BibiGPT sign-in (OAuth), so no API key is pasted.

```bash
# Claude Code: add the hosted MCP server
claude mcp add --transport http bibigpt https://bibigpt.co/api/mcp

# Or install the plugin (MCP server plus all four skills)
/plugin marketplace add JimmyLv/bibigpt-skill
/plugin install bibi@bibigpt

# Or install the skills via skills.sh
npx skills add JimmyLv/bibigpt-skill
```

For Cursor, add the server to `.cursor/mcp.json`:

```json
{ "mcpServers": { "bibigpt": { "url": "https://bibigpt.co/api/mcp", "type": "streamable-http" } } }
```

The CLI is a separate path. Install the desktop app, then sign in:

```bash
curl -fsSL https://bibigpt.co/install.sh | bash
bibi auth login
```

Both paths need a BibiGPT account. The API-key path (Bearer token, issued at bibigpt.co/user/integration) skips OAuth for the CLI and direct HTTP calls.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| bibi | 1,924 | Summarize a video, podcast or local file: transcript, chapter breakdown and a short summary, plus optional vertical-video remix. |
| bibi-vision | 69 | Extract slides, OCR and on-screen text from a video, and build an XMind mind map from a saved summary. |
| bibi-library | 68 | Browse, search and organize already-summarized videos, notes and collections. |
| bibi-feed | 68 | Subscribe to channels, pull the latest feed and mark items seen. |

No indexed listings fall below the 60-install threshold; all four appear above.

## Why This Matters for Hermes Agents

The skills give an agent a clean, one-command route from a video URL to a timestamped transcript, a chapter-by-chapter summary and a short takeaway, and the work runs server-side so the agent does not need ffmpeg or whisper installed locally.

That convenience has a cost. Summarization happens on BibiGPT's servers, so the URL and any local file you point at it leave the machine. For an agent that handles meeting recordings or internal material, that is a data-boundary decision to make before the first call.

The bibi skill is a router: it hands library lookups, channel feeds and visual analysis to its three siblings, so each skill stays narrow and the intent detection has fewer false matches.

The hosted-MCP design also means the tool list updates server-side. The agent does not fetch new tools until its MCP client restarts, which matters when a new tool appears and the agent keeps answering from an old cache.

## Usage

| You say | What happens |
|---|---|
| "Summarize this video: https://www.youtube.com/watch?v=xxxxx" | Calls the summarize_video tool and returns a summary plus a chapter breakdown. |
| "Get the timestamped transcript for this podcast episode" | Calls get_subtitle and returns subtitles with timestamps. |
| "What did I already save about this topic?" | Runs bibi-library and searches the saved summaries, notes and collections. |
| "Subscribe to this channel and give me the latest" | Runs bibi-feed and pulls the newest items, marking them seen. |
| "What is on screen in this video, and make a mind map" | Runs bibi-vision to OCR frames and slides, then builds an XMind map. |
| "Summarize this long lecture in the background" | Creates an async summary task and returns a status the agent can poll. |

## Verification

Probe two skills on the branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/JimmyLv/bibigpt-skill/main/skills/bibi/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/JimmyLv/bibigpt-skill/main/skills/bibi-library/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/JimmyLv/bibigpt-skill/main/skills/bibi-vision/SKILL.md
```

The four skills live under `skills/<name>/SKILL.md`. The bibi skill also ships `scripts/bibi-check.sh`, which auto-detects CLI versus API mode.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bibi | Fail | Warn | Warn |
| bibi-vision | Fail | Pass | Warn |
| bibi-library | Fail | Pass | Pass |
| bibi-feed | Fail | Pass | Warn |

Every sampled skill fails the Gen Agent Trust Hub, and bibi, the most installed skill in the pack, also carries Socket and Snyk warns. Those are failing verdicts, not missing ones, and they are the first thing to read before installing.

Beyond the verdicts, this pack is a front end to a paid third-party service. Summarization runs on BibiGPT's servers, so any URL, transcript request or local file you hand it leaves your machine. Do not point it at internal or confidential material.

That does not make the skills unsafe for public videos, but it does change the trust model versus a local summarizer: you are trusting BibiGPT with your content and your account, on top of whatever the skills.sh auditors flagged.

## Limitations

- Snapshot data, verified 2026-11-13: 2,129 combined installs across 4 indexed listings; 141 GitHub stars; MIT licence; last pushed 2026-11-13. Counts drift over time.
- This is not a self-contained summarizer. Every skill depends on the BibiGPT hosted service or the bibi CLI, which requires a BibiGPT account (sign-in or API key). Without that account nothing summarizes.
- Summarization is a paid service and data leaves the machine. The URL or file you submit is processed on BibiGPT's servers, so keep internal material off it.
- All four sampled skills fail the Gen Agent Trust Hub, and three carry Socket or Snyk warns. Treat the failing verdicts as the headline, not a footnote.
- The hosted MCP tool list is served remotely. The agent does not pick up new tools until its MCP client restarts.
- The bibi skill has a broad remit (YouTube, Bilibili, TikTok, X, Xiaohongshu, podcasts, local files); its accuracy depends on BibiGPT's platform support, which can change.

## Related

- [YouTube Skills - Transcript API Suite for Agents](/hermes/skills/catalog/youtube-skills-setup)
- [Claude Video Watch Skill - Agent Video Input Setup](/hermes/skills/catalog/claude-video-watch-skill-setup)
- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use the hosted MCP server first. It has nothing to install, and the first OAuth sign-in is the whole setup. The skills are optional sugar on top.
- Read skills/bibi/SKILL.md before wiring the API-key path into CI or a container. A Bearer token in an environment variable is a secret, not a config line.
- Keep internal meetings off it. Route public YouTube and Bilibili links through bibi, and use a local tool for anything confidential.
- Restart the MCP client after BibiGPT ships new tools; the server updates remotely but the client's tool cache does not.
- Remember the tier. The Orange verdict and four Gen Agent Trust Hub failures are the reason to review before production use, not a reason to skip it silently.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
