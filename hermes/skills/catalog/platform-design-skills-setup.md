---
title: "Platform Design Skills - HIG & Material Setup"
description: "Setup guide for ehmo/platform-design-skills - 12.8K combined installs. 450+ design rules for Apple HIG, Material Design 3, and WCAG 2.2."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/platform-design-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "design systems", "apple hig", "material design", "accessibility"]
---

# Platform Design Skills - Setup Guide

**Source:** [ehmo/platform-design-skills](https://www.skills.sh/ehmo/platform-design-skills) via skills.sh - 12.8K combined installs across 8 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [ehmo/platform-design-skills](https://github.com/ehmo/platform-design-skills) (606 stars, MIT license; last pushed Mar 19, 2026; per-platform layout `skills/<platform>/SKILL.md` across 8 platform directories)
**Category:** Design Systems / Platform Guidelines
**Quality Tier:** 🟡 Beta - 606-star MIT skill pack (Apple HIG + Material 3 + WCAG 2.2); all sampled verdicts Pass

Platform Design Skills, from independent publisher ehmo, distills the Apple Human Interface Guidelines, Google's Material Design 3, and WCAG 2.2 into per-platform rule files that agents can apply while evaluating, improving, or creating designs. The README headline promises 450+ rules; the GitHub description says 300+ - either way, this is one of the most direct ways to hand a coding agent platform-convention knowledge it can cite. The pack was built by scraping the Apple HIG (a compiled PDF ships in the repo) and distilling the material into succinct but exhaustive skill files.

Eight skills cover the major platforms: iOS, iPadOS, macOS, watchOS, visionOS, tvOS, Android, and the web. Each skill bundles a SKILL.md with agent instructions, a metadata.json, individual rule files with examples under rules/, and an AGENTS.md quick-context file. The install mix follows platform adoption: macos-design-guidelines leads at 4,029 installs, with every listing above 850.

---

## Installation

```bash
npx skills add ehmo/platform-design-skills
```

One command installs all eight platform skills. Skills activate automatically when an agent detects platform-relevant work.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| macos-design-guidelines | 4,029 | Mac app conventions: menu bars, window management, toolbars, keyboard-driven interaction, SwiftUI or AppKit |
| ios-design-guidelines | 1,798 | iPhone HIG: navigation, layout, accessibility, gestures, and components like tab bars, sheets, and Dynamic Island |
| android-design-guidelines | 1,562 | Material Design 3 for Android: Material You, dynamic color, navigation patterns, and components |
| web-design-guidelines | 1,410 | Web best practices: responsive design, WCAG accessibility, performance, progressive enhancement, modern CSS/HTML |
| ipados-design-guidelines | 1,130 | iPad HIG: multitasking, Split View and Slide Over, Stage Manager, pointer and keyboard support |
| watchos-design-guidelines | 1,012 | Apple Watch HIG: glanceable interfaces, Digital Crown, complications, Always On display, wrist interactions |
| tvos-design-guidelines | 970 | Apple TV HIG: focus-based navigation, Siri Remote, Top Shelf, living-room viewing distances |
| visionos-design-guidelines | 858 | Apple Vision Pro HIG: spatial UI, eye and hand input, windows, volumes, immersive spaces, ornaments |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Agents produce UI for Apple platforms, Android, and the web, and they routinely violate platform conventions in ways human reviewers catch only late: a macOS toolbar that ignores window expectations, an Android screen that fights Material You, a form that misses WCAG contrast. This pack gives the agent the normative rules at generation time - Apple HIG, Material Design 3, and WCAG 2.2 distilled into per-platform files - so reviews can cite platform documentation rather than taste. That matters most for cross-platform product teams, where the same agent output has to pass different convention checks per target. The skills also work as review instruments: ask for an audit and the agent walks the rule files instead of eyeballing the screenshot. Everything is plain markdown with rule files and examples, MIT licensed, and installable through the standard skills CLI. And because rules ship per platform, an agent working on iOS does not have to carry Material or web guidance it will never use.

## Usage

| You say | What happens |
|---|---|
| "Review this SwiftUI view for iOS HIG compliance" | The iOS skill checks navigation, layout, gestures, and components against HIG rules |
| "Check this Android Compose screen against Material Design" | The Android skill validates Material You, dynamic color, and component usage |
| "Audit this web page for accessibility" | The web skill checks WCAG criteria, responsive behavior, and performance |
| "Our iPad layout needs Stage Manager support" | The iPadOS skill covers Split View, Slide Over, pointer, and keyboard patterns |
| "Design a watch complication that reads at a glance" | The watchOS skill applies glanceability, Digital Crown, and Always On rules |
| "Review our macOS menu bar and toolbar" | The macOS skill checks menu, window, and desktop power-user conventions |
| "The Vision Pro layout feels off in immersive space" | The visionOS skill reviews spatial UI, eye and hand input, and ornament usage |

## Verification

```bash
# Confirm the skills are installed (adjust to your agent's skills directory)
npx skills list | grep -i design-guidelines

# Review a platform skill straight from GitHub before installing (layout: skills/<platform>/SKILL.md)
curl -s https://raw.githubusercontent.com/ehmo/platform-design-skills/main/skills/macos/SKILL.md | head -20
```

Each skill directory also ships metadata.json, a rules/ folder, and an AGENTS.md if you want to audit coverage before or after installing.

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| macos-design-guidelines | Pass | Pass | Pass |
| ios-design-guidelines | Pass | Pass | Pass |
| watchos-design-guidelines | Pass | Pass | Pass |

## Limitations

- Last pushed March 2026: platform guidelines evolve with each OS release, so the rule files are a snapshot rather than a live mirror of HIG, Material, or WCAG.
- Documentation counts disagree: the README headline claims 450+ rules while the GitHub description says 300+; scope expectations accordingly.
- Security verdicts were sampled for 3 of the 8 skills (macOS, iOS, watchOS); the other five carry no sampled verdicts.
- These are guidance files, not linters: the agent still authors and reviews the design, and the skills steer it toward platform conventions.
- The skills summarize public platform documentation; the normative sources remain the authority for compliance sign-off.
- Snapshot data, verified Oct 10, 2026: 12,769 combined installs across 8 indexed listings; 606 GitHub stars; MIT; last pushed Mar 19, 2026. Counts drift over time.

## Related

- [Macos Computer Use Setup](/hermes/skills/catalog/macos-computer-use-setup) - desktop automation for verifying macOS UI behavior
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup) - interface craft polish to pair with HIG compliance checks
- [Mobile App UI Design Skill - Mobile Interface Setup](/hermes/skills/catalog/mobile-app-ui-design-skill-setup) - mobile UI production workflow for app targets
- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup) - dedicated accessibility auditing for compliance sign-off
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Let activation do the work: mention the platform and task ("review this Android screen", "audit this page for accessibility") and the matching skill loads on demand.
- Ask for findings that name the specific rules from the rules/ directory so review feedback stays traceable to platform documentation.
- Install the pack once per project instead of vendoring single platforms; the skills are small markdown files and load only when relevant.
- Use the AGENTS.md and metadata.json in each skill directory to see coverage and references before a big review pass.
- For compliance work, treat the web skill's WCAG coverage as a first pass and follow with a dedicated audit suite (see Related).

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
