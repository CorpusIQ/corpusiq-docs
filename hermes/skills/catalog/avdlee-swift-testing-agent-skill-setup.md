---
title: "AvdLee Swift Testing Skill - XCTest Migration Setup"
description: "avdlee/swift-testing-agent-skill on skills.sh: 5.4K combined installs; Swift Testing macros, parameterized tests, traits and XCTest migration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/avdlee-swift-testing-agent-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "swift", "swift testing", "xctest"]
---

# AvdLee Swift Testing Skill - Setup Guide

**Source:** [avdlee/swift-testing-agent-skill](https://www.skills.sh/avdlee/swift-testing-agent-skill) via skills.sh - 5.4K combined installs across 1 indexed listing; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 479 stars, MIT, last pushed 2026-04-22, one SKILL.md at `swift-testing-expert/SKILL.md` with nine topic references beside it under `references/`
**Category:** Swift testing for agents: parameterized tests, traits and tags, async testing and migration away from XCTest
**Quality Tier:** 🟢 Production - MIT licensed, 479 stars, and every sampled audit passes.

This is not the same project as twostraws/swift-testing-agent-skill, which this catalog documents separately as [Swift Testing Pro Skill](/hermes/skills/catalog/swift-testing-pro-skill-setup). Different publisher, different repository, different skill name: AvdLee publishes `swift-testing-expert` (Antoine van der Lee, SwiftLee), twostraws publishes `swift-testing-pro` (Paul Hudson). The install counts belong to their own sources and should never be added together.

The skill is a single agent playbook for Swift Testing, the modern test framework that replaced most of XCTest's assertion style. It opens with an eight rule behavior contract for the agent: prefer Swift Testing for unit and integration tests, keep XCTest for UI automation through `XCUIApplication`, performance metrics through `XCTMetric` and Objective-C test code; treat `#expect` as the default assertion and `#require` as the way to stop a test when a prerequisite is missing; default to parallel safe guidance before reaching for `.serialized`.

Behind the playbook sit nine reference files, each one topic: fundamentals, expectations, traits and tags, parameterized testing, parallelization and isolation, performance and best practices, async testing and waiting, migration from XCTest, and Xcode workflows. The SKILL.md is a routing table into those files, which is what keeps a 5,422 install skill usable inside a normal context window.

## Installation

The README's recommended route is the skills CLI, pinned to the single skill in the repository:

```bash
npx skills add https://github.com/avdlee/swift-testing-agent-skill --skill swift-testing-expert
```

For Claude Code there is a plugin route. Add the marketplace, then install the skill:

```bash
/plugin marketplace add AvdLee/Swift-Testing-Agent-Skill
/plugin install swift-testing-expert@swift-testing-agent-skill
```

If a release does not show up after updating, the README's fix is to refresh the marketplace first, since Claude Code reads plugin versions from its local marketplace copy:

```bash
/plugin marketplace update swift-testing-agent-skill
```

A team can also enable it per repository through `.claude/settings.json`, which prompts each member to install it when they open the project:

```json
{
  "enabledPlugins": {
    "swift-testing-expert@swift-testing-agent-skill": true
  },
  "extraKnownMarketplaces": {
    "swift-testing-agent-skill": {
      "source": {
        "source": "github",
        "repo": "AvdLee/Swift-Testing-Agent-Skill"
      }
    }
  }
}
```

The manual route is a clone plus a copy or symlink of the `swift-testing-expert/` folder into whatever location your harness reads skills from, following that tool's own documentation.

## What It Provides

One listing, far above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| swift-testing-expert | 5,422 | Writing, reviewing, migrating and debugging Swift tests: #expect and #require, suites, traits and tags, parameterized tests, parallel isolation, async waiting, XCTest coexistence |

No indexed listings fall below the 500-install threshold; the single listing appears above.

## Why This Matters for Hermes Agents

Swift Testing is recent enough that most training data still reflects XCTest habits, and the difference is not cosmetic. A model that writes `XCTAssertEqual` in a new target gets tests that work but miss the diagnostics, the parameterization and the parallel defaults the framework was built around. A model that reaches for `.serialized` at the first flaky test hides an isolation bug instead of fixing it, which the skill calls out as a temporary compromise rather than a solution.

The agent behavior contract is the part that changes output most. Rule three alone, defaulting to parallel safe guidance and proposing isolation fixes before serialization, prevents the most common regression an agent introduces when it is asked to make a test suite pass.

The references also handle the migration question honestly. XCTest does not disappear: UI automation, performance metrics and Objective-C tests stay where they are, and the skill maps the rest incrementally, assertions first, then suite organization, then parameterization and traits. That staged path is far more useful to an agent working in a real target than a blanket rewrite instruction.

Because the material is grounded in the SwiftLee article set and the two WWDC 2024 Swift Testing sessions, the advice is checkable against primary sources rather than invented.

## Usage

| You say | What happens |
|---|---|
| "Review this test target for migration opportunities" | Applies the migration reference: assertion mapping first, then suites, then parameterization, keeping UI and performance tests on XCTest |
| "These ten tests differ only by input" | Converts them into one parameterized `@Test(arguments:)` with a clean argument list |
| "Why is this test suite flaky in CI?" | Works the isolation angle: shared state first, in-memory repositories, `.serialized` only as a transition step |
| "Should this be #expect or #require?" | Uses the prerequisite rule: `#require` when later lines depend on the value, `#expect` otherwise |
| "Tag our smoke tests so the plan can filter them" | Applies traits and tags guidance, then tag driven test plan filtering instead of name based include and exclude |
| "This callback API is awkward to test" | Bridges it to async and await with the continuation patterns in the async reference |
| "Which assertions still have to stay XCTest?" | Names the exceptions: `XCUIApplication`, `XCTMetric` and Objective-C only test code |

## Verification

Read the routing file before installing, since it is the contract the agent follows:

```bash
curl -fsSL https://raw.githubusercontent.com/avdlee/swift-testing-agent-skill/main/swift-testing-expert/SKILL.md | head -5
```

It should open with `name: swift-testing-expert` and a description listing test structure, `#expect` and `#require`, traits and tags, parameterized tests and XCTest migration. Then confirm the reference corpus arrived, which is where most of the detail lives:

```bash
git clone --depth 1 https://github.com/avdlee/swift-testing-agent-skill.git
ls swift-testing-agent-skill/swift-testing-expert/references | wc -l
```

The count should be 10: `_index.md` plus the nine topic files. After installing, find the skill directory and confirm both parts are present:

```bash
find ~ -maxdepth 5 -type d -name "swift-testing-expert" 2>/dev/null
```

The behavioral check from the README is that the agent references the routing playbook in `SKILL.md` and then opens the relevant file under `references/` rather than answering from memory.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| swift-testing-expert | Pass | Pass | Pass |

Everything in the repository is markdown: one SKILL.md, nine reference files, a README, a contributing guide and a license. There are no scripts, no hooks and no install time execution, and the Agent Skills format it follows carries instructions only.

The content is advisory, so the practical risk is not code execution but bad advice applied confidently. The references cite Apple documentation and WWDC sessions, which makes a disputed claim checkable.

## Limitations

- Snapshot data, verified 2026-11-05: 5,422 combined installs across 1 indexed listing; 479 GitHub stars; MIT; last pushed 2026-04-22. Counts drift over time.
- The repository name collides with twostraws/swift-testing-agent-skill, which ships a different skill called `swift-testing-pro`. Check the publisher and the skill name before following any install command you find in a blog post.
- It assumes a toolchain that has Swift Testing. The README grounds the material in the WWDC 2024 sessions, so a project pinned to an older Xcode gets guidance it cannot compile.
- It is guidance, not tooling. There is no test runner, no report parser and no CI integration; it tells the agent what to write and how to reason about a failure.
- The skill is opinionated about keeping XCTest for UI automation, performance metrics and Objective-C tests, so a migration that reads it as "convert everything" will produce advice the skill itself does not support.
- One maintainer and one repository. The references are thorough for the topics listed, but there is no coverage of third party test frameworks or server side Swift testing beyond the general patterns.

## Related

- [Swift Testing Pro Skill - Swift Testing Suite Setup](/hermes/skills/catalog/swift-testing-pro-skill-setup)
- [Swift Concurrency Agent Skill - Swift 6 Setup](/hermes/skills/catalog/avdlee-swift-concurrency-setup)
- [Swift iOS Skills - iOS 26 and SwiftUI Suite Setup](/hermes/skills/catalog/dpearson-swift-ios-skills-setup)

## Pro Tips

- Ask for the migration in stages. Assertions first, then suites, then parameterization and traits, because a single pass over a large target usually breaks the build in several places at once.
- Have the agent name the reference it used. "Per references/parallelization-and-isolation.md" is a checkable claim, and it keeps answers inside the documented material.
- Use `.serialized` only with a written reason. The skill treats it as a transition step, and a comment saying what shared state is still being fixed makes the debt visible.
- Pair this with a concurrency skill on async test problems. Waiting patterns and actor isolation questions overlap heavily once tests start crossing isolation boundaries.
- Run the review on new tests before they land. It is cheaper as a writing constraint than as a cleanup pass over a suite that already passes.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
