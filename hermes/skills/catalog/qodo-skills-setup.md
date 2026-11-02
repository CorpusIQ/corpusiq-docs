---
title: "Qodo Skills - Code Review and Standards Suite"
description: "qodo-ai/qodo-skills: 5.4K combined installs. Qodo local review, PR review resolver, codebase wisdom and review standards skills for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/qodo-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "pull requests", "standards"]
---

# Qodo Skills - Setup Guide

**Source:** [qodo-ai/qodo-skills](https://www.skills.sh/qodo-ai/qodo-skills) via skills.sh - 5.4K combined installs across 10 indexed listings; first seen 2026-11-01 (evening sweep)

**GitHub:** [qodo-ai/qodo-skills](https://github.com/qodo-ai/qodo-skills) - 59 stars, MIT, branch main, last pushed 2026-11-01; 35 `SKILL.md` directories in the clone, the 7 canonical skills under `skills/` plus four generated provider projections

**Category:** Code review and standards enforcement for agents: local review, PR review resolution and rules discovery

**Quality Tier:** 🟡 Beta - vendor maintained by Qodo, 59 stars with an MIT LICENSE in the repo root, 10 indexed listings against 35 `SKILL.md` files, and four of the five sampled listings carry a Snyk warning

Qodo Skills is the vendor's canonical, provider-neutral source for its local coding-agent skills. Qodo authors each skill once and projects it into generated packages for Claude Code, Codex, Antigravity and Kiro, so one reviewed workflow reaches every host; the generated roots are byte-equivalent projections of the canonical skill, with distribution and host provenance stamped into commands and frontmatter. Two packages exist. `qodo` installs by default and carries setup, codebase wisdom, local review and the PR review resolver. `qodo-standards` stays opt-in and carries rules discovery and standards administration, and updating the core package never installs it.

Installation and updates are split between the marketplace that owns the plugin and the CLI that owns the runtime. Every distributed skill contains its complete reviewed workflow, so an agent does not fetch task instructions from the CLI; the CLI supplies authentication, managed tools, offline tool help, runtime updates and passive update notices. In the clone, `distribution/catalog.json` describes package version 2.1.6, with `qodo` as the runtime command and a minimum CLI version of 2.0.0.

The index is much narrower than the tree. skills.sh lists 10 names, the clone holds 35 `SKILL.md` files, and the canonical set under `skills/` is 7 skills before projection into the four generated provider roots. `qodo-pr-resolver` is still indexed at 2,365 installs even though the v2.0.0 release notes remove that compatibility skill in favour of `qodo-review-resolver`, and `qodo-get-relevant-rules` and `get-qodo-rules` have no directory either; the compatibility guide describes the leftover receipt aliases as migration metadata that do not create additional skills.

## Installation

The README's first path is the marketplace. Use the official Qodo listing in Claude Code, Codex or Kiro; the marketplace owns installation and updates, and the Qodo CLI is installed separately with `qodo login` completed on first use. Antigravity bundles ship as release artifacts with their own acceptance gate in `docs/antigravity.md`.

For a local agent without an official listing, skills.sh takes the same skills, one command per package, with several agents per command:

```sh
npx skills add https://github.com/qodo-ai/qodo-skills \
  --skill qodo-setup \
  --skill qodo-codebase-wisdom \
  --skill qodo-review \
  --skill qodo-review-resolver \
  --agent cursor \
  --agent gemini-cli \
  --global \
  --yes
```

Standards is a second command rather than a flag, and the README is explicit that it is installed only when asked for:

```sh
npx skills add https://github.com/qodo-ai/qodo-skills \
  --skill qodo-get-rules \
  --skill qodo-manage-standards \
  --agent cursor \
  --global \
  --yes
```

The CLI can reach the same packages, and it prints what it would do before doing it:

```sh
qodo agents status --json
qodo agents catalog --json
qodo agents install --agent cursor,gemini-cli --json
qodo agents install --agent cursor --standards --json
```

`--standards` adds a separate standards command and never broadens the core package. Hermes is not covered by any documented path, so copy the canonical directories and keep the CLI on PATH for the review commands:

```bash
git clone https://github.com/qodo-ai/qodo-skills.git
cp -R qodo-skills/skills/qodo-* ~/.hermes/profiles/corpusiq/skills/
qodo login
```

The skills tell an agent to run the `qodo` CLI or a connected Qodo MCP server, so installed files alone prove nothing about access. That check is what `qodo-setup` exists to perform, and it is the right first request after an install.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| qodo-get-rules | 2,578 | Retrieving the coding rules that apply to the task at hand and applying them while the code is written, through semantic queries against Qodo's rules search, with reuse for the same workspace and scope. |
| qodo-pr-resolver | 2,365 | The compatibility name for pull-request review resolution; the v2.0.0 release notes remove it and point existing prompts at `qodo-review-resolver`. |
| qodo-review | 98 | Local review during coding: sends the diff, new and untracked files plus session context, with `--fast --async` checkpoints, an automatic depth for the pre-PR pass and `--deep` for a high blast radius. |
| qodo-review-resolver | 93 | Reading and resolving a PR's review: status, reviewed commit SHA and every finding as structured JSON, then fixing findings locally and recording dismiss or mark-implemented so the merge-policy block clears. |
| qodo-setup | 89 | Verifying that Qodo works in this agent: probe one read-only managed tool or set up and sign in to the CLI, then report the verified scope and what stays unverified. |
| qodo-codebase-wisdom | 86 | Answering how code works, where something is defined, who changed it and which repositories are coupled, returned as cited findings, including repos that are not checked out. |
| qodo-manage-standards | 62 | Administering Review Standards: capturing a convention as a rule, editing or retiring one, scoping it to a repository, triaging suggestions and mapping review skills, with a dry run before bulk work. |
| qodo-get-relevant-rules | 30 | A rules listing with no skill directory in the clone; the compatibility guide describes the leftover receipt aliases as migration metadata, not as skills. |
| qodo-review-notes | 16 | Keeping Development Track Notes and PR Review Notes in the platform: binding notes to a pull request, publishing source HEAD before creation and keeping the text revision-safe. It does not review code. |
| get-qodo-rules | 12 | A legacy rules listing at 12 installs with no skill directory in the clone; the current rules workflow is `qodo-get-rules`. |

All 10 indexed listings appear in the table above; the smallest is 12 installs.

## Why This Matters for Hermes Agents

Most review tooling asks an agent to scrape rendered PR comments, which is lossy, provider-specific and easy to read against the wrong commit. `qodo-review-resolver` replaces that with a structured read of the review session: status, the commit that was reviewed, and every finding with its resolution status, for any PR rather than only your own. The skill states the rule plainly, forbids the `gh` and `curl` route for review content, and keeps plain git metadata reads such as `git rev-parse HEAD` in scope for the freshness check.

The review loop has a defined end. Findings fixed in code do not clear the merge-policy block by themselves; the agent records `mark-implemented` or `dismiss` through Qodo's own tools, and Qodo reconciles the PR comments. Skip that step and the review stays red until a human clicks through, which is exactly where an autonomous agent stops when it treats "fixed" as done.

Review depth is chosen rather than guessed. `qodo-review` maps situations to flags: `--fast --async` for a light checkpoint during substantive coding, no depth flag for the ordinary pre-PR pass, and `--deep` only when the request or the blast radius justifies it. Shared authorization, a destructive migration or a contract used by several services count as justification; diff size, session length or a security-related filename do not.

The second package is the one teams care about. `qodo-get-rules` applies a workspace's own standards while code is written, and `qodo-manage-standards` is its write counterpart: capture a convention as a rule, scope it to a repository, triage the suggestion queue. Both are opt-in and both need a connected QAR managed-tools MCP server or an authenticated CLI, so a review setup can adopt standards without handing an agent write access to them.

## Usage

| You say | What happens |
|---|---|
| "Review my local diff before I open the PR" | qodo-review runs the default depth over the local changes, collects structured findings and assesses them before anything is pushed. |
| "Is the review clean on PR 214, and is it clean at head" | qodo-review-resolver reads status, reviewed commit and findings as JSON, compares the reviewed SHA with head and reports whether the review is current. |
| "Fix the open Qodo findings on this PR and record what you did" | qodo-review-resolver applies authorized fixes, then marks each finding implemented or dismissed so the merge-policy block clears. |
| "What are our review rules for this repository" | qodo-get-rules turns the task into semantic queries, retrieves the rules that apply and applies them while writing, reusing earlier results for the same workspace. |
| "Capture this convention as a rule for the payments repo" | qodo-manage-standards proposes the rule, scopes it to the repository, shows the dry run and waits for approval before writing. |
| "How does the billing service work, and what breaks if I change it" | qodo-codebase-wisdom reads code, history and cross-repository coupling through Qodo's read tools and returns cited findings, including repos not on disk. |
| "Is Qodo actually connected in this agent" | qodo-setup probes one read-only tool or checks the CLI login, then reports the verified scope and what remains unverified. |

## Verification

Probe the paths before installing, on branch `main`. The four below returned 200 when this guide was written, and the seven canonical directories resolve the same way:

```bash
for p in skills/qodo-setup/SKILL.md skills/qodo-review/SKILL.md \
         skills/qodo-review-resolver/SKILL.md skills/qodo-get-rules/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/qodo-ai/qodo-skills/main/$p"
done
```

The two to read first are the review skill and the resolver, because one decides when work gets reviewed and the other decides what happens to the findings:

- https://raw.githubusercontent.com/qodo-ai/qodo-skills/main/skills/qodo-review/SKILL.md
- https://raw.githubusercontent.com/qodo-ai/qodo-skills/main/skills/qodo-review-resolver/SKILL.md

After install, confirm the directory count, the CLI version and what each side can see:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -c '^qodo-'
qodo --version
qodo agents status --json
npx skills list --json
```

A setup run that returns one read-only result and an explicit list of unverified capabilities is the honest state. A run that reports write access before any authorized action is not, and the skill says so.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| qodo-get-rules | Pass | Pass | Pass |
| qodo-review | Pass | Pass | Warn |
| qodo-codebase-wisdom | Pass | Pass | Warn |
| qodo-get-relevant-rules | Pass | Pass | Warn |
| get-qodo-rules | Pass | Pass | Warn |

Four of the five sampled listings carry a Snyk Warn and none carries a Fail. The clean sample is `qodo-get-rules`. The four that warn are the ones that move code, history or review state across a boundary, which is a reason to read each `SKILL.md` before installing it rather than a verdict on the repository, which is not audited as a whole.

What leaves the machine is the part to get right. `qodo review` sends your diff, new and untracked files and coding-session context to Qodo. `qodo-review-resolver` and `qodo-codebase-wisdom` read review state and repository history through Qodo's managed tools instead of your forge. Assume a review service sees the change, and keep secrets out of a diff you ask an agent to review.

The write surfaces are narrow and named. `qodo-manage-standards` creates, edits and retires rules and review-skill mappings, with a dry run required before bulk operations and approval resolved for the exact target. The resolver writes to Qodo's review database, not to the git forge, and `qodo-codebase-wisdom` is documented as read-only: it drives Qodo's read tools and never posts to the forge.

Credentials stay outside the skills. `qodo-setup` is written not to handle them: on the MCP path the host owns authentication, and missing tools or `MT-AUTH-FORBIDDEN` are treated as capability or authorization failures rather than as a prompt for an API key. The repository also carries a `SECURITY.md` for reporting.

## Limitations

- Snapshot data, verified 2026-11-01: 5,429 combined installs across 10 indexed listings; 59 GitHub stars; MIT; last pushed 2026-11-01. Counts drift over time.
- The index covers 10 listings against 35 `SKILL.md` directories in the clone, which are the 7 canonical skills under `skills/` projected into the generated Claude, Codex, Antigravity and Kiro packages. Three indexed names, `qodo-pr-resolver`, `qodo-get-relevant-rules` and `get-qodo-rules`, have no directory of their own in that tree.
- Two listings describe names the repository has moved past: the v2.0.0 release notes remove `qodo-pr-resolver` in favour of `qodo-review-resolver`, and the compatibility guide calls the remaining receipt aliases migration metadata rather than skills. Install by canonical name, and expect the old names to keep carrying install counts.
- Nothing works without Qodo access. Every skill assumes either a connected QAR managed-tools MCP server or an authenticated Qodo CLI, some notes operations need CLI 2.0.0 or newer, and there is no offline mode.
- Four of the five sampled listings carry a Snyk Warn, on `qodo-review`, `qodo-codebase-wisdom`, `qodo-get-relevant-rules` and `get-qodo-rules`. The repository as a whole is not covered by that sample.
- Skill updates and CLI updates are separate consents. The README states that skill-update approval does not authorize a CLI upgrade, so an agent asked to update one will stop and ask for the other.

## Related

- [CodeRabbit Skills - AI Code Review Setup](/hermes/skills/catalog/coderabbit-skills-setup)
- [Review Loop Skill - Continuous Code Review Discipline Setup](/hermes/skills/catalog/review-loop-skill-setup)
- [Alibaba Open Code Review - AI Code Review CLI Setup](/hermes/skills/catalog/alibaba-open-code-review-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `qodo-setup` first. It separates "the plugin is installed" from "the account is reachable", and every other skill in the pack assumes the second.
- Keep `qodo-standards` opt-in. `qodo-get-rules` is useful on its own, but `qodo-manage-standards` writes rules, so installing both by default hands an agent rule-editing rights it does not need for review.
- Treat the merge-policy block as part of the loop. Fixing code without recording `mark-implemented` or `dismiss` leaves the PR red, so ask for both in the same request.
- Use the resolver instead of scraping comments. It returns the reviewed commit SHA, which is the only reliable way to tell a clean review from a stale one once head has moved.
- Check what a review uploads before wiring it into a cron. `qodo review` sends untracked files as well as tracked changes, so a workspace holding a local `.env` is the wrong place to run it unattended.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
