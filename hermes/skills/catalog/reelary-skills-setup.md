---
title: "Reelary Skills - Local Footage Search for Agents"
description: "reelary/skills - 6.8K combined installs across 6 indexed listings: local footage search and cut export for agents through the Reelary desktop app."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/reelary-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "video", "local", "search"]
---

# Reelary Skills - Setup Guide

**Source:** [reelary/skills](https://www.skills.sh/reelary/skills) via skills.sh - 6.8K combined installs across 6 indexed listings; first seen Nov 15, 2026 (Nov 15 evening sweep)
**GitHub:** 1 star, no LICENSE file, `main` branch, last pushed 2026-10-24, six `SKILL.md` files under `skills/`
**Category:** Local video search and cut export for agents
**Quality Tier:** 🟡 Yellow - no LICENSE file and one Snyk Warn in the sample.

Reelary indexes the videos and photos already on a Mac or Windows PC and lets agents search every frame by meaning and cut the matches into a video. The six skills are a client for the Reelary desktop application: indexing, search and cut export happen locally through that app, so nothing leaves the computer. The skills work with Claude Code, Cursor, Codex and 60+ other agents.

The first time an agent is asked about footage, it offers to install the Reelary app and connect it, so the skills are the interface and the app is the engine. A free plan covers indexing, visual search and rough cuts, while Pro unlocks dialogue search, people, places, NLE export and full-quality exports.

## Installation

```bash
npx skills add reelary/skills
```

Install one skill only:

```bash
npx skills add reelary/skills --skill find-footage
```

The skills need the Reelary application. On first use the agent offers to install the app and connect it, and indexing, search and cut export all run locally through that app.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| broll-finder | 1,154 | B-roll for a voiceover or interview. |
| vertical-video | 1,145 | Shorts, Reels and TikTok in 9:16 and 1:1. |
| rough-cut | 1,135 | Rough cuts, script-to-video, montages and highlight reels. |
| nle-export | 1,125 | FCPXML, XML and EDL exports for Premiere, Final Cut and Resolve. |
| find-footage | 1,125 | Shots by description, photos, quotes, people, places and drone GPS. |
| reelary | 1,103 | Start here: install, index folders and drives, troubleshoot. |

No indexed listings fall below the threshold; all 6 appear above.

## Why This Matters for Hermes Agents

Search over video is a task a text-trained agent cannot do on its own: it has no way to read the frames of an hour of footage. These skills hand that job to a local indexer, so an agent can answer "find where she talks about the budget" or "cut a 30-second recap" without shipping the footage anywhere. The privacy property is the point: everything runs locally.

The split of responsibilities is the second useful pattern. The skills are thin interfaces, and the Reelary app does the indexing, search and cut export. An agent should say plainly that the skills need the Reelary application, because the skills alone do nothing.

For a builder, the plan boundary is worth knowing: dialogue search, people, places and NLE export are Pro features behind a one-time purchase, while indexing, visual search and rough cuts are free.

## Usage

| You say | What happens |
|---|---|
| "Index ~/Movies and find drone shots of the coast" | The agent installs the app, indexes the folder and searches for matching shots. |
| "Find b-roll for this voiceover" | Uses broll-finder to surface b-roll for the voiceover or interview. |
| "Find where she talks about the budget" | Uses find-footage to locate the moment by dialogue search. |
| "Cut a 30-second 9:16 recap of my Lisbon trip" | Uses vertical-video to build a Shorts or Reels cut. |
| "Rough cut this script from my footage" | Uses rough-cut to assemble a script-to-video cut. |
| "Export for DaVinci Resolve" | Uses nle-export to write an EDL or XML the editor reads. |

## Verification

Check the skill files and install:

```bash
curl -fsSL https://raw.githubusercontent.com/reelary/skills/main/skills/reelary/SKILL.md | head -30
curl -fsSL https://raw.githubusercontent.com/reelary/skills/main/skills/find-footage/SKILL.md | head -30
npx skills add reelary/skills
```

The skills are the interface and the Reelary desktop app is the engine. Confirm the app is installed and connected before expecting search results, since indexing, search and cut export all run locally through it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-15) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| broll-finder | Pass | Pass | Pass |
| vertical-video | Pass | Pass | Pass |
| rough-cut | Pass | Pass | Pass |
| nle-export | Pass | Pass | Pass |
| find-footage | Pass | Pass | Pass |
| reelary | Pass | Pass | Warn |

The one Snyk Warn sits on the reelary entry skill, the one that drives the app install and connection.

## Limitations

- Snapshot data, verified 2026-11-15: 6,787 combined installs across 6 indexed listings; 1 GitHub star; no LICENSE file; last pushed 2026-10-24. Counts drift over time.
- The skills are a client for the Reelary desktop app; indexing, search and cut export do not run without that application installed.
- There is no LICENSE file, so treat the repository as unlicensed rather than open source until the author states otherwise.
- Dialogue search, people, places and NLE export are Pro features behind a one-time purchase; the free plan is indexing, visual search and rough cuts at 720p with a watermark, up to 60 seconds and five per month.
- One GitHub star means the project has essentially no community validation yet; the tier reflects a single-author collection.

## Related

- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)
- [Media Use Setup - Agent Media OS for HyperFrames (182.7K installs)](/hermes/skills/catalog/media-use-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the reelary entry skill; it drives install, folder indexing and troubleshooting.
- Say plainly that the skills need the Reelary application before claiming a search result.
- Keep the free plan in mind: dialogue search and NLE export are Pro features behind a one-time purchase.
- Ask for specific shots, not a topic, because the indexer matches meaning across frames.
- Prefer the local workflow for private footage; nothing leaves the computer by design.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
