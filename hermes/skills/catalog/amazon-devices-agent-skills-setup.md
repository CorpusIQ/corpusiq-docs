---
title: "Amazon Devices Agent Skills - Fire TV and Vega Setup"
description: "amazonappdev/devices-agent-skills: 11.0K combined installs. Community agent skills for Fire TV, Vega OS and React Native TV app development."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/amazon-devices-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "fire tv", "vega os", "react native", "tv"]
---

# Amazon Devices Agent Skills - Setup Guide

**Source:** [amazonappdev/devices-agent-skills](https://www.skills.sh/amazonappdev/devices-agent-skills) via skills.sh - 11.0K combined installs across 2 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [amazonappdev/devices-agent-skills](https://github.com/amazonappdev/devices-agent-skills) - 6 stars, MIT License, branch main, last pushed 2026-09-21; 2 skills in a flat `skills/<name>/SKILL.md` layout, `rn-tv-ui-best-practices` carrying five `references/` pages plus `references/scripts/audit.js`, and `vega-multi-tv-migration` carrying three phase documents under `references/` plus eight config templates with companion docs and a validation checklist under `assets/templates/`

**Category:** Fire TV, Vega and React Native TV application development

**Quality Tier:** 🟢 Green - all sampled skills Pass on all three auditors; two first-party MIT skills that cover TV UI review across four runtimes and a phased Vega OS to multi-platform React Native migration

`amazonappdev/devices-agent-skills` is Amazon's community skills repository, described in its README as "a collection of Agent Skills, structured knowledge packages that give AI assistants specialized capabilities and guided workflows". Skills follow the Agent Skills specification at agentskills.io. The README splits the world in two: this repository holds skills for open-source frameworks and workflows that benefit from community input, while work against proprietary Amazon SDKs and APIs is pushed to Amazon Devices Builder Tools for AI, a separate MCP server documented under the Vega docs.

The two skills are complementary halves of the same TV engineering problem. `vega-multi-tv-migration` is the large one at 10,951 installs, and it turns a single-platform Vega OS (Fire TV) app into a React Native monorepo with claimed 70-85% code reuse across Android TV, Apple TV and Vega OS, in three ordered phases with a decision tree that tells the agent where to start. `rn-tv-ui-best-practices` is the review skill, covering focus management, D-pad and remote input, swimlanes and hero banners, overscan, typography at ten feet and HDR behaviour across tvOS, Android TV, Fire TV and Vega OS. It is attributed in its own file to The Ultimate Guide to React Native TV Development, co-authored by Amazon and Callstack.

## Installation

The README documents three routes and no more. The GitHub CLI route installs everything, or one skill scoped to a project:

```bash
gh skill install AmazonAppDev/devices-agent-skills --all
```

```bash
gh skill install AmazonAppDev/devices-agent-skills vega-multi-tv-migration --agent <your-agent> --scope project
```

The skills.sh CLI route needs no setup beyond `npx`:

```bash
npx skills add AmazonAppDev/devices-agent-skills
```

```bash
npx skills add AmazonAppDev/devices-agent-skills --skill vega-multi-tv-migration
npx skills add AmazonAppDev/devices-agent-skills --skill rn-tv-ui-best-practices
```

The README names `claude-code`, `kiro-cli`, `cursor`, `codex` and `github-copilot` as agents for the `--agent` flag, and Hermes is not on that list, so the durable route for this profile is the README's third option, manual installation. Clone the repository and copy each skill directory into `~/.hermes/profiles/corpusiq/skills/<name>/`:

```bash
cp -r skills/vega-multi-tv-migration skills/rn-tv-ui-best-practices \
  ~/.hermes/profiles/corpusiq/skills/
```

Copy the whole directory rather than the markdown. `rn-tv-ui-best-practices` is a router over five reference files plus a zero-dependency audit script, and `vega-multi-tv-migration` ships its phase documents and the config templates that phase 2 asks the agent to copy, so a lone `SKILL.md` leaves the agent pointing at files that are not there.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| vega-multi-tv-migration | 10,951 | Moving a Vega OS (Fire TV) app to a Yarn workspaces monorepo that also builds Android TV and Apple TV, in three gated phases: codebase analysis and dependency classification, monorepo scaffolding with VMRP and Metro resolution, then per-platform native modules, with templates for root and shared package files, Metro configs and a validation checklist. |

The remaining 1 indexed listings range from 27 to 27 installs.

## Why This Matters for Hermes Agents

TV is the platform where general React Native advice quietly produces a broken app, and these two skills are the correction. A model that has only seen mobile React Native will reach for touch gestures, 14px type and pixel measurements taken at phone distance, and none of that survives a couch, a nine-button remote and a focus ring. `rn-tv-ui-best-practices` starts by making the agent check the runtime in `package.json` before applying anything, so a project on `react-native-tvos` and a project on `@amazon-devices/react-native-kepler` get different answers, and a non-TV project gets told the skill does not apply.

The migration skill is valuable for a different reason: it is ordered. Three phases with a priority table and a decision tree, each with a checkpoint, replace the usual agent behaviour of generating a plausible monorepo in one pass and leaving the resolution errors for the human. The hard parts of the move are the parts it names explicitly, including Yarn dependency deduplication, Metro resolution under the Vega module resolver preset, and TypeScript project references.

Both skills also carry the honesty that agent tooling usually lacks. The UI skill ships `node references/scripts/audit.js src` as a static helper and then says plainly that it is a helper and not a review, because most of its rules need judgement or real hardware. When it finishes, it hands back a checklist of things a human must confirm, framed as outstanding work rather than completed checks: overscan crop, focus indicator visibility in ambient light, contrast under HDR, animation feel, legibility at ten feet.

For a Hermes profile, that combination is the useful shape. The knowledge is narrow enough to keep in context, the entry check prevents misfires on non-TV codebases, and the handoff list gives a subagent something concrete to report instead of a false all-clear.

## Usage

| You say | What happens |
|---|---|
| "We have a Vega OS Fire TV app and need Apple TV and Android TV builds" | `vega-multi-tv-migration` walks its decision tree: no existing analysis means phase 1, so it inventories the codebase and classifies business logic, UI and utilities as shared, native modules and DRM as platform-specific, then produces the migration plan before any code moves. |
| "Set up the monorepo for packages/shared, packages/vega and packages/expotv" | Phase 2 scaffolding, using the `root-package.json`, `shared-package.json`, `root-tsconfig.json` and `yarnrc.yml` templates under `assets/templates/`, with the Yarn workspaces block checked by the skill's own grep snippet. |
| "Metro cannot resolve our shared package after the move" | It goes to the Metro and VMRP sections of phase 2, checks whether `@vega-tv/react-native-module-resolver-preset` is wired into `packages/vega/babel.config.js`, and works through duplicate React versions and path mapping in order. |
| "Focus jumps to the wrong card when I press left" | `rn-tv-ui-best-practices` routes to `navigation-and-focus.md` and picks the mechanism: `TVFocusGuideView`, `hasTVPreferredFocus`, `trapFocus`, `FocusManager`, `Navigable` or `useTVEventHandler`, naming the runtime it applies to. |
| "Review this TV screen for ten-foot legibility" | It reads `typography-and-color.md` and `layout-patterns.md` for font sizes, contrast, safe zones and swimlane layout, then hands back the checks it cannot do without hardware: HDR bloom, overscan crop, focus ring visibility under ambient light. |
| "Add voice search and QR sign-in to the TV app" | `input-handling.md` covers the remote model and button vocabulary, `TextInput` behaviour, the search and login flows, voice input and the QR companion-app pattern, so the agent reduces typing instead of shipping a phone keyboard. |
| "Rename this screen component and tidy the styles" | Neither skill activates. The UI skill requires `Platform.isTV` or a TV runtime in dependencies, and the migration skill requires a Vega or TV app to move, so an ordinary React Native task proceeds without TV constraints applied. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} migration\n" \
  https://raw.githubusercontent.com/amazonappdev/devices-agent-skills/main/skills/vega-multi-tv-migration/SKILL.md
curl -sL -o /dev/null -w "%{http_code} ui\n" \
  https://raw.githubusercontent.com/amazonappdev/devices-agent-skills/main/skills/rn-tv-ui-best-practices/SKILL.md
```

Expect `200` twice. Read the file before installing, because the frontmatter is the routing contract: `vega-multi-tv-migration` declares its own trigger list (migrating a Vega app, adding Android TV or Apple TV support, converting a single-platform app to a monorepo), and `rn-tv-ui-best-practices` names the specific APIs it knows, which is how the agent decides whether it applies to your codebase.

After the copy lands in the profile, confirm the frontmatter and that the supporting directories came with it:

```bash
head -4 ~/.hermes/profiles/corpusiq/skills/vega-multi-tv-migration/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/vega-multi-tv-migration/references/ ~/.hermes/profiles/corpusiq/skills/vega-multi-tv-migration/assets/templates/
ls ~/.hermes/profiles/corpusiq/skills/rn-tv-ui-best-practices/references/
```

A good copy shows `name:` and `description:` as the only frontmatter fields, three phase documents plus the validation checklist in the migration skill, and five reference pages plus `scripts/audit.js` in the UI skill. The audit script is the cheapest integrity check that it is intact, and it exits non-zero when it finds something:

```bash
node ~/.hermes/profiles/corpusiq/skills/rn-tv-ui-best-practices/references/scripts/audit.js ./src --only focus
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| vega-multi-tv-migration | Pass | Pass | Pass |
| rn-tv-ui-best-practices | Pass | Pass | Pass |

Both listings are clean on all three auditors, and that matches what the files actually contain: markdown guidance, configuration templates, and one small Node script that greps source files for focus, input, layout and typography patterns with no dependencies and no network access. Nothing in either skill reads credentials, calls a service or writes to a project by itself.

The real risk surface is the advice, not the code. Phase 2 tells an agent to scaffold packages and rewrite build configuration, and phase 3 tells it to add native modules, so an unsupervised run against a production app touches `package.json`, Metro and Babel configs and TypeScript references. Run the migration on a branch, keep the validation checklist as the gate, and remember that the skills intentionally defer Vega API specifics to Amazon's live documentation rather than shipping a copy that will age out.

## Limitations

- Snapshot data, verified 2026-10-30: 10,978 combined installs across 2 indexed listings; 6 GitHub stars; MIT License; last pushed 2026-09-21. Counts drift over time.
- Two skills is the whole repository. There is no MCP server, no CLI and no eval harness here, and the README points at Amazon Devices Builder Tools for AI for anything touching proprietary Amazon SDKs, so this collection covers framework-level guidance only.
- The install counts do not describe the pair. One listing carries 10,951 installs and the other 27, so the combined figure is the migration skill's number rather than a signal for both, and 6 stars is a very low GitHub footprint for a repository with five-figure index installs. Judge each `SKILL.md` on its content.
- The UI skill is explicitly incomplete by design. It covers cross-runtime gotchas and defers Vega API specifics to Amazon's live docs, and it will not verify overscan, HDR contrast, focus ring visibility, animation feel or ten-foot legibility, all of which it hands back as human work. `audit.js` catches only statically detectable patterns, so a clean run is not a clean review.
- The migration numbers are claims, not measurements. The 70-85% code reuse target comes from the skill's own overview, and real reuse depends on how much of the app is native modules, DRM and player logic, which is the platform-specific bucket the skill tells you to isolate in phase 1.
- Layout is flat and unversioned: two directories under `skills/`, no tags and no package manifest at the root, so pin a commit SHA when you copy rather than tracking `main`.

## Related

- [React Native Update Skill - OTA Update Integration Setup](/hermes/skills/catalog/react-native-update-skill-setup)
- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [Callstack Agent Skills - React Native Skill Suite Setup](/hermes/skills/catalog/callstackincubator-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the runtime check before anything else. `react-native-tvos` means tvOS and Android TV, `@amazon-devices/react-native-kepler` means Vega, and a monorepo can hold both per package, so tell the agent which package you are in rather than letting it guess from the root `package.json`.
- Install the migration skill only while you are migrating. It is a phase machine with its own decision tree, and it will try to structure a task that does not need phases if you leave it active on ordinary React Native work.
- Copy `assets/templates/` with the migration skill. Phase 2 references those files by path for Yarn workspaces, TypeScript references, Metro and the Vega module resolver preset, and the `yarnrc.yml` deduplication template is the fix for the duplicate React version error most monorepo moves hit.
- Ask for the human verification list explicitly at the end of a review. The UI skill ends each reference with a handoff section, and asking for it turns the silent gaps (overscan, HDR contrast, focus ring in ambient light) into a checklist you can run on a real device.
- Keep `audit.js` in CI as a lint, not as a review. It is zero-dependency and exits 1 on findings, which makes it a good pre-commit gate for focus and input patterns, and it will never cover the rules that need judgement.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
