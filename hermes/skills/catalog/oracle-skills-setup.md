---
title: "Oracle Skills - Database, OCI and APEX Guidance"
description: "oracle/skills on skills.sh: 6.0K combined installs across 7 listings; source-backed Oracle Database, OCI, APEX, Fusion and GraalVM guidance."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/oracle-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "oracle", "database", "cloud infrastructure"]
---

# Oracle Skills - Setup Guide

**Source:** [oracle/skills](https://www.skills.sh/oracle/skills) via skills.sh - 6.0K combined installs across 7 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep, first documentation)
**GitHub:** 914 stars, Universal Permissive License 1.0 in LICENSE.txt, last pushed 2026-11-02, 30 SKILL.md directories across five domain trees (db, oci, apex, graal, fusion)
**Category:** Oracle estate for agents: Database, OCI, APEX, Fusion applications and GraalVM with source-backed guidance
**Quality Tier:** 🟡 Caution - Socket reports Warn on the db audit, and the licence is Oracle's own UPL 1.0 in LICENSE.txt rather than a standard MIT text; 914 stars.

Oracle Skills is Oracle's own repository, and the README states the ambition plainly: "give developers and agents a single place to find source-backed Oracle guidance across Oracle Database, Oracle Cloud Infrastructure, GraalVM, Oracle Fusion, Oracle APEX, and future domains." The design is a set of root-level domain directories, each an entry point with a routing table that sends the agent to the smallest file that answers the question. The README's stated goal is that each domain can evolve its own taxonomy without breaking repo-wide consistency.

Depth is uneven and that is visible in the tree. `db/` is the deep end, with categories for admin, appdev, architecture, containers, design, devops, features, frameworks, migrations, monitoring, ORDS, performance, PL/SQL, security, SQL development, SQLcl and VecDB. `oci/` carries Functions deployment and troubleshooting, OKE cluster generation and remediation, IoT Platform digital twins, Enterprise AI, and four Terraform modules under a landing-zone directory. `apex/` routes into versioned APEXlang sets for APEX 26.1 and 26.2, and `graal/` covers Native Image. `fusion/` is a placeholder with a single SKILL.md.

## Installation

The README installs one domain at a time by appending the root-level domain directory to the repository name:

```bash
npx skills add oracle/skills/db
npx skills add oracle/skills/oci
npx skills add oracle/skills/graal
```

The same repository ships as a Claude Code plugin marketplace, with each domain folder published as its own plugin:

```bash
# Register this repo as a marketplace
/plugin marketplace add oracle/skills

# Install one or more domain plugins
/plugin install db@oracle-skills
/plugin install graal@oracle-skills
```

If you already cloned the repository, the README points the marketplace at the local path instead:

```bash
/plugin marketplace add ./
```

Enabled plugins are tracked in `.claude/settings.json` under `enabledPlugins`, and `/plugin` browses and toggles them at any time.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| db | 2,982 | Oracle Database work: SQL and PL/SQL authoring and review, SQLcl, ORDS, VecDB, tuning, security, migrations and agent-safe operations |
| apex | 1,618 | Oracle APEX application development, routing into the versioned APEXlang sets for APEX 26.1 and 26.2 |
| oci | 528 | OCI design and operations: OKE clusters, Functions, IoT Platform, Terraform modules for security zones, IAM, networking and Exadata, plus Enterprise AI |

The remaining 4 indexed listings range from 46 to 353 installs: graal (353), oracle-db-skills (288), fusion (163) and apexlang (46). oracle-db-skills carries an install count but has no matching directory in the current tree, and fusion is a placeholder that holds one SKILL.md.

## Why This Matters for Hermes Agents

Oracle guidance is where general model knowledge ages fastest. The difference between an `AUTHID CURRENT_USER` and an invoker-rights package, between `DBMS_VECTOR` and a vector index created through the Python SDK, or between a 19c and a 23ai multitenant layout is exactly the kind of detail a model will approximate if nothing corrects it. This repository answers with Oracle's own text, and the `oci` SKILL.md adds a rule the vendor wrote rather than one an operator guessed: prefer official documentation and live read-only discovery before making design or remediation recommendations.

The domain gateways change how an agent behaves rather than what it knows. The `oci` SKILL.md tells the agent to ask before any command that creates, updates, deletes, restarts, scales or drains a resource, and to keep OCI-owned design decisions in that domain while routing database-owned SQL and vector implementation to `db/features/`. That is an escalation policy written by the vendor, not a house rule added afterwards.

The APEXlang branch is the most agent-shaped part of the tree. A versioned set exists for each of APEX 26.1 and 26.2, with separate skills for compiling, deploying, inventorying and shipping example applications, and 26.1 additionally carrying a generation skill. Real example applications are shipped as complete source trees to use as authoring evidence. An agent asked to build an APEX page has a compiler contract and a reference application instead of a blank editor.

For a Hermes agent the practical gain is scope discipline. The routing table means a question about OKE node pools opens a handful of service files, and the OCI Terraform modules are constrained generators rather than free-form advice. That is the difference between an agent that writes plausible cloud configuration and one that writes configuration you can plan against.

## Usage

| You say | What happens |
|---|---|
| "Review this PL/SQL package for injection risk" | The db skill pulls the security and PL/SQL categories and reviews against Oracle's guidance |
| "Why is this query doing a full scan?" | db performance material covers optimizer plans, indexes, AWR and ASH |
| "Write a Terraform module for an OCI VCN" | oci routes to the constrained networking generator instead of free-form HCL |
| "My OKE pods cannot pull images from OCIR" | oci troubleshooting covers Workload Identity, image pulls and node pool configuration |
| "Generate an APEX 26.2 app from this APEXlang tree" | apex routes to the 26.2 set and the compile and deploy skills |
| "Build this Java service as a native image" | graal covers native-image CLI, Maven and Gradle Native Build Tools, and reachability metadata |
| "Deploy a function and work out why it fails" | oci functions deploy and troubleshoot skills, diagnosis first |

## Verification

Confirm the domain index the installer pulls before trusting the tree:

```bash
curl -fsSL https://raw.githubusercontent.com/oracle/skills/main/db/SKILL.md | head -3
```

It should open with a `name: db` frontmatter block and a description naming SQL, PL/SQL, SQLcl, ORDS and VecDB. Then confirm the marketplace manifest still publishes the domain plugins:

```bash
curl -fsSL https://raw.githubusercontent.com/oracle/skills/main/.claude-plugin/marketplace.json | head -12
```

For a plugin install, open `/plugin` in Claude Code and check that the domains you asked for are enabled, or read the `enabledPlugins` block in `~/.claude/settings.json`. Note that this repository uses `main`, so every raw URL above depends on that branch.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| db | Pass | Warn | Pass |
| apex | Pass | Pass | Pass |
| graal | Pass | Pass | Pass |
| fusion | Pass | Pass | Pass |
| apexlang | Pass | Pass | Pass |

The repository ships a SECURITY.md. The tree is markdown and reference material, with a few helper scripts under `oci/iot-platform/scripts` and `oci/oke`, so read those before running them against a live tenancy. The `oci` domain's own instruction to ask before mutating commands is the control that matters in practice, because a skill cannot tell a sandbox tenancy from a production one.

## Limitations

- Snapshot data, verified 2026-11-05: 5,978 combined installs across 7 indexed listings; 914 GitHub stars; Universal Permissive License 1.0 in LICENSE.txt; last pushed 2026-11-02. Counts drift over time.
- The licence is Oracle's Universal Permissive License 1.0, not MIT. It is permissive, but the text in LICENSE.txt is what governs redistribution, so read it rather than assuming a standard OSI default.
- The install index outruns the tree: oracle-db-skills carries 288 installs and has no matching directory in the current tree, so treat it as an index artifact rather than a fourth database skill.
- `fusion/` is a placeholder with one SKILL.md and no content behind it. Any Fusion question lands on an empty domain today.
- The install unit is the whole domain directory. Installing `db` brings every category file to disk; the routing table tells the agent what to open, but nothing prunes the rest.
- APEXlang is duplicated per APEX version, so the apex tree carries parallel compile, deploy, example-application and inventory skills that differ by target version, with a generation skill present for 26.1 only. Check the version before following an instruction.

## Related

- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)
- [ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup)
- [PlanetScale Database Skills - MySQL & Postgres](/hermes/skills/catalog/planetscale-database-skills-setup)

## Pro Tips

- Install the domain, not the repository. `oracle/skills/db` keeps the OCI and GraalVM trees out of the context a SQL question needs.
- Say which Oracle version you are on. The multitenant, vector and APEX material is version-sensitive and the answer changes with it.
- Ask for the routing table first when a question crosses domains. It is one file and it names the specific file each sub-question needs.
- Treat mutating OCI commands as a separate approval. The `oci` skill asks before create, delete, restart and scale operations; keep that behavior in your harness instead of prompting past it.
- Use the APEXlang example applications as evidence, not as templates. They are complete source trees from real apps, which makes them good references and poor scaffolding.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
