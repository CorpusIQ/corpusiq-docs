---
title: "Superwall Skills - iOS Paywall Setup"
description: "superwall/skills on skills.sh: 11.4K combined installs across 12 listings; Superwall CLI, paywall editor, React paywall framework and WWDC lookup."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/superwall-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "paywalls", "ios", "swiftui"]
---

# Superwall Skills - Setup Guide

**Source:** [superwall/skills](https://www.skills.sh/superwall/skills) via skills.sh - 11.4K combined installs across 12 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 30 stars, MIT licence, last pushed 2026-11-05, 10 SKILL.md directories under skills/ and plugins/superwall/skills/
**Category:** Subscription paywalls for mobile apps: Superwall CLI resources, paywall authoring, onboarding funnels and WWDC research
**Quality Tier:** 🟡 Beta - Snyk Warn on the three sampled skills; MIT; 30 stars.

Superwall publishes official agent skills for integrating its SDKs, managing account resources, analyzing revenue data and building paywalls. The repository splits into a CLI and account skill (`superwall`), a browser-driven paywall editor (`superwall-editor`), a code-first framework skill (`superwall-framework`) that authors paywalls and onboarding as React mini-apps, a mobile design skill, two onboarding funnel skills, and a `wwdc` skill that looks up Apple developer session content.

The same skills ship twice in the tree, once at `skills/<name>` and once inside `plugins/superwall/skills/<name>`. The plugin route bundles them with the authenticated Superwall MCP connector for Claude, Codex and other Agent Plugins clients; the standalone skills.sh install described below remains available and is what the README recommends.

## Installation

The README recommends the skills.sh CLI and installs everything for all frontier agents:

```bash
npx skills add superwall/skills --agent claude-code universal --global --yes
```

A single skill installs with `--skill`:

```bash
npx skills add superwall/skills --skill superwall --agent claude-code universal --global --yes
```

The `superwall` CLI itself is installed once by the user, and the agent is told to use the installed binary rather than upgrading it:

```bash
npm install --global superwall
superwall login
superwall whoami --json
```

For CI, the README authenticates without a browser:

```bash
superwall login --api-key <key>
```

The `superwall-framework` skill is a public beta that `superwall login` and `superwall skills` install from `main`. The README also documents installing it by hand:

```bash
npx skills add https://github.com/superwall/skills --skill superwall-framework --global --yes --agent claude-code universal --full-depth
```

## What It Provides

Three listings clear the 500 install threshold.

| Skill | Installs | Use For |
|---|---|---|
| superwall | 4,623 | Driving the CLI across apps, products, entitlements, campaigns, paywalls, App Store Connect, Apple Search Ads and ClickHouse analytics |
| superwall-editor | 3,695 | Driving the visual paywall editor over a pairing code, marked LEGACY in favor of superwall-framework |
| wwdc | 2,631 | Finding, comparing, citing, summarizing and navigating WWDC session content through wwdc.ai |

The remaining 9 indexed listings range from 11 to 92 installs.

## Why This Matters for Hermes Agents

Paywalls are the highest-leverage screen in a subscription app and the one most likely to be hardcoded. A skill that can create a paywall as a hosted surface means the agent changes copy, pricing or layout without a release, which is the whole argument for using Superwall in the first place.

The pack is also honest about its own history. `superwall-editor` is still the second most installed listing, and its description now opens with LEGACY and redirects agents to `superwall-framework` for any screen an agent builds. That is a useful example of versioning guidance inside a skill file instead of a changelog nobody reads.

The `superwall` skill carries the account side, including App Store Connect keys, server notifications, revenue provider configuration and ClickHouse analytics, and the README notes that agents should pass `--json` to data and mutation commands. Machine-readable output is what makes an account skill usable in a pipeline.

The `wwdc` skill is a small but practical addition: citing an Apple session by ID is a common research task for mobile work, and a skill that resolves session content beats a model recalling a talk from training data.

## Usage

| You say | What happens |
|---|---|
| "Set up Superwall in this iOS app" | superwall walks the integration playbook for the app's framework and adds placements |
| "Create a paywall for the pro tier" | superwall-framework authors the paywall as code and registers it behind a placement |
| "Change the headline on the onboarding paywall" | the agent edits the surface rather than the binary, so no release is needed |
| "Which products and entitlements exist for this app?" | superwall queries the account through the CLI with `--json` |
| "Connect App Store Connect and pull revenue" | superwall walks the key, server notification and revenue provider setup |
| "Summarize the WWDC session on SwiftUI navigation" | wwdc resolves the session and cites the transcript |
| "Make this web screen feel native in the app" | mobile-design applies press feedback, keyboard handling and iOS versus Android conventions |

## Verification

Fetch the account skill and confirm the frontmatter covers the CLI surface:

```bash
curl -fsSL https://raw.githubusercontent.com/superwall/skills/main/skills/superwall/SKILL.md | head -6
```

The response should open with `name: superwall` and a description naming the CLI, App Store Connect and ClickHouse. Then confirm the CLI session is live:

```bash
superwall whoami --json
```

Finally, check that the install created one directory per skill:

```bash
ls ~/.claude/skills | grep superwall
```

Both `superwall` and `superwall-editor` should be present, along with any of the `next`-channel skills you installed deliberately.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| superwall | Pass | Pass | Warn |
| superwall-editor | Pass | Pass | Warn |
| wwdc | Pass | Pass | Warn |
| superwall-flutter-quickstart | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified 2026-11-04: 11,365 combined installs across 12 indexed listings; 30 GitHub stars; MIT licence; last pushed 2026-11-05. Counts drift over time.
- skills.sh indexes 12 listings against 10 skill directories, and the tree duplicates `superwall` and `superwall-editor` under both `skills/` and `plugins/superwall/skills/`, so identical skills appear under more than one name.
- `superwall-editor` is marked LEGACY in its own description yet still draws 3,695 installs. Use `superwall-framework` for any screen an agent builds, and the editor only for pairing with an existing browser session.
- `mobile-design`, `onboarding-questions` and `animate-onboarding` are described in the README as `next` only, so they are not the stable channel. Install them deliberately rather than as part of an all-skills pull.
- All three sampled skills carry a Snyk Warn. The only clean sample is `superwall-flutter-quickstart`, which has no matching directory in the pack's layout listing.
- Account commands need a live login, and the session is stored under `~/.superwall`. Treat that directory as a credential and never bake it into an image.

## Related

- [SwiftUI Agent Skill - Apple UI Development Setup](/hermes/skills/catalog/avdlee-swiftui-agent-skill-setup)
- [Swift iOS Skills - iOS 26 and SwiftUI Suite Setup](/hermes/skills/catalog/dpearson-swift-ios-skills-setup)
- [Swift Testing Pro Skill - Swift Testing Suite Setup](/hermes/skills/catalog/swift-testing-pro-skill-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `superwall-framework`, not the editor, for new work. The editor is for pairing with a browser session that already exists; everything an agent builds should be React code.
- Run `superwall whoami --json` before any account task. It catches an expired session in one call instead of halfway through a campaign edit.
- Keep the CLI version pinned in CI and authenticate with `--api-key`. The README expects the user to install and upgrade the CLI, not the agent.
- Ask for `--json` output on data commands and parse it. Prose tables are for humans and break the moment a column is added.
- Use `wwdc` for citation rather than recall. Session IDs and API names from training data are frequently wrong, and the skill resolves the real page.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
