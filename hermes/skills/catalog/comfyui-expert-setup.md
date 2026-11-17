---
title: "ComfyUI Expert Skills - Video Production Setup"
description: "mckruz/comfyui-expert: 13.4K combined installs across 15 listings, Claude Code skills for ComfyUI image, video, voice and LoRA pipelines."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/comfyui-expert-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "comfyui", "video production", "image generation"]
---

# ComfyUI Expert Skills - Setup Guide

**Source:** [mckruz/comfyui-expert](https://www.skills.sh/mckruz/comfyui-expert) via skills.sh - 13.4K combined installs across 15 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 94 stars, MIT license, `master` branch, archived, last pushed 2026-03-18, 15 skills under `skills/<name>/SKILL.md`
**Category:** ComfyUI image / video / voice agent skills
**Quality Tier:** 🟠 Orange - two Gen Agent Trust Hub Fails in the 15-skill sample, and the repository is archived.

VideoAgent (ComfyUI Expert) is a session-scoped Claude Code orchestrator that turns Claude into a video-production technical director. Its 15 skills cover the full ComfyUI pipeline: workflow JSON generation, prompt engineering, character generation, video and voice synthesis, LoRA training, assembly and publishing.

The skills are read-on-demand markdown routed by `CLAUDE.md`; nothing is installed globally unless you run the sync script. The repository is archived and the default branch is `master`, which is why both facts are called out below.

## Installation

The README installs by cloning the repo and launching a Windows batch file:

```bash
git clone https://github.com/MCKRUZ/ComfyUI-Expert.git
cd ComfyUI-Expert
video-agent.bat
```

The launcher writes `state/session.json`, then starts Claude Code, which auto-loads `CLAUDE.md`. Options set the active project and the ComfyUI URL:

```bash
video-agent.bat --project "my-video"
video-agent.bat --comfyui "http://<remote-ip>:8188"
```

On first run (or after adding models), scan the ComfyUI installation so workflows can be validated against installed nodes:

```powershell
pwsh -File scripts/scan-inventory.ps1 -ComfyUIPath "C:\ComfyUI"
```

To install all skills into the global Claude skills directory, use the sync script:

```powershell
pwsh -File scripts/sync-skills.ps1
```

Prerequisites are Claude Code, ComfyUI, FFmpeg and PowerShell 7+, and Windows (the launcher is a `.bat`; the README notes Linux/macOS adaptation is straightforward).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| comfyui-workflow-builder | 2,285 | Generate ComfyUI workflow JSON from natural language, validated against installed nodes. |
| comfyui-api | 2,120 | Connect to a running ComfyUI instance, queue workflows and retrieve results. |
| comfyui-prompt-engineer | 1,431 | Craft model-specific prompts for FLUX, SDXL, SD1.5 and Wan video models. |
| comfyui-video-pipeline | 1,363 | Generate video with Wan, FramePack or AnimateDiff from images or text. |
| comfyui-troubleshooter | 1,104 | Diagnose ComfyUI errors, workflow failures and quality issues. |
| comfyui-character-gen | 796 | Build identity-preserving character workflows with face-preservation methods. |
| comfyui-inventory | 623 | Discover and cache installed ComfyUI models, nodes and capabilities. |
| comfyui-lora-training | 606 | Prepare datasets and configure LoRA training for character consistency. |
| comfyui-video-production | 503 | Plan and orchestrate end-to-end video pipelines with validation gates and retries. |

The remaining 6 indexed listings range from 393 to 471 installs.

## Why This Matters for Hermes Agents

The value for an agent is the domain knowledge: node class types, VRAM budgets, model-specific prompts and the correct step ordering for video (generate, validate, animate, validate, concatenate). A generic agent does not know which identity method (InfiniteYou, PuLID, InstantID, IP-Adapter) fits a use case, or that Wan 2.2 and FramePack have different VRAM floors.

The 3-tier context system matters for builders too: foundation files load at session start while reference files load only when a skill asks, so the agent stays inside its context window and still reaches deep detail on demand.

The inventory-first pattern is worth copying: every workflow is validated against a cached list of installed models and nodes before execution, which prevents the most common ComfyUI failure of referencing a node or model the user does not have.

## Usage

| You say | What happens |
|---|---|
| "Generate a photorealistic portrait using FLUX" | Routes to comfyui-workflow-builder, checks inventory, builds workflow JSON and queues it. |
| "Make a talking head video where she says 'Welcome to my channel'" | Orchestrates voice synthesis, video generation, lip-sync, face enhancement and assembly. |
| "Train a LoRA from these 20 reference images" | Runs comfyui-lora-training for dataset prep, training config and evaluation. |
| "Craft a better prompt" | Runs comfyui-prompt-engineer for model-specific optimization. |
| "Check for new ComfyUI video models released this month" | Runs comfyui-research to scan channels and update references. |
| "Something broke" | Runs comfyui-troubleshooter for error-pattern matching and fixes. |
| "Upload to YouTube" | Runs video-publisher for metadata and upload delegation. |

## Verification

Probe skills on the `master` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/mckruz/comfyui-expert/master/skills/comfyui-workflow-builder/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/mckruz/comfyui-expert/master/skills/comfyui-api/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/mckruz/comfyui-expert/master/skills/comfyui-prompt-engineer/SKILL.md
```

Skills live at `skills/<name>/SKILL.md` on the `master` branch.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| comfyui-workflow-builder | Warn | Pass | Pass |
| comfyui-api | Fail | Pass | Pass |
| comfyui-prompt-engineer | Pass | Pass | Pass |
| comfyui-video-pipeline | Pass | Pass | Pass |
| comfyui-troubleshooter | Pass | Pass | Pass |
| comfyui-character-gen | Pass | Pass | Pass |
| comfyui-inventory | Pass | Pass | Pass |
| comfyui-lora-training | Pass | Pass | Pass |
| comfyui-video-production | Pass | Pass | Pass |
| comfyui-prompt-interview | Fail | Pass | Pass |
| comfyui-research | Pass | Pass | Warn |
| comfyui-voice-pipeline | Pass | Pass | Pass |
| video-assembly | Pass | Pass | Pass |
| project-manager | Pass | Pass | Pass |
| video-publisher | Pass | Warn | Pass |

The sample covers all 15 indexed listings. Two skills (comfyui-api and comfyui-prompt-interview) fail Gen Agent Trust Hub; comfyui-workflow-builder carries a Trust Hub Warn, video-publisher a Socket Warn and comfyui-research a Snyk Warn.

## Limitations

- Snapshot data, verified 2026-11-17: 13,445 combined installs across 15 indexed listings; 94 GitHub stars; MIT; last pushed 2026-03-18. Counts drift over time.
- The repository is archived, so the skills are not actively maintained, and the model landscape (Wan, FramePack, LTX and the TTS tools) ages quickly.
- The default branch is `master`, not `main`; every raw URL must use `master`.
- The README's "The 13 Skills" section omits comfyui-character-gen and comfyui-video-production, which are present in the tree and the install index, so the README count trails the actual 15.
- Installation is Windows-first (a `.bat` launcher plus PowerShell scripts); Linux/macOS need a shell-equivalent launcher and `pwsh`.
- The publishing skill delegates uploads to global YouTube skills that live outside this repository, so publishing depends on skills installed separately.

## Related

- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)
- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the inventory scan first; every workflow is validated against it, and stale inventory is the main cause of "model not found" errors.
- Launch through `video-agent.bat`, not a bare `claude`, so `CLAUDE.md` loads and the routing table activates.
- Keep the skills project-local; only run `sync-skills.ps1` when you want them available to every session.
- Edit `foundation/hardware-profile.md` with your real GPU and VRAM before generating, so recommendations match your machine.
- Because the repo is archived, treat the model landscape as a starting point and run a research update before planning around a specific model.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
