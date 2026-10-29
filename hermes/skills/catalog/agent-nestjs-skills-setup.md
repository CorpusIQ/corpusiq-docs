---
title: "NestJS Best Practices - 40-Rule Agent Skill Setup Guide"
description: "NestJS Best Practices: 30.7K combined installs. One agent skill with 40 rules across 10 categories, from modules and DI to security and testing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-nestjs-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "nestjs", "typescript", "backend"]
---

# NestJS Best Practices - Setup Guide

**Source:** [kadajett/agent-nestjs-skills](https://www.skills.sh/kadajett/agent-nestjs-skills) via skills.sh - 30.7K combined installs across 1 indexed listing; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [kadajett/agent-nestjs-skills](https://github.com/kadajett/agent-nestjs-skills) - 292 stars, no license file at the repository root (the GitHub API reports no SPDX identifier), branch main, last pushed 2026-07-23; one skill directory at `skills/nestjs-best-practices/` holding `SKILL.md` plus 40 rule files and two support files under `rules/`, with `metadata.json`, a generated `AGENTS.md` and a `scripts/` build at the root

**Category:** NestJS backend engineering rules packaged as a single agent skill

**Quality Tier:** 🟡 Beta - single-author skill at 30,694 installs on its only indexed listing, 292 GitHub stars, no license file at the repository root, and a last push three months before this snapshot

Kadajett's repository is one skill rather than a collection: 40 NestJS rules across 10 categories, ordered by impact from CRITICAL architecture and dependency injection down to LOW-MEDIUM DevOps and deployment. The README describes it as a structured repository for creating and maintaining NestJS best practices optimized for agents and LLMs, and the structure is borrowed from the Vercel React Best Practices skill set. It carries 30,694 installs on a single indexed listing and 292 GitHub stars, so that figure is a statement about one skill, and a fairly widely used one.

The layout is built for progressive reading. `SKILL.md` stays short: a priority table for the ten categories, a quick reference listing all 40 rule ids by prefix, then instructions to read individual rule files. Each rule is its own markdown file under `rules/` with frontmatter for title, impact and impactDescription, a short explanation of why it matters, and a paired incorrect and correct code example. A build script in `scripts/` compiles every rule into `AGENTS.md` at the repository root, which is the same content in one file for agents that read that convention. `metadata.json` dates the set January 2026 at version 1.2.0, and the fuller documentation site lives on a separate `docs` branch.

## Installation

Install through the skills.sh CLI. The README gives three spellings:

```bash
npx skills add Kadajett/agent-nestjs-skills
npx skills add Kadajett/agent-nestjs-skills --global
npx skills add Kadajett/agent-nestjs-skills -a claude-code -a cursor
```

The first installs into the current project, `--global` installs for every project, and `-a` narrows the target agents. The README names Claude Code, OpenCode, Codex, Cursor, Antigravity and Roo Code as supported agents, and a later section adds AdaL. What the installer copies is `skills/nestjs-best-practices/`, which the README calls out explicitly, so the rule files travel with the entry point.

Nothing in the repository is written for Hermes. The manual route is a clone plus a directory copy:

```bash
git clone https://github.com/kadajett/agent-nestjs-skills.git
cp -R agent-nestjs-skills/skills/nestjs-best-practices ~/.hermes/profiles/corpusiq/skills/
```

Copy the whole directory rather than just `SKILL.md`. The quick reference points at `rules/*.md` relative to the skill folder, so a bare file copy leaves the agent with 40 dangling paths.

The build is only needed when you edit rules. If you fork the repository and add or change one:

```bash
cd agent-nestjs-skills/scripts && npm install
npm run build
```

The README offers `./scripts/build.sh` as an alternative to `npm run build`. Neither runs at install time; the skill is markdown all the way down.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| nestjs-best-practices | 30694 | Writing, reviewing or refactoring NestJS code against 40 impact-ranked rules in 10 categories: feature-module architecture and circular dependencies, dependency injection scopes and injection tokens, exception filters and async errors, JWT auth, guards, class-validator input validation and rate limiting, caching and query performance, Nest testing utilities and Supertest E2E, transactions and N+1 queries, DTO serialization, interceptors, API versioning, microservice patterns, queues and health checks, and ConfigModule, structured logging and graceful shutdown. |

No indexed listings fall below the threshold; the single listing in the index is the row above.

The quick reference splits those 40 rules into ten sections, each with an impact level and a filename prefix:

- 1. Architecture (CRITICAL, `arch-`): circular module dependencies, feature modules over technical layers, module exports and duplicate providers, single-responsibility services, the repository pattern for testability, and events for decoupling.
- 2. Dependency Injection (CRITICAL, `di-`): constructor injection over property injection, injection tokens for interfaces, singleton/request/transient scope awareness, and the service locator, interface segregation and Liskov rules.
- 3. Error Handling (HIGH, `error-`): centralized exception filters, NestJS HTTP exceptions, and async error handling.
- 4. Security (HIGH, `security-`): JWT authentication, guards, input validation with class-validator, output sanitization against XSS, and rate limiting.
- 5. Performance (HIGH, `perf-`): async lifecycle hooks, caching, database query optimization, and lazy-loaded modules.
- 6. Testing (MEDIUM-HIGH, `test-`): the Nest testing module, Supertest for E2E, and mocking external services.
- 7. Database and ORM (MEDIUM-HIGH, `db-`): transaction management, N+1 avoidance, and migrations.
- 8. API Design (MEDIUM, `api-`): DTO and response serialization, interceptors, versioning, and pipes for input transformation.
- 9. Microservices (MEDIUM, `micro-`): message and event patterns, health checks for orchestration, and background job queues.
- 10. DevOps and Deployment (LOW-MEDIUM, `devops-`): ConfigModule for environment configuration, structured logging, and graceful shutdown.

## Why This Matters for Hermes Agents

NestJS goes wrong in ways that still compile. A circular module import, a request-scoped provider pulled into a singleton, a service that quietly became the place everything calls: none of these break the build, and all of them are expensive to unpick later. An agent answering from general Node knowledge tends to produce a controller that works and a module graph that does not scale.

The impact column is what makes this usable as an instruction set rather than a style guide. An agent can order its own review: CRITICAL architecture and dependency injection first, HIGH security and performance next, MEDIUM API design last. That is a cheap way to spend a fixed context budget on the findings that change the module graph.

Every rule ships as an explanation plus an incorrect and a correct example, so review output can name the rule and show the pattern it is replacing instead of asserting a preference. The ids are short and stable (`arch-module-sharing`, `db-avoid-n-plus-one`), which makes them easy to cite in a commit message, a PR comment or a follow-up prompt.

The compiled `AGENTS.md` doubles the reach. Coding agents that read a root `AGENTS.md` get all 40 rules in one file without walking `rules/`, while Hermes can stay on the skill and open a single rule file when a question is narrow. For a profile that already carries a large skill library, an entry point under 5 KB with on-demand rules is close to free.

What it does not do is enforce anything. There is no linter, no generator and no test runner in the repository; the skill supplies the standard, and the build, type check and test suite are still what prove a change.

## Usage

| You say | What happens |
|---|---|
| "Review this controller and service before I merge" | The skill walks the architecture, dependency injection and error handling rules against the files, flags a circular import or an overloaded service, and names the rule behind each finding. |
| "Add JWT auth with guards to this module" | It works through `security-auth-jwt`, `security-use-guards` and `security-validate-all-input`, keeping token handling in the strategy and validation in the pipe layer. |
| "This endpoint got slow after we added the orders relation" | `db-avoid-n-plus-one` and `perf-optimize-database` point at the eager relation and the query pattern, with `perf-use-caching` as the follow-up if the read is genuinely hot. |
| "Why does injecting this provider slow every request down" | `di-scope-awareness` explains request scope propagation, and why one request-scoped provider pulls its dependents into that scope. |
| "Write E2E tests for the checkout route" | `test-e2e-supertest` plus `test-use-testing-module` builds the app inside a test module, and `test-mock-external-services` replaces the payment call. |
| "Split this god service into proper modules" | `arch-single-responsibility`, `arch-feature-modules` and `arch-module-sharing` propose the split and the export surface, with `arch-use-events` where the new modules would otherwise import each other. |
| "Get this API ready to run in production" | `api-versioning`, `devops-use-config-module`, `devops-use-logging`, `micro-use-health-checks` and `devops-graceful-shutdown` cover the deployment surface in one pass. |

## Verification

All six URLs below returned 200 on the main branch when this guide was written. The first is the entry point and the rest are files it points at or that the index relies on:

```bash
for p in skills/nestjs-best-practices/SKILL.md \
         skills/nestjs-best-practices/rules/_sections.md \
         skills/nestjs-best-practices/rules/security-validate-all-input.md \
         skills/nestjs-best-practices/rules/arch-avoid-circular-deps.md \
         AGENTS.md \
         metadata.json; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/kadajett/agent-nestjs-skills/main/$p"
done
```

Read the entry point before installing, then the one rule you are least sure about:

- https://raw.githubusercontent.com/kadajett/agent-nestjs-skills/main/skills/nestjs-best-practices/SKILL.md
- https://raw.githubusercontent.com/kadajett/agent-nestjs-skills/main/skills/nestjs-best-practices/rules/security-validate-all-input.md

After the copy, confirm the entry point and the rule files both landed. The frontmatter name and the directory name should match, and the rule count should match the 40 ids in the quick reference plus `_sections.md` and `_template.md`:

```bash
ls ~/.hermes/profiles/corpusiq/skills/nestjs-best-practices
head -5 ~/.hermes/profiles/corpusiq/skills/nestjs-best-practices/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/nestjs-best-practices/rules/*.md | wc -l
```

A count of 42 means the whole set came across, because two of those files are support files the build skips. If the count is 1, the copy took `SKILL.md` alone and every rule path in it is broken.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nestjs-best-practices | Pass | Pass | Pass |

All three auditors pass, and that sample covers the whole indexed surface because the repository carries a single listing.

The license position needs care rather than a verdict. The GitHub API reports no SPDX identifier and there is no `LICENSE` file at the repository root, while `SKILL.md` declares `license: MIT` in its own frontmatter. Read the repository as unlicensed at the project level: the per-file claim is a statement of intent, not a grant that clearly covers redistribution.

What runs on install is small. The CLI copies a markdown directory, and the repository has no manifest at its root, so there is no root-level lifecycle script to execute. The only npm surface sits in `scripts/`, whose `package.json` declares TypeScript, ts-node and the Node types as devDependencies with `build` and `build:watch` entries and no install or postinstall hook. Nothing in the skill directory executes when an agent loads it.

The content is where the risk sits, because the rules teach security plumbing: JWT authentication, guards, DTO validation, output sanitization and rate limiting. Generated guard and strategy code should get the same review as a contractor's PR, and the failure to watch is a default that reads secure and is not, such as validation wired to one controller while a second entry point accepts the same payload unchecked.

One independence note: the README features and links the maintainer's own product, Semfora, a semantic code analysis engine with nine MCP tools. `SKILL.md` does not reference it, and nothing in the install path depends on it.

## Limitations

- Snapshot data, verified 2026-10-28: 30694 combined installs across 1 indexed listing; 292 GitHub stars; no license file at the repository root; last pushed 2026-07-23. Counts drift over time.
- One listing, one skill, one framework. The install figure measures a single NestJS skill with nothing else in the repository to compare it against, and it offers nothing for React, Angular, Vue or a plain Node service.
- The repository is unlicensed at the project level: no `LICENSE` file at the root and no SPDX identifier from the GitHub API, while the skill's own frontmatter says MIT. Confirm terms with the maintainer before vendoring or republishing it.
- Install documentation covers the skills.sh CLI and the six named agents plus AdaL. Nothing names Hermes, the `--agent` flag is not documented, and the directory copy above is the route to use.
- Maintenance is paced. The last push was 2026-07-23, roughly three months before this snapshot, the README note says the maintainer has a few hours a week, and the rules carry no NestJS version pin beyond metadata version 1.2.0 dated January 2026.
- Rules are guidance, not enforcement, and the root `AGENTS.md` is generated from `rules/`. Nothing here lints, generates or tests your code, so a compliant-looking diff still needs the build, type check and test suite, and edits belong in the rule files rather than in the compiled output.

## Related

- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)

## Pro Tips

- Spend the first pass on the two CRITICAL sections. Architecture and dependency injection change the module graph, and every later rule reads differently once that graph is right.
- Name the rule id when you know it, for example "apply `security-validate-all-input` to this DTO". The quick reference lists all 40 ids, so the agent opens one file instead of re-reading the summary.
- Use `rules/` for review work and `AGENTS.md` for tools that read that convention. Same content, and the compiled file saves a walk through 40 paths when the whole set is needed at once.
- Copy the directory, not the file. `SKILL.md` is a router, and an install that carries only the router looks like it works until the agent needs the rule it cites.
- Ask for the incorrect and correct pair when a finding is contested. Each rule file has both, which turns a disagreement about style into a diff you can compare.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
