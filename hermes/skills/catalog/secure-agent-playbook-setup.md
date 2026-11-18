---
title: "Secure Agent Playbook - OWASP AI Agent Security Setup"
description: "owasp/secure-agent-playbook: 5.8K combined installs across 19 listings; OWASP security procedures for AI agents, from code review to agent audits."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/secure-agent-playbook-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "security", "owasp", "appsec"]
---

# Secure Agent Playbook - Setup Guide

**Source:** [owasp/secure-agent-playbook](https://www.skills.sh/owasp/secure-agent-playbook) via skills.sh - 5.8K combined installs across 19 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 227 stars, NOASSERTION license, `main` branch, last pushed 2026-10-15. Skills live in `plugins/code-security-skills/skills/` and `plugins/ai-security-skills/skills/`, with the full procedures in parallel `plays/` folders.
**Category:** OWASP security review and audit procedures for AI agents
**Quality Tier:** 🟠 Orange - 50 Pass, 6 Warn and 1 Fail across the 57 sampled verdict cells; GitHub reports NOASSERTION, so the licence is ambiguous.

The OWASP Secure Agent Playbook Project ships structured, OWASP-grounded security procedures that an agent follows to produce evidence-based findings. Each play is a step-by-step procedure with checklists and output templates, and each skill summarizes one procedure, so results are reproducible across runs and assessments instead of ad-hoc prompting.

GitHub reports NOASSERTION for the repository licence even though the bundled LICENSE.md reads CC-BY-4.0, so the licence status is ambiguous rather than clearly permissive. The skills work beyond Claude Code: the plays are standalone Markdown procedures that any agent can follow by pointing at the file.

## Installation

With Claude Code, register the plugin marketplace and install one or both skill sets:

```bash
/plugin marketplace add OWASP/secure-agent-playbook
/plugin install code-security-skills@agent-security-playbook
/plugin install ai-security-skills@agent-security-playbook
```

For an organization install, download the release asset zip from the latest GitHub release and upload it under Organization settings. For a local clone:

```bash
/plugin marketplace add /path/to/agent-security-playbook
/plugin install code-security-skills@agent-security-playbook
```

Without Claude Code, skip installation entirely and point any agent at a play file, for example `plugins/ai-security-skills/plays/agent-security-audit.md`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| web-security-review | 881 | Review web applications against the OWASP Top 10 (2021), covering injection, broken auth, and XSS. |
| api-security-review | 684 | Review APIs against the OWASP API Security Top 10 (2023), covering BOLA/IDOR, broken auth, mass assignment, and SSRF. |
| code-review-security | 516 | Security-focused code review mapped to OWASP Top 10 and ASVS for pull requests and pre-merge gate checks. |
| security-guidance | 492 | Security-first development guidance based on OWASP ASVS for code that touches input, auth, persistence, or network I/O. |
| secrets-scan | 427 | Detect hardcoded credentials, API keys, tokens, and secrets in source code and configuration files. |
| sca-audit | 358 | Scan project dependencies for known CVEs across package.json, requirements.txt, go.mod, and other lockfiles. |
| agent-security-audit | 302 | Audit AI agent configurations for excessive permissions, prompt injection surfaces, and missing guardrails. |

The remaining 12 indexed listings range from 116 to 225 installs.

## Why This Matters for Hermes Agents

The playbook turns "review my code for security" from a surface-level checklist into a documented OWASP procedure. Findings carry severity, CWE mappings, OpenCRE cross-references, evidence snippets, and remediation code, which makes results reproducible and auditable rather than ad hoc.

Because the plays are plain Markdown procedures, they are not tied to Claude Code: any agent can follow a play file as a checklist, while Claude Code users get plugin installation plus bundled agents. The skills split across two plugins, one for code and infrastructure security and one for AI and agent security, and the second is the more unusual half given how new agent-specific threat models are.

## Usage

| You say | What happens |
|---|---|
| "Review this code for security issues" | code-review-security audits the code against OWASP Top 10 and ASVS and returns findings with severity and remediation. |
| "Scan my dependencies for CVEs" | sca-audit checks dependency files for known vulnerabilities. |
| "Scan for hardcoded secrets" | secrets-scan detects credentials, API keys, and tokens in source and configuration files. |
| "Review this API for security" | api-security-review checks the API against the OWASP API Security Top 10 (2023). |
| "Review this web app for OWASP Top 10" | web-security-review walks the classic Top 10 risks including injection and XSS. |
| "Audit this agent's configuration" | agent-security-audit checks permissions, prompt injection surfaces, and data exfiltration paths. |
| "Generate code that handles user input" | security-guidance auto-triggers ASVS guidance for the security-sensitive parts. |

## Verification

Probe one skill file on the `main` branch before installing. It returns HTTP 200:

```bash
curl -fsSL https://raw.githubusercontent.com/OWASP/secure-agent-playbook/main/plugins/code-security-skills/skills/web-security-review/SKILL.md | head -12
```

For organization installs, use the release asset zip rather than GitHub's "Download ZIP" button, which nests files in a subdirectory the plugin validator rejects.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| web-security-review | Pass | Pass | Pass |
| api-security-review | Pass | Warn | Pass |
| code-review-security | Pass | Pass | Warn |
| security-guidance | Pass | Pass | Pass |
| secrets-scan | Pass | Pass | Pass |
| sca-audit | Pass | Pass | Pass |
| agent-security-audit | Pass | Pass | Pass |
| mobile-code-review | Pass | Pass | Fail |
| prompt-injection-test | Pass | Warn | Pass |
| mcp-server-review | Pass | Pass | Warn |
| iac-security-review | Pass | Pass | Pass |
| securability-engineering | Pass | Pass | Pass |
| multi-agentic-threat-model | Pass | Pass | Pass |
| llm-risk-assess | Pass | Warn | Pass |
| prd-securability-enhancement | Pass | Pass | Pass |
| securability-engineering-review | Pass | Pass | Warn |
| agentic-ai-risk-assess | Pass | Pass | Pass |
| ai-security-verification | Pass | Pass | Pass |
| your-skill-name | Pass | Pass | Pass |

The sample covers all 19 indexed listings. The one Fail cell is a Snyk flag on mobile-code-review; the Warn cells sit on api-security-review, code-review-security, prompt-injection-test, mcp-server-review, llm-risk-assess, and securability-engineering-review.

## Limitations

- Snapshot data, verified Nov 18, 2026: 5,835 combined installs across 19 indexed listings; 227 GitHub stars; NOASSERTION; last pushed 2026-10-15. Counts drift over time.
- GitHub reports NOASSERTION for the repository licence, while the bundled LICENSE.md reads CC-BY-4.0; treat the licence status as ambiguous and check it before redistribution.
- The skills are Claude Code plugins at heart; using them elsewhere means pointing an agent at the raw play Markdown files rather than a clean install.
- One listing, your-skill-name, is the repository's SKILL.md template rather than a real skill, yet it carries installs and is included in the security sample.
- Findings depend on the agent actually following the procedure; the playbook supplies the method, not a runtime that guarantees execution.

## Related

- [Trailofbits Security Setup](/hermes/skills/catalog/trailofbits-security-setup)
- [ClawHub Skill Vetting - Security Scanner Setup](/hermes/skills/catalog/clawhub-skill-vetting-setup)
- [Security Hardening - AI Agent Security Setup](/hermes/skills/catalog/security-and-hardening-setup)
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use the release asset zip for organization installs; GitHub's "Download ZIP" nests files in a subdirectory the validator rejects.
- For non-Claude environments, point the agent directly at a play file under `plugins/*/plays/` rather than trying to install.
- Prefer the per-skill zips, or run `scripts/package_skills.sh` from a clone, for the organization Skills upload, which rejects zips over 200 files.
- Keep the report template (`plugins/*/templates/report.md`) when consolidating a team assessment so findings stay uniform.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
