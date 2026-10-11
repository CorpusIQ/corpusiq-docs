---
title: "Ghost Security Skills - AppSec Agent Plugin Setup"
description: "Setup guide for ghostsecurity/skills - 28.0K combined installs. AppSec plugin suite: secret, dependency, and code scanning inside the agent workflow."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ghostsecurity-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "appsec", "security scanning", "devsecops"]
---

# Ghost Security Skills - Setup Guide

**Source:** [ghostsecurity/skills](https://www.skills.sh/ghostsecurity/skills) via skills.sh - 28.0K combined installs across 8 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [ghostsecurity/skills](https://github.com/ghostsecurity/skills) (409 stars, Apache-2.0 license; pushed Sep 28, 2026; `plugins/<plugin>/skills/<name>/SKILL.md` layout)
**Category:** Application Security / DevSecOps
**Quality Tier:** 🟡 Beta - company-backed (Ghost Security); Apache-2.0; mixed sampled verdicts (Socket Warn) - see Security

Ghost Security, an AppSec vendor, publishes this Claude Code plugin marketplace with two plugins: `ghost` (the AppSec skill set) and `exo` (workflow orchestration on the vendor's platform). The AppSec plugin wraps four deterministic engines in an AI skills layer: Poltergeist (secret scanner with dual-engine pattern matching and entropy analysis), Wraith (dependency scanner powered by the OSV database), Reaper (MITM HTTPS proxy for live vulnerability validation), and Exorcist (AI-powered code analysis covering 102 vulnerability types). The flagship listing, `ghost-scan-code`, sits at 4,860 installs, and all eight indexed listings are above 685.

The architecture the README stresses: real tools produce real data, and AI adds judgment on top. Pattern matches, CVE lookups, and traffic captures stay deterministic and auditable; the skills then assess exploitability and return findings with remediation guidance the agent can apply. The skills follow a find, validate, fix loop, results are cached on your machine, and the underlying tools can also be used standalone.

---

## Installation

Claude Code plugin marketplace:

```bash
claude plugin marketplace add ghostsecurity/skills
claude plugin install ghost@ghost-security
claude plugin install exo@ghost-security
```

Or install from inside a Claude Code session:

```text
/plugin marketplace add ghostsecurity/skills
/plugin install ghost@ghost-security
/plugin install exo@ghost-security
```

Install only the plugins you need. If the install summary asks for it, run `/reload-plugins` to activate the plugin. The README's installation doc covers loading plugins without installing them, where data is stored, and how to update.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| ghost-scan-code | 4,860 | AI-powered detection of code security issues (SAST) |
| ghost-scan-secrets | 4,144 | Context assessment of detected secrets and credentials |
| ghost-scan-deps | 4,023 | Exploitability analysis of dependency vulnerabilities (SCA) |
| ghost-proxy | 3,666 | HTTP proxy that powers the ghost-validate live-validation skill |
| ghost-validate | 3,567 | Dynamic validation of findings against a live application (DAST) |
| ghost-report | 3,559 | Combined security report across all scan results |
| ghost-repo-context | 3,542 | Build shared repository context: business criticality, sensitive data, and component map |
| ghost-exo | 685 | Build, improve, and debug workflows on the exo agent orchestration platform |

All 8 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Agent-written code ships faster than humans can audit it, and this plugin targets exactly that gap with an agent-native AppSec pipeline. The split architecture is the interesting part: the scanners are deterministic binaries whose output is auditable, while the AI layer only adds context and exploitability judgment, so findings arrive with a reason and a fix path instead of raw alerts. The skills map onto how coding agents already work: `ghost-repo-context` to learn the codebase, `ghost-scan-secrets` and `ghost-scan-deps` for fast wins, `ghost-scan-code` for SAST depth, `ghost-validate` to prove a finding against a running app, then `ghost-report` to summarize. Rules and criteria are YAML files you can extend or replace, and the tools work standalone, so one scanner can be adopted without the full pipeline. For Hermes agents, the pattern generalizes: deterministic tools plus an orchestration prompt is the same shape as a well-built multi-tool agent workflow.

## Usage

| You say | What happens |
|---|---|
| "Scan this repo for leaked secrets before I push" | ghost-scan-secrets runs Poltergeist and assesses each match in code context |
| "Are any of our dependencies exploitable?" | ghost-scan-deps checks lockfiles through Wraith and OSV, then ranks exploitability |
| "Give this service a security review" | ghost-scan-code runs AI-powered SAST detection over the codebase |
| "Prove this finding is real against the running app" | ghost-validate uses Reaper's proxy to dynamically validate findings (DAST) |
| "Summarize this sprint's security findings" | ghost-report combines results from all engines into one report |
| "What should we threat-model first in this repo?" | ghost-repo-context maps business criticality, sensitive data, and components |
| "Build a workflow on exo for triaging scans" | ghost-exo routes the request to build, improve, or debug intents on the exo platform |

## Verification

After installation, open Claude Code and confirm `ghost` and `exo` appear as installed plugins, running `/reload-plugins` if the install summary asks for it. Review the skill source before installing:

```bash
# Fetch the layout-verified scan-code SKILL.md straight from GitHub
curl -sL https://raw.githubusercontent.com/ghostsecurity/skills/main/plugins/ghost/skills/scan-code/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ghost-scan-code | Pass | Warn | Pass |
| ghost-scan-deps | Pass | Warn | Warn |
| ghost-scan-secrets | Pass | Pass | Pass |

Two of the three sampled skills carry Socket Warns, and `ghost-scan-deps` also scores a Snyk Warn; the sample covers three of the eight listings, so extend the review before wiring the plugin into CI.

## Limitations

- Mixed sampled verdicts: Socket Warn on `ghost-scan-code` and `ghost-scan-deps`; Snyk Warn on `ghost-scan-deps`. The sample is three skills.
- The primary flow is the Claude Code plugin marketplace; this is a `claude plugin install`, not a generic SKILL.md drop-in.
- Wraith queries the OSV database over the network and the scanner engines ship as GitHub release binaries; air-gapped setups need extra planning.
- Young project from a single vendor: 409 stars, first indexed Oct 9, 2026; the `exo` plugin ties into the vendor's own orchestration platform.
- Snapshot data, verified Oct 10, 2026: 28,046 combined installs across 8 indexed listings; 409 GitHub stars; Apache-2.0; last pushed Sep 28, 2026. Counts drift over time.

## Related

- [Cloudflare Security Audit Skill - Agent Code Auditing Setup](/hermes/skills/catalog/cloudflare-security-audit-setup) - a complementary code-auditing pass for agent workflows
- [Sentry Agent Skills - Security & Code Review Suite Setup](/hermes/skills/catalog/sentry-agent-skills-setup) - error and security review suite for production code
- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup) - heavier autonomous pentesting when you need it
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup) - vet any skill before installing it
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `ghost-repo-context` first so scans can weigh findings against business criticality and sensitive-data locations.
- Keep `ghost-validate` for systems you are authorized to test; it exercises a live application through the proxy.
- Start with `ghost-scan-secrets` standalone; Poltergeist works without the rest of the pipeline.
- Skip the `exo` plugin unless you use Ghost Security's orchestration platform; the AppSec skills install independently.
- Re-check the skills.sh security pages before production use: two of the three sampled skills scored Socket Warn.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
