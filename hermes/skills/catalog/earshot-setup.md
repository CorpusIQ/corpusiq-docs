---
title: "earshot - Sound Effects for Coding Agents"
description: "leonxlnx/earshot: 7.0K combined installs. Sound effects for coding agents, rendered in code from 922 designs on CPU with no audio model."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/earshot-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "sound effects", "audio", "foley"]
---

# earshot - Setup Guide

**Source:** [leonxlnx/earshot](https://www.skills.sh/leonxlnx/earshot) via skills.sh - 7.0K combined installs across 2 indexed listings; first documented 2026-11-27 (evening sweep)

**GitHub:** [leonxlnx/earshot](https://github.com/leonxlnx/earshot) - 5,952 stars, MIT, branch main, last pushed 2026-11-22; the two agent skills live under `skills/earshot/SKILL.md` and `skills/real-sound/SKILL.md`, with the Claude Code plugin in `.claude-plugin/`.

**Category:** Sound effects and audio for coding agents: foley, interface sounds, ambience, film sound and listening

**Quality Tier:** 🟡 Yellow - one of the two sampled skills (earshot) carries a Snyk Warn; real-sound passes all three auditors.

earshot makes sound effects for a coding agent, which cannot hear them. The agent asks in plain words, earshot answers from a catalogue of 922 designs and renders a new take of the best one, entirely in code on the CPU, with no audio model in the generation path. When the catalogue has no such sound, `earshot build` assembles it from recorded parts and listens to the result with its own ears, an optional extra that downloads two open models on first use.

The repository ships as a command-line tool, a Python package, an MCP server with 20 tools and a Claude Code plugin with two commands, plus two agent skills: `earshot` for making and judging sounds, and `real-sound` for building realistic soundtracks for code-made videos from licensed recordings. Everything earshot renders belongs to whoever rendered it, free for any use.

## Installation

Install the agent skills and the tool separately. Install from GitHub, because the name `earshot` on PyPI belongs to another project:

```bash
npx skills add Leonxlnx/earshot                                   # the agent skills
pip install "earshot @ git+https://github.com/Leonxlnx/earshot"   # the tool
```

As a uv tool, with the extras in the brackets:

```bash
uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
```

The `listen` extra brings the two listening models and downloads about 1.1 GB on first use; making sounds needs none of that. For Claude Code, install the plugin, which brings both skills, the MCP server and the `/earshot:make` and `/earshot:make-set` commands:

```text
/plugin marketplace add Leonxlnx/earshot
/plugin install earshot@earshot
```

The MCP server also runs from any client's `.mcp.json`:

```json
{"mcpServers": {"earshot": {"command": "/path/to/earshot/.venv/bin/python", "args": ["-m", "earshot", "mcp"], "env": {"EARSHOT_THREADS": "3"}}}}
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| earshot | 3,666 | Making sound effects in code from a 922-design catalogue (interface sounds, foley, ambience, game sounds, drums and motion effects) and listening to any audio file to describe, judge or compare it. |
| real-sound | 3,337 | Building realistic soundtracks for code-made videos and animations from licensed recordings, with sourcing, mixing, mastering, credits and mux. |

Both indexed listings appear above.

## Why This Matters for Hermes Agents

earshot closes a loop that most agent-built products hit: a coding agent that writes interfaces, games and films cannot hear what it makes, so it cannot judge a sound effect. It renders sounds from a fixed catalogue of 922 designs on the CPU with no audio model, and it ships an optional listening layer that describes, measures and compares audio, so an agent can both produce a sound and verify it. The generation path is deterministic and offline, which suits a builder who wants repeatable assets without a GPU or a network call.

The two-skill split is the pattern to copy. `earshot` is the general-purpose maker and listener; `real-sound` is the narrower film-soundtrack process that layers sourcing, licence checks, mixing, mastering and mux on top. Separating the generic capability from the opinionated workflow keeps each skill focused and lets a router pick the right one for the job.

The trust boundary is also worth noting. The README is explicit that no listening model decides whether a made sound is good, and that the listening models only judge, never generate. For a builder wiring this into a pipeline, that means treating earshot's verdicts as hints and falling back to measurements and a human ear for anything production-critical.

## Usage

| You say | What happens |
|---|---|
| "Make a soft success sound for my app" | earshot make renders a new take from the catalogue and writes the file. |
| "Give my app a full UI sound set" | earshot make --set ui renders the 17 interface sounds with a manifest.json. |
| "What does this recording sound like?" | earshot describe returns calibrated tags, AudioSet labels and measurements. |
| "Build a sound the catalogue does not have" | earshot build drafts parts, renders a recipe and tunes it with the listening model. |
| "Does this clip sound recorded or synthesized?" | earshot realness gives a verdict with evidence. |
| "Give my code-made film a soundtrack from real recordings" | The real-sound skill runs sourcing, licence checks, mixing, mastering and mux. |

## Verification

The two skills sit at fixed paths on branch main (from the repository tree). Fetch the raw SKILL.md files to review before install; each should return 200:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/leonxlnx/earshot/main/skills/earshot/SKILL.md
curl -sL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/leonxlnx/earshot/main/skills/real-sound/SKILL.md
```

After a clone, confirm the skill layout:

```bash
git clone --depth 1 https://github.com/leonxlnx/earshot /tmp/earshot
ls /tmp/earshot/skills/
```

`skills/` should list `earshot` and `real-sound`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| earshot | Pass | Pass | Warn |
| real-sound | Pass | Pass | Pass |

This guide is Yellow because one of the two sampled skills (earshot) carries a Snyk Warn while real-sound passes all three auditors; there are no Fail cells in the sample. The repository stores no audio files: learned sounds are numbers analysed from public-domain recordings, and the generation path is CPU-only with no audio model, so the Snyk flag on earshot is worth reading on the skills.sh security page before production use.

## Limitations

- Snapshot data, verified 2026-11-27: 7,003 combined installs across 2 indexed listings; 5,952 GitHub stars; MIT; last pushed 2026-11-22. Counts drift over time.
- earshot makes no speech, singing or melodies; it plays instruments only as single notes and short figures, and realistic sounds exist only for things someone recorded and put in the public domain.
- A request that describes a mood is understood less well than one that names the sound, and a pick without a guess line can still be wrong.
- earshot build is not a path to any sound: it works for textures of many similar events and for pulsing, not for rain or hail on a new surface, a vehicle passing built from another motor, voices or pure tones; its fit comes from a listening model, not a person's ear.
- The listening tools (describe, match, realness and the ears of build) need the optional `listen` extra, which downloads about 1.1 GB of models on first use; making sounds itself is CPU-only and offline.
- The two indexed listings both map to directories in the tree (`skills/earshot` and `skills/real-sound`); there is no index-versus-tree drift.

## Related

- [iart JavaScript Animation Skills - Code-Drawn Motion](/hermes/skills/catalog/iart-javascript-animation-skills-setup)
- [Songwriting & AI Music Generation - Hermes Skill Setup Guide](/hermes/skills/catalog/songwriting-and-ai-music-setup)
- [Music Production Skills - Songwriting, Lyrics and Release](/hermes/skills/catalog/claude-ai-music-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the thing, the job or the sound first, then feelings, material and numbers: a request that names the sound does far better than one that describes a mood.
- Use earshot make --set ui for a whole interface sound set in one call, then level the set with the shipped manifest rather than asking for sounds one at a time.
- For more than a few listening calls, run the MCP server or one Python script (`from earshot import api`) so the models stay loaded instead of reloading on every CLI call.
- Always install from GitHub, and update with `uv tool upgrade earshot` if you installed it as a uv tool.
- Everything earshot renders is yours to use commercially without credit; only fit outputs made from your own recordings keep that recording's licence.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
