---
title: "Dify Skills - Official Dev Workflow Suite Setup"
description: "Setup guide for langgenius/dify - 22.6K combined installs. Official Dify agent skills for frontend code review, testing, and refactoring."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dify-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "dify", "engineering workflows", "code review"]
---

# Dify Skills - Setup Guide

**Source:** [langgenius/dify](https://www.skills.sh/langgenius/dify) via skills.sh - 22.6K combined installs across 15 indexed listings; first seen Aug 12, 2026 (evening sweep); converted Oct 10, 2026 (zero-catalog audit)
**GitHub:** [langgenius/dify](https://github.com/langgenius/dify) (158,105 stars, NOASSERTION license; pushed Oct 11, 2026; `.agents/skills/<name>/SKILL.md` layout with `.claude/skills/<name>` symlinks)
**Category:** Full-Stack Development / Official Workflows
**Quality Tier:** 🟢 Production - official Dify repository (158,105 stars); internal engineering workflow skills; mixed sampled verdicts - see Security

Dify is one of the most widely starred open-source LLM application platforms, and this is its official set of internal engineering-workflow skills for AI coding agents. The indexed skills mirror the work the Dify team does on its own monorepo: frontend code review (9,983 installs), frontend testing, component refactoring, backend code review, and more, published straight from the product repository instead of a side project.

The skills live under `.agents/skills/<name>/SKILL.md`, with `.claude/skills/<name>` symlinks pointing into that directory. One caveat up front: the skills.sh index carries 15 listings for this repository, but the current tree ships only five skill directories (backend-code-review, e2e-cucumber-playwright, frontend-code-review, frontend-testing, how-to-write-component). The other 10 indexed listings have no counterpart in the current tree, so verify a skill exists before you rely on it. A difyctl README in the repo's `skills/` directory documents the base skill's install mechanism.

---

## Installation

Prerequisites: Node.js for the skills CLI, or a working `difyctl` install if you prefer the repository's own tooling.

```bash
# Browse what the skills CLI sees for this repo
npx skills add langgenius/dify --list

# Install the difyctl base skill (command from the repo's skills README)
npx skills add langgenius/dify --skill difyctl -g
```

Or route through difyctl itself, which pulls the skills from the commit the CLI was built from:

```bash
difyctl install skills <dir>
```

`--from` can point difyctl at any GitHub folder with the same layout, or at a local folder. Because of the index-vs-tree drift described in Limitations, confirm each skill against the current tree before scripting installs; the review and testing skills are the safest anchors.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| frontend-code-review | 9,983 | Review frontend changes against Dify's engineering conventions |
| frontend-testing | 3,741 | Frontend test workflow and conventions for the Dify web app |
| component-refactoring | 3,697 | Refactor frontend components safely in the Dify codebase |
| backend-code-review | 2,063 | Backend code review for Dify's platform services |
| skill-creator | 755 | Create new skills in Dify's internal skills format |
| orpc-contract-first | 713 | Contract-first development workflow built around oRPC |
| web-design-guidelines | 688 | Apply Dify's web design guidelines to interface work |
| vercel-react-best-practices | 612 | Vercel's React best practices applied to frontend work in Dify |

The remaining 7 indexed listings range from 2 to 116 installs, led by e2e-cucumber-playwright (116) and how-to-write-component (109).

## Why This Matters for Hermes Agents

These are production engineering workflows from one of the most active LLM-application repositories in the ecosystem, and they target the same work Hermes agents do on real codebases: review frontend and backend diffs against house conventions, write and run tests, and refactor components without breaking contracts. The distribution pattern is worth studying as much as the skills themselves, with agent skills living inside the product repo and installed both through the public Vercel skills CLI and through the product's own difyctl tooling. The `.agents/skills/` plus `.claude/skills/` symlink layout is also a clean reference for multi-agent directory conventions, where one canonical tree serves several agent platforms. And the index-vs-tree drift is a useful lesson in verification: an index count is not proof a skill still exists, so check the tree before scripting installs. For teams building on Dify, adopting these skills shortens the distance between platform conventions and agent output.

## Usage

| You say | What happens |
|---|---|
| "Review my frontend changes before I open a PR" | frontend-code-review runs the Dify frontend review conventions over the diff |
| "Write tests for the new dashboard component" | frontend-testing applies the repo's frontend testing workflow |
| "Refactor this component without changing behavior" | component-refactoring drives a safe component refactor |
| "Check my backend changes against our conventions" | backend-code-review reviews backend code in Dify's house style |
| "Scaffold a new internal skill for the team" | skill-creator sets up a skill in Dify's internal format |
| "Apply our design guidelines to this page" | web-design-guidelines checks interface work against Dify's web standards |
| "Structure this API work contract-first" | orpc-contract-first organizes the implementation around API contracts |

## Verification

```bash
# Confirm the install through the skills CLI
npx skills list | grep -i dify

# Check the .agents/skills layout in a checkout of the repo
ls .agents/skills/

# Review the frontend-code-review skill from GitHub before installing
curl -sL https://raw.githubusercontent.com/langgenius/dify/main/.agents/skills/frontend-code-review/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| frontend-code-review | Pass | Pass | Warn |
| frontend-testing | Pass | Pass | Pass |
| component-refactoring | Pass | Pass | Pass |

## Limitations

- Index-vs-tree drift: the index lists 15 skills, but only 5 have a counterpart in the current tree; the other 10 indexed listings have no matching directory.
- License caveat: GitHub reports NOASSERTION for this repository, so review the license terms before production use.
- The skills are internal engineering workflows for the Dify monorepo, not a general-purpose skill collection.
- The parent repository is extremely active and the skill tree can move between reads; pin a commit if you vendor copies.
- Snapshot data, verified Oct 10, 2026: 22,620 combined installs across 15 indexed listings; 158,105 GitHub stars; NOASSERTION; last pushed Oct 11, 2026. Counts drift over time.

## Related

- [LangChain Agent Skills - Memory, RAG, Persistence & Middleware Setup](/hermes/skills/catalog/langchain-skills-setup) - adjacent LLM-app framework skills for RAG and agent work
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup) - another official platform skill suite worth comparing
- [Open Mercato Skills - Enterprise ERP Engineering Setup](/hermes/skills/catalog/open-mercato-skills-setup) - another product-repo engineering workflow suite
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Treat `.agents/skills/` as the source of truth; the `.claude/skills/` entries are symlinks into it, so you only maintain one tree.
- Verify existence before installing: with most indexed listings absent from the current tree, the repo beats the index.
- Start with frontend-code-review, the flagship at 9,983 installs, if you work in the web app.
- The difyctl route keeps installed skills matched to the CLI build you run (`difyctl install skills <dir>`).
- Re-check the skills directory after upgrading Dify; active development means it changes often.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
