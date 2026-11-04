---
title: "DuckDB Skills - Local Analytics for Agents"
description: "duckdb/duckdb-skills on skills.sh: 9.4K combined installs across 9 listings; SQL querying, file reading and object storage exploration over DuckDB."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/duckdb-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "duckdb", "analytics", "sql"]
---

# DuckDB Skills - Setup Guide

**Source:** [duckdb/duckdb-skills](https://www.skills.sh/duckdb/duckdb-skills) via skills.sh - 9.4K combined installs across 9 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 616 stars, MIT licence, last pushed 2026-04-23, 9 SKILL.md directories under skills/
**Category:** Local analytics for agents: DuckDB querying, file formats, extensions and analytical patterns over local data
**Quality Tier:** 🟡 Yellow: every sampled skill passes Gen Agent Trust Hub and Socket, but read-file and s3-explore each draw a Snyk Warn

A Claude Code plugin that gives an agent DuckDB: one skill attaches a database, one runs SQL against it, one profiles any data file, and the rest handle documentation lookup, session memory, extensions, format conversion, spatial data and object storage.

The design idea worth stealing is the shared state file. Every skill reads and writes a single `state.sql` per project, holding ATTACH, USE and LOAD statements, secrets and macros, and any skill restores the session with `duckdb -init state.sql`. That is why `attach-db` can hand a schema to `query` without the user restating anything.

## Installation

The README installs the plugin from GitHub as a marketplace:

```
/plugin marketplace add duckdb/duckdb-skills
```

```
/plugin install duckdb-skills@duckdb-skills
```

Skills are then available as `/duckdb-skills:<skill-name>` in all later sessions. Updates take two steps, marketplace first:

```
/plugin marketplace update duckdb-skills
```

```
/plugin update duckdb-skills@duckdb-skills
```

Submission to the Anthropic marketplace is described in the README as coming soon, so the GitHub route is the one that works today. For a non-Claude agent, clone the repo and point the agent at `skills/*/SKILL.md`, which is how the README's own local development path works:

```bash
git clone https://github.com/duckdb/duckdb-skills.git
cd duckdb-skills
claude --plugin-dir .
```

DuckDB CLI must be installed. If it is not, the skills offer to install it through `install-duckdb`.

## What It Provides

Nine listings, all above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| query | 1,514 | SQL against attached databases or ad-hoc against files, accepting raw SQL or natural language questions in DuckDB's Friendly SQL dialect |
| duckdb-docs | 1,370 | Full-text search over DuckDB and DuckLake documentation and blog posts, run over HTTPS against hosted indexes with an optional local cache |
| read-file | 1,270 | Profiling CSV, JSON, Parquet, Avro, Excel, spatial, SQLite and notebook files locally or from S3, GCS, Azure or HTTPS through the read_any macro |
| attach-db | 1,078 | Attaching a database file, exploring its schema, tables, columns and row counts, and writing the state file other skills restore from |
| install-duckdb | 976 | Installing or updating extensions, including name@repo community syntax and an --update flag that also checks the CLI version |
| read-memories | 847 | Recovering decisions, patterns and open TODOs from past session logs, offloading large result sets to a temporary DuckDB file |
| convert-file | 822 | Format to format conversion across CSV, Parquet, JSON, Excel and GeoJSON, including binary outputs the agent cannot write natively |
| spatial | 758 | Spatial questions over coordinates, distances, containment and spatial joins, with Overture Maps data on S3 requiring no API keys |
| s3-explore | 742 | Listing and querying data on S3, Cloudflare R2, GCS, MinIO or any S3-compatible store without downloading it first |

No indexed listings fall below the threshold; all 9 appear above.

## Why This Matters for Hermes Agents

Most agents meet a CSV by loading it into pandas and hoping it fits in memory. DuckDB answers the same question with SQL, streams from disk, and reads Parquet and remote object storage natively, which changes the size of data an agent can reason over on a laptop.

The friendly SQL detail matters more than it sounds. DuckDB accepts `FROM sales LIMIT 10` and `FROM 'exports.csv' WHERE amount > 100`, so a natural-language question maps to a short query instead of a generated script with a parsing bug in it.

Session state is the second transferable pattern. A single append-only, idempotent `state.sql` means an attached database, a set of secrets and a few macros survive across skills and across conversations, so the agent does not re-derive context every turn.

The documentation skill closes the loop: when a query fails, the skill can search the DuckDB docs rather than guessing at syntax.

## Usage

| You say | What happens |
|---|---|
| "Attach my analytics database" | attach-db explores the schema and writes state.sql so later queries pick it up automatically |
| "What are the top customers by revenue?" | query turns the question into SQL against the attached database |
| "What is in this Parquet file?" | read-file detects the format, profiles the columns and suggests query for the follow-up |
| "What is in this bucket?" | s3-explore lists the remote prefix and previews the files without downloading them |
| "Turn these CSVs into Parquet" | convert-file rewrites the files in the target format |
| "How do I read a CSV with custom delimiters?" | duckdb-docs searches the hosted documentation index and returns the page |
| "Include the spatial extension" | install-duckdb installs or updates the named extension, with name@repo for community builds |

## Verification

Fetch one skill file and confirm the frontmatter and the Friendly SQL examples are there:

```bash
curl -fsSL https://raw.githubusercontent.com/duckdb/duckdb-skills/main/skills/query/SKILL.md | head -20
```

Then confirm the plugin is registered and the CLI is present:

```
/plugin
```

```bash
duckdb --version
```

Inside a session, `/duckdb-skills:query SELECT 42` is the skill's own smoke test, and it needs no database attached.

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| query | Pass | Pass | Pass |
| read-file | Pass | Pass | Warn |
| install-duckdb | Pass | Pass | Pass |
| convert-file | Pass | Pass | Pass |
| s3-explore | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified November 4, 2026: 9,377 combined installs across 9 indexed listings; 616 GitHub stars; MIT licence; last pushed 2026-04-23. Counts drift over time.
- The install route is a Claude Code plugin. Other agents have to load `skills/*/SKILL.md` from a clone, and the namespaced slash commands in the README apply to Claude Code only.
- `state.sql` holds ATTACH statements, secrets and macros in plain SQL inside the project or home directory. Treat it as a credential file and keep it out of version control.
- The README states the skills are tested on macOS and Linux, with Windows only partly supported because of shell commands and path handling.
- The README documents six of the nine indexed skills in its Skills section; convert-file, spatial and s3-explore are described in their own SKILL.md files, so read those before relying on the summaries above.
- read-memories searches past Claude Code session logs, which limits it to agents that store conversations the same way.

## Related

- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [AntV Chart Visualization Skills - Data to Charts](/hermes/skills/catalog/antvis-chart-visualization-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run attach-db once per project and keep the state file inside the repo directory, gitignored. The home directory option keeps the tree clean but hides the state from reviewers.
- Answer with a file path instead of a schema description. read-file and query both resolve paths, and a path cannot be misremembered the way a column list can.
- Reach for convert-file when you need Parquet for speed. A converted file makes later queries cheaper and removes the parsing step entirely.
- Let query fail before you write a script. The docs skill will usually find the syntax in one search, and a two-line query is easier to audit than generated Python.
- Treat s3-explore as read-only reconnaissance. It lists and previews remote data, so confirm credentials and bucket scope before pointing it at production storage.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
