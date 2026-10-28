---
title: "Agent Skills - UI, Design and Shipping Suite Setup"
description: "Matthew Blode's agent-skills: 32.4K combined installs. UI design and animation audits, skill authoring, PR shipping and npm release skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mblode-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "ui design", "code review", "skill authoring"]
---

# Agent Skills - Setup Guide

**Source:** [mblode/agent-skills](https://www.skills.sh/mblode/agent-skills) via skills.sh - 32.4K combined installs across 63 indexed listings; snapshot 2026-10-27 (Oct 27 sweep)

**GitHub:** [mblode/agent-skills](https://github.com/mblode/agent-skills) - 167 stars, MIT, branch main, 28 skill directories under `skills/`, each one a `SKILL.md` with YAML frontmatter plus optional `references/`, `scripts/` and `evals/` folders

**Category:** UI design, animation, auditing and shipping workflows for coding agents

**Quality Tier:** 🟡 Beta - single-maintainer suite by Matthew Blode, 167 stars, 63 indexed listings against 28 in-tree skill directories

This is a craft suite rather than a platform integration. There is no SDK to wire and no hosted service to authenticate: each directory under `skills/` is a self-contained `SKILL.md` that tells a coding agent how to design an interface, audit typography, review a diff, open a pull request or ship an npm release. The README groups them into six families (Architecture, Design, Writing, Quality, Shipping, Authoring), and the framing throughout is adversarial toward generated output: audits end in a ship verdict, reviews separate confirmed findings from plausible ones, and several skills exist only to check work another skill produced.

The repository is built as a publishing operation, not a collection of prompts. 459 Markdown files make up the skills tree, 28 of them entry points, so most of the depth is in `references/` documents the agent opens only when a task reaches that level of detail. Seven shell scripts and six Python scripts handle the mechanical parts: frame extraction and motion tracking, PR comment fetching, CI timing analysis, AI visibility prompt panels. A validator enforces every mechanical authoring rule (frontmatter limits, body length, reference chains, table of contents, kebab-case, rule-count reconciliation, README bullets), and CI runs it with the unit tests on every push to main.

## Installation

The README documents one install command, run at user level:

```bash
npx skills add mblode/agent-skills -g --agent codex claude-code -y
```

`-g` installs for the current user rather than the current project, and the `--agent` flag targets Codex and Claude Code explicitly. The repo's `AGENTS.md` states the same command without the agent flag and notes that Cursor and OpenCode read the skills as well. A single skill installs on its own:

```bash
npx skills add mblode/agent-skills -g --skill tidy -y
```

The CLI deploys once to `~/.agents/skills/<name>/`. Any agent whose skills directory is `.agents/skills` reads that canonical path directly and needs nothing further; Claude Code reads `.claude/skills`, so it alone gets a relative symlink, `~/.claude/skills/<name> -> ../../.agents/skills/<name>`. For an agent with its own directory layout, clone and copy the one folder you want:

```bash
git clone --depth 1 https://github.com/mblode/agent-skills.git
cp -R agent-skills/skills/tidy ~/.hermes/skills/tidy
```

`AGENTS.md` calls the `cp -R` route a bypass of the symlink chain and recommends the CLI instead, which is fair for a full install and irrelevant when you are vendoring a single skill into a directory the CLI does not manage. Editing the clone does not update installed copies until you reinstall or symlink the folder directly.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ui-animation | 10,475 | Adding, reviewing and measuring UI motion: springs, gestures, scroll effects, easing matched from a screen recording, and sparse interface sound. |
| multi-tenant-architecture | 1,723 | Tenant isolation, hostname routing, custom-domain lifecycle and plan limits on Cloudflare or Vercel, with forged-header and wrong-host probes. |
| ui-design | 1,437 | Building and auditing React, Next and Tailwind UI: visual direction, design-system extraction, dark mode, responsive work, worst-case data, and a UX audit with a ship verdict. |
| typography-audit | 1,037 | Auditing font loading, type scales, measure, spacing, OpenType and rendered punctuation against 78 scoped rules. |
| agent-skills-creator | 973 | Writing and auditing skills with a validator, routing scenarios, and evidence-based keep, cut, merge or retire decisions. |
| docs-writing | 948 | Documentation prose in the house voice. The name is retired: `maintenance/retired-names.tsv` maps it to ghostwriter. |
| presentation-creator | 885 | Decks with a story spine, speaker notes and a contrast-checked QA pass, as Marp markdown, a web deck, or a handoff for editable PowerPoint. |
| product-design | 828 | Specifying interaction choices before anyone builds: action scope, reversibility, recovery and reachable states. |
| agents-md | 812 | Wiring a repo so Claude Code, Codex and Cursor read one instruction file, migrating to native AGENTS.md, then auditing instructions with grades. |
| ui-audit | 733 | Auditing UI defects. No directory in the current tree and no row in `retired-names.tsv`; ui-design Audit mode and ui-verification are the in-tree equivalents. |
| scaffold-nextjs | 728 | Scaffolding a Next.js turborepo with Blode UI, Ultracite (oxlint, shadcn), workspace hooks, and GitHub plus Vercel setup. |
| scaffold-cli | 695 | Scaffolding a TypeScript CLI and npm package: ESM, dual tsdown outputs, vitest, changesets, CI and publish templates. |
| optimise-seo | 647 | SEO fixes. Retired: `retired-names.tsv` maps it to seo, which now carries technical SEO, demand research, briefs and AI visibility measurement. |
| autoship | 633 | Running a changesets npm release: fix loop, CI watch, Version Packages merge, OIDC publish verification, and diagnosing a release that did not publish. |
| readme-creator | 604 | README writing. Retired: `retired-names.tsv` maps it to ghostwriter. |
| ax-audit | 536 | Agentic experience audit: 24 rules for tool parity, authority, approval payloads, recovery and escape hatches, with a ship verdict. |
| pr-creator | 525 | Opening or rewriting a GitHub PR with house-style titles and bodies, issue linking, repository templates and draft state. |
| pr-babysitter | 515 | Watching an open PR for CI failures, conflicts and review threads, reporting state changes, and fixing what it can. |

The remaining 42 indexed listings range from 17 to 483 installs. That tail includes the two most-used review skills, copywriting at 483 and tidy at 436, plus eli5 (317), ghostwriter (196), test-audit (175), agent-ready (173), ci-speedup (162) and app-verification (131), and it runs down to a cluster of small study and document skills such as quiz (17) and mind-map (18).

## Why This Matters for Hermes Agents

Most agent skill collections answer "how do I call this API". This one answers "is the output good enough to ship", which is the harder half of delegated work. A Hermes agent that builds a page, a deck or a PR is usually confident and sometimes wrong, and the audits here are written to break that confidence: findings carry a confirmed or plausible tier, and a verdict the caller can overrule rather than prose that reads as approval.

The routing is explicit. Each `SKILL.md` names what it is not for and hands off to the sibling that owns the job, so `ui-verification` will not restyle UI, `typography-audit` sends new visual direction to `ui-design`, and `planning` defers review to `tidy`. That matters when an agent picks a skill by name alone: a wrong pick produces a loop, a correct handoff produces one more tool call.

The suite also carries its own quality machinery. `agent-skills-creator` ships `scripts/validate.sh`, which encodes the frontmatter limits, body length, reference chains and rule-count reconciliation the repo enforces on itself, and CI runs it across every skill on each push. If you maintain a skill directory of your own, that validator is useful independently of the content.

Finally, the shipping skills assume an agent is allowed to act. `pr-babysitter` watches and repairs a PR, `autoship` runs a release through the version PR and OIDC publish, and `ci-speedup` goes as far as installing an agentic merge loop in a repository. Those are the skills to read before granting unattended repository access, because they describe exactly what the agent will do with it.

## Usage

| You say | What happens |
|---|---|
| "This panel animation feels wrong, match it to this recording" | ui-animation extracts frames with ffmpeg, tracks the motion, fits the curve, and returns spring or easing values with code. |
| "Review this landing page before we ship it" | ui-design runs its audit mode over the build, tiers the defects, and closes with a ship verdict instead of a suggestion list. |
| "The typography on our docs looks off" | typography-audit walks the 78 scoped rules on font loading, scale, measure and rendered punctuation, and reports rule IDs. |
| "Open a PR for this branch" | pr-creator reads the repository template, writes a short human description with the issue link, and opens it in draft state. |
| "Watch that PR and fix the CI" | pr-babysitter polls CI, conflicts and review threads, reports state changes, and repairs what it can without touching unrelated code. |
| "Release this package" | autoship merges the Version Packages PR, watches the publish workflow, and verifies the version is on the registry with provenance. |
| "Turn this doc into a deck" | presentation-creator builds a story spine, speaker notes and a contrast-checked slide set, defaulting to Marp. |

## Verification

After a full install the skills land as one folder per skill. The canonical path and the Claude Code symlink resolve to the same content:

```bash
ls ~/.agents/skills | sort
ls ~/.claude/skills/tidy/
```

The second listing should show `SKILL.md` plus any `references/` folder. `AGENTS.md` warns that a directory listing alone does not establish parity when other repositories contribute to the same skills directory, so compare each owned folder against its source.

Read a skill before installing it. These four paths return HTTP 200 on the current `main` branch (probed 2026-10-27):

- https://raw.githubusercontent.com/mblode/agent-skills/main/skills/ui-animation/SKILL.md
- https://raw.githubusercontent.com/mblode/agent-skills/main/skills/ui-design/SKILL.md
- https://raw.githubusercontent.com/mblode/agent-skills/main/skills/chat-history/SKILL.md
- https://raw.githubusercontent.com/mblode/agent-skills/main/skills/seo/scripts/prompt-panel.py

The repo ships its own validator, and running it against a skill you intend to install is the fastest way to see the authoring contract the suite enforces:

```bash
git clone --depth 1 https://github.com/mblode/agent-skills
cd agent-skills
skills/agent-skills-creator/scripts/validate.sh skills/ui-animation
```

There is no doctor command and no feature map. `AGENTS.md` states that the validator is the only automated proof, and that authored eval scenarios validate structurally only: behavioural evidence, with and without the skill, needs a separate isolated run.

## Security

skills.sh verdicts were not sampled for this fire, so every cell below reads Not checked. Open each skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ui-animation | Not checked | Not checked | Not checked |
| multi-tenant-architecture | Not checked | Not checked | Not checked |
| ui-design | Not checked | Not checked | Not checked |
| typography-audit | Not checked | Not checked | Not checked |
| agent-skills-creator | Not checked | Not checked | Not checked |
| docs-writing | Not checked | Not checked | Not checked |
| presentation-creator | Not checked | Not checked | Not checked |
| product-design | Not checked | Not checked | Not checked |
| agents-md | Not checked | Not checked | Not checked |
| ui-audit | Not checked | Not checked | Not checked |
| scaffold-nextjs | Not checked | Not checked | Not checked |
| scaffold-cli | Not checked | Not checked | Not checked |
| optimise-seo | Not checked | Not checked | Not checked |
| autoship | Not checked | Not checked | Not checked |
| readme-creator | Not checked | Not checked | Not checked |
| ax-audit | Not checked | Not checked | Not checked |
| pr-creator | Not checked | Not checked | Not checked |
| pr-babysitter | Not checked | Not checked | Not checked |

The risk here is in the shipped scripts, not in install hooks. There is no package manifest at the repository root, so nothing executes at install time; the surface opens when a skill calls one of its thirteen scripts. Three of those matter.

`skills/seo/scripts/prompt-panel.py` reads `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` and `GEMINI_API_KEY` from the environment and posts prompt panels directly to each provider over `urllib`, threaded, with 180 second timeouts. A panel run spends money on three accounts and sends your prompts and brand terms to three vendors. The same `SKILL.md` instructs the agent to use keys the user names or the current environment supplies, and explicitly not to search other projects' `.env` files for credentials.

`skills/chat-history/scripts/history.py` is read-only but reads the most private data on the machine: `~/.claude/projects`, the directory in `CODEX_HOME` (default `~/.codex`), and `~/.grok/sessions`, plus SQLite sources. It shells out to ripgrep and reports source evidence, which means past conversations leave the transcript they were stored in.

`skills/ci-speedup/assets/github/` contains workflows and a merge loop that an install copies into your repository. Those workflows request `pull-requests: write`, and `loop.sh` is described in its own header as a controller that classifies, bisects and reverts, with higher modes re-landing and auto-merging low-risk repairs. The sibling scripts (`fetch-comments.sh`, `ci-flow.sh`, `ci-timings.sh`, `ci-health.sh`) require an authenticated `gh` and `jq` and read PR, review-thread and workflow data under your token. Read `ci-speedup` before letting an unattended agent install it.

Local execution is the remaining piece. `ui-animation` shells out to ffmpeg and needs `opencv-python`, `numpy` and `scipy` for tracking and curve fitting, so a screen recording is processed on your machine rather than uploaded anywhere.

## Limitations

- Snapshot data, verified 2026-10-27: 32,370 combined installs across 63 indexed listings; 167 GitHub stars; MIT; branch main. Counts drift over time.
- The tree is much smaller than the index: 28 skill directories against 63 indexed listings. Of the listings that carry an install count, 32 have no directory in the current tree, and `maintenance/retired-names.tsv` explains the mapping for several of them (`docs-writing` and `readme-creator` to ghostwriter, `optimise-seo` and `seo-program` to seo, `pr-reviewer` to tidy). The Use For cells for those rows come from the README and that retired-name map, not from a current `SKILL.md`.
- ui-audit carries 733 installs but has no directory in the tree and no row in the retired-name map. Treat its described scope as covered by ui-design Audit mode and ui-verification rather than as a skill you can install today.
- The README install command names Codex and Claude Code only. Other agents install through the universal `~/.agents/skills` path or by copying a directory, which means no host-specific slash commands, hooks or plugin wiring.
- There is no doctor command, no feature map and no behavioural test harness in the repo. Authored eval scenarios validate structurally, so a prose change to a skill is unverified until someone runs its scenarios in separate isolated runs.
- Several skills assume local tooling that is not installed by the skill: `gh` and `jq` for the PR and CI skills, ffmpeg plus Python imaging packages for ui-animation, and a browser automation driver (Playwright or the Chrome DevTools tools) for ui-verification.

## Related

- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)
- [UI Skills - Design Engineer Skill Registry Setup](/hermes/skills/catalog/ibelick-ui-skills-setup)
- [Agent Skill Creator - Skill Generation and Templating Setup](/hermes/skills/catalog/agent-skill-creator-setup)
- [Ultracite - Zero-Config Lint Preset Setup](/hermes/skills/catalog/ultracite-skills-setup)

## Pro Tips

- Install the whole suite, then read the `IS NOT` section of each `SKILL.md` you plan to rely on. The handoff rules are what stop an agent from asking `ui-verification` to restyle a component.
- `AGENTS.md` carries the deploy chain detail that the README omits: content lands in `~/.agents/skills/<name>/` and Claude Code gets a relative symlink. If your agent reads a different directory, copy the folder and skip the CLI.
- Reference files load only when the `SKILL.md` lists them. Dropping a file into `references/` does not make an agent read it, which is also why trimming the reference list is how you cut context cost.
- Run `skills/agent-skills-creator/scripts/validate.sh` against your own skill directories. It encodes frontmatter limits, body length and rule-count reconciliation that are otherwise re-litigated in every review.
- Keep the retired names in mind when searching skills.sh. `optimise-seo` and `readme-creator` still carry install counts but resolve to seo and ghostwriter in the tree, so install the current name.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
