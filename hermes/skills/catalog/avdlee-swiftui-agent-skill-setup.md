---
title: "SwiftUI Agent Skill - Apple UI Development Setup"
description: "avdlee/swiftui-agent-skill: 37.9K combined installs. An MIT SwiftUI expert skill for agents: 33 reference files and an Apple docs API refresh loop."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/avdlee-swiftui-agent-skill-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "swiftui", "ios development", "apple platforms"]
---

# SwiftUI Agent Skill - Setup Guide

**Source:** [avdlee/swiftui-agent-skill](https://www.skills.sh/avdlee/swiftui-agent-skill) via skills.sh - 37.9K combined installs across 2 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [AvdLee/SwiftUI-Agent-Skill](https://github.com/AvdLee/SwiftUI-Agent-Skill) - 3,791 stars, MIT License, branch main, last pushed 2026-10-06; two skill directories, at `skills/swiftui-expert-skill/SKILL.md` (33 reference files under `references/`, plus `scripts/record_trace.py`, `scripts/analyze_trace.py`, an 11-module `scripts/instruments_parser/` package and `assets/`) and `.agents/skills/update-swiftui-apis/SKILL.md` (with `references/scan-manifest.md`), inside an Agent Plugins 1.0.0 root carrying `plugin.json` at version 5.2.1 plus `.claude-plugin/`, `.codex-plugin/` and `.cursor-plugin/` manifests, where the top-level `swiftui-expert-skill` is a symlink to the real skill folder

**Category:** Apple platform app development: SwiftUI state, layout, performance and API-currency guidance for coding agents

**Quality Tier:** 🟢 Production - all sampled verdicts Pass on both indexed skills; MIT, 3,791 stars, two skill directories, active Apple-platform documentation work

The publisher is Antoine van der Lee, whom the repository's own `llms.txt` introduces as the author of the SwiftLee material, and the package is two skills rather than a suite of forty. `swiftui-expert-skill` is the one that does the work: an 11,613 character SKILL.md holding operating rules, a task workflow, a 33-entry topic router and a 17-item correctness checklist, with every topic's depth pushed into a separate reference file that loads only when the task touches it. `update-swiftui-apis` is the maintenance loop beside it, and it is a different kind of artifact entirely: a procedure that scans Apple's own documentation through the Sosumi MCP and rewrites the deprecated-API list rather than a source of coding advice.

What makes it notable is how much of the value is in the routing and so little of it in the entry file. The checklist is written as hard rules ("violations are always bugs"), the router gives one reference per topic from state management to `macos-scenes.md` and `liquid-glass.md`, and the two bundled Python scripts turn an Instruments `.trace` file into a ranked answer about which view is re-rendering and what is invalidating it. The repository is also packaged properly for distribution: a portable `plugin.json`, per-client manifests for Claude Code, Codex and Cursor, and an `llms.txt` that pins the install command and corrects the two commands agents tend to invent.

## Installation

The README's recommended route is skills.sh, and `--skill` is required because the repository carries two skills and the real one sits under `skills/` rather than at the root:

```bash
npx skills@latest add https://github.com/avdlee/swiftui-agent-skill --skill swiftui-expert-skill
```

The repository's own `llms.txt` pins that same command and adds two corrections worth keeping: the command is `skills add` (there is no `skills load`), and an existing install is refreshed with `npx skills@latest update` on skills CLI 1.5.24 or newer, which migrates the saved path after the Agent Plugins move instead of treating the skill as deleted.

The repository does not document Hermes, so the predictable route is the manual option in `INSTALLATION.md` pointed at the profile skills directory. Copy the folder that contains `SKILL.md`, not the file, because the references and scripts sit beside it:

```bash
git clone --depth 1 https://github.com/AvdLee/SwiftUI-Agent-Skill.git /tmp/swiftui-agent-skill
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -R /tmp/swiftui-agent-skill/skills/swiftui-expert-skill \
  ~/.hermes/profiles/corpusiq/skills/
export SKILL_DIR=~/.hermes/profiles/corpusiq/skills/swiftui-expert-skill
```

`SKILL_DIR` is not optional for the profiling workflows. Both of them invoke `python3 "${SKILL_DIR}/scripts/record_trace.py"` and `python3 "${SKILL_DIR}/scripts/analyze_trace.py"`, and nothing in the repository or in Hermes sets that variable, so export it in the profile environment or substitute a literal path. The copy also brings `assets/` with it, which is 432 KB of logo files the skill never reads; drop that directory if profile size matters.

The second skill needs a separate copy, since the installer ran with a single `--skill` name:

```bash
cp -R /tmp/swiftui-agent-skill/.agents/skills/update-swiftui-apis \
  ~/.hermes/profiles/corpusiq/skills/
```

Two other documented routes matter for teams. Claude Code takes it as a plugin, which gets automatic updates:

```bash
/plugin marketplace add AvdLee/SwiftUI-Agent-Skill
/plugin install swiftui-expert@swiftui-expert-skill
```

And `INSTALLATION.md` covers pi (`pi install https://github.com/AvdLee/SwiftUI-Agent-Skill`), Gemini CLI (`gemini skills install`), Autohand Code and ChatGPT or Codex through the OpenAI Plugins Directory. None of these are needed for Hermes. Node.js is a requirement only for the `npx` route; a copied skill is plain markdown and Python.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| swiftui-expert-skill | 35,473 | Reviewing, refactoring and writing SwiftUI against a fixed rule set: an Operating Rules block that treats each View type as an invalidation boundary and keeps data close to the smallest affected subtree, a 17-item correctness checklist (`@State` must be `private`, `ForEach` needs stable identity and never `.indices`, `.animation(_:value:)` must pass `value`, custom `@Entry` defaults must be stable, display scale comes from `@Environment(\.displayScale)`), a topic router that loads one of 33 reference files per topic, a hard-versus-soft deprecation policy, and two Instruments workflows that record an `xctrace` session and rank the SwiftUI update causes behind a hot view. |
| update-swiftui-apis | 2,380 | Keeping the API list current instead of trusting training data: reads `references/scan-manifest.md`, searches and fetches Apple developer documentation through the Sosumi MCP (`searchAppleDocumentation`, `fetchAppleDocumentation`, `fetchAppleVideoTranscript`), compares new deprecations against the 583-line `latest-apis.md`, adds entries in the established modern-then-deprecated snippet format plus a Quick Lookup Table row, and opens a PR on a branch named `update/latest-apis-YYYY-MM`. Requires Sosumi MCP and write access to a fork. |

No indexed listings fall below the threshold; all 2 appear above.

## Why This Matters for Hermes Agents

SwiftUI is one of the worst domains for stale training data, because Apple deprecates APIs quietly: a soft-deprecated symbol is marked with the placeholder version `100000.0`, which suppresses the compiler warning, so an agent can write `NavigationView` in 2026 and see a clean build. `references/latest-apis.md` answers the mechanical half of that with 41 lookup rows across seven version segments (iOS 15+ through iOS 27.1+), and `references/soft-deprecation.md` answers the behavioural half: replace hard deprecations during feature work, flag soft ones without rewriting them, and never mention them in code the task did not touch.

The token economics are the second argument. The entry file is 11,613 characters, small enough to sit in context, and the 33 reference files stay on disk until the router sends the agent to one of them, so a review of a sheet and a navigation stack does not drag macOS window styling or Swift Charts accessibility along with it; that is roughly 440 KB of guidance available without ever entering the prompt.

The checklist is what changes review output, because it converts taste into assertions the agent can fail: `@State` not `private`, a constant number of views per `ForEach` element, no closures stored in custom `@Environment` keys, `.animation(_:value:)` with the `value` parameter present, safe-area content that does not double-apply `GeometryProxy.safeAreaInsets`. A Hermes agent asked to review a diff can report against those lines instead of producing prose.

Finally, the maintenance skill makes currency a procedure instead of a hope: pointed at Sosumi MCP after a WWDC release, it produces a diff against Apple's own documentation and, if you want it, a pull request. The honest limit is that the skill cannot compile, preview or run the code it recommends, so pair it with a build step and treat its output as review notes.

## Usage

| You say | What happens |
|---|---|
| "Review this SwiftUI view for state-management problems" | The agent reads the code, identifies which router topics apply, loads `references/state-management.md` and likely `references/performance-patterns.md`, then reports against the checklist: `@State` visibility, owned versus injected objects, `@StateObject` for view-owned and `@ObservedObject` for injected, `@State` with `@Observable` on iOS 17+, and stable `ForEach` identity. |
| "Is `foregroundColor` still fine here?" | The agent checks `references/latest-apis.md`, finds `foregroundStyle(_:)` in the Always Use (iOS 15+) segment, replaces the hard deprecation if the task is a migration, and leaves soft deprecations in untouched code alone by design. |
| "Why does this screen re-render when a toggle flips?" | The agent explains the invalidation boundary, proposes narrower data reads close to the smallest subtree, and moves the frequently changing dependency out of the parent view rather than adding caching. |
| "Profile the app and tell me what is slow" | `python3 "${SKILL_DIR}/scripts/record_trace.py" --list-devices` enumerates targets as JSON, then a recording runs with the SwiftUI template (or Time Profiler on the iOS Simulator, where the SwiftUI lane comes back empty) and a `--stop-file` for background sessions. |
| "Here is a `.trace` file, what is hot?" | `analyze_trace.py --json-only --top 10` returns correlation coverage, `swiftui-causes.top_sources` and per-view cost, and `--fanin-for "<view>"` ranks the nodes invalidating that view. The agent cites coverage percentages and log timestamps before recommending anything. |
| "We moved to iOS 26, what should change?" | The agent works through the iOS 26+ and SDK 27 segments, gates version-specific APIs with `#available` and a fallback, and treats Liquid Glass as opt-in only, since the Operating Rules say to adopt it when the user asks. |
| "Refresh the deprecation list after the Xcode release" | `update-swiftui-apis` reads `scan-manifest.md`, scans Apple docs through Sosumi MCP, diffs against the existing entries, adds new rows in the house format and opens a PR on an `update/latest-apis-YYYY-MM` branch. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-29, which matters here because the second skill lives under a dot directory:

```bash
curl -sL -o /dev/null -w "%{http_code} swiftui-expert-skill\n" \
  https://raw.githubusercontent.com/avdlee/swiftui-agent-skill/main/skills/swiftui-expert-skill/SKILL.md
curl -sL -o /dev/null -w "%{http_code} update-swiftui-apis\n" \
  https://raw.githubusercontent.com/avdlee/swiftui-agent-skill/main/.agents/skills/update-swiftui-apis/SKILL.md
```

Read the first one before installing it. The frontmatter is only `name` and `description` (851 characters, no `allowed-tools`, no `license` key), the Operating Rules block is a short list of behavioural constraints, and the executable surface is two Python scripts plus `scripts/instruments_parser/`. Counting the checklist confirms the file that arrived is the file described here:

```bash
curl -sL https://raw.githubusercontent.com/avdlee/swiftui-agent-skill/main/skills/swiftui-expert-skill/SKILL.md \
  | grep -c '^- \[ \]'
```

Expect `17`. Then confirm the installed copy kept the references directory, which is where almost all of the guidance lives:

```bash
ls ~/.hermes/profiles/corpusiq/skills/swiftui-expert-skill/references | wc -l
head -4 ~/.hermes/profiles/corpusiq/skills/swiftui-expert-skill/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/update-swiftui-apis/references/
```

Expect `33` from the first command, a `name: swiftui-expert-skill` line from the second, and `scan-manifest.md` from the third. If the reference count is `0`, a single-file install is what happened and the router will send the agent to files that are not there.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| swiftui-expert-skill | Pass | Pass | Pass |
| update-swiftui-apis | Pass | Pass | Pass |

There is no failing verdict here, so nothing leads the section: both sampled listings pass all three auditors. What the verdicts cover is small and readable, which is the useful part. The coding skill is markdown plus two Python files that shell out to `xctrace`, and the repository ships `tests/test_record_trace.py`, described as security-focused tests for the recording wrapper, whose cases assert that environment values are redacted when a command is echoed, so credentials passed with `--env` do not land in a transcript. The maintenance skill ships no executable code of its own, but it requires the Sosumi MCP and repository write access, and it ends by opening a pull request with `gh`, so scope it to a fork you own rather than to a branch you deploy from.

## Limitations

- Snapshot data, verified 2026-10-29: 37,853 combined installs across 2 indexed listings; 3791 GitHub stars; MIT License; last pushed 2026-10-06. Counts drift over time.
- The index and the tree agree on two skills but split them oddly: skills.sh indexes `swiftui-expert-skill` and `update-swiftui-apis`, and the tree holds one SKILL.md under `skills/` and one under `.agents/skills/`. The root `swiftui-expert-skill` entry is a symlink left for pre-migration clones, and INSTALLATION.md says it will be removed in the next major version, so point any copy at `skills/swiftui-expert-skill/`.
- The Instruments workflows are macOS-only. `record_trace.py` drives `xctrace` from Xcode, and `analyze_trace.py` reads the trace through the bundled parser, so on a Linux host both workflows are inert while the reference reading still works. On the iOS Simulator the SwiftUI template returns an empty lane, so the skill itself routes simulators to the Time Profiler template.
- `update-swiftui-apis` is a maintainer tool, not a coding aid. It needs the Sosumi MCP server reachable, write access to the repository or a fork, and the `gh` CLI for its final step, so a read-only checkout can do nothing with it.
- One person maintains the package. Antoine van der Lee is the author in every manifest, the current version is 5.2.1, and the README badge claims 31.4k weekly installs while skills.sh records 35,473 for the same listing; those are different windows and this guide does not reconcile them.
- It is a knowledge skill with no compiler behind it. Nothing in the package builds, previews or runs the app, so a suggestion that does not compile will not be caught by the skill; the honest use is review notes plus your own build.

## Related

- [Swift iOS Skills - iOS 26 and SwiftUI Suite Setup](/hermes/skills/catalog/dpearson-swift-ios-skills-setup)
- [Xcode Build Optimization - iOS Build Performance Setup](/hermes/skills/catalog/xcode-build-optimization-setup)
- [Swift Testing Pro Skill - Swift Testing Suite Setup](/hermes/skills/catalog/swift-testing-pro-skill-setup)
- [Limrun Skills - Cloud iOS & Android Simulator Setup](/hermes/skills/catalog/limrun-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Export `SKILL_DIR` once in the profile environment. Every profiling command in the skill is written against that variable, and without it the agent improvises a path and gets a missing-file error instead of a trace.
- Ask for the checklist by name. "Run the correctness checklist on this file" gets a line-by-line verdict, while "review this" gets prose; the 17 rules are the part that catches real bugs.
- Give it the scope when you want migrations to stay quiet. The soft-deprecation rule is deliberately narrow, so name the files you want migrated and expect no commentary about the rest of the tree.
- Drop `assets/` after copying. It is 432 KB of logos the skill never opens, and a profile skills directory is the wrong place to keep them.
- Re-run `update-swiftui-apis` after each Xcode or WWDC cycle rather than trusting `latest-apis.md` indefinitely. The file is dated by its last commit, and the SDK 27 and iOS 27.1 segments show how fast it moves.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
