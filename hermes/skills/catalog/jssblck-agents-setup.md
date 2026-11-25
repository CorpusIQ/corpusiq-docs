---
title: "Jess Agent Skills - GitHub Workflow Suite Setup"
description: "jssblck/agents - 17.6K combined installs: a personal GitHub-workflow agent suite for PR merging, release tagging, parallel agents and code craft."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jssblck-agents-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "github workflow", "pull requests", "code review"]
---

# Jess Agent Skills - Setup Guide

**Source:** [jssblck/agents](https://www.skills.sh/jssblck/agents) via skills.sh - 17.6K combined installs across 27 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [jssblck/agents](https://github.com/jssblck/agents) - 0 stars, GPL-3.0 license, last pushed Oct 29, 2026, main branch; one directory per skill under skills/ and machine/, plus an install script, .cursor/ environment files, and .github/ scripts.
**Category:** GitHub Workflow (Agent Skills)
**Quality Tier:** 🟡 Yellow - sampled skills.sh verdicts are mostly Pass, with a Gen Agent Trust Hub Warn on using-sops and Snyk Warns on five workflow skills; no Fails. A personal GPL-3.0 suite with 0 GitHub stars.

jssblck/agents publishes Jess's personal agent skills, one directory per skill in the Agent Skills format. Project skills live under skills/ and machine skills live under machine/. The suite covers the GitHub workflow end to end: merging PRs, tagging releases, working in PR stacks, shipping changes, resolving merge conflicts, and babysitting CI, alongside code-craft, testing-craft, using-sops, and stop-slop guidance for the work itself.

skills.sh indexes 27 listings at 17.6K combined installs, but the current tree ships 16 skill directories. Twelve indexed listings have no directory in the current tree: parallel-agents, stop-slop, here-now, codebase-diagram, computer-and-browser, mergeable-edits, improve, hotspot-audit, hatch-pet, frontend-design, doc-gardening and one-feature-one-file. parallel-agents and stop-slop still rank among the most-installed and were removed in later commits; their Use For descriptions below come from the SKILL.md each last shipped.

## Installation

Installation is a single shell script in the repository root. Run it from the repo checkout:

```bash
./install -g   # replace user-level skills with the machine skills
./install      # sync project skills into the current repo; keep the project's own
```

With -g, the script deletes the user-level skill directories and installs only the machine/ skills globally. Without -g, it installs the project skills into the current directory under .agents/skills/, linked from .claude/skills/, and records the result in skills-lock.json. Copies of skills this repo has since deleted are removed when git does not track them; project-owned skills and installs from other sources are kept. The README points browser and desktop tasks at Codex's built-in computer use and browser tools rather than bundled skills.

## What It Provides

The 13 most-installed listings appear below with their skills.sh install counts. parallel-agents and stop-slop no longer ship in the current tree; their descriptions come from the SKILL.md each last carried.

| Skill | Installs | Use For |
|---|---|---|
| using-sops | 1,670 | secrets and key setup in repos with .sops.yaml or encrypted environment files |
| code-craft | 1,670 | Jess's engineering conventions: invariants, state, effects, proofs, and error handling |
| ship-it | 1,665 | ship a completed change: commit, open a PR, push and watch CI |
| merge-open-prs | 1,662 | merge all open PRs or a specified set together |
| tag-release | 1,659 | tag or cut a patch, minor, or major release |
| gh-stack | 1,655 | checked-out PR stacks, dependent PRs, and stacked-PR planning |
| parallel-agents | 1,622 | concurrent agents sharing files, merge conflicts, AGENTS.md or CLAUDE.md upkeep |
| github-image-upload | 1,246 | attach screenshots or recordings to a GitHub PR, issue, or comment |
| testing-craft | 1,225 | write, review, or refactor tests; choose verification for a change |
| stop-slop | 1,186 | durable prose (docs, UI copy, commits, PR text) free of machine-written slop |
| project-bootstrap | 798 | repository setup, tooling infrastructure, and the full project template |
| resolve-pr-conflicts | 669 | PR merge conflicts with a base branch |
| babysit | 668 | babysit a GitHub PR or wait for its CI or review checks |

The remaining 14 indexed listings range from 3 to 39 installs.

## Why This Matters for Hermes Agents

The suite encodes a full GitHub workflow as small, single-purpose skills, so a Hermes agent told to land a batch of PRs has merge-open-prs, gh-stack, resolve-pr-conflicts and babysit to lean on instead of improvising git plumbing. Each skill states when to use it and the canonical pattern: ship-it for commit-and-open-PR, tag-release for semver tags, github-image-upload for attaching screenshots to a PR. code-craft and testing-craft carry the engineering conventions (invariants, boundary typing, errors as values, proofs) and language-specific test guidance for Go, Python, Rust and TypeScript, while using-sops handles the secrets workflow that trips agents up most often. The collection is one engineer's opinionated toolbox rather than a vendor platform, but that is also its strength: it is small enough to review in full, GPL-3.0 licensed, and easy to install per project or globally. The main caveats are provenance and drift: several top listings no longer ship in the current tree, and a 0-star, single-maintainer suite can change without notice.

## Usage

| You say | What happens |
|---|---|
| Merge all the open PRs | Uses merge-open-prs to land the full set together |
| Ship this change | Uses ship-it to commit, open a PR and push to CI |
| Cut a patch release | Uses tag-release to tag the version bump |
| This PR conflicts with main | Uses resolve-pr-conflicts to fix the merge conflicts |
| Write tests for this change | Uses testing-craft to write or refactor the verification |
| Set up sops for this repo | Uses using-sops for secrets and key setup |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/jssblck/agents/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/jssblck/agents/main/skills/code-craft/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it; the README documents the ./install script behavior, and skills this repo deleted are dropped on the next ./install when git does not track them.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| using-sops | Warn | Pass | Pass |
| code-craft | Pass | Pass | Pass |
| ship-it | Pass | Pass | Warn |
| merge-open-prs | Pass | Pass | Warn |
| tag-release | Pass | Pass | Pass |
| gh-stack | Pass | Pass | Pass |
| parallel-agents | Pass | Pass | Pass |
| github-image-upload | Pass | Pass | Warn |
| testing-craft | Pass | Pass | Pass |
| stop-slop | Pass | Pass | Pass |
| project-bootstrap | Pass | Pass | Pass |
| resolve-pr-conflicts | Pass | Pass | Warn |
| babysit | Pass | Pass | Warn |
| write-like-jess | Pass | Pass | Pass |
| database-craft | Pass | Pass | Pass |

15 of 27 indexed listings were sampled. using-sops carries a Gen Agent Trust Hub Warn, and ship-it, merge-open-prs, github-image-upload, resolve-pr-conflicts and babysit each carry a Snyk Warn; no sampled skill carries a Fail.

## Limitations

- Snapshot data, verified Nov 25, 2026: 17,568 combined installs across 27 indexed listings; 0 GitHub stars; GPL-3.0 license; last pushed Oct 29, 2026. Counts drift over time.
- The install index outruns the tree: 12 indexed listings have no directory in the current tree, including parallel-agents and stop-slop, which still rank among the top installs.
- A single-maintainer personal suite with 0 stars and no tagged releases to pin; treat it as an opinionated starting point rather than a maintained dependency.
- code-craft and testing-craft ship language-specific guidance only for Go, Python, Rust and TypeScript.
- The repository has not been pushed since Oct 29, 2026.

## Related

[Agentara Skills - AI Builder Skill Suite](/hermes/skills/catalog/agentara-skills-setup) | [Kanon Repo - PR and Code Review Skills Setup](/hermes/skills/catalog/kanon-repo-setup) | [GSD Core - Spec-Driven Development Workflow Skills](/hermes/skills/catalog/gsd-core-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install project skills per repo with ./install so each repo keeps its own set, and use ./install -g only when you want the machine skills globally.
- Read skills/code-craft/SKILL.md first; its principles and language notes underpin most of the other workflow skills.
- Have the agent run tag-release and ship-it together so a release tag always follows a clean merged PR.
- Keep the machine skills (write-like-jess, reddit, social-fetch) out of project repos unless you specifically want them there.
- Re-run ./install after pulling to drop skills the repo has since deleted.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
