---
title: "PostPlus Skills - Marketing Research and Publishing"
description: "postplusai/postplus-skills: 46.5K combined installs across 82 listings; marketing skills for platform research, ad briefing and channel publishing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/postplus-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "marketing", "social media"]
---

# PostPlus Skills - Setup Guide

**Source:** [postplusai/postplus-skills](https://www.skills.sh/postplusai/postplus-skills) via skills.sh - 46.5K combined installs across 82 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 27 stars, NOASSERTION (a LICENSE file is present but the licence is not identified), last pushed 2026-10-31, 27 SKILL.md directories
**Category:** Marketing for agents: platform research, asset routing and campaign publishing across social channels
**Quality Tier:** 🟡 Three of the five sampled listings carry a Snyk warning, and the licence reads NOASSERTION rather than a named open licence

PostPlus is a marketing skill pack organised in numbered stages rather than by platform: `00-shared`, `10-routing`, `20-research`, `30-measurement`, `40-creative`, `50-publishing` and `60-ads`. The README states the interface plainly. You describe the marketing result you want, the agent selects the specific skill, uses the evidence and inputs you provide, and returns a usable result, and you do not need to learn skill names first.

The pack is delivered by its own CLI rather than as a folder of Markdown you copy: the installer prepares PostPlus and a dedicated runtime, and the CLI ships a bundled catalog of skills which it verifies against what is actually installed. Cloud tasks need a connected account, channel connections belong to your personal account, and publishing, replacing business content, new subscriptions and external ad spend require authorization before the agent proceeds.

## Installation

The README points at an installation guide rather than a command, and the installer prepares its own runtime without changing the Node.js already on the machine:

```bash
# follow the official guide the README links
# https://postplus.io/postplus-agent-install.md
postplus list
postplus install --current-directory
```

`postplus install --current-directory` is the project-only installation the README documents. After install, use the command path the installer returned for the current session and continue the original task; new shells pick up the registered `postplus` command. The README is explicit that correct installations are reused and that you should not run a separate skills installer afterwards, which includes the generic skills.sh one-liner, because the CLI derives available skills from its bundled catalog and checks the installed content itself.

Channel access is a separate step and a browser step for you, not for the agent:

```bash
postplus channels list
postplus channels connect google-ads
postplus channels tools list --toolkit googleads
postplus auth login
```

The README says to run `postplus auth login` when the CLI asks for it and to approve the real browser connection yourself, and never to share credentials with the agent. A listed tool does not prove your account has the platform permissions to use it, so the connection check comes before the task, not after it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| audio-transcription | 1,320 | Turning a recorded voice or track into text; the folder sits at `skills/40-creative/audio-transcription`. |
| video-transcription | 1,241 | Word-level text from a video file, which is the input for subtitles and shot notes. |
| google-trends-research | 1,180 | Sizing demand for a topic over time before any campaign is planned. |
| facebook-research | 1,119 | Reading Facebook pages and ad activity for a market. |
| youtube-research | 1,106 | Reading YouTube channels and videos as reference material. |
| video-analysis | 1,074 | Breaking a video into its parts for a brief; indexed on skills.sh, and no folder of this name appears in the 27-directory layout, where `media-analysis` occupies the analysis slot. |
| tiktok-research | 1,065 | Reading TikTok content and its patterns for a market. |
| postplus-shared | 1,039 | The shared rules and evidence handling the other skills read; indexed on skills.sh, while the layout's shared slot is `00-shared/postplus-workspace`. |
| benchmark-to-brief | 1,037 | Turning competitor benchmarks into a written brief a build can follow. |
| social-media-publisher | 1,034 | Publishing a finished asset to a channel; indexed, with no folder of this name in the layout, where `50-publishing` holds `social` and `channel-messaging`. |
| reference-decode | 1,032 | Decoding a reference video or post into the elements a build should reproduce; the folder sits at `skills/10-routing/reference-decode`. |
| image-batch-runner | 1,032 | Running a batch of image generations from one spec. |
| editing-decision-engine | 1,029 | Deciding cut order and pacing for a set of clips; indexed, with no folder of this name in the layout. |
| video-batch-runner | 1,023 | Running a batch of video generations from one spec. |
| social-media-extractor | 1,013 | Pulling the assets and copy out of a social post; indexed, with no folder of this name in the layout. |
| subtitle-packager | 1,009 | Packaging subtitles into uploadable files; indexed, with no folder of this name in the layout. |
| voice-batch-runner | 1,008 | Running a batch of voice generations from one spec; indexed, with no folder of this name in the layout. |
| sourcing-selection | 1,008 | Choosing which sourced clips and images make the cut; indexed, with no folder of this name in the layout. |
| creative-qa | 998 | A quality pass over creative before it goes out; indexed, with no folder of this name in the layout. |
| media-router | 992 | Routing a request to the right media skill; indexed, while `10-routing` in the layout carries `image-generation` and `reference-decode`. |

The remaining 62 indexed listings range from 1 to 968 installs.

The layout is complete at 27 `SKILL.md` directories, so the ten table rows without a matching folder are indexed names the repository tree does not carry. That is consistent with how the pack ships: the CLI installs from its bundled catalog, and the tree is not the source of truth for what runs.

## Why This Matters for Hermes Agents

Marketing requests arrive as outcomes, not as skill names: review Meta ad performance, prepare a Facebook Page post, adapt a video for Instagram and TikTok. A pack that routes on the outcome lets an agent take that sentence and find the work, which is the difference between an assistant that needs a manual and one that can be handed a task. The numbered stages give the routing somewhere to land, research before creative, creative before publishing, publishing before ads.

The evidence rule is the part worth copying into other stacks: the README's framing is that the agent uses the evidence and inputs you provide, and the named skills include a reference decoder, a benchmark-to-brief step and a creative QA pass. That sequence keeps a campaign grounded in something that exists rather than in what a model remembers about a market.

Publishing is treated as a permissioned action rather than a finishing step, and the README separates estimate-only requests, which do not execute, from work that spends credits. For an agent running unattended, that split is what makes a marketing pack safe to schedule: the read and draft work can run on its own, and the write work waits for a human.

The channel model also matters for a multi-tenant setup, because connections belong to a personal account rather than to a workspace, a teammate's subscription does not cover you, and disconnecting one affects every workspace that uses it, so an agent should check connection status before continuing rather than assuming a channel is live.

## Usage

| You say | What happens |
|---|---|
| "What is trending for running shoes this month?" | google-trends-research sizes the topic over time, then the brief skills turn the trend into something a creative step can use. |
| "Break down this competitor TikTok and tell me why it works" | tiktok-research with reference-decode reads the post for its structure, and video-analysis names the parts if no tree folder matches. |
| "Turn these three competitor ads into a brief" | benchmark-to-brief writes the brief, with reference-decode supplying the elements to reproduce. |
| "Make five UGC style ads from this product photo" | image-batch-runner or video-batch-runner runs the batch, with creative-qa checking the set before anything is published. |
| "Add subtitles to this video and package them for upload" | video-transcription produces the text and subtitle-packager prepares the files; audio-transcription covers voice-only input. |
| "Post this to our Facebook Page and Instagram" | social-media-publisher takes the asset, but publishing needs your authorization and a live channel connection before it executes. |
| "Check our Google Ads performance for last month" | The ads stage reads the connected account through `channels tools`, after `postplus channels list` confirms the connection. |

## Verification

The raw path below was built from the repository layout on branch main. Probe it before installing, and expect an HTTP 200:

```bash
curl -sL -o /dev/null -w "%{http_code} audio-transcription\n" \
  "https://raw.githubusercontent.com/postplusai/postplus-skills/main/skills/40-creative/audio-transcription/SKILL.md"
```

Installed content is confirmed through the CLI, which verifies what it wrote rather than trusting a listing:

```bash
postplus list
postplus channels list
postplus install --help
```

`postplus list` prints the tasks the CLI believes it can handle from its bundled catalog, and `channels list` shows which channels are actually connected. A skill appearing in `postplus list` is a claim about the install, not about your account permissions, so check the channel side before planning work that publishes.

If you cloned the repository to inspect it, count the tree instead of trusting the index, since the CLI ships its own catalog:

```bash
git clone --depth 1 https://github.com/postplusai/postplus-skills.git /tmp/postplus-skills
find /tmp/postplus-skills/skills -name SKILL.md | wc -l
```

The count should be 27.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| audio-transcription | Pass | Pass | Warn |
| frame-extraction | Pass | Pass | Warn |
| lifestyle-ad | Pass | Pass | Pass |
| x-research | Pass | Pass | Warn |
| seo-geo | Pass | Pass | Warn |

Every sampled listing passes Gen Agent Trust Hub and Socket, and four of five carry a Snyk warning, so the warnings cluster on one auditor rather than across all three. Read the individual security pages before a run that transcribes or publishes: a transcription skill uploads your media to a service, and a publishing skill acts on a live account.

The licence is the second open question. The repository has a LICENSE file but GitHub classifies it as NOASSERTION, which means the terms could not be identified automatically, so treat redistribution as unresolved until you read that file. The bigger surface is credentials: the README says never to share them with the agent and to approve browser connections yourself, and that instruction should be enforced by the operator rather than left to the model.

## Limitations

- Snapshot data, verified November 3, 2026: 46,456 combined installs across 82 indexed listings; 27 GitHub stars; NOASSERTION licence; last pushed 2026-10-31. Counts drift over time.
- The licence is NOASSERTION, so the terms are not established by the repository metadata and a fork needs a human read of the LICENSE file.
- Ten of the twenty table rows have no matching folder in the 27-directory layout, so the tree is not a complete picture of what the CLI installs.
- There is no GitHub repository description, and the README does not enumerate skills, which is deliberate: capability discovery happens through `postplus list` on an installed CLI.
- Cloud tasks, channel connections and publishing need an eligible subscription on your own account, and a teammate's subscription does not cover you.
- The install path is a dedicated runtime prepared by the PostPlus installer rather than a plain skill folder, so it does not drop into a Hermes profile the way a Markdown pack does.

## Related

- [Apidojo Social Media Skills - X/Instagram/TikTok Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)
- [Blacktwist Social Media Skills - 14-Skill Content Suite Setup](/hermes/skills/catalog/blacktwist-social-media-skills-setup)
- [Charlie Hills Social Media Skills - 17-Skill Content System Setup](/hermes/skills/catalog/charlie-hills-social-media-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the outcome sentence, not a skill name. The pack is built for that interface, and naming a skill you half remember sends the request down the wrong stage.
- Do the research stage before the creative stage. A brief built from google-trends-research and a decoded reference produces far fewer rewrites than one built from a prompt alone.
- Keep the estimate and the execute separate. The README treats estimate-only requests as non-executing, so ask for the estimate first and approve the spend as a second decision.
- Check `postplus channels list` at the start of any publishing run. A disconnected channel fails late, after the creative work is already paid for.
- Never let the agent hold credentials. The README requires you to approve the browser connection, and the authorization prompts for publishing and ad spend are the controls that make scheduled runs safe.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
