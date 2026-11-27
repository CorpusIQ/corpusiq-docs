---
title: "Turso Skills - SQLite-Compatible Database Engineering"
description: "tursodatabase/turso: 13.4K combined installs. Fourteen skills for engineering the SQLite-compatible Turso database in Rust."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/turso-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "turso", "sqlite", "database"]
---

# Turso Skills - Setup Guide

**Source:** [tursodatabase/turso](https://www.skills.sh/tursodatabase/turso) via skills.sh - 13.4K combined installs across 14 indexed listings; first documented 2026-11-27 (morning sweep)

**GitHub:** [tursodatabase/turso](https://github.com/tursodatabase/turso) - 25,383 stars, MIT, branch main, last pushed 2026-11-27; nine skill directories under `.claude/skills/<name>/SKILL.md`, with five more indexed listings carrying no SKILL.md in the current tree.

**Category:** Database engineering skills for the Turso engine: SQLite compatibility, MVCC, CDC, async I/O, testing and fuzzing

**Quality Tier:** 🟢 Green - all fourteen sampled listings pass the Gen Agent Trust Hub, Socket and Snyk.

Turso is a SQL database written in Rust that is SQLite-compatible and now also speaks Postgres through a second, experimental frontend; the README describes it as aiming to be for databases what LLVM is to compilers, one core with many SQL frontends compiled onto it. The fourteen skills in the skills.sh index are engineering skills for that engine itself, not user-facing database skills: they document how to change MVCC, CDC, the async I/O model and the storage format correctly.

The skills ship inside the repository under `.claude/skills/`, where Claude Code discovers them automatically when the repo is checked out. Nine of the fourteen indexed names have a SKILL.md in the tree; the other five (code-quality, index-knowledge, storage-format, pr-workflow and allocator-migration) carry install counts but no counterpart file, which is index-versus-tree drift to be aware of before relying on them.

## Installation

This repository is the Turso database itself, and its agent skills ship inside it rather than through a separate registry command. The README does not document a skills.sh CLI or Hermes install route for them; the nine skill directories under `.claude/skills/` load automatically in Claude Code when the repo is present.

The manual route is a clone, after which the skills are already in place:

```bash
git clone https://github.com/tursodatabase/turso.git
ls turso/.claude/skills/
```

The database and its CLI install separately through the scripted installer the README documents:

```bash
curl --proto '=https' --tlsv1.2 -LsSf \
  https://github.com/tursodatabase/turso/releases/latest/download/turso_cli-installer.sh | sh
```

The CLI also runs as an MCP server so an agent can query a database directly:

```bash
tursodb your_database.db --mcp
```

Claude Code users register that server with the built-in `claude mcp add` command, passing the database path and the `--mcp` flag. Language bindings install the engine through their own package managers, as the README documents (`cargo add turso`, `npm i @tursodatabase/database`, `uv pip install pyturso`, `go get turso.tech/database/tursogo`).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| code-quality | 1,790 | Correctness rules, Rust patterns and comment conventions, with explicit advice against over-engineering. |
| index-knowledge | 1,327 | Generating a hierarchical AGENTS.md knowledge base, with a root file plus complexity-scored subdirectory documentation. |
| debugging | 1,316 | Debug tursodb: bytecode comparison, logging, ThreadSanitizer, deterministic simulation, stack usage and corruption analysis. |
| async-io-model | 1,275 | Code that returns IOResult or keeps I/O state across yields: state machines, re-entrancy, CompletionGroup. |
| testing | 1,266 | Write and run tests: .sqltest files, Rust integration tests, converting .test files to .sqltest. |
| storage-format | 1,260 | The SQLite file format as tursodb implements it: B-trees, pages, cells, overflow and the freelist. |
| pr-workflow | 1,242 | Commit, formatting, CI, dependency and security conventions for contributing. |
| transaction-correctness | 1,241 | WAL mechanics, checkpointing, concurrency rules and recovery in tursodb. |
| differential-fuzzer | 1,221 | Run the differential fuzzer comparing Turso against SQLite on generated SQL, reproduce and minimize failures. |
| mvcc | 1,220 | MVCC journal mode: snapshot isolation, row versions, logical log, checkpoint and GC settings, how to test. |

The remaining 4 indexed listings range from 15 to 154 installs.

Four of the ten listings above (code-quality, index-knowledge, storage-format and pr-workflow) carry skills.sh install counts but have no SKILL.md in the current repo tree; their Use For cells come from the description on each skills.sh listing page rather than from a file in the repository. The four listings below the cut-off are cdc (154), memory-benchmark (62), yield-injections (43) and allocator-migration (15); the first three have SKILL.md files in the tree and allocator-migration does not.

## Why This Matters for Hermes Agents

This suite is a different shape from the catalog norm: it is an engine's own engineering playbook, not a set of user-facing integrations. The skills encode the invariants a contributor must respect, such as how MVCC snapshot isolation works, how the async I/O model survives yields, and how the WAL recovers, which is exactly the knowledge an agent lacks when it first opens a 25,000-star Rust database. For builders working on a fork or a client of Turso, that is far more useful than a generic SQL cheat sheet.

The discipline of the skills is also the point. Several target failure classes rather than features: the differential fuzzer compares Turso against SQLite on generated SQL, yield-injections covers synthetic failure injection at resumable state-machine boundaries, and debugging covers deterministic simulation and corruption analysis. That orientation, writing down how to break and then verify the engine, is a pattern worth copying for any systems-level project.

The setup is low-ceremony for Claude Code: the skills are plain files under `.claude/skills/`, so they load from a clone with no registry and no package step. The tradeoff is that they are not individually installable through skills.sh in the README's documentation, so a Hermes-style runtime must either copy the directories or point at them in place.

The index-versus-tree drift is the one thing to plan around. Five of the fourteen indexed names have no SKILL.md in the tree, so an agent told to load a skill by name may open a path that does not exist; route on the nine in-tree names and treat the rest as index-only.

## Usage

| You say | What happens |
|---|---|
| "How does the WAL recover after a crash?" | Loads transaction-correctness for WAL mechanics, checkpointing and recovery rules. |
| "Why did this query behave differently under concurrency?" | Uses mvcc for snapshot isolation, row versions and checkpoint/GC settings. |
| "Add CDC to this change" | Loads cdc for the capture_data_changes_conn pragma, schema versions and how the sync engine reads rows. |
| "Find where memory is being allocated in this SQL workload" | Uses memory-benchmark with the memory-benchmark crate and the dhat heap profiler. |
| "Run the fuzzer and reproduce a failure" | Uses differential-fuzzer to compare Turso against SQLite and minimize the failing SQL. |
| "Write a test for this .test file" | Uses testing to convert a .test file to .sqltest or write a Rust integration test. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/tursodatabase/turso/main/.claude/skills/debugging/SKILL.md
```

After a clone, confirm the skill directories are present and that nine exist:

```bash
git clone --depth 1 https://github.com/tursodatabase/turso.git /tmp/turso
ls -d /tmp/turso/.claude/skills/*/ | wc -l
head -3 /tmp/turso/.claude/skills/debugging/SKILL.md
```

The count should print 9, and head should show the debugging skill's frontmatter. Five indexed listings (code-quality, index-knowledge, storage-format, pr-workflow, allocator-migration) have no SKILL.md in the tree, so do not expect fourteen directories.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| code-quality | Pass | Pass | Pass |
| index-knowledge | Pass | Pass | Pass |
| debugging | Pass | Pass | Pass |
| async-io-model | Pass | Pass | Pass |
| testing | Pass | Pass | Pass |
| storage-format | Pass | Pass | Pass |
| pr-workflow | Pass | Pass | Pass |
| transaction-correctness | Pass | Pass | Pass |
| differential-fuzzer | Pass | Pass | Pass |
| mvcc | Pass | Pass | Pass |
| cdc | Pass | Pass | Pass |
| memory-benchmark | Pass | Pass | Pass |
| yield-injections | Pass | Pass | Pass |
| allocator-migration | Pass | Pass | Pass |

This guide is Green because all fourteen sampled listings pass the Gen Agent Trust Hub, Socket and Snyk. The skills themselves are Markdown under `.claude/skills/`; the repository is a Rust database with an `install.sh`-style CLI installer and an MCP server mode, so the skills.sh verdicts cover the skill files specifically, not the engine, which should be audited on its own before production use.

## Limitations

- Snapshot data, verified 2026-11-27: 13,432 combined installs across 14 indexed listings; 25,383 GitHub stars; MIT; last pushed 2026-11-27. Counts drift over time.
- The install index outruns the tree: five listings (code-quality, index-knowledge, storage-format, pr-workflow, allocator-migration) carry install counts but have no SKILL.md in the current tree.
- The README does not document a skills.sh CLI or Hermes install route; the skills are embedded for Claude Code discovery and are copied manually for other runtimes.
- The skills describe the Turso engine internals, so most of them are only useful when working on the database itself or a close client, not for end-user querying.
- The Postgres frontend is experimental, and the project has not reached 1.0; the README recommends independent backups until then.
- These verdicts cover the Markdown skill files; the Rust engine and the CLI installer are separate surfaces to review independently.

## Related

- [MotherDuck Skills - Analytics Apps on DuckDB Data](/hermes/skills/catalog/motherduckdb-agent-skills-setup)
- [Neo4j Skills - Graph Database Agent Suite](/hermes/skills/catalog/neo4j-skills-setup)
- [HelixDB Skills - Query, Memory, and Foundry MCP Setup](/hermes/skills/catalog/helixdb-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Route on the nine in-tree skill names; five indexed names have no SKILL.md, so a name-only lookup can point at a missing file.
- Use the MCP server mode for query work and the skills for engine work: `tursodb your_database.db --mcp` gives an agent live query access, while the skills teach it how the engine behaves.
- Read debugging and differential-fuzzer before touching storage or concurrency code; they document how the project verifies its own correctness.
- Copy the whole `.claude/skills/<name>/` directory, since the debugging skill carries a `references/` and a `scripts/` tree beside the SKILL.md.
- Keep the experimental-Postgres framing in mind: skills describe SQLite-frontend behavior, and Postgres compatibility is additive and still evolving.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
