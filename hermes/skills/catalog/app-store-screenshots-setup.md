---
title: "App Store Screenshots - Store Assets Skill"
description: "parthjadhav/app-store-screenshots: 16.1K combined installs across 1 listing, end-to-end App Store and Google Play screenshot generation with AI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/app-store-screenshots-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "app store", "screenshots", "marketing"]
---

# App Store Screenshots - Setup Guide

**Source:** [parthjadhav/app-store-screenshots](https://www.skills.sh/parthjadhav/app-store-screenshots) via skills.sh - 16.1K combined installs across 1 indexed listing; first seen Nov 14, 2026 (sweep)
**GitHub:** 7,933 stars, MIT license, `main` branch, last pushed 2026-11-07, one `SKILL.md` under `skills/app-store-screenshots/`
**Category:** App Store and Google Play marketing screenshot generation
**Quality Tier:** 🟢 Green - the single sampled verdict passes all three auditors.

This is a single-skill repo that scaffolds a production-ready Next.js editor for designing and exporting App Store and Google Play marketing screenshots. The skill copies a template, installs dependencies, drops in your source screenshots and app icon, and starts a dev server for an editor with a connected canvas, device frames, inspector controls and one-click export bundles at store-ready sizes.

It is fully self-contained: the README's only requirements are Node.js 20.9+ and a package manager (bun, pnpm, yarn or npm). No external image provider or API key is involved; the editor renders PNGs locally with html-to-image.

## Installation

```bash
npx skills add ParthJadhav/app-store-screenshots
```

Install globally:

```bash
npx skills add ParthJadhav/app-store-screenshots -g
```

Manual install:

```bash
git clone https://github.com/ParthJadhav/app-store-screenshots ~/.claude/skills/app-store-screenshots
```

The README notes this works with Claude Code, Cursor, Windsurf, OpenCode, Codex and other agents supported by the Vercel `skills` CLI.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| app-store-screenshots | 16,069 | Build App Store or Google Play screenshot pages and export store-ready marketing screenshot bundles. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Store screenshots are marketing assets with strict, platform-specific resolution requirements that are tedious to get right by hand. This skill turns the job into a guided workflow: the agent gathers app context, source screenshots, platforms, locales and visual direction, then scaffolds an editor instead of hand-writing a static page.

The editor ships real device frames (Apple's bundled bezels plus Android, tablet and feature graphic decks), 18 named visual styles, a headline copy library, and connected-canvas support so phones, captions and decorative elements can span adjacent screenshots. That removes the design guesswork an agent would otherwise do poorly.

The export side is the part agents most often fumble. The skill emits exact PNG bundles for every required App Store, Mac App Store and Google Play size, including the universal 5244 x 2950 creative asset and iPhone Duo outer and inner displays, and waits until each screenshot has actually painted before writing.

## Usage

| You say | What happens |
|---|---|
| "Build App Store screenshots for my habit tracker" | The skill gathers app context, then scaffolds the Next.js editor with your source screenshots and a chosen style. |
| "Generate Play Store screenshots for my finance app" | The editor produces Android phone, tablet and feature graphic decks at store-ready sizes. |
| "Make an Arabic screenshot set" | The skill supports locales and RTL-aware copy and layout guidance, not just translated text. |
| "Create App Store creative assets" | Exports the universal 5244 x 2950 asset or separate header and search results crops. |
| "Resume my screenshot project" | The deck state in app-store-screenshots.json is git-trackable, so a fresh clone restores the project. |

## Verification

Probe the skill on the `main` branch before installing. Returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/parthjadhav/app-store-screenshots/main/skills/app-store-screenshots/SKILL.md
```

The skill lives at `skills/app-store-screenshots/SKILL.md`, with its template and style prompts co-located under the same directory.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| app-store-screenshots | Pass | Pass | Pass |

The single sampled skill passes all three auditors. The sample covers the only indexed listing, so it reflects the whole source, but re-check the skills.sh page before production use.

## Limitations

- Snapshot data, verified 2026-11-14: 16,069 combined installs across 1 indexed listing; 7,933 GitHub stars; MIT; last pushed 2026-11-07. Counts drift over time.
- Single-skill source: the only indexed listing is the skill itself, so the install figure is the entire surface.
- No external image provider or API key is required; the editor renders PNGs locally with html-to-image, and the only requirements are Node.js 20.9+ and a package manager.
- Apple's device bezels ship bundled from Apple Design Resources and are licensed for mock-ups of apps for Apple platforms only.
- Uploaded screenshots and the deck state are written to disk and are git-trackable; commit both to keep the deck reproducible after a fresh clone.

## Related

- [ASO Skills - App Store Optimization Suite Setup](/hermes/skills/catalog/aso-skills-setup)
- [ImageGen Skills - Design Images for Coding Agents](/hermes/skills/catalog/imagegen-skills-setup)
- [Designlang Skill - Extract Any Site's Design System](/hermes/skills/catalog/design-extract-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Capture source iPhone screenshots on the 6.1-inch simulator; it reduces manual image adjustment inside the frames.
- Name a visual style in your prompt, such as "use Swiss Grid Bold", to apply its whole spec in one shot.
- Treat screenshots as ads, not documentation: each slide should sell one user outcome and pass the one-second thumbnail test.
- Run the dev server and iterate in the editor rather than hand-crafting page.tsx, device frames or export logic.
- Use the Style Lab to compare four complete looks side by side, then keep the parts you like with the color, type, layout and scene locks.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
