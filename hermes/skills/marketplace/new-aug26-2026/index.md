---
title: "New Skills - August 26, 2026"
description: "skills.sh 15-query tiered sweep (605 unique skills): Generative Media Skills (calesthio, 137⭐ MIT, 153 skills, 2.1K indexed installs) - a full media production brain for Hermes agents with explicit HERMES.md support - 1 new publisher cluster, 1 setup guide."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug26-2026/"
robots: "index,follow"
last_updated: "2026-08-26"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-26"
new_publishers: 1
new_skills: 46
guides_drafted: 1
---

# New Skills - August 26, 2026

Fifteen-query skills.sh API sweep (605 unique skills, zero query failures) with tiered cross-reference against the full hermes/ tree: name-hit → covered, repo-hit → PARTIAL, repo-anywhere → ecosystem-covered. 89 skills flagged NEW and 113 PARTIAL; every NEW flag sat below the 100-install bar (max 89). The two PARTIAL candidates above the bar were verified as standing rejections. One NEW publisher cluster cleared the bar on explicit Hermes compatibility plus capability fit.

## New Publisher Clusters - Guided This Sweep

| Cluster | Skills | Installs | GitHub | Tier | Guide |
|---|---|---|---|---|---|
| calesthio/generative-media-skills | 153 (46 indexed) | 2.1K indexed | 137⭐ MIT | 🔵 | [Generative Media Skills Setup](/docs/hermes/skills/catalog/generative-media-skills-setup) |

## Method Notes

- Standard 15-query sweep (hermes agent, hermes skill, hermes automation, ecosystem repos: gbrain, honcho, devtools-skills, antigravity-awesome-skills, clawpilot, opendirectory, mercury-agent-skills) returned 605 unique skills: 89 NEW, 113 PARTIAL, zero ≥100-install NEW entries.
- Per the Aug 21 calibration, the numeric "5+ new" heuristic alone would over-fire on this distribution - the house bar required either ≥100 installs, a new ecosystem, or a capability gap before drafting.
- `calesthio/generative-media-skills` surfaced via its `production-design-direction` (44) and `topaz-video-enhancement` (40) NEW flags. Repo-level verification changed the picture: 137⭐ MIT, 153 skill packages, and a README that names "OpenClaw/Hermes-style agents" as a first-class target, with a dedicated `HERMES.md` entrypoint. The install path was executed end-to-end this sweep (`npx skills add calesthio/generative-media-skills --list` → 151 packages discovered), not just documented from the README.
- Capability fit is direct: the suite covers UGC video, GPT-Image-2 workflows, ElevenLabs voiceover, HyperFrames composition, and media QA - the exact surfaces CorpusIQ operates daily. Guided as 🔵 Community rather than parked, mirroring the Aug 24 System Atlas precedent (below-bar installs, clear relevance, clean record).
- The two PARTIAL ≥100-install candidates were re-verified against their READMEs and remain rejections: `skill-composer-studio` (onewave-ai/claude-skills, 264 - a Claude Code skill-chain composer from a Claude Code library) and `azure-chaos-studio` (microsoftdocs/agent-skills, 118 - Azure-platform-bound, same family as previously rejected azure-devtest-labs/azure-lab-services).

## Evaluated and Queued

| Skill | Source | Installs | Disposition |
|---|---|---|---|
| tanstack-devtools (112-skill catalog) | oakoss/agent-skills | 89 | Parked - 14⭐, no license, not Hermes-explicit; watch for growth |
| looker-studio | thatrebeccarae/claude-marketing | 83 | Parked - Claude-Code-branded marketing suite, no Hermes target |
| electrobun-native-ui | rajavijayach/electrobun-skills | 87 | Rejected - Electrobun desktop framework, platform-specific |
| rpgjs-studio | rsamaium/rpg-js | 85 | Rejected - RPG game framework, out of scope |
| new-rails-project | shpigford/skills | 70 | Rejected - Rails scaffolding, out of scope |
| arkweb-app-debug | openharmonyinsight/openharmony-skills | 54 | Rejected - OpenHarmony platform skill |
| field-lab | kyleamathews/field-lab | 31 | Parked - single quirky skill, below bar |
| hermes-agent-dissect, hermes-onboarding, hermes-vps-setup, hermes-principle, hermes-agent-bridge, hermes-chrome, hermes-subagent | kohoj/skills, moonlight-lupin/agent-skills, alejandro-ao/skills, and others | 1-8 | Parked below bar - Hermes-named but 1-8 installs each; watch for growth |
| skill-composer-studio | onewave-ai/claude-skills | 264 | Rejected (re-verified) - Claude Code skill-chain composer |
| azure-chaos-studio | microsoftdocs/agent-skills | 118 | Rejected (re-verified) - Azure platform skill |

Remaining 70+ NEW flags are scattered sub-50-install single skills from obscure repos - all below the bar, none Hermes-targeted.

## Notable Signals for CorpusIQ

- **elevenlabs-tts and elevenlabs-dubbing-voice-conversion** close the oldest open item on the Mac Mini media stack: the macOS `say` voice was rejected ("Computer voice awful! Really bad") - these skills carry the researched ElevenLabs production playbook to replace it.
- **openai-gpt-image** encodes the GPT Image 2 lifecycle against official docs (aliases, deprecation dates, rate limits) - one-to-one with the `image_generate` backend (gpt-image-2-medium) already in production.
- **hyperframes-video-composition and comfyui-media-workflows** (which validates HyperFrames timelines) harden the existing HyperFrames UGC pipeline with production craft instead of per-task improvisation.
- **media-qc-delivery and media-provenance-rights** give the daily video pipeline a deterministic QA and provenance pass - a scriptable content gate before Postiz publishing.
- Watchlist: oakoss/agent-skills (112 skills, top skill 89 installs) is one growth spurt away from the bar; kohoj's hermes-agent-dissect and the six other Hermes-named 1-8-install skills signal an emerging Hermes-focused publisher wave worth re-checking next sweep.

## Index State After Sweep

- catalog/index.md: +1 entry
- marketplace/index.md: header 910 → 911, footer 961 → 962
- last_updated on both indexes: 2026-08-26
