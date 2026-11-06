---
title: "Apple Design Skill - HIG Review Across Frameworks"
description: "dickwu/apple-design-skill on skills.sh: 13.0K combined installs; Apple HIG review that translates to Flutter, React Native, Tauri and Electron."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/apple-design-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "apple hig", "design review", "flutter", "react native"]
---

# Apple Design Skill - Setup Guide

**Source:** [dickwu/apple-design-skill](https://www.skills.sh/dickwu/apple-design-skill) via skills.sh - 13.0K combined installs across 1 indexed listing; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 2,880 stars, no licence file in the repo root, last pushed 2026-10-28, a single SKILL.md at the repository root with a references/ tree beside it
**Category:** Apple HIG review for agents: layout, motion and control craft translated to Flutter, React Native, Tauri and Electron
**Quality Tier:** 🟡 Review - clean scanner verdicts and a large star count, held back by having no licence file at all, so the terms of reuse rest on a README paragraph rather than a license.

One skill, one reviewer, and a reference library behind it. The repository packages an AI design reviewer grounded in Apple's Human Interface Guidelines: 123 pages pulled from developer.apple.com, including 57 component pages, plus a curated Liquid Glass guide and a cross-platform translation layer for Flutter, React Native, Tauri, Electron, SwiftUI, UIKit and AppKit.

The purpose is narrower than "make it look Apple". The README describes a reviewer that audits and improves mobile and desktop UI, translates Apple's vocabulary into the framework you actually use, and adds a design-craft lens so the result feels native without looking like a template. It also covers the two-display iPhone Duo, which is the kind of platform detail a general model has no reason to know.

Every finding is structured: a What, a Why that cites the guideline file and heading, and a Fix written in your framework. That citation discipline is the reason the skill is worth installing over a general design prompt.

## Installation

The README's primary route is the skills CLI:

```bash
npx skills add dickwu/apple-design-skill
```

The variations it documents:

```bash
npx skills add dickwu/apple-design-skill -a claude-code   # install for one agent only
npx skills add dickwu/apple-design-skill -g               # user-wide instead of this project
npx skills add dickwu/apple-design-skill --list           # show what would be installed
npx skills update apple-design                            # pull the latest version later
```

For Claude Code, the README also gives the by-hand route, because Claude Code reads skills from `.claude/skills/` in a project or `~/.claude/skills/` for the user:

```bash
git clone https://github.com/dickwu/apple-design-skill.git ~/.claude/skills/apple-design
```

The skill triggers on design-review requests and is also available as `/apple-design`.

Other harnesses use the same repository with different entry points. Cursor installs with `npx skills add dickwu/apple-design-skill -a cursor`, or keeps the repo's `.cursorrules` next to your own rules. Codex installs with `-a codex`, or takes the repository as a submodule and points `AGENTS.md` at it:

```bash
git submodule add https://github.com/dickwu/apple-design-skill.git .design-rules
```

Antigravity installs with `-a antigravity`, or clones into `.agents/skills/apple-design` and can keep the repo's `GEMINI.md` beside your project rules.

## What It Provides

One listing, one skill, and it clears the threshold on its own:

| Skill | Installs | Use For |
|---|---|---|
| apple-design | 13,047 | Apple HIG audit and review: eight design principles, blocking accessibility checks, platform conventions, visual craft, interaction, copy, and fixes written in your framework |

The single indexed listing clears the 500-install threshold and appears in the table above.

What sits behind that one listing is the reference tree, which is where most of the work happens. `SKILL.md` holds the stance, the page index, the principles, the lenses, the report format and the improvement mode. `references/hig/` holds the 123 generated pages: 6 getting-started pages, 16 foundations, 24 patterns, 57 components, 7 inputs, 13 technologies and the 1 curated Liquid Glass guide. `references/hig-lookup.md` is the generated index with Apple's own summaries, change dates, and the list of pages Apple publishes for other platforms that this skill omits. `references/cross-platform.md` maps Apple's vocabulary onto Flutter, React Native, Tauri and Electron terms, and `references/code-audit.md` holds the code patterns for Apple Pay, Liquid Glass and iPhone Duo.

## Why This Matters for Hermes Agents

Apple's guidelines are a specification with numbers in it, and an agent working from memory reproduces the vocabulary without the numbers. The skill forces the agent to open the guideline file before it writes a word, and every finding has to cite the file and heading it came from. That one constraint removes most of the confident-but-wrong design advice a coding agent produces.

The cross-platform layer is the piece that makes this usable outside Xcode. Most teams building iOS-shaped interfaces are doing it in Flutter, React Native, Tauri or Electron, and the guidelines are written in SwiftUI and UIKit terms. A translation file that names the equivalent is the difference between advice an agent can apply and advice it has to guess at.

Accessibility is treated as blocking rather than advisory. The README lists text scaling, contrast ratios, control sizes, screen readers, keyboard access, and motion and transparency settings, with the actual numbers. That is the section a generated interface usually fails, and it is the section a reviewer is most useful for.

The code audit mode is unusual for a design skill. It reads source rather than screenshots, searching for Apple Pay buttons and marks Apple did not draw (the cause of App Store Review Guideline 4.9 rejections), Liquid Glass applied where it should not be, and fixed widths or custom bars that stop an app adapting to iPhone Duo. Each match is cited as `path:line` with the guideline it breaks, which is a form an agent can act on and a human can check.

The improvement mode goes past review. It grounds the design in the product, plans a token system, critiques that plan against generic defaults before proposing it, and sequences the fixes from accessibility to polish. For an agent asked to make a screen feel designed rather than generated, that ordering matters more than any single suggestion.

The maintenance story is honest. Apple revises the HIG several times a year, and the repository ships `scripts/pull-hig.mjs` to re-pull the pages, with a documented rule that running it twice produces identical output. A skill that can be refreshed is a skill you can keep trusting.

The caveats are real too: this reviews against Apple's conventions, so it will push an Android-first or web-first product toward iOS patterns it may not want, and the whole suite is one maintainer's reading of Apple's text.

## Usage

| You say | What happens |
|---|---|
| "Review my Flutter app's home screen against Apple's guidelines" | The reviewer loads the relevant HIG pages and reports What, Why and Fix in Flutter terms |
| "Audit this Tauri app for accessibility" | The accessibility lens runs as a blocking pass: text scaling, contrast, control sizes, screen readers, keyboard, motion settings |
| "Does this settings screen follow macOS conventions?" | Platform conventions for the menu bar, windows, sidebars, shortcuts and settings drive the review |
| "Is my Flutter app ready for iPhone Duo's two displays?" | iPhone Duo mode walks outer display, inner display, partial fold and Split View against Apple's guidance |
| "This looks generic, give it a point of view" | Improvement mode plans a token system and one signature element, then critiques the plan before proposing it |
| "Audit this repo for anything App Review would reject in our Apple Pay checkout" | Code audit mode searches for marks Apple did not draw and cites each match as path:line |
| "Check this app icon" | The app icon mode reviews the icon against the HIG's app icon guidance and the craft lens |

## Verification

Read the skill before installing it. This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/dickwu/apple-design-skill/main/SKILL.md | head -30
```

It should open with a description naming the Human Interface Guidelines, the 123 pulled pages, the 57 component pages and the design-craft lens, and it should name every guideline file the skill expects to load.

The reference tree is the part worth confirming after install, because the skill is only as current as those files. If you took the clone route, the skill's own directory is `apple-design`:

```bash
ls ~/.claude/skills/apple-design/references/hig | wc -l
curl -fsSL https://raw.githubusercontent.com/dickwu/apple-design-skill/main/references/hig-lookup.md | head -20
```

The directory should hold the generated pages plus the curated Liquid Glass guide, and `hig-lookup.md` should open with the generated index of Apple's pages, their summaries and change dates. If the page count is far below the README's figure, the clone is stale.

To refresh the guidelines from Apple, the repository's own script is the documented path. It needs Node 18 or newer, has no dependencies, and makes about 170 requests:

```bash
node scripts/pull-hig.mjs
```

The README's own test is that running it twice produces identical output, so a clean `git status` after a second run means the reference tree is in sync.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| apple-design | Pass | Pass | Pass |

The install surface is small. The skill is markdown plus a reference folder, with one Node script (`scripts/pull-hig.mjs`) that is only run when you choose to refresh, and no package dependencies at all. Nothing in the review path executes code from the repository.

The licence is the real gap. There is no LICENSE file in the repository root, the README states only that the skill, the curated guide and the script are "provided as they are; use them at your own discretion", and the guideline text itself belongs to Apple Inc. and is reproduced from the public Human Interface Guidelines with a source link at the top of every file. Absent a licence, you have no grant of rights beyond what the README says informally, so treat redistribution as unresolved and check with the maintainer before shipping the reference pages inside a product.

The other consideration is what the skill reads. Code audit mode reads your source tree, and the review modes read screens; if you are reviewing a client's app, that is client material inside your agent's context.

The README also states that the project is not affiliated with or endorsed by Apple, which matters if you plan to describe the output as HIG-certified. It is a reviewer built on Apple's public text, not an Apple product.

## Limitations

- Snapshot data, verified 2026-11-06: 13,047 combined installs across 1 indexed listing; 2,880 GitHub stars; no licence file; last pushed 2026-10-28. Counts drift over time.
- No LICENSE file. The README offers the skill, the curated guide and the script as they are, at your discretion, and the guideline text remains Apple's copyright. Redistribution rights are unresolved.
- Apple's guidelines move. The 123 pages are a snapshot taken by the repository's pull script, Apple revises the HIG several times a year, and pages the script no longer finds are removed on refresh.
- The reference set is deliberately partial. The README says the 35 pages Apple publishes for other platforms or Apple-only services are omitted, and `references/hig-lookup.md` lists them with the reason.
- It reviews against Apple's conventions. Web-first, Android-first or cross-platform products get advice toward iOS and macOS patterns, which is useful for a native-feeling app and wrong for a product that has chosen a different system.
- A review is advice, not a gate. Nothing here fails a build or blocks a merge; the findings only change what the agent does next, and visual layout plus OS accessibility still need native review on a device.

## Related

- [claude-design - Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/claude-design-setup)
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the citation. The report format is What, Why and Fix, where the Why names the guideline file and heading; if a finding arrives without that, the agent did not read the reference and the finding is not worth acting on.
- Run code audit mode before a submission, not after a rejection. It targets the specific things App Review flags, including marks Apple did not draw on an Apple Pay button, and it cites them by line.
- Point it at one screen and one framework. The cross-platform file is only useful when the agent knows which vocabulary to translate into, so say "Flutter" rather than "mobile".
- Refresh before a design sprint, not mid-review. `node scripts/pull-hig.mjs` rewrites the reference tree, and a refresh halfway through a review changes the citations under you.
- Use it as a second opinion on a generated screen. The craft lens exists to catch the three looks that dominate generated UI, which is exactly the failure a design skill should be pointed at.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
