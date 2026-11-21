---
title: "Cloudinary Skills - Media API for Agents"
description: "cloudinary-devs/skills: six Cloudinary media skills for transforms, delivery, uploads and the Next.js and React SDKs - 3.1K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cloudinary-dev-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "cloudinary", "media", "image video"]
---

# Cloudinary Skills - Media API for Agents

**Source:** [cloudinary-devs/skills](https://www.skills.sh/cloudinary-devs/skills) via skills.sh - 3.1K combined installs across 6 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [cloudinary-devs/skills](https://github.com/cloudinary-devs/skills) - 13 stars, no LICENSE file, main branch, last pushed Nov 12, 2026; six skills grouped by category under `skills/platform/` (docs, transformations, upload, video) and `skills/frameworks/` (next, react), each a SKILL.md plus reference files.
**Category:** Media, Image and Video APIs
**Quality Tier:** 🟡 Yellow - 6 of 6 sampled skills pass Gen Agent Trust Hub, with 1 Socket Warn (cloudinary-next) and 1 Snyk Warn (cloudinary-video); no Fails.

Cloudinary's developer relations team publishes this package so agents write correct Cloudinary code instead of hallucinating SDK calls or delivery URLs. Six skills cover the media API surface: looking up current documentation, building delivery and transformation URL strings, uploading assets, and the Next.js and React SDK patterns. The skills are grouped by category in the repo (platform versus frameworks), but each installs individually by name.

The docs skill is the safety net: it reads the latest Cloudinary documentation through the relevant llms.txt before any API, SDK or delivery-URL code is written. The transformations skill turns natural-language edits like crop, resize, effects and overlays into valid URL strings. Cloudinary complements the skills with an MCP server for the write side, and a version check keeps each skill current against Cloudinary's live index. First seen in the Nov 21, 2026 morning sweep.

## Installation

Install the skills you need by name, or everything at once:

```bash
npx skills add cloudinary-devs/skills --skill cloudinary-docs,cloudinary-transformations
npx skills add cloudinary-devs/skills --skill cloudinary-upload
npx skills add cloudinary-devs/skills --skill cloudinary-next
```

```bash
npx skills add cloudinary-devs/skills
```

Install globally or per project. The skills pair with the Cloudinary MCP server: skills spell out best practices (such as using named transformations), and the model then decides which MCP tools to run to create them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| cloudinary-docs | 1,056 | looking up the latest Cloudinary docs via llms.txt before writing any Cloudinary API, SDK or delivery-URL code |
| cloudinary-transformations | 911 | turning natural-language image and video transformations into valid delivery URL strings |
| cloudinary-react | 707 | opinionated React SDK patterns for configuration, common integrations, errors and TypeScript pitfalls |
| cloudinary-next | 353 | Next.js SDK patterns through next-cloudinary and the Node SDK v2: CldImage, upload widget, server uploads and deletes |
| cloudinary-upload | 38 | uploading assets: signed and unsigned uploads, presets, naming, large files and signature generation |
| cloudinary-video | 29 | building video with the Cloudinary Video Player: adaptive delivery, captions, chapters and titles |

No indexed listings fall below the threshold; all 6 appear above.

## Why This Matters for Hermes Agents

Media handling is where agents ship plausible but wrong code: an image URL that looks right, a transform that is silently ignored, an SDK call that changed in the last release. This package removes that guesswork by tying every decision to the current documentation. The docs skill is read-only and triggered before any Cloudinary call, so an agent consults real docs rather than its training data, which is exactly where Cloudinary integration errors come from.

The transformations skill is the most operationally useful: an operator asks for a resized, cropped or overlaid variant, and the agent returns a URL string that follows Cloudinary best practices instead of an improvised query. Upload has a dedicated reference because signed versus unsigned uploads, presets and signature generation are easy to get wrong in a way that breaks at deploy time. The framework skills keep Next.js and React code inside the component boundaries and patterns those SDKs actually use, so generated code compiles and runs rather than just looking familiar. Because the skills are scoped to Cloudinary's own docs and API surface, an agent cannot wander outside the account and asset space it is connected to.

## Usage

| You say | What happens |
|---|---|
| Resize this image to a square and add a blur effect | The transformations skill builds a valid delivery URL with the crop, resize and effect applied |
| Set up Cloudinary in my Next.js app | The cloudinary-next skill walks through next-cloudinary setup, CldImage and the upload widget |
| My Cloudinary image URL throws an error | The transformations skill debugs the syntax and returns a corrected URL string |
| Upload this file to Cloudinary from the server | The cloudinary-upload skill pulls the signed-upload, preset and signature reference |
| Add a video player with captions to this page | The cloudinary-video skill references player and caption generation patterns |
| What does the upload API return on failure? | The cloudinary-docs skill looks up the current docs via llms.txt |

## Verification

Confirm the skills are visible to your agent after install, then review one skill's instructions before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/cloudinary-devs/skills/main/skills/platform/cloudinary-docs/SKILL.md | head -40
```

Each SKILL.md opens with a version-check block that fetches Cloudinary's skills index on first use and reports only if a newer version exists. Run the read-only transformations skill on one known image URL as a first test before any write or upload work.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cloudinary-docs | Pass | Pass | Pass |
| cloudinary-transformations | Pass | Pass | Pass |
| cloudinary-react | Pass | Pass | Pass |
| cloudinary-next | Pass | Warn | Pass |
| cloudinary-upload | Pass | Pass | Pass |
| cloudinary-video | Pass | Pass | Warn |

The skills hold no credentials. On first use each skill runs a version check that fetches Cloudinary's skills index and sends the skill name, version, agent product and model, the task kind, and your cloud name if already known from the conversation. It never sends API keys or secrets, and it never opens files to find your cloud name; tell the agent to skip the check in `AGENTS.md` or `CLAUDE.md` if you want it off.

## Limitations

- Snapshot data, verified Nov 21, 2026: 3,094 combined installs across 6 indexed listings; 13 GitHub stars; no LICENSE file; last pushed Nov 12, 2026. Counts drift over time.
- All 6 indexed listings map one-to-one to a SKILL.md directory under `skills/platform/` or `skills/frameworks/`; there is no index-versus-tree drift in this repo.
- The repo carries no root LICENSE file, even though each SKILL.md frontmatter declares `license: MIT`; treat redistribution terms as unresolved until the repo adds one.
- Skill behaviour tracks Cloudinary's current documentation and API, so a skill can lag the live service; the built-in version check mitigates this but needs network access.
- cloudinary-upload and cloudinary-video are lightly adopted (38 and 29 installs) relative to the docs and transformations skills.

## Related

- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [Higgsfield Skills - AI Video & Image Generation Cluster Setup](/hermes/skills/catalog/higgsfield-skills-setup)
- [Media Use Setup - Agent Media OS for HyperFrames (182.7K installs)](/hermes/skills/catalog/media-use-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with cloudinary-docs or cloudinary-transformations: they are the two most-installed skills and the read-only foundation for every other Cloudinary task.
- Prefer named transformations for transforms you apply across many assets, then reuse that name instead of re-deriving the URL each time.
- Pin the skill version you tested, because the version-check block fetches a fresh index and the skills change as Cloudinary's API changes.
- Pair the skills with the Cloudinary MCP server for the write side, so transforms the agent designs can actually be created rather than just described.
- For Next.js and React projects, install cloudinary-next or cloudinary-react alongside cloudinary-upload, since upload patterns differ per framework.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
