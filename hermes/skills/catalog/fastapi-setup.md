---
title: "FastAPI - Official FastAPI Agent Skill Setup"
description: "fastapi/fastapi - 16.6K combined installs: the official FastAPI framework's agent skill for APIs, Pydantic, dependencies, and SSE."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fastapi-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "fastapi", "python", "api"]
---

# FastAPI - Setup Guide

**Source:** [fastapi/fastapi](https://www.skills.sh/fastapi/fastapi) via skills.sh - 16.6K combined installs across 1 indexed listing; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [fastapi/fastapi](https://github.com/fastapi/fastapi) - 105,048 stars, MIT license, last pushed Nov 24, 2026, master branch; one skill at fastapi/.agents/skills/fastapi/SKILL.md.
**Category:** Python Web Framework (FastAPI)
**Quality Tier:** 🟢 Green - the single listing is sampled and passes all three checks.

This is the official FastAPI framework repository, and its agent skill is a single listing, not a skill collection. skills.sh indexes exactly one skill named fastapi, and the full 16,588 combined installs attach to that single listing. The skill lives inside the framework monorepo at fastapi/.agents/skills/fastapi/SKILL.md, with eight reference files (dependencies, fastapi-cloud, other-tools, parameter-models, path-operations, pydantic, responses, and streaming) alongside it.

The skill itself is a compact best-practices guide for working with FastAPI APIs, Pydantic models, dependencies, and streaming responses including Server-Sent Events (SSE), plus serving frontend apps. The default branch is master, not main, so every raw URL in this guide uses master.

## Installation

The skill is a Markdown file inside the FastAPI monorepo, and the README documents no skills-CLI install for it. To use it, clone the repo and copy the skill folder into your agent's skills directory:

```bash
git clone --depth 1 https://github.com/fastapi/fastapi.git
mkdir -p ~/.claude/skills
cp -r fastapi/fastapi/.agents/skills/fastapi ~/.claude/skills/
```

Adjust the destination for your agent (for example ~/.agents/skills/ for Codex, or .claude/skills/ for a project). The FastAPI framework itself installs with uv:

```bash
uv add "fastapi[standard]"
```

## What It Provides

skills.sh publishes a per-skill install count for the single indexed listing.

| Skill | Installs | Use For |
|---|---|---|
| fastapi | 16,588 | FastAPI best practices and conventions for APIs, Pydantic models, dependencies, SSE streaming responses, and serving frontend apps |

No indexed listings fall below the 1,000-install threshold.

## Why This Matters for Hermes Agents

FastAPI is one of the most-used Python web frameworks, and an agent that scaffolds or edits FastAPI code benefits from a single, current conventions file rather than re-deriving patterns from memory. The skill keeps the agent aligned with the latest FastAPI features and patterns, and its eight reference files split concerns so the agent can load only the guidance it needs for a given change. Because the skill lives in the framework's own monorepo and is maintained alongside the code, it tracks upstream changes more closely than a third-party FastAPI skill would. The trade-off is distribution: there is no skills-CLI install path documented, so a Hermes agent setup must copy the folder or read the SKILL.md directly, and the skill is one listing among 3,279 repo files.

## Usage

| You say | What happens |
|---|---|
| Scaffold a FastAPI endpoint | Uses the skill's path-operations and parameter-models references for clean route and parameter design |
| Add a Pydantic model to my API | Uses the pydantic reference for model and validation conventions |
| Add a dependency to this route | Uses the dependencies reference for the dependency-injection patterns |
| Stream responses from my endpoint | Uses the streaming reference, including Server-Sent Events |
| Serve a frontend from FastAPI | Uses the fastapi-cloud and serving guidance for hosting frontend apps |

## Verification

Confirm the README and the skill body resolve on the master branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/fastapi/fastapi/master/README.md | head -40
curl -sL https://raw.githubusercontent.com/fastapi/fastapi/master/fastapi/.agents/skills/fastapi/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/fastapi/fastapi/master/fastapi/.agents/skills/fastapi/references/pydantic.md | head -40
```

All three URLs return 200. After installing, review the SKILL.md and its reference files before relying on it.

## Security

skills.sh verdicts for the sampled skill (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| fastapi | Pass | Pass | Pass |

Across the 1 sampled skill there are 3 Pass, 0 Warn, and 0 Fail cells; the single listing passes all three checks.

## Limitations

- Snapshot data, verified Nov 26, 2026: 16,588 combined installs across 1 indexed listing; 105,048 GitHub stars; MIT license; last pushed Nov 24, 2026. Counts drift over time.
- The default branch is master, not main; every raw URL in this guide uses master, and scripts that assume main will 404.
- This is one skill inside the FastAPI framework monorepo, not a skill collection; the 16,588 installs attach to the single fastapi listing.
- The skill sits at fastapi/.agents/skills/fastapi/SKILL.md (inside the FastAPI package directory), not at the repo root; most of the 3,279 repo files are framework source, docs, and tests unrelated to the skill.
- The README is product-level and documents no skills-CLI install command, so installation is a manual copy rather than npx skills add.

## Related

[OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup) | [Apollo GraphQL Skills - GraphQL and Rust Setup](/hermes/skills/catalog/apollographql-skills-setup) | [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use the master branch in every raw URL; the repo has no main branch.
- Load only the reference file you need (pydantic.md for models, dependencies.md for DI, streaming.md for SSE) instead of reading the whole skill.
- Copy the folder into your agent's own skills directory rather than pointing at the monorepo, so upstream updates do not rewrite your working copy.
- Pin the framework version separately with uv (uv add "fastapi[standard]"); the skill tracks the latest patterns, not a specific release.
- Keep the reference files together with SKILL.md; the skill cross-links them by relative path.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
