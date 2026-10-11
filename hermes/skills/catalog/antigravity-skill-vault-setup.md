---
title: "Antigravity Skill Vault - 300+ Skills Setup"
description: "Setup guide for rmyndharis/antigravity-skills - 10.1K combined installs. 300+ skills for Google Antigravity, ported from wshobson/agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/antigravity-skill-vault-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "google antigravity", "skill collection", "developer agents"]
---

# Antigravity Skill Vault - Setup Guide

**Source:** [rmyndharis/antigravity-skills](https://www.skills.sh/rmyndharis/antigravity-skills) via skills.sh - 10.1K combined installs across 96 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [rmyndharis/antigravity-skills](https://github.com/rmyndharis/antigravity-skills) (1,730 stars, MIT; pushed 2026-10-01; layout `skills/<name>/SKILL.md`, flattened)
**Category:** Skill Collection / Google Antigravity
**Quality Tier:** 🟡 Beta - 1,730-star MIT collection; port of wshobson/agents; all sampled verdicts Pass

The "Antigravity Skill Vault" is a 1,730-star curated collection of agent skills for Google Antigravity, ported from the wshobson/agents Claude Code ecosystem. The README claims 300+ skills across development, operations, security, and business domains; the skills.sh API indexes 96 listings for this repository (its page cap), which carry 10.1K combined installs. The install curve is steep: `unity-developer` alone accounts for 2,944 installs, with the rest of the meaningful usage in the architect, language-pro, and specialist skills below.

The vault flattens three kinds of source material into one skill format: domain skills, specialist agent personas (architects, security auditors, analysts) turned into instruction sets, and commands and workflows turned into multi-step procedures. The README's install guidance is token-conscious: Antigravity loads metadata for every installed skill at session start, so it recommends targeted installs by search, tag, or bundle (`core-dev`, `security-core`, `k8s-core`, `data-core`, `ops-core`) over `install --all`. For Hermes agents the vault is most useful as a source of role-flavored skills: architect reviews, specialist coding personas, and business analysis.

---

## Installation

Prerequisites: Node.js for the `npx` installer. Skills install to workspace scope (`<workspace-root>/.agent/skills/`) or globally (`~/.gemini/antigravity/skills/`).

```bash
# Search first, then install targeted skills (recommended)
npx @rmyndharis/antigravity-skills search kubernetes
npx @rmyndharis/antigravity-skills install bash-pro

# Or install a bundle or tag
npx @rmyndharis/antigravity-skills install --bundle core-dev
npx @rmyndharis/antigravity-skills install --tag kubernetes

# Global install
npx @rmyndharis/antigravity-skills install bash-pro --global
```

The README also documents an experimental native route (`agy plugin install https://github.com/rmyndharis/antigravity-skills`, not yet verified end-to-end per the README) and manual copying into the skills directory. `install --all` exists but is explicitly not recommended: it inflates session context and can trigger unrelated skills.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| unity-developer | 2,944 | Unity 6 LTS game dev: optimized C# scripts, URP/HDRP pipelines, asset management, cross-platform deployment |
| dotnet-architect | 346 | .NET backend architecture: C#, ASP.NET Core, Entity Framework, Dapper, enterprise patterns |
| backend-architect | 243 | Scalable API and microservice design: REST/GraphQL/gRPC, service boundaries, resilience patterns |
| java-pro | 225 | Modern Java 21+: virtual threads, pattern matching, Spring Boot 3.x, GraalVM, cloud-native patterns |
| frontend-developer | 221 | React 19 and Next.js 15 components: responsive layouts, state management, accessibility, performance |
| business-analyst | 220 | AI-powered business analysis: KPI frameworks, predictive models, dashboards, strategic recommendations |
| database-architect | 208 | Data layer design: SQL/NoSQL/TimeSeries selection, schema modeling, migration planning |
| ui-ux-designer | 149 | Interface design and design systems: wireframes, design tokens, component libraries, accessibility |
| code-refactoring-refactor-clean | 141 | Refactor code to clean-code principles: SOLID patterns, maintainability, performance |
| architect-review | 134 | Review designs and code changes for architectural integrity, scalability, and maintainability |
| csharp-pro | 133 | Modern C#: records, pattern matching, async/await, enterprise .NET patterns |
| backend-security-coder | 129 | Secure backend coding: input validation, authentication, API security reviews |
| minecraft-bukkit-pro | 121 | Minecraft server plugins: Bukkit, Spigot, and Paper APIs, event-driven architecture, performance |

The remaining 83 indexed listings range from 38 to 118 installs; quant-analyst and bash-pro (118 each) lead that tail, which bottoms out at 38 installs for legal-advisor, firmware-analyst, security-scanning-security-hardening, and git-advanced-workflows.

## Why This Matters for Hermes Agents

The vault's pitch is breadth at zero authoring cost: 96 indexed skills that give an agent prebuilt domain expertise and specialist personas, from Unity game work and .NET architecture to database design and Minecraft plugin development. The port lineage matters: wshobson/agents is a widely used Claude Code agent collection, and this project repackages that material for Antigravity's skill format, so the content has real mileage behind it. Install strategy is the main skill: loading the metadata of 300+ skills is a context tax, and targeted installs by tag or bundle keep sessions lean. Role skills change agent behavior in a useful way: an architect-review or backend-security-coder persona makes the agent reason in a discipline's vocabulary rather than generically. One caveat on coverage: only three skills were security-sampled, and while the sampled ones passed, the other 93 indexed listings are unreviewed.

## Usage

| You say | What happens |
|---|---|
| "Review this system design for architectural integrity" | architect-review applies clean-architecture, microservices, and DDD review criteria |
| "Refactor this module to clean-code standards" | code-refactoring-refactor-clean applies SOLID patterns and modern engineering practices |
| "Build this Unity feature with a proper asset pipeline" | unity-developer applies Unity 6 LTS, URP/HDRP, and cross-platform build patterns |
| "Design the backend API for this service" | backend-architect covers REST/GraphQL/gRPC design, service boundaries, and resilience |
| "Move this Java service to modern patterns" | java-pro applies Java 21+ features (virtual threads, pattern matching) and Spring Boot 3.x |
| "Model the database layer for a new product" | database-architect selects SQL/NoSQL, designs the schema, and plans migrations |
| "Write the requirements doc for this feature" | business-analyst builds KPI frameworks and data-driven recommendations |

## Verification

```bash
# Confirm installed skills (local and global scopes)
npx @rmyndharis/antigravity-skills installed
npx @rmyndharis/antigravity-skills installed --global

# Review a skill straight from GitHub before installing (returns 200)
curl -s https://raw.githubusercontent.com/rmyndharis/antigravity-skills/main/skills/unity-developer/SKILL.md | head -20
```

`doctor` and `stats` commands are also available for install health and inventory. Check that installed skills land in `.agent/skills/` (workspace) or `~/.gemini/antigravity/skills/` (global).

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| unity-developer | Pass | Pass | Pass |
| code-refactoring-refactor-clean | Pass | Pass | Pass |
| react-expert | - | - | - |

Both sampled skills with verdict data are clean on all three engines; a third sample (react-expert) returned no data. Sampling covers a tiny slice of the 96 listings, so treat unsampled skills as unreviewed.

## Limitations

- Indexing cap: skills.sh exposes 96 listings (its API page cap) against a README-claimed 300+ skills, so the counts here cover only the visible window.
- Port of another publisher's collection (wshobson/agents); upstream changes can lag before they reach this vault.
- Last push Oct 1, 2026; check freshness for fast-moving stacks before relying on a skill.
- Bulk installs are a context tax: the README warns that `install --all` increases token usage and can trigger unrelated skills.
- The native `agy plugin install` route is experimental and not verified end-to-end; use `npx` or manual installs instead.
- Snapshot data, verified Oct 10, 2026: 10.1K combined installs across 96 indexed listings; 1,730 GitHub stars; MIT; last pushed Oct 1, 2026. Counts drift over time.

## Related

- [Skills for Antigravity - Game & Research Collection Setup](/hermes/skills/catalog/skills-for-antigravity-setup) - a different publisher's Antigravity pack worth comparing
- [wshobson/agents - Agent Plugin Marketplace Setup](/hermes/skills/catalog/wshobson-agents-setup) - the upstream collection this vault ports
- [Unity AI Skills - Official Unity 29-Skill Game Dev Suite Setup](/hermes/skills/catalog/unity-ai-skills-setup) - the official Unity alternative to unity-developer here
- [AntiGravity Lazy Pack Skills Setup](/hermes/skills/catalog/antigravity-lazy-pack-setup) - another Antigravity-oriented skill pack
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install targeted, not wholesale: `search` then `install <name>`, or pick a bundle (core-dev, security-core, k8s-core, data-core, ops-core).
- Long names have aliases (aliases.json); check the alias before scripting an install of names like code-refactoring-refactor-clean.
- Keep role skills project-scoped (`.agent/skills/`) so personas do not follow you into unrelated projects.
- `update`, `installed --global`, `doctor`, and `stats` round out lifecycle management.
- The vault unifies domain skills, specialist personas, and workflow commands, so you can mix discipline depth (kubernetes-architect) with execution flows (full-stack-orchestration-full-stack-feature).

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
