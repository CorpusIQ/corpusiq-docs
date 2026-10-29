---
title: "Java Development Plugin - 12-Skill Java Engineering Setup"
description: "Java Development Plugin: 17.5K combined installs. 12 skills cover Spring Boot, JUnit 5 testing, Maven and Gradle builds, JPA/Hibernate and Docker."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/custom-plugin-java-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "java", "spring boot", "maven", "jpa"]
---

# Java Development Plugin - Setup Guide

**Source:** [pluginagentmarketplace/custom-plugin-java](https://www.skills.sh/pluginagentmarketplace/custom-plugin-java) via skills.sh - 17.5K combined installs across 12 indexed listings; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [pluginagentmarketplace/custom-plugin-java](https://github.com/pluginagentmarketplace/custom-plugin-java) - 41 stars, license field NOASSERTION with no standard SPDX license at the root (the repository ships a custom `LICENSE` file labelled Plugin Agent Marketplace - Custom License), branch main, last pushed 2026-01-05; 12 `SKILL.md` directories under `skills/`, one for every indexed listing, alongside 8 agent definitions in `agents/`, 4 slash commands in `commands/` and a `.claude-plugin/` manifest pair

**Category:** Java engineering skill pack for Claude Code plugins and agent skill directories

**Quality Tier:** 🟡 Beta - vendor maintained by Plugin Agent Marketplace, 41 GitHub stars, all 12 indexed listings map to a `SKILL.md` directory in the current tree, and the repository carries a custom license rather than a standard SPDX one

The pack is published as "Java Assistant", a Claude Code plugin at version 3.0.0 that pairs 8 agents with 12 SASMP-compliant skills covering one slice of Java work each: language fundamentals, Spring Boot, testing, Maven and Gradle, JPA and Hibernate, microservices, concurrency, performance and Docker. Each skill directory holds a single `SKILL.md` with a parameter block that asks for the target Java version, Spring version or database before it starts writing code, which is the detail that keeps an agent from answering with Java 8 idioms for a Java 21 service.

Adoption is lopsided in a useful way. The Spring Boot skill alone carries 11,783 of the 17,533 combined installs, and the next four sit between 615 and 904, so the practical core of the pack is roughly five skills, with seven more in the 263 to 499 range that cover the specialist edges of the stack. The install surface is the plugin, but the portable unit is the `skills/` tree: plain `SKILL.md` directories that any agent runtime can read.

## Installation

The README documents Claude Code as the target, and it leads with the marketplace route:

```text
/plugin marketplace add pluginagentmarketplace/custom-plugin-java
/plugin install java-development-assistant@pluginagentmarketplace-java
```

Restart Claude Code after the install, and it exposes eight agents under the `java-development-assistant` namespace, from `01-java-fundamentals` through `08-java-devops`. The second README option clones the repository and loads it from disk:

```bash
git clone https://github.com/pluginagentmarketplace/custom-plugin-java.git
cd custom-plugin-java
```

```text
/plugin load .
```

The README lists Claude Code CLI v2.0.27 or newer and an active Claude subscription as prerequisites, and it publishes no skills.sh CLI command. For a Hermes profile the skills directory is the install target, since each listing is a self-contained `SKILL.md` directory with no plugin runtime requirement:

```bash
git clone https://github.com/pluginagentmarketplace/custom-plugin-java.git
cp -R custom-plugin-java/skills/* ~/.hermes/profiles/corpusiq/skills/
```

That copy route is a manual pattern rather than a documented one. Commit or prune the copied directories afterwards, because 12 new top-level skill folders compete for the same Java trigger phrases as anything already installed.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| java-spring-boot | 11783 | Production Spring Boot 3.x application work: REST APIs, security configuration, data access, actuator monitoring and cloud integration, with Spring version and module as declared parameters. |
| java-testing | 904 | Writing unit, integration, contract and end-to-end tests with JUnit 5, Mockito, AssertJ, Spring Boot Test and Testcontainers, including TDD patterns and coverage strategy. |
| java-maven | 897 | Configure Maven POM files, lifecycle phases, build plugins, dependency management with BOMs, and single, library or multi-module project structure. |
| java-fundamentals | 621 | Core Java 8 through 21: syntax, OOP design, choosing collection types, the streams API, generics and exception handling. |
| java-jpa-hibernate | 615 | Persistence layers: entity design, Spring Data repositories, query strategies, transactions and caching, with N+1 queries called out as the thing to prevent. |

The remaining 7 indexed listings range from 263 to 499 installs.

## Why This Matters for Hermes Agents

Java backends are where agents do the most damage when they improvise, because the correct answer depends on a version and a framework generation that the request rarely states. Every skill in this pack opens with a parameter block that forces that declaration: `java_version` accepts 8, 11, 17 or 21 and defaults to 21, `spring_version` defaults to 3.2, and the persistence skill asks for postgresql, mysql, oracle or h2 before it writes a line.

The coverage is organised by task rather than by language feature, which matches how an agent gets asked for help. A request to fix a slow endpoint lands in the Spring Boot skill, a request to stop a flaky suite lands in the testing skill, and a request to explain why a Hibernate call fires 200 selects lands in the persistence skill that names N+1 as its target.

The bond structure is worth knowing before you install. Eight skills are primary, each bonded to one of the eight README agents, and four are secondary, which is why the secondary skills carry the thinner install counts and the narrower scope. In Hermes only the `skills/` tree matters, so the agent and command layers are optional context rather than load-bearing parts of the install.

Tool scope is narrow and declarable: every sampled `SKILL.md` lists Read, Write, Bash, Glob and Grep, so the skills can run a build or a test command but are not written to fetch anything from the network. That makes the permission conversation short, and it also means a skill that starts reaching for downloads is behaving outside its own declaration.

## Usage

| You say | What happens |
|---|---|
| "Add a paginated REST endpoint to this Spring Boot service" | java-spring-boot asks for the Spring version and module focus, then writes the controller, service and repository layers with the project's existing conventions. |
| "These JUnit tests pass alone and fail in the suite, tighten them" | java-testing works through isolation and lifecycle problems, then adds a Testcontainers integration test where a mocked boundary is the real cause. |
| "The Maven build takes nine minutes, find out why" | java-maven reads the POM, inspects lifecycle phases and plugin configuration, and proposes the profile and dependency changes that shorten the build. |
| "Why is this stream collector slower than the loop it replaced" | java-fundamentals explains the boxing and allocation cost, then rewrites the pipeline in the style the JDK version supports. |
| "This Hibernate query fires two hundred selects, fix it" | java-jpa-hibernate finds the N+1 pattern, switches to a fetch join or entity graph, and checks the transaction boundary around it. |
| "Split this module into two services with a saga" | java-microservices picks a saga, CQRS or API gateway shape from its declared parameters, then lays out the service boundaries and the messaging choice. |
| "We are moving this project from Java 11 to 21" | java-fundamentals sets `java_version` to 21 and walks the syntax, collection and streams changes that matter for the upgrade. |

## Verification

Every URL below returned 200 on branch `main` when this guide was written. Probe them before installing and read the Spring Boot and testing skills first, since those two set the conventions the rest follow:

```bash
for p in skills/java-spring-boot/SKILL.md \
         skills/java-testing/SKILL.md \
         skills/java-jpa-hibernate/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/pluginagentmarketplace/custom-plugin-java/main/$p"
done
```

- https://raw.githubusercontent.com/pluginagentmarketplace/custom-plugin-java/main/skills/java-spring-boot/SKILL.md
- https://raw.githubusercontent.com/pluginagentmarketplace/custom-plugin-java/main/skills/java-testing/SKILL.md

The frontmatter is the cheap sanity check: `name` should match the directory, `sasmp_version` should read 1.3.0, and `bond_type` should say PRIMARY_BOND for the eight primary skills. After the copy route, confirm what actually landed:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -c '^java-'
head -6 ~/.hermes/profiles/corpusiq/skills/java-spring-boot/SKILL.md
```

A count of 12 is the expected result, one directory per indexed listing. If you installed the Claude Code plugin instead, restart the editor and check that the eight `java-development-assistant:` agents appear in the agent list.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| java-spring-boot | Pass | Pass | Pass |
| java-testing | Pass | Pass | Pass |
| java-maven | Pass | Pass | Pass |
| java-fundamentals | Pass | Pass | Pass |
| java-jpa-hibernate | Pass | Pass | Pass |
| java-microservices | Pass | Pass | Pass |

All six sampled skills pass all three auditors, and the sample covers the five skills above the 500-install threshold plus java-microservices. The remaining six listings are not in the sample, so the pack is not audited end to end.

What you install is close to what you review: each skill directory holds a single `SKILL.md`, and the repository root carries `agents/`, `commands/`, `hooks/` and `skills/` next to the `.claude-plugin` manifests. The `hooks/` directory is the part to read before enabling the plugin in Claude Code, because hooks run shell commands on lifecycle events rather than only when a skill is invoked. Under the copy route those hooks never load, which is one reason the manual install is the calmer option for a shared Hermes profile.

The declared tool surface is Read, Write, Bash, Glob and Grep on every sampled skill. Bash is there because a Java skill has to run builds and tests, so a skill run can execute Maven or Gradle against your working tree. Point it at a branch you can discard.

Licensing is the open item. The GitHub license field reports NOASSERTION, and the root `LICENSE` file is a custom Plugin Agent Marketplace license from the 2025 authors rather than a recognised OSI license, so confirm what redistribution your use requires before vendoring these directories into a client repository or shipping them inside another product.

## Limitations

- Snapshot data, verified 2026-10-28: 17533 combined installs across 12 indexed listings; 41 GitHub stars; license field NOASSERTION with no standard license file at the repo root; last pushed 2026-01-05. Counts drift over time.
- The root `LICENSE` file is a custom Plugin Agent Marketplace license naming Dr. Umit Kacar and Muhsin Elcicek as authors, and it is not a recognised SPDX license. Treat the skills as source-available and read the terms before redistributing them.
- The install base is one skill plus a supporting set: java-spring-boot carries 11,783 of the 17,533 combined installs, and the seven listings below the threshold sit between 263 and 499, which suggests most users install the plugin rather than cherry-pick.
- The README targets Claude Code CLI v2.0.27 or newer with an active Claude subscription and publishes no skills.sh CLI command, so the Hermes path above is a manual directory copy rather than a documented install.
- The repository README advertises version 3.0.0 with a 2025-12-30 update date while GitHub reports the last push as 2026-01-05, and it carries no topics, so version metadata has to come from `plugin.json` rather than from browsing the repo page.
- There is no index-versus-tree drift to report: all 12 indexed listings match a `SKILL.md` directory under `skills/` in the current clone. The repository is otherwise larger than the skill set, with eight agents, four slash commands and a hooks directory that have no install counts.

## Related

- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)

## Pro Tips

- State the version before anything else. `java_version` and `spring_version` are explicit parameters, and setting them to 17 or 11 up front avoids a rewrite when the agent assumes 21.
- Install the five skills that carry the install counts and add the specialist ones only when the work needs them. Seven secondary listings compete for the same trigger phrases with far less use behind them.
- Skip the `agents/` and `commands/` directories in Hermes. They are Claude Code plugin surface, and the `skills/` tree is the part that travels between runtimes.
- Run the copy route against a scratch branch first. These skills declare Bash so they can run `mvn` and `gradle`, and a first run that touches your working tree is easier to undo on a branch.
- Read the root `LICENSE` before you vendor the skills into anything you ship. A custom license is not the same permission as MIT even when the repository looks like a normal open source pack.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
