---
title: "Plinth - Java Enterprise SDLC Toolkit Setup"
description: "jabrena/plinth: 31.3K combined installs across 96 listings, a numbered Java enterprise SDLC skill suite spanning Spring Boot, Quarkus, and Micronaut."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jabrena-plinth-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "java", "spring boot", "enterprise"]
---

# Plinth - Setup Guide

**Source:** [jabrena/plinth](https://www.skills.sh/jabrena/plinth) via skills.sh - 31.3K combined installs across 96 indexed listings; first seen Nov 13, 2026 (evening sweep)
**GitHub:** 462 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-13, 126 `SKILL.md` files in `skills/<NNN-name>/` folders
**Category:** Java enterprise SDLC skills, commands, agents and MCP servers
**Quality Tier:** 🟢 Green - 126 in-tree skills, Apache-2.0 license, and all four sampled verdicts pass.

Plinth is an AI-native engineering toolkit for Java enterprise SDLC, built from reusable Skills, Agents, Commands and MCP servers. The README counts 14 commands, 9 agents and 125 skills; the tree holds 126 `SKILL.md` files across numbered families - 0xx inventory, installation, agile and planning, 1xx Java core and design, 3xx Spring Boot, 4xx Quarkus, 5xx Micronaut, 7xx technologies and 8xx EU regulations.

The search API caps a source at 96 rows, so the 96 listings in this pack are a floor. The combined-installs figure counts only those 96 rows, while the tree shows more skills than that. The repo is not prompt-only either - it ships 397 XML files, 171 `.feature` files and Maven wrapper files alongside the markdown skills. Apache-2.0.

## Installation

Install every skill for your preferred agent:

```bash
npx skills add jabrena/plinth --skill '*' --agent claude-code -y
npx skills add jabrena/plinth --skill '*' --agent cursor -y
```

Then install the commands and agents the skills rely on:

```text
install @004-commands-installation claude-code
install @005-agents-installation claude-code
```

The README also documents a full AI-native workflow: run `/onboarding` to establish a root `AGENTS.md` and one OpenSpec project, then move an issue through `/update-issue`, `/explore-problem`, `/create-acceptance-criteria`, `/create-spec`, `/explore-design`, `/implement-spec` and `/close-spec`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| 110-java-maven-best-practices | 505 | Review or improve a pom.xml: BOMs, plugin configuration, version centralization, multi-module structure, build profiles. |
| 121-java-object-oriented-design | 496 | Review or refactor OOD: SOLID, DRY, YAGNI, encapsulation, inheritance, polymorphism, and code-smell removal. |
| 124-java-secure-coding | 486 | Java secure coding: input validation, injection defense, least privilege, strong crypto, safe exception and secrets handling. |
| 131-java-testing-unit-testing | 474 | Unit tests: JUnit 4 to 5 migration, AssertJ, Given-When-Then, parameterized tests, Mockito, boundary conditions. |
| 141-java-refactoring-with-modern-features | 453 | Refactor to modern Java: lambdas, Stream API, Optional, java.time, text blocks, var, Java 25 features. |
| 125-java-concurrency | 426 | Concurrency: thread safety, ExecutorService, CompletableFuture, virtual threads, structured concurrency, backpressure. |
| 301-frameworks-spring-boot-core | 413 | Spring Boot 4.0.x: @SpringBootApplication, bean scoping, @ConfigurationProperties, profiles, constructor injection. |
| 122-java-type-design | 413 | Type design: type hierarchies, naming, value objects over primitives, generics, fluent interfaces, numeric precision. |
| 302-frameworks-spring-boot-rest | 412 | REST APIs with Spring Boot: HTTP methods, status codes, DTOs, versioning, idempotency, ETag, caching, error handling. |
| 321-frameworks-spring-boot-testing-unit-tests | 408 | Spring Boot unit tests: @WebMvcTest, @MockitoBean, @JsonTest, parameterized tests, test profiles. |
| 111-java-maven-dependencies | 407 | Maven dependencies: JSpecify, Error Prone plus NullAway, VAVR, ArchUnit, JavaMoney through a consultative approach. |

The remaining 85 indexed listings range from 210 to 398 installs.

## Why This Matters for Hermes Agents

Plinth treats an SDLC as a pipeline with named stages rather than a grab bag of prompts. The workflow moves an issue through problem framing, acceptance criteria, specification, design, implementation and close, and each stage has a command and a set of skills behind it. An agent working that pipeline produces traceable artifacts - user stories, ADRs, OpenSpec changes - instead of a pile of edits with no provenance.

The framework coverage is the second point. The same numbered pattern repeats across Spring Boot (3xx), Quarkus (4xx) and Micronaut (5xx), so a Java agent can apply the same rest, validation, security, migration and testing guidance regardless of which framework the repo uses. The 7xx and 8xx families add framework-agnostic technologies and EU regulations, which most Java skill packs skip.

The compliance skills are explicit about their own limits. The README states they support engineering awareness and do not provide legal advice, which is the right scope for an agent that should surface obligations but never sign off on them.

## Usage

| You say | What happens |
|---|---|
| "Review this Maven project" | Runs @110-java-maven-best-practices over the pom.xml and returns structured findings. |
| "Write unit tests for this service" | Runs @131-java-testing-unit-testing with JUnit 5, AssertJ and Mockito guidance. |
| "Review this Spring Boot REST API" | Runs @302-frameworks-spring-boot-rest for status codes, DTOs, versioning and idempotency. |
| "Add Flyway migrations" | Runs @313-frameworks-spring-db-migrations-flyway for db/migration scripts and configuration. |
| "Is this system NIS2-ready?" | Runs @804-regulations-eu-nis2 against a maintainer-sanitized evidence inventory. |
| "Generate a WireMock stub" | Runs @702-technologies-wiremock for stub design and request matching. |
| "Onboard this repo for the full workflow" | Runs `/onboarding` to establish AGENTS.md and one OpenSpec project. |

## Verification

Probe skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/jabrena/plinth/main/skills/110-java-maven-best-practices/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/jabrena/plinth/main/skills/121-java-object-oriented-design/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/jabrena/plinth/main/skills/124-java-secure-coding/SKILL.md
```

Skills live at `skills/<NNN-name>/SKILL.md`, with the number prefix in the directory name, so keep the prefix when constructing raw URLs.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| 110-java-maven-best-practices | Pass | Pass | Pass |
| 121-java-object-oriented-design | Pass | Pass | Pass |
| 124-java-secure-coding | Pass | Pass | Pass |
| 131-java-testing-unit-testing | Pass | Pass | Pass |

All four sampled skills pass all three auditors. The sample covers only 4 of the 96 indexed listings, so it says little about the remaining 92. The repo also runs five scanners in its own CI pipeline per the README - MarkdownValidator, skill-check, the Cisco AI skill scanner, NVIDIA SkillSpector and Snyk agent-scan - but that does not substitute for re-checking the skills.sh security pages. The repo ships 397 XML files, 171 `.feature` files and Maven wrapper files whose contents the skill-level verdicts do not cover.

## Limitations

- Snapshot data, verified 2026-11-13: 31,263 combined installs across 96 indexed listings; 462 GitHub stars; Apache-2.0; last pushed 2026-11-13. Counts drift over time.
- The search API caps a source at 96 rows, so both the listing count and the combined-installs figure are a floor. The tree holds 126 `SKILL.md` files, meaning at least 30 skills are not in the index.
- All four sampled verdicts pass, but the sample covers only 4 of 96 listings; the rest publish no verdict on skills.sh.
- This is not a prompt-only pack. The repo ships 397 XML files, 171 `.feature` files and Maven wrapper files, and the skill-level verdicts do not cover those artifacts.
- The 8xx regulation skills support engineering awareness only and do not provide legal advice, per the README.
- Skill results are not deterministic across model runs, and some interactive skills need premium models; the README states a software engineer must review and validate AI-generated outcomes before use.

## Related

- [Claude Code Java - Spring and JVM Review Suite](/hermes/skills/catalog/claude-code-java-setup)
- [Java Development Plugin - 12-Skill Java Engineering Setup](/hermes/skills/catalog/custom-plugin-java-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `/onboarding` first to establish a root `AGENTS.md` and one OpenSpec project; the rest of the workflow assumes that baseline.
- Start an existing repo with @110-java-maven-best-practices to learn the review style before adopting the full pipeline.
- Treat the 8xx regulation skills as awareness aids, not legal advice; pair them with a qualified owner for real compliance work.
- Prefer the framework-specific testing skills (321, 421, 521) over the generic 131 when the project uses Spring Boot, Quarkus, or Micronaut.
- Keep a human in the loop for corporate data; the README warns about authorization, leakage and unintended-modification risk before granting an AI workflow access.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
