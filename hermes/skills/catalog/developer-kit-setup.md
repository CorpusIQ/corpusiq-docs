---
title: "Developer Kit - Java and TypeScript Skill Suite Setup"
description: "Giuseppe Trisciuoglio's developer-kit: 408.7K combined installs. Spring Boot, Next.js, React, NestJS, AWS and unit-test skills in one plugin set."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/developer-kit-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "spring boot", "nextjs", "typescript", "java"]
---

# Developer Kit - Setup Guide

**Source:** [giuseppe-trisciuoglio/developer-kit](https://www.skills.sh/giuseppe-trisciuoglio/developer-kit) via skills.sh - 408.7K combined installs across 130 indexed listings; snapshot 2026-10-28 (Oct 28 morning sweep)

**GitHub:** [giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit) - 365 stars, MIT, branch main, 119 `SKILL.md` files under `plugins/<plugin>/skills/` across 11 plugin directories, with the CloudFormation and AWS families nested one directory deeper

**Category:** Full-stack application patterns for Java, TypeScript, Python and PHP teams, with AWS and AI skills

**Quality Tier:** 🟡 Beta - single maintainer, 365 GitHub stars, 130 indexed listings against 119 skill directories, security verdicts sampled for 6 skills only

Developer Kit is Giuseppe Trisciuoglio's modular plugin marketplace for coding agents, version 4.0.1 in `.claude-plugin/marketplace.json`. Each plugin carries four layers: skills that load on demand, subagents, slash commands, and path scoped rules that activate from the `globs:` patterns in their headers. The split is by stack rather than by task. `developer-kit-java` carries 51 skills for Spring Boot, LangChain4J, the AWS SDK and GraalVM, `developer-kit-typescript` carries 25 for NestJS, React, Next.js, Drizzle ORM and monorepos, and `developer-kit-core`, `developer-kit-aws`, `developer-kit-ai`, `developer-kit-php`, `developer-kit-python`, `developer-kit-tools` and `developer-kit-devops` add the rest, while `github-spec-kit` ships three commands and no skills. The README is published in English, Italian, Chinese and Spanish.

The install index and the tree do not fully agree, and that is the first thing to know. skills.sh indexes 130 listings against 119 skill directories in the clone. Fourteen of those listings, from `knowledge-graph` at 1,919 installs down to `qdrant-vector-database-integration` at 68, have no matching directory anywhere in the current tree. The names read like a spec and project management family from an earlier layout, and the current `plugins/github-spec-kit` ships three `speckit.*` commands and no skills at all. Treat that block as historical until the publisher restores it, and install from the directories that exist.

## Installation

The README leads with the Claude Code plugin marketplace:

```bash
/plugin marketplace add giuseppe-trisciuoglio/developer-kit
```

The second documented route clones the repository and runs the Makefile installer, which detects the CLIs on the machine or takes an explicit target:

```bash
git clone https://github.com/giuseppe-trisciuoglio/developer-kit.git
cd developer-kit
make install
make install-claude
make install-codex
make install-opencode
make install-copilot
make install-kimi
make install-kiro
```

The targets differ in what they copy. Codex and Kimi receive skills only, with no agents and no commands; Kiro receives skills plus agents as JSON and prompts; OpenCode receives agents, commands and skills; Copilot receives agents and skills but no commands. Every target reads the `skills[]` array from each plugin's `plugin.json`, and those 11 manifests enumerate 119 entries in total, which is every skill directory in the tree. Claude Desktop users enable Skills in Settings, then add `giuseppe-trisciuoglio/developer-kit`.

No per-skill installer is documented for other agents, so on Hermes the tree is the install source. Each directory under `plugins/<plugin>/skills/` holds one `SKILL.md`, so a copy is equivalent to a CLI install of that skill:

```bash
git clone --depth 1 https://github.com/giuseppe-trisciuoglio/developer-kit.git
cp -R developer-kit/plugins/developer-kit-typescript/skills/shadcn-ui \
  ~/.hermes/profiles/corpusiq/skills/
```

Rules are a separate step that no plugin performs. The README offers `make copy-rules PLUGIN=developer-kit-java`, or a manual copy of `plugins/developer-kit-[language]/rules/*.md` into `.claude/rules/`, and they then activate by file glob.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| shadcn-ui | 22,376 | Installing and configuring shadcn/ui in a React app: component setup, forms with React Hook Form and Zod, Tailwind theme customization, and buttons, dialogs, dropdowns, tables and complex form layouts. |
| tailwind-css-patterns | 17,667 | Styling with Tailwind utility-first patterns: responsive layout, flexbox and grid, spacing, typography, colour scales and design-system work in React, Vue and Svelte components. |
| drizzle-orm-patterns | 5,434 | Drizzle ORM work end to end: schema definition, CRUD, relations, type-safe queries, transactions and Drizzle Kit migrations across PostgreSQL, MySQL, SQLite, MSSQL and CockroachDB. |
| unit-test-bean-validation | 4,891 | Testing Jakarta Bean Validation without a Spring context: `@Valid`, `@NotNull`, `@Min`, `@Max` and `@Email` constraints with Hibernate Validator, custom validators, violation assertions and validation groups. |
| nextjs-performance | 4,870 | Next.js performance work against Core Web Vitals: `next/image` and `next/font`, `unstable_cache` and `revalidateTag` caching, Suspense streaming, Server Component conversion and bundle analysis, on Next.js 16 with React 19. |
| react-patterns | 4,738 | React 19 server and concurrent patterns: Server Components, Server Actions, `useOptimistic`, `useActionState`, `useTransition`, Suspense boundaries and memoization with React Compiler. |
| tailwind-design-system | 4,544 | Building a design system on Tailwind and shadcn/ui: design tokens, CSS variable theming, component primitives and the initial configuration pass. |
| react-code-review | 4,349 | Reviewing React changes before merge: component architecture, hooks usage, React 19 patterns, state management, performance, accessibility and TypeScript typing. |
| spring-boot-test-patterns | 4,268 | Spring Boot test coverage: unit, slice, integration and Testcontainers runs with JUnit 5 and Mockito, plus `@MockBean` wiring and test suite performance. |
| nestjs | 4,238 | NestJS services with Drizzle ORM: REST and GraphQL APIs, authentication guards, database schemas and microservice setup. |
| typescript-docs | 4,224 | TypeScript documentation: JSDoc and TypeDoc output, API references, decision records and audience-specific examples for NestJS, Express, React, Angular and Vue. |
| spring-boot-rest-api-standards | 4,164 | REST endpoint design for Spring Boot: DTOs, error handling, pagination, security headers, HATEOAS and layering rules. |
| spring-boot-security-jwt | 4,125 | JWT authentication on Spring Boot 3.5 with Spring Security 6: JJWT token generation, Bearer and cookie authentication, database or OAuth2 identity, and RBAC plus permission checks. |
| spring-data-jpa | 4,086 | Persistence layers with Spring Data JPA: repositories, entity relationships, derived and `@Query` queries, pagination, auditing, transactions, UUID keys and multi-database indexing. |
| turborepo-monorepo | 4,063 | Turborepo monorepos: workspaces, `turbo.json` tasks, Next.js and NestJS apps inside one repo, Vitest and Jest pipelines, CI/CD, remote caching and build profiling. |
| unit-test-boundary-conditions | 4,054 | Java boundary and edge case tests with JUnit 5 and AssertJ: minimum and maximum values, nulls, empty collections, numeric overflow, floating point precision and off-by-one errors. |
| spring-boot-openapi-documentation | 4,020 | API documentation with SpringDoc OpenAPI 3 and Swagger UI on Spring Boot 3: annotations, security schemes, examples and schema definitions. |

The remaining 113 indexed listings range from 2 to 3,961 installs. `drawio-logical-diagrams` (3,961) and `clean-architecture` (3,954) sit closest to the cut, followed by a dense block of unit-test and Spring Boot skills between 3,600 and 3,800, the LangChain4J and AWS SDK for Java v2 families, the CloudFormation templates at 65 to 68, and five listings at 2 or 3 installs. Fourteen of those listings have no directory in the current tree.

## Why This Matters for Hermes Agents

Most skill suites answer one question well. This one is organised like a team's standards library, and the value is in the boring parts that agents usually improvise: where the DTO boundary sits, how a JWT filter is wired, which annotation actually triggers validation, what a Spring Boot test should slice. An agent that has to reconstruct those from memory produces code that compiles and then fails review.

The unit-test family is the most distinctive block. Fifteen separate `unit-test-*` skills cover validation, boundary conditions, the service layer, controller and repository slices, WireMock against a REST API, JSON serialization, caching, scheduled and async work, security authorization, mapper converters and configuration properties. That granularity means an agent can be pointed at one kind of test instead of being told to "write tests" and inventing a shape.

The TypeScript side is version-aware in a way that matters for review quality. `nextjs-performance` targets Next.js 16 with React 19 and names the current caching primitives, `react-patterns` covers Server Actions and the optimistic hooks rather than the class component era, and the code review skills are separate from the build skills, so the review pass is not the same prompt that wrote the code.

Two practical caveats for agent use. First, `allowed-tools` in these files is mostly `Read, Write, Edit, Bash, Glob, Grep`, so the skills assume they can edit files and run commands; a Hermes session should keep its own approval gates in front of that. Second, the Java half assumes a Spring Boot 3.5 baseline and the TypeScript half assumes current majors, so an agent working on an older stack should be told the versions explicitly rather than trusting the defaults.

## Usage

| You say | What happens |
|---|---|
| "Generate a CRUD module for a User entity with NestJS and Drizzle" | nestjs and drizzle-orm-patterns produce the schema, repository, service and controller, with the query layer type-safe and the relation wiring explicit. |
| "Review this Spring Boot service for security issues" | spring-boot-security-jwt and spring-boot-rest-api-standards walk the authentication chain, authorization checks, error handling and header configuration, then report findings before editing. |
| "Write tests for this Java validation logic" | unit-test-bean-validation builds the validator tests without starting a Spring context, asserts the constraint violations, and adds parameterized cases for the validation groups. |
| "Our Next.js dashboard is slow on mobile" | nextjs-performance works through Core Web Vitals: image and font loading, the caching calls, Suspense boundaries and bundle size, then proposes Server Component conversions. |
| "Set up a design system on top of shadcn/ui" | tailwind-design-system defines tokens and CSS variable theming, then wraps the shadcn primitives so later components inherit one source of truth. |
| "This monorepo build takes nine minutes" | turborepo-monorepo inspects `turbo.json` task inputs and outputs, checks cache misses per package, and adjusts the pipeline and remote cache settings. |
| "Document the REST API before handover" | spring-boot-openapi-documentation adds SpringDoc annotations and security schemes, then points Swagger UI at the generated spec. |

## Verification

Probe the paths before installing. All five URLs below returned 200 when this guide was written:

```bash
for p in plugins/developer-kit-typescript/skills/shadcn-ui/SKILL.md \
         plugins/developer-kit-typescript/skills/tailwind-css-patterns/SKILL.md \
         plugins/developer-kit-java/skills/spring-boot-security-jwt/SKILL.md \
         plugins/developer-kit-ai/skills/prompt-engineering/SKILL.md \
         plugins/developer-kit-core/hooks/hooks.json; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/giuseppe-trisciuoglio/developer-kit/main/$p"
done
```

Read the two that touch credentials and authentication before installing them:

- https://raw.githubusercontent.com/giuseppe-trisciuoglio/developer-kit/main/plugins/developer-kit-java/skills/spring-boot-security-jwt/SKILL.md
- https://raw.githubusercontent.com/giuseppe-trisciuoglio/developer-kit/main/plugins/developer-kit-core/hooks/hooks.json

After a copy install, confirm what actually landed, since the copy step decides what is present:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -cE '^(shadcn-ui|tailwind-css-patterns|react-|nextjs-|spring-)'
head -5 ~/.hermes/profiles/corpusiq/skills/shadcn-ui/SKILL.md
```

The `head` output should show `name: shadcn-ui`, which is also the name the install index uses, so a mismatch there means you copied a different directory. Check counts against the source rather than against the index: the clone holds 119 `SKILL.md` files and the index lists 130.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| shadcn-ui | Pass | Pass | Pass |
| tailwind-css-patterns | Pass | Pass | Pass |
| drizzle-orm-patterns | Pass | Pass | Pass |
| unit-test-bean-validation | Pass | Pass | Pass |
| nextjs-performance | Pass | Warn | Pass |
| react-patterns | Pass | Pass | Pass |

Six skills were sampled out of 130 listings, so the verdict table covers the most installed few and nothing else. The repository runs its own checks in CI, `security-scan.yml` and `plugin-validation.yml`, and `.skills-validator-check/validators/cli.py` validates components locally, but a passing author validator is not an independent audit.

The install surface wires one executable component. `plugins/developer-kit-core/hooks/hooks.json` wires a `PreToolUse` hook on `Bash` that runs `prevent-destructive-commands.py`, a standard library only Python script that blocks commands matching a destructive pattern list or targeting paths outside the working directory, exiting 2 to block. A second file, `auto-learn-on-stop.py`, exists in the same directory but the `Stop` array in `hooks.json` is empty, so it is not wired and will not run.

At run time the skills can write and execute. `allowed-tools` across the tree most commonly lists `Read, Write, Edit, Bash, Glob, Grep`, 35 files use exactly that set and a handful add `Task`, `WebFetch` or `AskUserQuestion`. The README says plainly that skills can execute code and asks readers to review `SKILL.md` before enabling and to test outside production. The Java and AWS skills scaffold projects, edit source and emit CloudFormation templates, so keep the review step and the approval gate between the skill and any real account.

## Limitations

- Snapshot data, verified 2026-10-28: 408,740 combined installs across 130 indexed listings; 365 GitHub stars; MIT; last pushed 2026-09-10. Counts drift over time.
- The index outruns the tree by 14 listings. `knowledge-graph` (1,919), `specs-code-cleanup` (1,774), `ralph-loop` (1,747), `create-pr-from-spec` (1,450), `constitution` (1,424), `brainstorm-prompt-optimizer` (880), `specs-e2e-verification` (874), `sdd-init` (874), `specs-explore` (871), `task-quality-kpi` (532), `claude-md-management` (301), `clean-architecture-php` (90), `rag-implementation` (70) and `qdrant-vector-database-integration` (68) have no directory anywhere in the clone. A per-skill install of any of them has nothing to copy from this tree.
- The README badges advertise 150+ skills and 45+ agents. The clone holds 119 `SKILL.md` files, 44 agent definitions, 35 command files and 31 rule files, so the badges round upward past what is present.
- `clean-architecture` exists as four separate directories, one each under the java, typescript, php and python plugins, but only one listing is indexed, pointed at the TypeScript path. An install of "clean-architecture" installs one stack's version, not all four.
- Rules are not installed by the plugins. Anything that depends on the auto-activating `globs:` rules needs the separate `make copy-rules PLUGIN=<name>` step, and that step targets `.claude/rules/`, not a Hermes skills directory.
- The installer targets Claude Code, Copilot CLI, OpenCode, Codex, Kimi and Kiro. There is no Hermes target and no documented skills.sh CLI install, so the copy route is the only supported path here, and it brings no agents, commands, rules or hooks with it.

## Related

- [Jeff Allan Claude Skills - Full-Stack Dev Setup](/hermes/skills/catalog/jeffallan-claude-skills-setup) - the closest all-round full-stack counterpart
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup) - deeper Next.js coverage than the bundled skills
- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup) - the single-library counterpart to the most installed skill here
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by plugin group, not the whole marketplace. `developer-kit-typescript` and `developer-kit-java` are each large enough to cost context on every turn, and pulling both when the job is one of them is wasted budget.
- Start with `developer-kit-core`. It holds the commands and the destructive command hook, and the other plugins assume the core layer is present.
- Ask which version baseline the skill is writing against before accepting code. The Java half targets Spring Boot 3.5 with Spring Security 6 and the TypeScript half targets Next.js 16 with React 19, and an older codebase needs to be stated, not assumed.
- Use the review skills as a separate pass. `react-code-review`, `nestjs-code-review` and `nextjs-code-review` are distinct from the skills that generate the code, and running them after the edit catches the patterns the generator itself chose.
- Keep the hooks out unless you want them. `prevent-destructive-commands.py` blocks Bash commands outside the working directory, which is useful for unattended runs and surprising for a scripted workflow that legitimately touches paths elsewhere.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
