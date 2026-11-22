---
title: "VoiceStudio Skills - Local Voice Platform Setup"
description: "debpalash/voicestudio: open-source local voice cloning, dubbing and transcription skills plus an MCP server - 5.7K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/voicestudio-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "voice", "tts", "audio"]
---

# VoiceStudio Skills - Local Voice Platform Setup

**Source:** [debpalash/voicestudio](https://www.skills.sh/debpalash/voicestudio) via skills.sh - 5.7K combined installs across 6 indexed listings; first catalogued Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [debpalash/voicestudio](https://github.com/debpalash/voicestudio) - 116,057 stars, AGPL-3.0, main branch, last pushed Nov 22, 2026; skills live under `skills/voicestudio` and `skills/voicestudio-maintainer`, with dev skills under `.agents/skills/` and a legacy entry under `.claude/skills/`, plus an MCP server at `backend/mcp_server.py`.
**Category:** Local AI Voice and Speech Platform
**Quality Tier:** 🟢 Green - no Fail cells in the 6-skill sample: Gen Agent Trust Hub and Socket Pass on all six, Snyk Warn on voicestudio-maintainer, omnivoice and oss-maintainer.

VoiceStudio is debpalash's open-source, fully-local voice platform and an ElevenLabs alternative: voice cloning, voice design, video dubbing, dictation, transcription and audiobook creation in 646 languages, running on device with no account. The repository ships two agent skills aimed at different jobs: voicestudio drives audio work through the app's REST API or MCP server, and voicestudio-maintainer handles repository maintenance such as issue triage, contributor PR review, CI diagnosis and release prep.

The skills.sh index lists six names, but the install counts are concentrated on the two lead skills. voicestudio carries 3,832 installs and voicestudio-maintainer 1,626; omnivoice sits at 158, while oss-maintainer (75), vite (3) and fastapi-python (3) are a long tail. The repository is large and actively maintained, with 116,057 GitHub stars and a push on Nov 22, 2026.

## Installation

The README installs the agent skills through the skills CLI, pointing it at the repository:

```bash
npx skills add debpalash/VoiceStudio
```

To install one skill, pass `--skill` with `voicestudio` for audio work or `voicestudio-maintainer` for repository maintenance:

```bash
npx skills add debpalash/VoiceStudio --skill voicestudio
```

The voicestudio skill talks to the running app, so install the app first with the one-command installer (Linux, macOS, Windows, Docker and other platform installs are in the README):

```bash
curl -fsSL https://voicestudio.sh/install | sh
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| voicestudio | 3,832 | generate local speech with saved or designed voices, transcribe audio, and automate dubbing or narration through the REST API or MCP server |
| voicestudio-maintainer | 1,626 | triage GitHub issues, review contributor pull requests, diagnose CI, and prepare releases for the Electron app and Python backend |
| omnivoice | 158 | legacy .claude/skills entry for the OmniVoice TTS engine that powers VoiceStudio's default voice |

The remaining 3 indexed listings range from 3 to 75 installs.

## Why This Matters for Hermes Agents

VoiceStudio gives an agent a self-hosted speech stack - voice cloning, voice design, dubbing, dictation, transcription and audiobook narration - instead of a per-call cloud API, all on local hardware with no account. The voicestudio skill routes audio work through VoiceStudio's REST API or MCP server, so an agent can generate speech with saved or designed voices and automate dubbing or narration workflows end to end. The voicestudio-maintainer skill is scoped separately to repository work, so an agent handling the repo never conflates code maintenance with audio generation. The MCP server at backend/mcp_server.py is the programmatic entry point for wiring VoiceStudio into a larger agent or automation pipeline. The security sample is clean: all six listings Pass Gen Agent Trust Hub and Socket, with the only Warns three Snyk cells on the lower-count skills. The constraint to plan around is licensing: the code is AGPL-3.0 and the default OmniVoice model weights are non-commercial (CC-BY-NC), so check each model's license in the Model Manager before client work.

## Usage

| You say | What happens |
|---|---|
| Clone my voice from this recording | Generates speech in the cloned voice through the local REST API |
| Dub this video into Spanish | Translates and dubs the video with speech timed to the original |
| Transcribe this audio file | Runs local transcription and returns the text |
| Make an audiobook from this book | Sets up a longform narration project and renders chapters to speech |
| Design a warm British narrator voice | Generates a voice from a text description via voice design |
| Triage the open issues on the repo | Uses voicestudio-maintainer to sort and label GitHub issues |

## Verification

Confirm the two shipped skill files exist in the repository and read their top lines:

```bash
curl -sL https://raw.githubusercontent.com/debpalash/voicestudio/main/skills/voicestudio/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/debpalash/voicestudio/main/skills/voicestudio-maintainer/SKILL.md | head -40
```

Confirm the MCP server module the skills target is present:

```bash
curl -sL https://raw.githubusercontent.com/debpalash/voicestudio/main/backend/mcp_server.py | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| voicestudio | Pass | Pass | Pass |
| voicestudio-maintainer | Pass | Pass | Warn |
| omnivoice | Pass | Pass | Warn |
| oss-maintainer | Pass | Pass | Warn |
| vite | Pass | Pass | Pass |
| fastapi-python | Pass | Pass | Pass |

The sample is clean: every listing Passes Gen Agent Trust Hub and Socket, and the only Warns are three Snyk cells on voicestudio-maintainer, omnivoice and oss-maintainer.

## Limitations

- Snapshot data, verified Nov 21, 2026: 5,697 combined installs across 6 indexed listings; 116,057 GitHub stars; AGPL-3.0; last pushed Nov 22, 2026. Counts drift over time.
- The index and the tree only partially line up: skills.sh lists six names, but only voicestudio and voicestudio-maintainer have in-tree SKILL.md files under `skills/`, omnivoice appears only as a legacy `.claude/skills` entry (LEGACY.md), and oss-maintainer has no directory in the tree.
- The install counts are concentrated on the two lead skills, which carry 5,458 of the 5,697 total; the remaining 239 installs are spread across omnivoice (158), oss-maintainer (75), vite (3) and fastapi-python (3).
- The AGPL-3.0 license constrains commercial reuse: the app code is free for commercial use under AGPL terms, but model weights carry separate licenses, and the default OmniVoice weights are non-commercial (CC-BY-NC), so each model's license must be checked before client work.
- The README's responsible-use disclaimer prohibits unauthorized voice cloning and impersonation; cloning a voice requires the owner's permission.

## Related

- [Vapi Skills - Voice AI Agent Building Setup](/hermes/skills/catalog/vapi-skills-setup)
- [Noiz AI Skills - Voice and Speech for Agents](/hermes/skills/catalog/noizai-skills-setup)
- [elevenlabs Skills](/hermes/skills/catalog/elevenlabs)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the app first with the one-command installer before adding the skills; the voicestudio skill talks to the running app's REST API and MCP server.
- Pick voicestudio for audio work and voicestudio-maintainer for repo work; the two are deliberately separate so maintenance never triggers audio generation.
- Treat omnivoice, oss-maintainer, vite and fastapi-python as incidental in-tree skills rather than the main product; the two lead skills are what most installs use.
- Before commercial client work, check each model's license in the Model Manager; AGPL-3.0 covers the code but the default OmniVoice weights are CC-BY-NC.
- Wire the MCP server at backend/mcp_server.py when you want VoiceStudio as a tool in a larger agent rather than a one-off CLI call.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
