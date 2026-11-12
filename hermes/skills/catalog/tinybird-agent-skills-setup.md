---
title: "Tinybird Agent Skills - Analytics Platform Setup"
description: "tinybirdco agent skills: 4.7K combined installs across 4 listings for datasources, pipes, the tb CLI and the TypeScript and Python SDKs"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tinybird-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "analytics", "tinybird", "sql", "typescript"]
---

# Tinybird Agent Skills - Setup Guide

**Source:** [tinybirdco/tinybird-agent-skills](https://www.skills.sh/tinybirdco/tinybird-agent-skills) via skills.sh - 4.7K combined installs across 4 indexed listings; first seen Jan 20, 2026 (Nov 11, 2026 sweep)
**GitHub:** 21 stars, no LICENSE file in the repository, `main` branch, last pushed 2026-07-29, 53 tracked files with four `SKILL.md` files under `skills/`
**Category:** Real-time analytics: datasource and pipe authoring, SQL and endpoint design, CLI operations, SDK usage
**Quality Tier:** 🟡 Established - a first-party vendor pack with clean scanner results on the core skill, held back by 21 stars, a missing LICENSE file and Warns on the CLI skill.

Tinybird is a managed platform for turning event streams into SQL endpoints. The unit of work is a project of files: `.datasource` definitions for what you ingest, `.pipe` files for the transforms and the endpoint, `.connection` files for anything external. That file format is the reason this pack works at all, and it is also where agents go wrong. A model that has never seen a `.pipe` file writes a query and then invents the surrounding structure.

These four skills cover the mechanics of that structure. `tinybird-best-practices` is the core, with 18 rule files across project layout, datasources, pipes, endpoints, SQL optimisation, deployments, testing and secrets. `tinybird-cli-guidelines` covers the `tb` command surface: local development, builds, deploys, appends, token management and mock data. The TypeScript and Python SDK skills cover defining datasources, pipes and queries with full type inference in code rather than in files.

The 18-rule core is the most useful part for an agent, because it encodes the constraints an agent cannot infer. Query optimisation in a streaming platform is not the same as query optimisation in Postgres, and the local development story has its own vocabulary.

The pack is small by every community measure. 21 stars is the thinnest signal in this batch, and the repository has no LICENSE file, so this is documentation that a vendor publishes for its own platform rather than a community project.

## Installation

The README's route is the skills CLI:

```bash
npx skills add tinybirdco/tinybird-agent-skills
npx skills update
```

Skills are available to the agent as soon as they are installed, and the agent selects them when the task matches. The README notes a way to check what the agent sees if you use the `amp` CLI.

There is no manual install section, which means the CLI path is the only documented one. If you install by hand, copy the four `skills/<name>/` directories rather than the repository root, and keep the `rules/` and `references/` folders inside each skill: the core skill cites its 18 rule files by relative path.

For the work to be useful you also need a Tinybird account and the `tb` CLI installed. The skills guide the agent through using them, not installing them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| tinybird | 1,741 | Core project guidelines: 18 rule files on datasources, pipes, endpoints, SQL optimisation, deployments and testing. |
| tinybird-cli-guidelines | 1,300 | The `tb` command surface: local development, builds, deploys, data appends, token and secret management, mock data. |
| tinybird-typescript-sdk-guidelines | 1,053 | Defining datasources, pipes and queries with the TypeScript SDK and full type inference. |
| tinybird-python-sdk-guidelines | 649 | The same definitions in Python with `tinybird-sdk`, for Python services and notebooks. |

All 4 indexed listings clear the threshold and appear above.

One naming fact matters when you look for the files: the listing named `tinybird` maps to the `skills/tinybird-best-practices/` directory in the tree. The README calls the skill `tinybird-best-practices` throughout, so the index and the repository disagree on the name of the core skill.

## Why This Matters for Hermes Agents

Analytics platforms fail agents in a specific way: the SQL is fine and the platform is not. A query that runs against a local database can be rejected by a streaming engine, and the error arrives after the agent has already written the endpoint.

The rule files pre-empt that. Rather than teaching SQL, they teach this platform's constraints: how a datasource is declared, what a pipe is allowed to reference, where the endpoint sits, how deployments promote changes, and how testing works. An agent that has read them writes files the build accepts on the first pass.

The CLI skill covers the half that agents usually skip. Local development with Tinybird Local, then a deploy, then a data append, then verifying the endpoint: that sequence is where a plausible change turns into a working one. Without it the agent edits files and declares success without ever running the build.

For a team already on Tinybird, the value is small per session and large over time. It removes the round trip where someone who knows the platform corrects what the agent wrote.

## Usage

| You say | What happens |
|---|---|
| "Create a datasource for these events" | Writes a `.datasource` file that matches the project layout the rule files describe rather than a bare SQL table. |
| "Build an endpoint that returns daily signups" | Creates the pipe and endpoint files, applies the query optimisation rules and names the endpoint path. |
| "Deploy this to production" | Uses the CLI guidelines for the build and deploy sequence, then reports the deployment result. |
| "Why is this pipe failing to build?" | Checks the pipe definition against the structural rules rather than only the SQL. |
| "Append this dataset to the datasource" | Uses the documented `tb` data operation and verifies the append. |
| "Write this as a typed TypeScript call" | Uses the TypeScript SDK skill for a typed query with inferred result types. |
| "Do the same in Python" | Uses the Python SDK skill for the equivalent definition and query. |

## Verification

The skills live under `skills/` in the repository. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/tinybirdco/tinybird-agent-skills/main/skills/tinybird-best-practices/SKILL.md | head -6
```

Confirm the rule files arrived, because the core skill references them by relative path and degrades quietly without them:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/tinybirdco/tinybird-agent-skills/main/skills/tinybird-cli-guidelines/SKILL.md
```

After installation, list the agent skills directory and look for four folders. If only one appeared, the installer took the root and missed the nested layout.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tinybird | Pass | Pass | Pass |
| tinybird-cli-guidelines | Pass | Warn | Warn |

The core skill passes all three. The CLI skill draws Warns, which tracks what it asks for: it documents `tb` commands that deploy, append and delete data, and manage tokens and secrets. A skill that teaches an agent to run those commands is legitimately flagged, and the flag is about consequence rather than about malice.

The practical control is scope. A Tinybird token is a credential with a defined permission set, and the right posture is a token that can do the work in front of you and nothing else. Neither the skill nor the scanner will enforce that.

## Limitations

- Snapshot data, verified 2026-11-11: 4,743 combined installs across 4 indexed listings; 21 GitHub stars; no LICENSE file; last pushed 2026-07-29. Counts drift over time.
- No LICENSE file is present in the repository. Treat it as vendor documentation published for use with Tinybird, not as an openly licensed package.
- 21 stars is a thin community signal. There is no user base reading each other's issues, so questions go to the vendor.
- The index names the core skill `tinybird` while the tree and the README call it `tinybird-best-practices`. Scripts that match on the listing name will miss the directory.
- The skills assume a Tinybird account, the `tb` CLI and a project already structured in the file format. None of that is installed by the pack.
- Warns on the CLI skill cover deploy, append, delete and token operations. Use a scoped token and read what the agent is about to run.

## Related

- [ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup)
- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)
- [Neon Postgres Skills - Database Design and Performance](/hermes/skills/catalog/neon-postgres-skills-setup)

## Pro Tips

- Ask for the project layout before the query. The structural rules are what make a build pass, and a query written first usually forces a rewrite.
- Run the build locally before deploying. The CLI skill documents the sequence, and a local build catches the file-level mistakes that a deploy reports as an opaque failure.
- Ask which SDK the project already uses. Mixing the TypeScript and Python definitions in one project is possible and confusing; the agent will do it if the request is ambiguous.
- Give the agent the rule file by name when a build fails: "apply the pipe structure rules" is a more useful prompt than quoting the error.
- Keep tokens scoped to one environment. The CLI skill manages secrets, and an agent with a production token can deploy a broken pipe in one step.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
