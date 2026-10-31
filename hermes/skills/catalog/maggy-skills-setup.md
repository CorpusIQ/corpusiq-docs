---
title: "Maggy Skills - Android and Kotlin Agent Suite"
description: "alinaqi/maggy: 32.0K combined installs. Seventy-three skills for Android, Kotlin, web and mobile engineering plus the Maggy review and memory harness."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/maggy-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "android", "kotlin", "claude code"]
---

# Maggy Skills - Setup Guide

**Source:** [alinaqi/maggy](https://www.skills.sh/alinaqi/maggy) via skills.sh - 32.0K combined installs across 73 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [alinaqi/maggy](https://github.com/alinaqi/maggy) - 710 stars, MIT, branch main, last pushed 2026-10-13; 73 skill directories under `skills/` with one `SKILL.md` each, beside 25 slash commands, 13 hooks, 9 conditional rules, a FastAPI harness and a Cortex MCP server

**Category:** Android app development: Kotlin, Compose, architecture, testing and release workflows

**Quality Tier:** 🟢 Green - all five sampled skills Pass all three auditors, and the license is MIT, though the installer is a shell script that rewrites parts of `~/.claude`

Maggy is two products in one repository. Claude Bootstrap is the skill and hook pack: 73 skill directories under `skills/`, 25 slash commands, 13 hooks, 9 conditional rules and a set of templates that the installer copies into `~/.claude/`. Maggy is the optional harness on top, a local FastAPI server with a dashboard on port 8080, intent-driven protocols, multi-model routing across 13 tiers, the Cortex code-intelligence MCP server and a memory layer called Mnemos. The README is explicit that Bootstrap comes first and the harness is added when routing and memory are wanted.

The label on this catalog page says Android and Kotlin, and the top of the install table says something wider: `pwa-development` at 4,143 installs, `playwright-testing` at 3,313 and `android-kotlin` at 3,308 are the three leaders, followed by `code-review`, `ui-mobile` and `posthog-analytics`. What you are actually installing is a general web and mobile engineering pack with an Android core, and the honest way to read the table is as the author's daily-driver skill set rather than a focused Android toolkit.

## Installation

The README's Bootstrap route clones and runs the installer, which is the 30-second path it advertises:

```bash
git clone https://github.com/alinaqi/maggy.git
cd maggy && ./install.sh
```

The harness route installs a package and starts the dashboard:

```bash
pipx install maggy-harness   # or: pip install maggy-harness
maggy bootstrap              # installs skills, hooks, ~/bin model wrappers, plugins
maggy serve                  # auto-configures from your local repos,
                             # then opens the dashboard at localhost:8080
```

Both routes target Claude Code. `install.sh` copies into `~/.claude/skills`, `~/.claude/commands`, `~/.claude/hooks`, `~/.claude/rules` and `~/.claude/templates`, detects a Kimi or Codex CLI and installs skills there too, and wires hooks through a generated `settings.json`. Read the script before running it on a host you care about: it removes `~/.claude/skills` and `~/.claude/rules` before copying, so anything of your own in those directories is gone.

For Hermes, take the skills and leave the Claude Code scaffolding behind. The directories are self-contained and the frontmatter carries `name`, `description`, `when-to-use`, `paths` and `effort`, which is enough for routing without the hooks:

```bash
git clone --depth 1 https://github.com/alinaqi/maggy.git /tmp/maggy
cp -r /tmp/maggy/skills/. ~/.hermes/profiles/corpusiq/skills/
```

That copies all 73 directories and about 1.6 MB. A focused subset is easier to live with: `android-kotlin`, `android-java`, `code-review`, `security`, `code-deduplication`, `commit-hygiene`, `playwright-testing`, `supabase`, `supabase-nextjs` and `nodejs-backend` cover the Android and full-stack core. Skip `install.sh`, which is the README's route for Claude Code, not a Hermes installer.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| pwa-development | 4,143 | Progressive web apps: service workers, caching strategies, offline behaviour, Workbox configuration and manifests, triggered on `sw.*`, `service-worker.*` and `workbox-config.*`. |
| playwright-testing | 3,313 | End-to-end testing with Playwright: page objects, cross-browser runs, CI wiring and debugging specs under `**/e2e/**`. |
| android-kotlin | 3,308 | Android Kotlin source: coroutines, Jetpack Compose, Hilt injection and MockK tests, triggered on `.kt`, `.kts`, `android/**` and `build.gradle.kts`. |
| code-review | 1,393 | The mandatory review pass before commits and deploys, invoked directly or through `/code-review`, with a read-only tool budget. |
| ui-mobile | 1,183 | Mobile UI patterns across React Native, iOS and Android: touch targets and platform layout conventions for `**/*.tsx`, `ios/**` and `**/*.dart`. |
| posthog-analytics | 809 | PostHog instrumentation: event tracking, user identification, feature flags and project dashboards. |
| flutter | 737 | Flutter and Dart work with Riverpod state, Freezed models, go_router navigation and mocktail tests. |
| supabase-nextjs | 723 | A Next.js application on Supabase with Drizzle ORM, covering `src/app`, `src/db` and `supabase/`. |
| android-java | 670 | Android Java with MVVM, ViewBinding and Espresso tests, triggered on `.java` and `android/**`. |
| supabase | 608 | Core Supabase work: the CLI, migrations, row level security and Edge Functions. |
| code-deduplication | 585 | A capability index consulted before new utility code is written, so semantic duplicates never get created in the first place. |
| user-journeys | 584 | Journey mapping, UX validation and error recovery paths defined before a flow is built. |
| react-native | 536 | React Native patterns and platform-specific code across `ios/**`, `android/**` and `app.json`. |
| klaviyo | 517 | Klaviyo email and SMS marketing: profiles, events, flows, campaigns and segmentation. |
| aws-dynamodb | 494 | DynamoDB single-table design, GSI patterns, and SDK v3 usage in TypeScript and Python. |
| nodejs-backend | 435 | Express and Fastify backends: API routes, middleware, server setup and repository layers. |
| security | 427 | OWASP patterns, secrets handling and security testing for code that touches auth, user input or API keys. |
| aeo-optimization | 400 | AI Engine Optimization: semantic triples, page templates and content clusters built for AI citations. |
| agentic-development | 372 | Building agents with Pydantic AI in Python or the Claude SDK in Node, including tool use and multi-step workflows. |
| woocommerce | 360 | WooCommerce REST API integration: products, orders, customers, webhooks and extensions. |

The remaining 53 indexed listings range from 7 to 359 installs.

Every one of the 73 listings has a matching directory in the clone, so this is the rare pack with no index-versus-tree gap. The tail is where the harness lives: `council-review` at 49, `cross-agent-delegation` at 88, `maggy` at 99, `mnemos` at 102, `icpg` at 124 and `model-routing` at 11 are the skills that make the multi-model routing and memory story real, and they are also the least installed things in the repository.

## Why This Matters for Hermes Agents

The enforcement layer is what separates this pack from a folder of style guides. `code-review` is described as mandatory before commits and deploys, `commit-hygiene` covers the message, `tdd-workflow` is a conditional rule rather than a skill, and the harness runs lint, typecheck and tests before a push protocol completes. An agent that adopts the same order produces diffs a human can review instead of a pile of changes with a summary attached.

The Android half is solid and conventional. `android-kotlin` covers coroutines, Compose, Hilt and MockK, `android-java` covers the MVVM and ViewBinding generation that still ships in most large codebases, `ui-mobile` handles touch targets and platform conventions, and `playwright-testing` handles the web side of the same product. For a profile that touches both a Compose screen and a Next.js admin panel in the same week, that pairing is more useful than a deeper but narrower Android suite.

The memory and routing skills are the part worth stealing even if the harness is not. `code-deduplication` maintains a capability index so an agent checks what exists before writing a new helper, `session-management` handles checkpointing and resumability, and `context-shunt` hands large multi-file reads to a cheap worker model so raw bytes never enter the session, and `mnemos` and `icpg` describe fatigue-aware checkpointing and intent tracking. Those are answers to problems every long-running Hermes profile has, written from production use rather than theory.

The pack also states its own quality bar. The README advertises 1,100 or more passing tests, a skill linter that runs on every skill pull request, and a `security-audit` skill that the harness copies into every new project to run a structured adversarial audit. Treat the numbers as the author's claims and the linter as the checkable part: `PYTHONPATH=scripts python3 -m skill_lint --fail-on error skills/<name>/` runs against any skill you add.

## Usage

| You say | What happens |
|---|---|
| "Ship the marketing site as an installable PWA" | `pwa-development` produces the service worker, a Workbox caching strategy per asset class, an offline fallback and the manifest entries. |
| "Add a settings screen with Hilt injection" | `android-kotlin` supplies the Compose screen, the coroutine scope, the Hilt module and the MockK test shape. |
| "Review this branch before I push" | `code-review` runs the review pass, and `commit-hygiene` shapes the commit message that follows. |
| "Instrument the checkout flow in PostHog" | `posthog-analytics` defines the events, the identify call and the feature flag, then the dashboard view that proves it works. |
| "Where should this helper live so we do not duplicate it" | `code-deduplication` checks the capability index before a new utility is written, and points at the existing one when it finds it. |
| "Audit this app for OWASP issues" | `security` covers the preventive patterns, and `security-audit` runs the multi-phase adversarial audit that writes machine-readable findings. |
| "This app needs to run on Postgres with migrations" | `supabase` handles the CLI, migrations and row level security, and `supabase-nextjs` wires Drizzle and the app routes around it. |

## Verification

The raw path for the highest-install Android skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} android-kotlin\n" \
  https://raw.githubusercontent.com/alinaqi/maggy/main/skills/android-kotlin/SKILL.md
```

Expect `200`. After the copy, confirm the count and the frontmatter shape this repository uses, which is broader than the Agent Skills minimum:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/*/ | wc -l
head -8 ~/.hermes/profiles/corpusiq/skills/android-kotlin/SKILL.md
```

The header should show `name: android-kotlin`, a `description:` mentioning coroutines, Compose, Hilt and MockK, a `when-to-use:` line, a `paths:` list and `effort: medium`. If `when-to-use` is missing, you copied a different repository's skill. For a subset install, count only what you meant to copy, since a bare `ls` over the profile also catches every other suite in the catalog.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pwa-development | Pass | Pass | Pass |
| agentic-development | Pass | Pass | Pass |
| firebase | Pass | Pass | Pass |
| azure-cosmosdb | Pass | Pass | Pass |
| security-audit | Pass | Pass | Pass |

All five sampled skills Pass all three auditors, and the sample spans web, agent development, two managed database backends and the audit skill itself. No Fail and no Warn appears in the sample.

The auditors scan skill content, and the risk in this repository sits outside that content. `install.sh` is a 247-line shell script that deletes and recreates `~/.claude/skills` and `~/.claude/rules`, copies templates, marks hook scripts executable and writes a `settings.json` that wires 13 hooks into a Claude Code session. Some of those hooks run on session start, pre-push and post-commit, which means arbitrary shell execution on your host at moments you are not watching. The harness adds a FastAPI server on localhost:8080 and an optional `cortex-mcp` server that indexes your repositories into SQLite. On a Hermes profile none of that is needed: copy the skill directories, skip the installer, and keep hooks out unless you have read every one.

Credential handling is the other live area. The `credentials` skill exists precisely because agent workflows tend to leak keys, and `security` covers secrets management. The README states that the harness starts in local mode with no API keys, and that `GITHUB_TOKEN` or `ANTHROPIC_API_KEY` are added later only for GitHub sync or API-model features, so a local install that never sets them has no credential surface at all.

## Limitations

- Snapshot data, verified 2026-10-31: 32,037 combined installs across 73 indexed listings; 710 GitHub stars; MIT; last pushed 2026-10-13. Counts drift over time.
- The catalog label undersells the contents. The three highest-install skills are PWA development, Playwright testing and Android Kotlin, and roughly half the table has nothing to do with Android, so an Android team adopting this for Compose gets a full-stack web pack in the same copy.
- The repository's own numbers disagree. The README badge and changelog show version 6.66.0 and "73 skills", while `install.sh` prints version 6.35.0 and its closing summary says 67 skills; trust the 73 directories in the tree over either string.
- Install counts are not a ranking of value. The routing, memory and review skills that justify the harness, `model-routing` at 11 installs, `council-review` at 49 and `mnemos` at 102, sit at the bottom of the table, below generic skills like `flutter` and `klaviyo`.
- The installer is destructive and Claude-specific. `install.sh` wipes `~/.claude/skills` and `~/.claude/rules` before copying and wires hooks into a Claude Code `settings.json`, none of which a Hermes profile reads.
- Overlap is real across the pack. `code-review`, `codex-review`, `gemini-review` and `council-review` all answer "review this", `security` and `security-audit` split prevention from audit, and `supabase`, `supabase-nextjs`, `supabase-node` and `supabase-python` differ by framework rather than topic, so routing depends on the file paths in the frontmatter.
- Android guidance ages quickly. Compose, Hilt and Gradle patterns in these skills track a 2026 toolchain, and the repository has not been pushed since 2026-10-13, so check version-specific advice against your own compiler before applying it.

## Related

- [Android Skills - Play Policy and App Quality Setup](/hermes/skills/catalog/android-skills-setup)
- [Solana Mobile Skills - Android Wallet Dev Setup](/hermes/skills/catalog/solana-mobile-skills-setup)
- [Chris Banes Skills - Compose and Kotlin Suite](/hermes/skills/catalog/chrisbanes-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy the skill directories and never run `install.sh` on a Hermes host. The installer exists for Claude Code, wipes `~/.claude/skills` on the way through, and installs hooks that only that client will ever call.
- Pair this pack with Chris Banes on a Compose codebase. Banes covers state, effects and recomposition at a depth this pack does not attempt, while Maggy covers review enforcement, full-stack web and the memory layer, and the two overlap less than the labels suggest.
- Take `code-deduplication` even if you install nothing else. It is the only skill here that changes what an agent writes before it writes it, by forcing a capability-index lookup ahead of new utility code.
- Read the `when-to-use` and `paths` fields rather than the names. Most skills in this repository are `user-invocable: false` and are meant to activate on file paths, which is a different routing model from skills that expect an explicit invocation.
- Treat the harness as optional. `maggy serve`, the routing tiers and the Cortex MCP server are worth a separate evaluation on a machine you can reboot, and the skills work without any of them.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
