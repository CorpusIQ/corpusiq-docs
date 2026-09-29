---
title: "Dotnet Skills - .NET AI Coding Setup"
description: "Official Microsoft .NET team skills for AI coding agents working with C# and .NET; ~206,971 indexed installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dotnet-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "dotnet", "csharp"]
---

# Dotnet Skills - Setup Guide

**Source:** [dotnet/skills](https://github.com/dotnet/skills) (5,505⭐)
**Skill family:** `dotnet/skills` (6 installable skills)
**Combined Installs:** ~206,971 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Developer Tools
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

Published by the official Microsoft .NET team, this repository holds the .NET team's curated set of portable skills and host-specific custom agents for coding agents, following the Agent Skills standard at agentskills.io. The README lists 15 plugins (dotnet, dotnet-data, dotnet-diag, dotnet-msbuild, dotnet-nuget, dotnet-upgrade, dotnet-maui, dotnet-ai, dotnet-aspnetcore, dotnet-blazor, dotnet-test, and more); the skills.sh snapshot indexes 6 entries, led by test running, EF Core query optimization, performance analysis, OpenTelemetry configuration, and test anti-patterns.

---

## Installation

```bash
npx skills add dotnet/skills
```

## Roster - Top Skills

| Skill | Installs | What It Does |
|---|---|---|
| run-tests | 4,232 | Running .NET test suites |
| optimizing-ef-core-queries | 4,184 | EF Core query optimization |
| analyzing-dotnet-performance | 3,534 | .NET performance analysis |
| configuring-opentelemetry-dotnet | 3,467 | OpenTelemetry setup for .NET |
| test-anti-patterns | 3,170 | Avoiding test anti-patterns |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| .NET repo CI health | Use run-tests for test invocation and filtering patterns |
| EF Core performance tuning | Apply optimizing-ef-core-queries to database-backed services |
| Adding observability to .NET apps | Use configuring-opentelemetry-dotnet for tracing and metrics setup |

## Limitations / Verification

- The Sep 29, 2026 snapshot indexes 6 skills with 0/6 published verification entries; the repo README documents a much larger plugin catalog (15 plugins) that the sweep does not fully cover.
- The main-branch README was fetched to confirm the skill layout; install and star counts come from the marketplace snapshot.
- No live install test has been run from Hermes yet.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
