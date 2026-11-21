---
title: "Farmage OpenCode Skills - 67 AI Skills Setup Guide"
description: "farmage/opencode-skills: 67 specialized AI skills plus 9 workflow commands for OpenCode - 21.5K combined installs across 67 indexed listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/farmage-opencode-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "opencode", "coding skills", "developer tools"]
---

# farmage OpenCode Skills - 67 AI Skills Setup Guide

**Source:** [farmage/opencode-skills](https://www.skills.sh/farmage/opencode-skills) via skills.sh - 21.5K combined installs across 67 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [farmage/opencode-skills](https://github.com/farmage/opencode-skills) - 247 stars, MIT license, main branch, last pushed Sep 27, 2026; canonical skills under `skills/<name>/SKILL.md` plus an `.opencode/` wrapper tree and 9 workflow commands under `.opencode/commands/`.
**Category:** Coding and Development Skills
**Quality Tier:** 🟡 Yellow - sampled skills.sh verdicts are mostly Pass with a few Warn cells (code-reviewer and prompt-engineer on Snyk; security-reviewer and nextjs-developer on Socket); no Fails.

`farmage/opencode-skills` is an OpenCode adaptation of Claude Skills by jeffallan, shipping 67 specialized agent skills plus 9 workflow commands that plug into OpenCode's native skill and command system. The skills span 12 domains: languages, frameworks, infrastructure and DevOps, architecture and quality, and specialized topics such as Salesforce, Shopify, MCP development, prompt engineering, RAG and fine-tuning. The workflow commands cover discovery, planning, execution and retrospectives, with optional Jira and Confluence integration through the Atlassian MCP setup.

Each skill is a `SKILL.md` plus a `references/` directory of deep-dive technical documents that load on demand, keeping context small until a skill activates. OpenCode matches a message against skill descriptions and triggers, loads the matching `SKILL.md`, then pulls reference files only as needed. The README recommends installing with `install.sh`, `make`, or a remote curl one-liner, then restarting OpenCode. First seen in the Nov 20, 2026 evening sweep.

## Installation

Clone and run the installer (recommended):

```bash
git clone https://github.com/farmage/opencode-skills.git
cd opencode-skills
./install.sh
```

Alternative via Makefile, global or project-local:

```bash
make install          # global (~/.config/opencode/)
make install-local    # project-local (.opencode/)
```

Remote one-liner, no clone needed:

```bash
curl -fsSL https://raw.githubusercontent.com/farmage/opencode-skills/main/install.sh | bash
```

Restart OpenCode after installation so the new skill descriptions are picked up.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| code-reviewer | 409 | structured code review reports with prioritized, actionable feedback |
| prompt-engineer | 390 | prompt templates, structured output schemas and evaluation rubrics |
| debugging-wizard | 384 | systematic hypothesis-driven debugging of errors, stack traces and logs |
| api-designer | 383 | REST and GraphQL API design, OpenAPI specs and versioning |
| test-master | 368 | unit, integration, E2E and security test generation and coverage analysis |
| architecture-designer | 366 | system design, ADRs and component interaction planning |
| python-pro | 362 | type-safe Python 3.11+ with async, pytest and linting |
| security-reviewer | 360 | vulnerability audits and remediation reports with severity ratings |
| react-expert | 359 | React 18+ components, hooks, Server Components and performance |
| typescript-pro | 354 | advanced type systems, type guards and full-stack type safety |
| nextjs-developer | 350 | Next.js 14+ App Router, server components and server actions |

The remaining 56 indexed listings range from 86 to 346 installs.

## Why This Matters for Hermes Agents

This library turns a coding agent into a domain specialist that loads the right expertise on demand instead of carrying every rule into every prompt. A message about a slow PostgreSQL query matches database-optimizer and postgres-pro; a security review request matches security-reviewer and code-reviewer. That routing is driven by each skill's description and triggers, and only the matching `SKILL.md` plus its references load, so context stays small. The multi-skill workflow chains are the real value: Feature Forge to Architecture Designer to Fullstack Guardian to Test Master for feature work, and Secure Code Guardian to Security Reviewer to Test Master for security passes. Skills ship as plain directories under `skills/<name>/SKILL.md`, so the same content is portable to any agent host that reads the Agent Skills layout. The 9 workflow commands extend the skills into project management, with Jira and Confluence integration available through the Atlassian MCP setup.

## Usage

| You say | What happens |
|---|---|
| Implement JWT authentication in my NestJS API | Loads nestjs-expert plus secure-code-guardian for auth and security hardening |
| Debug this memory leak in my Node.js app | Loads debugging-wizard plus the matching framework expert to trace the leak |
| Review this PR for security issues | Loads security-reviewer plus code-reviewer for a broad-scope pass |
| Design the architecture for a new microservices platform | Loads architecture-designer and microservices-architect for system design and ADRs |
| Write unit tests for this FastAPI service | Loads test-master and fastapi-expert for pytest coverage |
| Set up a CI/CD pipeline in GitHub Actions | Loads devops-engineer for pipeline and container configuration |

## Verification

```bash
# after install, confirm skills landed in the global OpenCode path
ls ~/.config/opencode/skills/
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/farmage/opencode-skills/main/skills/code-reviewer/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. Skills live under `skills/<name>/SKILL.md` in the repo; the installer places them in `~/.config/opencode/skills/` for a global install or `.opencode/skills/` for a project-local install.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| code-reviewer | Pass | Pass | Warn |
| prompt-engineer | Pass | Pass | Warn |
| debugging-wizard | Pass | Pass | Pass |
| api-designer | Pass | Pass | Pass |
| test-master | Pass | Pass | Pass |
| architecture-designer | Pass | Pass | Pass |
| python-pro | Pass | Pass | Pass |
| security-reviewer | Pass | Warn | Pass |
| react-expert | Pass | Pass | Pass |
| typescript-pro | Pass | Pass | Pass |
| nextjs-developer | Pass | Warn | Pass |
| postgres-pro | Pass | Pass | Pass |
| fastapi-expert | Pass | Pass | Pass |
| code-documenter | Pass | Pass | Pass |
| database-optimizer | Pass | Pass | Pass |
| devops-engineer | Pass | Pass | Pass |
| sql-pro | Pass | Pass | Pass |
| javascript-pro | Pass | Warn | Pass |
| secure-code-guardian | Pass | Pass | Pass |
| vue-expert | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 21,497 combined installs across 67 indexed listings; 247 GitHub stars; MIT license; last pushed Sep 27, 2026. Counts drift over time.
- Only 20 of the 67 listings carry skills.sh verdicts; the other 47 are unverified on that platform.
- The repository is an OpenCode adaptation of jeffallan's Claude Skills, so skill content and workflow commands derive from that upstream and should be attributed accordingly.
- The `.opencode/` tree duplicates the canonical `skills/` and `commands/` trees as OpenCode-format wrappers; canonical content lives under `skills/` and `commands/`.
- The workflow commands integrate with Jira and Confluence only when the Atlassian MCP server is configured, which is a separate setup step.

## Related

- [OpenCode Skills - Agent Skill Collection Setup](/hermes/skills/catalog/opencode-skills-setup)
- [OpenCode Workflows - Workflow Automation Setup](/hermes/skills/catalog/opencode-workflows-setup)
- [OpenCode - Terminal Coding Agent Setup](/hermes/skills/catalog/opencode-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use `make install` for a global install and `make install-local` for a project-scoped copy; keep them separate so per-project overrides do not leak into the global set.
- Use `make dev-link` to symlink skills into `~/.config/opencode/skills/` for live editing, and `make validate` to check YAML, names and cross-references.
- Restart OpenCode after installing or changing skills so the updated descriptions and triggers are reloaded.
- Leave `references/` files intact: they load on demand and are cross-referenced by their skill, so editing them out of context can break a skill.
- Chain skills for complex tasks (Feature Forge to Architecture Designer to Fullstack Guardian to Test Master) instead of invoking them one at a time.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
