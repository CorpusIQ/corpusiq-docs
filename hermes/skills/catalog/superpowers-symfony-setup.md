---
title: "Superpowers Symfony - 44 Symfony Skills for Coding Agents"
description: "dev-toolings/superpowers-symfony - 28.6K combined installs across 88 indexed listings: 44 skills for Doctrine ORM, API Platform, TDD and Messenger."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/superpowers-symfony-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "symfony", "doctrine", "api platform", "tdd"]
---

# Superpowers Symfony - Setup Guide

**Source:** [dev-toolings/superpowers-symfony](https://www.skills.sh/dev-toolings/superpowers-symfony) via skills.sh - 28.6K combined installs across 88 indexed listings; first seen Nov 16, 2026 (Nov 16 evening sweep)
**GitHub:** 234 stars, MIT license, `main` branch, last pushed 2026-11-11, 44 skills under `content/skills/<name>/SKILL.md` plus 7 agents and 13 commands under `content/agents/` and `content/commands/`
**Category:** Symfony for coding agents - Doctrine ORM 3, API Platform, TDD, Messenger, security and DDD
**Quality Tier:** 🟡 Yellow - no scanner verdicts are published for this publisher: the Gen Agent Trust Hub, Socket and Snyk columns are empty on all 24 sampled skills.

Superpowers Symfony is a Claude Code plugin that doubles as a plain Markdown skill library for Symfony 7.4 LTS and 8.x. The tree is vendor-neutral: `content/` is the source of truth, and a Bun build generates per-harness adapters for Codex, Cursor, Windsurf, Copilot, Gemini, aider and others, while Claude Code reads `content/` directly through plugin.json.

Version accuracy is the point. Guidance targets Symfony 7.4 LTS and 8.x (6.4 LTS as legacy), API Platform 5 with a 4.4 bridge, and Doctrine ORM 3, so signatures and examples match the framework an agent actually runs. A `bin/symfony-context` probe detects the Symfony version, API Platform, Docker setup (Symfony Docker, DDEV, Compose or host) and test framework, then prints the correctly prefixed console, composer and test commands; Claude Code runs it at session start.

## Installation

Claude Code plugin marketplace (the README's own path):

```sh
claude plugin marketplace add dev-toolings/superpowers-symfony
claude plugin install superpowers-symfony@superpowers-symfony
```

Other harnesses use `AGENTS.md` plus the generated adapters, or the skills CLI:

```sh
npx skills add dev-toolings/superpowers-symfony
```

By hand: copy `content/skills/<name>/` into your agent's skills directory. Each skill is one `SKILL.md` plus a `reference.md`; for a Hermes profile that is `~/.hermes/profiles/corpusiq/skills/`. Copy the whole `content/skills/` tree if you use the workflow, since the skills link to each other.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| symfony:interfaces-and-autowiring | 708 | Dependency injection: autowiring, #[Target] binding, decoration and tagged services. |
| symfony:controller-cleanup | 655 | Refactoring fat controllers into lean services, handlers and invokable commands. |
| symfony:doctrine-migrations | 641 | Creating and managing migrations (bundle 4.x, library 3.9) with rollbacks and deploy paths. |
| symfony:tdd-with-phpunit | 634 | RED-GREEN-REFACTOR with PHPUnit 10/11 via KernelTestCase and WebTestCase. |
| symfony:quality-checks | 622 | PHP-CS-Fixer, PHPStan and type safety checks. |
| symfony:doctrine-relations | 612 | OneToMany, ManyToMany and ManyToOne with cascade, orphan removal and N+1 prevention. |
| symfony:bootstrap-check | 598 | Verifying .env, services.yaml, doctrine settings and framework requirements. |
| symfony:cqrs-and-handlers | 595 | Separate Command and Query buses and handlers via Messenger. |
| symfony:symfony-messenger | 589 | Async messaging with RabbitMQ, Redis or Doctrine transports, middleware and retries. |
| symfony:twig-components | 566 | UX Twig Components with props, slots, anonymous components and CVA. |
| symfony:using-symfony-superpowers | 565 | The entry point: workflow guidance and the command map. |
| symfony:effective-context | 554 | Giving the agent relevant files, patterns and constraints. |
| symfony:doctrine-transactions | 550 | wrapInTransaction, optimistic and pessimistic locking, and flush strategies. |
| symfony:functional-tests | 546 | WebTestCase, getContainer, loginUser and DAMA rollback for controllers. |
| symfony:config-env-parameters | 539 | .env files, parameters, secrets vault and environment-specific settings. |
| symfony:symfony-voters | 536 | Granular authorization that decouples permission logic from controllers. |
| symfony:symfony-cache | 536 | Cache pools, tag invalidation and stampede prevention. |
| symfony:api-platform-security | 534 | Security expressions, voters, securityPostValidation and operation-level access. |
| symfony:value-objects-and-dtos | 530 | Readonly value objects and DTOs for domain and transfer boundaries. |
| symfony:doctrine-fetch-modes | 526 | DTO hydration, fetch joins, lazy loading, query hints and DBAL 4. |
| symfony:executing-plans | 525 | Executing implementation plans with TDD and incremental commits. |
| symfony:api-platform-state-providers | 525 | ProviderInterface and ProcessorInterface to decouple retrieval from entities. |
| symfony:ports-and-adapters | 524 | Hexagonal architecture separating domain logic from infrastructure. |
| symfony:doctrine-batch-processing | 521 | toIterable, flush and clear, and bulk DQL for large datasets. |
| symfony:api-platform-dto-resources | 521 | Mapping entities to API DTOs with #[Map] and stateOptions. |
| symfony:doctrine-fixtures-foundry | 518 | Zenstruck Foundry v2 factories for test data. |
| symfony:api-platform-filters | 517 | QueryParameter and the Parameters API for search, date, range and custom filters. |
| symfony:brainstorming | 515 | Structured brainstorming for features and architecture. |
| symfony:api-platform-tests | 512 | ApiTestCase assertions for collections, items, filters, schema and auth. |
| symfony:api-platform-resources | 511 | Explicit operations, pagination and typed OpenAPI. |
| symfony:strategy-pattern | 505 | Tagged services for runtime algorithm selection. |
| tdd-with-phpunit | 150 | The plain-name listing of the same tree directory as symfony:tdd-with-phpunit, shown here to explain the double indexing below. |

The remaining 56 indexed listings range from 101 to 499 installs.

The row with 150 installs sits below 500 on purpose. Every skill directory is indexed twice, once with the `symfony:` plugin prefix and once by its plain directory name, so the 88 indexed listings map onto 44 tree directories. The plain-name twins (tdd-with-phpunit, doctrine-migrations, doctrine-transactions and the rest) carry far lower install counts than their prefixed versions, which is where the traffic lands.

## Why This Matters for Hermes Agents

Superpowers Symfony is a full framework curriculum in one skill tree, and the version targeting is what makes it useful: guidance is pinned to Symfony 7.4 LTS and 8.x, API Platform 5 and Doctrine ORM 3, so an agent writes signatures that exist in the project it is actually working on. The `bin/symfony-context` probe turns that into automation by detecting the stack at session start and printing the right console, composer and test commands, which removes the Docker-setup guessing that normally precedes any Symfony task.

The coverage spans Doctrine schema and query tuning, API Platform resources and security, Messenger async workflows, voters and rate limiting, plus the plan and TDD loop that wraps them, and seven read-only and implement agents let a builder fan out audits and TDD cycles as sub-agents. The plan workflow is the part worth copying: brainstorming, writing-plans, executing-plans and daily-workflow take a feature from idea to verified commits, with executing-plans insisting on TDD and one verified commit per step.

The content is vendor-neutral plain Markdown, with per-harness adapters generated from it, so a Hermes profile can consume the same `content/skills/` tree as Claude Code, Codex or Cursor with no lock-in.

## Usage

| You say | What happens |
|---|---|
| "Create a Doctrine migration for the new orders table" | symfony:doctrine-migrations walks schema versioning, dependencies and rollback so the migration matches the bundle in use. |
| "Add a OneToMany relation between users and orders without N+1 queries" | symfony:doctrine-relations configures cascade and orphan removal and flags the fetch-mode choices. |
| "Secure this API endpoint with a voter" | symfony:api-platform-security and symfony:symfony-voters add security expressions and permission logic outside the controller. |
| "I want to do TDD on this feature" | symfony:tdd-with-phpunit (or symfony:tdd-with-pest) drives a RED-GREEN-REFACTOR cycle with KernelTestCase or WebTestCase. |
| "Set up async messaging with retries" | symfony:symfony-messenger and symfony:messenger-retry-failures configure transports, middleware and failure recovery. |
| "Refactor this fat controller" | symfony:controller-cleanup extracts business logic into services, handlers and invokable commands. |
| "Run the quality checks before I commit" | symfony:quality-checks runs PHP-CS-Fixer and PHPStan, then reports the failures. |

## Verification

Check the tree before copying:

```sh
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/dev-toolings/superpowers-symfony/main/content/skills/interfaces-and-autowiring/SKILL.md
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/dev-toolings/superpowers-symfony/main/content/skills/doctrine-migrations/SKILL.md
```

Each URL prints 200. The skill root is `content/skills/` on branch `main`, and every directory named in the table sits directly under it with its own SKILL.md plus a reference.md.

After copying, count what landed:

```sh
find ~/.hermes/profiles/corpusiq/skills -maxdepth 2 -name SKILL.md | wc -l
```

The count should be 44 if the profile started empty.

## Security

skills.sh publishes no scanner verdicts for this publisher (checked Nov 16, 2026) - the Gen Agent Trust Hub, Socket and Snyk cells are empty on all 24 sampled skill pages, so re-check the skills.sh pages yourself before production use:

An empty verdict is not a pass. Treat every skill in this set as unread by the three scanners, and read the `SKILL.md` of any skill that touches authentication, authorization or migrations before an agent runs it. `symfony:api-platform-security` and `symfony:symfony-voters` are the two that write security expressions and voter logic, so start there. The repository is MIT licensed and every skill is plain Markdown plus the `bin/symfony-context` probe, so the review surface is a text read rather than a compiled dependency.

## Limitations

- Snapshot data, verified Nov 16, 2026: 28,628 combined installs across 88 indexed listings; 234 GitHub stars; MIT; last pushed 2026-11-11. Counts drift over time.
- Every skill directory is indexed twice, once with the `symfony:` prefix and once by plain directory name, so any per-listing install figure is roughly half the skill's real usage.
- None of the 24 sampled skills carries a scanner verdict on skills.sh, so there is no automated security signal here; read the SKILL.md before an agent runs one.
- The per-harness adapters are generated by a Bun build, and CI fails if `dist/` drifts from `content/`, so edits must go through the build rather than by hand.
- Runtime accuracy depends on the `bin/symfony-context` probe running first; without it the agent does not get the correctly prefixed console and composer commands.
- Some skills assume a Docker setup (Symfony Docker, DDEV or Compose); on a bare host the runner-selection skill must pick the right runner first.

## Related

- [Obra Superpowers](/hermes/skills/catalog/obra-superpowers-setup)
- [Superpowers Framework](/hermes/skills/catalog/superpowers-setup)
- [Laravel Boost](/hermes/skills/catalog/laravel-boost-setup)
- [Appwrite Skills](/hermes/skills/catalog/appwrite-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy the whole `content/skills/` tree: the plan and TDD skills link to each other, and a partial copy breaks the workflow chain.
- Run `bin/symfony-context --format=markdown` first in any session; the agent needs the detected version and runner before it can write correct Symfony code.
- Use executing-plans for anything larger than one edit: TDD with one verified commit per step keeps long runs reversible.
- Prefer the prefixed listing names (symfony:doctrine-migrations) when searching install traffic; the plain-name twins carry a fraction of the installs.
- Route security work to the symfony-security-auditor agent, which is read-only and reports, rather than letting a generic implement agent touch security.yaml.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
