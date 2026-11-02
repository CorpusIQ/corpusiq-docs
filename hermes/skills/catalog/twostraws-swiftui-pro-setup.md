---
title: "SwiftUI Pro - Apple UI Development Skill"
description: "twostraws/swiftui-agent-skill: 36.5K combined installs. One SwiftUI review skill with twelve reference files on API, layout and accessibility."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/twostraws-swiftui-pro-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "swiftui", "ios", "code review"]
---

# SwiftUI Pro - Setup Guide

**Source:** [twostraws/swiftui-agent-skill](https://www.skills.sh/twostraws/swiftui-agent-skill) via skills.sh - 36.5K combined installs across 1 indexed listing; first seen 2026-11-02 (morning sweep)

**GitHub:** [twostraws/swiftui-agent-skill](https://github.com/twostraws/swiftui-agent-skill) - 6,438 stars, MIT with a `LICENSE` file in the root, branch main, last pushed 2026-10-26; 1 `SKILL.md` at `swiftui-pro/SKILL.md` next to a `references/` folder of twelve files, an `agents/openai.yaml` and two icon assets

**Category:** SwiftUI engineering for agents: view composition, state, animation, accessibility and HIG review

**Quality Tier:** 🟢 Production - one skill, 6,438 stars, MIT licensed, and the single sampled listing passes Gen Agent Trust Hub, Socket and Snyk

SwiftUI Pro is Paul Hudson's agent skill for Apple platform UI work, published from Hacking with Swift and built on top of his existing AGENTS.md file. It is a single skill rather than a suite, and it does one job: review and steer SwiftUI code so an assistant writes modern, accessible, efficient views instead of plausible code that fails the platform.

The target is specific. The README says the rules exist because models make the same mistakes repeatedly, and names three: buttons that are invisible to VoiceOver, frequent use of deprecated API, and code that causes surprising performance problems. The skill body says the same thing in its first line, which is to report only genuine problems and not to invent issues or nitpick. Everything in the pack is arranged around that: a review order, a set of reference files, and a fixed output format.

It uses the Agent Skills format, so the same folder works in Claude Code, Codex, Gemini, Cursor and anything else that reads the standard. The README also points at three sibling skills in the same family, SwiftData Pro, Swift Concurrency Pro and Swift Testing Pro, which are separate repositories rather than part of this install.

## Installation

The README's install command names the full repository URL and the one skill in it:

```bash
npx skills add https://github.com/twostraws/swiftui-agent-skill --skill swiftui-pro
```

If `npx` is missing, the README says to install Node through Homebrew first, and to install Homebrew if that fails:

```bash
brew install node
```

The npx flow asks which agents to install for and whether the skill should be available in one project or all of them. The manual route is a clone plus a copy, which is what a Hermes profile needs since nothing in the repository mentions Hermes:

```bash
git clone https://github.com/twostraws/swiftui-agent-skill.git /tmp/swiftui-agent-skill
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -R /tmp/swiftui-agent-skill/swiftui-pro ~/.hermes/profiles/corpusiq/skills/
```

Copy the whole `swiftui-pro` folder, not just the `SKILL.md`. The review order in the skill points at `references/api.md`, `references/views.md` and the rest, and a skill installed without its references loses most of its value.

Claude Code users can take the marketplace route, which the repository is packaged for:

```text
/plugin marketplace add twostraws/SwiftUI-Agent-Skill
/plugin install swiftui-pro@swiftui-agent-skill
```

Then trigger it three ways: `/swiftui-pro` in Claude Code, `$swiftui-pro` in Codex, or plain language such as "use the SwiftUI Pro skill to look for performance problems in this project". All three accept a narrower instruction, for example `/swiftui-pro Check for deprecated API` or `$swiftui-pro Focus on accessibility`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| swiftui-pro | 36,507 | An eleven-step review of Swift and SwiftUI code across deprecated API, view structure, data flow, navigation, design, resizing, accessibility, localization, performance, Swift style and hygiene, with findings by file, the rule broken, a before and after fix, and a prioritized summary. |

No indexed listings fall below the threshold; the single listing appears above.

There is one skill but twelve reference files, and they are the substance of the pack: `api.md` for modern API and its deprecated replacements, `views.md` for structure, composition and animation, `data.md` for state and property wrappers, `navigation.md` for stacks, alerts and sheets, `design.md` for Human Interface Guidelines conformance, `resizability.md` for window resizing and iPhone Duo layouts, `accessibility.md` for Dynamic Type, VoiceOver and Reduce Motion, `localization.md` for localizable text and resource bundles, `performance.md` for efficiency, `swift.md` for modern Swift and concurrency, and `hygiene.md` for long-term maintainability. The twelfth, `performance-plus.md`, is deliberately kept out of routine reviews and loaded only for a requested deep performance review.

## Why This Matters for Hermes Agents

Most UI skills tell an agent how to build a screen. This one tells it how to judge code it has already written, which is the more valuable half for an agent working in a repository it did not author. The review order is fixed, the references are loaded per area, and the output contract is explicit: the file and line, the rule being violated, a short before and after, and a prioritized summary at the end. That is a review a human can act on rather than a wall of opinions.

The rules are pointed at failures that are invisible in a screenshot. A button built from an SF Symbol with no label looks fine and is unusable with VoiceOver. A `foregroundColor()` call compiles and is deprecated. A `Binding(get:set:)` in a view body works until the side effect in the setter fires at the wrong time. None of those show up in a preview, and all three are named in the skill's own examples.

It also constrains behaviour around the review. The skill says to report only genuine problems, to complete a requested feature or fix and suggest unrelated modernization separately rather than applying it unasked, and never to introduce a third-party framework without asking. For an agent in an unattended loop, those are the instructions that stop a code review from turning into an unrequested refactor.

The project conventions are current rather than generic. The skill states that iOS 27 is the default deployment target for new apps, that Xcode 27.1 APIs should not be dismissed as speculative, that iPhone Duo is a folding phone with two displays, and that Swift 6.4 or later is the target. It also says to check the project's own deployment target before applying any version-specific advice, which is the instruction that keeps the guidance from breaking an older app.

## Usage

| You say | What happens |
|---|---|
| "/swiftui-pro" | A full review in the fixed order, loading each reference as it goes, with findings grouped by file and a prioritized summary of the most impactful changes. |
| "/swiftui-pro Check for deprecated API" | A partial review that loads only the API reference and reports deprecated calls with the modern replacement and a before and after snippet. |
| "Focus on accessibility" | Partial review against Dynamic Type, VoiceOver and Reduce Motion, including missing labels, unlabelled images and motion that ignores the setting. |
| "Look for performance problems in this project" | The performance reference is applied to view structure and dependency shape, and `performance-plus.md` is only pulled in if the review is explicitly deep. |
| "Review this screen before I open the PR" | Findings by file with rule names and fixes, plus a summary ordered by impact, so the PR discussion starts from the list rather than from opinion. |
| "Make this view resize properly on iPad" | The resizability rules are applied to adaptive bars, safe areas, window resizing and the folding iPhone layouts. |
| "Audit this app for localization" | The localization reference checks hardcoded strings, resource bundles and locale-aware formatting. |

## Verification

The two raw paths below returned 200 on branch main when this guide was written on 2026-11-02. The second matters, because a skill installed without its references is half an install:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  "https://raw.githubusercontent.com/twostraws/swiftui-agent-skill/main/swiftui-pro/SKILL.md"
curl -sL -o /dev/null -w "%{http_code} references/api.md\n" \
  "https://raw.githubusercontent.com/twostraws/swiftui-agent-skill/main/swiftui-pro/references/api.md"
```

After a clone, confirm the shape of the install rather than the file count alone:

```bash
git clone --depth 1 https://github.com/twostraws/swiftui-agent-skill.git /tmp/swiftui-pro
find /tmp/swiftui-pro -name SKILL.md | wc -l
ls /tmp/swiftui-pro/swiftui-pro/references | wc -l
head -12 /tmp/swiftui-pro/swiftui-pro/SKILL.md
```

The first count should be 1 and the second 12. The `head` prints the frontmatter and the start of the review order, which is the part the agent actually follows.

The skill's own rule is worth repeating as a check on the guide rather than the repo: before you accept a version-specific suggestion, confirm the project's deployment target. The skill tells the agent to do that, and the same discipline applies to a human reading the findings.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| swiftui-pro | Pass | Pass | Pass |

There is one listing and it passes all three auditors, so the sample is the whole pack rather than a subset of it.

What lands on disk is text and two images. The repository holds 15 Markdown files, one YAML file, two JSON manifests and two icon assets, and no executable of any kind. There is no install script, no build step and no post-install hook, so nothing runs when the skill is cloned or copied.

The only thing the skill asks of an agent is to read code and write a review, which keeps the risk surface small. The two JSON files are the Claude Code marketplace and plugin manifests, and `agents/openai.yaml` is the interface manifest: display name, icons, brand colour, a default prompt of "$swiftui-pro to review my project" and an `allow_implicit_invocation` policy set to true, which is why natural language triggers it. If you review the skill before installing, read `SKILL.md` first, then whichever reference covers the area you care about.

## Limitations

- Snapshot data, verified 2026-11-02: 36,507 combined installs across 1 indexed listing; 6,438 GitHub stars; MIT; last pushed 2026-10-26. Counts drift over time.
- This is a review skill, not a generator. It reads code and reports findings; it does not build, run or compile the project, so a clean report is not a build check.
- The security sample is one listing, because the pack has one skill. There is no per-skill variation to average, and the verdict is only as current as the scan.
- The README badges say iOS 26 and Swift 6.4, while the skill body states that iOS 27 is the default deployment target for new apps. The skill itself says to check the project's target before applying version-specific advice, and that is the rule to follow.
- The install command needs the full repository URL and `--skill swiftui-pro`, and the plugin block uses the capitalised `twostraws/SwiftUI-Agent-Skill`, while the repository slug is lowercase `swiftui-agent-skill`. Both work, but the spellings differ.
- Nothing in the repository mentions Hermes, so the copy route above is the one to use against a Hermes profile, and it must copy the whole `swiftui-pro` folder with its references.

## Related

- [SwiftUI Agent Skill - Apple UI Development Setup](/hermes/skills/catalog/avdlee-swiftui-agent-skill-setup)
- [Swift Testing Pro Skill - Swift Testing Suite Setup](/hermes/skills/catalog/swift-testing-pro-skill-setup)
- [Xcode Build Optimization - iOS Build Performance Setup](/hermes/skills/catalog/xcode-build-optimization-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Scope the review instead of asking for everything. A partial run loads one reference and produces a short, fixable list, which is easier to act on than a full sweep of eleven areas.
- Run it on a branch before you open a PR. The output is keyed to file and line with a before and after, so it reads as review comments rather than as a rewrite request.
- Keep `performance-plus.md` for diagnosed problems. The skill deliberately excludes deeper restructuring from routine reviews, and loading it on every pass turns a review into a refactor.
- Check the deployment target before accepting any advice about a newer API. The skill says this itself, and the README badge and the skill body disagree on the current iOS major.
- Pair it with the sibling skills rather than expecting one skill to cover persistence, concurrency and testing. SwiftData Pro, Swift Concurrency Pro and Swift Testing Pro are separate repositories with their own rules.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
