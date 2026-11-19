---
title: "Oldwinter Skills - Personal Agent Skills and Loop Kit Setup"
description: "oldwinter/skills: 4.3K combined installs across 96 listings; a personal agent skill set with model-invoked and user-invoked skills plus a loop kit."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/oldwinter-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "personal productivity", "devops cli", "agent loops"]
---

# Oldwinter Skills - Setup Guide

**Source:** [oldwinter/skills](https://www.skills.sh/oldwinter/skills) via skills.sh - 4.3K combined installs across 96 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 11 stars, MIT licence, `main` branch, last pushed 2026-11-17. Skills live at the repo root as `<skill>/SKILL.md` (17 of them), under `obsidian-skills/` (3), and `.claude/skills/verify`; the README is written in Chinese.
**Category:** Personal productivity, DevOps CLI, and agent loop maintenance
**Quality Tier:** 🟠 Orange - Fail verdicts on aws-cli and argocd-cli (Gen Agent Trust Hub and Snyk), with Warns on github-cli, kubectl, and agent-browser; MIT licence.

Oldwinter Skills is a personal agent skill set, mostly self-written with a few renamed forks, that keeps only the skills the author actually uses. The README, written in Chinese, states that third-party skills are installed from upstream rather than copied into this repo, and that skills should be installed one at a time rather than as a whole pack, since the repo keeps alternative entries side by side.

The install index and the repo tree are far apart. skills.sh indexes 96 listings, but the current tree holds 21 skill directories. On 2026-10-13 the repo was trimmed to keep only in-use skills, and the pre-cleanup snapshot lives in the `archive/2026-10-13` tag; the README names Lenny, Huashu, mattpocock, and OpenAI third-party copies among the removed skills. Most of the 96 indexed listings - including github-cli, aws-cli, kubectl, argocd-cli, and the Lenny-style product and career skills - correspond to skills that now exist only in that archive tag.

## Installation

Install individual root-level skills (no `--full-depth` needed):

```bash
npx --yes skills@latest add oldwinter/skills --skill done change-evidence
```

Only `obsidian-skills/` is a nested directory, so installing those skills needs `--full-depth`; add `--agent` to pick a harness and `--global` to install globally:

```bash
npx --yes skills@latest add oldwinter/skills --skill to-note vault-moc canvas-atlas --global --agent claude-code --full-depth
```

The loop kit is the one set meant to be installed together; the four skills reference each other by relative path and must land in the same skills directory:

```bash
npx --yes skills@latest add oldwinter/skills --skill loop-kit loop-triage-github loop-watch-social loop-nightly-review --agent claude-code
```

Then initialize once in the target project (idempotent, safe to re-run):

```bash
python3 .claude/skills/loop-kit/scripts/loopkit.py init
python3 .claude/skills/loop-kit/scripts/loopkit.py doctor
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| personal-productivity | 365 | Build a personal productivity system: weekly timebox plan, capture and to-do system, and review rituals. |
| github-cli | 145 | Interact with GitHub via the gh CLI: repositories, CI/CD, issues, and pull requests. |
| aws-cli | 135 | Interact with AWS services via the CLI, across EC2, S3, Lambda, RDS, and more. |
| kubectl | 101 | Interact with Kubernetes clusters via kubectl: pods, deployments, and logs. |
| positioning-and-messaging | 86 | Create product positioning and messaging frameworks with validation and iteration guidance. |
| setting-okrs-and-goals | 56 | Set measurable OKRs and goals with alignment, guardrails, and review cadence. |
| retention-and-engagement | 50 | Improve activation, retention, and engagement through hypothesis-driven growth experiments. |
| obsidian-dashboard | 50 | Generate statistics and an overview of an Obsidian vault: file counts, tags, and links. |
| finding-mentors-sponsors | 50 | Build a mentor and sponsor plan: portfolio, target list, outreach scripts, and cadence. |
| argocd-cli | 50 | Manage GitOps deployments via the ArgoCD CLI: sync, rollback, and status checks. |
| career-transitions | 49 | Plan a career transition with a progress map, target archetypes, and an option scorecard. |
| skill-creator | 48 | Create or update an agent skill that extends a coding agent with a workflow or knowledge. |
| running-effective-1-1s | 47 | Run effective 1:1s and skip-levels with cadence plans, agendas, and coaching prompts. |
| remotion-best-practices | 45 | Apply best practices for building video in React with Remotion. |
| finding-mentors-and-sponsors | 45 | Build a mentor and sponsor network with targeted outreach and follow-up cadence. |
| designing-surveys | 45 | Design and launch a product survey with a brief, questionnaire, and analysis plan. |
| agent-browser | 45 | Automate a browser from an agent: navigate pages, fill forms, and click buttons. |
| partnership-bd | 44 | Create a partnership and business development pack with thesis, scoring, and outreach. |
| organizational-design | 44 | Design an org structure and operating model with a current-state map and decisions. |
| obsidian-markdown | 44 | Write Obsidian Flavored Markdown with wikilinks, embeds, callouts, and properties. |
| aws-cost-explorer | 44 | Query AWS cost and usage details for a specific date at service level. |

The remaining 75 indexed listings range from 31 to 43 installs.

## Why This Matters for Hermes Agents

For an agent operating a personal workspace, this set is a working example of the two-invocation split that Hermes also uses: model-invoked skills that trigger when the task calls for them, and user-invoked skills that run only on an explicit `/name` or `$name`. The repo marks the difference in two places - `disable-model-invocation` in the SKILL.md frontmatter and `policy.allow_implicit_invocation` in `agents/openai.yaml` - which is a clean pattern to copy when authoring your own skills.

The loop kit is the most reusable part for builders. loop-kit is a base layer for maintenance loops, and the three loop skills (triage-github, watch-social, nightly-review) are one-shot loops driven from it, with a Reply Desk that gates outward actions on human approval. The `init` and `doctor` commands scaffold the loop config and self-check the setup before you start any timers.

The CLI skills (github-cli, aws-cli, kubectl, argocd-cli) are archived upstream copies, so if you want current versions of those, install them from their original publishers; the repo's own guidance says exactly that.

## Usage

| You say | What happens |
|---|---|
| "Install done and change-evidence from oldwinter" | The two skills are added one at a time with `npx skills add`. |
| "Set up the loop kit in this repo" | loop-kit plus its three loops install together, then `loopkit.py init` scaffolds the config. |
| "Run the loop doctor" | `loopkit.py doctor` prints PASS/WARN/FAIL/SKIP per check; a FAIL means do not start the timers yet. |
| "Give me a GitHub PR triage loop" | loop-triage-github watches your PRs and queues outward actions in the Reply Desk. |
| "Review my Obsidian vault" | obsidian-dashboard or obsidian-markdown handles vault stats and Obsidian-specific Markdown. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/oldwinter/skills/main/skills-doctor/SKILL.md
```

Then confirm the target skills directory contains the installed skill, and run the repo's own gate:

```bash
just check-all
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| personal-productivity | Pass | Pass | Pass |
| github-cli | Warn | Pass | Warn |
| aws-cli | Fail | Pass | Pass |
| kubectl | Warn | Pass | Pass |
| positioning-and-messaging | Pass | Pass | Pass |
| setting-okrs-and-goals | Pass | Pass | Pass |
| retention-and-engagement | Pass | Pass | Pass |
| obsidian-dashboard | Pass | Pass | Pass |
| finding-mentors-sponsors | Pass | Pass | Pass |
| argocd-cli | Fail | Pass | Fail |
| career-transitions | Pass | Pass | Pass |
| skill-creator | Pass | Pass | Pass |
| running-effective-1-1s | Pass | Pass | Pass |
| remotion-best-practices | Pass | Pass | Pass |
| finding-mentors-and-sponsors | Pass | Pass | Pass |
| designing-surveys | Pass | Pass | Pass |
| agent-browser | Pass | Pass | Warn |
| partnership-bd | Pass | Pass | Pass |
| organizational-design | Pass | Pass | Pass |
| obsidian-markdown | Pass | Pass | Pass |

The sample covers 20 of 96 indexed listings; aws-cli and argocd-cli carry Fails, and github-cli, kubectl, and agent-browser carry Warns.

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,313 combined installs across 96 indexed listings; 11 GitHub stars; MIT licence; last pushed 2026-11-17. Counts drift over time.
- The install index outruns the tree: 96 indexed listings against 21 skill directories. The indexed github-cli, aws-cli, kubectl, and argocd-cli are archived `devops-skills/` entries, and the Lenny-style product, career, and organizational listings were third-party copies, all removed in the 2026-10-13 cleanup and available only in the `archive/2026-10-13` tag.
- The README is written in Chinese; the install commands and loop-kit workflow above are translated from it, so confirm exact flags against the source if you read Chinese.
- `done` is user-invoked only and its `disable-model-invocation: true` must stay set; `tdd-pstack` and `teach-pstack` are renamed forks of upstream `tdd` and `teach`, so install one of each pair, not both.

## Related

- [Lenny Skills - PM Methodology from Lenny Rachitsky Setup](/hermes/skills/catalog/lenny-skills-setup)
- [Obsidian Agent Skills - Markdown, Bases and Canvas](/hermes/skills/catalog/obsidian-skills-setup)
- [Loopy - Agent Loop Library Setup](/hermes/skills/catalog/loopy-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install skills one at a time, not the whole pack; the repo keeps alternative entries side by side and a full install would pull both.
- Use `--full-depth` only for the `obsidian-skills/` subtree; root-level skills do not need it.
- Treat the loop kit as one unit: loop-kit is the base and the three loops reference it by relative path, so keep all four in one skills directory.
- For the archived CLI and Lenny-style skills, install from their upstream publishers instead; this repo deliberately does not keep third-party copies.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
