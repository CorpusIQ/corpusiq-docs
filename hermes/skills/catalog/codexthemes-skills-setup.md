---
title: "CodexThemes Skills - Theme Build and Install Setup"
description: "codexthemes/skills on skills.sh: 5.2K combined installs across 6 listings; create, find, install and submit Codex desktop themes."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/codexthemes-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "codex", "theming", "desktop"]
---

# CodexThemes Skills - Setup Guide

**Source:** [codexthemes/skills](https://www.skills.sh/codexthemes/skills) via skills.sh - 5.2K combined installs across 6 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 7 stars, Apache-2.0 licence, last pushed 2026-07-21, six skill directories under `skills/<name>/SKILL.md`, each with `agents/openai.yaml` and `scripts/`
**Category:** Codex desktop theming for agents: create, find, install and submit native-safe themes
**Quality Tier:** 🟡 Yellow - Socket and Snyk both Warn on codex-theme-switcher and codex-theme-installer; Apache-2.0, 7 stars.

CodexThemes Skills is the official skill set for theming the Codex desktop app. The repository describes itself as the canonical source for the skill served through `codexthemes.ai/SKILL.md`, and it deliberately ships no bundled artwork: no celebrity images, no third-party themes, no copied screenshots, no generated theme packages and no private user assets.

The set splits into two halves. Creation and application are local: `codex-theme-creator` scaffolds a theme from a brief or reference image in one of four explicit modes, and `codex-theme-switcher` applies, hot-swaps and restores it from the local `~/.codexthemes` library. Distribution is networked: `codex-theme-finder` searches the published gallery, `codex-theme-installer` downloads a theme's source files, and `codex-theme-submitter` publishes an exported package through the authenticated API. A sixth skill converts Codex theme packages into the separate Tencent WorkBuddy format.

The runtime story matters more than the feature list. Theme creation, validation, session application and restore are self-contained TypeScript workflows that talk to Codex's loopback-only debugging endpoint, never patch the signed app bundle, and do not depend on CodeDrobe, Dream/Fiona or any other theme injector.

## Installation

Install the creator globally for Codex, which is the entrypoint most users start with:

```bash
npx skills add codexthemes/skills --skill codex-theme-creator -g -a codex
```

Drop the `-g` to install into the current project instead:

```bash
npx skills add codexthemes/skills --skill codex-theme-creator -a codex
```

The rest of the set installs the same way, one skill at a time:

```bash
npx skills add codexthemes/skills --skill codex-theme-finder -g -a codex
npx skills add codexthemes/skills --skill codex-theme-installer -g -a codex
npx skills add codexthemes/skills --skill codex-theme-switcher -g -a codex
npx skills add codexthemes/skills --skill codex-theme-submitter -g -a codex
npx skills add codexthemes/skills --skill workbuddy-theme-manager -g
```

List what the repository offers, and update an installed copy:

```bash
npx skills add codexthemes/skills --list
npx skills update codex-theme-creator
```

An agent can also be handed the website entrypoint directly, which tells it to load the canonical skill and its references from this repository:

```text
https://codexthemes.ai/SKILL.md
```

One migration note from the README: the creator skill was previously named `new-theme`. Reinstall under the new name and remove the old local directory if both are present, because keeping both makes skill routing ambiguous.

## What It Provides

Three listings carry nearly all of the installs; the other three are the distribution and conversion skills.

| Skill | Installs | Use For |
|---|---|---|
| codex-theme-switcher | 1,748 | Applying, switching and restoring themes from the local library, hot-swapping a running app or scheduling a restart-surviving relaunch, verifying against the real DOM |
| codex-theme-installer | 1,717 | Downloading a published theme from codexthemes.ai and installing its source files into `~/.codexthemes/themes/<id>/` |
| codex-theme-creator | 1,382 | Creating, redesigning, validating, previewing and packaging a theme from a visual brief or reference image across four layout modes |

The remaining 3 indexed listings range from 22 to 227 installs.

## Why This Matters for Hermes Agents

Desktop theming is a good stress test for an agent that claims to verify its work. A theme either renders correctly across the app's real surfaces or it does not, and the difference shows up in settings, menus, diffs, terminal panes, sidebar hover states and narrow windows rather than in the hero image the theme was designed around. The creator skill defaults to preserving the native layout and names the four modes it is allowed to operate in, so an agent has a bounded contract instead of an aesthetic opinion.

The security posture is unusually explicit for a desktop tool. The README states the runtime uses Codex's loopback-only debugging endpoint, never patches the signed app bundle, and does not touch `app.asar`, WindowsApps, user tasks or authentication data. The creator skill repeats the authority boundary in its own SKILL.md: it is the sole design and QA authority for a new theme, and it must not read or combine another installed theme skill unless the user names that source.

The install and submit half is where agents usually go wrong, and the skills encode the answers. Both gallery skills work anonymously inside a free quota and, on an HTTP 429, guide the user to create an API key at `codexthemes.ai/settings/apikeys`. The submitter checks `CODEXTHEMES_API_KEY` or `~/.codexthemes/credentials.json`, validates the package with a dry run, then posts to the authenticated endpoint. The README is also clear that submitting confirms the uploader's sharing permission and that the skill performs no legal or copyright review.

For a Hermes agent, the practical value is that theming stops being a set of ad hoc CSS injections. Themes live in a managed library with a package format, a validation pass and a restore path, so a failed experiment is reversible without reinstalling the app.

## Usage

| You say | What happens |
|---|---|
| "Use $codex-theme-creator to build a light theme from this image" | Scaffolds a theme in the default native layout mode, validates it, previews it and packages a `.codex-theme` file |
| "Make a native-immersive theme and check every surface" | Keeps the geometry and coordinates all semantic surfaces, then verifies settings, menus, diffs, terminal and narrow windows |
| "Find a dark anime theme on CodexThemes" | Queries the gallery API within the free anonymous quota and lists matching themes |
| "Install the noir-anime theme locally" | Downloads the theme's source files into `~/.codexthemes/themes/<id>/` |
| "Switch Codex to noir-anime" | Hot-swaps the running app if the debugging endpoint is live, otherwise schedules a relaunch, then verifies the result and keeps a restore path |
| "Submit my exported theme to codexthemes.ai" | Checks for an API key, dry-runs validation, then publishes the package through the submit endpoint |
| "Convert this theme to WorkBuddy and apply it" | Builds a `.workbuddy-theme` package under `~/.codexthemes/workbuddy-exports/` and applies it through its own CDP lifecycle |

## Verification

Pull the creator entrypoint from the branch the installer uses:

```bash
curl -fsSL https://raw.githubusercontent.com/codexthemes/skills/main/skills/codex-theme-creator/SKILL.md | head -5
```

It should open with `name: codex-theme-creator` and a description covering creation, validation, preview and packaging. Then confirm the library layout the skills write to:

```bash
ls ~/.codexthemes/themes
ls ~/.codexthemes/exports
```

Editable themes live in `~/.codexthemes/themes/<id>/`, shareable packages in `~/.codexthemes/exports/<id>.codex-theme`, and runtime state in `~/.codexthemes/state/`. To check a clone rather than an install, the README's own validation is:

```bash
npm ci
npm run check
```

That runs strict TypeScript type checking, the bundled metadata validator, and tests for every scaffold mode plus the static theme rejection rules. The repository does not require Python.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| codex-theme-switcher | Pass | Warn | Warn |
| codex-theme-installer | Pass | Warn | Warn |
| codex-theme-finder | Pass | Pass | Warn |
| codex-theme-submitter | Pass | Pass | Pass |
| workbuddy-theme-manager | Pass | Warn | Pass |

Four of the five sampled skills carry at least one Warn. Socket Warns on the switcher, the installer and the WorkBuddy manager; Snyk Warns on the switcher, the installer and the finder. Only `codex-theme-submitter` is clean across all three scanners. Every sampled Gen Agent Trust Hub result is a Pass.

The warnings line up with what the skills actually do: they inject CSS into a running desktop app over a loopback CDP endpoint, download files from a gallery, and write into `~/.codexthemes`. Read the scripts before running them unattended, and treat API keys for `codexthemes.ai` as credentials rather than configuration.

## Limitations

- Snapshot data, verified 2026-11-05: 5,154 combined installs across 6 indexed listings; 7 GitHub stars; Apache-2.0; last pushed 2026-07-21. Counts drift over time.
- Yellow tier follows the sampled audits: Socket and Snyk Warn on `codex-theme-switcher` and `codex-theme-installer`, and Snyk also Warns on `codex-theme-finder`.
- The launcher supports macOS and Windows only. Builds that drop the Chromium debugging flags, such as some store packages, cannot be themed and are reported as such.
- A theme may need to be applied again after a full app quit, because the runtime works through the debugging endpoint rather than by modifying the application bundle.
- The finder and installer are rate limited anonymously; past the free quota they return HTTP 429 and require an API key, and the submitter always needs one.
- Submission confirms the uploader's sharing permission but performs no legal or copyright review, so rights checks stay with the person publishing the theme.
- The repository is small and has not been pushed since 2026-07-21, so it tracks Codex releases at its own pace rather than in lockstep.

## Related

- [Codex - Delegate Coding Tasks to OpenAI Codex CLI](/hermes/skills/catalog/codex-setup)
- [OpenAI Codex Skills - Official Skills Catalog](/hermes/skills/catalog/openai-codex-skills-setup)
- [Hermes Desktop Neo Theme - Setup Guide](/hermes/skills/catalog/hermes-desktop-neo-theme-setup)

## Pro Tips

- Start in `native-background` mode. Changing only scoped artwork and readability veils is the cheapest way to find out whether a reference image survives contact with the real layout.
- Verify on the surfaces the README lists, not on the home page: settings, menus, diffs, terminal panes, sidebar hover states and narrow windows.
- Keep the exports directory as your rollback. A `.codex-theme` package can be reinstalled, but a theme directory you edited in place cannot be reconstructed.
- Create the API key before a batch of installs. Hitting HTTP 429 halfway through a theme sweep is the common failure, and the fix is a settings page rather than a retry.
- Remove the old `new-theme` directory if you installed the creator under its previous name. Two copies of the same skill make routing ambiguous and the symptom looks like the skill being ignored.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
