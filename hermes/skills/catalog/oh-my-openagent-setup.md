---
title: "Oh My OpenAgent Skills - OmO Agent Workflow Suite"
description: "code-yeongyu/oh-my-openagent: 11.1K combined installs across 44 listings of OmO skills for GitHub triage, PR workflow, planning and QA."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/oh-my-openagent-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "github", "code review", "workflow"]
---

# Oh My OpenAgent Skills - Setup Guide

**Source:** [code-yeongyu/oh-my-openagent](https://www.skills.sh/code-yeongyu/oh-my-openagent) via skills.sh - 11.1K combined installs across 44 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 70,963 stars, NOASSERTION license (not a recognised permissive licence in metadata; the README badge points at SUL-1.0), `dev` branch, last pushed 2026-11-17, skills split across `.agents/skills/`, `.opencode/skills/` and `packages/`
**Category:** Agent workflow and developer automation skills
**Quality Tier:** 🟠 Orange - 3 of 20 sampled skills fail Gen Agent Trust Hub, 4 fail Snyk, and the license field is ambiguous.

code-yeongyu/oh-my-openagent is OmO, an agent harness that turns one command into finished work across research, code, frontends and backends. Its skills encode the developer workflow the harness itself uses: read-only GitHub triage, the full PR lifecycle, a 12-agent pre-publish release gate, adversarial planning, dead-code removal, and QA suites for opencode, the Codex Light edition and the Senpi adapter.

The repository is a very large monorepo (14,416 tree entries) and its default branch is dev rather than main. Security sampling covered 20 of the 44 indexed listings: 3 fail Gen Agent Trust Hub and 4 fail Snyk, so treat the skills as supervised-use rather than production-grade.

## Installation

The README installs the whole OmO product with a curl script, not a skills.sh command:

```bash
curl -fsSL https://get.omo.dev/install.sh | bash
omo
```

On Windows, in PowerShell: `irm https://get.omo.dev/install.ps1 | iex`. The script installs the native `omo` binary into `~/.local/bin`, checks it against the release checksums, and falls back to GitHub Releases when the mirror is unreachable. A package-manager install is `bun add -g omo-ai` (or `npm i -g omo-ai`).

The skills themselves are indexed on skills.sh; install one by name with the skills.sh CLI, confirming the name exists in the current dev tree first:

```bash
npx skills add code-yeongyu/oh-my-openagent --skill 'github-triage' -g
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| github-triage | 2,762 | Read-only GitHub triage of issues and PRs that writes evidence-backed reports and takes no actions. |
| github-issue-triage | 1,304 | Issue triage listing; no matching directory in the current dev tree. |
| work-with-pr | 786 | Full PR lifecycle in a task-owned worktree: implement, QA, review, merge, clean up. |
| pre-publish-review | 775 | Run a 12-agent release gate before publishing to npm. |
| hyperplan | 612 | Adversarial multi-agent planning with cross-critique before a plan is formalized. |
| remove-deadcode | 549 | Remove unused code with LSP-verified safety and atomic commits. |
| security-research | 508 | Team-mode security audit with vulnerability hunters and PoC engineers. |
| omomomo | 504 | Easter egg command about oh-my-opencode. |
| get-unpublished-changes | 501 | Compare HEAD with published npm versions and list unpublished changes. |
| publish | 497 | Publish to npm via the GitHub Actions workflow and verify artifacts. |
| opencode-qa | 465 | QA, smoke-test and debug opencode itself in isolation. |
| tech-debt-audit | 425 | File-cited technical debt audit across 9 dimensions with AST-grep. |
| codex-qa | 409 | QA the Codex Light edition plugin in strict isolation. |

The remaining 31 indexed listings range from 1 to 258 installs.

## Why This Matters for Hermes Agents

OmO's skills describe the exact workflow its own maintainers run, so an agent loading them gets the project's real release discipline: evidence-bound triage, worktree PRs with mandatory QA, and a release gate that refuses to publish unreviewed changes.

The most-installed skill, github-triage (2,762), is read-only by design - it writes reports to disk and never comments, merges or closes anything on GitHub. That constraint matters for Hermes agents: a triage pass that cannot mutate the remote is safe to run unattended.

work-with-pr and pre-publish-review show how far an agent can go when each step has a verification loop; hyperplan adds adversarial cross-critique so weak assumptions surface before a plan is locked. The QA skills (opencode-qa, codex-qa, senpi-qa) run in strict isolation against a mock model, never touching the user's real config.

## Usage

| You say | What happens |
|---|---|
| "Triage my open issues and PRs" | Runs github-triage, which writes evidence-backed reports and takes no GitHub actions. |
| "Create a PR for this change" | Runs work-with-pr for the full PR lifecycle in a task-owned worktree. |
| "Is this ready to publish?" | Runs pre-publish-review, a 12-agent release gate. |
| "Plan this feature rigorously" | Runs hyperplan for adversarial cross-critique planning. |
| "Remove unused code" | Runs remove-deadcode with LSP-verified safety. |
| "Audit the codebase for vulnerabilities" | Runs security-research with parallel vulnerability hunters. |
| "How much tech debt is here?" | Runs tech-debt-audit for a cited debt report. |

## Verification

Probe the skills on the `dev` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/dev/.agents/skills/github-triage/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/dev/.agents/skills/pre-publish-review/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/dev/.agents/skills/work-with-pr/SKILL.md
```

Skills live under `.agents/skills/<name>/SKILL.md`, mirrored in `.opencode/skills/`, with some under `packages/`; use `dev`, not `main`, when constructing raw URLs.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| github-triage | Pass | Pass | Warn |
| github-issue-triage | Pass | Pass | Warn |
| work-with-pr | Pass | Pass | Warn |
| pre-publish-review | Pass | Pass | Pass |
| hyperplan | Pass | Pass | Pass |
| remove-deadcode | Pass | Pass | Pass |
| security-research | Pass | Warn | Pass |
| omomomo | Pass | Pass | Pass |
| get-unpublished-changes | Pass | Pass | Pass |
| publish | Pass | Warn | Warn |
| opencode-qa | Pass | Warn | Warn |
| tech-debt-audit | Pass | Pass | Pass |
| codex-qa | Pass | Pass | Fail |
| frontend-ui-ux | Pass | Pass | Pass |
| frontend | Fail | Pass | Pass |
| github-pr-triage | Pass | Warn | Warn |
| git-master | Pass | Pass | Fail |
| senpi-qa | Pass | Pass | Pass |
| agent-browser | Fail | Pass | Fail |
| dev-browser | Fail | Warn | Fail |

The sample covers 20 of the 44 indexed listings. Three fail Gen Agent Trust Hub (frontend, agent-browser, dev-browser) and four fail Snyk (codex-qa, git-master, agent-browser, dev-browser); the remaining 24 listings are unaudited.

## Limitations

- Snapshot data, verified 2026-11-17: 11,102 combined installs across 44 indexed listings; 70,963 GitHub stars; NOASSERTION; last pushed 2026-11-17. Counts drift over time.
- The branch is `dev`, not `main`; every raw URL must use `dev`.
- GitHub reports NOASSERTION, which is not a recognised permissive licence; the README badge points at LICENSE.md (SUL-1.0). Treat it as source-available rather than a standard permissive OSI licence.
- This is a very large monorepo (14,416 tree entries); the skills sit inside a much larger codebase of Rust crates, packages and tests, and the skill-level verdicts cover the skills only.
- The 44 indexed listings are split across several directories (`.agents/skills/`, `.opencode/skills/`, `packages/...`), some duplicated across harnesses, and at least one listing (github-issue-triage) has no matching directory in the current tree.
- 3 of 20 sampled skills fail Gen Agent Trust Hub and 4 fail Snyk; the sample is partial, covering 20 of 44 listings.

## Related

- [Sentimony Skills - Dev Workflow & Review Gates Setup](/hermes/skills/catalog/sentimony-skills-setup)
- [Review Loop Skill - Continuous Code Review Discipline Setup](/hermes/skills/catalog/review-loop-skill-setup)
- [CodeRabbit Skills - AI Code Review Setup](/hermes/skills/catalog/coderabbit-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use `dev` in every raw URL and checkout; the default branch here is not `main`.
- Run github-triage unattended - it is read-only and cannot comment, merge or close anything.
- Trigger pre-publish-review explicitly before a release; a plain publish ships without the gate.
- Re-check the security pages on skills.sh before production use, since several sampled skills carry Fail verdicts.
- The QA skills run against mock models in isolation, so they are safe to use without risking your real opencode, Codex or Senpi config.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
