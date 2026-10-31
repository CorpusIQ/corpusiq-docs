---
title: "Chris Banes Skills - Compose and Kotlin Suite"
description: "chrisbanes/skills: 32.8K combined installs. Twenty Kotlin and Jetpack Compose skills for state, motion, performance, testing and Gradle workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/chrisbanes-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "android", "jetpack compose", "kotlin"]
---

# Chris Banes Skills - Setup Guide

**Source:** [chrisbanes/skills](https://www.skills.sh/chrisbanes/skills) via skills.sh - 32.8K combined installs across 35 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [chrisbanes/skills](https://github.com/chrisbanes/skills) - 1,133 stars, Apache-2.0, branch main, last pushed 2026-10-31; 20 skill directories under `skills/` with one `SKILL.md` each, 16 carrying a `references/` folder and 3 shipping `scripts/`

**Category:** Android and Kotlin Multiplatform engineering: Jetpack Compose, coroutines, Gradle and testing

**Quality Tier:** 🟡 Yellow - four of the five sampled skills Pass all three auditors, but Snyk marks `changelog` as Warn, and that is the skill every release workflow calls

Chris Banes maintains this repository as his own skill set for Kotlin, Android and Jetpack Compose work, and it is the most opinionated Android suite in this batch. Twenty skill directories, one `SKILL.md` each, 16 of them carrying a `references/` folder of deeper material and 3 shipping `scripts/`, which is where the Gradle runner, the GitHub Project watcher and the release checks live. The repository is also a portable Agent Plugins v1.0.0 package, so the root `plugin.json` and the immediate directories under `skills/` are the whole discovery surface for conforming clients.

The number to read carefully is 35. skills.sh indexes 35 listings for this source and the clone holds 20 directories, and the gap is a documented taxonomy change rather than neglect: the README's migration table folds 13 former entrypoints into five consolidated skills, so `compose-state-authoring`, `compose-state-hoisting` and `compose-side-effects` all route to `compose-state-and-effects` today, and three Kotlin API skills collapse into `kotlin-api-design`. The retired names still carry install counts, which is why the table below lists 20 skills while 15 listings remain in the tail.

## Installation

The README gives four routes, and the skills CLI is the first because it works for any agent that reads a `skills/` directory:

```bash
npx skills add chrisbanes/skills
```

As a Claude Code plugin marketplace, then as a Codex plugin:

```bash
/plugin marketplace add chrisbanes/skills
/plugin install chrisbanes-skills@chrisbanes-skills
```

```bash
codex plugin marketplace add chrisbanes/skills --ref main
codex plugin add chrisbanes-skills@chrisbanes-skills
```

OpenCode V2 takes a plugin entry instead, with V1 1.18.29 and newer using `plugin` rather than `plugins`:

```json
{
  "plugins": ["chrisbanes-skills@git+https://github.com/chrisbanes/skills.git"]
}
```

None of those routes knows about Hermes, so the durable install for this profile is a directory copy. The layout is flat, `skills/<name>/SKILL.md` with no language nesting, and the frontmatter `name` must match the directory name, so copy the directories rather than the files:

```bash
git clone --depth 1 https://github.com/chrisbanes/skills.git /tmp/chrisbanes-skills
cp -r /tmp/chrisbanes-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

That copies all 20. For a Compose-only install, take `compose-state-and-effects`, `compose-performance`, `compose-component-design`, `compose-animations`, `compose-focus-navigation` and `compose-ui-testing-patterns` by name. The README asks for one pairing: install `changelog` alongside `release-kotlin-library`, since the release skill uses it for notes and the plugin bundle always ships both.

Three optional providers sit outside the repository. `deliver-spec` GitHub readiness wants `triage` from `mattpocock/skills`, `implement-with-subagents` wants `tdd` at approved test seams, and `run-github-project` can use `triage`, `wayfinder` or `research`. Installing this suite does not install them, and the README states the workflows never install them implicitly.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| compose-ui-testing-patterns | 2,311 | Choosing the testing layer: plain UI tests, semantics assertions, key and focus tests, interaction-state tests with `MutableInteractionSource`, screenshot and baseline evidence, previews, fake image loading, keyboard input. |
| compose-focus-navigation | 1,985 | Keyboard, TV, D-pad and focus-first navigation: `FocusRequester`, `focusProperties`, key events, initial focus behaviour and accessibility focus order. |
| compose-animations | 1,915 | Picking between `AnimatedVisibility`, `animate*AsState`, `rememberTransition`, `AnimatedContent` and `Crossfade` for visibility, value targets, colour and size transitions, coordinated multi-property motion and content swaps. |
| shepherd | 1,255 | Polling open pull requests and merge requests, triaging review comments, repairing CI failures with the affected checks, and following a host monitor's wake events instead of polling. |
| kotlin-control-flow | 1,227 | Subject `when` and guard conditions, sealed exhaustiveness, smart casts, nullable branching, early returns, and replacing long if/else chains. |
| compose-state-and-effects | 1,212 | State ownership, `remember`, hoisting, screen state holders, `LaunchedEffect`/`DisposableEffect`/`SideEffect`, Flow collection, navigation, snackbar, analytics and focus requests. |
| compose-performance | 1,190 | Recomposition cost, compiler stability reports, skippability, unstable parameters, frame-rate State reads, cross-phase snapshot back-writing and `@ReadOnlyComposable` contracts. |
| using-chrisbanes-skills | 1,181 | The router for the suite: several overlapping Kotlin or Compose concerns, or physical Android benchmark evidence that needs a configuration decision. |
| kotlin-concurrency-and-flow | 1,178 | Coroutine scope ownership, raw `Thread` and `Executor` work, init launches, non-suspending launch APIs, `runBlocking`, cancellation, `StateFlow`/`SharedFlow`/`Channel`, `stateIn` and `SharingStarted`. |
| compose-component-design | 1,105 | Reusable component APIs: modifier parameters, root layout placement, caller-provided slots, primitive and optional content parameters, boolean shape flags. |
| kotlin-api-design | 1,033 | Function ownership (member against extension), factories, single-field domain types, value classes, data classes, expect/actual declarations, platform service boundaries. |
| kotlin-coroutines-structured-concurrency | 1,031 | Retired entrypoint, folded into `kotlin-concurrency-and-flow` by the README migration table, which now owns scope ownership and cancellation. |
| compose-recomposition-performance | 1,028 | Retired entrypoint, folded into `compose-performance`, which took over recomposition cost and stability diagnosis. |
| kotlin-flow-state-event-modeling | 1,021 | Retired entrypoint, folded into `kotlin-concurrency-and-flow`, which now covers Flow state, event sharing, replay and one-shot delivery. |
| compose-modifier-and-layout-style | 1,017 | Retired entrypoint, folded into `compose-component-design`, which now covers modifier parameters and layout placement. |
| compose-side-effects | 1,016 | Retired entrypoint, folded into `compose-state-and-effects` beside the `LaunchedEffect`, `DisposableEffect` and `SideEffect` guidance. |
| kotlin-multiplatform-expect-actual | 998 | Retired entrypoint, folded into `kotlin-api-design`, which now covers expect/actual declarations and platform boundaries. |
| compose-stability-diagnostics | 995 | Retired entrypoint, folded into `compose-performance`, which took over stability reports and skippability evidence. |
| compose-state-authoring | 994 | Retired entrypoint, folded into `compose-state-and-effects`, which now owns state ownership and hoisting. |
| compose-state-deferred-reads | 989 | Retired entrypoint, folded into `compose-performance`, which now covers deferred State reads and frame-rate reads. |

The remaining 15 indexed listings range from 5 to 970 installs.

Eight of the 20 rows above have no directory in the clone, and every one of them is a pre-cluster name that the README's migration table retires in favour of one of five live skills, so a search that lands on `compose-state-deferred-reads` should end up reading `compose-performance`. Two further listings, `compose-state-holder-ui-split` and `implement-issue`, appear neither in the tree nor in the migration table, and the clone cannot account for them.

## Why This Matters for Hermes Agents

Compose work fails quietly. The code compiles, the app runs, and the problem survives because state is read in the wrong phase, a lambda is unstable, or a modifier chain belongs to the caller rather than the component. This suite attacks those failures with one skill per failure mode and a router skill that decides which one applies, which is exactly the shape an agent needs: the router answers "which of these fifteen concerns is this question", and the leaf skill answers it in specifics.

The consolidation is the strongest signal about how the author wants the suite used. Rather than fifteen narrow entrypoints competing for attention, five consolidated skills cover state and effects, performance, component design, concurrency and API design, with a migration table that tells an agent what happened to the old names. A consolidated skill costs less context and routes more reliably, and the README backs the change with a cluster-behaviour evaluation that checks routing, required references, safeguards and finish gates at the agent-facing seam.

The workflow half is where the repository stops being a style guide. `to-plan`, `implement-with-subagents`, `deliver-spec`, `run-github-project`, `shepherd` and `gradle-run` describe an entire delivery loop: produce a plan with observable slices, choose solo or worker ownership from the task graph, deliver through a reviewed PR, keep the Project board honest, poll and repair the PR, and run every Gradle command through a wrapper that returns a bounded summary instead of a thousand lines of output. `gradle-run` is the one to notice on a Hermes host, because it exists to keep build noise out of the context window.

The suite is also cheap to carry. It is markdown plus a handful of Python and Node scripts, 99 files and 1.3 MB in total, with deep material pushed into 16 `references/` folders that are read on demand. Installing all 20 skills costs almost nothing until one of them is routed to.

## Usage

| You say | What happens |
|---|---|
| "The chat list janks while scrolling" | `compose-performance` starts from compiler stability output and skippability, then checks frame-rate State reads and cross-phase writes before proposing any code change. |
| "Write UI tests for this dialog, including the hover state" | `compose-ui-testing-patterns` chooses the layer: semantics assertions for logic, interaction-state tests through `MutableInteractionSource`, screenshot evidence where pixel drift matters. |
| "This composable takes seven boolean flags" | `compose-component-design` rewrites the API around a modifier parameter, a fixed root layout and caller-provided slots instead of flags. |
| "Cut a 2.1.0 release of the library" | `release-kotlin-library` checks the `gradle-maven-publish-plugin` prerequisite, pulls notes from `changelog`, prepares Metalava API snapshots, then runs the publication gates. |
| "Why did the build fail on CI?" | `gradle-run` recovers run identity and bounded results by workflow ID with read-only status, and diagnoses the failure fingerprint without starting another build. |
| "Keep this PR moving while I am in meetings" | `shepherd` polls the open PR, triages review comments and repairs CI failures against the affected checks. |
| "Plan these three issues and tell me who implements what" | `to-plan` produces a risk-scaled plan with observable slices, then `implement-with-subagents` picks solo or worker ownership from the task graph. |

## Verification

The raw path for the highest-install live skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} compose-ui-testing-patterns\n" \
  https://raw.githubusercontent.com/chrisbanes/skills/main/skills/compose-ui-testing-patterns/SKILL.md
```

Expect `200`. After the copy lands, confirm the count, the frontmatter and that the reference folders came along:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/compose-* \
      ~/.hermes/profiles/corpusiq/skills/kotlin-* \
      ~/.hermes/profiles/corpusiq/skills/{shepherd,to-plan,deliver-spec,gradle-run,changelog,grounded-writing,run-github-project,implement-with-subagents,release-kotlin-library,android-benchmark-comparison,using-chrisbanes-skills} | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/compose-performance/SKILL.md
find ~/.hermes/profiles/corpusiq/skills/compose-performance/references -type f | wc -l
```

The count should print 20, and the header should show `name: compose-performance` with a `description:` that opens "Use when investigating Jetpack Compose recomposition cost". A missing `references/` directory is the failure to watch for, since `compose-performance`, `compose-state-and-effects` and `run-github-project` lose most of their detail without it.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| compose-ui-testing-patterns | Pass | Pass | Pass |
| kotlin-concurrency-and-flow | Pass | Pass | Pass |
| compose-stability-diagnostics | Pass | Pass | Pass |
| compose-state-hoisting | Pass | Pass | Pass |
| changelog | Pass | Pass | Warn |

No Fail appears in the sample. One Warn does: Snyk flags `changelog`, the skill that reconciles Unreleased notes against Git history, issue and PR evidence, and the one `release-kotlin-library` calls on every release. Two of the sampled rows, `compose-stability-diagnostics` and `compose-state-hoisting`, are retired entrypoints, so their clean verdicts describe content that now lives inside `compose-performance` and `compose-state-and-effects` rather than a directory you can install.

The risk surface is instructions rather than packages. The repository installs with `cp`, has no postinstall hook, and the only executable code is in three skill folders: `gradle-run` ships a wrapper and a status script that shell out to Gradle, `run-github-project` ships a ticket ranker and a read-only Project watcher, and `release-kotlin-library` ships release checks that touch publishing credentials. An agent following those skills can run builds and, in the release case, publish artifacts, so keep publishing tokens out of the environment where the agent runs and give it its own Gradle wrapper. Snyk's Warn on `changelog` is worth reading for the same reason: the skill instructs the agent to reconcile text against history, which is a write to your repository.

## Limitations

- Snapshot data, verified 2026-10-31: 32,776 combined installs across 35 indexed listings; 1,133 GitHub stars; Apache-2.0; last pushed 2026-10-31. Counts drift over time.
- Index and tree disagree by 15 directories. The clone holds 20 skills and skills.sh lists 35, because a breaking taxonomy change retired 13 entrypoints, and two more listings (`compose-state-holder-ui-split`, `implement-issue`) appear in neither the tree nor the migration table.
- Install counts are not a ranking. Eight of the 20 table rows are retired names whose counts predate the consolidation, so `compose-state-deferred-reads` at 989 installs describes a skill you cannot install and `compose-performance` at 1,190 carries all of that guidance today.
- The skills overlap by design at the routing seam. `compose-performance`, `compose-state-and-effects` and `compose-component-design` all have something to say about stability and modifier choices, which is why `using-chrisbanes-skills` exists; skip the router and a mis-route produces confident guidance for the wrong concern.
- Android advice ages on a Kotlin and Compose release cadence. The skills track compiler stability reports, `AnimatedContent` and Metalava snapshots, all of which change between Kotlin and Compose BOM versions, so pin the clone date when you rely on a specific API recommendation.
- The workflow skills assume a GitHub Project and a Gradle build. `run-github-project`, `deliver-spec` and `gradle-run` are close to useless on a repository with neither, and the optional `tdd`, `triage` and `wayfinder` providers they expect are not installed by this suite.

## Related

- [Android Skills - Play Policy and App Quality Setup](/hermes/skills/catalog/android-skills-setup)
- [Solana Mobile Skills - Android Wallet Dev Setup](/hermes/skills/catalog/solana-mobile-skills-setup)
- [Maggy Skills - Android and Kotlin Agent Suite](/hermes/skills/catalog/maggy-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `using-chrisbanes-skills` installed and leave it in place. It is the only skill in the suite whose job is to decide which other skill applies when a question touches state, performance and component design at once.
- Trust the migration table over the install counts. Fifteen retired names still appear in the index with real numbers beside them, and thirteen of them now resolve to one of five live skills, so route by the current name and ignore the historical table in this guide when installing.
- Copy `references/` with the skill. `compose-performance`, `run-github-project` and `release-kotlin-library` keep their decision detail in reference documents, and a directory copy that grabs only `SKILL.md` leaves the agent with the summary and none of the evidence rules.
- Read `changelog` before you let an agent run a release. It writes to your repository and it is the one skill in this suite with a Snyk Warn, so review the diff it produces rather than accepting an automated changelog commit.
- Pin the clone to a date you tested. The suite follows a CalVer release train with a nightly workflow, and Compose performance guidance in particular tracks compiler behaviour that changes between releases.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
