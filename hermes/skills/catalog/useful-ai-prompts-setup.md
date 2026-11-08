---
title: "Useful AI Prompts - 260 Skill Prompt Library Setup"
description: "aj-geddes/useful-ai-prompts on skills.sh: 128.7K combined installs across 200 listings; 260+ skills of production-ready prompts and code patterns."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/useful-ai-prompts-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "prompt library", "engineering prompts", "claude code skills"]
---

# Useful AI Prompts - Setup Guide

**Source:** [aj-geddes/useful-ai-prompts](https://www.skills.sh/aj-geddes/useful-ai-prompts) via skills.sh - 128.7K combined installs across 200 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 378 stars, MIT, last pushed 2026-03-04, 259 SKILL.md directories under `skills/`, plus 488 prompts in `prompts/`, 7 automation hooks in `hooks/` and a machine-readable `PROMPT-INDEX.json`
**Category:** Breadth-first prompt and skill library covering engineering, infrastructure, data, design, security and product work
**Quality Tier:** 🟡 Yellow - MIT licence with a LICENSE file in the root, but one sampled skill returns a Socket warn and the repository also ships seven shell hooks that run outside the skills.

This is a catalog rather than a product. The repository holds 488 prompts arranged across 47 categories, each written to a single template with seven XML tags, and it also ships 259 skill directories that package the same domain knowledge for a coding agent. The README rounds that up to 260+ skills and 488+ prompts; the tree counts in this guide are the ones to trust.

The consistency is the selling point. Every prompt carries the same metadata block, the same `<role>`, `<context>`, `<task>` and `<quality_criteria>` sections, and the README lists eleven quality gates that each prompt had to pass, including measurable criteria, realistic examples and copy-paste readiness. Whether or not every file lives up to that, the format means you can read one prompt and predict the shape of the other 487.

## Installation

The README has no skills CLI line. Its documented route is a copy into a project skills directory:

```bash
cp -r skills/ /path/to/your/project/.claude/skills/
```

Because skills.sh indexes the repository, the skills CLI also works. The README does not spell out a skill name, so confirm the name in the current tree before adding one:

```bash
npx skills add aj-geddes/useful-ai-prompts
npx skills add aj-geddes/useful-ai-prompts --skill nodejs-express-server
```

Prompts are not installed. Browse `prompts/` or the GitHub Pages index, copy the body of the `## Prompt` section including the XML tags, and paste it into the agent.

Hooks are separate from skills and need their own copy, from the hooks README:

```bash
cp -r hooks/security-scan /your/project/.claude/hooks/
```

The copy route is the Hermes route. Each entry under `skills/` is a plain folder with a `SKILL.md`, so the same tree can be copied or linked into a Hermes profile's skills directory. The repository does not ship a Hermes specific command, so the copy is the supported path and the CLI is a convenience wrapper.

## What It Provides

Twenty three listings clear the 800-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| nodejs-express-server | 3,298 | Express servers with middleware chains, routing, authentication and database access |
| code-review-analysis | 2,422 | Structured pull request review: best practices, security checks, constructive feedback |
| jenkins-pipeline | 2,147 | Declarative and scripted Jenkins pipelines, multi-branch builds, deployment stages |
| rest-api-design | 2,092 | Resource modelling, HTTP methods, status codes, versioning and API documentation |
| architecture-diagrams | 1,973 | Mermaid, PlantUML, C4, flowchart and sequence diagrams for system design |
| ansible-automation | 1,860 | Playbooks, roles and inventories for configuration management and patching |
| ios-swift-development | 1,521 | Native iOS with Swift, MVVM, SwiftUI, URLSession, Combine and Core Data |
| nginx-configuration | 1,478 | Reverse proxy, load balancing, TLS, caching and API gateway configuration |
| android-kotlin-development | 1,473 | Kotlin apps with MVVM, Jetpack Compose, Retrofit, Room and navigation |
| flask-api-development | 1,441 | Lightweight Flask APIs with blueprints, auth and database integration |
| wireframe-prototyping | 1,436 | Wireframes and interactive prototypes for feedback before development |
| markdown-documentation | 1,307 | GitHub Flavored Markdown, README files and documentation formatting |
| terraform-infrastructure | 1,177 | Modular infrastructure as code, state management and multi-cloud provisioning |
| responsive-web-design | 1,104 | Grid, Flexbox and media queries for layouts that adapt across devices |
| penetration-testing | 1,084 | Ethical hacking methodology, exploit frameworks and manual validation |
| css-architecture | 968 | BEM, SMACSS and CSS-in-JS patterns for maintainable styling |
| api-contract-testing | 924 | Pact and consumer-driven contracts that catch breaking changes |
| root-cause-analysis | 913 | Structured RCA methods intended to stop an issue recurring |
| event-sourcing | 892 | Event stores, aggregates and projections with CQRS |
| mobile-first-design | 867 | Designing at phone size first, then scaling up |
| api-security-hardening | 867 | Auth, rate limiting, CORS and input validation for endpoints |
| mobile-app-testing | 831 | Unit, UI and integration tests with Detox, Appium and XCTest |
| technical-specification | 810 | Requirements, design and architecture specification documents |

The remaining 177 indexed listings range from 454 to 792 installs.

The shape of the set matters more than any single row. The top eight rows are all implementation work in an existing stack: a server, a review, a pipeline, an API, a diagram. The design and testing rows sit lower, and the data science skills sit lower still, which matches a library written for web and infrastructure engineers first.

## Why This Matters for Hermes Agents

An agent asked to "set up CI" or "review this PR" works from whatever general knowledge the model carries. That output is usually plausible and often close, and the missing parts are the ones a specialist would not miss: the retry policy on the deploy stage, the migration order, the rollback step. A skill that encodes a checklist closes part of that gap cheaply.

The prompt format is the reusable part. Because every prompt separates role, context, inputs, task, output specification, quality criteria and constraints, the agent can be told to produce work in that shape, and a human can review the result against stated criteria instead of taste. Copying the structure into your own prompt files is worth more than copying any individual prompt.

The breadth has a cost. 259 skills in one directory is a large surface to audit, many of them overlap with what a modern model already does well, and the last push predates the current generation of agent tooling. Treat the library as a source of checklists and scaffolds to adapt, not as a curated install.

For a Hermes agent, the practical use is reference. Point it at one skill for the task at hand, such as `api-contract-testing` before a breaking change, rather than loading the whole tree. The per-skill folders are small, and the agent reads one file at a time.

The hooks are a different category of risk. They are bash scripts wired to pre-commit, post-save and session-start events, and they run with your shell permissions on every matching event. Read `hook.sh` before you copy one.

## Usage

| You say | What happens |
|---|---|
| "Review this pull request for security issues" | `code-review-analysis` walks a review checklist: correctness, security checks, test coverage, feedback wording |
| "Design the endpoints for a booking API" | `rest-api-design` proposes resources, methods, status codes, versioning and an OpenAPI shape |
| "Write the Jenkins pipeline for this repo" | `jenkins-pipeline` produces a declarative or scripted pipeline with stages, agents and parameters |
| "Draw the architecture for our event pipeline" | `architecture-diagrams` emits Mermaid or PlantUML source for a C4 or sequence view |
| "Why does this keep breaking in production?" | `root-cause-analysis` applies a structured RCA sequence instead of a guess |
| "Write the technical spec for this feature" | `technical-specification` produces a requirements and design document with open questions called out |
| "Harden these API endpoints" | `api-security-hardening` checks auth, rate limiting, CORS and input validation in order |

## Verification

Read one skill before installing anything. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/aj-geddes/useful-ai-prompts/main/skills/nodejs-express-server/SKILL.md | head -12
```

The file should open with `name: nodejs-express-server` and a description about building production-ready Express servers.

After the copy, confirm the folder count. The tree holds 259 skill directories at this commit:

```bash
ls .claude/skills | wc -l
```

If the number is far lower, the copy landed in a subdirectory and the agent will not find the skills. Two other useful probes: `curl` the same raw path for `root-cause-analysis` to check the second batch of files, and open `SKILLS-MATRIX.md`, which is the repository's own index of what each skill covers.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07). This is a snapshot, so re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nodejs-express-server | Pass | Warn | Pass |
| code-review-analysis | Pass | Pass | Pass |
| jenkins-pipeline | Pass | Pass | Pass |

Every skill is a `SKILL.md` with optional reference files, and 209 of the 259 skill directories also ship a `scripts/` folder holding one small bash helper, named `validate-api.sh`, `scaffold-tests.sh`, `security-checklist.sh` and similar. Those helpers print checklists or write files, and they run only when the agent is told to run one; nothing in the install fires them. The hooks are the part that fires on its own. `hooks/` contains seven bash scripts, including `security-scan`, which greps staged files for AWS keys, GitHub tokens, bearer tokens and private keys, and `dependency-check`, which runs an audit. They are copied separately from the skills and are not part of `npx skills add`, so an install of the skills alone leaves them inert.

The Socket warning on the most installed skill is worth reading on skills.sh rather than assuming the worst. A warn on a skill folder containing markdown and a helper script is a different finding from a warn on a package you install and run.

The licence is MIT with a `LICENSE` file in the repository root, so the usual MIT terms apply to reuse and redistribution.

## Limitations

- Snapshot data, verified 2026-11-07: 128,658 combined installs across 200 indexed listings; 378 GitHub stars; MIT; last pushed 2026-03-04. Counts drift over time.
- The last push is March 2026, the oldest in this wave. The prompts describe tooling as it stood then, so treat versions, API shapes and framework advice as needing a check against current docs.
- The README advertises 260+ skills and 488+ prompts. The tree at this commit counts 259 skill directories with a `SKILL.md` each, and `prompts/` is the only place the full prompt count can be confirmed, so the marketing numbers are one or two above the tree.
- Breadth is not depth. Several of the 259 skills restate what a current model already does well, and the per-skill files are short, so the library is a scaffold to adapt rather than a specialist consultant.
- The hooks library is not covered by the skills.sh verdicts at all, and `hooks/README.md` describes six hooks while `hooks/` holds seven directories. Read the script you plan to use.
- The install index and the tree use different naming for a few entries: display names such as Funnel Analysis and Time Series Analysis appear in the index while the directories use hyphenated slugs. Match on the slug.

## Related

- [Claude Code Skills - Agentic Coding & Skill](/hermes/skills/catalog/claude-code-skills-setup)
- [Agentic Awesome Skills (AAS) - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup)
- [Awesome LLM Apps Skills - Role-Based Agent Skills](/hermes/skills/catalog/awesome-llm-apps-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start from `SKILLS-MATRIX.md`, which maps skill names to one-line descriptions, then install only the handful you would actually invoke in a week.
- Read the `## Prompt` body of a prompt you already know well. It is the fastest way to judge whether the eleven quality gates mean anything.
- Keep the prompts and the skills separate in your head. Prompts are text you paste, skills are files the agent loads, and mixing them wastes context.
- If you use the hooks, run each `hook.sh` by hand once with `bash -x` on a scratch repo. Pre-commit hooks that fail closed can block every commit until you find the regex.
- Copy the `quality_criteria` section shape into your own skills. The measurable-criteria requirement is the part most home-grown skills lack.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
