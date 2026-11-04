---
title: "Agent Reference Skills - 174 Role Playbooks"
description: "fandhe-ai/agent-reference-skills on skills.sh: 15.8K combined installs across 135 listings; 174 reference playbooks for frameworks and platforms."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-reference-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "api reference", "claude code"]
---

# Agent Reference Skills - Setup Guide

**Source:** [fandhe-ai/agent-reference-skills](https://www.skills.sh/fandhe-ai/agent-reference-skills) via skills.sh - 15.8K combined installs across 135 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 4 stars, no LICENSE file, last pushed 2026-11-04, 174 SKILL.md directories
**Category:** Vendor API reference for agents: Apple, Android and Windows platform docs plus Anthropic, OpenAI and Google SDK coverage
**Quality Tier:** 🟡 Yellow: the repo ships no LICENSE file and carries only 4 stars, and three of the five sampled skills draw a Warn from Gen Agent Trust Hub or Socket

This is a documentation library rather than a workflow library. Each skill is a set of reference pages pulled from a vendor's own docs and structured as markdown, so an agent writing or reviewing code can read the current API surface instead of recalling it. Coverage runs across the Apple stack (Swift, SwiftUI, UIKit, AppKit, Metal, Core ML), Android (Compose, Room, CameraX, Wear OS), Windows (WinUI 3, Windows App SDK), the Anthropic, OpenAI and Google platforms, plus framework and tooling references such as Playwright, Zod, Biome, Turborepo and Supabase.

Two counts disagree and both matter. skills.sh indexes 135 listings, while the repo tree carries 174 SKILL.md directories: 149 under skills/, 23 under .agents/skills/ and 2 under .claude/skills/. The 23 workflow skills (create-pr, implement-issue, project-sync-issues and similar) are Claude Code process automation, not API reference, so the library is a mix of the two. The repo has no LICENSE file and 4 stars, which is worth knowing before you build a dependency on it.

## Installation

The README uses the vercel-labs skills CLI, and every command in this section comes from it:

```bash
npx skills add Fandhe-AI/agent-reference-skills --list
```

```bash
npx skills add Fandhe-AI/agent-reference-skills --skill vitest
```

```bash
npx skills add Fandhe-AI/agent-reference-skills --skill vitest --skill zod --skill biome
```

```bash
npx skills add Fandhe-AI/agent-reference-skills --all
```

By default the CLI symlinks into the project's .claude/skills/ directory; add --copy to place real files instead. The -g flag installs into ~/.claude/skills/ so every project on the machine can use the skill:

```bash
npx skills add Fandhe-AI/agent-reference-skills --skill react-router -g
```

For Hermes, the practical route is the official one: run the CLI with --copy and then move the resulting skill directory into your agent's own skills directory, since the CLI targets Claude Code paths by default. Add one skill at a time when you are testing, because --all pulls the full 174 directories plus their references/ trees.

## What It Provides

Twenty of the 135 indexed listings clear 151 installs.

| Skill | Installs | Use For |
|---|---|---|
| github-docs | 1,487 | GitHub REST, GraphQL, Actions, webhooks and gh CLI reference |
| commitlint | 1,239 | Commit message linting against Conventional Commits rules |
| lefthook | 1,220 | Git hooks manager for pre-commit and pre-push checks |
| editorconfig | 1,217 | .editorconfig format and editor settings |
| rust | 1,017 | Rust ownership, lifetimes, traits, async and Cargo |
| anthropic-claude-code | 729 | Claude Code CLI basics, settings.json, CLAUDE.md and env vars |
| make | 591 | GNU Make rules, variables, .PHONY, parallel and recursive builds |
| anthropic-claude-code-extend | 462 | Claude Code extension: Agent Skills, subagents, hooks, MCP and plugins |
| openai-codex | 389 | OpenAI Codex across CLI, IDE and cloud, AGENTS.md and sandbox |
| nvidia-cuda | 360 | CUDA C++ and Python kernels, nvcc, PTX and Blackwell tuning |
| apple-silicon | 298 | Metal shading language, compute dispatch, unified memory and MLX |
| chakra-ui | 255 | Chakra UI v3 components, theme, recipes and style props |
| fandhe-backend | 254 | The author's Rust HTTP framework: server, router, middleware |
| amd-rocm | 252 | ROCm and HIP programming, hipify, rocBLAS, MIOpen and RCCL |
| playwright | 234 | Playwright E2E tests, locators, fixtures, trace and auth |
| fandhe-frontend | 226 | The author's Rust frontend framework: SSR, SPA, SSG and hydration |
| dgx-spark | 213 | DGX Spark GB10 setup, ConnectX-7 cluster and local LLM playbook |
| windows-interop-modernize | 194 | Win32 and COM interop, C++/WinRT, XAML Islands and WPF migration |
| ark-ui | 156 | Ark UI headless components, asChild, RootProvider and collections |
| anthropic-api-tools-mcp | 151 | Claude API tool use, server tools, Skills API and MCP connector |

The remaining 115 indexed listings range from 3 to 144 installs.

## Why This Matters for Hermes Agents

Most skill packs answer "how should I approach this task". This one answers "what is the current signature", which is the failure mode that bites an agent most often: a correct-looking call to an API that moved two versions ago.

For Hermes agents the useful pattern is retrieval by domain. A platform skill such as apple-silicon or android-compose-ui ships a top-level SKILL.md plus a references/ tree that the skill tells the agent to walk, so the agent reads the specific page rather than one long document. That keeps context spend proportional to the question.

The split between reference and workflow skills is also instructive. The .agents/skills entries (create-commit, create-pr, create-plan, implement-issue) are small procedural playbooks that pair a reference lookup with a repo action, which is the shape most teams end up writing by hand.

Coverage is uneven by design. Vendor platforms and the author's own frameworks are covered in depth; the newer language and tooling entries are thinner. Treat the install count as a hint about maturity, not a guarantee.

The infrastructure is the weak point, not the content: 4 stars, no licence and a single author means you are depending on a personal repository that gets pushed often. Pin what you use.

## Usage

| You say | What happens |
|---|---|
| "Add a GitHub Actions workflow that publishes on tag" | github-docs walks workflow syntax, triggers and token permissions |
| "Why does the compiler reject this borrow?" | rust explains ownership, lifetimes and the trait bound in play |
| "Set up pre-commit hooks for this repo" | lefthook writes the hook config and commitlint adds the message rules |
| "Build a settings dialog with Chakra" | chakra-ui covers v3 recipes and theme tokens, ark-ui supplies the headless primitive |
| "Port this WPF screen to WinUI 3" | windows-interop-modernize covers XAML Islands and the C#/WinRT route |
| "Write an E2E test for checkout" | playwright sets up locators, fixtures and trace capture |
| "Expose a tool to my Claude agent" | anthropic-api-tools-mcp covers tool use, server tools and the MCP connector |

## Verification

List what the CLI can see before installing anything:

```bash
npx skills add Fandhe-AI/agent-reference-skills --list
```

Then fetch one raw skill file to confirm the tree matches what skills.sh indexed. This URL is the skills/github-docs/SKILL.md path on branch main:

```bash
curl -fsSL https://raw.githubusercontent.com/fandhe-ai/agent-reference-skills/main/skills/github-docs/SKILL.md | head -30
```

A response with YAML frontmatter, a name field and a directory map of the references tree confirms the content is live. After installing, check the skill landed where the agent looks:

```bash
ls .claude/skills
```

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| github-docs | Pass | Pass | Pass |
| react-hook-form | Warn | Pass | Pass |
| android-wear | Pass | Pass | Pass |
| upstash | Pass | Warn | Pass |
| anthropic-admin-platform | Pass | Warn | Pass |

The repo has no LICENSE file, so there is no stated grant to copy, redistribute or embed these skills in a product. The maintainer's own AGENTS.md sets strict rules against dangerous command examples and prompt injection in reference content, which is a good sign for the content itself, but a review policy is not a licence.

## Limitations

- Snapshot data, verified November 4, 2026: 15,776 combined installs across 135 indexed listings; 4 GitHub stars; no LICENSE file; last pushed 2026-11-04. Counts drift over time.
- The tree carries 174 SKILL.md directories against 135 indexed listings, and three of those listings have no matching directory, so 42 directories have no public install data. The repo's own docs disagree further: the README heading says 141 skills and AGENTS.md says 110.
- No LICENSE file exists anywhere in the repository root. Treat the content as all rights reserved until the author states otherwise.
- 4 stars and a single author is a thin adoption signal for a library this size; pin a commit rather than tracking main.
- Three indexed listings have counts but no matching SKILL.md directory in the current tree: react-router-v7, fandhe-vector-db and dgx-spark-user-guide.
- 23 of the 174 directories live under .agents/skills/ and are Claude Code workflow skills (create-issue, implement-review, project-create-issues), not API reference. The README and the skill bodies are written in Japanese, so expect Japanese prompt text inside the skills.

## Related

- [Agentic Awesome Skills - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Anthropic Claude API Skills - Official Claude API](/hermes/skills/catalog/anthropics-claude-api-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the one skill you need with --skill rather than --all. The github-docs references tree alone runs to dozens of files.
- Read the skill's directory map in SKILL.md before letting an agent loose on it; the reference pages are meant to be fetched selectively.
- Prefer the platform skills (apple-swift, android-data, windows-app-sdk) over general framework skills when the question is about SDK behaviour, since those trees come straight from vendor docs.
- Skip the .agents/skills workflow entries unless you actually work inside this repository's process; they assume its issue and PR conventions.
- Check a skill's fetched date in the SKILL.md before trusting a signature. Some references were captured in October 2026 and vendor APIs move.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
