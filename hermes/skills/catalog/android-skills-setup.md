---
title: "Android Skills - Play Policy and App Quality Setup"
description: "android/skills: 48.5K combined installs. Google's official Android skill suite for Play policy audits, app quality, testing and Compose migration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/android-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "android", "google play", "jetpack compose"]
---

# Android Skills - Setup Guide

**Source:** [android/skills](https://www.skills.sh/android/skills) via skills.sh - 48.5K combined installs across 35 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [android/skills](https://github.com/android/skills) - 10,111 stars, Apache-2.0, branch main, last pushed 2026-10-29; 36 `SKILL.md` files in nested trees, one per skill, grouped under 18 top-level domains such as `system/`, `jetpack-compose/`, `play/`, `performance/`, `device-ai/`, `wear/`, `tv/` and `xr/`, alongside `README.md`, `LICENSE.txt`, `.claude-plugin/marketplace.json` and `.codex-plugin/`

**Category:** Official Android platform skills for build, quality, Play policy and form factors

**Quality Tier:** 🟡 Yellow - four of five sampled skills Pass on all three auditors while android-cli carries one Snyk Warn, and the suite is Apache-2.0 from Google itself

This is Google's own repository. `android/skills` is published by the Android team as a dedicated set of AI-optimized, modular instructions, written to steer agents toward the guidance on developer.android.com rather than around it. The README is explicit about the editorial line: skill development concentrates on "use cases and workflows where evaluations show LLMs underperform" and deliberately does not spend effort on areas where models are already competent, such as basic Jetpack Compose best practices. That framing is why the suite leans toward migration, auditing, policy compliance and form-factor work instead of tutorial-grade content.

The scope is broad for a single repository: 36 skills spanning build tooling, R8 shrinking, Compose and views, testing, profiling, Play Billing and policy, credentials, on-device AI, wearables, TV, cars and XR display glasses. Every `SKILL.md` carries `metadata: author: Google LLC` with a per-skill last-updated date and a keyword list, and 32 of the 36 skill directories ship a `references/` tree of mirrored developer.android.com pages, so an agent can read the same source documentation a human would. One sampled listing, `android-cli`, carries a Snyk Warn while the rest of the sample Passes, which is the reason for the yellow tier rather than green.

## Installation

The README installs skills through the `android` command line tool, which it assumes is already present and points at developer.android.com/tools/agents/android-cli for. One skill into one project:

```bash
android skills add r8-analyzer --project=.
```

Every skill, into the agent directories the CLI detects:

```bash
android skills add --all
```

There is a trap in the flags worth reading twice: if `--all` is omitted, only the `android-cli` skill is installed, not the one named on the command line alone. `--agent` takes a comma-separated list of agents, and `--project` sets the install root. With no existing agent directories and no explicit agents, the README says skills land at `~/.gemini/antigravity/skills` for Gemini and Antigravity. Updates work the same way:

```bash
android skills update --all
android skills update wear-compose-m3
```

Two plugin marketplaces are documented as well. Claude Code:

```text
/plugin marketplace add android/skills
/plugin install android-skills@android-skills
```

And Codex:

```bash
codex plugin marketplace add android/skills
codex plugin add android-skills@android-skills
```

Hermes is not one of the documented agent targets, so the durable route for this profile is the skills directory itself. Each skill is a self-contained directory, so copying one is the whole install, and copying the tree gives you a curated set:

```bash
cp -r play/play-policy-insights ~/.hermes/profiles/corpusiq/skills/play-policy-insights
```

The checkout holds 36 skill directories. Copy deliberately rather than wholesale: several directories carry large reference trees, and 36 skill descriptions competing for routing attention is a real cost.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| edge-to-edge | 3,380 | Adding adaptive edge-to-edge display support, and fixing content hidden behind the navigation bar, status bar or IME. |
| navigation-3 | 3,374 | Installing and migrating to Jetpack Navigation 3, including deep links, multiple backstacks, scenes and Hilt integration. |
| r8-analyzer | 3,362 | Auditing R8 keep rules for redundancy, over-broad package rules and rules that already subsume library consumer rules. |
| android-cli | 3,111 | Driving the android command line tool for project creation, emulator control, screenshots and skill installation. |
| testing-setup | 2,687 | Building a testing strategy and standing up unit, UI, screenshot and end-to-end harnesses. |
| adaptive | 2,615 | Making one UI adapt across phones, tablets, foldables, desktop, TV, Auto and XR while preserving UI and playback state. |
| migrate-xml-views-to-jetpack-compose | 2,475 | Running a staged XML View to Compose migration that keeps interoperability intact. |
| styles | 2,201 | Index listing only; no matching skill directory in the current tree, so its behavior is unconfirmed from source. |
| play-billing-library-version-upgrade | 1,969 | Moving any legacy Play Billing Library version to the current stable release. |
| android-intent-security | 1,862 | Auditing manifest components and Intent handling for redirection and unauthorized access. |
| appfunctions | 1,676 | Exposing app workflows as AppFunctions so agents, voice commands and shortcuts can run them without the UI. |
| display-glasses-with-jetpack-compose-glimmer | 1,599 | Building projected Android XR apps for display glasses with the Jetpack Compose Glimmer toolkit. |
| engage-sdk-integration | 1,591 | Integrating, debugging and fixing Play Engage SDK publishing code and entity mapping. |
| verified-email | 1,565 | Adding OTP-free verified email retrieval through the Credential Manager API. |
| play-policy-insights | 1,442 | Cross-checking code against Play Store declarations for data safety, permissions and identity policy gaps. |
| agp-9-upgrade | 1,361 | Migrating a project to Android Gradle Plugin 9. |
| camerax | 1,314 | Implementing CameraX capture, asynchronous recording lifecycles and ML Kit or Media3 effect wiring. |
| wear-compose-m3 | 1,293 | Building or migrating Wear OS apps to Compose Material 3, including the Horologist migration. |
| android-profiler | 1,208 | Recording and analyzing Perfetto traces, heap profiles and CPU stacks to find jank, ANRs and battery drain. |
| media3-cast-integration | 884 | Adding Google Cast to a Media3 app, or migrating off the legacy Cast SDK. |
| leanback-to-compose-tv-migration | 884 | Moving Android TV apps from Leanback and Views to Jetpack Compose for TV. |

The remaining 14 indexed listings range from 241 to 820 installs.

## Why This Matters for Hermes Agents

Most agent coding failures on Android are not comprehension failures, they are recency failures. AGP 9, Navigation 3, Play Billing deprecations, edge-to-edge enforcement and the Glimmer toolkit are all newer than the bulk of training data, and an agent that writes plausible-looking pre-2025 Android code produces a build that fails at exactly the step a human would have to debug. This suite exists to patch that gap with the vendor's own instructions rather than with a third party's summary.

The structure suits a Hermes profile well. Skills activate on task description, so an agent asked to fix a navigation bar overlap picks up `edge-to-edge` without being told the name, and an agent asked to shrink an APK picks up `r8-analyzer`. Because each skill is a directory with a narrow description and, in many cases, a `references/` copy of the official documentation, an installed skill gives the agent quotable source material instead of a paraphrase.

The auditing skills are the ones with the clearest payoff for non-UI work. `play-policy-insights` cross-references static code analysis against Play Store declarations across permissions, identity and data safety, `android-permissions-security` and `android-intent-security` cover the two most common Android attack surfaces, and `anr-audit-and-fix` reads stack dumps rather than guessing. For anyone shipping to Play, those three convert a review rejection into a fix list.

The license matters here too. Apache-2.0 from Google means the content can be vendored into a private profile, copied into a monorepo and read by an agent in CI without a legal conversation, which is not true of most of the community skill repos this catalog covers. The one caveat is the Snyk Warn on the installer skill, covered below.

## Usage

| You say | What happens |
|---|---|
| "My list is sliding under the gesture bar on Android 15" | The agent picks up `edge-to-edge`, migrates the Compose app to inset-aware layout and fixes the IME and system bar legibility cases. |
| "Our APK ballooned after we added the new SDK" | `r8-analyzer` reads the build files and keep rules, flags package-wide rules and rules that duplicate library consumer rules, and proposes a trimmed set. |
| "Will this release pass Play data safety review?" | `play-policy-insights` compares the code against the store declarations and reports undeclared collection, missing disclosures and architectural risk per policy domain. |
| "We are still on Play Billing 5, upgrade us" | `play-billing-library-version-upgrade` walks the migration to the current stable library, including the API changes between versions. |
| "The settings screen hangs for two seconds" | `android-profiler` records a trace, analyzes it for jank and main thread stalls, and points at the offending frames. |
| "Port this phone app to the TV" | `leanback-to-compose-tv-migration` maps Leanback fragments, presenters and adapters onto Compose for TV equivalents with focus memory intact. |
| "Set up tests, we have none" | `testing-setup` picks the layers, adds the dependencies and generates unit, UI, screenshot and end-to-end harnesses. |

## Verification

The raw path below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} edge-to-edge\n" \
  https://raw.githubusercontent.com/android/skills/main/system/edge-to-edge/SKILL.md
```

Expect `200`. To confirm the tree holds what the README claims, count the skill files in a fresh clone:

```bash
git clone --depth 1 https://github.com/android/skills.git /tmp/android-skills
find /tmp/android-skills -name SKILL.md | wc -l
```

Expect `36`. After a copy into the profile, confirm the frontmatter survived and that no reference tree was dropped:

```bash
head -8 ~/.hermes/profiles/corpusiq/skills/play-policy-insights/SKILL.md
find ~/.hermes/profiles/corpusiq/skills/play-policy-insights -type f | wc -l
```

A good copy shows `name: play-policy-insights`, a one-line description and a `metadata:` block with `author: Google LLC` and `last-updated`. If the second count is 1, only the markdown came across and the `references/` tree did not, which is the common failure when a copy follows a symlink or skips hidden paths.

## Security

One sampled skill, android-cli, carries a Snyk Warn while the other four samples Pass on all three auditors, so the installer is the one skill to read before you run it, and a Warn is not a Fail: it flags behavior worth inspecting rather than a known compromise.

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| edge-to-edge | Pass | Pass | Pass |
| navigation-3 | Pass | Pass | Pass |
| r8-analyzer | Pass | Pass | Pass |
| android-cli | Pass | Pass | Warn |
| anr-audit-and-fix | Pass | Pass | Pass |

Five of 35 listings were sampled, so the table describes a sample and not the suite. Across the whole tree the surface is still small: most skill directories hold markdown and bundled docs with no executable code, and Python appears in exactly two. `play-policy-insights` ships five scripts, including a Play Store page scraper and a report generator, and `r8-analyzer` ships three, one of them a generated protobuf module that converts R8 keep-radius output to JSON. Both are Apache-2.0 AOSP files, but they are the two places where reading the markdown is not the same as reviewing what runs. The sampled Warn sits on `android-cli`, and that exception is structural rather than suspicious: the skill exists to drive a command line tool that creates projects, installs APKs onto devices and manages SDK components, so any auditor reading it will see device and filesystem operations by design. Read that one before granting it a device.

The larger point of trust here is provenance. This is a Google-published Apache-2.0 repository with a visible commit history and a vendor documentation trail behind each skill, which is a different risk profile from an unattributed skill that asks for network access. The residual risk is the ordinary one: skills instruct an agent to run builds, install packages and touch devices, so scope what the agent can reach rather than what the markdown says.

## Limitations

- Snapshot data, verified 2026-10-30: 48,501 combined installs across 35 indexed listings; 10,111 GitHub stars; Apache-2.0; last pushed 2026-10-29. Counts drift over time.
- The index and the tree disagree in both directions. Five listings have no matching skill directory in the checkout (`styles`, `camera1-to-camerax`, `jetpack-compose-m3`, and `perfetto-trace-analysis` and `perfetto-sql`, which exist only as workflow files inside `android-profiler`), while six directories have no skills.sh listing at all (`litert-lm`, `mlkit-agent-api`, `ink-app-builder`, `ink-custom-brush-builder`, `projected-hardware`, `glance-appwidget-updates-and-memory`). Install from the tree, not from the install counts.
- The counts are not a ranking. The spread is flat, 3,380 at the top and 241 at the bottom of the index, because these are one vendor suite published at once rather than independent projects competing for attention. The number beside a skill says how often it was pulled, not how good it is.
- Installation assumes the `android` CLI. The README does not install it, only links to developer.android.com/tools/agents/android-cli, and no Hermes-specific route is documented, so a profile without that tool is limited to copying directories by hand.
- Only five of 35 listings carry audit results, and one of the five is a Warn. The other 30 skills have no published verdict to check.
- Contributions are closed. The README states that public contributions are not accepted and asks for GitHub issues instead, so a wrong instruction has to be worked around locally rather than patched upstream.

## Related

- [Solana Mobile Skills - Android Wallet Dev Setup](/hermes/skills/catalog/solana-mobile-skills-setup)
- [Capgo Skills - Capacitor Mobile Release Suite Setup](/hermes/skills/catalog/capgo-skills-setup)
- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `android-cli` first even if you want others. It is what the CLI adds when `--all` is omitted, and it is the skill that teaches an agent to create projects, drive emulators and take screenshots, which every other skill assumes.
- Read the "Don't use for" clause in each description before installing. Google wrote explicit exclusions, for example `r8-analyzer` excludes general Gradle errors and Compose performance, `agp-9-upgrade` excludes Kotlin Multiplatform, and the Glimmer skill excludes audio-only glasses and non-glasses XR headsets, so honoring them keeps routing clean.
- Copy the skill directory whole, including `references/`. The bundled developer.android.com pages are the part that makes the answers quotable, and a markdown-only copy silently loses them.
- Run `play-policy-insights` before a submission, not after a rejection. It is the only skill in the suite that compares code to the declarations already filed in Play Console, which is where most data safety rejections originate.
- Prefer `android skills update <name>` over re-copying. It respects the install root and agent list you used the first time, so the directory layout does not drift between updates.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
