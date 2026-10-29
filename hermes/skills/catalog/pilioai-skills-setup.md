---
title: "Pilio Skills - Image and PDF Utility API Skills Setup"
description: "Pilio skills: 64.0K combined installs across 7 image and PDF utility skills that hand generation, cutouts and watermark removal to the Pilio CLI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pilioai-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "image generation", "image editing", "media api"]
---

# Pilio Skills - Setup Guide

**Source:** [pilioai/skills](https://www.skills.sh/pilioai/skills) via skills.sh - 64.0K combined installs across 7 indexed listings; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [pilioai/skills](https://github.com/pilioai/skills) - 44 stars, MIT, branch main, last pushed 2026-07-26; 6 skill directories in the clone, one `SKILL.md` each under `skills/<name>/`

**Category:** Image generation, image cleanup and PDF utility skills for the Pilio developer API

**Quality Tier:** 🟡 Beta - vendor maintained with an MIT license but only 44 stars, 7 indexed listings against 6 skill directories in the tree, and a last push three months before this snapshot

Pilio Skills is the vendor skill set for Pilio's developer API, a hosted image and PDF utility service. The seven indexed listings cover image generation with GPT Image 2 and Nano Banana Pro, background removal, image watermark removal, PDF watermark removal and upscaling, and together they carry 64.0K installs, which makes this one of the larger media utility sources in the skills index despite the repository being six `SKILL.md` directories. Six of the seven listings have a matching directory on the `main` branch; the seventh, `nano-banana-2` at 13,485 installs, does not appear in the current tree.

Every skill is deliberately thin. A `SKILL.md` carries the trigger description, the exact `pnpm dlx @pilio/cli` invocation and the option list, and all upload, task polling, credit accounting and error handling live in the official CLI and SDK behind one `PILIO_API_KEY` environment variable. That split suits agent work: the skill decides when to act and the CLI owns the transport, so each install is a short markdown file rather than a bundled client. Pilio also publishes browser versions of the same tools at pilio.ai, which is the fastest way to confirm what a command will produce before an agent runs it unattended.

## Installation

The README installs one function at a time and names three of the listings as examples:

```bash
pnpm dlx skills add pilioai/skills --skill gpt-image-2
pnpm dlx skills add pilioai/skills --skill nano-banana-pro
pnpm dlx skills add pilioai/skills --skill remove-background
```

The same shape covers the remaining listings, so a full set for an image cleanup pipeline is three more calls:

```bash
pnpm dlx skills add pilioai/skills --skill remove-image-watermark
pnpm dlx skills add pilioai/skills --skill upscale-image
pnpm dlx skills add pilioai/skills --skill remove-pdf-watermark
```

The skills assume the CLI is reachable and the key is set. Both are documented in the README:

```bash
export PILIO_API_KEY="your-key-here"
pnpm dlx @pilio/cli task wait <task_id>
```

The README documents no install target and no Hermes path, so where the CLI writes is not specified. For a Hermes profile, clone once and copy the directory you want, which keeps the directory and skill names identical to the index:

```bash
git clone https://github.com/pilioai/skills.git
cp -R skills/gpt-image-2 ~/.hermes/profiles/corpusiq/skills/
```

Each copied directory holds a single `SKILL.md`, so the copy is the whole skill. Copy only the listings you need: the trigger descriptions overlap heavily between the two generation skills and between the two watermark skills.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gpt-image-2 | 20348 | Text-to-image generation and prompt-based editing through GPT Image 2: restyling, product-photo transformation and composition from one or more local reference images, with `--aspect-ratio` and `--quality` controls. |
| nano-banana-2 | 13485 | Image generation listing carried by the install index at 13,485 installs; no directory of that name exists in the current tree, so its `SKILL.md` could not be reviewed. |
| remove-background | 7631 | Transparent-background cutouts for portraits and product shots: one command takes a local file, and `task wait` polls the returned task to completion. |
| remove-image-watermark | 7555 | Cleaning visible watermark overlays off PNG, JPG, JPEG and WEBP images, with the finished file fetched from the task payload's `download_url`. |
| upscale-image | 7535 | AI super-resolution and clarity improvement for small or soft images, uploaded and polled through the CLI task queue rather than a synchronous call. |
| remove-pdf-watermark | 7419 | PDF watermark removal in the default mode or with `--mode editable` for editable output and `--mode ai` for page reconstruction. |
| nano-banana-pro | 72 | Premium image generation and reference-image editing through Nano Banana Pro, with a `--resolution` choice of 1K, 2K or 4K and the same reference-image composition path. |

All 7 indexed listings clear the 50-install threshold and appear in the table above, so there is no tail listing.

## Why This Matters for Hermes Agents

Media work is where agents tend to improvise. Asked for a cleaned product shot, a general agent will reach for an ImageMagick chain or a Python image library, produce something that looks approximately right and never tell you which step degraded the source. This suite replaces that improvisation with one documented command per job, and the command returns a task payload instead of a guess about whether the work finished.

The asynchronous shape is the part worth copying into your own skills. Every destructive or generative operation returns a task, and the companion command `pnpm dlx @pilio/cli task wait <task_id>` blocks until it settles. That gives a Hermes run a clean checkpoint: the agent can start a job, wait, and then read a `download_url` rather than assuming a fixed size or a silent success.

Credential handling is explicit in the files. Each `SKILL.md` requires `PILIO_API_KEY` in the environment and instructs the agent not to ask the user to paste a key into the conversation, which is the behavior you want in an unattended cron where a prompt asking for a secret has nobody to answer it. The image watermark skill goes further and warns against sending the key to result `download_url` values, a real leak path when a skill hands a signed URL to an external fetch.

The small footprint is also an argument in its favor. A skill directory is one short file with no scripts, no dependency tree and nothing that executes on install, so reviewing what you are about to trust costs one read. For a media step inside a larger pipeline, that is a better trade than importing a heavier framework skill that carries its own tooling.

## Usage

| You say | What happens |
|---|---|
| "Make me a 16:9 hero image of a matte black desk lamp on concrete" | gpt-image-2 builds the prompt call with `--aspect-ratio 16:9` and a `--quality` setting, runs the CLI, then polls the task until the file is ready. |
| "Restyle this product photo into a studio shot, keep the label readable" | gpt-image-2 runs in edit mode with `--input ./product.png` and the edit prompt, so the source image and the instruction travel together. |
| "Cut the background out of these portraits" | remove-background uploads each file, takes the returned task ids and waits on them, leaving transparent PNGs to collect. |
| "This client sent screenshots with a stock watermark baked in, clean them" | remove-image-watermark processes the PNG or WEBP files and returns a `download_url` per result, without the API key attached to the fetch. |
| "Take the watermark off this contract PDF but keep the text editable" | remove-pdf-watermark runs with `--mode editable`, which is the path for documents that still need to be edited rather than flattened. |
| "This logo is too small to use on a banner, clean it up" | upscale-image sends the file for super-resolution and polls the task, returning a higher-resolution version of the same image. |
| "Give me a premium campaign visual at 4K from these references" | nano-banana-pro composes from one or more `--input` files at `--resolution 4K` and returns a premium render of the prompt plus references. |

## Verification

Probe the paths before installing. All six of these returned 200 on the `main` branch when this guide was written:

```bash
for p in skills/gpt-image-2/SKILL.md \
         skills/remove-background/SKILL.md \
         skills/remove-image-watermark/SKILL.md \
         skills/upscale-image/SKILL.md \
         skills/remove-pdf-watermark/SKILL.md \
         skills/nano-banana-pro/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/pilioai/skills/main/$p"
done
```

The seventh indexed listing does not resolve, which is worth confirming rather than assuming, because a 404 here means the install index is ahead of the repository:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  "https://raw.githubusercontent.com/pilioai/skills/main/skills/nano-banana-2/SKILL.md"
```

Read the two files that carry the most risk before installing them, since one generates new assets and the other strips marks from someone else's:

- https://raw.githubusercontent.com/pilioai/skills/main/skills/gpt-image-2/SKILL.md
- https://raw.githubusercontent.com/pilioai/skills/main/skills/remove-image-watermark/SKILL.md

After install, confirm what landed and that the frontmatter name matches the directory you copied or installed:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -E '^(gpt-image-2|nano-banana|remove-|upscale-image)'
head -3 ~/.hermes/profiles/corpusiq/skills/gpt-image-2/SKILL.md
```

Then confirm the key is visible to the agent's shell and that the CLI answers, which separates a missing credential from a bad command before you spend a credit:

```bash
test -n "$PILIO_API_KEY" && echo key set || echo key missing
pnpm dlx @pilio/cli --help
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gpt-image-2 | Pass | Pass | Pass |
| nano-banana-2 | Pass | Pass | Warn W012 |
| remove-background | Pass | Pass | Pass |
| remove-image-watermark | Pass | Pass | Pass |
| upscale-image | Pass | Pass | Pass |
| remove-pdf-watermark | Pass | Pass | Pass |

Six listings were sampled and five of them pass all three auditors. The single Snyk warning is on `nano-banana-2` with code W012, and that is the one listing with no directory in the current tree, so the warning sits on a skill file nobody can read at the branch this guide was written against. Treat that pairing as the reason to install `nano-banana-pro` instead if you want a Nano Banana model, or to pin a commit before installing `nano-banana-2` at all.

What the install runs is minimal. Each directory is a single markdown file with a documented CLI invocation, the repository root holds a license, a README and the `skills` folder with no package manifest, and there is no lifecycle script to run on clone. The risk lives in the delegation target: every skill shells out to `@pilio/cli`, which uploads your files to a hosted API and spends credits from your account.

Two habits keep that contained. Keep the key in the environment rather than in a skill file or a prompt, which the skills themselves instruct, and scope one key per pipeline so revoking a key used by an unattended image cron does not also sign out an interactive session. Then watch where results come from: a returned `download_url` is a plain URL, and `remove-image-watermark` explicitly warns against attaching the API key to it.

Removing watermarks and removing backgrounds are also the two operations with real legal exposure. The suite will strip a visible overlay from any image you hand it, including stock photography you do not own, so keep those two skills out of any unattended pipeline that pulls images from the open web.

## Limitations

- Snapshot data, verified 2026-10-28: 64045 combined installs across 7 indexed listings; 44 GitHub stars; MIT license; last pushed 2026-07-26. Counts drift over time.
- The install index is ahead of the repository: `nano-banana-2` carries 13,485 installs, the second largest count in the source, but no directory of that name exists on `main`. Installing it cannot be verified against a skill file.
- The repository is small and has been quiet. Six skill directories, 44 stars and a last push on 2026-07-26 mean three months without a commit at snapshot time, so expect no quick upstream fixes if a command breaks against the current API.
- Every skill needs a live Pilio account, a `PILIO_API_KEY` and credits. There is no offline mode and no local model path, so the suite is unusable in an air-gapped or fully local setup.
- The security sample covers 6 of the 7 listings, and the one it warned on is the one with no readable skill file. The repository as a whole is not audited by that sample.
- Nothing here is documented for Hermes. The README covers the `skills add` CLI and hosted browser tools only, so the clone and copy route above is the one to use, and the destination directory it lands in is up to the installer.

## Related

- [GPT-Image-2 Style Library - Industrial Prompt & Style Templates Setup](/hermes/skills/catalog/gpt-image-2-style-library-setup)
- [Skills Collective AI Media - Image & Video Gen Setup](/hermes/skills/catalog/skills-collective-ai-media-setup)
- [Higgsfield Skills - AI Video & Image Generation Cluster Setup](/hermes/skills/catalog/higgsfield-skills-setup)

## Pro Tips

- Install one skill per job, not the whole source. The two generation skills and the two watermark skills share trigger phrases, and a full install leaves the agent choosing between near-duplicates on every image request.
- Always follow a destructive command with `task wait`. Every cleanup skill returns a task rather than a finished file, and an agent that skips the wait will report success on a job that is still processing or has failed.
- Test the workflow in the browser at pilio.ai before wiring it into a cron. The hosted tools run the same operations, so you learn the output quality without spending agent time on prompt iteration.
- Keep the key in the environment and never in a skill file. All six files say the same thing, and it stays true even when the key is only ever read by the CLI.
- Restrict `remove-image-watermark` and `remove-background` to jobs where you hold the rights to the source image. The commands work on anything you pass them, which is exactly why they need a human in the loop.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
