---
title: "Kanon Repo - PR & Code Review Skills Setup"
description: "gjkim42/kanon-repo: PR and code review skills (review-all, api-review, address-pr-review, finish-pr) - 26.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/kanon-repo-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "pull requests", "pr review"]
---

# Kanon Repo - PR & Code Review Skills Setup

**Source:** [gjkim42/kanon-repo](https://www.skills.sh/gjkim42/kanon-repo) via skills.sh - 26.3K combined installs across 10 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [gjkim42/kanon-repo](https://github.com/gjkim42/kanon-repo) - 0 stars, no LICENSE file, main branch, last pushed Nov 20, 2026; seven skill directories under `skills/<name>/SKILL.md` plus a `kanon.yaml` and `kanon.lock` at the root.
**Category:** Code Review and Pull Request Workflow
**Quality Tier:** 🟡 Yellow - 0 stars and no LICENSE file; the 10 sampled skills carry no Fail cells, with a Gen Agent Trust Hub Warn on pre-session-end and Snyk Warns on seven skills.

Kanon is an individual publisher's suite for reviewing and finishing pull requests, built around a two-agent review pass and a Kubernetes API and CRD design review for a project the skills call Kelos. The core pair is review-all, which spawns two clean-context agents that examine the same committed branch diff in parallel (one running Codex's native codex review base command, the other against Google's code review guidance) and merges both into one agreement-ranked report, and finish-pr, which loops a Kelos review request until the review approves and the branch is finalized. The README was not fetched in the sweep, so install steps and intent come from the tree and the skill descriptions rather than the repository's own documentation.

The index outruns the tree. Three of the ten listings (pre-session-end, pr-finish and agora) have no directory in the repository, and pr-finish appears to be an older name for the finish-pr loop, which is the review-and-fix skill the tree actually ships. The remaining seven skills map one to one under skills/, with review-all and api-review the two highest-count listings at just over 5,000 installs each.

## Installation

The README was not fetched, so no install line is available. Install the skills through the skills CLI:

```bash
npx skills add gjkim42/kanon-repo
```

This installs the skills only. The repository ships no plugin manifest and no MCP configuration, so there is no daemon or plugin to wire, and the skills run in whatever agent reads the SKILL.md files. Install a single skill with `--skill <name>`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| review-all | 5,033 | two-agent parallel code review merging two independent reviews into one report |
| api-review | 5,027 | Kubernetes API and CRD design review for the Kelos branch or a named PR |
| gjkim-instruction | 4,758 | maintain the root loop-engineering requirements document |
| design-cleanup | 4,652 | sweep a branch for leftovers of an abandoned design after a decision change |
| address-pr-review | 2,752 | apply the valid review findings on a PR; changes code |
| pre-session-end | 1,664 | index-only listing with no directory in the tree |
| pr-finish | 1,148 | index-only listing; the finish-pr skill covers the review-and-fix loop |
| finish-pr | 1,012 | loop review requests until the review approves and the PR is finalized |

The remaining 2 indexed listings range from 72 to 202 installs.

## Why This Matters for Hermes Agents

Review-all's design is worth copying: instead of one agent reviewing its own diff, it spawns two agents with clean context and merges their findings, which removes the self-review blind spot that makes single-agent reviews rubber-stamp the code they just wrote. The api-review skill is scoped to Kubernetes API and CRD conventions, so it catches the breaking surface changes (renamed fields, removed defaults, version skew) that generic reviewers miss. finish-pr encodes the whole review-and-fix loop as a skill, so an agent can drive a PR from review request through squash to approval without a human re-prompting each step. address-pr-review is deliberately the write side of that loop, and its description flags that it changes code rather than reviewing. For operators the caveats are the 0-star, unlicensed repository and the missing README, which means the install path and the author's own intent are not documented upstream.

## Usage

| You say | What happens |
|---|---|
| Run review-all on this branch | Spawns two clean-context agents on the committed diff and merges their findings into one agreement-ranked report |
| Review the API changes | Runs the Kubernetes API and CRD design review for the Kelos branch or the named PR |
| Address the PR review | Applies the valid review findings and changes the code |
| Finish this PR | Loops review requests and fixes until the review approves, then squashes and updates the PR |
| Clean up the old approach | Sweeps the branch for leftovers of the abandoned design and rewrites the affected code |
| Explain this PR | Walks through the motivation, a before/after sample and a flow diagram with file:line citations |

## Verification

Confirm the review-all skill landed and read its routing before running it:

```bash
curl -sL https://raw.githubusercontent.com/gjkim42/kanon-repo/main/skills/review-all/SKILL.md | head -40
```

Review the API review skill that backs api-review:

```bash
curl -sL https://raw.githubusercontent.com/gjkim42/kanon-repo/main/skills/api-review/SKILL.md | head -40
```

Inspect finish-pr's loop contract before letting it squash and push:

```bash
curl -sL https://raw.githubusercontent.com/gjkim42/kanon-repo/main/skills/finish-pr/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| review-all | Pass | Pass | Pass |
| api-review | Pass | Pass | Warn |
| gjkim-instruction | Pass | Pass | Pass |
| design-cleanup | Pass | Pass | Pass |
| address-pr-review | Pass | Pass | Warn |
| pre-session-end | Warn | Pass | Warn |
| pr-finish | Pass | Pass | Warn |
| finish-pr | Pass | Pass | Warn |
| explain-pr | Pass | Pass | Warn |
| agora | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified Nov 21, 2026: 26,320 combined installs across 10 indexed listings; 0 GitHub stars; no LICENSE file; last pushed Nov 20, 2026. Counts drift over time.
- The README was not fetched in the sweep, so no install instructions or author intent are documented here; the install path above is the skills CLI fallback, not a command from the repository.
- Three listings (pre-session-end, pr-finish and agora) have no directory in the tree, so the install index outruns the seven directories the repository actually ships.
- There is no LICENSE file at the repository root, so redistribution and modification rights are unclear despite the skills being public.
- review-all and finish-pr spawn additional agents and loop review requests, which costs extra model turns per PR.

## Related

- [Review Loop Skill - Continuous Code Review Discipline Setup](/hermes/skills/catalog/review-loop-skill-setup)
- [CodeRabbit Skills - AI Code Review Setup](/hermes/skills/catalog/coderabbit-skills-setup)
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run review-all on the committed diff only; it reviews the same base in two agents, so commit before invoking it or the second agent has nothing to diff.
- Use api-review for any change under api/, generated CRDs or examples/; it is review-only and defaults to the current branch.
- Keep address-pr-review as the only write step; review-all, api-review and explain-pr are all read-only and give no verdict, change no code and post nothing.
- Record requirements in gjkim_instruction.md first so later loop iterations are not locked into early guesses.
- Because the repository has no LICENSE file and 0 stars, read each SKILL.md and its review checklist before relying on the workflow for production PRs.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
