---
title: "Rust Skills - Rust Engineering Skills Setup Guide"
description: "full-stack-skills/rust-skills: 35 Rust engineering skills for AI coding agents - 4.9K combined installs for testing, Cargo, concurrency and web."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/full-stack-skills-rust-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "rust", "cargo", "concurrency"]
---

# Rust Skills - Rust Engineering Skills Setup Guide

**Source:** [full-stack-skills/rust-skills](https://www.skills.sh/full-stack-skills/rust-skills) via skills.sh - 4.9K combined installs across 35 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [full-stack-skills/rust-skills](https://github.com/full-stack-skills/rust-skills) - 16 stars, Apache-2.0 license, main branch, last pushed Sep 23, 2026; 29 skills under `skills/<name>/SKILL.md` plus agent wrapper trees (`.agents`, `.kimi-code`, `.zcode`, `.claude-plugin`) and an `openspec/` layer.
**Category:** Rust Engineering
**Quality Tier:** 🟠 Orange - two of 20 sampled skills hold a Fail on Gen Agent Trust Hub (rust-performance, rust-dependencies) and two a Warn on Snyk (rust-code-review, rust-crate-discovery).

`full-stack-skills` is a Rust engineering skill set built for AI coding agents, not a Rust crate. The `rust-skills` repository packages validated, progressively loaded skills that teach agents to write idiomatic Rust across the language, toolchain and ecosystem: the standard library, Cargo, async and concurrency, testing, unsafe and FFI, web services, embedded, and macros. Each skill ships a SKILL.md with trigger metadata and task routing, plus offline references and compilable golden examples, so an agent reads source material instead of hallucinating API or crate names.

The repository organizes 29 skills under a canonical `skills/` tree, with the four openspec workflow skills duplicated into `.agents`, `.kimi-code` and `.zcode` wrapper trees for several agent layouts. It installs through the `skills` CLI in the Agent Skills format. The skills are layered from core language semantics (`rust-stable`) outward through design, engineering, domain and quality gates, and each routes related questions to the right sibling instead of over-answering. First seen in the Nov 20, 2026 evening sweep.

## Installation

```bash
npx skills add full-stack-skills/rust-skills --list
npx skills add full-stack-skills/rust-skills
```

Install one skill for the current project without prompts, or everything for all detected agents:

```bash
npx skills add full-stack-skills/rust-skills --skill rust-web --yes
npx skills add full-stack-skills/rust-skills --all
npx skills add full-stack-skills/rust-skills --global --all
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| rust-testing | 211 | unit, integration, doctest, property, fuzz, benchmark and concurrency test strategies |
| rust-performance | 198 | measure, profile and regression-test latency, throughput, memory, size and compile time |
| rust-style-clippy | 193 | rustfmt, Clippy lints, Edition migrations, diagnostics and API Guidelines lint mapping |
| rust-concurrency | 191 | threads, Send/Sync, Tokio/Rayon, locks, channels, backpressure and Loom model tests |
| rust-code-review | 183 | review Rust diffs and PRs for safety, error semantics, cloning, lock scope and API compatibility |
| rust-workspace | 176 | crate and workspace topology, dependency DAGs and crate-boundary decisions |
| rust-cargo-build | 176 | Cargo manifests, features, profiles, build scripts, cross-compilation and publishing |
| rust-api-design | 171 | Rust API Guidelines naming, interop traits, type safety and future-proofing |
| rust-stable | 166 | ownership, borrowing, lifetimes, traits, generics and Edition differences |
| rust-observability | 163 | tracing, structured logs, metrics, OpenTelemetry context and runtime diagnostics |
| rust-module-layout | 163 | in-crate src/ layout, mod declarations, visibility and re-exports |
| rust-unsafe-ffi | 162 | unsafe Rust, raw pointers, FFI boundaries, Pin and Miri validation |
| rust-dependencies | 159 | dependency governance with cargo-deny, cargo-audit, feature minimization and supply-chain policy |
| rust-http-client | 158 | reqwest/hyper clients, TLS and proxy, retries, timeouts and SSRF controls |
| rust-database | 156 | SQLx, Diesel and SeaORM, migrations, transactions, pools and real-database tests |
| rust-web-security | 153 | threat modeling, auth, authorization, sessions, tokens, CSRF, CORS and secrets |
| rust-web | 152 | axum and Actix Web services, routing, middleware, error mapping and shutdown |
| rust-semver | 152 | breaking-change classification, cargo-semver-checks and workspace publishing |
| rust-documentation | 152 | rustdoc, doctests, mdBook guides, docs.rs readiness and documentation CI |

The remaining 16 indexed listings range from 2 to 147 installs.

## Why This Matters for Hermes Agents

The hardest part of generating Rust with an agent is the borrow checker plus the toolchain: ownership, lifetimes and Send/Sync violations fail to compile in ways that are hard to debug without the right mental model, and Cargo, Clippy and semver have their own idioms. These skills give an agent that model, layered so it loads only what a task needs: rust-stable for language semantics, rust-api-design for idiomatic public APIs, rust-workspace and rust-module-layout for project structure, and rust-testing plus rust-performance for proof that the code works and stays fast. The quality-gate pair, rust-code-review and rust-style-clippy, turns reviews into checklist-driven passes over safety, error semantics, allocations and API compatibility. For builders shipping services, rust-web, rust-web-security, rust-http-client and rust-database cover the server, its security controls, outbound calls and data layer, while rust-unsafe-ffi and rust-concurrency handle the lower-level and parallel parts. Because every skill carries offline references and compilable golden examples, an agent verifies against real code instead of inventing crate or trait names.

## Usage

| You say | What happens |
|---|---|
| Review this Rust PR for safety and API issues | Applies the code-review checklist over correctness, error semantics, allocations and lock scope |
| Why will not this code compile | Diagnoses the ownership, borrowing or lifetime error against stable Rust semantics |
| Design a public API for this crate | Applies the Rust API Guidelines on naming, interop traits, type safety and future-proofing |
| Add a retrying HTTP client to this service | Configures reqwest/hyper with TLS, timeouts, retries and SSRF controls |
| Split this crate into a workspace | Derives crate boundaries and workspace layout from the project scale |
| Prove this fix is not a performance regression | Runs Criterion benchmarks and profiles CPU, memory and compile time |
| Migrate this Java service to Rust | Runs the evidence-driven Java-to-Rust migration workflow with parity audits |

## Verification

```bash
# after install, confirm the skills land in the project skills directory
npx skills add full-stack-skills/rust-skills --list
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/full-stack-skills/rust-skills/main/skills/rust-testing/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. Each skill lives at `skills/<name>/SKILL.md` on the main branch, so the 29 in-tree skills install as plain directories under the project or user skills path.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rust-testing | Pass | Pass | Pass |
| rust-performance | Fail | Pass | Pass |
| rust-style-clippy | Pass | Pass | Pass |
| rust-concurrency | Pass | Pass | Pass |
| rust-code-review | Pass | Pass | Warn |
| rust-workspace | Pass | Pass | Pass |
| rust-cargo-build | Pass | Pass | Pass |
| rust-api-design | Pass | Pass | Pass |
| rust-stable | Pass | Pass | Pass |
| rust-observability | Pass | Pass | Pass |
| rust-module-layout | Pass | Pass | Pass |
| rust-unsafe-ffi | Pass | Pass | Pass |
| rust-dependencies | Fail | Pass | Pass |
| rust-http-client | Pass | Pass | Pass |
| rust-database | Pass | Pass | Pass |
| rust-web-security | Pass | Pass | Pass |
| rust-web | Pass | Pass | Pass |
| rust-semver | Pass | Pass | Pass |
| rust-documentation | Pass | Pass | Pass |
| rust-crate-discovery | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified Nov 20, 2026: 4,893 combined installs across 35 indexed listings; 16 GitHub stars; Apache-2.0 license; last pushed Sep 23, 2026. Counts drift over time.
- Small publisher: 16 stars and 4.9K combined installs mean modest community scrutiny compared with larger Rust tooling, so review each skill before trusting it in production.
- Version grounding: the `rust-stable` entry skill is grounded in Rust 1.97.1 and requires agents to check the project's actual toolchain and MSRV before using version-sensitive APIs, and some golden examples are version-locked (UniFFI 0.32.0, lombok-macros 2.0.32) with one Clippy rule targeting Rust 1.81+.
- The index outruns the tree: 35 indexed listings against 29 in-tree skills, the difference being four openspec workflow skills that live only in the wrapper trees plus two legacy listings (rust-1.93, rust-project-structure) with no current directory; rust-1.93 was replaced by rust-stable.
- Two of the 20 sampled skills carry a Fail on Gen Agent Trust Hub and two a Warn on Snyk, so treat the suite's security posture as mixed rather than clean.

## Related

- [Code Review Skill - Review Workflow Setup](/hermes/skills/catalog/code-review-skill-setup)
- [Security and Hardening - Agent Security Setup](/hermes/skills/catalog/security-and-hardening-setup)
- [GitHub Code Review - PR Review Setup](/hermes/skills/catalog/github-code-review-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with rust-stable for language semantics and let it route specialized questions to the right sibling skill.
- Install only the skills your stack needs with --skill selectors; --all pulls the whole suite including migration and embedded skills you may not use.
- Run rust-style-clippy and rust-code-review as CI quality gates so lint and review pass before merge.
- Check the project toolchain and MSRV before trusting version-sensitive guidance, since rust-stable is grounded in Rust 1.97.1.
- Read a skill's references/ folder when the SKILL.md instruction is too compressed; the golden examples compile the idioms.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
