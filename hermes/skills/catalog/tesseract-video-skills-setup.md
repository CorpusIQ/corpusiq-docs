---
title: "Tesseract Video Skills - Agent Creative Suite Setup"
description: "mirage-hq/tesseract on skills.sh: 13.1K combined installs across 5 listings; video editing, motion graphics, 3D and design skills for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tesseract-video-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "video editing", "motion graphics", "3d"]
---

# Tesseract Video Skills - Setup Guide

**Source:** [mirage-hq/tesseract](https://www.skills.sh/mirage-hq/tesseract) via skills.sh - 13.1K combined installs across 5 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 285 stars, custom Tesseract terms of service in `LICENSE` (duplicated as `TERMS.md`) rather than an open source licence, last pushed 2026-11-06, five `SKILL.md` directories under `skills/`, one per skill, with plugin manifests at `plugin.json` and `.claude-plugin/plugin.json` (version 0.6.0)
**Category:** Creative production for agents: local video editing, motion graphics, 3D scenes, static design and a browser editor over one shared project file
**Quality Tier:** 🟡 Yellow - Snyk returns Warn for `tesseract-video` and the repository ships terms of service instead of an OSI licence, so reuse rights and one scanner result both need reading before production use.

Tesseract is a creative suite built for agents by Mirage, and the pitch on the README is narrow on purpose: editing, motion and sound, connected in one local project. It ships as five skills plus a command line tool called `tsrct`, and the split of duties is explicit. The skills teach the agent how to edit, animate and design. The CLI does the actual project work, from building the `.tsrct` document to previewing frames and rendering the finished video.

What makes the set interesting is the project file rather than the individual skills. Every skill reads and writes the same portable `.tsrct` document, so a single video can mix supplied footage, a motion graphics scene and an imported 3D model without an export step between them. The README states that the agent picks the skill from your request, which means the routing work happens before you see anything.

## Installation

The skills CLI line in the README is the shortest path, and it needs Node.js:

```bash
npx skills add mirage-hq/Tesseract
```

The README leads with the ChatGPT plugin instead, which keeps the skills up to date automatically and bundles an optional MCP. The Claude plugin is listed as coming soon. For Claude Code, Cursor and other agents the documented route is a paste-in prompt:

```text
Install the latest Tesseract skills from https://github.com/mirage-hq/Tesseract and finish any setup they need.
```

That route does not self-update. The README says to paste the prompt again to get the latest version, and re-running the `npx skills add` line does the same job for a CLI install.

The CLI is a separate download and it is not optional. The video skill's own reference file, `skills/tesseract-video/references/installation.md`, opens with the distinction: the skills and the plugin contain instructions, not the CLI. It looks for an installed `tsrct` binary in the platform location first, then on `PATH`, then runs `--version` and compares the result against the pinned `references/cli-version.txt`. The README's manual download table covers four builds, `darwin-arm64`, `darwin-x86_64`, `windows-x86_64` and `linux-x86_64`, taken from Releases, each ZIP with a matching `.sha256` file.

For Hermes, the skills are plain directories. Copy or link `skills/tesseract-video`, `skills/tesseract-motion`, `skills/tesseract-design`, `skills/tesseract-editor` and `skills/tesseract-3d` into the profile skills directory, and bring their `references/` and `assets/` folders with them, because the bodies load reference files by relative path. The CLI still has to be installed and reachable on `PATH`.

## What It Provides

Five skills, and all five are above the reporting threshold:

| Skill | Installs | Use For |
|---|---|---|
| tesseract-video | 4,004 | Editing supplied footage into a finished cut: cuts, dialogue preservation, purposeful sound design, the audio mix, and deciding where a motion scene earns its place |
| tesseract-motion | 3,999 | Editable motion graphics: full-frame animated scenes, typography, diagrams, lower thirds and overlays on footage you supply |
| tesseract-design | 2,303 | Static design as an editable composition rendered to PNG: posters, social graphics, slide layouts, diagrams and web or UI mockups |
| tesseract-editor | 2,092 | A custom browser editor for `.tsrct` files, for editor controls, previews and saving, with no backend and no native CLI required |
| tesseract-3d | 653 | Editable 3D scenes with cameras, lights, meshes, materials, imported Blender and glTF models and property animation, on a 3D-enabled CLI build |

No indexed listings fall below the threshold; all 5 appear above.

The boundaries between them are written into the skill descriptions, which is unusual and useful. `tesseract-3d` says to use `tesseract-motion` for 2D motion graphics and warns that Scene3D needs a 3D-enabled CLI build, with a concrete check for it. `tesseract-motion` defers to `tesseract-video` when the job is assembling or revising a complete footage edit. `tesseract-design` is the one that produces still images, and its primary deliverable is a rendered PNG with the editable source kept beside it.

## Why This Matters for Hermes Agents

Most agent video work ends in a hosted render queue: the agent writes a prompt, a service returns an mp4, and the intermediate state is lost. Tesseract inverts that. The artefact is a project file on local disk, the render is a CLI call, and a revision is an edit to the same document rather than a fresh generation. That is the difference between a one-shot output and something a client can ask you to change.

The second useful idea is that the agent can see its own work. The documentation describes a filmstrip review and a critic loop, with reference files named `filmstrip-review.md` and `critic-review.md`, so the workflow includes looking at rendered frames and fixing what is wrong before delivery. An agent that renders, inspects, and re-renders is far more reliable than one that renders once and describes the result.

Third, the suite is a clean example of skill routing by deliverable type rather than by tool. Four skills share one document format and differ only in what the deliverable is: a cut, a motion scene, a still, a 3D scene. A Hermes agent with several media skills can copy that split, because the ambiguous cases are exactly the ones where a single mega-skill produces the wrong artefact.

Finally, ownership matters. The tool renders locally, the terms carve out output from the redistribution ban, and the licence is not open source. Read the Limitations section before you build a commercial pipeline on it.

## Usage

| You say | What happens |
|---|---|
| "Turn my travel footage into a 30 second vlog with beat-synced music" | `tesseract-video` takes the attached clips, cuts to the music and mixes audio into one `.tsrct` project |
| "Animate a diagram of how an order ships, 8 seconds, 16:9" | `tesseract-motion` builds the animated scene with your colours and duration, then previews frames |
| "Make a 3D gold coin flip over a purple gradient, vertical, 3 seconds" | `tesseract-3d` authors a Scene3D composition with camera and materials, after checking the CLI supports 3D layers |
| "Make a thumbnail for this video and match its fonts and colours" | `tesseract-design` produces a still composition and renders it to PNG with the editable source alongside |
| "Update this project file: make the title arrive earlier and soften the motion" | The matching skill reopens the existing `.tsrct` document and revises it rather than starting over |
| "Build an editor for this project so I can change the background and text colours" | `tesseract-editor` generates a static browser application over the browser API, with no backend to run |

## Verification

Read the video skill before installing. This path returned HTTP 200 on the repository's `main` branch when this guide was written:

```bash
curl -fsSL https://raw.githubusercontent.com/mirage-hq/tesseract/main/skills/tesseract-video/SKILL.md | head -12
```

It should open with `name: tesseract-video` and a description about editing existing footage into finished videos locally, with cuts, dialogue, sound design and an audio mix. The 3D skill is the one to check second, because it carries the capability gate:

```bash
curl -fsSL https://raw.githubusercontent.com/mirage-hq/tesseract/main/skills/tesseract-3d/SKILL.md | head -12
```

After install, confirm five skill directories landed in the skills directory your agent uses, and confirm the CLI is present and modern enough:

```bash
tsrct --version
tsrct project schema > /tmp/tsrct-schema.json && grep -c createFxScene3DLayer /tmp/tsrct-schema.json
```

A non-zero count from the second command means the build can author 3D scenes. A zero means it cannot, and `tesseract-3d` says to stop and report that rather than substituting 2D layers, which is the honest behaviour and worth checking before you ask for a 3D job.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tesseract-video | Pass | Pass | Warn |
| tesseract-motion | Pass | Pass | Pass |
| tesseract-design | Pass | Pass | Pass |

The sampled verdicts are mostly clean, and the one Warn sits on the skill with the widest reach, so read `tesseract-video` yourself before you run it on client footage.

Telemetry is the first practical consideration. The skill bodies state that the CLI may send basic usage telemetry for some commands, that attribution can be supplied through `TESSERACT_SKILL=<name>` and the variables documented in `references/telemetry.md`, and that the agent must respect the CLI's opt-out setting and never enable telemetry on the user's behalf. Set the opt-out deliberately on a machine that handles client material.

The second is the licence. `LICENSE` is not an open source licence: it is the Tesseract plugin terms, and section 2.2.3 withholds commercial use from a Covered Business, defined as a for-profit business with annual revenue at or above US$1,000,000, unless a separate written agreement authorises it. Section 2.2.2 also forbids using the plugin to build a competing product. Output is carved out of the redistribution ban, so what you render is yours, but check the terms against your entity before you make this the render path for paid work.

The third is operational rather than adversarial. Rendering uses the local GPU, the Linux bundle ships without an H.264 encoder and needs an external FFmpeg build for H.264 MP4 export, and the docs say explicitly not to bypass Gatekeeper or SmartScreen warnings. Treat a blocked launch as a decision for the machine's owner.

## Limitations

- Snapshot data, verified 2026-11-07: 13,051 combined installs across 5 indexed listings; 285 GitHub stars; custom terms of service (no OSI licence); last pushed 2026-11-06. Counts drift over time.
- Not open source. `LICENSE` and `TERMS.md` hold the same Tesseract plugin terms. Personal, non-profit, educational, governmental and professional use is permitted, commercial use by a business under the revenue threshold is permitted, and a business at or above US$1,000,000 in annual revenue needs a separate written agreement. Building a competing product is forbidden either way.
- The skills do nothing without the `tsrct` CLI. It is a per-platform binary download from Releases, not an npm package, and each skill checks the installed version against a pinned `cli-version.txt`.
- Linux cannot export H.264 MP4 out of the box. The 3D and video work is also GPU bound, so a headless cloud agent needs the right runtime before any of this is useful.
- The set is recent and small. Five skills, one of them with a Snyk Warn, and the skills carry version checks against a pinned CLI build. Expect both the CLI surface and the skill bodies to move.
- The comparison points in the docs are other editing tools, with dedicated reference files for Premiere Pro and After Effects conversion. That is useful for migration and useless if you expected native project interchange.

## Related

- [Remotion Best Practices - Setup Guide](/hermes/skills/catalog/remotion-best-practices-setup)
- [Motion Graphics Skills - Launch Video Suite](/hermes/skills/catalog/motion-graphics-skills-setup)
- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the CLI first, then the skills. The reverse order produces a session where every skill stops at the version check and reports the same missing binary.
- Ask for one deliverable at a time. The routing works because the deliverable type is unambiguous; a request that mixes a still, a cut and a 3D scene gets split by the agent and often split wrong.
- Keep the `.tsrct` project next to the render. Revisions are edits to that document, and regenerating from a prompt throws away every manual adjustment.
- Set the telemetry opt-out before the first client job, not after. The skill is instructed to respect the CLI setting and never to enable it on your behalf, so the decision belongs in your environment, not in a prompt.
- Check `tsrct --version` against `references/cli-version.txt` when a render fails oddly. The skill treats a version mismatch as the first suspect, and so should you.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
