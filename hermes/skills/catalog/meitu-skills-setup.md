---
title: "Meitu Skills - AI Image and Video Suite Setup"
description: "meitu/meitu-skills - 7.2K combined installs: 56 Meitu OpenAPI skills for image and video editing, beauty, ID photos and posters."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/meitu-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "meitu", "image editing", "video editing"]
---

# Meitu Skills - AI Image and Video Suite Setup

**Source:** [meitu/meitu-skills](https://www.skills.sh/meitu/meitu-skills) via skills.sh - 7.2K combined installs across 56 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [meitu/meitu-skills](https://github.com/meitu/meitu-skills) - 37 stars, MIT, main branch, last pushed Aug 28, 2026; a root routing SKILL.md, a meitu-tools command aggregate, and scene plus atomic-command skills under skills/.
**Category:** AI Media Generation and Editing
**Quality Tier:** 🟠 Orange - two Fail cells (image-poster-generate and image-background-replace) and Warn cells across seven skills, named in Security.

Meitu exposes its photo and video editing models to coding agents through the Meitu OpenAPI and a local meitu CLI. This collection turns that capability into 56 indexed listings that install into Claude Code, Cursor and other supported agents. Each skill maps one editing task, beauty retouching, ID photos, poster generation, style transfer, face swap, product shots, cutouts, and a full set of image and video commands, to a single CLI call with credential and error handling.

The library splits work into three layers. A root routing skill decides which entry point a request belongs to, a meitu-tools aggregate documents the full command catalog and credential handling, and the skills/ directory holds scene skills and atomic command skills that map one to one to CLI commands. The useful property for an operator is that every skill reads the same local credentials and writes results to a local output directory, so outputs stay predictable across the set.

## Installation

Install all skills, then the runtime CLI, then credentials:

```bash
npm install -g clawhub
clawhub install meitu-skills
```

Fallback install by GitHub URL:

```bash
npx -y skills add https://github.com/meitu/meitu-skills --yes
```

Install the runtime CLI the skills call:

```bash
npm install -g meitu-cli@latest
```

Configure credentials one of three ways: the MEITU_OPENAPI_ACCESS_KEY and MEITU_OPENAPI_SECRET_KEY environment variables, a pre-provisioned ~/.meitu/credentials.json file, or an explicit local write via meitu config set-ak and meitu config set-sk.

Smoke test the CLI before relying on it:

```bash
meitu --version
meitu image-cutout --image_url https://example.com/sample.jpg --model_type 0 --json
```

The skills do not auto-install or auto-upgrade meitu-cli, so treat the runtime as a separate manual step and re-run npm install -g meitu-cli@latest to repair or upgrade it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| meitu-skills | 358 | global routing that picks the right skill for a request |
| meitu-beauty | 169 | AI beauty retouching for a single-person portrait |
| meitu-id-photo | 156 | spec-compliant ID photos, background colour swaps and portrait sets |
| image-poster-generate | 153 | turning text or an image into a laid-out poster |
| meitu-tools | 148 | the unified Meitu CLI layer for credentials, command mapping and error guidance |
| image-text-replace | 145 | replacing text already present in an image |
| image-style-transfer | 143 | restyling an image to a named preset such as anime, oil or cartoon |
| video-resolution-upscale | 141 | pixel-level video super-resolution to 720P, 1080P, 2K or 4K |
| video-quality-enhance | 141 | one-shot video repair: deblur, denoise, frame interpolation, low-light lift |
| image-search | 138 | keyword or image-to-image search across the platform library and Pinterest |
| image-face-swap | 138 | face or head swap between two images with skin and lighting blend |
| meitu-product-view | 137 | multi-angle product shots from a single product image |
| meitu-cutout | 137 | subject cutout to a transparent-background PNG |
| image-background-replace | 137 | replacing a full background while keeping the foreground subject |
| meitu-upscale | 135 | one-click super-resolution with portrait, product and graphic modes |
| meitu-image-fix | 135 | composite repair chaining enhance, edit and cutout in order |
| image-edit | 134 | base image editing and repainting through the CLI |
| audio-song-generate | 134 | lyric-driven full songs with vocals or strong-beat instrumental music |
| text-to-image | 133 | generating a new image from a text description |
| image-portrait-generate | 133 | high-precision portrait generation from a reference photo |
| image-id-photo-generate | 133 | generating ID photos from a portrait |
| meitu-stickers | 132 | a 2x2 sticker grid from a photo, split into four stickers or GIFs |
| image-denoise-enhance | 132 | image denoising and enhancement |
| image-cutout | 132 | the atomic cutout command behind meitu-cutout |
| image-outfit-swap | 131 | swapping an outfit on a subject image |
| audio-music-generate | 131 | generating music audio |
| image-superres-enhance | 130 | super-resolution enhancement |

The remaining 29 indexed listings range from 4 to 129 installs.

## Why This Matters for Hermes Agents

An agent asked to touch up a photo or cut a subject out of a scene otherwise falls back to shelling out to a graphics tool it may not have installed, or to a generic prompt that returns an image with no guarantee of format or background. This collection replaces that guesswork with a named CLI command per effect, so a portrait retouch, an ID photo with a white background and a product poster are each a deterministic call with a local output path.

The layering is what makes it operator-friendly. The root skill routes intent, the meitu-tools skill centralizes credential and error handling, and the atomic command skills map one to one to meitu CLI commands, which means the agent and the operator can reason about what ran instead of trusting a black box. For production use, meitu-id-photo and meitu-product-view cover the two highest-value cases: a compliant ID or passport photo, and a multi-angle e-commerce product set sized for a specific platform.

The video skills, video-resolution-upscale and video-quality-enhance, split resolution work from quality repair, which matters because upscaling is pixel-level and does not fix blur or noise on its own. The security verdicts below are not clean, so treat this as a capable but credential-bearing suite rather than a drop-in without review.

## Usage

| You say | What happens |
|---|---|
| Retouch this portrait photo | Uses meitu-beauty for smoothing, brightening and feature refinement |
| Make a passport photo on a blue background | Uses meitu-id-photo for spec sizing and background colour |
| Turn this line into a product poster | Uses image-poster-generate for layout, style and platform sizes |
| Remove the background from this product shot | Uses meitu-cutout for a transparent-background PNG |
| Upscale this blurry video to 4K | Uses video-resolution-upscale for pixel-level super-resolution |
| Make this old photo look better overall | Uses meitu-image-fix to chain enhance, edit and cutout in order |
| Restyle this photo as anime | Uses image-style-transfer with a named style preset |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/meitu/meitu-skills/main/README.md | head -40
```

Confirm the beauty skill body is present before retouching work:

```bash
curl -sL https://raw.githubusercontent.com/meitu/meitu-skills/main/skills/meitu-beauty/SKILL.md | head -30
```

Confirm the tool aggregate is present before credential-driven work:

```bash
curl -sL https://raw.githubusercontent.com/meitu/meitu-skills/main/meitu-tools/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| meitu-skills | Warn | Warn | Warn |
| meitu-beauty | Pass | Pass | Pass |
| meitu-id-photo | Pass | Pass | Warn |
| image-poster-generate | Fail | Pass | Pass |
| meitu-tools | Pass | Pass | Pass |
| image-text-replace | Pass | Pass | Pass |
| image-style-transfer | Pass | Pass | Pass |
| video-resolution-upscale | Pass | Pass | Pass |
| video-quality-enhance | Pass | Pass | Pass |
| image-search | Pass | Pass | Warn |
| image-face-swap | Pass | Pass | Pass |
| meitu-product-view | Pass | Pass | Warn |
| meitu-cutout | Pass | Pass | Pass |
| image-background-replace | Fail | Pass | Warn |
| meitu-upscale | Pass | Pass | Pass |
| meitu-image-fix | Warn | Pass | Pass |
| image-edit | Pass | Pass | Pass |
| audio-song-generate | Pass | Pass | Pass |
| text-to-image | Pass | Pass | Pass |
| image-portrait-generate | Warn | Pass | Pass |

Two Fail cells land on image-poster-generate and image-background-replace (both Gen Agent Trust Hub). Warn cells land on meitu-skills (all three columns), meitu-id-photo, image-search and meitu-product-view (Snyk each), image-background-replace (Snyk), and meitu-image-fix and image-portrait-generate (Gen Agent Trust Hub each). The other 36 listings were not sampled, so check their own pages before installing them.

## Limitations

- Snapshot data, verified Nov 23, 2026: 7,200 combined installs across 56 indexed listings; 37 GitHub stars; MIT licence; last pushed Aug 28, 2026. Counts drift over time.
- Every skill requires Meitu OpenAPI credentials and writes results to a local output directory, so it is not a credential-free local tool.
- The skills do not check npm or auto-install meitu-cli, so a missing or outdated runtime fails until an operator repairs it manually.
- Five in-table listings (image-id-photo-generate, image-denoise-enhance, image-outfit-swap, audio-music-generate and image-superres-enhance) have no dedicated in-repo description in the sampled copy, so their Use For cells stay at command-name level.
- Long action_url values are preserved as-is, and chat interfaces may visually truncate them even though the full URL still works when clicked.
- The install index outruns the tree: most tail listings below the table have no counterpart in the current skills/ directory layout.

## Related

- [GPT Image 2 Style Library Setup](/hermes/skills/catalog/gpt-image-2-style-library-setup)
- [Generative Media Skills Setup](/hermes/skills/catalog/generative-media-skills-setup)
- [GenMedia Skills Setup](/hermes/skills/catalog/genmedia-skills-setup)
- [ComfyUI Expert Skills - Video Production Setup](/hermes/skills/catalog/comfyui-expert-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run meitu --version before trusting any skill, and re-run npm install -g meitu-cli@latest after any manual repair or upgrade.
- Prefer environment variables for credentials over meitu config set-ak and set-sk, which write the keys to disk.
- Run the sensitive-data self-check from SECURITY.md before any commit or shipment.
- For one clearly scoped edit, call the matching atomic skill directly; meitu-image-fix chains several and is for multi-issue repair.
- Keep image and video requests separate from text generation, since the text skills route to a different layer of the CLI.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
