---
title: "Strix Security Skills — Autonomous Pentesting Suite Setup"
description: "usestrix/strix — 8 skills, 9.6K installs, 54.1K GitHub stars: autonomous AI pentesting, CI security scanning, and vulnerability fixing with validated proof-of-concept findings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/strix-security-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "security", "pentesting", "ci", "strix"]
---

# Strix Security Skills — Setup Guide

**Source:** [usestrix/strix](https://skills.sh/usestrix/strix)
**GitHub:** [usestrix/strix](https://github.com/usestrix/strix)
**Skills:** 8 skills · 9.6K total installs
**Category:** Security Testing
**First Seen:** catalogued August 18, 2026 sweep (first seen on skills.sh 11 days before the sweep)
**Quality Tier:** 🟡 Trusted — Socket Warn and Snyk Fail on the flagship (both named), Gen Agent Trust Hub Pass; hot-page momentum with four skills at +12 in one hour

Strix runs autonomous AI pentesting agents that dynamically exploit a target and report only findings validated with a working proof-of-concept. Two run modes share the same engine and produce the same findings: the open-source CLI (self-hosted, Docker sandbox, BYO LLM key, air-gap capable, docs at docs.strix.ai) and the Cloud API (managed, app.strix.ai/api/v1, adds team dashboards, scheduling, PR reviews, and downloadable reports). The GitHub repo carries 54.1K stars and the skills cluster appeared on the platform within the last two weeks.

---

## Installation

```bash
npx skills add usestrix/strix
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/usestrix/strix --skill penetration-testing-with-strix
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Open-source mode** | Docker, an LLM API key, and explicit authorization to test the target |
| **Cloud mode** | A Strix account with API access at app.strix.ai |
| **Authorization** | Written permission for any target not owned by the operator — the skills assume scoped engagements |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| penetration-testing-with-strix | 2.4K | Full autonomous pentest runs with PoC-validated findings |
| fix-security-vulnerabilities-with-strix | 2.3K | Guided remediation of validated findings |
| ci-security-scanning-with-strix | 2.2K | Security scanning wired into CI pipelines |
| managed-pentesting-with-strix | 2.2K | Cloud API workflow: scheduling, dashboards, PR reviews, PDF/DOCX reports |
| strix-pentest | 152 | Earlier-named core pentest skill |
| strix-ci-setup | 138 | CI integration setup variant |
| strix-fix-findings | 134 | Remediation variant |
| strix-cloud-api | 121 | Cloud API client variant |

The flagship skill explicitly instructs the agent to choose between the two run modes honestly per situation rather than defaulting — local for air-gapped or BYO-LLM work, cloud for team workflows and internal-network connectors.

## Quick Start

1. Install: `npx skills add usestrix/strix`
2. For local runs: pull the Docker sandbox and set your LLM key (docs.strix.ai)
3. Ask the agent to run a scoped pentest — only PoC-validated findings get reported

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **CI security posture** | ci-security-scanning-with-strix embeds autonomous testing into agent-built pipelines |
| **Agent-verified fixes** | fix-security-vulnerabilities pairs findings with guided remediation |
| **Scoped engagements** | PoC-validated-only reporting matches our verification-before-assertion discipline |
| **Security audit support** | Complements the security-auditor role in agent orchestration workflows |

## Limitations / Verification

- Security audits on the penetration-testing-with-strix flagship: Gen Agent Trust Hub Pass, Socket Warn, Snyk Fail (both named in the tier)
- Publisher-page total verified (9.6K across 8 skills); 54.1K GitHub stars as of the sweep
- Below the 20K install guide bar — drafted on hot-page momentum (four skills at +12 installs in one hour), 54.1K-star repo authority, and security relevance to agent operations
- Skills are new on the platform (11 days); the four tail variants (121-152 installs) are earlier-named iterations
- Pentesting tools carry inherent operational risk — scope authorization is a hard prerequisite

```bash
npx skills add usestrix/strix   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
