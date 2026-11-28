---
title: "Awesome Claude Code Toolkit - Setup Guide"
description: "rohitg00/awesome-claude-code-toolkit: 8.0K combined installs. A Claude Code toolkit of agents, skills, plugins, commands, hooks, rules and templates."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/awesome-claude-code-toolkit-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "toolkit", "agents"]
---

# Awesome Claude Code Toolkit - Setup Guide

**Source:** [rohitg00/awesome-claude-code-toolkit](https://www.skills.sh/rohitg00/awesome-claude-code-toolkit) via skills.sh - 8.0K combined installs across 39 indexed listings; first seen 2026-11-28 (morning sweep)

**GitHub:** [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) - 2,878 stars, Apache-2.0, branch main, last pushed 2026-05-12; skills live under `skills/<name>/SKILL.md`, and the toolkit spans 135 agents, 176+ plugins, 42 commands, 20 hooks, 15 rules and 7 templates.

**Category:** Claude Code toolkit - agents, skills, plugins, commands, hooks, rules and templates

**Quality Tier:** 🟢 Green - all 20 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk scans.

rohitg00/awesome-claude-code-toolkit bills itself as the most comprehensive toolkit for Claude Code, published as a public repository and indexed on skills.sh. It gathers a broad ecosystem under one tree: 135 specialized agents across ten categories, 35 curated skills, 42 slash commands, 176+ plugins, 20 hooks, 15 rules, 7 templates and a set of MCP configurations. The skills.sh index surfaces 39 skill listings from this repository, every one of them a self-contained `skills/<name>/SKILL.md` module.

The 39 indexed listings are the curated skills plus a few community skills, each teaching a narrow discipline with code examples, anti-patterns and checklists. Install counts are modest, with the top listing reading 280 installs, but the repository is popular as a reference collection, carrying 2,878 stars under an Apache-2.0 license.

## Installation

The README offers three install paths. The plugin marketplace is recommended:

```text
/plugin marketplace add rohitg00/awesome-claude-code-toolkit
```

A one-liner fetches and runs the interactive installer:

```bash
curl -fsSL https://raw.githubusercontent.com/rohitg00/awesome-claude-code-toolkit/main/setup/install.sh | bash
```

Or clone manually:

```bash
git clone https://github.com/rohitg00/awesome-claude-code-toolkit.git ~/.claude/plugins/claude-code-toolkit
```

The installer (`bash setup/install.sh`) clones the repo, symlinks configs and installs plugins. Individual skills install through the SkillKit marketplace:

```bash
npx skillkit@latest install claude-code-toolkit/tdd-mastery
```

Individual plugins install with `/plugin install claude-code-toolkit@smart-commit`, or all at once with `/plugin install claude-code-toolkit`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| devops-automation | 280 | CI/CD pipeline design with GitHub Actions, Docker, Kubernetes, Helm and GitOps patterns. |
| accessibility-wcag | 238 | Web accessibility patterns for WCAG 2.2: ARIA, keyboard navigation, screen readers and testing. |
| database-optimization | 227 | Query optimization, indexing and database tuning for PostgreSQL and MySQL. |
| websocket-realtime | 225 | Real-time patterns with WebSocket, Socket.io, Server-Sent Events and scaling. |
| react-patterns | 225 | React 19 patterns: Server Components, Actions, Suspense, hooks and composition. |
| python-best-practices | 223 | Pythonic code with type hints, dataclasses, async patterns and testing. |
| api-design-patterns | 221 | REST API design: resource naming, pagination, versioning and OpenAPI generation. |
| mobile-development | 219 | React Native and Flutter patterns: navigation, state management and responsive design. |
| frontend-excellence | 217 | Modern frontend patterns: React Server Components, performance and Core Web Vitals. |
| data-engineering | 216 | ETL pipelines, data warehousing, Apache Spark and data quality validation. |
| ci-cd-pipelines | 216 | CI/CD patterns for GitHub Actions, GitLab CI, testing and deployment automation. |
| claude-memory-kit | 215 | Persistent memory for Claude Code: a hot cache plus knowledge wiki, safety hooks and end-of-day synthesis. |
| security-hardening | 208 | Application security: input validation, auth, headers and secrets management. |
| redis-patterns | 208 | Redis caching, pub/sub, streams, Lua scripts and data structures. |
| postgres-optimization | 208 | PostgreSQL indexes, query plans, partitioning, JSONB and connection pooling. |
| continuous-learning | 207 | Extract patterns from coding sessions, track corrections and build reusable knowledge. |
| prompt-engineering | 206 | Structured prompts, chain-of-thought, few-shot and system prompt design. |
| monitoring-observability | 205 | OpenTelemetry, Prometheus, Grafana dashboards and structured logging. |
| typescript-advanced | 204 | Advanced TypeScript: generics, conditional types, mapped types and template literals. |
| docker-best-practices | 204 | Multi-stage builds, compose patterns, image optimization and security. |
| nextjs-mastery | 203 | App Router, React Server Components, ISR, server actions and middleware. |
| golang-idioms | 203 | Go error handling, interfaces, concurrency and project layout. |
| testing-strategies | 201 | Contract, snapshot and property-based testing. |
| microservices-design | 201 | Event-driven architecture, the saga pattern and service mesh. |
| springboot-patterns | 200 | Spring Boot JPA, REST controllers and layered architecture. |
| authentication-patterns | 200 | JWT, OAuth2 PKCE, RBAC and session management. |
| performance-optimization | 199 | Code splitting, image optimization and Core Web Vitals. |
| tdd-mastery | 197 | Red-green-refactor, test-first design and coverage targets. |
| rust-systems | 197 | Rust ownership, traits, async patterns and error handling. |
| mcp-development | 197 | MCP server tools, resources and transport setup. |
| llm-integration | 197 | Streaming, function calling, RAG and cost optimization. |
| git-advanced | 197 | Git worktrees, bisect, interactive rebase and hooks. |
| kubernetes-operations | 195 | Kubernetes deployments, Helm charts, HPA and troubleshooting. |
| django-patterns | 195 | Django REST Framework, ORM optimization, signals and middleware. |
| graphql-design | 192 | GraphQL schema design, DataLoader, subscriptions and pagination. |
| aws-cloud-patterns | 192 | Lambda, DynamoDB, CDK and S3 event processing. |
| manage-skills | 177 | Discover, create, edit and delete agent skills across 11 tools from the terminal. |
| deep-dive | 175 | DAG-based deep research: parallel subagents and a sourced report. |
| agentkit-seo | 136 | Audit and optimize GitHub profiles and repositories. |

All 39 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

This repository is a one-stop reference for how a Claude Code setup is composed: agents, skills, commands, plugins, hooks, rules, templates and MCP configs all live under one tree, each with a documented layout. A Hermes builder wiring a skill router can read it as a taxonomy of the extension mechanisms an agent runtime supports, and as a directory of the problem domains people hand off to agents.

The 35 curated skills are the most reusable part for Hermes work. Each is a self-contained `skills/<name>/SKILL.md` that teaches a narrow discipline, such as TDD, API design, database optimization or security hardening, with code examples and anti-pattern checklists. That structure maps directly onto the skills Hermes loads: a folder, a SKILL.md with frontmatter, and instructions.

The repository also models the line between a skill that is instructions-only and the executable layers that enforce those instructions. The skills are prose patterns, while the hooks, commands and plugins show where automation and hard constraints belong, which is a useful default for a builder deciding what belongs in a skill versus a hook versus a command.

The security posture on the sampled subset is clean: all 20 sampled skills pass the Gen Agent Trust Hub, Socket and Snyk scans. That makes this a low-friction collection to pull patterns from, though the modest install counts mean it reads more like a curated index than a widely deployed dependency.

## Usage

| You say | What happens |
|---|---|
| "Review my React component for hooks and Suspense issues" | Loads react-patterns to apply React 19 patterns for hooks, server components and error boundaries. |
| "Check the query plan on this slow PostgreSQL endpoint" | Loads postgres-optimization to reason about indexes, query plans and partitioning. |
| "Set up a test-first loop for this module" | Loads tdd-mastery for red-green-refactor and coverage targets. |
| "Design a versioned REST API from this spec" | Loads api-design-patterns for resource naming, versioning and OpenAPI generation. |
| "Harden this service's auth and secrets handling" | Loads security-hardening for input validation, auth and secrets management. |
| "Optimize this Dockerfile" | Loads docker-best-practices for multi-stage builds and image optimization. |

## Verification

The README installs through the plugin marketplace and `setup/install.sh` on branch main, so the cleanest pre-install check is to fetch a skill's SKILL.md directly and read its frontmatter:

```bash
curl -sL https://raw.githubusercontent.com/rohitg00/awesome-claude-code-toolkit/main/skills/tdd-mastery/SKILL.md
```

After a clone, confirm the skill directories:

```bash
git clone --depth 1 https://github.com/rohitg00/awesome-claude-code-toolkit.git /tmp/awesome-claude-code-toolkit
ls /tmp/awesome-claude-code-toolkit/skills/
head -3 /tmp/awesome-claude-code-toolkit/skills/tdd-mastery/SKILL.md
```

The skills listing should show 40 skill directories: the 39 indexed listings plus `styleseed`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| devops-automation | Pass | Pass | Pass |
| accessibility-wcag | Pass | Pass | Pass |
| database-optimization | Pass | Pass | Pass |
| websocket-realtime | Pass | Pass | Pass |
| react-patterns | Pass | Pass | Pass |
| python-best-practices | Pass | Pass | Pass |
| api-design-patterns | Pass | Pass | Pass |
| mobile-development | Pass | Pass | Pass |
| frontend-excellence | Pass | Pass | Pass |
| data-engineering | Pass | Pass | Pass |
| ci-cd-pipelines | Pass | Pass | Pass |
| claude-memory-kit | Pass | Pass | Pass |
| security-hardening | Pass | Pass | Pass |
| redis-patterns | Pass | Pass | Pass |
| postgres-optimization | Pass | Pass | Pass |
| continuous-learning | Pass | Pass | Pass |
| prompt-engineering | Pass | Pass | Pass |
| monitoring-observability | Pass | Pass | Pass |
| typescript-advanced | Pass | Pass | Pass |
| docker-best-practices | Pass | Pass | Pass |

This guide is Green because every sampled skill passes all three scanners. The Gen Agent Trust Hub, Socket and Snyk all return Pass on the 20 sampled listings; the other 19 indexed listings were not sampled.

## Limitations

- Snapshot data, verified 2026-11-28: 8,026 combined installs across 39 indexed listings; 2878 GitHub stars; Apache-2.0 licence; last pushed 2026-05-12. Counts drift over time.
- The tree holds 40 skill directories but only 39 are indexed: `styleseed` (the StyleSeed design-method skill) carries no skills.sh install count.
- Install counts are modest across the board (the top listing reads 280), so treat this as a curated reference index rather than a widely deployed dependency.
- The security sample covers 20 of the 39 indexed listings; the other 19 were not sampled.
- The README's own component tallies drift, with MCP configs described as 14, 15 and 16 in different sections, so treat the counts as approximate.

## Related

- [Anthropic Skills - Official Agent Skills Repository](/hermes/skills/catalog/anthropics-skills-setup)
- [Claude Code Extensions - Agents, Skills & Hooks Setup](/hermes/skills/catalog/nodnarbnitram-claude-code-extensions-setup)
- [AI Labs Claude Skills - 27 Skill Business Suite Setup](/hermes/skills/catalog/ailabs-claude-skills-setup)
- [Anthropic Claude API Skills - Official Claude API](/hermes/skills/catalog/anthropics-claude-api-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read a skill's SKILL.md before installing the whole toolkit: the 35 curated skills each carry a two-field frontmatter and instructions, so you can cherry-pick only the ones you need.
- Prefer the plugin marketplace or `setup/install.sh` on Claude Code; the one-liner and manual clone are equivalent, but the marketplace keeps plugins up to date.
- Use the skill directories as naming and structure references for your own SKILL.md files: a lowercase-hyphen directory plus a SKILL.md whose description states the discipline it teaches.
- Treat the hooks and rules folders as the enforcement layer to copy when a skill needs to become a hard constraint rather than guidance.
- Because the sample covers only 20 of the 39 listings, re-check the skills.sh security pages for any skill you plan to pull into a production profile.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
