---
title: "Indexion Skills - Source Code Exploration for Agents Setup"
description: "trkbt10/indexion-skills: 44.6K combined installs across 19 listings for code search, refactor detection, README and wiki upkeep via the indexion CLI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/indexion-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "code intelligence", "documentation"]
---

# Indexion Skills - Setup Guide

indexion-skills is a Claude Code plugin that teaches an agent to drive indexion, a source code exploration CLI from the same author. Where most code-reading skills tell the model to open files and reason, these ten skills tell it which command answers the question: a structural query for "where is this symbol", a similarity search for "which files look alike", a documentation graph for "what is stale", a segmentation command for chunking text into a retrieval pipeline.

The install pattern is the important part. The skills are thin Markdown wrappers around a real binary that has to be installed separately, so the agent gets deterministic output from a cached index instead of re-reading a tree on every question. That is also the main cost: the binary, not the skill files, is the thing you are trusting, and the repository README documents only the Claude Code plugin route.

**Source:** [trkbt10/indexion-skills](https://www.skills.sh/trkbt10/indexion-skills) via skills.sh - 44.6K combined installs across 19 indexed listings; first seen Apr 23, 2026
**GitHub:** [trkbt10/indexion-skills](https://github.com/trkbt10/indexion-skills) (2 stars; Apache License 2.0; branch main, pushed 2026-09-22; layout `skills/<name>/SKILL.md` for 10 skills, with `.claude-plugin/plugin.json` at version 0.19.0 registering `./skills/` and `marketplace.json` publishing the `indexion-skills` plugin)
**Category:** Developer Tooling / Code Intelligence
**Quality Tier:** 🔵 Community - 44.6K combined installs and clean verdicts on two of three sampled skills, but a 2-star repository, nine indexed listings with no directory in the current tree, and a prerequisite binary that arrives through a curl to shell installer

## Installation

```bash
# 1. Install the indexion binary every skill shells out to
curl -fsSL https://raw.githubusercontent.com/trkbt10/indexion/main/install.sh | bash
```

```bash
# 2. Add the plugin marketplace and install the skills (from the repo README)
claude marketplace add trkbt10/indexion-skills
claude plugin install indexion-skills
```

The README also notes that some skills need commands newer than an older installed binary may provide, and gives the orientation command as the version probe:

```bash
indexion agent orient --help
```

The repository is indexed on skills.sh as well, so `npx skills add trkbt10/indexion-skills` installs the same `skills/<name>/` directories through the generic skills CLI. That route is not in the repo README; the plugin marketplace route is the documented one. Either way the binary has to be on `PATH` before any skill does useful work, because each SKILL.md is instructions for invoking it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| indexion-readme | 5,100 | Build a README: initialize the template, generate per-package READMEs from doc comments, plan the writing tasks, assemble the root README and check edits with `plan drift` |
| indexion-sdd | 4,978 | Turn RFCs or specs into SDD requirements, then run spec draft, align and verify loops with codex or claude and use drift gates as CI checks |
| indexion-documentation | 4,958 | Assess documentation coverage, detect code-to-doc drift with `plan reconcile`, and map dependencies with `doc graph` |
| indexion-refactor | 4,948 | Find duplication at three levels (copy-paste blocks, cross-package shared code, unnecessary wrappers) plus concept-level single-source-of-truth violations, then fix and verify |
| indexion-wiki | 4,921 | Run the project wiki lifecycle: create pages, ingest source changes, update stale pages, lint structure, detect drift and manage search indexes |
| indexion-segment | 4,921 | Split text into contextual chunks for retrieval pipelines using window, tfidf, punctuation or hybrid strategies chosen by intent |
| indexion-kgf | 4,921 | Inspect and debug KGF language specs: tokenization output, parse trees and extracted edges, for adding language support or diagnosing a bad analysis |
| indexion-agent-orient | 4,916 | Produce a pre-edit structure brief so an agent knows likely owners, consumer surfaces and unsafe edit locations before it writes code |
| indexion-identity | 4,915 | Audit drift between file, folder and symbol names and their contents, then plan verified renames, moves, folder changes or splits |

The remaining 10 indexed listings range from 2 to 7 installs. `indexion-search` (7) does have a directory in the current tree; the nine listings at 2 installs (`indexion-plan-*`, `indexion-grep`, `indexion-explore`, `indexion-doc`) have no matching `skills/` directory, so their install counts outrun what the repo actually ships.

## Why This Matters for Hermes Agents

Code questions are the most context-expensive thing an agent does. Reading a repository to answer "where is this defined" or "which of these files are near-duplicates" costs tens of thousands of tokens and produces an answer that disappears with the session. A CLI that answers the same question from a cached index turns that into a few hundred tokens, and the skill exists to stop the model from picking the wrong mode, which is the usual failure.

The second reason is documentation drift. READMEs, wikis and docs pages maintained by agents rot in a specific way: the code moves and the prose does not. Three of these skills target that directly with a reconcile or drift step, and one runs the check as a CI gate, which is the difference between a doc review and a doc contract.

The third is edit safety. `indexion-agent-orient` exists because a zero-knowledge agent walking into an unfamiliar module guesses at ownership. A structure brief that names likely owners, consumers and unsafe edit locations is cheaper than a broken build, and `indexion-identity` covers the boring rename case that agents get wrong by editing names without touching every consumer.

The caveat is dependency weight. These are wrappers: the quality of an answer is the quality of the indexion build you have, and a stale index returns a confident wrong answer. The install also hands a remote shell script to `bash`, which is a larger trust decision than any SKILL.md in the repo, and the repository is a 2-star project carrying 44.6K installs, so the install count is not evidence of review.

## Usage

| You say | What happens |
|---|---|
| "Where is this function defined?" | Loads indexion-search, picks the structural or lexical mode instead of a blind file walk, and runs the matching indexion command |
| "Find duplicated code across packages" | Loads indexion-refactor, detects copy-paste blocks, shared code and wrapper bloat, then fixes and verifies |
| "Is the README still accurate?" | Loads indexion-readme together with the drift plan and reports which claims no longer match the code |
| "Which docs went stale this week?" | Loads indexion-documentation or indexion-wiki, reconciles source changes against pages and lists the stale set |
| "Rename this module safely" | Loads indexion-identity, audits name and content drift, then plans the rename or move with the consumer list |
| "Give me a brief before I edit this module" | Loads indexion-agent-orient and returns owners, consumer surfaces and unsafe edit locations first |
| "Turn this RFC into a checked spec" | Loads indexion-sdd and runs draft, align and verify until the implementation matches the requirements |

## Verification

Confirm the prerequisite is present and current enough for the skills before trusting any output:

```bash
indexion agent orient --help
```

Read the skills before installing them. These URLs returned 200 with `curl -s -o /dev/null -w "%{http_code}"` on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/trkbt10/indexion-skills/main/README.md
curl -sL https://raw.githubusercontent.com/trkbt10/indexion-skills/main/skills/indexion-agent-orient/SKILL.md
curl -sL https://raw.githubusercontent.com/trkbt10/indexion-skills/main/skills/indexion-readme/SKILL.md
curl -sL https://raw.githubusercontent.com/trkbt10/indexion-skills/main/skills/indexion-sdd/SKILL.md
curl -sL https://raw.githubusercontent.com/trkbt10/indexion-skills/main/skills/indexion-refactor/SKILL.md
```

The plugin manifest is the authoritative list of what a plugin install exposes, and it also returns 200:

```bash
curl -sL https://raw.githubusercontent.com/trkbt10/indexion-skills/main/.claude-plugin/plugin.json
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| indexion-readme | Pass | Pass | Pass |
| indexion-sdd | Warn | Pass | Warn |
| indexion-documentation | Pass | Pass | Pass |

No SKILL.md ships an `allowed-tools` field and the repository contains no scripts of its own: each directory is a single Markdown file plus frontmatter. What the skills do is instruct the agent to run a local binary, which means the security question moves one level down to `indexion` itself, and that binary is installed by piping a remote install script into a shell. Read the script before running it, or install the binary through a package manager you already trust.

`indexion-sdd` is the outlier on the scanners, and it is also the skill with the widest reach: it loops with codex or claude over spec files and is meant to run as a CI gate, so it will call other models and read your spec tree. Grant it a scope you would grant a CI job, not an interactive session with credentials.

Nothing in the plugin writes to the network on its own, sends telemetry, or handles a secret. The risk is ordinary and local: an index built over the wrong directory, or a command run from the wrong working directory, returns a confident answer about code that is not in scope.

## Limitations

- Requires an external binary. Every skill is a wrapper around `indexion`, so without it on `PATH` the skills produce instructions with nothing to run, and an older binary may lack commands a skill expects.
- Install script trust. The documented setup pipes a remote shell script into `bash`, which is a supply chain decision the guide cannot make for you.
- The index outruns the tree. Of 19 indexed listings, 9 have no matching `skills/` directory in the current tree and sit at 2 installs each, so the install index should not be read as a feature list.
- Low community signal for the install volume. 44.6K combined installs against 2 GitHub stars means almost no independent review, issue history or third-party writeup to check the claims against.
- Claude Code plugin route only in the README. The documented install uses `claude marketplace add` and `claude plugin install`; other runtimes need the generic skills CLI path or a manual copy of the directories.
- Snapshot data, verified Oct 26, 2026: 44,603 combined installs across 19 indexed listings; 2 GitHub stars; Apache License 2.0; last pushed 2026-09-22. Counts drift over time.

## Related

- [codebase-design - Deep Module Design Vocabulary Setup](/hermes/skills/catalog/codebase-design-setup) - the design vocabulary that makes refactor findings actionable rather than a list of duplicates.
- [shadcn Improve - Codebase Audit to Plan Setup](/hermes/skills/catalog/shadcn-improve-setup) - turns audit output into a written plan, which is what the refactor and drift skills stop short of.
- [Simplify Code - Parallel Review & Cleanup Setup](/hermes/skills/catalog/simplify-code-setup) - the reviewer-side complement to duplication detection.
- [Wiki History Ingest Setup](/hermes/skills/catalog/wiki-history-ingest-setup) - history ingestion for the same wiki pages that indexion-wiki maintains.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the binary first and probe it with `indexion agent orient --help`. Half the support questions for a wrapper suite are a missing or outdated CLI.
- Build the index once per repository and keep it out of version control. A stale index is worse than no index, because the answer still sounds confident.
- Start with `indexion-search` and `indexion-agent-orient`. They are the two that change how an agent behaves before it writes anything, and they need no document process.
- Use the drift checks on a schedule rather than on demand. Documentation rot is invisible until a gate fails on it.
- Keep the spec loop scoped. `indexion-sdd` calling a second model over a whole repository is the expensive path; point it at one spec directory at a time.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
