---
title: "Codex PPT Skill - Image-Based Slide Decks"
description: "ningzimu/codex-ppt-skill on skills.sh: 5.1K combined installs in one listing; a GPT-Image skill turning documents into image-based PowerPoint decks."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/codex-ppt-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "powerpoint", "slides", "image generation"]
---

# Codex PPT - Setup Guide

**Source:** [ningzimu/codex-ppt-skill](https://www.skills.sh/ningzimu/codex-ppt-skill) via skills.sh - 5.1K combined installs across 1 indexed listing; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 7,677 stars, MIT licence filed at the repository root, last pushed 2026-10-13, one SKILL.md directory at skills/codex-ppt/, with AGENTS.md at the root
**Category:** Slide generation for agents: image-based PowerPoint decks produced with GPT-Image through a single skill
**Quality Tier:** 🟢 Green - MIT licence, the sampled skill passes Gen Agent Trust Hub, Socket and Snyk, and the one indexed listing has a matching SKILL.md directory.

Codex PPT is a single skill that turns an article, report, paper, course note or outline into a PowerPoint deck where every slide is one generated 16:9 image. The pipeline is staged rather than one-shot: plan the outline, confirm the slide count and key points, pick a visual style, name the image backend, generate one sample slide for approval, then produce the remaining slides and assemble them into a `.pptx` with a local Python script. The README's own summary of the trade is that the format suits strong visual expression, and that slide elements are not directly editable afterwards.

Two things are worth knowing before the install. The repository is Chinese-first: the main `README.md` is Simplified Chinese, with `README_en.md` and `README_ko.md` alongside it, and this guide is written from the English file. And although it is named for Codex, the README explicitly lists Claude Code, OpenClaw and Hermes Agent as supported environments, with the caveat that non-Codex agents usually need an image backend configured, either `gpt-image-2.5-flare`, a third-party image API, or an OpenAI-compatible image endpoint.

## Installation

The README's recommended path is to let the agent install its own skill:

```text
Please install this codex-ppt skill for me: https://github.com/ningzimu/codex-ppt-skill
```

The manual Hermes Agent install uses the skills CLI and writes to `~/.hermes/skills/codex-ppt`:

```bash
npx -y skills@latest add ningzimu/codex-ppt-skill \
  --skill codex-ppt \
  --agent hermes-agent \
  --global
```

The same command with `--agent codex` targets `~/.codex/skills` instead, and Codex users can alternatively unzip a release archive into `~/.codex/skills/codex-ppt`. OpenClaw installs from ClawHub:

```bash
openclaw skills install codex-ppt
```

Restart the agent after installing or updating. Configuration and personal styles deliberately live outside the install directory, at `~/.codex-ppt-skill/.env` and `~/.codex-ppt-skill/references/`, so reinstalling does not lose them.

## What It Provides

One listing, one skill, and the whole workflow lives inside it: orchestration in `SKILL.md`, rules in `docs/`, a worker handoff in `prompts/slide-worker.md`, twelve visual style references, and the Python scripts that generate prompts, record slide state and assemble the deck.

| Skill | Installs | Use For |
|---|---|---|
| codex-ppt | 5,121 | Turning articles, reports, papers, notes or outlines into a visually unified image-based PPTX, with style selection, sample approval, parallel slide generation, QA and speaker notes |

The one indexed listing clears the 500-install threshold and appears in the table above.

## Why This Matters for Hermes Agents

Deck generation is a task where agents fail in a predictable way: they produce a plausible outline, then a wall of text-heavy slides with no visual consistency. This skill attacks that by making the visual identity a decision the agent must state and get approved before any image is generated, and by writing one sample slide before the full deck.

The approval gates are the unusual part. `SKILL.md` carries a hard constraint that final `deck_spec.json`, `speech.md`, slide jobs, images and the `.pptx` cannot exist before the gates in `docs/workflow-gates-and-progress.md` are passed, and that progress recorded in chat does not count as completion. For an agent working unattended, that is a useful brake: the state files are the evidence.

It is also honest about what it is not. The skill forbids local drawing, Pillow, SVG, HTML screenshots and python-pptx layouts as fallbacks, because the output contract is that every slide came from the chosen image backend. An agent that quietly substitutes a hand-built layout produces a deck with different provenance than the one it reported.

Parallelism is built in but bounded. After sample approval, one subagent handles one slide, each returns only an image path, a backend and a QA note, and the parent owns the outline, state and assembly. That maps cleanly onto a Hermes orchestration pattern where the parent does the bookkeeping.

The output structure is the last practical win: `outline.md`, `origin_image/slide_XX.png`, `speech.md` and the `.pptx` in one project directory. A reviewer can open the exact frame used for slide seven without unpacking the deck.

## Usage

| You say | What happens |
|---|---|
| "Use codex-ppt to turn this article into a 10-slide deck" | The skill drafts an outline, asks you to confirm slide count and key points, then stops |
| "Make it look like this deck I like" | It analyses the supplied PPTX or screenshots for colour, layout and typography, then offers style directions |
| "Use the built-in image tool" | It checks whether the built-in backend is callable, states what it checked and waits for confirmation |
| "Approve the sample, build the rest" | It records the sample method, creates per-slide jobs and dispatches one subagent per slide |
| "Put this paper figure on slide 4" | The figure is treated as a strict input and the layout is generated around it |
| "Slide 6 has a typo" | It regenerates that one slide with a tighter prompt or edits it, instead of rebuilding the deck |
| "Add speaker notes" | It writes `speech.md` and the assembly step writes those notes into each slide of the PPTX |

## Verification

Read the skill contract before installing it, on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/skills/codex-ppt/SKILL.md | head -5
```

It should open with `name: codex-ppt` and the description "Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines."

After the install, confirm the supporting tree came with it:

```bash
ls ~/.hermes/skills/codex-ppt
ls ~/.hermes/skills/codex-ppt/scripts
```

The first listing should show `SKILL.md` alongside `docs`, `prompts`, `references`, `scripts` and a `requirements.txt`; the second should show the assembly and slide-state scripts the workflow calls, including `assemble_ppt.py` and `record_slide_result.py`.

A first real check is one short deck: ask for four slides from a one-page note, approve the sample, and confirm the output directory holds `outline.md`, four files under `origin_image/`, `speech.md` and a `.pptx` that opens.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| codex-ppt | Pass | Pass | Pass |

The scanners rate the instruction surface, and the instruction surface is not the whole risk. This skill runs local Python scripts (`assemble_ppt.py`, `image_gen.py`, `prepare_slide_prompts.py`), ships a `requirements.txt` for their dependencies, and stores an API key and base URL in `~/.codex-ppt-skill/.env`. Read `scripts/image_gen.py` before pointing it at a paid endpoint, keep that `.env` out of any repository, and expect a cost per slide because each page is a generated image, not a layout.

## Limitations

- Snapshot data, verified 2026-11-06: 5,121 combined installs across 1 indexed listing; 7,677 GitHub stars; MIT; last pushed 2026-10-13. Counts drift over time.
- Slides are images. Text, charts and shapes are not separately editable in the `.pptx`, and the README points at a separate skill, `image-to-editable-ppt-skill`, for converting a finished deck back to editable shapes.
- Non-Codex environments need an image backend. The README states that Claude Code, OpenClaw and Hermes Agent usually require `gpt-image-2.5-flare`, a third-party image API or an OpenAI-compatible endpoint, so the install alone does not make the skill generate anything.
- Backend behaviour is not verifiable from inside the skill. The README's own tip says the built-in image tool's model, resolution and controls depend on the environment, and that a successful response does not prove them; output above 2560x1440 is described as experimental.
- The workflow is deliberately broader than most jobs need. It supports both built-in and API/CLI generation and both subagent and single-agent production, and the README recommends editing the skill afterwards to lock one route.
- The main README is Simplified Chinese, and some linked articles, including the design retrospective, exist only in Chinese. The English and Korean READMEs carry the install, feature and workflow sections this guide uses.

## Related

- [PowerPoint - Create, Read, Edit .pptx Decks Setup](/hermes/skills/catalog/powerpoint-setup)
- [GPT-Image-2 Style Library - Industrial Prompt & Style Templates Setup](/hermes/skills/catalog/gpt-image-2-style-library-setup)
- [Claude Office Skills - XLSX, DOCX and PPTX Setup](/hermes/skills/catalog/tfriedel-claude-office-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Approve one sample slide, not a whole deck. The gate exists because a style that looks right in one image usually holds, and a style that is wrong is cheap to abandon at that point.
- Write your backend preference into the skill after the first successful run. The README suggests exactly this, and it removes a decision from every future deck.
- Give page roles, not just a page count. "Slide 1 title, slides 2 to 4 problem, slide 5 chart" produces a better outline than "make 10 slides".
- Save a style you like into `~/.codex-ppt-skill/references/`. It survives updates, and a personal style with the same name overrides the built-in one.
- Check `slide_run_state.json` rather than the chat transcript when you want to know whether a deck is finished.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
