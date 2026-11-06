---
title: "Sonilo Skills - Music, SFX and Dubbing for Video"
description: "sonilo-ai/skills on skills.sh: 7.1K combined installs across 16 listings; licensed music, sound effects, dubbing and ducking for finished video."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sonilo-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "audio", "music", "video"]
---

# Sonilo Skills - Setup Guide

**Source:** [sonilo-ai/skills](https://www.skills.sh/sonilo-ai/skills) via skills.sh - 7.1K combined installs across 16 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 117 stars, MIT, last pushed 2026-10-27, thirteen SKILL.md directories at the repository root, plus `.claude-plugin`, `AGENTS.md` and `CLAUDE.md`
**Category:** Audio for agents: licensed music scored to a finished video, sound effects, dubbing, ducking and playback
**Quality Tier:** 🟡 Review - MIT licensed and clean on Gen Agent Trust Hub and Socket, but auto-dubbing carries a Snyk Warn and every generation skill spends money per call.

Sonilo is a licensed audio API, and its flagship capability is the one the repository is named for: give it a finished video and it composes an original soundtrack matched to the cut, because the model watched the pacing, motion and emotion rather than reading a prompt. The same API covers sound effects matched to footage, dubbing into other languages, ducking a music bed under a voice track, and the pre-dubbing proofread step that produces editable subtitles first.

The repository holds thirteen skills, one per tool, installed either through the Agent Skills CLI or as a plugin. It also documents three ways to reach the API behind them: an MCP server running locally, a hosted MCP server with OAuth, and the official Python and JavaScript SDKs with a CLI. That matters because the skills are only instructions; the audio comes from whichever client you wired up.

## Installation

The Agent Skills CLI installs all thirteen for any compatible assistant:

```bash
npx skills add sonilo-ai/skills
```

Or a single skill, if you only want the video scoring half:

```bash
npx skills add sonilo-ai/skills --skill video-to-music
```

Claude Code users can take the same thirteen skills as a plugin. It is a skills-only plugin: it carries no MCP server and no bundled tools, so the connection below still applies.

```
/plugin marketplace add sonilo-ai/skills
/plugin install skills@sonilo-skills
```

The Muse Code and Cursor plugins differ: both also connect the hosted Sonilo MCP server at `https://api.sonilo.com/mcp`, so there is no key to paste and the first tool call asks you to sign in with a Sonilo Platform account. Muse plugin management sits behind `MUSE_EXPERIMENTAL_PLUGINS` as of Muse Code 1.4.0, though what it installs runs without the flag.

For the local MCP server, sign in once and let the server read the same credential:

```bash
npm install -g sonilo-cli && sonilo login
```

The README then registers the server with `claude mcp add sonilo` and the `uvx sonilo-mcp` launch command (the Codex equivalent is `codex mcp add sonilo` with the same launcher), so the host config holds no secret. Approving in the browser mints a 90-day key named after the host in `~/.config/sonilo/credentials.json`; `sonilo whoami` shows what is active and `sonilo logout` revokes it.

For CI, containers, or if you would rather hold a key, add the `--env SONILO_API_KEY=sk-...` flag ahead of that same launch command. The variable takes precedence over the sign-in wherever both exist.

## What It Provides

Five listings clear the 500-install threshold, and between them they cover scoring, sound design and localisation.

| Skill | Installs | Use For |
|---|---|---|
| video-to-music | 1,524 | Score a finished video with original music matched to pacing, motion and emotion, returned as audio or a new video with the score muxed in |
| video-to-sfx | 1,431 | Sound effects matched to footage (footsteps, impacts, ambience, foley), optionally scripted to timed segments |
| text-to-sfx | 1,422 | One sound effect from a text description alone, no video input |
| audio-ducking | 1,239 | Duck a music bed under a voice track, lowering it wherever the voice speaks and lifting it back in the gaps |
| auto-dubbing | 1,103 | Dub a video into one or more languages with re-voiced speech, optionally from your own per-language script, with a re-timed SRT back |

The remaining 11 indexed listings range from 11 to 74 installs: setup-api-key (74), audio-playback (71), account (40), video-to-sound (37), task-recovery (35), video-analysis (24), text-to-music (22), proofread (11), plus music (13), dubbing (13) and sound-effects (12), which are the pre-v2 names and have no directories in the current tree.

## Why This Matters for Hermes Agents

Audio is the last step of a video pipeline and the one agents most often fake. A generated video with no score reads as a draft, and the usual workaround, dropping a stock track under the cut, is the reason so much automated video sounds identical. Scoring to the actual motion is a different job, and it is one where the model seeing the video is the whole point.

The suite is built around a pre-flight discipline that fits agents well. The repository's own reference files put inspection, duration caps, credit checks and verification before any paid call, and the `account` skill exists so an agent can read `trial[service].remaining` and the usage history before spending. An agent that knows what a call costs and whether a free run is left behaves very differently from one that fires and reports.

Cost shape is documented per service rather than hidden. Dubbing bills per language and its one free run is a 15-second preview, so the skill tells the agent to confirm the language count with the user before calling. That is a small instruction with a large effect: a five-language dub is five charges, and a model that discovers this after the fact has already produced the invoice.

The supporting half is what makes the output usable. `proofread` transcribes and translates into editable `.srt` files, one per target language plus the detected source, so wording can be corrected before anything is dubbed and nothing is spoken yet. `video-analysis` returns a creative brief, a music section plan with ready-to-use prompts and a sound-design brief, instead of a track. `task-recovery` recovers a timed-out generation from its task id rather than paying twice.

There is also an explicit intent behind the naming. The v2 rename moved every skill to the name of the tool it documents, and the repository ships five trigger evals for the routing decisions that split put at risk, including the combined music plus SFX request that must reach `video-to-sound` instead of billing twice through the two separate skills.

## Usage

| You say | What happens |
|---|---|
| "Put music under this cut" | video-to-music watches the video, composes a licensed score matched to its pacing and emotion, and returns audio or a muxed video |
| "Add footstep and impact sounds to this footage" | video-to-sfx generates effects matched to the video, optionally pinned to timed segments |
| "I need a door creak, no video" | text-to-sfx generates one effect from the description alone |
| "The narration is drowning out the music" | audio-ducking lowers the music bed wherever the voice speaks and lifts it in the gaps |
| "Dub this into Spanish and German" | auto-dubbing translates and re-voices per language, and asks about language count first because each one bills |
| "Just give me subtitles to check first" | proofread transcribes, translates and writes editable `.srt` files per language without speaking anything |
| "What sounds should this scene have?" | video-analysis returns a sound-design brief and a music section plan with prompts, not a track |
| "What is left on my free trial?" | account reads available services, rate limits, trial allowance and usage history |

## Verification

Read the two skills that decide most of the spend before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/sonilo-ai/skills/main/video-to-music/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/sonilo-ai/skills/main/auto-dubbing/SKILL.md | head -20
```

The first should open with `name: video-to-music` and the description about scoring a finished video and handing text-only music to the `text-to-music` skill; the second with `name: auto-dubbing`, the per-language billing note and the 15-second preview. Both returned HTTP 200 on 2026-11-06.

The install command is also the check that the package resolves, since the skills are plain directories at the repository root:

```bash
npx skills add sonilo-ai/skills
```

Then confirm the credential the tools will use, whether it came from a sign-in or from `SONILO_API_KEY`:

```bash
sonilo whoami
```

The README documents that this shows what is active and `sonilo logout` revokes it, which is the fastest way to confirm an agent is not running on a 90-day key minted for a different host.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| video-to-music | Pass | Pass | Pass |
| auto-dubbing | Pass | Pass | Warn |
| video-to-sound | Pass | Pass | Pass |
| music | Pass | Pass | Pass |
| proofread | Pass | Pass | Pass |

The sampled set is clean except for one Warn, on `auto-dubbing`, and that is the skill that both re-voices speech and bills per language. The warning is worth reading on skills.sh rather than assuming, but the operational risk it points at is clear enough: it is the skill most likely to spend money and the one that produces a synthetic voice saying things the user did not write.

Credentials deserve the same attention. A `sonilo login` mints a 90-day key in `~/.config/sonilo/credentials.json`, and `SONILO_API_KEY` takes precedence wherever both exist, so a stale environment variable can silently override a sign-in an operator believes is current. The hosted MCP server avoids the local key entirely by using OAuth against a Sonilo Platform account, which is a smaller secret footprint if you do not need local execution.

The data question is inherent to the product: every generation skill uploads the video or the prompt to a hosted API. That is the service, and it is still the thing to check against your own footage rules before an agent is pointed at client material.

Licensing is the bright spot. Audio generated through the API can be used commercially, in your own product and by your end users, including ads, client work and monetized channels, and it is billed pay-as-you-go from a prepaid balance rather than through a consumer subscription. The stated exceptions are film, TV and broadcast use, and releasing tracks to streaming services, which need sales contact first.

## Limitations

- Snapshot data, verified 2026-11-06: 7,071 combined installs across 16 indexed listings; 117 GitHub stars; MIT; last pushed 2026-10-27. Counts drift over time.
- Sixteen indexed listings against thirteen directories. `music`, `dubbing` and `sound-effects` still carry install counts but were renamed in v2 and no longer exist, so an agent that installs from those names gets nothing. The README's own advice is to reinstall under the new names.
- Everything that generates audio is paid. Self-serve accounts get a few free runs per service, dubbing's free run is a 15-second preview, and the rest bills from a prepaid balance. An agent that skips the `account` check can spend without warning.
- The Claude Code plugin is skills-only. It carries no MCP server and no tools, so the hosted or local connection still has to be configured separately, which is a common source of "the skill is installed and nothing happens".
- Commercial terms have edges. Film, TV and broadcast use, and releasing tracks to Spotify, Apple Music or other streaming services, require contacting sales first.
- The bundled trigger evals are early-access gated in Claude Code and routing-only. They check that the right skill fires, not that the call produces correct audio, and the README says functional evals are still open.

## Related

- [Songwriting & AI Music - Creative Music Generation Setup](/hermes/skills/catalog/songwriting-and-ai-music-setup)
- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `account` first on a new install. It reports the trial allowance per service, and knowing whether a free run is left changes how much an agent experiments.
- Proofread before dubbing. The `.srt` pass costs far less than re-voicing and it is the only point where the translated wording is cheap to correct.
- State the language count before an auto-dubbing call. Billing is per language, and the skill is written to confirm rather than assume.
- Use `video-to-sound` when a video needs both music and effects. It is a single balanced call, and the repository's evals exist specifically because routing that request to two skills bills twice.
- Keep `sonilo whoami` in your checks. A 90-day key or a leftover `SONILO_API_KEY` can outlive the project it was minted for, and this is the one command that shows which is active.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
