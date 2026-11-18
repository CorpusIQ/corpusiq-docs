---
title: "Han Skills - Claude Code Plugin Marketplace Setup"
description: "thebushidocollective/han: 15.0K combined installs across 96 indexed listings; a Claude Code plugin marketplace for quality gates and tooling."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/han-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "plugin marketplace", "quality gates"]
---

# Han Skills - Setup Guide

**Source:** [thebushidocollective/han](https://www.skills.sh/thebushidocollective/han) via skills.sh - 15.0K combined installs across 96 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 201 stars, NOASSERTION license, `main` branch, last pushed 2026-11-10. Skills live in `plugins/<category>/<plugin>/skills/<name>/SKILL.md` across nine plugin categories, each plugin shipping its own plugin manifest and hooks.
**Category:** Curated Claude Code plugin marketplace
**Quality Tier:** 🟠 Orange - 57 Pass, 0 Warn, 0 Fail and 3 unparsed cells across the 60 sampled verdict cells; GitHub reports NOASSERTION, so the licence is ambiguous rather than a standard permissive one.

Han is a curated marketplace of Claude Code plugins from The Bushido Collective, built around the idea of ship-ready code from an AI coding agent. The README advertises 340 plugins for quality gates, tooling, memory, and specialized agents, installed through a CLI that auto-detects the project stack and runs validation hooks when a coding session ends.

## Installation

The README installs in two commands: fetch the CLI, then auto-detect and install plugins for the project:

```bash
curl -fsSL https://han.guru/install.sh | bash
han plugin install --auto
```

Homebrew is the alternative route:

```bash
brew install thebushidocollective/tap/han
```

Validation hooks run automatically when a Claude Code conversation ends. Further commands include `han plugin install <name>` to install a specific plugin, `han plugin search <query>` to search the marketplace, and `han hook explain` to list configured hooks.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| android-jetpack-compose | 2,274 | Build Android UIs with Jetpack Compose, including state management and declarative UI patterns. |
| fastapi-async-patterns | 961 | Build high-performance FastAPI APIs with async patterns for concurrent requests. |
| atomic-design-fundamentals | 786 | Organize UI components into atoms, molecules, organisms, templates, and pages with Atomic Design. |
| storybook-story-writing | 680 | Write Storybook stories in CSF3 format that showcase component variations and build successfully. |
| solid-principles | 609 | Design modules, functions, and components around the SOLID principles for maintainable architecture. |
| docker-compose-production | 487 | Deploy Docker Compose applications to production with security hardening, resource management, health checks, logging, and monitoring. |
| rails-hotwire | 349 | Build modern reactive Rails applications with Turbo and Stimulus without complex JavaScript frameworks. |
| angular-rxjs-patterns | 291 | Handle async operations in Angular with observables, operators, and subjects. |
| PHP Security Patterns | 277 | Apply PHP security patterns such as input validation, SQL injection prevention, XSS protection, CSRF tokens, and password hashing. |
| django-rest-framework | 265 | Build RESTful APIs with Django REST Framework serializers, viewsets, and authentication. |

The remaining 86 indexed listings range from 52 to 246 installs.

## Why This Matters for Hermes Agents

The core loop is install, code, validate: stop hooks run linters, formatters, type checkers, and tests automatically when a coding session ends, so an agent inherits project-specific quality gates without reconfiguring them. Local metrics track task success and confidence calibration on the machine, so nothing leaves the host. The plugin model spans languages, frameworks, validation, tooling, integrations, patterns, and specialized agents such as Android and iOS.

## Usage

| You say | What happens |
|---|---|
| "Build an Android screen with Jetpack Compose" | Loads android-jetpack-compose for declarative UI and state management. |
| "Make my FastAPI endpoints handle concurrent requests" | Loads fastapi-async-patterns for async handlers and concurrency. |
| "Structure my component library" | Loads atomic-design-fundamentals to organize components into atoms, molecules, and organisms. |
| "Write stories for these components" | Loads storybook-story-writing for CSF3 stories and component variations. |
| "Refactor this module to follow SOLID" | Loads solid-principles for module and component design. |
| "Harden my docker-compose setup for production" | Loads docker-compose-production for security, health checks, and resource limits. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/thebushidocollective/han/main/plugins/core/skills/solid-principles/SKILL.md | head -12
```

Then install and confirm the hooks are wired:

```bash
han plugin install --auto
han hook explain
```

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| android-jetpack-compose | Pass | Pass | Pass |
| fastapi-async-patterns | Pass | Pass | Pass |
| atomic-design-fundamentals | Pass | Pass | Pass |
| storybook-story-writing | Pass | Pass | Pass |
| solid-principles | Pass | Pass | Pass |
| docker-compose-production | Pass | Pass | Pass |
| rails-hotwire | Pass | Pass | Pass |
| angular-rxjs-patterns | Pass | Pass | Pass |
| PHP Security Patterns | not parsed | not parsed | not parsed |
| django-rest-framework | Pass | Pass | Pass |
| cpp-modern-features | Pass | Pass | Pass |
| react-native-web-testing | Pass | Pass | Pass |
| tailwind-responsive-design | Pass | Pass | Pass |
| ansible-roles | Pass | Pass | Pass |
| bdd-patterns | Pass | Pass | Pass |
| playwright-bdd-gherkin-syntax | Pass | Pass | Pass |
| bdd-scenarios | Pass | Pass | Pass |
| storybook-component-documentation | Pass | Pass | Pass |
| sop-maintenance | Pass | Pass | Pass |
| cucumber-best-practices | Pass | Pass | Pass |

The sample covers 20 of the 96 indexed listings; the three not parsed cells all sit on the PHP Security Patterns row, whose listing name uses spaces and capital letters. The other 57 sampled cells are Pass.

## Limitations

- Snapshot data, verified Nov 18, 2026: 15,036 combined installs across 96 indexed listings; 201 GitHub stars; NOASSERTION; last pushed 2026-11-10. Counts drift over time.
- GitHub reports the license as NOASSERTION while the README states MIT, so the license is ambiguous; review it before relying on the plugins in production.
- The security cells for PHP Security Patterns were not parsed by skills.sh because its listing name uses spaces and capital letters; its directory is `php-security-patterns`.
- The `android-jetpack-compose` listing resolves to a directory named `jetpack-compose`; the SKILL.md inside carries the name `android-jetpack-compose`.
- The 10 skills above carry most of the install volume; the other 86 indexed listings sit between 52 and 246 installs and are long-tail.
- The security sample covers 20 of the 96 indexed listings; the remaining 76 have not been re-checked here.

## Related

- [CodeStable Skills - AI Coding Workflow Setup](/hermes/skills/catalog/codestable-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Tech Leads Club Skills - Secure Registry Setup](/hermes/skills/catalog/tech-leads-club-skills-setup)
- [Security Hardening - AI Agent Security Setup](/hermes/skills/catalog/security-and-hardening-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `han plugin install --auto` once per project so validation hooks fire on the right stack.
- Use `han hook explain` to see which linters, formatters, and tests will run when a session ends.
- Install specific plugins by name with `han plugin install <name>` when auto-detect picks the wrong stack.
- Prefer the Homebrew tap on macOS and Linux if you already manage tools with Homebrew.
- Check the license before relying on the plugins: GitHub reports NOASSERTION while the README says MIT.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
