---
title: "Cognite Builder Skills - Industrial Flows Apps"
description: "cognitedata/builder-skills on skills.sh: 45.6K combined installs; Flows app scaffolding, Atlas MCP wiring and CDF functions for industrial data apps."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cognite-builder-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "cognite", "industrial data", "flows apps"]
---

# Cognite Builder Skills - Setup Guide

**Source:** [cognitedata/builder-skills](https://www.skills.sh/cognitedata/builder-skills) via skills.sh - 45.6K combined installs across 38 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 6 stars, Apache-2.0, last pushed 2026-11-04, 35 SKILL.md directories under skills/, one per app-building workflow
**Category:** Industrial data apps for agents: Flows app scaffolding, Atlas MCP connections, CDF functions and code-quality passes
**Quality Tier:** 🟡 Review - heavy adoption and a permissive licence, held back by a 6-star repository and Warn verdicts from Socket and Snyk on the most-installed skill.

This is the skill library Cognite ships for building apps on Flows, its framework for industrial data applications on top of CDF. The README states the position plainly: agent-agnostic AI skills that work with Claude Code, Cursor, Copilot and any agent that supports the skills format. Thirty-five of them live in the repository, each in its own `skills/<name>/SKILL.md` directory.

The set splits into three jobs. First, getting an app running: Fusion start-building ceremony, local HTTPS, Flows auth, the Atlas MCP connection, migrating a legacy Dune proof of concept onto Flows infrastructure. Second, wiring in product surface: the Atlas chat sidebar, in-app client tools, the file viewer, the 3D Reveal viewer, the graph viewer, the Aura topbar. Third, review passes with real thresholds attached, including a certification flow with a specific design score to hit.

That third group is the unusual part. Most skill libraries describe review. This one encodes the numbers: 80 percent line coverage as a hard gate, zero Must Fix items before submission, a 3.8 average on the ten design questions. An agent given those targets behaves differently from one told to "check quality".

## Installation

The README's route is the Cognite CLI, run inside the Flows app you are working on. Pull everything:

```bash
npx @cognite/cli@latest apps skills pull
```

Or pull one skill at a time:

```bash
npx @cognite/cli@latest apps skills pull --skill integrate-fusion-agent
```

The repository is also indexed on skills.sh, which gives the standard skills CLI route for agents that install from there:

```bash
npx skills add cognitedata/builder-skills
```

The README's own ordering advice matters more than the install command. If the app started from Fusion Custom apps, run **start-flows-app** first so `https://localhost` is up, and write the App-Brief after the conversation with the subject matter expert rather than dumping an empty template as the opening move.

The certification flow is four skills, run in order:

1. **flows-app-brief** writes `App-Brief.md`.
2. **flows-code-review** writes `reviews/code-review/feedback-round-<N>/` and is re-run until zero Must Fix items remain.
3. **flows-design-review** scores the ten quality questions and writes `reviews/design-review/feedback-round-<N>/`, targeting an average of 3.8 or better.
4. **flows-external-app-submit** verifies the prior three artifacts and runs `npx @cognite/cli apps submit`.

## What It Provides

Twenty of the thirty-eight indexed listings clear the 1,677-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| skill-creator | 2,528 | Author a new skill or improve an existing one, with test prompts, evals and benchmark runs |
| code-quality | 1,975 | Lint-first review of a Flows app: types, naming, dead code, duplication, component size |
| test-coverage | 1,930 | Find and fix coverage gaps against the 80 percent line coverage hard gate |
| dependencies-audit | 1,919 | Fix vulnerable, outdated, deprecated and licence-problem dependencies |
| design | 1,914 | Aura components and tokens, layouts, UX copy, async feedback and accessibility |
| reveal-3d | 1,914 | Embed the Reveal 3D viewer for CAD models, point clouds and 360 images |
| integrate-todo-list | 1,910 | Add the TodoWrite panel to an already-approved in-app chat |
| correctness-and-error-handling | 1,908 | Find and fix bugs, missing error states, unhandled rejections and edge cases |
| integrate-atlas-chat | 1,905 | Use in-app `useAtlasChat` when the EOS sidebar cannot work |
| dm-limits-and-best-practices | 1,905 | CDF data modeling concurrency, pagination, batching and the LLM-over-rows cap |
| security | 1,904 | Find and fix credential, injection, XSS and input-handling problems |
| integrate-file-viewer | 1,904 | Wire CogniteFileViewer for PDFs, images and text, including worker setup |
| setup-python-tools | 1,900 | Pyodide Python tools for an approved in-app chat |
| setup-flows-auth | 1,899 | Migrate a React app to Flows auth or add DuneAuthProvider |
| graph-viewer | 1,899 | Embed the CDF graph viewer for data model relationships and instances |
| performance | 1,896 | Re-renders, query patterns, unbounded fetches, bundles and memory leaks |
| pull-changes-resolve-conflicts | 1,894 | List conflicts, analyse ours and theirs, get approval before resolving |
| create-client-tool | 1,894 | Scaffold an AtlasTool for an approved in-app chat |
| use-topbar | 1,892 | Wire the Aura Topbar: breadcrumbs, tabs, share, notifications, theme, Atlas |
| migrate-app-to-flows | 1,677 | Move a legacy Dune proof of concept onto Flows app infrastructure |

The remaining 18 indexed listings range from 2 to 1,675 installs.

What sits behind those rows is a working method rather than a pile of prompts. `flows-review-checks` is the shared review bar that `flows-code-review` loads, and its header tells the reader not to copy the checks elsewhere, not to score from memory, and not to substitute a fix skill for the review bar. Fix skills like `code-quality`, `security`, `performance` and `test-coverage` find and repair issues; the review skills only judge. Keeping those two modes apart is the design decision that holds the certification flow together.

## Why This Matters for Hermes Agents

The interesting thing here is not the domain, it is the transferable pattern. Each of these skills carries a contract in its frontmatter and a workflow in its body: which tools it may use, where it writes its artifacts, what counts as done. `flows-code-review` writes to a numbered feedback-round folder, so a re-run never overwrites the previous review. `flows-external-app-submit` refuses to submit until the brief exists, the code review has zero Must Fix items and the design review averages at least 3.8. That is a gate an agent cannot talk its way past, and it is the shape any serious multi-step agent workflow needs.

The domain constraints are equally practical. CDF data modeling has real limits on concurrency, pagination and how many rows an LLM may be shown, and `dm-limits-and-best-practices` states them as numbers rather than advice. The 3D and file viewers need specific Vite and worker wiring that a model will otherwise improvise badly, and both skills say so explicitly: do not manually wire react-pdf, do not hand-roll the viewer.

There is also a licensing and identity angle worth noting. This is first-party vendor material, Apache-2.0, maintained by the company that owns the platform, which is a different risk profile from a community skill library that reverse-engineers a product. If you are building anything on CDF, the vocabulary alone is worth the install: Flows, Fusion, Aura, Atlas, EOS, DMS, tygen.

The caveats are the mirror image. Six GitHub stars against 45.6K installs means this library reaches people through the vendor CLI and skills.sh rather than through open-source gravity, so there is no crowd of contributors catching mistakes. The install path assumes a Flows app already exists.

## Usage

| You say | What happens |
|---|---|
| "Start a Flows app from this Fusion build prompt" | start-flows-app walks the local HTTPS ceremony, the token and hosting checks, then the App-Brief and deploy steps |
| "Connect the Industrial MCP for this project" | connect-atlas-mcp runs the injected MCP command as written, finishes browser OAuth, then explores the data models |
| "Review this app for code quality before I open a PR" | code-quality runs the linter first, then reads the code and reports findings with file paths and line numbers |
| "Run the technical review for certification" | flows-code-review loads flows-review-checks and writes a numbered feedback round with Must Fix, Should and Nice tiers |
| "Score this deck against the design questions" | flows-design-review answers the ten quality questions and reports the average against the 3.8 target |
| "Add the file viewer for PDFs and images" | integrate-file-viewer handles the install, the Vite config, the worker setup and the component usage |
| "This screen is slow with 10,000 rows" | performance measures first, then fixes render counts, fetch bounds and pagination, and measures again |

## Verification

The repository is small enough to read before installing. This path returned 200 on the `main` branch when checked on 2026-11-06:

```bash
curl -fsSL https://raw.githubusercontent.com/cognitedata/builder-skills/main/skills/code-quality/SKILL.md | head -20
```

It should open with a frontmatter block naming the skill, a `MUST be used whenever` description with a trigger list, and allowed tools, followed by a body that starts with the linter step.

After a pull, confirm the skills landed in the app you ran the command from. The CLI copies skill directories into the Flows app, so the check is a file search rather than a fixed path:

```bash
find . -maxdepth 4 -name SKILL.md | head -20
find . -maxdepth 4 -name SKILL.md | wc -l
```

The count should match the number of skills you asked for. If you pulled the whole set and the count is far below 35, the pull was interrupted or a partial directory was skipped. A single skill pull is the cleaner probe:

```bash
npx @cognite/cli@latest apps skills pull --skill flows-review-checks
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| skill-creator | Pass | Warn | Warn |
| dm-limits-and-best-practices | Pass | Pass | Pass |
| migrate-app-to-flows | Pass | Pass | Pass |
| call-cognite-function | Pass | Pass | Pass |
| connect-atlas-mcp | Pass | Pass | Pass |

Four of the five sampled skills pass all three scanners. The exception is `skill-creator`, the most-installed skill in the set at 2,528, which carries Warn from both Socket and Snyk. That is a supply-chain signal rather than a verdict of malice: a skill about creating skills tends to bundle scaffolding scripts and reference material, which is what these scanners flag. Read its body before running it.

The licence is clean. Apache-2.0 in the repository root, with a SECURITY.md beside it, which is the most permissive posture of anything in this catalog batch and the reason the tier is Yellow rather than lower. Nothing in the review or documentation skills executes remote code; the fix skills do run your package manager, which is their stated purpose.

The real exposure is the app itself. `setup-flows-auth` and the MCP connection skills touch credentials and OAuth flows, `pull-changes-resolve-conflicts` can rewrite history if you approve it carelessly, and every fix skill edits your source tree. Treat the certification skills as read-only and the fix skills as write access, because that is how the repository itself draws the line.

## Limitations

- Snapshot data, verified 2026-11-06: 45,575 combined installs across 38 indexed listings; 6 GitHub stars; Apache-2.0; last pushed 2026-11-04. Counts drift over time.
- Six GitHub stars for a 45.6K-install library. Distribution runs through the Cognite CLI and skills.sh, so there is very little community review of the skill bodies.
- The listings and the repository do not line up one to one. Thirty-eight listings are indexed against 35 SKILL.md directories, and some listed skills (`flows-app-review`, `setup-dune-auth`, `dune-app-review`) have no directory in the current tree.
- It assumes the platform. Every skill is written for a Flows app with CDF behind it, so the value collapses to near zero outside that stack.
- The design review target is a number, not a measurement. A 3.8 average on ten questions is the skill's own rubric, scored by the agent running it.
- Vendor material moves with the vendor. The certification gates here are Cognite's, and a change to their submission bar lands as a new commit with no changelog in the repository root.

## Related

- [Astronomer Agents - Airflow Data Engineering Setup](/hermes/skills/catalog/astronomer-agents-setup)
- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [Databricks Agent Skills - Data & AI Platform Skills](/hermes/skills/catalog/databricks-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install in the order the README implies, not all at once. start-flows-app, then the App-Brief, then the integration skills, then the review passes. Running the code review before the app runs produces findings about files that do not exist yet.
- Keep the fix skills and the review skills in separate turns. `flows-review-checks` explicitly forbids fixing, and an agent that starts rewriting during a review loses the audit trail the certification depends on.
- Ask for the line numbers. Every fix skill in this set reports findings with file paths and line numbers, so a summary without them is a summary of nothing.
- Use the numbered feedback rounds. Re-running `flows-code-review` writes a new round rather than overwriting, which gives you a before and after for the zero Must Fix claim.
- Steal the pattern even if you never touch CDF. A skill that declares its allowed tools, its output path and its done condition is the reusable idea in this repository.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
