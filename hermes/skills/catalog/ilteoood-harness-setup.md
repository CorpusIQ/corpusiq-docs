---
title: "ilteoood Harness - Agent Skills and Provisioning Setup"
description: "ilteoood/harness - 19.2K combined installs: a machine-provisioning harness with 44 skills for GitHub, planning, web and mobile development."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ilteoood-harness-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "machine provisioning", "skill catalog", "developer tooling"]
---

# ilteoood Harness - Setup Guide

**Source:** [ilteoood/harness](https://www.skills.sh/ilteoood/harness) via skills.sh - 19.2K combined installs across 44 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [ilteoood/harness](https://github.com/ilteoood/harness) - 2 stars, no LICENSE file, main branch, last pushed Nov 24, 2026; skills live under skills/<category>/<name>/SKILL.md across seven categories (core, plan, development, web-development, nodejs-development, mobile-development, presentation-creation).
**Category:** Machine Provisioning and Agent Skill Catalog
**Quality Tier:** 🟠 Orange - dependabot fails Snyk and seven of the 15 sampled skills carry a Warn cell; the repo has no LICENSE file.

ilteoood/harness publishes AI harness, a curated catalog of 44 agent skills grouped by project category, together with the scripts that configure the machines those agents run on. Skills are synced in from several upstream repositories - github/awesome-copilot, github/gh-stack, mattpocock/skills, anthropics/skills, vercel-labs/agent-skills, mcollina/skills, raineorshine/npm-check-updates, callstackincubator/agent-skills and slidevjs/slidev - via sync-config.js and sync-skills.js, with a handful of skills maintained in place.

Two provisioning scripts - claude-code.sh and pi-agent.sh - bootstrap a fresh Debian/Ubuntu machine with system packages, language toolchains, the GitHub CLI, global npm tools, and this repository's skills. The catalog spans seven categories: core/ (git, GitHub, security, dev tooling), plan/ (specs, READMEs, design interviews), development/ (implementation workflows), web-development/, nodejs-development/, mobile-development/ and presentation-creation/.

## Installation

Install only the skills, without the machine provisioning:

```bash
skills add https://github.com/ilteoood/harness -g -a claude-code -y
```

To provision a fresh machine and install the agent plus every skill globally, run one of the provisioning scripts instead:

```bash
./claude-code.sh
./pi-agent.sh
```

Core skills should live at the root .claude folder so they are available across every project; category-scoped skills belong in the .claude folder of the projects they apply to. To add an upstream skill, declare its repository, branch and category in sync-config.js, then run node sync-skills.js to download it into skills/<category>/<name>.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| github-issues | 630 | create, update and manage GitHub issues through MCP tools |
| git-commit | 626 | stage files, write a Conventional Commits message and run git commit |
| conventional-commit | 623 | generate Conventional Commits messages from a structured prompt and workflow |
| create-technical-spike | 623 | write time-boxed technical spike documents for research decisions |
| codeql | 621 | set up and configure CodeQL code scanning via GitHub Actions and the CodeQL CLI |
| create-specification | 621 | create a specification file optimized for AI consumption |
| github-release | 620 | release a new GitHub library version with SemVer and Keep a Changelog |
| create-readme | 620 | generate a README.md file for the project |
| create-implementation-plan | 620 | create an implementation plan for features, refactors or package upgrades |
| create-agentsmd | 620 | generate an AGENTS.md file for a repository |
| commit-message-storyteller | 620 | generate narrative commit messages that explain why a change was made |
| dependabot | 619 | configure and manage GitHub Dependabot and dependency updates |
| create-tldr-page | 619 | build a tldr page from documentation URLs and command examples |
| create-llms | 619 | create an llms.txt file from the repository structure |

The remaining 30 indexed listings range from 137 to 612 installs.

Index-vs-tree drift: the listing fastify-best-practices (611) has no directory under that exact name in the tree (the tree carries skills/nodejs-development/fastify/), gh-cli (327), thermos (221), thermo-nuclear-review (221) and thermo-nuclear-code-quality-review (220) have no matching directory at all, and react-native-development plus react-frontend-development exist in the tree but carry no listing.

## Why This Matters for Hermes Agents

The catalog is a single curated entry point to well-known upstream skill suites, from github/awesome-copilot's git and GitHub skills to mattpocock/skills' planning and design interviews, mcollina/skills' Node and Fastify guidance, and callstackincubator/agent-skills' React Native set, so it is a fast way to give a Hermes agent a broad, tested base layer. The category split (core, plan, development, then language- and platform-specific folders) is the layout worth copying: universal skills at the root, domain skills scoped to the projects that need them. The sync-config.js plus sync-skills.js pair shows how to pin a catalog to upstream versions and update it reproducibly instead of vendoring files by hand. The provisioning scripts go beyond Markdown skills, wiring system packages, toolchains, the GitHub CLI, plugins and daemons in one script. The no-LICENSE status and the single Snyk fail are the trade-offs to weigh before adopting the catalog wholesale.

## Usage

| You say | What happens |
|---|---|
| File a bug on this repo | Uses github-issues to create a GitHub issue with labels and fields |
| Commit my changes | Uses git-commit to stage files and write a Conventional Commits message |
| Set up CodeQL scanning | Uses codeql to configure a GitHub Actions workflow |
| Write a spec for this feature | Uses create-specification to draft a specification optimized for AI consumption |
| Release a new version | Uses github-release to walk through SemVer and Keep a Changelog |
| Document this repository | Uses create-readme and create-agentsmd to generate the docs files |
| Make an llms.txt for this repo | Uses create-llms to build the file from the repository structure |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/ilteoood/harness/main/README.md | head -40
```

Review a representative skill body before installing:

```bash
curl -sL https://raw.githubusercontent.com/ilteoood/harness/main/skills/core/git-commit/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| github-issues | Pass | Pass | Warn |
| git-commit | Pass | Pass | Warn |
| conventional-commit | Warn | Pass | Pass |
| create-technical-spike | Pass | Pass | Warn |
| codeql | Pass | Pass | Pass |
| create-specification | Pass | Pass | Pass |
| github-release | Pass | Pass | Warn |
| create-readme | Pass | Pass | Warn |
| create-implementation-plan | Pass | Pass | Pass |
| create-agentsmd | Pass | Pass | Pass |
| commit-message-storyteller | Pass | Pass | Pass |
| dependabot | Pass | Pass | Fail |
| create-tldr-page | Pass | Pass | Warn |
| create-llms | Pass | Pass | Pass |
| git-flow-branch-creator | Pass | Pass | Pass |

Only 15 of the 44 listings were sampled. The repository has no LICENSE file, so review usage terms before adopting the skills.

## Limitations

- Snapshot data, verified Nov 24, 2026: 19,226 combined installs across 44 indexed listings; 2 GitHub stars; no LICENSE file; last pushed Nov 24, 2026. Counts drift over time.
- The repository has no LICENSE file, so the skills are not under a stated open-source license; treat reuse terms as unclear.
- Index-vs-tree drift: fastify-best-practices, gh-cli, thermos, thermo-nuclear-review and thermo-nuclear-code-quality-review carry install counts but have no directory under their listed names, while fastify, react-native-development and react-frontend-development exist in the tree under names the index does not list.
- Skills are synced from third-party upstream repositories, so fixes and updates land through sync-skills.js rather than being authored in this repository.
- One sampled skill fails Snyk (dependabot) and seven others carry Warn cells; re-check before production use.

## Related

- [FuDesign2008 Open Skills - Jira, Git and Workflow Setup](/hermes/skills/catalog/fudesign-open-skills-setup)
- [khasky - Awesome Agent Skills Setup](/hermes/skills/catalog/khasky-awesome-agent-skills-setup)
- [Darkmatter Skills - Team Skill Catalog Setup](/hermes/skills/catalog/darkmatter-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install skills-only with `skills add https://github.com/ilteoood/harness -g -a claude-code -y` if you only want the catalog without the machine provisioning.
- Keep core skills at the root .claude folder and category skills in the projects they apply to, as the README advises.
- Add upstream skills through sync-config.js and node sync-skills.js rather than copying files by hand.
- Review the no-LICENSE status and the dependabot Snyk verdict before adopting the catalog in production.
- Treat claude-code.sh and pi-agent.sh as machine-wide changes; they install system packages and register plugins and daemons.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
