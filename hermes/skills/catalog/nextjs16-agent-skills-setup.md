---
title: "Next.js 16 Agent Skills - Migration and Framework Setup"
description: "gocallum/nextjs16-agent-skills - 4.7K combined installs: Next.js 16, Prisma 7, Auth.js and AI SDK v6 skills for AI agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nextjs16-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "nextjs", "prisma", "ai-sdk"]
---

# Next.js 16 Agent Skills - Setup Guide

**Source:** [gocallum/nextjs16-agent-skills](https://www.skills.sh/gocallum/nextjs16-agent-skills) via skills.sh - 4.7K combined installs across 8 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [gocallum/nextjs16-agent-skills](https://github.com/gocallum/nextjs16-agent-skills) - 23 stars, no LICENSE file, main branch, last pushed Jan 21, 2026; one SKILL.md per directory under skills/, with scripts/ and references/ alongside several skills.
**Category:** Next.js and Web Framework Skills
**Quality Tier:** 🟡 Yellow - nextjs16-skills, clerk-nextjs-skills and resend-integration-skills each carry one Warn cell; no Fail cells among the 8 sampled.

gocallum/nextjs16-agent-skills is a collection of skills for AI coding agents focused on the newest major versions of popular web frameworks, so agents produce code that matches current APIs instead of deprecated patterns from older training data. Each skill is packaged instructions with a SKILL.md plus optional scripts/ and references/ directories, and the collection follows the Agent Skills open standard, working with Claude Code, GitHub Copilot, Google Antigravity and other compatible agents.

The eight indexed skills cover Next.js 16 migration (Turbopack and async request APIs), Prisma ORM 7 (ESM-only and driver adapters), AI SDK 6 (agents, ToolLoopAgent and Vercel AI Gateway), Auth.js v5, Clerk authentication, Resend email via MCP, MCP server patterns and Upstash Vector DB. The repository was last pushed in January 2026, so the Next.js 16 guidance in particular may have drifted from the framework's current state since this snapshot.

## Installation

Install all skills with the skills CLI:

```bash
npx skills add gocallum/nextjs16-agent-skills
```

Individual skills can also be copied manually. For Claude Code, copy a skill folder into ~/.claude/skills/; for GitHub Copilot in VS Code, into .github/skills/ or .vscode/skills/; for Cursor, into .cursor/skills/.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| prisma-orm-v7-skills | 1,040 | upgrading to Prisma ORM 7 and its breaking changes |
| authjs-skills | 799 | Auth.js v5 setup for Next.js authentication |
| nextjs16-skills | 727 | Next.js 16 breaking changes, Turbopack and async request APIs |
| ai-sdk-6-skills | 485 | AI SDK 6 agents, tool approval and Vercel AI Gateway |
| clerk-nextjs-skills | 439 | Clerk authentication for Next.js 16 with proxy.ts setup |
| resend-integration-skills | 415 | Resend email via MCP for AI agents |
| mcp-server-skills | 388 | building MCP servers in Next.js with shared Zod schemas |
| upstash-vector-db-skills | 369 | Upstash Vector DB semantic search and embedding models |

All 8 indexed listings clear the 300-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Framework migration is exactly where AI agents are weakest: models trained on older versions generate deprecated Next.js, Prisma and AI SDK patterns without explicit guidance. This collection meets that gap by packaging the breaking changes of each major release, so an agent asked to migrate a project sees the actual codemods, async request APIs and ESM-only requirements instead of guessing. The Next.js 16 skill covers Turbopack and the async request API shift; prisma-orm-v7-skills documents the ESM-only migration, driver adapters and prisma.config.ts; ai-sdk-6-skills covers ToolLoopAgent and tool approval. The integration skills extend the same idea to services: Clerk proxy.ts migration from middleware.ts, Resend email via MCP, and Upstash Vector for semantic search. Builders who run multiple agents get the same skills across Claude Code, Copilot, Cursor and Google Antigravity because the collection follows the Agent Skills open standard. The main caveat is freshness: the repository was last pushed in January 2026, so re-verify the migration steps against current framework docs.

## Usage

| You say | What happens |
|---|---|
| Migrate my app to Next.js 16 | Uses nextjs16-skills for Turbopack, async request APIs and the upgrade path |
| Upgrade my schema to Prisma ORM 7 | Uses prisma-orm-v7-skills for the ESM-only and driver adapter breaking changes |
| Add AI SDK agents to my app | Uses ai-sdk-6-skills for agents, tool approval and Vercel AI Gateway |
| Set up Auth.js v5 authentication | Uses authjs-skills for Google OAuth, credentials and environment config |
| Move from middleware.ts to proxy.ts for Clerk | Uses clerk-nextjs-skills for the App Router proxy setup |
| Send transactional email from an agent | Uses resend-integration-skills for Resend via MCP |
| Add semantic search to my Vercel app | Uses upstash-vector-db-skills for vectors and embedding models |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/gocallum/nextjs16-agent-skills/main/README.md | head -40
```

Confirm the Prisma 7 skill body is present before migration work:

```bash
curl -sL https://raw.githubusercontent.com/gocallum/nextjs16-agent-skills/main/skills/prisma-orm-v7-skills/SKILL.md | head -30
```

Confirm the Next.js 16 skill body is present (note the uppercase .MD extension):

```bash
curl -sL https://raw.githubusercontent.com/gocallum/nextjs16-agent-skills/main/skills/nextjs16-skills/SKILL.MD | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| prisma-orm-v7-skills | Pass | Pass | Pass |
| authjs-skills | Pass | Pass | Pass |
| nextjs16-skills | Pass | Pass | Warn |
| ai-sdk-6-skills | Pass | Pass | Pass |
| clerk-nextjs-skills | Pass | Warn | Pass |
| resend-integration-skills | Pass | Warn | Pass |
| mcp-server-skills | Pass | Pass | Pass |
| upstash-vector-db-skills | Pass | Pass | Pass |

Three of the eight sampled skills carry a Warn cell: nextjs16-skills on Snyk, and clerk-nextjs-skills and resend-integration-skills on Socket. The remaining five sampled skills pass all three checks.

## Limitations

- Snapshot data, verified Nov 24, 2026: 4,662 combined installs across 8 indexed listings; 23 GitHub stars; no LICENSE file; last pushed Jan 21, 2026. Counts drift over time.
- The last push was January 2026, about ten months before this snapshot, so the Next.js 16, Prisma 7 and AI SDK 6 migration guidance may have drifted from the frameworks' current state.
- The README footer states MIT, but the repository ships no LICENSE file, so confirm licensing before redistribution.
- Index-vs-tree drift: the repo tree ships three more skill directories than the eight indexed listings (ai-agents-ui-skills, ba-prd-skills and shadcn-skills), which carry no install counts.
- Several skills bundle shell scripts (setup-clerk-nextjs.sh, setup-resend-mcp.sh) and reference files, a larger audit surface than Markdown-only skills.

## Related

- [Claude Code Next.js Skills - Next.js 16 and AI SDK Setup](/hermes/skills/catalog/claude-code-nextjs-skills-setup)
- [Next.js Agent Skills - Official Vercel Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [OpenReview Next.js Skills - Vercel Engineering Suite](/hermes/skills/catalog/openreview-next-skills-setup)
- [Tailwind 4 Docs Skill - Local Docs Snapshot Setup](/hermes/skills/catalog/tailwind-4-docs-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the full set with npx skills add gocallum/nextjs16-agent-skills, or copy only the skills your project actually uses.
- Re-check the upstream Next.js 16, Prisma 7 and AI SDK 6 docs before trusting the migration steps, since the repo was last pushed in January 2026.
- Use prisma-orm-v7-skills before generating or troubleshooting a schema, since Prisma 7's ESM-only change alters generation behavior.
- For Clerk, follow the proxy.ts migration in clerk-nextjs-skills rather than keeping middleware.ts on Next.js 16.
- Review the bundled setup shell scripts before running them, since they are the largest audit surface in the collection.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
