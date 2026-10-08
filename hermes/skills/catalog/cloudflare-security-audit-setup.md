---
title: "Cloudflare Security Audit Skill - Agent Code Auditing Setup"
description: "Setup guide for cloudflare/security-audit-skill: Cloudflare's official security auditor skill - six-phase vulnerability hunting for AI coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cloudflare-security-audit-setup/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skill setup", "security", "audit", "cloudflare"]
---

# Cloudflare Security Audit Skill - Setup Guide

**Source:** [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) via [skills.sh](https://www.skills.sh/cloudflare/security-audit-skill/security-audit) (25.6K installs, first seen Jun 18, 2026; 26,403⭐ on GitHub, MIT LICENSE; last pushed Sep 14, 2026)
**Skill:** `security-audit` (single-skill repo; originally from `89jobrien/steve`, adapted and maintained by Cloudflare)
**Category:** Security / Code Auditing
**Quality Tier:** 🟢 Production (official Cloudflare publisher; battle-tested origin as the seed of Cloudflare's vulnerability discovery harness; MIT LICENSE; active development; Gen Agent Trust Hub Pass / Socket Pass / Snyk Warn - verified Oct 8, 2026)

The official Cloudflare skill that turns any coding agent into a security auditor. It orchestrates isolated agents through reconnaissance, coverage-led hunting, candidate validation, structured output, independent record verification, and target-neutral reporting. It seeded Cloudflare's vulnerability discovery harness, described in [Build your own vulnerability harness](https://blog.cloudflare.com/build-your-own-vulnerability-harness): the harness grew into a multi-stage, fleet-wide system, and this skill is the single-repo starting point it evolved from. The skill is agent-neutral (works with any agent platform) and MIT-licensed; per skills.sh it was originally from `89jobrien/steve` before Cloudflare adapted it.

---

## Installation

```bash
# Single skill install (this repo ships one skill)
npx skills add cloudflare/security-audit-skill --skill security-audit

# GitHub URL form, as shown in the skill README
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit

# User-level installation
npx skills add cloudflare/security-audit-skill --skill security-audit --global
```

This is a single skill, not a suite: there is no wildcard family install, just `security-audit`. Requirements: a coding agent with tool use and parallel sub-agents, Node.js for the zero-dependency validators, and (for full audits) an OS-enforced sandbox for target-controlled builds, tests, processes, browsers, emulators, fuzzers, and fixtures.

## The Six-Phase Workflow

| Phase | Output | What Happens |
|---|---|---|
| 1. Reconnaissance | `architecture.md`, `coverage-ledger.json` | Map architecture, trust boundaries, input surfaces, prior evidence, and deterministic coverage |
| 2. Coverage-led hunting | hunter records plus critic gap reports | Assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps |
| 3. Candidate validation | validated candidates | Give every unique candidate to a fresh verifier that tries to disprove it |
| 4. Structured output | `findings.json` validated against `report-schema.json` | Write `confirmed`, `needs_validation`, and `rejected` records |
| 5. Independent record verification | verified records | Fresh agents verify final source claims; material replacements receive another independent verifier |
| 6. Target-neutral reporting | `REPORT.md`, `FINDINGS-DETAIL.md`, `NEEDS-VALIDATION.md` | Derive reports from the verified records and the coverage ledger |

Helper scripts (zero-dependency, run with Node.js): `validate-coverage-ledger.cjs` runs after the ledger is created and after each later ledger update; `validate-findings.cjs` runs in Phase 4 and again after every Phase 5 replacement.

### Verdict Semantics

| Verdict | Meaning |
|---|---|
| `confirmed` | Complete source trace plus a bounded observed result |
| `needs_validation` | Exact unresolved fact; no severity attached |
| `rejected` | Candidate disproved during verification |

Multiple runs against the same repo are additive: prior ledgers and findings target gaps, changed source gets revalidated, and stale or unresolved work is never treated as covered.

### Operating Modes

| Mode | When It Applies | Behavior |
|---|---|---|
| Guidance (default) | Security questions and focused vulnerability work | Uses only the relevant parts of the skill; no automatic full workflow or artifact creation |
| Full audit | An explicit request to audit or pen-test a codebase | Runs the six-phase workflow and writes report artifacts; an unspecified output directory defaults to `~/security-audit-skill/<repo-name>/run-<N>` |

Full audit mode writes inside the target repository only when you explicitly select a directory that version control ignores.

Key files: `SKILL.md` (setup, core principles, anti-patterns) plus hunting-class references such as `RECONNAISSANCE.md`, `HUNTING.md`, `ATTACK-CLASSES.md`, `MEMORY-SAFETY-AND-BINARY.md`, `AI-AND-LLM.md` (prompt-injection and agent/tool hunting), `WEB-PROTOCOL-AND-AUTH.md`, `CLIENT-SIDE.md`, `SUPPLY-CHAIN-AND-RELEASE.md`, `CLOUD-AND-DEPLOYMENT.md`, and `VALIDATION-AND-REPORTING.md`.

## Why This Matters for Hermes Agents

Agents shipping real code need a structured, evidence-first security review loop, not ad hoc pattern matching. This skill is the public distillation of a production vulnerability discovery harness that grew fleet-wide at Cloudflare, packaging the expensive lessons (isolated hunters, adversarial verification, auditable coverage) into a workflow any agent can run on any codebase. It is agent-neutral and MIT-licensed, so it drops into a Hermes fleet with no platform lock-in.

## Usage

Start the agent in (or pointed at) the codebase you want audited, then trigger the skill:

```text
security audit this codebase
find security vulnerabilities in ./src
do a security review, output to ~/audits/my-project
```

The skill activates automatically on matching requests (security audit, find vulnerabilities, pen-test the code, security review). Focused security questions stay in guidance mode; a direct audit or pen-test request switches to full audit mode. Re-run against the same repo to grow coverage - Cloudflare notes that in its test runs a single run found roughly half of the vulnerabilities that repeated runs found in total.

## Verification

```bash
# Confirm the skill is installed locally
hermes skills list | grep security-audit

# Confirm the validators are present in the skill directory
ls validate-coverage-ledger.cjs validate-findings.cjs
```

Smoke test: point the agent at a small repo and ask "security audit this codebase". In full audit mode it should create `coverage-ledger.json` during reconnaissance and later produce `findings.json`, `REPORT.md`, `FINDINGS-DETAIL.md`, and `NEEDS-VALIDATION.md` in the output directory. Cross-check install counts and per-skill verdicts on the skills.sh page linked above.

## Security

skills.sh security verdicts for `security-audit` (verified Oct 8, 2026) - check the skill's security page on skills.sh before production use:

| Check | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Pass |
| Snyk | Warn |

Note: the skill writes files, and in full audit mode may execute target-controlled code paths (builds, tests, processes, browsers, emulators, fuzzers, fixtures). Run it on a branch or worktree, keep output out of version control, and use an OS-enforced sandbox before executing target code.

## Limitations

- Two modes matter: guidance mode (the default) does not run the full workflow or create artifacts. Full audit mode must be explicitly requested.
- `needs_validation` is not a severity level. It records an exact unresolved fact for follow-up, so it should not be triaged as a reported vulnerability.
- Full audit mode writes report artifacts and may execute target code paths. Plan for a branch or worktree, an ignored or external output directory, and the README's sandbox requirements (no external networking, sanitized allowlisted environment, resource limits, scratch-only writes).
- Runtime is heavyweight by design: a required coding agent with parallel sub-agents plus Node.js for the validators. This is an audit harness, not a quick linter.
- Snapshot data, verified Oct 8, 2026: 25.6K skills.sh installs; 26,403 GitHub stars; MIT LICENSE; last pushed Sep 14, 2026. Counts will drift over time.
- Authorship note: per the skills.sh listing, the skill was originated by 89jobrien as `89jobrien/steve` and adapted by Cloudflare; this catalog entry documents the Cloudflare-maintained version.

## Related

- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup)
- [trailofbits/skills - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/trailofbits-security-setup)
- [CTF Security Skills - Offensive Security Suite Setup](/hermes/skills/catalog/ctf-security-skills-setup)
- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run a guidance-mode focused pass on your highest-risk area (auth, input parsing, agent tool handling) before committing to a full six-phase audit - it is fast and often surfaces where the real risk lives.
- Keep audit output out of version control: choose an ignored directory or a path outside the repo, and run on a branch or worktree since artifacts land on disk.
- Re-run against the same repo instead of treating one pass as complete. Runs are additive: prior ledgers target gaps and revalidate changed source.
- Do not skip the validators: `validate-coverage-ledger.cjs` after each ledger update and `validate-findings.cjs` after Phase 5 replacements keep artifacts schema-clean.
- Treat `needs_validation` entries as a follow-up queue of exact unresolved facts; clearing them on the next run is where repeated audits earn their keep.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
