---
title: "Amethyst Skills - Kotlin & Compose Expertise Setup"
description: "vitorpamplona/amethyst - 3.1K combined installs: Kotlin Multiplatform and Compose expertise skills from the Amethyst Nostr client for Android."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/amethyst-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "kotlin", "compose", "android"]
---

# Amethyst - Setup Guide

**Source:** [vitorpamplona/amethyst](https://www.skills.sh/vitorpamplona/amethyst) via skills.sh - 3.1K combined installs across 25 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [vitorpamplona/amethyst](https://github.com/vitorpamplona/amethyst) - 1,626 stars, MIT license, last pushed Nov 26, 2026, main branch; skills live under .claude/skills/<name>/SKILL.md with matching .agents/skills/<name>/ directories.
**Category:** Mobile (Kotlin Multiplatform / Compose)
**Quality Tier:** 🟢 Green - 2 of 25 listings sampled: both carry Pass across Gen Agent Trust Hub, Socket, and Snyk.

Amethyst is a Nostr client for Android built on Kotlin Multiplatform and Compose Multiplatform. The two skills this guide covers were written for that app's contributors and encode the project's own conventions: where Kotlin Multiplatform code should live and how the shared Compose UI is structured. They transfer to other Kotlin and Compose projects as general guidance.

The install counts concentrate almost entirely on two skills: kotlin-multiplatform (1,576) and compose-expert (1,353). The other 23 indexed listings are single-purpose project rules in the 4 to 18 install range, so this is effectively a two-skill collection.

## Installation

The README is product-level (build and run the app) and documents no skills CLI install command for the skills themselves. The skills are plain Markdown files in the repository under .claude/skills/<name>/SKILL.md, so contributors get them by cloning the repo:

```bash
git clone https://github.com/vitorpamplona/amethyst.git
```

They can then be copied into any agent's skills directory.

## What It Provides

skills.sh publishes per-skill install counts for all 25 indexed listings. The 2 most-installed skills are listed below; the remaining 23 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| kotlin-multiplatform | 1,576 | KMP placement and Gradle in Amethyst: module and source-set selection, expect/actual vs ports, secp256k1 JNI variants, R8 |
| compose-expert | 1,353 | shared Compose UI in commonsUI: screens, the navigation shell, RichTextParser, and Compose API/perf review |

The remaining 23 indexed listings range from 4 to 18 installs.

## Why This Matters for Hermes Agents

These two skills carry hard-won Kotlin Multiplatform and Compose conventions that a coding agent would otherwise improvise per task. kotlin-multiplatform encodes placement discipline: which module or source set a change belongs in, when to use expect/actual versus a port interface, and the secp256k1 JNI and R8 specifics that break builds silently. compose-expert is a map of a large shared Compose UI layer: the navigation shell, the component catalog, and RichTextParser, plus explicit API and performance review guidance. For an agent contributing to Amethyst itself these are the house rules; for any other KMP or Compose project they are transferable guidance, not a drop-in. The caveat is scope: the skills were written for this one app, so their module names and specifics are Amethyst's, and the other 23 listings are single-purpose project rules rather than reusable knowledge.

## Usage

| You say | What happens |
|---|---|
| Where should this KMP change live? | Uses kotlin-multiplatform to pick the right module or source set |
| Is expect/actual right here? | Uses kotlin-multiplatform to decide expect/actual versus a port interface |
| Review this shared Compose UI | Uses compose-expert for Compose API and performance review against commonsUI |
| Find the nav shell for this screen | Uses compose-expert to locate ScreenLayoutSpec and the Navigation 3 back stacks |
| Parse this rich text | Uses compose-expert's RichTextParser guidance |
| Will this break the Android build? | Uses kotlin-multiplatform for R8 and secp256k1 JNI variant notes |

## Verification

Confirm the two skill files resolve on the main branch before copying them:

```bash
curl -sL https://raw.githubusercontent.com/vitorpamplona/amethyst/main/.claude/skills/kotlin-multiplatform/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/vitorpamplona/amethyst/main/.claude/skills/compose-expert/SKILL.md | head -40
```

Both URLs return 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| kotlin-multiplatform | Pass | Pass | Pass |
| compose-expert | Pass | Pass | Pass |

Across the 2 sampled skills there are 6 Pass, 0 Warn, and 0 Fail cells. skills.sh sampled only 2 of the 25 listings, so the other 23 carry no published verdict.

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,131 combined installs across 25 indexed listings; 1,626 GitHub stars; MIT license; last pushed Nov 26, 2026. Counts drift over time.
- The skills were written for Amethyst's own contributors and transfer as Kotlin and Compose guidance, not as drop-in tooling for other projects.
- The install counts are top-heavy: two skills hold 2,929 of the 3,131 combined installs, and the remaining 23 listings sit at 4 to 18 installs each.
- The install index outruns the tree: the repository carries 12 skill directories under .claude/skills/, but skills.sh indexes 25 listings, so several compose-* and kotlin-* tail listings have no matching directory in the current tree.
- The README is product-level (app build, install, and release) and documents no skills CLI install command for the skills themselves.
- skills.sh sampled only 2 of the 25 listings; the other 23 carry no published security verdict.

## Related

[Kotlin Agent Skills - Official JVM Guidance](/hermes/skills/catalog/kotlin-agent-skills-setup) | [Android Skills - Play Policy and App Quality Setup](/hermes/skills/catalog/android-skills-setup) | [Awesome Android Agent Skills - Compose and Kotlin Setup](/hermes/skills/catalog/awesome-android-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Treat the two high-install skills as the core; the other 23 are single-purpose project rules, not reusable knowledge.
- For contributing to Amethyst, read CONTRIBUTING-WITH-AI.md before planning any change; the gates there are not optional.
- The module and source-set names in kotlin-multiplatform are Amethyst-specific; map them to your own project's layout.
- compose-expert's RichTextParser and navigation-shell guidance is the most transferable part of the collection.
- Both sampled skills carry clean verdicts, but re-check the security pages on skills.sh before relying on the unsampled listings.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
