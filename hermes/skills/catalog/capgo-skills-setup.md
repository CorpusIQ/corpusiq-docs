---
title: "Capgo Skills - Capacitor Mobile Release Suite Setup"
description: "Capgo's Capacitor suite: 45.4K combined installs. OTA live updates, native builds, plugin wiring, and store release skills for mobile agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/capgo-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "capacitor", "mobile devops", "live updates"]
---

# Capgo Skills - Setup Guide

**Source:** [cap-go/capgo-skills](https://www.skills.sh/cap-go/capgo-skills) via skills.sh - 45.4K combined installs across 55 indexed listings; snapshot 2026-10-27 (Oct 27 evening sweep)

**GitHub:** [Cap-go/capgo-skills](https://github.com/Cap-go/capgo-skills) - 73 stars, MIT, branch main, 55 canonical skill directories under `skills/` mirrored byte for byte into 11 plugin groups under `plugins/<plugin>/skills/`, for 113 `SKILL.md` files in the clone

**Category:** Mobile app delivery for Capacitor, iOS and Android, with OTA updates

**Quality Tier:** 🟡 Beta - vendor maintained, 73 GitHub stars, 55 indexed listings against 55 canonical skill directories, security verdicts not audited this sweep

Capgo sells the operational half of Capacitor: maintained plugins, cloud native iOS and Android builds, live updates with channels and rollback, and release monitoring. This repository is that company's skill set for AI coding agents, formerly published as `@capgo/capacitor-skills`, and it covers the whole lifecycle of a mobile app rather than a single library. The README organizes it by stage (build, plugins, migrate, upgrade, debug, test, security, publish, live updates) and ships 11 plugin groups for the Claude Code, Cursor and Codex marketplaces, with the same directories copied under `skills/` for any agent that reads `SKILL.md` files directly.

The design worth noticing is the routing layer. `capgo-cli-usage` and `capgo-cloud` are dispatch skills: they map the CLI surface and hand off to narrower skills instead of doing the work themselves, and most specialists end their own description with explicit "do not use for" clauses naming the sibling that should handle the request. Version awareness is built in as well. `capacitor-best-practices` tracks Capacitor 8.5 stable with 9 in alpha, `ionic-design` covers Ionic 9 while noting Ionic 8 is still common, and the upgrade family ships one skill per major step from v4 to v9 for both apps and plugins.

## Installation

The README leads with the skills.sh CLI, which installs from the repository into the agent's skill directory:

```bash
npx skills add Cap-go/capgo-skills
```

Claude Code users can instead add the repository as a plugin marketplace and install the groups they need:

```bash
claude plugin marketplace add Cap-go/capgo-skills
claude plugin install capgo-cloud@capgo-skills
```

Gemini CLI installs the repository as an extension:

```bash
gemini extensions install https://github.com/Cap-go/capgo-skills
```

Cursor and Codex use the same plugin groups through their own manifests, `.cursor-plugin/marketplace.json` and `.agents/plugins/marketplace.json`. Add the repository as a marketplace in either tool, then install from the group list.

For any other agent, the tree itself is the install source. Each directory under `skills/` holds one `SKILL.md` plus its `references/` folder, so a clone and a copy of the directories you want is equivalent to a CLI install of those skills:

```bash
git clone --depth 1 https://github.com/Cap-go/capgo-skills.git
cp -R capgo-skills/skills/capgo-live-updates ~/.hermes/profiles/corpusiq/skills/
```

The updater skills assume the Capgo MCP server or CLI is reachable. Two options are documented in `capacitor-mcp`: the hosted server at `https://api.capgo.app/mcp` over streamable HTTP with OAuth or an API key, and the local CLI server started with `npx @capgo/cli@latest mcp`, which can read the local project but needs `npx @capgo/cli@latest login` first.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| capacitor-best-practices | 2,697 | Reviewing a Capacitor codebase against current practice: a `capacitor.config.ts` audit, new project setup, and aligning `@capacitor/core`, `cli`, `ios`, `android` and plugin majors across 8.5 stable and 9 alpha. |
| ionic-design | 1,596 | Building or reviewing Ionic UI inside a Capacitor app: page structure with `ion-header`, `ion-content` and `ion-footer`, lists, modern form syntax, sheet modals and tabs on Ionic 9 or the still-common Ionic 8. |
| capacitor-plugins | 1,591 | Choosing, installing and wiring native-feature plugins: camera, filesystem, geolocation, biometrics, in-app purchases, social login, SQLite, contacts, health, BLE and NFC, official packages plus Capgo recommendations. |
| debugging-capacitor | 1,348 | Diagnosing runtime failures: white or blank screen on launch, startup crashes, a plugin reported as not implemented on one platform, cleartext and App Transport Security blocks, and CORS on the local WebView origin. |
| capacitor-testing | 1,306 | Setting up web-layer unit and component tests with Vitest and mocked plugins, Playwright against the web build, and Appium end-to-end runs with the native and WebView context switch. |
| safe-area-handling | 1,306 | Fixing notch, Dynamic Island, home indicator and system bar overlap with `viewport-fit=cover`, the safe-area inset environment variables, and the Capacitor 8 SystemBars insets handling. |
| capacitor-deep-linking | 1,280 | Implementing and debugging universal links and app links: the association file and Associated Domains entitlement on iOS, asset links with autoVerify on Android, and routing through the app URL open event. |
| ios-android-logs | 1,269 | Streaming, filtering and saving device logs and crash reports from simulators, emulators and physical devices, including why iOS bridge output never reaches the system console. |
| capacitor-security | 1,225 | Running an app-layer security audit: the Capsec scanner and its rule IDs, secrets inlined into the web bundle, token storage, CSP, certificate pinning, root detection and cleartext settings. |
| capacitor-accessibility | 1,218 | Making an app work with VoiceOver, TalkBack, Dynamic Type, Android font scale, Switch Control, hardware keyboards, Reduce Motion and Increase Contrast. |
| capacitor-performance | 1,191 | Fixing slow cold starts and long splash screens, white screens after the camera or backgrounding kills the WebView process, large base64 bridge payloads and long list rendering. |
| capacitor-app-store | 1,168 | Preparing and submitting a release: build numbers, signing, archiving and uploading the IPA or AAB, TestFlight, Play tracks and closed testing, icons and screenshots. |
| capacitor-splash-screen | 1,125 | Configuring launch splash screens with the splash-screen plugin and the assets tool, including auto-hide behaviour, the fade-out default change and the Android 12 splash API. |
| capacitor-push-notifications | 1,102 | Setting up and debugging remote push with FCM and APNs: APNs keys, the push capability, entitlements, or the Capgo Firebase messaging and notifications alternatives. |
| capacitor-offline-first | 1,070 | Designing offline-first data: local SQLite as the source of truth through the Capgo fast-sql plugin, an outbox sync queue, delta pulls, conflict resolution and network status handling. |
| capacitor-keyboard | 1,019 | Fixing on-screen keyboard behaviour: iOS resize modes, keyboard height events, accessory bar visibility, scroll and style options, and the Ionic-specific workarounds. |
| capacitor-ci-cd | 964 | Designing or repairing pipelines on GitHub Actions, GitLab CI, Fastlane or Capgo Cloud Build: web build and tests, native sync, iOS archive and export, Android bundling, and signing secrets in CI. |
| tailwind-capacitor | 962 | Setting up Tailwind CSS v4 in a Capacitor app: CSS-first configuration, the Vite and PostCSS plugins, and upgrading from a v3 config file. |
| capacitor-mcp | 919 | Wiring MCP servers for Capacitor and Ionic work: the community Ionic server, the Capgo hosted and local CLI servers, and Xcode's bridge, plus diagnosing servers that connect with no tools. |
| capacitor-apple-review-preflight | 900 | Auditing an iOS app against App Review Guidelines before submission or after a rejection, including minimum functionality, Sign in with Apple, data collection and account deletion. |
| framework-to-capacitor | 874 | Configuring a web framework build so Capacitor can ship it: Next.js static export, Nuxt 4, Angular output paths and SvelteKit adapter-static. |
| capgo-live-updates | 853 | Installing and debugging the Capgo updater plugin: autoUpdate modes, the ready callback, manual download and next flows, channel assignment, and the error codes behind updates that never apply. |

The remaining 33 indexed listings range from 51 to 838 installs. konsta-ui (838) and cocoapods-to-spm (799) sit closest to the cut, followed by the operational Capgo skills `capgo-native-builds` (715), `capgo-release-workflows` (712), `capgo-release-management` (710) and `capgo-cloud` (695), the plugin upgrade ladder from v4 to v9 (629 to 638), the Cordova, Appflow, Ionic Enterprise SDK and Capawesome migrations, and seven smaller listings between 51 and 55 installs led by `capacitor-ios-resizability` (55) and ending at `capawesome-live-update-migration` (51).

## Why This Matters for Hermes Agents

Mobile delivery is the part of a build where an agent can do real damage without raising an error. A wrong channel assignment ships the wrong bundle, a missing ready callback makes every update roll back, and a cleartext allowance added to fix a local test reaches production. This suite exists because those decisions have known correct answers, and the skills state them as procedures rather than advice.

The version discipline is the clearest gain. The updater's major version tracks the Capacitor major, and `capgo-live-updates` lists the exact install line per major and warns that the `9.0.0` package on npm is a deprecated 2023 release for Capacitor 5, not a Capacitor 9 line. An agent working from memory would happily install it and report success.

The security skill is directly useful for agent work as well. `capacitor-security` builds the web app, then greps the output for inlined environment values, which is exactly where API keys leak when a bundler substitutes `import.meta.env` at build time. It also tells the agent to triage and report before making invasive changes such as certificate pinning, which can lock users out when certificates rotate.

For unattended runs, the most valuable content is the stop list. The Capgo skills instruct agents not to accept API keys, signing passwords, `.p8` keys, keystores or service-account JSON in chat, and to confirm before anything that mutates remote state: uploading a bundle, promoting or changing a channel, deleting apps, bundles or keys, or requesting a build that publishes to a store. Carrying those instructions into a Hermes session is cheaper than discovering them after an agent has already promoted a channel.

## Usage

| You say | What happens |
|---|---|
| "Ship a hotfix without waiting for App Store review" | capgo-live-updates confirms the Capacitor major, installs the matching updater line, places the ready callback in the app entry point, and uploads the first bundle after asking before it touches remote state. |
| "Users get a white screen after the splash on Android" | debugging-capacitor works through the known causes in order: WebView process kill, plugin not registered on that platform, cleartext or transport security, and renders a diagnosis with the files it inspected. |
| "Audit this app for leaked keys before we submit" | capacitor-security runs the Capsec scan from the project root, greps the built bundle for inlined environment values, then reports findings by severity with file and line before any fix. |
| "Set up push notifications on both platforms" | capacitor-push-notifications wires FCM and APNs, the push capability and entitlements, then covers the delivery checks that separate a configured key from a working notification. |
| "Our CI uploads fail with no API key found" | capacitor-ci-cd and capgo-release-workflows resolve the credential precedence, check that the token is exported into the step environment, and pin the CLI version for reproducibility. |
| "Why did this update roll back on half the devices" | capgo-live-updates maps the reported error code to its cause: no new version on that channel, a blocked major-version update, a private channel mismatch, or an on-premise build, then fixes the cause rather than the symptom. |
| "We are on Cordova, move us to Capacitor" | framework-to-capacitor or cordova-to-capacitor takes the migration, with cocoapods-to-spm for the iOS dependency swap and capacitor-app-upgrades for the version ladder afterwards. |

## Verification

Probe the paths you plan to install from. The canonical tree and the plugin mirrors both exist on main, and all five URLs below returned 200 when this guide was written:

```bash
for p in skills/capgo-live-updates/SKILL.md \
         skills/capacitor-security/SKILL.md \
         skills/capacitor-mcp/SKILL.md \
         skills/capacitor-best-practices/SKILL.md \
         plugins/capgo-cloud/skills/capgo-live-updates/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/Cap-go/capgo-skills/main/$p"
done
```

Read the two that touch credentials and remote state before installing them:

- https://raw.githubusercontent.com/Cap-go/capgo-skills/main/skills/capgo-live-updates/SKILL.md
- https://raw.githubusercontent.com/Cap-go/capgo-skills/main/skills/capacitor-security/SKILL.md

After install, each skill appears as one directory with its own `SKILL.md`. Confirm what actually landed before relying on a skill being present, since the CLI decides what it copies:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -cE '^(capacitor|capgo)-'
head -5 ~/.hermes/profiles/corpusiq/skills/capgo-live-updates/SKILL.md
```

The `head` output should show the frontmatter name `capgo-live-updates`, which is also the name the install index uses, so a mismatch there means you are reading a stale copy.

## Security

skills.sh verdicts from the Gen Agent Trust Hub, Socket and Snyk auditors were not sampled this fire, so every cell below reads Not checked. Open each skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| capacitor-best-practices | Not checked | Not checked | Not checked |
| ionic-design | Not checked | Not checked | Not checked |
| capacitor-plugins | Not checked | Not checked | Not checked |
| debugging-capacitor | Not checked | Not checked | Not checked |
| capacitor-testing | Not checked | Not checked | Not checked |
| safe-area-handling | Not checked | Not checked | Not checked |
| capacitor-deep-linking | Not checked | Not checked | Not checked |
| ios-android-logs | Not checked | Not checked | Not checked |
| capacitor-security | Not checked | Not checked | Not checked |
| capacitor-accessibility | Not checked | Not checked | Not checked |
| capacitor-performance | Not checked | Not checked | Not checked |
| capacitor-app-store | Not checked | Not checked | Not checked |
| capacitor-splash-screen | Not checked | Not checked | Not checked |
| capacitor-push-notifications | Not checked | Not checked | Not checked |
| capacitor-offline-first | Not checked | Not checked | Not checked |
| capacitor-keyboard | Not checked | Not checked | Not checked |
| capacitor-ci-cd | Not checked | Not checked | Not checked |
| tailwind-capacitor | Not checked | Not checked | Not checked |
| capacitor-mcp | Not checked | Not checked | Not checked |
| capacitor-apple-review-preflight | Not checked | Not checked | Not checked |
| framework-to-capacitor | Not checked | Not checked | Not checked |
| capgo-live-updates | Not checked | Not checked | Not checked |

The execution surface is narrow at install time and wide at run time. The repository's `package.json` has no lifecycle hooks, so adding the skills does not run code; what runs later is the CLI the skills tell the agent to invoke, and the skills do that 101 times across the tree with `npx @capgo/cli@latest`, plus 4 times with `npx @capgo/capgo-sec@latest`. Both fetch the newest package from npm on every invocation, so pin an exact version in any pipeline that matters.

Credentials are handled by name and by precedence, which is where the practical risk sits. The CLI resolves an API key from `--apikey`, then `CAPGO_TOKEN`, then `~/.capgo`, then `./.capgo` in the project, and the global key wins over the project key, so an agent on a multi-account machine can act against the wrong organization while every command reports success. The skills respond by telling agents to run `npx @capgo/cli@latest login` themselves, to keep `.capgo` out of git, and never to ask for an API key, signing password, `.p8` key, keystore or service-account JSON in chat.

Two write paths deserve their own review. Live updates are a code delivery channel: uploading a bundle or promoting a channel changes what runs on installed devices, and encrypted bundles add a private key to the release pipeline. Native builds and store submission add signing material on top of that. The MCP path is the other one: `capacitor-mcp` edits client configuration files such as `.cursor/mcp.json`, `.vscode/mcp.json` and the Claude Desktop config, and the hosted Capgo server holds account authority over apps, bundles, channels, devices and webhooks, so scope its token as you would a deploy credential.

## Limitations

- Snapshot data, verified 2026-10-27: 45,408 combined installs across 55 indexed listings; 73 GitHub stars; MIT; branch main. Counts drift over time.
- 113 `SKILL.md` files back 55 indexed listings: 55 canonical skills, 56 byte-for-byte plugin copies (one skill appears in two plugin groups), and two copies of the `broken-skill` fixture that `skill-creator` uses for validation. Install one surface, not both, or the same skill is indexed twice.
- The repository is more than skills. The root carries `AGENTS.md` and `CLAUDE.md` with contributor instructions that assume `bun`, and `scripts/` with the manifest generator and the skill sync script. None of that is skill content and none of it installs with the skills.
- Version coverage has a gap at the top. The upgrade ladder ships per-major skills from v4 to v9, but there is no updater line for Capacitor 9 as of October 2026, and the skill says the `9.0.0` package on npm is a deprecated 2023 release for Capacitor 5.
- The documented install paths are skills.sh, Claude Code, Gemini CLI, Cursor and Codex. Nothing documents a per-skill install for other agents, so on Hermes the copy route is the only one available, and it brings no slash commands, hooks or MCP wiring with it.
- Skill behaviour depends on the CLI version resolved at run time, because the instructions use `@latest` throughout. A skill that worked last month can describe a flag the current CLI no longer has, or miss one it added.

## Related

- [Capawesome Skills - Capacitor and Ionic Ecosystem Suite Setup](/hermes/skills/catalog/capawesome-skills-setup)
- [React Native Update Skill - OTA Update Integration Setup](/hermes/skills/catalog/react-native-update-skill-setup)
- [App Store Connect CLI - Mobile Release Automation Setup](/hermes/skills/catalog/app-store-connect-cli-skills-setup)
- [Xcode Build Optimization - iOS Build Performance Setup](/hermes/skills/catalog/xcode-build-optimization-setup)

## Pro Tips

- Install the plugin group, not the whole tree, when you know the job. `capacitor-quality` alone carries testing, debugging, logs, performance, accessibility and security, and the rest of the set cost context on every turn.
- Start with `capgo-cli-usage` for anything CLI-shaped. It is the dispatch skill, it knows the key precedence order, and it sends you to the narrow skill instead of making you guess which of the eleven groups owns the task.
- Ask the agent to print what it inspected before it edits. Every one of these skills opens with a read step (config file, manifest, entitlements, build output), and asking for that list catches the case where it audited the wrong project.
- When a live update fails, quote the error code from the skill's own table rather than describing the symptom. The codes separate a missing version from a channel mismatch from a blocked major upgrade, and the fix differs for each.
- Keep `CAPGO_TOKEN` in the environment and `.capgo` in `.gitignore` for anything automated. The global key winning over the project key is the failure that looks like a permissions bug and is not.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
