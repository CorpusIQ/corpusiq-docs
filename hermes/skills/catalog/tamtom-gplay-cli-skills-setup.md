---
title: "Google Play CLI Skills - Android Release Automation Setup"
description: "tamtom/gplay-cli-skills: 19 agent skills for the Google Play Console CLI covering releases, metadata, IAP and vitals - 7.0K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tamtom-gplay-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "android", "google play", "mobile release"]
---

# Google Play CLI Skills - Android Release Automation Setup

**Source:** [tamtom/gplay-cli-skills](https://www.skills.sh/tamtom/gplay-cli-skills) via skills.sh - 7.0K combined installs across 19 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [tamtom/gplay-cli-skills](https://github.com/tamtom/gplay-cli-skills) - 53 stars, MIT license, main branch, last pushed Jul 26, 2026; skills live under `skills/<name>/SKILL.md` with a single `scripts/check-commands.py` validator that checks every skill command against the CLI reference.
**Category:** Mobile Release Automation
**Quality Tier:** 🟡 Yellow - all 19 sampled skills pass Gen Agent Trust Hub; one Socket Warn (gplay-purchase-verification) and Snyk Warn cells on 4 of the 19 sampled skills.

gplay-cli-skills is a focused set of agent skills for shipping Android apps with the Google Play Console CLI (`gplay`, from tamtom/play-console-cli). The publisher maintains the companion CLI and keeps the skills from drifting by validating every `gplay` command and flag used in a skill against the CLI's generated command reference in CI. The suite spans the release lifecycle: pre-submission checks, Gradle builds, metadata and localization, in-app purchases, staged rollouts, testers, reviews, vitals monitoring and report downloads.

The install index lists 19 skills; the current tree holds 17 SKILL.md directories. Two index-only listings, gplay-signing-setup and gplay-subscription-localization, carry install counts but no directory and no README section, with their functionality folded into gplay-gradle-build (signing) and gplay-iap-setup (subscription localization). First seen in the Nov 21, 2026 morning sweep.

## Installation

Install the skills with the skills CLI:

```bash
npx skills add tamtom/gplay-cli-skills
```

Check for updates and pull the latest versions:

```bash
npx skills check
npx skills update
```

Skills are plain markdown instructions, so the skill set needs no runtime beyond the `gplay` CLI itself and a host that loads SKILL.md files.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gplay-submission-checks | 497 | pre-submission validation of metadata, screenshots, bundle integrity, data safety and policy compliance |
| gplay-cli-usage | 475 | correct gplay command flags, output formats, pagination, auth and discovery |
| gplay-iap-setup | 441 | in-app products, subscriptions, base plans, offers and bulk subscription localization |
| gplay-gradle-build | 440 | build, sign and package Android apps with Gradle into an APK or AAB |
| gplay-metadata-sync | 431 | Play Store listing metadata and localization sync, including Fastlane format |
| gplay-release-flow | 426 | end-to-end release to internal, beta and production tracks with rollout |
| gplay-review-management | 399 | review monitoring, filtering and automated responses |
| gplay-screenshot-automation | 387 | manage, validate and upload listing screenshots by locale and device type |
| gplay-testers-orchestration | 384 | tester and closed-track management for internal and beta testing |
| gplay-vitals-monitoring | 381 | crash and ANR rates, error trends and performance metrics from Play Developer Reporting |

The remaining 9 indexed listings range from 153 to 377 installs.

## Why This Matters for Hermes Agents

Shipping an Android release is a checklist of rejectable mistakes: missing data-safety answers, a wrong screenshot dimension, a 32-bit-only build, or a pricing table that ignores purchasing power. This suite turns each checklist item into a skill an agent can run before the Play Console rejects it. gplay-preflight is the standout: an offline, credential-free scan of an AAB or APK over manifest flags, restricted permissions, 64-bit and 16 KB alignment, secrets, billing and privacy SDKs, so a build can be gated in CI before any Play credentials exist. The release and rollout skills give an agent one path to internal, beta and production tracks with staged percentage rollouts, and vitals-monitoring pulls crash and ANR rates straight from the Play Developer Reporting API to gate a release on stability. Because every command is validated against the real CLI surface, the skills cannot quietly teach a flag that no longer exists, which is the failure mode that silently breaks release automation.

## Usage

| You say | What happens |
|---|---|
| Build and upload my app to the internal track | Runs the Gradle build, packages the AAB and uploads to internal testing |
| Release v1.2.3 to production with a 10% staged rollout | Promotes the build to production and starts a 10% rollout with monitoring |
| Set up a subscription with monthly and yearly base plans | Creates the in-app products, base plans and offers in Play Console |
| Sync Fastlane metadata from ./metadata and upload | Imports the Fastlane metadata directory and pushes listing updates |
| Respond to all 1-star reviews from last week | Filters reviews by rating and drafts or sends automated responses |
| Run gplay preflight on this build before I upload | Runs the offline compliance scan and reports manifest, permission and size findings |
| Download last month's earnings report | Lists and downloads the financial reports from Google Cloud Storage |

## Verification

Confirm the skills are visible to your agent after install:

```bash
npx skills add tamtom/gplay-cli-skills
ls ~/.claude/skills 2>/dev/null || ls ./.claude/skills
```

Review the usage skill before composing commands:

```bash
curl -sL https://raw.githubusercontent.com/tamtom/gplay-cli-skills/main/skills/gplay-cli-usage/SKILL.md | head -40
```

Check for updates with `npx skills check` and `npx skills update`.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gplay-submission-checks | Pass | Pass | Pass |
| gplay-cli-usage | Pass | Pass | Pass |
| gplay-iap-setup | Pass | Pass | Pass |
| gplay-gradle-build | Pass | Pass | Pass |
| gplay-metadata-sync | Pass | Pass | Pass |
| gplay-release-flow | Pass | Pass | Pass |
| gplay-review-management | Pass | Pass | Warn |
| gplay-screenshot-automation | Pass | Pass | Pass |
| gplay-testers-orchestration | Pass | Pass | Pass |
| gplay-vitals-monitoring | Pass | Pass | Warn |
| gplay-ppp-pricing | Pass | Pass | Pass |
| gplay-purchase-verification | Pass | Warn | Warn |
| gplay-rollout-management | Pass | Pass | Warn |
| gplay-reports-download | Pass | Pass | Pass |
| gplay-user-management | Pass | Pass | Pass |
| gplay-migrate-fastlane | Pass | Pass | Pass |
| gplay-preflight | Pass | Pass | Pass |
| gplay-signing-setup | Pass | Pass | Pass |
| gplay-subscription-localization | Pass | Pass | Pass |

The sample is largely clean: Gen Agent Trust Hub passes on all 19, with one Socket Warn and four Snyk Warn cells concentrated on the purchase-verification and monitoring skills.

## Limitations

- Snapshot data, verified Nov 21, 2026: 6,998 combined installs across 19 indexed listings; 53 GitHub stars; MIT license; last pushed Jul 26, 2026. Counts drift over time.
- The install index outruns the tree: gplay-signing-setup and gplay-subscription-localization carry install counts (168 and 153) but have no SKILL.md directory and no README section in the current repository.
- Most skills drive the external `gplay` CLI, so they depend on that tool being installed, authenticated and current; the skills document the CLI surface but do not ship it.
- The repository last pushed Jul 26, 2026, so treat the documented commands as current against the CLI version they were validated on.
- Write skills (release, rollout, metadata, IAP) change a live Play Console listing; run gplay-preflight and gplay-submission-checks first and keep a staging track for dry runs.

## Related

- [App Store Connect CLI - Mobile Release Automation Setup](/hermes/skills/catalog/app-store-connect-cli-skills-setup)
- [ASO Skills - App Store Optimization Suite Setup](/hermes/skills/catalog/aso-skills-setup)
- [Android Skills - Play Policy and App Quality Setup](/hermes/skills/catalog/android-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Make `gplay preflight` a CI gate that runs before any Play credentials exist; it is offline and credential-free, so it fits the earliest build stage.
- Use staged rollouts and vitals-monitoring together: release to 10%, then check crash and ANR rates from the Developer Reporting API before widening.
- Keep Fastlane metadata as the source of truth and sync through gplay-metadata-sync, so listing text and screenshots stay in version control.
- Batch subscription localization through gplay-iap-setup instead of editing locales one at a time.
- Validate skill-implied commands against the CLI's GPLAY.md reference when you upgrade the CLI, since the skills are pinned to a specific command surface.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
