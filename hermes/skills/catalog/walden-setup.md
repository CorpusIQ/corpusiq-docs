---
title: "Walden - Spec-Driven Development with Executable Proofs"
description: "andrearaponi/walden: 8.0K combined installs across 3 listings; a deterministic Go CLI that proves code meets its spec with executable proofs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/walden-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "spec-driven development", "go", "quality gates"]
---

# Walden - Setup Guide

**Source:** [andrearaponi/walden](https://www.skills.sh/andrearaponi/walden) via skills.sh - 8.0K combined installs across 3 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 62 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-12, a Go CLI with skills under `skill/<name>/SKILL.md` and docs in `docs/`
**Category:** Spec-driven development and proof gates
**Quality Tier:** 🟢 Green - all 9 verdict cells on the 3 listed skills are Pass.

Walden proves that your code meets its spec, and shows what is no longer proven when either one changes. It is an open-source, deterministic Go CLI that takes a feature from intention to certified release through reviewed documents, executable proofs, and durable evidence. Most teams run it through a coding agent: the AI skill handles the non-deterministic half (clarifying questions, drafting requirements, design, task planning) and drives the CLI at every step, while the CLI enforces the deterministic half (phase order, freshness fingerprints, verification proofs, execution evidence, and the release gate).

This is a three-listing repository, not a large suite. The walden skill carries 7,333 of the 8,034 combined installs; walden-history (693) narrates a repository's past from git history, and walden-testability (8) reviews a design for testability before the task plan exists.

## Installation

Walden is two artifacts with one manager each: the binary comes from GitHub releases, the AI skill from the skills CLI. Neither installs the other.

```bash
# binary (darwin/linux, amd64/arm64), checksum-verified to ~/.local/bin/walden
curl -fsSL https://raw.githubusercontent.com/andrearaponi/walden/main/install.sh | sh

# AI skill, project-level for the agents the skills CLI detects
npx skills add andrearaponi/walden --skill walden
```

From source: `go install github.com/andrearaponi/walden/cmd/walden@latest`. Later, `walden update` upgrades the binary in place.

A project-level skill install commits the skill directories and skills-lock.json into the repository; `walden release check` blocks on uncommitted paths, so commit those files. The skill does not install the CLI: if it is missing or incompatible, the skill stops, detects your platform, and points you to the installer.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| walden | 7,333 | Draft and maintain feature specs in .walden/specs/ with EARS requirements, reviewed design, tasks, and executable proofs. |
| walden-history | 693 | Narrate a repository's past from git history: feature chronicles, rework reports, and retirement of superseded specs. |
| walden-testability | 8 | Review a design for testability before the task plan exists: controllability, observability, and proof cost per criterion. |

No indexed listings fall below the threshold; all 3 appear above.

## Why This Matters for Hermes Agents

Walden splits the workflow between what an agent is good at and what a deterministic tool is good at. The agent asks clarifying questions, drafts EARS requirements, designs the architecture, and plans tasks; the CLI then enforces phase order, document freshness, and proof execution so nothing ships on a checked box alone.

Every feature moves through four phases, Requirements to Design to Tasks to Execute, and each phase has an approval gate that must pass before the next begins. Human review stays with you: the skill drafts and proposes, it never approves. Completing a task records durable evidence bound to the approved spec chain and to the code it proved.

For a Hermes agent this is a spec-driven-development loop it can drive without trusting itself: the CLI's freshness fingerprints surface staleness when a document or the code changes after approval, and `walden release check` returns one deterministic verdict with exit code 0 only when there is no blocker.

## Usage

| You say | What happens |
|---|---|
| "Set up Walden in this repo" | Runs `walden repo init`: .walden/ layout, a PR template, and a pinned CI workflow. |
| "Start a feature for user auth" | Runs `walden feature init <name>`, scaffolding the three draft spec documents. |
| "Open requirements for review" | Runs `walden review open <feature> --phase requirements`, then approve seals the fingerprint. |
| "Where are we on this feature?" | Runs `walden status <feature>` for the current phase, blockers, and next action. |
| "Run the proof for task T3" | Runs `walden task complete <feature> T3`, executing the proof steps and checking the box on pass. |
| "Is this releasable?" | Runs `walden release check [<feature>] --strict` for one deterministic verdict, exit 0 only with no blocker. |

## Verification

Probe the skill and the installer before running anything:

```bash
curl -fsSL https://raw.githubusercontent.com/andrearaponi/walden/main/skill/walden/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/andrearaponi/walden/main/install.sh
```

Both return 200. The binary installer verifies the release checksum before installing to ~/.local/bin/walden; the skill installs with `npx skills add andrearaponi/walden --skill walden`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| walden | Pass | Pass | Pass |
| walden-history | Pass | Pass | Pass |
| walden-testability | Pass | Pass | Pass |

The sample covers all 3 indexed listings, so this is a full census; all 9 verdict cells pass. The repository also ships a SECURITY.md and a checksum-verified self-update path.

## Limitations

- Snapshot data, verified 2026-11-17: 8,034 combined installs across 3 indexed listings; 62 GitHub stars; Apache-2.0; last pushed 2026-11-12. Counts drift over time.
- The install count is concentrated: walden holds 7,333 of the 8,034 installs, while walden-testability sits at 8.
- The AI skill requires Walden CLI v0.10.4 or newer and does not install the CLI itself; install the binary separately.
- The POSIX installer does not run on Windows; install from source with Go or download the release asset, and `walden update` refuses on Windows.
- Every phase has an approval gate and nothing gets approved on the user's behalf, so a spec cannot be rushed through by the agent alone.

## Related

- [Spec Kit Skills - Specify, Plan, Implement](/hermes/skills/catalog/speckit-agent-skills-setup)
- [Fernando Skills - Spec-Driven Development for Agents](/hermes/skills/catalog/fernando-skills-setup)
- [Dogfood - Systematic QA Testing Setup](/hermes/skills/catalog/dogfood-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Commit the skill directories and skills-lock.json after a project-level install, or `walden release check` blocks on uncommitted paths.
- Use `walden adopt <feature> --json` to assess an existing spec read-only before executing any proof.
- Run `walden release check --strict` to bind the exact spec and evidence inputs to one commit before cutting a release.
- Keep the CLI and the skill updated separately: `walden update` for the binary, `npx skills update walden` for the guide.
- Drive the CLI through the walden skill; it keeps approvals and workflow state consistent.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
