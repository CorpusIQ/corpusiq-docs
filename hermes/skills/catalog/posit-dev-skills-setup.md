---
title: "Posit Skills - R, Quarto and Maintainer Workflows"
description: "posit-dev/skills on skills.sh: 19.3K combined installs across 36 listings; R package, Quarto, Shiny and maintainer workflow skills from Posit."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/posit-dev-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "r packages", "quarto", "shiny"]
---

# Posit Skills - Setup Guide

**Source:** [posit-dev/skills](https://www.skills.sh/posit-dev/skills) via skills.sh - 19.3K combined installs across 36 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 556 stars, MIT (LICENSE in the repo root), last pushed 2026-11-02, 30 SKILL.md directories in category folders such as r-lib/, shiny/ and quarto/
**Category:** R and Quarto work for agents: package checks, CRAN release passes, SQL over data frames, alt text and maintainer replies
**Quality Tier:** 🟡 Review - the collection splits across 30 directories and 36 indexed listings, one sampled skill (ggsql) carries a Snyk Warn, and several skills push commits or pull requests on the agent's behalf.

Posit's collection is organised the way R work actually happens: a category per workflow rather than a skill per package. The README groups it into `posit-dev` for general developer skills, `github` for pull request work, `open-source` for releases and changelogs, `r-lib` for package development, `shiny` for apps and theming, `quarto` for documents and publishing, `ggsql` for SQL graphics, and `connect` for deployment.

The install data puts document authoring and code review at the top. `quarto-authoring` leads at 1,447 installs, `critical-code-reviewer` follows at 1,052, and `brand-yml` at 955 covers the one file that keeps Shiny apps and Quarto documents on the same visual system. Package development, PR workflows and the CRAN checks fill out the rest of the table, and the long tail is where the narrow r-lib helpers sit.

This is also a suite with a real release process behind it. The repository is Posit-maintained, last pushed on 2026-11-02, and the README documents four install routes (the skills CLI, Posit Assistant, the Claude Code marketplace, and a manual clone) because the same skills are meant to run in several harnesses.

## Installation

The README's first route works for any agent the skills CLI supports:

```bash
npx skills add posit-dev/skills --list
npx skills add posit-dev/skills --all
npx skills add posit-dev/skills --skill cli --skill lifecycle
npx skills add posit-dev/skills --agent claude-code --global
```

`--list` shows what would be installed, `--all` opens the interactive menu, `--skill` takes individual names, and `--agent` plus `--global` scopes the install to one harness for every project.

For Posit Assistant, the README installs to its own skills directory, or copies a skill directly:

```bash
npx skills add posit-dev/skills --agent posit-assistant
cp -r open-source/release-post ~/.posit/assistant/skills/
```

For Claude Code, the repository is a plugin marketplace, and each category installs as its own plugin:

```
/plugin marketplace add posit-dev/skills
/plugin install posit-dev@posit-dev-skills
/plugin install github@posit-dev-skills
/plugin install open-source@posit-dev-skills
/plugin install ggsql@posit-dev-skills
/plugin install r-lib@posit-dev-skills
/plugin install shiny@posit-dev-skills
/plugin install quarto@posit-dev-skills
/plugin install connect@posit-dev-skills
```

Each of those commands installs every skill in that category. The manual route is a clone and a copy, which is the one to use offline or when you want to edit the text.

## What It Provides

Twenty listings clear the 533-install threshold. They cover the full R maintainer loop: write the document or package, review it critically, test it, release it, write it up, and handle the pull requests in between.

| Skill | Installs | Use For |
|---|---|---|
| quarto-authoring | 1,447 | Quarto documents and migration: .qmd files, _quarto.yml, callouts, cross-references, books, sites and presentations |
| critical-code-reviewer | 1,052 | Adversarial review for correctness, security, accessibility, maintainability, tests and edge cases |
| brand-yml | 955 | Creating and applying _brand.yml across Shiny (R and Python) and Quarto, including troubleshooting existing files |
| r-package-development | 849 | R packages with devtools, testthat and roxygen2: tests, documentation and package infrastructure |
| shiny-bslib | 843 | Bootstrap 5 Shiny apps and dashboards, including migration from fluidPage and tabsetPanel patterns |
| describe-design | 830 | Researching a codebase into architectural documentation with Mermaid diagrams and stable code references |
| shiny-bslib-theming | 790 | bs_theme(), Bootswatch presets, custom colours, typography, Sass variables, dark mode and dynamic theming |
| pr-create | 764 | Creating a pull request from current changes, then monitoring CI and debugging failures until it passes |
| testing-r-packages | 749 | No directory of that name in the current tree; the index carries the listing without a matching 30-directory counterpart |
| create-release-checklist | 741 | Release checklist and GitHub issue for an R package, with automatic version calculation |
| release-post | 721 | Release blog posts for tidyverse.org or shiny.posit.co following Tidyverse and Shiny conventions |
| r-cli-app | 720 | Command-line apps in R with Rapp: argument parsing, shebang scripts and direct execution |
| pr-threads-resolve | 705 | Bulk resolving unresolved PR review threads on the current branch |
| pr-threads-address | 705 | Working every unresolved review thread: analyse the comment, change the code, test, commit, optionally reply and resolve |
| cli | 705 | The cli R package: inline markup, semantic messages, progress indicators and output theming |
| cran-extrachecks | 664 | The ad-hoc CRAN requirements devtools::check() misses: DESCRIPTION fields, URLs and documentation standards |
| alt-text | 628 | Alt text for figures in pkgdown sites and Quarto documents: fig.alt chunks, static images, multi-plot chunks |
| mirai | 578 | Async and parallel R with mirai: dependency passing, daemons, mirai_map, Shiny integration, HPC launchers |
| ggsql | 564 | ggsql queries, a grammar of graphics for SQL: writing, modifying and reading a visualisation query |
| implement | 533 | Orchestrating a plan file by delegating to subagents in parallel, with branch checks and progress tracking |

The remaining 16 indexed listings range from 77 to 532 installs. They are the task-level helpers rather than the craft skills: `working-on` (532) and `new-work` (366) keep a tracking document as the session's source of truth, `review-testing` (518) audits test code after a fix, `maintainer-decline` (447) and `lifecycle` (446) cover open-source housekeeping, `deploy-to-connect` (256) publishes to Posit Connect, and the r-lib singles (`r-testthat` 125, `r-tidyverse-style` 116, `r-cli` 107, `r-lifecycle` 105, `r-mirai` 104, `r-cran-extrachecks` 101) duplicate narrow slices of the larger skills, alongside `shiny-r-optimize` (81) and `shiny-py-optimize` (77).

## Why This Matters for Hermes Agents

R package work has a specific shape that general coding agents handle badly. `devtools::check()` is not the finish line, CRAN has ad-hoc requirements the checker does not enforce, NEWS.md has conventions, and a release is a checklist rather than a commit. `r-package-development` and `cran-extrachecks` encode that, and they encode the difference between "the tests pass" and "this would survive a CRAN review".

The Quarto skills matter for the same reason. `quarto-authoring` covers the migration path from R Markdown, bookdown, blogdown, xaringan and distill, plus the Quarto-specific features (hashpipe, cross-references, callouts, extensions) that an agent trained on R Markdown will otherwise get wrong. `alt-text` adds the accessibility step that gets skipped: figure descriptions in `fig.alt` chunks and static images, using a stated three-part formula.

The GitHub cluster is process, not knowledge. `pr-create` creates the branch and the pull request, watches CI and iterates on failures. `pr-threads-address` works unresolved review threads one at a time. `pr-threads-resolve` bulk-resolves them afterwards. For an agent expected to carry a change to merge, those three are the difference between a patch and a pull request.

`implement` and `describe-design` are the orchestration layer. One takes a plan file and delegates work to parallel subagents with branch-state checks; the other researches a codebase into architectural documentation with Mermaid diagrams and stable code references. Both are useful to an agent that has to hand work to another agent or another session.

The visual side is covered by `brand-yml` and the two bslib skills, which is more consequential than it sounds. `_brand.yml` is the single file that unifies Shiny (R and Python) and Quarto styling, so a theming change is one file rather than three, and `shiny-bslib-theming` carries the migration guidance from legacy Shiny layout patterns.

`critical-code-reviewer` earns its second place. It is scoped to adversarial review across Python, R, JavaScript, TypeScript, SQL and front-end code, which makes it the one skill in the set with no R dependency at all, and the one to install first if you only want a reviewer.

## Usage

| You say | What happens |
|---|---|
| "Convert this R Markdown report to Quarto" | quarto-authoring walks the migration, then applies callouts, cross-references and hashpipe syntax |
| "Is this package ready for CRAN?" | cran-extrachecks runs the ad-hoc checks devtools::check() misses, including DESCRIPTION fields and URLs |
| "Review this PR hard before I ask for review" | critical-code-reviewer works correctness, security, edge cases and tests |
| "Turn my plan into a pull request" | implement delegates the plan to parallel subagents, and pr-create opens the PR and drives CI to green |
| "Work through the review comments on this branch" | pr-threads-address changes, tests and commits per thread; pr-threads-resolve closes what is left |
| "Set up a release checklist for this R package" | create-release-checklist computes the version and files the checklist as a GitHub issue |
| "Theme this Shiny app to match our Quarto site" | brand-yml applies one _brand.yml to both, with shiny-bslib-theming for bs_theme() level control |

## Verification

Two probes, both 200 on the repository's `main` branch, showing the category-folder layout:

```bash
curl -fsSL https://raw.githubusercontent.com/posit-dev/skills/main/posit-dev/critical-code-reviewer/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/posit-dev/skills/main/quarto/quarto-authoring/SKILL.md | head -20
```

The first opens with a description scoped to rigorous review of code and pull requests for correctness, security, accessibility, maintainability and tests. The second scopes to Quarto, `.qmd` files, `_quarto.yml` and the migration path from other document tools. Paths are not uniform: skills sit inside category folders (`posit-dev/`, `github/`, `open-source/`, `r-lib/`, `shiny/`, `quarto/`, `connect/`, `ggsql/`), and a few live one level deeper, as in `ggsql/ggsql/SKILL.md` and `connect/deploy-to-connect/SKILL.md`.

Before installing anything, ask the CLI what it can see:

```bash
npx skills add posit-dev/skills --list
```

That list is the practical check against this guide: the index names a few skills more briefly than their directories are named (`cli` for `r-lib/r-cli`, `mirai` for `r-lib/r-mirai`, `cran-extrachecks` for `r-lib/r-cran-extrachecks`), so a name that looks missing from a `git clone` may simply be spelled differently there.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| quarto-authoring | Pass | Pass | Pass |
| create-release-checklist | Pass | Pass | Pass |
| ggsql | Pass | Pass | Warn |
| quarto-alt-text | Pass | Pass | Pass |
| shiny-py-optimize | Pass | Pass | Pass |

`ggsql` is the single Warn, and it is the skill in this set with the least R surface: it writes queries against a grammar of graphics for SQL, so the failure mode is a wrong query rather than a wrong package. Read its instructions before pointing it at a warehouse.

The more consequential security question is what the GitHub skills are allowed to do. `pr-create` pushes a branch, opens a pull request and iterates on CI; `pr-threads-address` commits code changes; `pr-threads-resolve` closes threads. Those are write operations on a shared repository, and they run under whatever token your agent already holds. Scope the token and the repository before installing that category.

`deploy-to-connect` is the other execution path: it publishes content to a Posit Connect server using rsconnect, which means credentials and a deployment target. Treat it as a deployment tool, not a documentation skill.

The skill text itself is markdown under an MIT licence with a LICENSE file in the root. The repository also ships `AGENTS.md` and a `.claude-plugin` directory at the root, which is the packaging for the marketplace route rather than instructions you need to follow.

## Limitations

- Snapshot data, verified 2026-11-06: 19,262 combined installs across 36 indexed listings; 556 GitHub stars; MIT; last pushed 2026-11-02. Counts drift over time.
- The install index is wider than the tree: 36 listings against 30 skill directories, some index names are shorter than their directory names, and `testing-r-packages` has no directory of that name in the current tree.
- Several skills act on infrastructure rather than advising. `pr-create`, `pr-threads-address`, `pr-threads-resolve` and `deploy-to-connect` push, commit, close threads or publish, so the install decision is also a permissions decision.
- The set is R-first. `critical-code-reviewer` and `describe-design` are language-agnostic, but the package, CRAN, Shiny and Quarto skills assume an R toolchain on the machine.
- Install counts in the tail are small (77 to 532), so ranking below the top five reflects adoption of narrow helpers, not quality. `r-testthat` at 125 duplicates a slice of `r-package-development` at 849.
- Coverage tracks Posit's own conventions: tidyverse style, Tidyverse and Shiny blog formats, r-lib packages. A team with different conventions gets advice it will have to overrule.

## Related

- [AI Research Skills - 100-Skill ML Research Library Setup](/hermes/skills/catalog/ai-research-skills-setup)
- [Databricks Agent Skills - Data & AI Platform Skills](/hermes/skills/catalog/databricks-agent-skills-setup)
- [CLI Printing Press - Agent-Native CLI Generator Setup](/hermes/skills/catalog/cli-printing-press-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by category, not with `--all`. The `/plugin install r-lib@posit-dev-skills` form gives you package development without pulling the Shiny, Quarto and Connect skills into the same directory.
- Start with `critical-code-reviewer`. It is the one skill here that works on any language and any repository, and it pairs with the R-specific skills rather than replacing them.
- Run `cran-extrachecks` before `devtools::check()`, not after. The point of the skill is the requirements the checker does not enforce, so running it last wastes a submission cycle.
- Use `implement` with a plan file you wrote. The skill delegates to parallel subagents and verifies branch state, which works from a written plan and badly from a one-line request.
- Keep `_brand.yml` in the repo root and point both Shiny and Quarto at it. `brand-yml` covers discovery and application, and one file is the whole reason the skill exists.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
