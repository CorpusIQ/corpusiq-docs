---
title: "SwiftData Pro - Swift Data Modeling Skill Setup"
description: "twostraws/swiftdata-agent-skill: 9.8K combined installs from one listing, a SwiftData review skill covering models, predicates, indexes and CloudKit."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/swiftdata-pro-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "swiftdata", "swift", "ios"]
---

# SwiftData Pro - Setup Guide

**Source:** [twostraws/swiftdata-agent-skill](https://www.skills.sh/twostraws/swiftdata-agent-skill) via skills.sh - 9.8K combined installs across 1 indexed listing; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 471 stars, MIT license, `main` branch, last pushed 2026-10-19, one `SKILL.md` at `swiftdata-pro/SKILL.md` with five reference files in `swiftdata-pro/references/`
**Category:** Swift and Apple platform data modeling
**Quality Tier:** 🟢 Green - the single sampled skill passes all three auditors.

SwiftData Pro is Paul Hudson's agent skill for SwiftData, the persistence framework that replaced Core Data in Apple's modern stack. It is written for coding assistants rather than for people: the skill points the agent at a review process, then loads only the reference files that the project actually needs.

The author's stated design goal is unusual and useful. The skill is deliberately not a dump of SwiftData fundamentals, on the grounds that models already know the basics and re-teaching them burns context. What the references carry instead are the mistakes models make: unsafe predicates, CloudKit constraints that break sync, indexing opportunities on newer deployment targets, and class inheritance patterns introduced in iOS 26.

## Installation

Install the skill through the Claude Code plugin marketplace:

```text
/plugin marketplace add twostraws/SwiftData-Agent-Skill
/plugin install swiftdata-pro@swiftdata-agent-skill
```

Or install it with the skills CLI for any agent that supports the Agent Skills standard:

```bash
npx skills add https://github.com/twostraws/swiftdata-agent-skill --skill swiftdata-pro
```

The plugin path requires the marketplace name and the plugin name in that exact order. The `npx` path prompts for the target agent and lets you choose a single project or all projects.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| swiftdata-pro | 9,797 | Writing and reviewing SwiftData code: models, safe predicates, CloudKit constraints, indexing and class inheritance. |

The single indexed listing appears in the table above.

## Why This Matters for Hermes Agents

SwiftData is one of the areas where a general coding model produces confident, plausible and wrong code: a predicate that compiles but cannot be translated by the store, a relationship that looks correct until CloudKit rejects it, or a model stack that quietly needs an index nobody added. The skill converts those failure modes into a checklist the agent walks before it answers.

The structure is what makes it usable inside an agent loop. `SKILL.md` is a router with a five-step review process, and each step names the reference file that grounds it. An agent reviewing a single view can load `references/predicates.md` alone instead of the whole library, which keeps the context cost proportional to the question asked.

It also sets project conventions the agent would otherwise guess at. The skill states that the user prefers SwiftData across the board, that Core Data should not be suggested unless a feature genuinely needs it, and that third-party frameworks require a question before adoption. For a Hermes agent working in an existing iOS codebase, that removes a class of unhelpful suggestions.

The output contract is worth noting too. On a review request the skill asks for findings grouped by file, each with the line reference, the rule that was violated, a before-and-after snippet, and a prioritized summary at the end. That is a review a human can act on without reading the diff twice.

## Usage

| You say | What happens |
|---|---|
| "Review my SwiftData models" | Runs the core-rules pass over every model file and reports findings grouped by file. |
| "Why does this fetch return nothing?" | Checks the predicate against the supported predicate rules and reports the unsupported clause. |
| "Add iCloud sync to this app" | Loads the CloudKit reference and applies its constraints before suggesting a configuration. |
| "This list is slow with 50,000 rows" | Checks the deployment target and recommends indexes for the queried properties. |
| "Should I model this as a subclass?" | Loads the class-inheritance reference on iOS 26 targets and checks whether inheritance fits the schema. |
| "Use Core Data here instead" | Holds the SwiftData convention and asks before introducing a second persistence stack. |

## Verification

Fetch the skill file before installing so you can read the routing rules yourself:

```bash
curl -fsSL https://raw.githubusercontent.com/twostraws/swiftdata-agent-skill/main/swiftdata-pro/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/twostraws/swiftdata-agent-skill/main/swiftdata-pro/references/core-rules.md
```

Both paths live under `swiftdata-pro/` rather than at the repository root, so a hand-written install path that points at `SKILL.md` at the top level will 404.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| swiftdata-pro | Pass | Pass | Pass |

The skill is Markdown and reference prose with no executable code, and the repository ships an `agents/openai.yaml` descriptor alongside the Claude Code plugin manifest.

## Limitations

- Snapshot data, verified 2026-11-14: 9,797 combined installs across 1 indexed listing; 471 GitHub stars; MIT; last pushed 2026-10-19. Counts drift over time.
- One skill only. This is not a SwiftData toolkit: there is no migration generator, no schema diffing and no test harness in the repository.
- The indexing reference is scoped to iOS 18 and later, and the class-inheritance reference to iOS 26 and later. Older deployment targets get the core rules only.
- The skill assumes a SwiftData project. It states plainly that Core Data should not be suggested, which is a convention rather than a technical constraint.
- Sibling repos (SwiftUI Pro, Swift Concurrency Pro, Swift Testing Pro) are maintained separately and are not installed by this command.

## Related

- [SwiftUI Pro - Apple UI Development Skill](/hermes/skills/catalog/twostraws-swiftui-pro-setup)
- [Swift Concurrency Skill - Structured Concurrency Setup](/hermes/skills/catalog/swift-concurrency-skill-setup)
- [Dimillian Skills - Apple Platform Engineering Suite Setup](/hermes/skills/catalog/dimillian-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the plugin rather than copying files by hand, so `/plugin update` can move you to newer reference rules.
- Ask for a review of one feature folder at a time; the router loads fewer references and the findings stay readable.
- If a predicate is rejected at runtime, point the agent at `references/predicates.md` explicitly instead of asking it to retry the query.
- Keep the deployment target in the prompt ("this app targets iOS 18") so the agent knows whether the indexing and inheritance references apply.
- The skill is deliberately terse. If your agent ignores short instructions, pair it with a rule that says to run the review process before answering.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
