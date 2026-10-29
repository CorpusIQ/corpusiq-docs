---
title: "OpenCode Workflows - Command and Agent Template Suite Setup"
description: "OpenCode Workflows: 12.0K combined installs. 51 skill directories of OpenCode command templates, agent prompts and a configurator meta-agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/opencode-workflows-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "opencode", "agent prompts", "workflow templates"]
---

# OpenCode Workflows - Setup Guide

**Source:** [igorwarzocha/opencode-workflows](https://www.skills.sh/igorwarzocha/opencode-workflows) via skills.sh - 12.0K combined installs across 38 indexed listings; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [igorwarzocha/opencode-workflows](https://github.com/igorwarzocha/opencode-workflows) - 122 stars, no license file at the repository root, archived read-only, branch master, last pushed 2026-02-04; 51 `SKILL.md` directories spread across `.opencode/skill/`, `agents/<pack>/.opencode/skill/`, `agents/<pack>/skill/` and `cowork/.opencode/skill/`, alongside `commands/`, `plugins/`, `mcp-configs/` and the `at/` reference files

**Category:** OpenCode command templates, global agent prompts and skill scaffolding

**Quality Tier:** 🟡 Beta - single-author collection, 122 GitHub stars, archived read-only with no license file at the repository root, 51 skill directories against 38 indexed listings, and one Snyk warning in the six-skill sample

Igor Warzocha describes this as an ever evolving set of OpenCode workflow examples, filtered down to the parts that worked in daily use. The entry point is the Opencode Configurator in `agents/opencode-configurator/`, a meta-configuration agent that takes a plain request such as "is there a plugin for reducing token usage" or "set up permissions so destructive commands require approval" and routes it to one of seven skills: plugin-installer, opencode-config, command-creator, skill-creator, agent-architect, mcp-installer and model-researcher. Every prompt in the tree is written with RFC 2119 keywords (MUST, MUST NOT, SHOULD, MAY) inside XML tags, which is the same shape most agent runtimes already parse well, so the files read as instruction sets rather than tutorials.

The rest of the repository is a set of agent packs: a security reviewer bundling 10 framework-specific audit skills, a Vite plus React 19 plus Convex stack pack, a parallel PRD planner, a component engineer, a repo navigator, and the plugin development workflow. `commands/` holds 13 slash commands, `cowork/` is a multi-agent project management framework, and the `.opencode/` directory at the root is maintenance tooling that the README marks internal-only. Install counts are lopsided: powerpoint alone carries 6,007 of the 12,015 combined installs, so the index measures interest in document generation far more than in OpenCode configuration.

## Installation

The README has one install command, a plain clone:

```bash
git clone https://github.com/igorwarzocha/opencode-workflows.git
```

Its installation line for the configurator is "drop the `skill/` and `agent/` folders into `~/.config/opencode/`", and the Getting Started deploy step is the same idea per pack: copy the agents you want into `~/.config/opencode/agent/` and the skills into `~/.config/opencode/skill/`. OpenCode resolves skills from two scopes, project first and global second, so the same directory works either way:

```bash
# project scope, resolved from the git worktree root upward
mkdir -p .opencode/skill
cp -R opencode-workflows/.opencode/skill/skill-creator .opencode/skill/

# global scope, available in every project
mkdir -p ~/.config/opencode/skill
cp -R opencode-workflows/cowork/.opencode/skill/powerpoint ~/.config/opencode/skill/
```

For Hermes, copy the same directories into the profile skills folder. The skills are markdown plus their own `references/` and `scripts/` folders, so copy the whole directory rather than a lone `SKILL.md`:

```bash
git clone https://github.com/igorwarzocha/opencode-workflows.git
cp -R opencode-workflows/.opencode/skill/* ~/.hermes/profiles/corpusiq/skills/
cp -R opencode-workflows/cowork/.opencode/skill/powerpoint ~/.hermes/profiles/corpusiq/skills/
```

The skills.sh CLI is the other route, since these are its indexed listings. The repository itself documents only manual copies, so confirm a name against the tree before filtering:

```bash
npx skills add igorwarzocha/opencode-workflows --skill powerpoint --agent hermes-agent
```

Do not install the root `.opencode/` directory anywhere. The README carries a caution block on exactly this point: those commands and the `repo-maintenance` skill are hard-coded to this repository's own structure and metadata rules, and the README says not to install them globally.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| powerpoint | 6007 | Building decks by writing 720pt by 405pt HTML slides, rasterizing gradients and icons to PNG, then running `html2pptx.js` to produce the pptx, with a thumbnail grid audit for cutoff and overlap before delivery. |
| word | 774 | Writing .docx files with `python-docx` or raw OOXML, then a render and review loop that converts to PDF with `soffice`, to PNG with `pdftoppm`, and inspects the pages, plus tracked-change redlining and pandoc text extraction. |
| security-nextjs | 368 | Auditing a Next.js App Router codebase for the usual footguns: `NEXT_PUBLIC_` variables that are really secrets, Server Actions missing auth or input validation, middleware matcher gaps, API route auth and security headers. |
| create-opencode-plugin | 347 | Building an OpenCode plugin against the `@opencode-ai/plugin` SDK: custom tools, event hooks, auth providers and tool execution interception, with a seven-step procedure from SDK regeneration through testing and npm publish. |
| agent-architect | 318 | A guided question-and-answer pass that generates an agent's frontmatter, scope, permissions and model preferences, and diagnoses agents that ignore context or run slower than they need to. |
| opencode-config | 308 | Editing `opencode.json` and `AGENTS.md` with guided setup for providers and API keys, default models, permission blocks for destructive tools, formatter rules and environment variables, including global versus project precedence. |
| skill-creator | 290 | Scaffolding a skill directory and `SKILL.md`, writing and tuning the frontmatter description so the skill actually triggers, and organizing `scripts/`, `references/` and `assets/`. |
| excel | 202 | Spreadsheet modeling with openpyxl and pandas under zero-formula-error rules, assumptions held in dedicated input cells, unit labels and color coding, then a mandatory `recalc.py` audit pass before handoff. |

The remaining 30 indexed listings range from 92 to 184 installs.

## Why This Matters for Hermes Agents

The value here is not the OpenCode product, it is the prompt engineering. Every skill and agent in the tree states requirements with RFC 2119 keywords inside XML tags, which is exactly the discipline that makes a skill file predictable: MUST versus SHOULD separates a hard constraint from a preference, and the tags give a model an unambiguous boundary between instructions, examples and context. Copying a skill into a Hermes profile keeps that structure intact.

The configurator's seven skills also answer the questions that come up whenever a new agent CLI is wired into a host, and they answer them as procedures rather than as prose. Permission design, provider keys, MCP server discovery, model research for something that is not in models.dev yet, and skill authoring are each one skill file, so they can be lifted into a Hermes setup or used as a template for a house skill.

The document skills are the part with a track record, given where the installs sit. powerpoint, word and excel all encode the same rule: generate the file, render it, look at the render, fix what looks wrong, and only then deliver. That loop is the difference between an agent that produces a .pptx and an agent that produces a deck someone can open in a meeting.

The security reviewer is a reusable audit checklist split by stack, covering ten frameworks including Next.js, Express, FastAPI, Django, Docker, secrets handling and AI keys. Even with the repository archived, those checklists remain useful as review criteria for a Hermes agent that is asked to audit someone else's codebase.

## Usage

| You say | What happens |
|---|---|
| "Audit this Next.js app for leaked secrets and unauthenticated Server Actions" | security-nextjs greps the env files for `NEXT_PUBLIC_` prefixes, flags values that would be visible in view-source, then checks each Server Action and API route for auth and input validation. |
| "Turn this quarterly report into a 10-slide deck" | powerpoint builds the slides as HTML at 720pt by 405pt, rasterizes the visual assets, converts with `html2pptx.js`, then renders a thumbnail grid to check for cut text and overlap. |
| "Create a plugin that blocks destructive shell commands" | create-opencode-plugin verifies the SDK reference first, then implements a tool execution before hook with the blocking logic, and walks the test and publish steps. |
| "This agent keeps ignoring the context I give it" | agent-architect reviews the description clarity, allowed tools and permissions, and returns a revised frontmatter with the changes explained. |
| "Restrict this project so deletes require approval" | opencode-config adds a permission block to `opencode.json`, with the deny and allow entries scoped to the tools you named, and shows the merged result of project over global. |
| "My new skill never triggers" | skill-creator rewrites the frontmatter description to match how a runtime decides relevance, then checks the directory layout for the `references/` and `scripts/` paths the body cites. |
| "Build a budget model with formulas, no hardcoded totals" | excel puts every input in an assumption cell, writes the calculations as Excel formulas, formats per the input and formula color convention, and runs `recalc.py` until no error is reported. |

## Verification

Eight raw `SKILL.md` URLs for the top listings returned 200 on the `master` branch when this guide was written. Probe before installing, and note that `master` here is the default branch, not `main`:

```bash
for p in cowork/.opencode/skill/powerpoint/SKILL.md \
         cowork/.opencode/skill/word/SKILL.md \
         agents/security-reviewer/.opencode/skill/security-nextjs/SKILL.md \
         agents/create-opencode-plugin/.opencode/skill/create-opencode-plugin/SKILL.md \
         .opencode/skill/agent-architect/SKILL.md \
         .opencode/skill/opencode-config/SKILL.md \
         .opencode/skill/skill-creator/SKILL.md \
         cowork/.opencode/skill/excel/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/igorwarzocha/opencode-workflows/master/$p"
done
```

Read two before installing the rest, because they set up everything else:

- https://raw.githubusercontent.com/igorwarzocha/opencode-workflows/master/.opencode/skill/opencode-config/SKILL.md
- https://raw.githubusercontent.com/igorwarzocha/opencode-workflows/master/.opencode/skill/skill-creator/SKILL.md

After the copy, confirm what landed and that each directory kept its supporting files:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -cE '^(powerpoint|word|excel|pdf|skill-creator|agent-architect|opencode-config)$'
ls ~/.hermes/profiles/corpusiq/skills/powerpoint
```

A directory holding only `SKILL.md` is incomplete if its body cites `scripts/` or `references/`, which is the usual reason a copied skill fails on first use.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| powerpoint | Pass | Pass | Pass |
| word | Pass | Pass | Pass |
| security-nextjs | Pass | Pass | Pass |
| create-opencode-plugin | Pass | Pass | Pass |
| agent-architect | Pass | Pass | Warn W011 |
| opencode-config | Pass | Warn | Pass |

Four of the six sampled listings pass all three auditors. The two warnings land on the two skills that change how an agent is allowed to act: agent-architect carries a Snyk Warn with code W011 and writes agent permissions, while opencode-config carries a Socket Warn and edits `opencode.json`, which is where tool allow and deny lists live. Read both files before running them against a configuration you care about, and treat a warning as a reason to review rather than a verdict on the repository.

The install itself is quiet. The repository has no manifest at the root, so no package lifecycle script runs on clone, and nothing executes until an agent follows a skill's own instructions. What those instructions then do is the real surface: the document skills shell out to `soffice`, `pdftoppm`, `bun`, `node` and Python, and the configurator skills write to configuration files.

The licensing position matters more than usual here. There is no license file at the repository root and the GitHub API reports no SPDX license, so default copyright applies: read the prompts, learn the patterns, and re-implement rather than redistribute the files. Combined with the archive flag there is also no upstream fix path, so any issue you find stays yours.

## Limitations

- Snapshot data, verified 2026-10-28: 12015 combined installs across 38 indexed listings; 122 GitHub stars; no license file at the repository root; master branch; last pushed 2026-02-04, and the repository is archived read-only, so the tree and the counts are frozen unless the owner unarchives it.
- The repository is archived. Nothing is merged, no dependency is bumped, and the scripts the document skills call (`html2pptx.js`, `recalc.py`, `extract-plugin-api.ts`) are pinned at the February 2026 state; verify they still run on your runtime before building a workflow on them.
- No license, so no permission to redistribute. There is no SPDX identifier in the API response and no `LICENSE` file in the tree, which makes this a reference to study and adapt, not a pack to vendor into a product.
- The skills are written for OpenCode's own paths and config surface: `~/.config/opencode/skill/`, `.opencode/skill/`, `opencode.json`, `AGENTS.md`, the `question` tool and OpenCode's subagent types. Hermes reads `~/.hermes/profiles/corpusiq/skills/` and has no `opencode.json`, so expect to remap config edits and permission guidance rather than run those two skills verbatim.
- The index and the tree do not describe the same thing. There are 51 `SKILL.md` directories against 38 indexed listings, because the same skill is duplicated under `cowork/`, `agents/<pack>/` and the root `.opencode/`; installing from two of those copies gives an agent competing instructions for the same trigger.
- The sample is six skills out of 38 indexed listings, and four of the six are document and audit skills. The configuration-changing skills carry the only warnings in the set, and the remaining 32 listings were not reviewed by any auditor.

## Related

- [PowerPoint - Create, Read, Edit .pptx Decks Setup](/hermes/skills/catalog/powerpoint-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)

## Pro Tips

- Install the configurator's seven skills first and leave the rest for when you need them. They answer the meta questions (permissions, providers, MCP servers, model research) that otherwise turn into an afternoon of reading OpenCode docs.
- Copy whole directories. `powerpoint`, `word` and `excel` reference sibling files by relative path, so a lone `SKILL.md` installs a skill that cannot run its own verification loop.
- Skip the root `.opencode/` tree. Its commands and the `repo-maintenance` skill are hard-coded to this repository's own layout, and the README says not to install them globally.
- Use `skill-creator`'s frontmatter section as a review checklist for your own Hermes skills. The failure it targets, a description that never matches a real request, is the most common reason a skill sits unused.
- Keep the raw URLs on `master`. If you paste one into a script later, remember this repository never had a `main` branch, and the archive means that will not change.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
