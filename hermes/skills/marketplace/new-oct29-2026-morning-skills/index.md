---
title: "New Skills - October 29, 2026 Morning"
description: "Skills.sh sweep (Oct 29 morning): 886 skills scanned, 10 publisher guides for 109,244 combined installs across 14 indexed listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct29-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 29, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 886 unique skills with 0 failed queries: 86 NEW, 266 PARTIAL.

This fire drained the queue the Oct 28 evening fire left behind, and added one find the queue did not contain. The standing window was silent above the 1,000-install trigger for the twenty-first consecutive fire, its top row reading 328 installs, and every one of the 60 NEW sources sized below 2,000 combined once queried by publisher. The trending board served 600 entries across 73 sources with 71 already covered, and the board's own row sizes understated both exceptions: `whobot-ai/skills` read 2,221 installs and sizes at 3,078, still under the floor, while `jakubantalik/transitions.dev` read a single 517-install row and sizes at **34,026 combined installs across 5 listings**, a 66x multiple and this fire's largest convert.

Nine of the ten clusters the previous fire queued came through unchanged, and the tenth, `agents365-ai/drawio-skill`, was already documented as a roster row inside the 365 Skills guide because the publisher ships it from its own repository. Ten guides are documented below for **109,244 combined installs across 14 indexed listings**, from 34,026 at the top to 5,521 at the bottom.

Every guide was drafted against a pre-built pack holding the exact per-listing install figures, the cloned repository tree, the row-to-path map and the three-auditor verdicts sampled from skills.sh, then checked with three gates: the format gate, the pack cross-check at a per-guide threshold, and the frontmatter audit. All 30 gate runs passed, re-run by the orchestrator after an md5 comparison of the three canonical scripts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standing window) | 886 (0 failed queries) |
| NEW (not in catalog) | 86 |
| PARTIAL (source known, skill not cataloged) | 266 |
| Trending board | 600 entries / 73 sources, 2 uncovered |
| Above-floor finds in the standing window | 0 (top row 328) |
| NEW sources sized by publisher | 60 (largest 2,077, under the floor) |
| Queue carried from the previous fire | 10 above-floor clusters, 9 drained |
| New publisher guides | 10 (14 indexed listings, 109,244 combined installs) |
| Marketplace count | 1,217+ to 1,227+ |

## New Publisher Guides

### 1. Transitions.dev Skills (34,026 combined)

**Source:** [jakubantalik/transitions.dev](https://www.skills.sh/jakubantalik/transitions.dev), 5 indexed listings, top skill `transitions-dev` at 21,518; 5,888 stars; Transitions.dev License (GitHub reports NOASSERTION); branch main; 5 `SKILL.md` files across `agent/skill/`, `refine/.agents/skills/refine-live/` and three under `skills/`.

A library of crafted CSS transitions plus three agent skills that use it: `transitions-dev` for drop-in motion on modals, dropdowns, panels, toasts, accordions, tabs, tooltips, skeleton reveals and streaming text, `transitions-polish` for tuning motion that already exists onto a shared token scale, and `transitions-ui-generation` for a generation reveal built from a component's own structure. A `transitions-agent` CLI rounds it out.

Two facts shape the guide. The repository is the transitions.dev **website** as well as the skills, so a shallow clone brings HTML pages, a CNAME and a sitemap along with the markdown, which the Limitations section says plainly. And the licence is not OSI: what is free to read is not free to redistribute, and the repository sells paid tiers elsewhere on the same site. All five sampled listings Pass on Gen Agent Trust Hub and Socket, with a Snyk `W012` on `transitions-agent` alone.

### 2. NotebookLM (9,973 combined)

**Source:** [teng-lin/notebooklm-py](https://www.skills.sh/teng-lin/notebooklm-py), 1 indexed listing (`notebooklm`); 19,968 stars; MIT; branch main; a single `SKILL.md` at the repository root beside a full Python package.

An unofficial Python API and CLI for Google Gemini Notebook, wrapped in one agent-facing skill file. The skill is an operating contract rather than a tutorial: JSON discovery with retained UUIDs, notebook pinning on every scoped command, a unique profile per concurrent run, `source wait` before generation, artifact downloads pinned to an exact id, `--run-id` for overlapping deep research, and confirmation gates before anything destructive or generating.

The guide is direct about the boundary: the publisher is not Google, the endpoints are undocumented and can change without notice, and the tool signs in to a real Google account and stores bearer credentials on disk. That is the surface the two Warn verdicts land on.

### 3. PDF Converter (MinerU) (9,620 combined)

**Source:** [tanis90/pdf-converter-mineru](https://www.skills.sh/tanis90/pdf-converter-mineru), 1 indexed listing (`pdf-converter`); 55 stars; no license file at the repository root; branch main; a single `SKILL.md` and a 1.1 KB README.

A thin instruction file that has the agent call the MinerU Open API CLI: a no-auth quick mode up to 10 MB or 20 pages, a token mode up to 200 MB or 600 pages, output as markdown, JSON, HTML, LaTeX or DOCX, an OCR toggle for scans, batch mode and page-range naming that stops chunked extracts overwriting each other.

It is the weakest listing in this batch and the guide says so in four places: no license, 55 stars against 9,620 installs, last pushed May 2026, and both Gen Agent Trust Hub and Snyk returning Fail while Socket passes. The skill also uploads documents to a third-party service, which is the part to read before pointing it at anything confidential.

### 4. Unlazy (9,609 combined)

**Source:** [leonxlnx/unlazy](https://www.skills.sh/leonxlnx/unlazy), 1 indexed listing (`unlazy`); 4,168 stars; MIT; branch main; a root `SKILL.md` with `references/`, `scripts/`, `agents/` and `templates/` behind it.

Completion discipline for long work. The mechanism is a gate ledger, `GATES.md`, where every gate carries one observable outcome and a runnable `CHECK:` with an `EXPECT:` string, validated by a parser that rejects zero-gate or duplicate-id ledgers, with `--status` inspection that executes nothing, explicit `--approve` consent and `--reverify` for returned work. Around that sit the Depth Tree decomposition with per-leaf ledgers, rolling dispatch with ownership leases, a linter for mechanically weak gates and terminal abandonment handoffs that cannot print as success.

The security section is unusually concrete because the checker runs each `CHECK:` through a shell: approval is bound to the ledger, gate, command, directory, shell, timeout and `PATH`, but not to the scripts the command calls, so anyone who can edit a ledger can forge evidence. The guide turns that into the rule it is.

### 5. Groundcover CLI (9,602 combined)

**Source:** [paymog/groundcover-cli](https://www.skills.sh/paymog/groundcover-cli), 1 indexed listing (`groundcover-cli`); 1 star; MIT; branch main; one `SKILL.md` under `skills/` beside a Go CLI.

A Go CLI over the Groundcover observability APIs with a 512-line skill that teaches an agent to drive it: SDK-backed CRUD for dashboards, monitors, silences, notification routes, service accounts, ingestion keys, policies, synthetic checks and workflows, plus raw HAR-derived commands for logs, traces, metrics, Prometheus passthrough, Grafana dashboards, Kubernetes drilldowns and billing or RBAC reads.

The listing fails Gen Agent Trust Hub with Socket and Snyk both warning, and the guide leads with what that means here: installing it hands an agent a service-account key that can read production telemetry and delete monitors and policies in the same tenant. One star against 9,602 installs is recorded as a distribution fact, not an argument.

### 6. incident.io CLI (9,298 combined)

**Source:** [paymog/incidentio-cli](https://www.skills.sh/paymog/incidentio-cli), 1 indexed listing (`incidentio-cli`); 0 stars; no license file at the repository root; branch main; one `SKILL.md` under `skills/` beside a TypeScript CLI.

A CLI generated from incident.io's OpenAPI specifications, 324 commands deep, covering incidents, actions, follow-ups, attachments, alerts and routes, escalations and on-call schedules, catalog entries, custom fields, severities, heartbeats and status pages, with bracket query filters and JSON output built for `jq`.

This is the only listing in the batch that Snyk fails: `W007` and `W012`, insecure credential handling and an unverifiable external dependency, with Socket warning and Gen Agent Trust Hub passing. The W007 class is visible in the skill text itself, which has the agent run `auth set` with a live key or import a pasted cURL that carries dashboard session cookies. The guide says who should not use it yet.

### 7. Chrome DevTools AXI (7,072 combined)

**Source:** [kunchenguid/chrome-devtools-axi](https://www.skills.sh/kunchenguid/chrome-devtools-axi), 1 indexed listing (`chrome-devtools-axi`); 445 stars; MIT; branch main; one `SKILL.md` beside a TypeScript CLI with a 27-file vitest suite.

A compact CLI that wraps the Chrome DevTools Protocol for agents, with snapshot-first output that keeps responses small: navigation with `uid=` references, click and form fill with stale-reference checks, console and network capture, screenshots, device emulation, performance traces and Lighthouse.

The design decision worth reading is the refusal to hand an agent a raw protocol dump. The guide also traces where the browser context comes from, because the one Warn verdict sits on a bridge process that listens on loopback and, in auto-connect modes, drives a browser that keeps its saved passwords.

### 8. Playwright Skill (7,056 combined)

**Source:** [lackeyjb/playwright-skill](https://www.skills.sh/lackeyjb/playwright-skill), 1 indexed listing (`playwright-skill`); 3,250 stars; MIT; branch main; one `SKILL.md` under `skills/` plus a `.claude-plugin` manifest.

An agent writes and runs real Playwright programs rather than clicking through a wrapper: dev-server detection before a URL is guessed, reusable scripts kept in `PW_SCRIPT_DIR` when they should survive, a visible browser by default, viewport-specific screenshots, login flows, cookie-banner handling, CDP attach to an existing Chrome and a progressive-disclosure API reference.

It is a sibling of the TestDino Playwright guide already in the catalog and a different publisher, which the Related section makes explicit. The guide notes that `playwright` is declared as a caret range, so `npm ci` against the shipped lockfile is the reproducible install, and that the one Snyk `W011` warning is about fetching a browser build at setup and executing code written at runtime.

### 9. Elestio Skill (7,467 combined)

**Source:** [elestio/elestio-skill](https://www.skills.sh/elestio/elestio-skill), 1 indexed listing (`elestio`); 1 star; no license file at the repository root while the README says MIT; branch main; a root `SKILL.md` plus `scripts/`.

The vendor's own skill for its managed DevOps platform: deploy catalog software as an isolated VM, as a replicated cluster or as a pipeline on a shared CI/CD target, then manage projects, firewalls, SSL, SSH keys, volumes, backups, billing, audit logs and cluster failover. A 24-row table maps each CLI command to its MCP equivalent.

Gen Agent Trust Hub fails this listing and the guide does not soften it, because the blast radius is a deleted production database or an open firewall port rather than a bad paragraph. The README's installer pipes curl into bash and runs `rm -rf` on an existing skills directory, so the guide documents the manual copy route instead and recommends a throwaway project and a scoped token for first contact.

### 10. Autopilot (5,521 combined)

**Source:** [nick-vels/skills](https://www.skills.sh/nick-vels/skills), 1 indexed listing (`autopilot`); 564 stars; MIT; branch main; `skills/autopilot/SKILL.md` plus `docs/`, `tools/`, `tests/` and a `skills-lock.json`.

The cleanest verdict set in the batch: one listing, three auditors, three passes. Autopilot takes a dictated idea through eight stages, from a numbered requirement manifest with verbatim quotes through question rounds only on real forks, a spec, a wave-ordered ticket plan, one executor subagent per ticket with one commit each, targeted and whole-branch review, and blind acceptance from a clean clone, with four modes, three depth settings and a local dashboard.

What installs is markdown plus one standard-library Python script, `ap.py`, which runs git, serves the dashboard on loopback and makes exactly one outbound request for a version check that can be switched off. The guide reviews the local behaviour rather than the download surface, including the narrowed dev-server detection that once matched too broadly.
