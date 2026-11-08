---
title: "Claude Cortex - Multi-Model Development Orchestration"
description: "nickcrew/claude-cortex on skills.sh: 11.8K combined installs across 150 listings; engineering skills behind a multi-model review loop."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-cortex-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "engineering workflow", "multi-model"]
---

# Claude Cortex - Setup Guide

**Source:** [nickcrew/claude-cortex](https://www.skills.sh/nickcrew/claude-cortex) via skills.sh - 11.8K combined installs across 150 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 66 stars, MIT, last pushed 2026-06-28, 156 `SKILL.md` files in the tree, of which 140 sit in their own directory under `skills/` with the rest bundled inside multi-skill folders, plus a Python CLI and TUI in `claude_ctx_py/`
**Category:** Engineering workflow for agents: implementation loops, independent review, test and lint gates, security review, documentation maintenance and design craft
**Quality Tier:** 🟡 Yellow - Socket returns Warn on `owasp-top-10` and several skills ship executable Python, so the set is reviewable rather than purely instructional despite the clean MIT licence.

Cortex is a development orchestration framework that treats the skill library as one half of a quality system. The other half is a CLI. The README states the governing rule in one line: the agent that writes the code never reviews it. A change implemented by Codex is reviewed by Claude first, then a different model family, and same-model review is the last resort rather than the default.

The library is broad for a 66 star repository. 150 listings cover engineering practice, security, documentation, product work, design and writing, and the README's own highlight reel picks four that carry the workflow: `agent-loops` for the implementation sequence, `test-review` for coverage auditing, `doc-claim-validator` for checking documentation claims against the code, and `doc-maintenance` for the documentation lifecycle.

## Installation

The README documents two package routes. Homebrew on macOS:

```bash
brew tap NickCrew/cortex
brew install cortex
```

`post_install` symlinks the bundled agents, skills, rules and schemas into `~/.claude` automatically, and `CORTEX_SKIP_LINK=1` opts out of that. The Python route works anywhere:

```bash
pipx install claude-cortex
```

The package also ships a smaller surface, `cortex-minimal`, aimed at agent runtime environments:

```bash
uvx --from claude-cortex cortex-minimal --help
```

It exposes only `git`, `tmux`, `statusline`, `hooks` and `completions`, sharing the same implementation as the full CLI. The README warns that installing through both Homebrew and pip leaves the winner to `$PATH` order, so pick one.

Once the CLI is present, linking and inspection:

```bash
cortex install link
cortex status
cortex skills list
cortex tui
```

The README does not include a skills CLI line, because the package installer is the documented path. If you only want the skill text without the framework, `npx skills add nickcrew/claude-cortex` follows the usual convention, but confirm the skill name in the current tree first, since directory names and skill names diverge here in several places.

For Hermes, the skill directories are self contained. `cortex install link` puts them under `~/.claude`, which a Hermes profile does not read, so copy the ones you want from `skills/<name>/` into the profile skills directory instead. Skills that ship `scripts/` need those files copied with them.

## What It Provides

Sixteen listings clear the reporting threshold, and the spread tells you where the attention went:

| Skill | Installs | Use For |
|---|---|---|
| react-performance-optimization | 1,908 | React performance work: memoisation, code splitting and efficient rendering for slow apps and large datasets |
| owasp-top-10 | 760 | OWASP Top 10 detection and remediation patterns for security audits and code review |
| ui-design-aesthetics | 359 | Generating non-generic UI design with progressive disclosure and distinctive aesthetics |
| threat-modeling-techniques | 357 | Threat modelling with STRIDE, attack trees and risk assessment for systems being designed |
| token-efficiency | 238 | Compressed agent communication using symbols and abbreviations when context is tight |
| repo-cleanup | 181 | Safe cleanup of dead code, build artefacts, unused dependencies, stale docs and tests, with validation steps |
| helm-chart-patterns | 179 | Reusable Helm charts and multi-environment Kubernetes deployments |
| typescript-advanced-patterns | 174 | Type-safe APIs and domain models using advanced TypeScript type features |
| code-explanation | 173 | Explaining code, concepts or system behaviour to a named audience level, with depth control |
| security-testing-patterns | 123 | SAST, DAST, penetration testing and vulnerability assessment in a pipeline |
| ux-review | 119 | Multi-perspective UX review combining usability heuristics, WCAG checks and interaction analysis |
| secure-coding-practices | 100 | Authentication, input handling, sensitive data and secure code review |
| event-driven-architecture | 88 | Event sourcing, CQRS and message-driven design for distributed systems |
| doc-maintenance | 87 | Documentation audits after feature work, refactors or dependency upgrades, with a prescribed `docs/` structure |
| dashboard-designer | 84 | Dashboard design: choosing KPIs, structuring layout, visual hierarchy and BI tool choice |
| terraform-best-practices | 83 | Terraform modules, state management and infrastructure automation at scale |

The remaining 134 indexed listings range from 31 to 74 installs.

The tail is not filler. It holds the workflow skills the README leads with, including `agent-loops` at 51, `test-review` at 67, `doc-claim-validator` at 42 and `skill-installer` at 63. If you install by install count, you get a React optimisation skill and a security checklist, not the review loop the framework is built around.

## Why This Matters for Hermes Agents

The no-self-review rule is the transferable idea. An agent asked to check its own work will usually confirm it, because the same context that produced the change also judges it. Cortex hard-codes the opposite: route the review to a different model, and only fall back to same-model review when the others are unavailable. A Hermes agent with subagent dispatch can implement the same rule with a reviewer subagent on a fresh context and a different prompt.

The second idea is the loop with a stopping condition. The README describes three sequential gates, a code change loop, a test writing loop and a lint gate, each with a maximum cycle count and circuit breakers, and P0 and P1 findings must be resolved before the loop exits. That is what stops the classic remediation spiral where an agent fixes one finding and introduces two.

Third, the skill library is wired to the work rather than to a menu. Recommendations run on every prompt through keyword matching in roughly 50 milliseconds, with optional semantic matching behind it, and the structured recommender uses file patterns, branch names and commit subjects. For a Hermes profile with a large skill directory, that is the difference between 150 skills that exist and 150 skills that fire.

The caveat is age. The last push is 2026-06-28, and the framework targets Claude Code's agent and hook surface as it stood in mid 2026.

## Usage

| You say | What happens |
|---|---|
| "Implement this feature and get it reviewed" | `agent-loops` drives implementation, routes review to a different model, remediates P0 and P1 findings and re-reviews |
| "Audit the tests for this module" | `test-review` checks coverage and test quality, then the test writing loop fills the gaps |
| "Our docs claim this endpoint exists, check it" | `doc-claim-validator` compares documentation claims against the actual code |
| "Clean up this repository before we hand it over" | `repo-cleanup` inventories dead code, artefacts and unused dependencies, then reports before deleting |
| "Threat model this design" | `threat-modeling-techniques` runs STRIDE and attack trees over the proposed system |
| "Why is this React list slow?" | `react-performance-optimization` reads the render path and proposes memoisation or splitting |
| "Explain this module to a junior developer" | `code-explanation` fixes an audience level and structures the explanation around it |

## Verification

Read the workflow skill before installing, since it is the one that changes how the others run. This path returned HTTP 200 on `main` when this guide was written:

```bash
curl -fsSL https://raw.githubusercontent.com/nickcrew/claude-cortex/main/skills/agent-loops/SKILL.md | head -8
```

It should open with `name: agent-loops` and a description covering atomic commits, the code change loop, the test writing loop, the lint gate and circuit breakers. The security skill is worth a second fetch, because it is the highest install count in the set:

```bash
curl -fsSL https://raw.githubusercontent.com/nickcrew/claude-cortex/main/skills/owasp-top-10/SKILL.md | head -8
```

After install, confirm the CLI sees the library:

```bash
cortex skills list | head -20
cortex skills validate --all
```

`cortex skills list` is documented as the discovery command and `cortex skills validate --all` as the integrity check, so a validate run with failures means the bundled assets did not link cleanly and the review scripts may not resolve.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react-performance-optimization | Pass | Pass | Pass |
| owasp-top-10 | Pass | Warn | Pass |
| ui-design-aesthetics | Pass | Pass | Pass |

The library is not purely markdown, which is the part to check. Several skills ship executable Python: `multi-llm-consult/scripts/consult_llm.py` makes model calls, `webapp-testing/scripts/with_server.py` starts servers, and the bundled document skills carry PDF and spreadsheet scripts that write files. Read any `scripts/` folder before you let an agent run it unattended.

The framework also installs a hook, described in the shipped skills guide at `docs/guides/skills.md` as `hooks/skill_auto_suggester.py`, which reads your prompt text, changed files, file types and directories, the git branch name and recent commit subjects to print skill suggestions. That is local matching rather than telemetry, but it does mean prompt content is inspected on every turn, and it is the kind of hook you want to see in a diff before it is installed into a shared environment.

Two licence details. The repository is MIT with a LICENSE file. A `skills/LICENSE.superpowers` file is also present, MIT and copyright 2025 obra, because part of the library is vendored from that project, so keep the notice if you copy those modules on.

## Limitations

- Snapshot data, verified 2026-11-07: 11,752 combined installs across 150 indexed listings; 66 GitHub stars; MIT; last pushed 2026-06-28. Counts drift over time.
- Install counts are thin and top heavy. The median listed skill sits at 50 installs and one skill accounts for 1,908 of the 11,752. Treat the ranking as interest inside a small user base, not as a quality measure.
- Names and directories diverge. 17 indexed names have no directory of that exact name under `skills/`, and several are present under a different folder: the skill named `playwright-cli` lives in `skills/playwright/`, and `pdf`, `pptx` and `xlsx` live inside `skills/document-skills/`. Confirm the skill's own `name:` field rather than the folder name.
- The last push is 2026-06-28, roughly four months before this snapshot. The framework depends on Claude Code features including hooks, agent teams and slash commands, and that surface moves quickly.
- The review loop needs the CLI. `agent-loops` requires `cortex git commit` for commits and calls bundled provider-aware review scripts, so the skills without the Python package are guidance rather than an enforced gate.
- Part of the library is vendored from obra's superpowers project, which ships its own MIT notice at `skills/LICENSE.superpowers`, and the bundled document skills carry their own scripts. Read what you copy and keep the notices.
- Homebrew and pip installs of the same CLI conflict. Whichever binary is first on `$PATH` wins, per the README, so uninstall one.

## Related

- [Full Stack Skills - 788-Skill Catalog for Agents](/hermes/skills/catalog/full-stack-skills-setup)
- [ECC Engineering Skills - Enterprise Engineering Suite](/hermes/skills/catalog/ecc-engineering-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill](/hermes/skills/catalog/claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the package, not just the skills, if you want the review gates. The no-self-review routing lives in the CLI and its scripts, and the skill text alone cannot enforce a model swap.
- Start with `agent-loops`, `test-review` and `doc-claim-validator` rather than the highest install count. Those three describe the loop, and the rest are reference material the loop pulls in.
- Run `cortex skills validate --all` after every upgrade. The library is large and cross-referenced, and a partially linked install fails quietly at the point of use.
- Read the hook before enabling it. Prompt text, branch names and commit subjects are inspected on every turn to produce suggestions, which is fine locally and awkward in a shared home directory.
- Keep your own review chain if you leave Cortex. The useful part is the rule about who reviews, and that rule ports to any agent framework that can dispatch a reviewer with a different context.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
