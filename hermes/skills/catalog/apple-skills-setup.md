---
title: "Apple Skills - iOS and macOS Development Suite Setup"
description: "Apple platform development: 13.1K combined installs across 96 listings, iOS and macOS build, App Store optimization and review handling"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/apple-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "ios", "macos", "swift", "app store"]
---

# Apple Skills - Setup Guide

**Source:** [rshankras/claude-code-apple-skills](https://www.skills.sh/rshankras/claude-code-apple-skills) via skills.sh - 13.1K combined installs across 96 indexed listings (13,116 exact, API row cap reached); first seen 2026-11-11 (Nov 11, 2026 sweep)
**GitHub:** 882 stars, MIT license, `main` branch, last pushed 2026-11-09, 184 `SKILL.md` files under `skills/<category>/` and `skills/<category>/<sub-skill>/`, documented as 165 skills across 23 categories
**Category:** Apple platform development: iOS, macOS, watchOS and visionOS engineering, App Store optimization, monetization, privacy and release review
**Quality Tier:** 🟡 Mixed - MIT licensed, the widest Apple surface in the marketplace and internally consistent by its own CI count check, with one trust-hub Warn and two Snyk Warns across twelve sampled skills.

Most Apple skill collections stop at SwiftUI patterns. This one covers the whole indie shipping loop, which is why its install count is the highest in this sweep: it starts at the product question, runs through code generation and platform guidance across four operating systems, and finishes at the App Store with keyword work, screenshots, ratings, rejection handling and the privacy policy that has to live at a URL before you can publish.

The category structure is deliberate and it shapes the context cost. The README describes the plugin surfacing 23 category skills, each routing to its sub-skills on demand, so only 23 short descriptions sit in context. The repository counts 165 skills in total across those categories, and the README states the total is enforced by `scripts/check-counts.sh` in CI, which is a maintenance detail that matters when a library is large enough to drift.

The README's own usage framing is refreshingly low-tech for a developer tool. It offers three entry points, starting with "I don't know what to build" for someone with no idea, then an idea validation path for a new app, then a review or feature path for an existing one.

## Installation

The Claude Code plugin is the recommended path:

```bash
/plugin marketplace add rshankras/claude-code-apple-skills
/plugin install apple-skills@indie-apple-stack
```

The README notes that updates come through the marketplace and that there is no version pinning, so an install tracks `main` and can change under you. The same marketplace also carries a separate SwiftShip package with 55 slash commands for anyone who wants the full workflow alongside the skills.

For agents outside the Claude Code plugin system, the README documents the open skills installer, which is the path a Hermes profile should use:

```bash
npx skills add rshankras/claude-code-apple-skills --list
npx skills add rshankras/claude-code-apple-skills --skill paywall-generator
```

A manual copy also works, either into a project or globally, and is the simplest route when you only want a few categories:

```bash
git clone https://github.com/rshankras/claude-code-apple-skills.git
cp -r claude-code-apple-skills/skills your-project/.claude/skills/
```

The README is explicit about three limits on the non-plugin path, and they are worth reading before you choose it. Cross-skill references point by path, so a skill that names `generators/paywall-generator` only resolves if that skill was installed too. The App Store Connect helper is not copied by the installer, which matters for `iap-finalizer` and `privacy-publish` because both run `skills/_shared/asc-api/asc.py`, so those two need a clone with the `ASC` variable pointed at it. And there are duplicate names across categories, which the README calls out rather than hiding.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| macos-development | 1,608 | macOS app development: windows, menus, app lifecycle, sandboxing and platform conventions |
| ios-development | 851 | iOS development guidance covering Swift practices, SwiftUI patterns, HIG review, accessibility audits and app planning |
| design | 713 | Interface design direction for Apple platforms, from layout and typography to platform-appropriate interaction |
| app-store | 614 | App Store work: descriptions, keyword optimization, screenshots, ratings, rejections and review responses |
| watchOS | 596 | Watch apps, complications, health and fitness features, and widgets |
| product-development | 570 | Validating an idea and shaping what to build before writing code |
| release-review | 535 | Pre-release audit checklists before a submission |
| apple-intelligence | 531 | Apple Intelligence integration across the platform frameworks |
| generators | 510 | Code generators, including the paywall generator that the README uses as its example |
| security | 507 | Privacy manifests, required reason APIs and platform security requirements |
| swift-development | 505 | Swift language work: concurrency, data modelling and modern language features |
| legal | 503 | Privacy policies, terms of service and EULAs, including publishing them and setting App Store Connect URLs |

The remaining 84 indexed listings range from 10 to 485 installs and cover the sub-skills inside those categories: accessibility audits, app planning, simulator and device runs, screenshot planning, review response writing, in-app purchase finalisation, keyword work, monetization tiers, Core ML, MapKit, SwiftData and the visionOS spatial skills.

The tree is deeper than the index in two directions. There are 184 `SKILL.md` files against 96 indexed listings, and 96 is also the API row cap, so both published figures are floors. The structure is two-level: a category file at `skills/<category>/SKILL.md` that routes, plus sub-skills at `skills/<category>/<sub-skill>/SKILL.md` that carry the detail.

## Why This Matters for Hermes Agents

Shipping an indie app is a sequence of distinct jobs that most agents handle badly as a single request. Validating the idea, choosing an architecture, writing the code, making it look like it belongs on the platform, writing the store listing, handling the rejection, and getting the privacy policy onto a URL are seven different pieces of work with seven different failure modes. This suite's value is that each piece has its own skill with its own trigger.

The App Store operations category is the part with no equivalent in most Apple skill collections, and it is where indie developers lose the most time. A rejection is not a code problem, it is a communication problem with a specific expected format, and `rejection-handler` and `review-response-writer` exist for exactly that. Screenshot planning and keyword optimisation sit alongside them.

The privacy manifest work is a compliance surface that bites late. Apple's required reason APIs and privacy manifests are the kind of requirement that surfaces in review rather than at build time, so `security` covering privacy manifests is more valuable than it first appears. The `legal` category then produces the policy documents and, per the README's category table, publishes them and sets the App Store Connect URLs, which closes the loop that usually leaves a submission blocked.

The category routing is what keeps this usable. A 165-skill library loaded whole would drown skill selection, but 23 category descriptions is a normal sized candidate set, and the routing happens inside the skill rather than in the model's selection step.

The platform spread is the last differentiator. macOS at 1,608 installs is the most installed skill in the family, which is worth noticing: Mac apps are underserved relative to iOS, and a suite that treats macOS as a first-class target rather than an iOS variant is filling a real gap.

## Usage

| You say | What happens |
|---|---|
| "I have an idea for a macOS app that tracks X. Should I build it" | Runs the product validation path, tests the idea against the platform and market, and returns a go or no-go with reasoning |
| "I don't know what to build" | Walks the ideation path from the user's skills and interests toward a concrete app concept |
| "Review my SwiftUI views for HIG problems" | Applies the iOS or macOS design guidance and reports specific interface convention violations |
| "Add a paywall to this app" | Uses the generator skill for the paywall implementation and the monetization skill for pricing and tiers |
| "Write the App Store description and keywords" | Produces the listing copy and the keyword set through the App Store category |
| "Apple rejected the app for guideline 4.2. Should I appeal" | Runs the rejection handler, which classifies the rejection and drafts the response path |
| "Write a privacy policy and publish it" | Produces the policy and, through the App Store Connect helper, sets the URL in the listing |

## Verification

Each category has a file at `skills/<category>/SKILL.md`, and this returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/rshankras/claude-code-apple-skills/main/skills/ios/SKILL.md | head -8
```

The frontmatter is informative rather than decorative. The `ios` file opens with `name: ios-development`, a description covering Swift practices and HIG review, an `allowed-tools` list, and both a `last_verified` and a `review_by` date, which is a convention worth copying into your own skills.

To confirm what actually landed, list the skill directories rather than assuming the plugin installed everything:

```bash
ls ~/.hermes/profiles/corpusiq/skills/ | head -30
```

If you installed through the `npx skills` route, check the two known gaps by hand: the shared App Store Connect helper needs a clone, and any cross-skill reference resolves only if its target was installed.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| macos-development | Pass | Pass | Pass |
| ios-development | Pass | Pass | Warn |
| design | Warn | Pass | Pass |
| app-store | Pass | Pass | Pass |
| watchOS | Pass | Pass | Pass |
| product-development | Pass | Pass | Warn |
| release-review | Pass | Pass | Pass |
| apple-intelligence | Pass | Pass | Pass |
| generators | Pass | Pass | Pass |
| security | Pass | Pass | Pass |
| swift-development | Pass | Pass | Pass |
| legal | Pass | Pass | Pass |

Nine of the twelve sampled skills carry three Passes, with one trust-hub Warn on `design` and Snyk Warns on `ios-development` and `product-development`. Nothing in the sample fails, which is a better profile than most large collections, but the sample covers the top twelve of 96 listings and the tail is unaudited here.

The capability to think about is App Store Connect access. `iap-finalizer` and `privacy-publish` run a helper at `skills/_shared/asc-api/asc.py` that talks to App Store Connect, which means credentials for an Apple developer account. That is real publishing authority over a store listing. Scope the key tightly, prefer an App Store Connect API key over an account password, and treat those two skills as the ones needing the most deliberate review before production use.

## Limitations

- Snapshot data, verified 2026-11-11: 13,116 combined installs across 96 indexed listings; 882 GitHub stars; MIT; last pushed 2026-11-09. Counts drift over time.
- Both published figures are floors. The API returns at most 96 rows and that cap was reached, while the tree carries 184 `SKILL.md` files and the README counts 165 skills across 23 categories, so the real totals are higher than either published number.
- No version pinning through the plugin path. The README states the install tracks `main`, so an update can change behaviour between sessions.
- The `npx skills` route has documented gaps: cross-skill references break without their targets, the App Store Connect helper is not copied, and duplicate skill names exist across categories.
- Apple credentials are needed for the publishing skills. Nothing in the package substitutes for a developer account, and the two skills that set listing URLs require App Store Connect access.
- The skills are guidance and generation. Nothing here compiles your app, runs your tests or reads build errors back, so a verification loop still has to come from Xcode or a CI build.
- The suite is Apple-only by design. Cross-platform frameworks such as Flutter or React Native have no path through it.

## Related

- [Swift iOS Skills - iOS 26 and SwiftUI Suite Setup](/hermes/skills/catalog/dpearson-swift-ios-skills-setup)
- [ASO Skills - App Store Optimization Suite Setup](/hermes/skills/catalog/aso-skills-setup)
- [App Store Connect CLI - Mobile Release Automation Setup](/hermes/skills/catalog/app-store-connect-cli-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask the category question first. Naming the job, "write the store listing" or "review these views for HIG", routes to the right category far better than naming a technology.
- Use `release-review` before every submission. It is the cheapest skill in the set and the failures it catches are the ones that cost a week in review.
- Keep the App Store Connect helper out of the default install. Clone the repository when you need `iap-finalizer` or `privacy-publish`, and leave those two uninstalled until you have scoped a key.
- Read the `last_verified` and `review_by` frontmatter fields. They tell you how current a category is against the OS version it claims, which is unusually honest for a skill library.
- Pair it with a build loop. This suite decides what to write; a compiler decides whether it was right.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
