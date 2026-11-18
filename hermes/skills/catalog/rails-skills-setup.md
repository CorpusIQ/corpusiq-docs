---
title: "Rails Skills - Ruby on Rails Agent Suite Setup"
description: "thinkoodle/rails-skills: 7.6K combined installs across 35 listings; opinionated Ruby on Rails guidance for AI coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rails-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "ruby on rails", "rails", "coding"]
---

# Rails Skills - Setup Guide

**Source:** [thinkoodle/rails-skills](https://www.skills.sh/thinkoodle/rails-skills) via skills.sh - 7.6K combined installs across 35 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 7 stars, licence unstated, `master` branch, last pushed 2026-09-08. Every skill lives under `skills/<name>/SKILL.md` with reference material alongside, either a single `reference.md` or a `references/` directory of topic files.
**Category:** Ruby on Rails development
**Quality Tier:** 🟡 Yellow - all 60 sampled verdict cells pass, but the repository ships no LICENSE file, so the licence is unstated.

Rails Skills is a collection of Ruby on Rails skills for AI coding agents such as OpenCode and Claude Code. Each skill is an opinionated, agent-focused `SKILL.md` (under 500 lines) plus reference material of detailed patterns, examples, and edge cases, aimed at Rails 8.1 conventions.

The set spans controllers, models, migrations, routing, testing, security, Hotwire (Turbo and Stimulus), Active Storage, caching, and more. The guidance is written as do this, not that rather than exhaustive documentation, so an agent gets a decision instead of a wall of text.

## Installation

Install all skills:

```bash
npx skills add ThinkOodle/rails-skills
```

Install a specific skill by name:

```bash
npx skills add ThinkOodle/rails-skills --skill migrations
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| minitest | 254 | Write fast, maintainable Minitest tests, covering model, policy, request, and system tests plus a TDD workflow. |
| security | 224 | Write secure Rails code, covering CSRF, XSS, SQL injection, credentials, CSP, session security, and other attack vectors. |
| testing | 222 | Set up and choose Rails test types: system, request, helper, mailer, job, and Action Cable tests, plus parallel testing and CI. |
| stimulus | 221 | Build Stimulus controllers with targets, values, actions, lifecycle callbacks, and progressive enhancement. |
| migrations | 221 | Write safe, reversible Active Record migrations for tables, columns, indexes, and schema changes. |
| routing | 220 | Define routes with resources, nested routes, namespaces, constraints, and member or collection routes. |
| active-storage | 220 | Handle file uploads, attachments, image variants, direct uploads, and S3, GCS, or Azure storage. |
| action-controller | 220 | Write controllers with strong parameters, rendering, redirects, sessions, cookies, and CSRF protection. |

The remaining 27 indexed listings range from 204 to 219 installs.

## Why This Matters for Hermes Agents

For an agent writing Rails code, the risk is plausible but wrong answers: a migration that is not reversible, strong parameters handled loosely, or an N+1 query introduced by a generated scope. These skills replace that with opinionated guidance tied to Rails 8.1, each SKILL.md kept under 500 lines so it loads as focused context rather than a documentation dump.

Security and testing are first-class here: the security skill walks every major attack vector with the Rails-idiomatic defense, and the testing skill covers the whole test matrix from system tests to parallel testing and CI. For a Hermes agent that edits code and runs the test suite, these map directly to review and CI gates.

## Usage

| You say | What happens |
|---|---|
| "Add a migration to add an index to this table" | migrations guides a safe, reversible schema change. |
| "Write controller actions with strong parameters" | action-controller covers params permitting, rendering, sessions, and CSRF. |
| "Set up a Minitest suite for this model" | minitest covers model, request, and system tests plus a TDD workflow. |
| "Secure this app against XSS and SQL injection" | security covers the attack vectors and Rails-idiomatic defenses. |
| "Add a Stimulus controller for this toggle" | stimulus covers targets, values, actions, and lifecycle callbacks. |
| "Add nested routes for this resource" | routing covers resources, nesting, namespaces, and constraints. |
| "Handle file uploads to S3" | active-storage covers attachments, variants, and direct uploads. |

## Verification

Probe one skill on the `master` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/thinkoodle/rails-skills/master/skills/migrations/SKILL.md
```

Then install everything, or one skill by name:

```bash
npx skills add ThinkOodle/rails-skills
npx skills add ThinkOodle/rails-skills --skill migrations
```

After install, ask your agent to add a migration or write a test and check it follows the skill's guidance.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| minitest | Pass | Pass | Pass |
| security | Pass | Pass | Pass |
| testing | Pass | Pass | Pass |
| stimulus | Pass | Pass | Pass |
| migrations | Pass | Pass | Pass |
| routing | Pass | Pass | Pass |
| active-storage | Pass | Pass | Pass |
| action-controller | Pass | Pass | Pass |
| turbo | Pass | Pass | Pass |
| lucide-icons | Pass | Pass | Pass |
| i18n | Pass | Pass | Pass |
| active-record-validations | Pass | Pass | Pass |
| active-record-querying | Pass | Pass | Pass |
| active-model | Pass | Pass | Pass |
| active-job | Pass | Pass | Pass |
| action-mailer | Pass | Pass | Pass |
| action-cable | Pass | Pass | Pass |
| uuid-primary-keys | Pass | Pass | Pass |
| generators | Pass | Pass | Pass |
| active-record-associations | Pass | Pass | Pass |

The sample covers 20 of the 35 indexed listings; every cell in all three columns passes.

## Limitations

- Snapshot data, verified Nov 18, 2026: 7,619 combined installs across 35 indexed listings; 7 GitHub stars; licence unstated; last pushed 2026-09-08. Counts drift over time.
- The repository ships no LICENSE file, so the licence is unstated even though the README's License section reads MIT.
- The eight skills shown above carry most of the install volume; the other 27 indexed listings sit between 204 and 219 installs.
- The skills are opinionated and target Rails 8.1 conventions; guidance may not match older or newer Rails versions.
- The repository lives on the `master` branch, so raw file links use `master` and would break if the default branch changes.

## Related

- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [CodeStable Skills - AI Coding Workflow Setup](/hermes/skills/catalog/codestable-skills-setup)
- [Ant Design Skills - Official antd Agent Suite Setup](/hermes/skills/catalog/ant-design-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install everything with npx skills add ThinkOodle/rails-skills, or pull one skill with --skill migrations.
- Read the reference material alongside the SKILL.md; the reference file holds the detailed patterns and edge cases.
- Use the security skill on any code that touches user input; it covers CSRF, XSS, SQL injection, credentials, and CSP.
- Check the Rails version before applying conventions; the skills assume Rails 8.1.
- Confirm the repo state from the master branch before trusting links, and note the licence is unstated.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
