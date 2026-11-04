---
title: "HeyGen Skills - Avatar Video Production Setup"
description: "heygen-com/skills: 20.2K combined installs. Avatar creation, scripted video generation and translation through the HeyGen v3 pipeline."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/heygen-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "avatar video", "text to speech", "video translation"]
---

# HeyGen Skills - Setup Guide

**Source:** [heygen-com/skills](https://www.skills.sh/heygen-com/skills) via skills.sh - 20.2K combined installs across 15 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 538 stars, license MIT, last pushed 2026-07-14, 4 SKILL.md directories
**Category:** Avatar video for agents: creator avatars, scripted video generation and translation through the HeyGen v3 pipeline
**Quality Tier:** 🟡 Yellow - MIT, 538 stars and a genuine install spec, but only one of the five sampled listings passes all three auditors and the other four carry Snyk warnings

HeyGen publishes this repository as AI agent skills for creating avatar videos, described in the README as giving an agent a face, a voice, and the ability to send video like a message. It works with Claude Code, OpenClaw, Codex, Cursor and other coding agents.

The tree ships three skills, `heygen-avatar`, `heygen-video` and `heygen-translate`, plus a fourth `SKILL.md` under `platforms/nanoclaw/heygen` for that platform. skills.sh indexes 15 listing names against those four directories, so most of the table below is listing names without a folder of their own. The README is explicit that the repository ships three skills and that the three are auto-discovered at `heygen-avatar/SKILL.md`, `heygen-video/SKILL.md` and `heygen-translate/SKILL.md` after a clone.

## Installation

The README's preferred path is to paste a prompt into the agent rather than run commands, because the install spec lives in the repository:

```text
Read https://raw.githubusercontent.com/heygen-com/skills/master/INSTALL_FOR_AGENTS.md and follow it.
Ask me for any API keys you need.
```

That document is what clones the repository, asks for the key, picks a transport, runs a verify test and ends with a working video. The manual routes the README lists alongside it:

```bash
gh skill install heygen-com/skills heygen-avatar
gh skill install heygen-com/skills heygen-video
gh skill install heygen-com/skills heygen-translate
```

`gh skill install` requires GitHub CLI v2.90 or newer and writes to the directory your agent reads. The README's other three routes are ClawHub (`clawhub install heygen-skills`), an OpenClaw plugin that bundles MCP support (`openclaw plugins install clawhub:@heygen/openclaw-plugin-heygen`), and a plain clone into `~/.claude/skills/heygen-skills` or `~/.openclaw/workspace/skills/heygen-skills`. For a Hermes profile, the clone route maps onto the profile skills directory:

```bash
git clone --single-branch --depth 1 https://github.com/heygen-com/skills.git /tmp/heygen-skills
cp -R /tmp/heygen-skills/heygen-avatar /tmp/heygen-skills/heygen-video /tmp/heygen-skills/heygen-translate ~/.hermes/profiles/corpusiq/skills/
```

Three steps follow the clone. Generate an API key at app.heygen.com/api, install the CLI with `curl -fsSL https://static.heygen.ai/cli/install.sh | bash`, then export `HEYGEN_API_KEY` in the shell or in a shell profile so it survives the session. The README verifies with `heygen --version` and `heygen auth status`, and notes that the CLI is a single static binary with no runtime dependencies. It also documents a remote MCP alternative that uses OAuth and needs no API key when a HeyGen plan with credits is already in place; the skills auto-detect MCP when no key is set.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| heygen-video | 3,133 | Scripted video generation through the v3 Video Agent pipeline; one of the three shipped skill directories. |
| heygen-avatar | 2,736 | Building the agent's own creator avatar from identity files, then reusing it across videos; a shipped directory. |
| heygen-translate | 2,140 | Translating and re-voicing an existing video into another language; a shipped directory. |
| heygen | 1,655 | Listing name for the HeyGen platform surface. No directory of its own; the shipped path is the `platforms/nanoclaw/heygen` tree. |
| text-to-speech | 1,189 | Speech synthesis as a standalone listing. No directory in the tree; voice work runs through the video and avatar skills. |
| video-translate | 1,154 | Second translation listing alongside heygen-translate, which is the shipped directory. |
| video-understand | 1,088 | Understanding an uploaded video. No directory in the tree and no matching capability in the README's three-skill list. |
| video-edit | 1,029 | Editing an existing video. No directory of its own; the nearest shipped skill is heygen-video. |
| avatar-video | 994 | Avatar video as a combined listing. The two shipped halves are heygen-avatar and heygen-video. |
| ai-video-gen | 987 | Generic generation listing with no directory; heygen-video is the shipped entry point for generation. |
| create-video | 945 | Another generation alias with no directory of its own. |
| video-download | 930 | Retrieving a finished render. No directory in the tree; the README's flow ends by delivering a share link. |
| visual-style | 921 | Style selection for a render. The README describes the video skill picking the best style, with no style skill of its own. |
| faceswap | 903 | Face replacement listing with no directory in the tree and no mention in the README's skill list. |
| heygen-skills | 381 | The ClawHub package name for the whole set, not a capability; it is the string `clawhub install` takes. |

All 15 indexed listings appear in the table above.

The gap between 15 listing names and four directories is the main thing to read here. Three of the fifteen, `heygen-video`, `heygen-avatar` and `heygen-translate`, are real skill folders that the README documents and auto-discovers. `heygen-skills` is the bundle name. The remaining eleven are index aliases around the same three capabilities, several in near-duplicate pairs: `video-translate` against `heygen-translate`, `avatar-video` against `heygen-avatar`, and `create-video`, `ai-video-gen` and `heygen-video` all pointing at generation.

## Why This Matters for Hermes Agents

A link is not a deliverable in most agent workflows, and video is the format that changes that. This pack turns a script into a rendered file with a face and a voice, which is the difference between an agent that drafts a launch announcement and one that ships it. The README's framing is blunt about the intended use: send video like a message.

The install pattern is worth stealing even if you never make an avatar. One prompt tells the agent to fetch `INSTALL_FOR_AGENTS.md` and follow it, and that file holds the clone path, the key prompt, the transport choice and a verify step. The install logic lives in the repository, so it can be corrected without asking every user to re-paste new instructions. For a builder shipping skills to other agents, that is a better contract than a README full of commands that go stale.

The three skills divide cleanly by job. `heygen-avatar` builds the identity asset once, `heygen-video` turns a script into a render, and `heygen-translate` re-voices an existing video into another language. An agent can plan those as three steps with an artifact between each, which is far easier to retry than one opaque generate call.

Two transports are supported, and the choice matters operationally. An API key is a static secret in the environment; the MCP route is OAuth against an existing plan. The skills auto-detect MCP when no key is present, so a profile can move between the two without editing skill files.

## Usage

| You say | What happens |
|---|---|
| "Create your own avatar and make a 30-second intro video" | heygen-avatar reads the agent's identity files, asks only what is missing and builds the avatar, then heygen-video renders the intro. |
| "Turn this blog post into a two-minute avatar video" | heygen-video takes the script through the v3 pipeline, generates the render and returns a share link. |
| "Dub this video into Spanish with my own voice" | heygen-translate translates and re-voices the existing video instead of regenerating it. |
| "Make a video of me presenting this deck" | heygen-avatar supplies the creator avatar and heygen-video drives the script and delivery. |
| "Check whether my HeyGen key is working" | The agent runs `heygen auth status` and reports the transport in use, API key or MCP. |
| "Use my HeyGen plan over OAuth, I have no API key" | The skills detect no key, fall back to the remote MCP server and authenticate through OAuth. |
| "Generate the same video in English and German" | heygen-video renders the source, then heygen-translate produces the German variant from it. |

## Verification

The raw path below is built from the layout in this pack and returned 200 on branch master when this guide was written on 2026-11-03. Note the branch, which is `master` for this repository rather than `main`:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  "https://raw.githubusercontent.com/heygen-com/skills/master/heygen-video/SKILL.md"
```

After a clone, confirm the directory count and the install spec the README tells agents to fetch, then check the CLI and the credential separately:

```bash
git clone --single-branch --depth 1 https://github.com/heygen-com/skills.git /tmp/heygen-skills
find /tmp/heygen-skills -name SKILL.md | wc -l
ls /tmp/heygen-skills/INSTALL_FOR_AGENTS.md
heygen --version && heygen auth status
```

The count should be 4, matching the pack layout: the three top-level skills plus `platforms/nanoclaw/heygen`. The second command confirms the install spec exists, because the paste-in install prompt fails silently if that file is missing. The last line separates the two failure modes that look identical in a render error: a CLI that is not installed, and a CLI that is installed but unauthenticated.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| heygen-video | Pass | Pass | Pass |
| heygen | Pass | Pass | Warn |
| video-edit | Pass | Pass | Pass |
| video-download | Pass | Pass | Warn |
| heygen-skills | Pass | Pass | Warn |

One of the five sampled listings passes all three auditors. `heygen-video`, the skill that does the actual generation, is the clean one, which is reassuring for the core path. The three warnings cluster on `heygen`, `video-download` and `heygen-skills`, and the first of those is the listing with no directory of its own, so a warning on it does not map to a folder you can read.

The install path deserves its own note. The README asks you to paste a prompt that tells an agent to fetch a remote Markdown file and follow it, which is convenient and also the widest grant in this pack: the agent clones a repository, asks for a key and runs a verify. A remote install spec can change after you read it, so pin it if that matters to you, or take the manual route and read the three `SKILL.md` files before installing.

The credential is a real one. A HeyGen API key bills a paid account, and the README's own instruction is to export it into a shell profile, where it persists for every later session. The MCP route exists precisely to avoid that: OAuth against the plan, no long-lived key in the environment. Either way, video generation spends credits, so an agent with this skill and no budget ceiling can spend real money one render at a time.

## Limitations

- Snapshot data, verified November 3, 2026: 20,185 combined installs across 15 indexed listings; 538 GitHub stars; license MIT; last pushed 2026-07-14. Counts drift over time.
- 15 indexed listing names behind four skill directories. Only `heygen-video`, `heygen-avatar` and `heygen-translate` are documented, auto-discovered skills, and several listings are near-duplicates of one another.
- `video-understand` and `faceswap` have no directory in the tree and no entry in the README's three-skill list. Treat them as index artifacts rather than capabilities until the repository shows otherwise.
- The paste-in install prompt fetches a remote spec from the `master` branch, so the commands it runs are not fixed at the moment you read the README.
- Avatar video spends account credits. The README documents no budget guard, and the CLI auth check tells you the key works, not what it will cost.
- Face and voice generation is a likeness and consent question before it is a technical one. Nothing in the repository states a consent policy for building a face from identity files.

## Related

- [ai-video-generation - AI Video Production (196K installs)](/hermes/skills/catalog/ai-video-generation-setup)
- [Noiz AI Skills - Voice and Speech for Agents](/hermes/skills/catalog/noizai-skills-setup)
- [ByteDance MediaKit CLI - Video Processing Setup](/hermes/skills/catalog/mediakit-cli-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the MCP route if you already pay for HeyGen. It authenticates by OAuth and keeps a billable API key out of your shell profile.
- Run `heygen auth status` before you debug a failed render. Auth failures and generation errors return the same kind of message, and the status call settles which one you have.
- Build the avatar once and reuse it. `heygen-avatar` is the slow step, and rendering from an existing avatar is what makes a five-video series practical.
- Translate rather than regenerate when you need another language. `heygen-translate` works from the finished video, so the picture and timing stay fixed while the audio changes.
- Copy only the three skill folders into a profile. The `platforms/nanoclaw` tree is for that platform, and pulling it in adds a duplicate `heygen` skill you will not call.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
