---
title: "Claude Bughunter - Red Team Skill Bundle Setup"
description: "elementalsouls/claude-bughunter: 25.4K combined installs across 83 listings, 82 vulnerability hunting skills for authorised red team and bounty work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/elementalsouls-claude-bughunter-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "security", "bug bounty", "red team", "pentesting"]
---

# Claude Bughunter - Setup Guide

**Source:** [elementalsouls/claude-bughunter](https://www.skills.sh/elementalsouls/claude-bughunter) via skills.sh - 25.4K combined installs across 83 indexed listings; first seen Nov 13, 2026 (evening sweep)

**GitHub:** 5,763 stars, MIT licence, `main` branch, last pushed 2026-11-13, 83 `SKILL.md` files matching the 83 indexed listings one-to-one, 47 Python files, 15 YAML and 3 PowerShell files in the tree

**Category:** Offensive security skills for bug bounty and external red-team work

**Quality Tier:** 🟡 Yellow - 83 skills and a strong README, but a Snyk Fail on hunt-auth-bypass and a Socket Warn on bb-methodology.

claude-bughunter is a self-contained skill bundle for bug hunting and external red-team work, built by Sachin Sharma. It ships 83 skills, 15 slash commands and 681 disclosed-report patterns across 24 vulnerability classes, plus enterprise identity and infrastructure attack matrices. The 83 indexed listings map one-to-one to the 83 `SKILL.md` files in the tree.

This is offensive security tooling. Every skill here is meant for authorised bug bounty and red-team work against targets you have written permission to test, and nothing else. The bundle is explicit about its scope: external attack surface only, with internal Active Directory, C2 frameworks, post-exploitation, evasion and iOS or hardware work deliberately left out.

## Installation

Option A installs as a Claude Code plugin (recommended). From inside Claude Code:

```text
/plugin marketplace add elementalsouls/Claude-BugHunter
/plugin install claude-bughunter@elementalsouls
```

Option B is a copy install:

```bash
git clone https://github.com/elementalsouls/Claude-BugHunter.git
cd Claude-BugHunter
bash scripts/install.sh          # macOS / Linux
pwsh ./scripts/install.ps1       # Windows (PowerShell)
```

Both copy the skills into `~/.claude/` (or `%USERPROFILE%\.claude\` on Windows) and wire the `hunt` engagement scaffolder. The multi-harness flags install to every harness at once, including Hermes Agent at `~/.hermes/skills/` via `--hermes`:

```bash
bash scripts/install.sh --all --burp-mcp
```

`--all` detects installed harnesses and copies skills to `~/.claude/skills`, `~/.agents/skills`, `~/.hermes/skills` and `~/.gemini/config/skills`; `--burp-mcp` wires the Burp MCP server into each.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| bb-methodology | 420 | Master orchestrator for bug bounty sessions: the 5-phase non-linear hunting workflow plus a critical-thinking framework (developer psychology, anomaly detection, What-If experiments); routes to every other skill by phase. |
| report-writing | 403 | Bug bounty report writing for HackerOne, Bugcrowd, Intigriti and Immunefi: templates, impact-first writing, CVSS 3.1 scoring, title and severity formulas, pre-submit checklist. |
| hunt-auth-bypass | 374 | Auth bypass hunting built from 12 disclosed reports: SAML XSW and parser-differential, signature stripping, domain-enforcement bypass, cross-IdP assertion reuse, XMLRPC SSO bypass. |
| evidence-hygiene | 368 | Evidence capture and PoC redaction: cookie redaction, PII black-bar rules, HAR sanitization and screenshot discipline before submission. |
| hunt-xss | 361 | XSS hunting built from 174 disclosed reports; the escalation path from hunt-html-injection once script execution is possible. |
| hunt-sqli | 357 | SQLi hunting built from 12 disclosed reports: NoSQL injection, ORM raw-fragment SQLi, second-order SOQL, time-based blind SQLi. |
| hunt-idor | 355 | IDOR hunting built from 26 disclosed reports. |
| hunt-ssrf | 354 | SSRF hunting built from 15 disclosed reports: cloud metadata (AWS, GCP, Azure), DNS rebinding and gopher-protocol chains. |
| hunt-rce | 349 | RCE hunting built from 67 disclosed reports. |
| offensive-osint | 348 | Operational recon arsenal: subdomain enum, GraphQL/Swagger/REST discovery, identity-fabric mapping, cloud bucket enum, CDN/WAF bypass, vendor fingerprinting. |
| web2-recon | 347 | Web2 recon pipeline: subdomain enumeration, live host discovery, URL crawling, directory fuzzing, JS analysis and continuous monitoring. |
| hunt-oauth | 345 | OAuth hunting built from 19 disclosed reports. |
| bug-bounty | 345 | End-to-end bug bounty workflow: recon, pre-hunt learning, hunting across 15+ vulnerability classes, and reporting. |
| hunt-ato | 339 | Account takeover taxonomy: 9 paths to ATO plus chains (password-reset flaws, OAuth link CSRF, MFA bypass, session fixation, JWT manipulation). |
| hunt-business-logic | 338 | Business logic hunting built from 12 disclosed reports: coupon race-stacking, price tampering, field overflow, PayPal redirect trust. |
| triage-validation | 336 | Finding validation before any report: the 7-Question Gate, pre-submission gates, always-rejected list, CVSS reference and severity guide. |
| hunt-graphql | 334 | GraphQL hunting built from 12 disclosed reports: IDOR via node() and GID, cross-tenant IDOR, SSRF, query-cost bypass, auth bypass. |
| hunt-cache-poison | 333 | Cache poisoning hunting built from 10 disclosed reports: header poisoning, cache deception and hop-by-hop smuggling. |
| bb-local-toolkit | 333 | Local-tooling companion to bug-bounty: the same workflow plus resolving where tools, wordlists and clones live (jhaddix, SecLists, trufflehog, ffuf, dalfox, ghauri). |
| hunt-race-condition | 332 | Race condition hunting built from 12 disclosed reports: HTTP/2 single-packet attacks, coupon and gift-card double-spend, MFA-OTP races. |

The remaining 63 indexed listings range from 195 to 328 installs.

## Why This Matters for Hermes Agents

The bundle installs to Hermes Agent directly: `bash scripts/install.sh --all` copies skills to `~/.hermes/skills/`, and the README lists Hermes Agent as a supported harness. The knowledge layer - all 83 skills - ports over; only the slash commands and the `/hunt` engine stay Claude Code-only by design.

The value for a Hermes agent is encoded tradecraft rather than general advice. Each `hunt-*` skill is built from a disclosed-report count and carries payloads, bypass tables and chain templates, so the agent tests from real triager patterns instead of inventing cases from the OWASP Top 10. The 7-Question Gate in triage-validation forces an in-scope check before anything is submitted.

The tradeoff is the trust surface. The skills run offensive tooling, so the verdicts and scope rules matter more than they would for a content skill.

## Usage

| You say | What happens |
|---|---|
| "Testing acme.com, an in-scope HackerOne target. Run recon and rank the surface." | Loads web2-recon, offensive-osint and bb-methodology, then ranks the attack surface. |
| "Hunt for XSS on this target" | hunt-xss loads with payloads and bypass tables drawn from 174 disclosed reports. |
| "Validate this finding before I write it up" | triage-validation runs the 7-Question Gate and the pre-submission gates. |
| "Write up this IDOR finding for HackerOne" | report-writing and evidence-hygiene produce the report and redact the PoC. |
| "Check this OAuth flow for token theft" | hunt-oauth loads with patterns from 19 disclosed reports. |
| "Map the enterprise surface, M365 and Okta" | Loads m365-entra-attack and okta-attack with current CVE chains. |

## Verification

Probe two skills on the `main` branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/elementalsouls/Claude-BugHunter/main/skills/bb-methodology/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/elementalsouls/Claude-BugHunter/main/skills/hunt-auth-bypass/SKILL.md
```

Skills live at `skills/<name>/SKILL.md` at the repo root. Read hunt-auth-bypass in full before installing it: it carries the pack's only failing verdict.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bb-methodology | Pass | Warn | Pass |
| report-writing | Pass | Pass | Pass |
| hunt-auth-bypass | Pass | Warn | Fail |
| evidence-hygiene | Pass | Pass | Pass |

hunt-auth-bypass carries a Snyk Fail, the only failing verdict in the sample. bb-methodology carries a Socket Warn, and hunt-auth-bypass carries the same Warn alongside its Fail. Read hunt-auth-bypass line by line before using it - it is the one skill the auditors flagged at the fail level. The other 79 listings publish no verdict at all, which is not the same as a pass. Four skills sampled out of 83 means a pass only covers that one file, not the bundle.

## Limitations

- Snapshot data, verified 2026-11-13: 25,418 combined installs across 83 indexed listings; 5,763 GitHub stars; MIT; last pushed 2026-11-13. Counts drift over time.
- hunt-auth-bypass carries a Snyk Fail, the only failing verdict among the sampled skills; bb-methodology and hunt-auth-bypass both carry a Socket Warn.
- The sample is four skills out of 83, so the verdicts describe a small slice of the bundle and the remaining listings are unverified.
- The slash commands and the `/hunt` engine are Claude Code-only; the knowledge layer ports to the other harnesses.
- Anthropic's runtime cyber safeguards can block authorised offensive-security work by default, so even in-scope tasks can hit a model refusal; the README points to the Cyber Verification Program for legitimate dual-use work.
- The bundle is external attack surface only. Internal Active Directory, C2 frameworks, post-exploitation, evasion and iOS or hardware work are excluded by design, so an internal red team needs different tooling for those phases.

## Related

- [Anthropic Cybersecurity Skills Setup Guide](/hermes/skills/catalog/anthropic-cybersecurity-skills-setup)
- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup)
- [OSINT Skills - 57-Skill Open-Source Intelligence Suite](/hermes/skills/catalog/osint-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install via the plugin first (Option A). It namespaces everything under `claude-bughunter:` and updates cleanly without copying files into `~/.claude/`.
- Run bb-methodology at the start of every session. It routes to the right hunt skill by phase, which is the difference between a checklist and a methodology.
- Run triage-validation before report-writing. The 7-Question Gate kills weak findings early and protects the acceptance ratio.
- Read hunt-auth-bypass in full before using it. It carries the only Snyk Fail in the sampled set.
- Keep evidence-hygiene in the loop for every PoC. Screenshots leak cookies and PII, and its redaction rules are the cheapest fix.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
