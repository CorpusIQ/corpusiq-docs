---
title: "Fal AI Community Skills - Media Generation Setup"
description: "fal-ai-community/skills on skills.sh: 11.2K combined installs across 31 listings; genmedia CLI plus prompting, cinematography and character design."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fal-ai-community-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "fal ai", "image generation", "video generation"]
---

# Fal AI Community Skills - Setup Guide

**Source:** [fal-ai-community/skills](https://www.skills.sh/fal-ai-community/skills) via skills.sh - 11.2K combined installs across 31 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 260 stars, no LICENSE file at the repository root and GitHub reports the licence as None while the README License section states MIT, last pushed 2026-10-23, 17 SKILL.md directories under skills/
**Category:** Media generation through fal.ai: endpoint catalog, model-family prompting, cinematography, character design and the genmedia CLI
**Quality Tier:** 🟡 Beta - Gen Agent Trust Hub Fail on three of four sampled skills and no LICENSE file in the repository.

The collection is a knowledge layer over one command line tool. `genmedia` is the surface that searches, inspects, runs and manages more than 1,200 fal.ai model endpoints, and every other skill tells the agent which endpoint to use, how to prompt it, and how to chain one call into the next. `fal-models-catalog` picks endpoints by modality, `fal-prompting` handles family-specific prompt structure, and the production skills cover the use cases: character design, cinematography, commercial work, marketing, storytelling and UGC.

Execution order is stated plainly in the README: discover an endpoint, inspect its schema, run it, poll status when needed, download the output. User-facing model execution should go through `genmedia` unless a skill documents another workflow in its own folder. Seventeen skill directories ship in the tree against 31 indexed listings.

## Installation

The README starts with an API key from the fal.ai dashboard, then installs the CLI and the skill bundle:

1. Create a key at fal.ai/dashboard/keys.
2. Install `genmedia` from the fal-ai-community/genmedia-cli repository, then run its setup step:

```bash
genmedia setup
```

3. Install the skills into the project:

```bash
genmedia init
```

That writes the default skill bundle into `.agents/skills/` or `.claude/skills/`. For Claude.ai, the README's other route is to upload the skill `.zip` files from `skills/` to the project. The README does not print a package-manager command for `genmedia` itself, so follow the instructions in genmedia-cli.

## What It Provides

Six of the 31 indexed listings meet the 500-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| cinematography | 1,193 | Shot language, camera movement, lighting, lens choice, colour grade and film texture for cinematic stills and video |
| fal-image-edit | 910 | Image editing through fal.ai endpoints, described at name level only because no SKILL.md description was found and it has no directory in the current tree |
| genmedia | 727 | The CLI surface: search models, fetch schemas, run endpoints, poll jobs, upload files and check pricing |
| fal-prompting | 561 | Model-family prompt craft for named families such as Kling, GPT Image 2 and Happy Horse |
| fal-models-catalog | 561 | Choosing an endpoint by modality, from text-to-image and image-to-video to 3D and audio |
| character-design | 504 | Original characters, reference and expression sheets, identity-preserving edits and character-to-video |

The remaining 25 indexed listings range from 82 to 495 installs, covering the narrower production and workflow skills such as commercial, marketing, storytelling, UGC and the 3D regeneration flows.

## Why This Matters for Hermes Agents

A model marketplace makes two things hard for an agent: choosing an endpoint and prompting it correctly. This pack separates them. A generated catalog answers the first question by modality, a prompting layer answers the second by model family, and the CLI owns execution, so the agent never has to guess a schema it could inspect.

That inspect-then-run loop is the pattern worth copying into any API-heavy skill. `genmedia schema` returns the fields an endpoint needs, which turns a plausible-looking call into a validated one before money is spent.

`cinematography` is the most portable skill here. Shot language, lens choice, lighting and grade vocabulary improve a video prompt whether or not fal.ai is the backend, which is why it is the highest-installed listing in the pack.

The honest caveats are quality and scope. Three of the four sampled skills fail Gen Agent Trust Hub, the repository ships no LICENSE file, and 25 of the 31 indexed listings sit below 500 installs, so most of the surface is thin.

## Usage

| You say | What happens |
|---|---|
| "which model should I use for image to video?" | fal-models-catalog picks an endpoint by modality and names the default |
| "how do I prompt Kling for this shot?" | fal-prompting applies the family-specific prompt structure |
| "make this product shot cinematic" | cinematography rewrites the prompt with lighting, lens and colour grade |
| "design a character sheet I can reuse" | character-design builds references and identity-preserving edits |
| "run this endpoint and save the output" | genmedia inspects the schema, runs the job, polls and downloads |
| "what does this endpoint cost?" | genmedia checks pricing before the run |
| "turn a product photo into a video ad" | fal-recipes runs the product-shot pipeline end to end |

## Verification

Fetch a raw skill file to confirm the tree still matches what skills.sh indexed. This path is `skills/cinematography/SKILL.md` on branch `main` and it returned 200 on November 4, 2026:

```bash
curl -fsSL https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/cinematography/SKILL.md | head -20
```

A response opening with `name: cinematography` and a description covering shot language, camera movement and lighting confirms the content is live. After `genmedia init`, confirm the bundle landed in the directory the README names:

```bash
ls .agents/skills
```

Then confirm the key is wired in with the setup step the README names:

```bash
genmedia setup
```

The README describes most of the pack as knowledge layers, and user-facing execution goes through `genmedia`, so nothing runs until the CLI can reach fal.ai with a valid key.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cinematography | Pass | Pass | Pass |
| fal-image-edit | Fail | Pass | Pass |
| genmedia | Fail | Pass | Warn |
| fal-generate | Fail | Pass | Warn |

Gen Agent Trust Hub fails three of the four sampled skills (`fal-image-edit`, `genmedia` and `fal-generate`), and Snyk adds a Warn on `genmedia` and `fal-generate`. Only `cinematography` passes all three auditors. The repository also ships no LICENSE file: there is no `LICENSE` or `LICENSE.md` at the root, GitHub reports the licence as None, and the README's License section states MIT. Treat the terms as unresolved until a file lands, and read the individual SKILL.md before enabling a failing skill.

## Limitations

- Snapshot data, verified 2026-11-04: 11,172 combined installs across 31 indexed listings; 260 GitHub stars; no LICENSE file (README states MIT); last pushed 2026-10-23. Counts drift over time.
- No LICENSE file exists at the repository root and GitHub reports the licence as None, while the README states MIT. Treat the terms as unresolved until the file lands.
- Gen Agent Trust Hub fails three of the four sampled skills, including `genmedia`, which every other skill depends on.
- The install index carries 31 listings against 17 directories under `skills/`. `fal-image-edit` is indexed and installed 910 times but has no matching directory in the current tree, so its row above is name level only.
- Execution depends on the external `genmedia` CLI and a fal.ai API key. The skills themselves are documentation and the README documents no package-manager install for the CLI.
- `genmedia init` installs the default skill bundle, not necessarily all 17 directories, so check what landed before assuming a skill is available.

## Related

- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)
- [Higgsfield Skills - AI Video & Image Generation](/hermes/skills/catalog/higgsfield-skills-setup)
- [Skills Collective AI Media - Image & Video Gen Setup](/hermes/skills/catalog/skills-collective-ai-media-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Inspect before you run. `genmedia schema` on the chosen endpoint answers required fields faster than guessing at them.
- Route by uncertainty: fal-models-catalog when the user has not named a model, fal-prompting when they have.
- Check pricing before a batch. The CLI exposes it, and a loop of video generations is where budgets disappear.
- Read `cinematography` even if you use another provider. The shot and lens vocabulary transfers directly.
- Chain through `fal-recipes` or `fal-workflow` for multi-step pipelines instead of hand-assembling calls, which is what those two skills exist for.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
