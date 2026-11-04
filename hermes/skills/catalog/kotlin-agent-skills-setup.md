---
title: "Kotlin Agent Skills - JetBrains JVM Guidance"
description: "kotlin/kotlin-agent-skills on skills.sh: 12.2K combined installs across 10 listings; AGP 9, Java to Kotlin and Gradle migration for JVM projects."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/kotlin-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "kotlin", "jvm", "gradle"]
---

# Kotlin Agent Skills - Setup Guide

**Source:** [kotlin/kotlin-agent-skills](https://www.skills.sh/kotlin/kotlin-agent-skills) via skills.sh - 12.2K combined installs across 10 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 1,105 stars, Apache-2.0 licence, last pushed 2026-10-30, 10 SKILL.md directories under skills/
**Category:** Kotlin for agents: idiomatic coding standards, coroutines, Gradle build craft and migration guidance from JetBrains
**Quality Tier:** 🟡 Yellow: four of the five sampled skills carry clean Trust Hub and Socket verdicts, but kotlin-tooling-gradle-to-kotlin-toolchain-plugin draws a Snyk Warn

The kotlin organisation publishes ten Agent Skills for the work Kotlin teams keep repeating: moving a multiplatform module to Android Gradle Plugin 9, converting Java sources to idiomatic Kotlin, taking a KMP module off CocoaPods, and diagnosing slow Kotlin/Native links on iOS.

The suite is narrow by design. Every skill follows the naming convention `kotlin-<category>-<functional-name>`, and the README lists two categories so far: `backend` for server-side work such as Spring and JPA, and `tooling` for build and migration work. The install index covers the repo exactly, with 10 listings against 10 skill directories in the tree.

## Installation

The README documents the skills CLI first:

```bash
npx skills add Kotlin/kotlin-agent-skills
```

Claude Code takes the plugin route, which also registers the Kotlin documentation MCP server:

```sh
claude plugin marketplace add Kotlin/kotlin-agent-skills
```

```sh
claude plugin install kotlin-agent-skills@Kotlin
```

Codex registers the same marketplace from the shell, then installs from inside the client:

```shell
codex plugin marketplace add Kotlin/kotlin-agent-skills
```

Inside `codex`, invoke `/plugins`, search for `kotlin-agent-skills`, press Enter and select Install plugin.

For a single skill, the README's manual path copies the folder into the agent skills directory:

```bash
cp -r skills/kotlin-tooling-agp9-migration .claude/skills/
```

The plugin routes also enable `https://mcp.kotlinlang.org/mcp`, which lets the agent search kotlinlang.org documentation and read full pages. The skills CLI and manual copy carry skills only, so add the server yourself on those routes:

```bash
# Claude Code
claude mcp add --transport http kotlinlang https://mcp.kotlinlang.org/mcp

# Codex
codex mcp add kotlinlang --url https://mcp.kotlinlang.org/mcp
```

## What It Provides

All ten indexed listings carry install counts above 500, so the whole suite appears below.

| Skill | Installs | Use For |
|---|---|---|
| kotlin-tooling-agp9-migration | 2,266 | KMP to Android Gradle Plugin 9.0+ migration: plugin replacement with com.android.kotlin.multiplatform.library, module splitting, DSL changes and the new default project structure |
| kotlin-tooling-java-to-kotlin | 2,085 | Framework-aware Java to Kotlin conversion for Spring, Lombok, Hibernate, Jackson, Micronaut, Quarkus, Dagger/Hilt, RxJava, JUnit, Guice, Retrofit and Mockito |
| kotlin-tooling-cocoapods-spm-migration | 1,933 | KMP dependency migration from CocoaPods to Swift Package Manager: pod() becomes swiftPackage(), cocoapods.* imports become swiftPMImport.*, and the Xcode project is reconfigured |
| kotlin-backend-jpa-entity-mapping | 1,686 | Spring Data JPA and Hibernate entity design in Kotlin: identity and equality, uniqueness constraints, relationships, fetch plans, N+1 and LazyInitializationException |
| kotlin-tooling-immutable-collections-0-5-x-migration | 1,116 | kotlinx.collections.immutable 0.3.x and 0.4.x to 0.5.x: the KEEP-0459 participial renames such as add to adding and put to putting, driven by compiler deprecation warnings |
| kotlin-tooling-native-build-performance | 1,051 | Slow Kotlin/Native compilation and linking on iOS: linkDebug and linkRelease tasks, XCFramework builds, cold CI toolchain downloads and transitiveExport usage |
| kotlin-tooling-kotlin-toolchain | 549 | Building, running, testing, packaging and linting a Kotlin or Java project with the Kotlin Toolchain (formerly Amper), including greenfield scaffolds with project.yaml, module.yaml or a ./kotlin wrapper |
| kotlin-tooling-gradle-to-kotlin-toolchain-project | 521 | Whole-project Gradle to Kotlin Toolchain conversion: build.gradle files, the wrapper, libs.versions.toml, buildSrc, CI rewrites and plugins with no native Toolchain equivalent |
| kotlin-tooling-kotlin-toolchain-plugin-authoring | 516 | Authoring a Kotlin Toolchain local plugin for code generation, build-time processing, custom verification or packaging that module.yaml cannot express |
| kotlin-tooling-gradle-to-kotlin-toolchain-plugin | 513 | Porting one Gradle plugin as a Toolchain local plugin, mapping Task, Extension, project.version, dependsOn, -P properties and afterEvaluate to Toolchain equivalents |

No indexed listings fall below the threshold; all 10 appear above.

## Why This Matters for Hermes Agents

JVMs are where a lot of production code lives, and a general-purpose coding agent tends to write Kotlin that compiles but fights the ecosystem: entities as data classes, blocking calls inside coroutines, an Android plugin block that no longer exists in AGP 9.

These skills front-load the version-specific detail that models get wrong. The AGP 9 skill names the replacement plugin id, the immutable collections skill lists the rename pairs, and the Java to Kotlin skill carries per-framework rules for Spring, Lombok and Hibernate rather than generic advice.

The Toolchain pair is the most unusual part of the set. It treats JetBrains' declarative build tool as a migration target with its own concept mapping, which is the sort of guidance an agent cannot infer from training data alone.

Because everything here runs through local build tools, Hermes can act on the guidance directly: edit the build files, run the build, read the failure, apply the next step.

## Usage

| You say | What happens |
|---|---|
| "Upgrade this KMP module to AGP 9" | kotlin-tooling-agp9-migration replaces the plugin, splits modules, rewrites the DSL and reports the structure changes |
| "Turn this Java service into Kotlin" | kotlin-tooling-java-to-kotlin converts sources with framework-aware handling for Spring, Lombok and Jackson |
| "Move this shared module off CocoaPods" | kotlin-tooling-cocoapods-spm-migration swaps pod() for swiftPackage() and rewires the Xcode project |
| "Why does our iOS framework take twelve minutes to link?" | kotlin-tooling-native-build-performance profiles link tasks and proposes a local versus CI build plan |
| "These JPA entities keep throwing LazyInitializationException" | kotlin-backend-jpa-entity-mapping reviews fetch plans, equality and relationship mapping |
| "We bumped immutable collections and now see deprecation warnings" | kotlin-tooling-immutable-collections-0-5-x-migration applies the participial renames the compiler names |
| "Start a new service on the Kotlin Toolchain" | kotlin-tooling-kotlin-toolchain scaffolds project.yaml and module.yaml and wires run, test and package |

## Verification

Fetch one skill file and confirm the frontmatter matches what skills.sh indexed:

```bash
curl -fsSL https://raw.githubusercontent.com/kotlin/kotlin-agent-skills/main/skills/kotlin-tooling-agp9-migration/SKILL.md | head -20
```

Then list the installed directories to confirm the copy landed whole:

```bash
ls -1 .claude/skills | grep '^kotlin-'
```

Ten entries means every skill arrived. If a directory is present but the build steps fail, check that its `references/` and `scripts/` folders came across with it, since the manual route copies a folder rather than a file.

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| kotlin-tooling-agp9-migration | Pass | Pass | Pass |
| kotlin-tooling-cocoapods-spm-migration | Pass | Pass | Pass |
| kotlin-tooling-native-build-performance | Pass | Pass | Pass |
| kotlin-tooling-gradle-to-kotlin-toolchain-project | Pass | Pass | Pass |
| kotlin-tooling-gradle-to-kotlin-toolchain-plugin | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified November 4, 2026: 12,236 combined installs across 10 indexed listings; 1,105 GitHub stars; Apache-2.0 licence; last pushed 2026-10-30. Counts drift over time.
- Nine of the ten skills sit in the tooling category and one in backend, so server-side coverage is a single JPA skill rather than a broad backend library.
- Several skills are pinned to one migration: AGP 9.0, kotlinx.collections.immutable 0.5.x, CocoaPods to Swift Package Manager. They lose value once a codebase has moved.
- The Toolchain skills tell the agent to skip repositories that still build with Gradle or Maven, which covers most existing projects today.
- kotlin-tooling-gradle-to-kotlin-toolchain-plugin carries a Snyk Warn. It is a porting skill that edits build scripts, so review its diffs.
- The documentation MCP server ships only with the Claude Code and Codex plugins; the skills CLI and manual copy leave the agent without it.

## Related

- [Android Skills - Play Policy and App Quality Setup](/hermes/skills/catalog/android-skills-setup)
- [Awesome Android Agent Skills - Compose and Kotlin Setup](/hermes/skills/catalog/awesome-android-agent-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill first with the manual cp route, run it on a real module, then take the rest. Ten skills at once fills the context with guidance you will not use in the same week.
- Add the documentation MCP server even on the CLI route. The migration skills cite API names that change between releases, and live docs settle the version question faster than the skill text.
- Ask for the migration plan before the diff. The AGP 9 and Toolchain project skills both describe module splitting, which is a decision you want to see before files move.
- Keep the Java to Kotlin skill on a directory at a time. Framework-aware conversion on a whole service at once produces a diff nobody reviews properly.
- Pin the clone to a commit when a migration is in flight, since the tooling skills are rewritten as the target versions change.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
