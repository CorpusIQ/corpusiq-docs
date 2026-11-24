---
title: "Tuist Agent Skills - Xcode Project Generation Suite Setup"
description: "tuist/agent-skills - 4.5K combined installs: 12 skills for working with Tuist-generated Xcode projects, from migration to build comparison."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tuist-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "tuist", "xcode", "ios"]
---

# Tuist Agent Skills - Xcode Project Generation Suite Setup

**Source:** [tuist/agent-skills](https://www.skills.sh/tuist/agent-skills) via skills.sh - 4.5K combined installs across 12 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [tuist/agent-skills](https://github.com/tuist/agent-skills) - 35 stars, MIT, main branch, last pushed Nov 7, 2026; one SKILL.md per skill under skills/, automatically updated from tuist/tuist.
**Category:** Xcode Project Generation and iOS Tooling
**Quality Tier:** 🟡 Yellow - the 12-skill sample has one Warn cell, debug-generated-project (Snyk), and no Fail cells.

Tuist Agent Skills is the official skill collection from the Tuist project, the Xcode project generation and module tool for Swift apps. The skills are pre-built instruction sets for complex, multi-step Tuist tasks: instead of manually walking an agent through a migration or a build comparison, you install a skill and let the agent run it. The repository is automatically updated from the main tuist/tuist repository, so the skills track the tool they describe.

Most of the twelve skills are comparison tools that diff two build, test, cache or generation runs to find regressions, and the rest handle migration, day-to-day generated-project work, debugging and flaky-test fixing. The indexed skill names differ from the directory names for two skills: using-tuist-generated-projects lives under generated-projects/ and migrating-to-tuist-generated-projects lives under migrate/, which is why the install CLI uses the short names.

## Installation

Install the collection with the skills CLI, which detects your coding agents and places the SKILL.md files correctly:

```bash
npx skills add tuist/agent-skills
```

Install a specific skill or target a specific agent:

```bash
npx skills add tuist/agent-skills --skill migrate
npx skills add tuist/agent-skills -a claude-code
npx skills add tuist/agent-skills -g
```

To install manually, download a SKILL.md into the agent skill directory. For example, for Claude Code:

```bash
mkdir -p .claude/skills/compare-builds
curl -o .claude/skills/compare-builds/SKILL.md https://raw.githubusercontent.com/tuist/agent-skills/main/skills/compare-builds/SKILL.md
```

Codex, Amp and OpenCode load skills from their own skills/ directories; the README lists each agent's project and global paths.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| using-tuist-generated-projects | 629 | day-to-day work in Tuist-generated workspaces: generation, build and test commands, buildable folders |
| debug-generated-project | 543 | debugging issues in Tuist-generated projects by reproducing and triaging generation and build failures |
| fix-flaky-tests | 529 | fixing flaky tests from Tuist test insights failure patterns |
| migrating-to-tuist-generated-projects | 521 | migrating existing Xcode projects to Tuist-generated workspaces with build and run validation |
| compare-builds | 317 | comparing two Xcode build runs for duration regressions and cache changes |
| analyze-selective-testing | 310 | analyzing which test targets were skipped or ran, and diagnosing selection regressions |
| compare-generations | 300 | comparing two tuist generate runs for cache hit rate changes |
| compare-bundles | 296 | comparing two app bundles for size changes and new or removed artifacts |
| compare-cache-runs | 291 | comparing two tuist cache runs for cache hit rate and invalidation causes |
| compare-test-runs | 265 | comparing two test runs for new failures and duration regressions |
| compare-test-case | 255 | comparing a single test case across two branches for pass, duration and flakiness |
| compare-gradle-builds | 239 | comparing two Gradle build runs for duration regressions and task outcomes |

All 12 indexed listings clear the 200-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Tuist's value is deterministic, declarative Xcode projects, and its failure modes show up as drift between runs: a build that got slower, a cache that stopped hitting, a test that turned flaky. The comparison skills are built for exactly those regressions, and each accepts the same invocation shapes (build IDs, dashboard URLs, or branch names), which makes them scriptable from an agent that already knows the branch it is on.

For an operator moving an existing app onto Tuist, migrating-to-tuist-generated-projects carries the full checklist (baseline the build, inventory targets and settings, extract xcconfig, validate on a simulator), and using-tuist-generated-projects covers the day-to-day commands afterward. debug-generated-project closes the loop when a generation fails by reproducing locally and deciding whether it is a Tuist bug, a misconfiguration, or a question for the team, and fix-flaky-tests turns a flaky test URL into a root-cause fix.

These skills assume a Tuist and Xcode environment already exists; they do not teach Swift or iOS from scratch, so pair them with the Apple platform skills in Related when the agent needs that context.

## Usage

| You say | What happens |
|---|---|
| Migrate our Xcode project to Tuist | Uses migrating-to-tuist-generated-projects for the baseline, inventory and validation steps |
| This build is slower than last week | Uses compare-builds to diff two build runs for regressions |
| Tests turned flaky after my branch | Uses fix-flaky-tests to analyze failure patterns and correct them |
| The cache hit rate dropped | Uses compare-cache-runs or compare-generations for root-cause analysis |
| Generation fails with a build error | Uses debug-generated-project to reproduce and triage |
| Compare the app bundle across these two branches | Uses compare-bundles for size and artifact changes |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/tuist/agent-skills/main/README.md | head -40
```

Confirm the compare-builds skill body is present before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/tuist/agent-skills/main/skills/compare-builds/SKILL.md | head -30
```

Confirm the day-to-day generated-project skill body, which lives under the directory name generated-projects:

```bash
curl -sL https://raw.githubusercontent.com/tuist/agent-skills/main/skills/generated-projects/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| using-tuist-generated-projects | Pass | Pass | Pass |
| debug-generated-project | Pass | Pass | Warn |
| fix-flaky-tests | Pass | Pass | Pass |
| migrating-to-tuist-generated-projects | Pass | Pass | Pass |
| compare-builds | Pass | Pass | Pass |
| analyze-selective-testing | Pass | Pass | Pass |
| compare-generations | Pass | Pass | Pass |
| compare-bundles | Pass | Pass | Pass |
| compare-cache-runs | Pass | Pass | Pass |
| compare-test-runs | Pass | Pass | Pass |
| compare-test-case | Pass | Pass | Pass |
| compare-gradle-builds | Pass | Pass | Pass |

Every indexed listing is in this sample. The single Warn cell is debug-generated-project (Snyk); the other eleven skills are clean.

## Limitations

- Snapshot data, verified Nov 23, 2026: 4,495 combined installs across 12 indexed listings; 35 GitHub stars; MIT license; last pushed Nov 7, 2026. Counts drift over time.
- The indexed names differ from the directory names for two skills: using-tuist-generated-projects lives under skills/generated-projects/ and migrating-to-tuist-generated-projects lives under skills/migrate/, which is why the install CLI uses the short names.
- The README documents only the migrate skill in its available-skills list; the other eleven skills are described in their own SKILL.md files.
- These skills assume an existing Tuist and Xcode setup; they do not install or configure Tuist itself.
- The repository is a mirror that is automatically updated from tuist/tuist, so skill bodies can change without a release on this repo.

## Related

- [AvdLee SwiftUI Agent Skill - SwiftUI Development Setup](/hermes/skills/catalog/avdlee-swiftui-agent-skill-setup)
- [Swift iOS Skills - Apple Platform Development](/hermes/skills/catalog/dpearson-swift-ios-skills-setup)
- [Axiom Swift Skills Setup](/hermes/skills/catalog/axiom-swift-skills-setup)
- [MobileBuildMCP - iOS and macOS Build Suite](/hermes/skills/catalog/mobilebuildmcp-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use the branch-name invocation shape so the agent can compare the base and head branches it is already on.
- Run migrating-to-tuist-generated-projects first, then using-tuist-generated-projects for daily work; the two cover adoption and steady state.
- Pair fix-flaky-tests with compare-test-runs so the agent first sees what is flaky, then fixes the root cause.
- Keep debug-generated-project handy in CI triage; it decides bug versus misconfiguration before a human is pulled in.
- The comparison skills share one argument style (IDs, dashboard URLs, or branch names), so a single agent helper can drive all seven.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
