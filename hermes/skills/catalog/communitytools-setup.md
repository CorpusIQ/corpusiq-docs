---
title: "Transilience Community Tools - Security Skills Setup"
description: "transilienceai/communitytools: Claude Code security skills and agents for authorised penetration testing and bug bounty - 10.8K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/communitytools-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "security testing", "penetration testing", "bug bounty", "offensive security"]
---

# Transilience Community Tools - Setup Guide

**Source:** [transilienceai/communitytools](https://www.skills.sh/transilienceai/communitytools) via skills.sh - 10.8K combined installs across 75 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 morning sweep)
**GitHub:** [transilienceai/communitytools](https://github.com/transilienceai/communitytools) - 630 stars, MIT licence, main branch, last pushed Jul 29, 2026. Skills live under `skills/<name>/SKILL.md`, with agent roles in `skills/coordination/`, report formatting in `formats/`, utility scripts in `tools/`, and the research benchmarks under `benchmarks/`.
**Category:** Security Testing
**Quality Tier:** 🔵 Blue (Community) - 28 Pass, 16 Warn and 16 Fail across 60 sampled verdicts (20 skills x 3 scanners); 12 of 20 sampled skills carry at least one Fail (Socket: osint, social-engineering, api-security, web-app-logic, server-side, authentication, infrastructure, injection, client-side, dfir; Gen Agent Trust Hub: reconnaissance, api-security, server-side, hackthebox, authentication, injection). MIT licence; dual-use offensive tooling for authorised testing only.

Transilience.ai's open-source Claude Code security testing suite. The README describes a consolidated set of skills and agents covering the full penetration testing lifecycle from reconnaissance to reporting, with 100% OWASP Top 10 and OWASP LLM Top 10 coverage, CVSS 4.0 reporting, Playwright browser automation, and 160+ reference files carrying PayloadsAllTheThings techniques. A companion paper ("Practice Makes Perfect", March 2026) reports an autonomous pentesting agent reaching 100% (104/104) on a published CTF benchmark using only structured markdown skill files, with cross-model transfer (Claude Sonnet 4.6 at 96.2%). The architecture is skills-only: canonical definitions live at the repo root and are symlinked into per-project environments, with three agent roles (coordinator, executor, validator) defined in `skills/coordination/`.

The skills.sh index carries 75 listings because sub-skills (the six techstack-identification domain skills) and format/report skills are counted separately from the repo's 26-27 top-level skills. The README frames the suite for authorised security testing only: penetration testing with written authorisation, bug bounty programs within scope, security research on your own systems, and CTF or training environments.

## Installation

Prerequisites from the README: the Claude Code CLI, Playwright (required for client-side testing, HackTheBox/HackerOne automation and browser evidence), Python 3 for the utility tools, and optionally Kali Linux tools (nmap, gobuster, ffuf, sqlmap) for network and infrastructure testing.

Clone the repository and launch Claude Code from the pentest project:

```bash
git clone https://github.com/transilienceai/communitytools.git
cd communitytools/projects/pentest
claude
```

The README also documents a Docker route that builds a Kali Rolling container with Claude Code, Playwright and the Kali tools preinstalled:

```bash
bash scripts/kali-claude-setup.sh projects/pentest
```

Install Playwright before browser-based testing:

```bash
npm install -g @playwright/mcp && npx playwright install chromium
```

Inside the Claude session, skills are invoked as slash commands:

```
Pentest https://target.com
/hackthebox
/hackerone
/techstack-identification
/reconnaissance target.com
/source-code-scanning ./app
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| attack-path-stitcher | 1,528 | Stitching confirmed findings into multi-hop attack paths |
| blockchain-security | 933 | Smart contract and blockchain CTF security testing |
| hackerone | 354 | HackerOne bug bounty automation and submissions |
| osint | 255 | OSINT: repository enumeration, secret scanning, employee footprint |
| reconnaissance | 252 | Domain assessment and web application mapping |
| cve-poc-generator | 242 | CVE research, safe Python PoC generation and reports |
| social-engineering | 228 | Phishing, pretexting, vishing and physical security testing |
| api-security | 224 | GraphQL, REST, WebSocket and Web-LLM API testing |
| web-app-logic | 223 | Business logic, race conditions, access control and cache attacks |
| source-code-scanning | 221 | SAST: OWASP/CWE review, dependency CVEs, hardcoded secrets |
| techstack-identification | 220 | Passive tech stack identification across six domains |
| server-side | 217 | SSRF, HTTP smuggling, traversal, deserialization, host header |
| hackthebox | 217 | HackTheBox challenge and machine automation |
| authentication | 217 | Auth bypass, JWT, OAuth, password and 2FA testing |
| infrastructure | 215 | Port scanning, DNS, MITM, VLAN hopping and SMB testing |
| injection | 214 | SQL, NoSQL, OS command, SSTI, XXE and XPath injection |
| ai-threat-testing | 214 | OWASP LLM Top 10 and AI-specific threat testing |
| client-side | 213 | XSS, CSRF, CORS, clickjacking, DOM and prototype pollution |
| reverse-engineering | 208 | Static and dynamic reverse engineering with Frida and anti-debug bypass |
| dfir | 206 | Forensics and incident response: logs, PCAP, memory, AD detection |
| essential-tools | 205 | Burp Suite, Playwright automation, methodology and reporting |
| coordination | 202 | Coordinator, executor and validator agent roles |
| cloud-containers | 201 | AWS, Azure, GCP, Docker and Kubernetes testing |

The remaining 52 indexed listings range from 1 to 199 installs (mobile-security and github-workflow at 199, system at 198, firewall-review at 191, cve-risk-score at 189, and the six techstack-identification domain sub-skills at 1 each).

## Why This Matters for Hermes Agents

Security testing is one of the few agent workloads where a wrong or invented result is worse than no result, so the value here is the structured, reviewable methodology rather than raw tool access. Each skill pairs a focused attack class (injection, authentication, server-side) with reference material that names the concrete technique, so an agent follows a known procedure instead of improvising a payload. The coordination layer matters for the same reason: findings are produced by an executor role and then checked by a validator role that reviews evidence only, a blind review that catches hallucinated exploits before they reach a report. For builders, the skills-only architecture is directly portable: canonical SKILL.md definitions at the repo root, symlinked into per-project environments, which is the same pattern Hermes uses for its own skills. The reporting path (CVSS 4.0, CWE, MITRE ATT&CK, Transilience-branded PDF) means a finished engagement ends in an artifact a human can act on. Everything is MIT licensed, and the whole suite is scoped to authorised testing, bug bounty programs within scope, your own systems and CTF labs.

## Usage

| You say | What happens |
|---|---|
| Pentest https://target.com | The coordination skill runs the full lifecycle through coordinator, executor and validator roles |
| /reconnaissance target.com | Subdomain discovery, port scanning, endpoint enumeration and attack surface mapping |
| /source-code-scanning ./app | SAST scan for OWASP Top 10, CWE Top 25, dependency CVEs and hardcoded secrets |
| /techstack-identification | Passive tech stack inference across frontend, backend, infra, security, osint and correlation |
| /hackthebox | Playwright-based login, challenge browsing and VPN management for HackTheBox |
| /hackerone | Scope CSV parsing, parallel asset testing and platform-ready submission reports |
| Generate a PoC for CVE-2024-1234 | cve-poc-generator researches NVD and writes a safe Python PoC plus a report |

## Verification

```bash
# after install, confirm the skill directories landed
ls skills/ | head
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/transilienceai/communitytools/main/skills/reconnaissance/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. `skills/injection/SKILL.md`, `skills/attack-path-stitcher/SKILL.md` and `skills/coordination/SKILL.md` were probed the same day and also returned 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| attack-path-stitcher | Pass | Pass | Warn |
| blockchain-security | Pass | Warn | Warn |
| hackerone | Pass | Warn | Pass |
| osint | Warn | Fail | Warn |
| reconnaissance | Fail | Warn | Warn |
| cve-poc-generator | Pass | Warn | Warn |
| social-engineering | Pass | Fail | Pass |
| api-security | Fail | Fail | Pass |
| web-app-logic | Pass | Fail | Pass |
| source-code-scanning | Pass | Pass | Pass |
| techstack-identification | Pass | Pass | Warn |
| server-side | Fail | Fail | Pass |
| hackthebox | Fail | Warn | Warn |
| authentication | Fail | Fail | Pass |
| infrastructure | Warn | Fail | Pass |
| injection | Fail | Fail | Pass |
| ai-threat-testing | Warn | Warn | Pass |
| client-side | Pass | Fail | Pass |
| reverse-engineering | Pass | Warn | Pass |
| dfir | Pass | Fail | Pass |

Across the 60 sampled verdicts there are 28 Pass, 16 Warn and 16 Fail. The Fail verdicts are concentrated in the skills that encode attack techniques (social-engineering, authentication, injection, osint), which is typical for offensive tooling that scanner engines flag by content. These are dual-use tools: the README frames them for authorised security testing only and lists unauthorised testing, malicious exploitation, data theft and system disruption as prohibited. Nothing here endorses unauthorised use.

## Limitations

- Snapshot data, verified Nov 20, 2026: 10,809 combined installs across 75 indexed listings; 630 GitHub stars; MIT licence; last pushed Jul 29, 2026. Counts drift over time.
- These are dual-use security tools, appropriate for sanctioned engagements (written authorisation, bug bounty scope, your own systems, CTF labs). Confirm scope and legal authorisation before running any of the offensive skills.
- Only 20 of 75 listings carry skills.sh verdicts; the remaining 55 are unverified on that platform.
- The 75 indexed listings outnumber the repo's top-level skill directories (the README counts 26 skills, Project Stats 27) because sub-skills and format/report skills are listed separately; listings such as pentest, domain-assessment, cve-testing, transilience-report-style and the six techstack-identification domain skills sit under a parent skill or the formats/ directory rather than at the skills/ root.
- The 16 Fail verdicts in the sample reflect scanner flags on offensive content, not a defect review; treat them as a cue to read each skill before use rather than a clean bill.

## Related

- [CTF Security Skills - Offensive Security Suite Setup](/hermes/skills/catalog/ctf-security-skills-setup)
- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup)
- [Trail of Bits Skills Curated - Agent Security Suite Setup](/hermes/skills/catalog/trailofbits-skills-curated-setup)
- [Yaklang Hack Skills - Offensive Security Toolkit Setup](/hermes/skills/catalog/hack-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run Claude Code from `projects/pentest` so the project only discovers the skills it symlinks, keeping context small.
- Use the Docker Kali route (`scripts/kali-claude-setup.sh`) for network and infrastructure testing, since nmap, gobuster, ffuf and sqlmap come preinstalled.
- Install Playwright first (`npm install -g @playwright/mcp && npx playwright install chromium`) or client-side and browser-evidence skills will not run.
- Read `skills/coordination/reference/validator-role.md` before a full engagement; the validator reviews evidence only, which is what catches fabricated findings.
- Stay within written scope. The suite is built for authorised engagements, bug bounty programs and CTF labs, and the README's prohibited-use list bars unauthorised testing outright.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
