---
title: "Awesome Security Skills - SecLists Testing Toolkit Setup"
description: "eyadkelleh/awesome-skills-security - 4.4K combined installs: 7 security skills with SecLists wordlists and payloads for authorized pentesting."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/awesome-skills-security-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "security", "pentesting", "seclists"]
---

# Awesome Security Skills - SecLists Testing Toolkit Setup

**Source:** [eyadkelleh/awesome-skills-security](https://www.skills.sh/eyadkelleh/awesome-skills-security) via skills.sh - 4.4K combined installs across 7 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [eyadkelleh/awesome-skills-security](https://github.com/eyadkelleh/awesome-skills-security) - 415 stars, no LICENSE file, main branch, last pushed June 8, 2026; 7 skills under skills/<name>/SKILL.md with references/ wordlists curated from SecLists.
**Category:** Security Testing and Offensive Tooling
**Quality Tier:** 🟠 Orange - security-webshells fails all three checks and llm-testing and security-payloads each carry a Fail cell; the repository also ships no LICENSE file.

eyadkelleh's awesome-skills-security packages a curated subset of the SecLists wordlists and payloads as seven agent skills for authorized security testing. The seven categories cover fuzzing payloads, password lists, sensitive-data patterns, exploit payloads, username lists, web-shell samples and LLM security testing, all reachable from an agent in plain language.

The repository bundles live offensive-security material, SQL injection payloads, web shells and darkweb breach lists, so it must be used only against systems you own or that you have written authorization to test. It carries 415 stars but no LICENSE file: the README labels the bundled SecLists content MIT-licensed, yet the repository itself ships no license text. All seven listings clear the 500-install threshold.

## Installation

List what is available, then install the whole set or specific skills:

```bash
npx skills add Eyadkelleh/awesome-skills-security --list
npx skills add Eyadkelleh/awesome-skills-security --skill '*' -y
npx skills add Eyadkelleh/awesome-skills-security --skill security-fuzzing --skill llm-testing -y
```

Install to a specific agent or globally:

```bash
npx skills add Eyadkelleh/awesome-skills-security -a cursor -y
npx skills add Eyadkelleh/awesome-skills-security --skill '*' -g -y
```

Update later, or clone the repository directly:

```bash
npx skills update -y
git clone https://github.com/Eyadkelleh/awesome-skills-security.git
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| security-patterns | 664 | sensitive data patterns: API keys, credit cards, emails, SSNs, phone numbers and IPs |
| security-fuzzing | 662 | SQL, NoSQL, command and LDAP injection fuzzing payloads |
| security-payloads | 642 | exploitation payloads: anti-virus test files, file-name exploits and malicious files |
| security-passwords | 624 | curated password wordlists for authorized credential testing |
| llm-testing | 620 | LLM security testing prompts for bias, data leakage and adversarial resistance |
| security-webshells | 614 | web shell samples for detection and defensive testing |
| security-usernames | 610 | username wordlists for enumeration |

All 7 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

For a Hermes agent doing defensive security or red-team support, this collection delivers the most-used wordlists and payloads without pulling the full 4.5GB SecLists repository. security-patterns is the most defensive of the seven and slots directly into code-review work, matching API keys, credit cards, emails, SSNs, phone numbers and IPs during a secret scan. llm-testing supplies structured prompts for bias, data-leakage and adversarial testing, which is the red-team equivalent for model work. The wordlists are small curated subsets (the password set stays under 10MB), so they are cheap to install and inspect. The critical constraint is scope: these are offensive-security resources, and the repository's own guidance requires written authorization before any test, so a Hermes agent should treat any request to use them against a third-party target as out of scope without proof of permission.

## Usage

| You say | What happens |
|---|---|
| Show me SQL injection payloads | security-fuzzing returns SQLi vectors from its fuzzing references |
| Scan this codebase for exposed API keys | security-patterns matches API key and credential patterns |
| Show common weak passwords to test | security-passwords returns curated password lists |
| Test this LLM for bias | llm-testing provides bias, leakage and adversarial prompts |
| I need XSS payloads for a CTF | security-payloads returns exploitation payloads |
| Show web shell samples for detection | security-webshells returns shell samples for detection testing |

## Verification

Confirm the skills install, then review one raw SKILL.md before use:

```bash
curl -sL https://raw.githubusercontent.com/Eyadkelleh/awesome-skills-security/main/skills/security-fuzzing/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| security-patterns | Pass | Pass | Warn |
| security-fuzzing | Pass | Warn | Pass |
| security-payloads | Fail | Warn | Fail |
| security-passwords | Pass | Pass | Pass |
| llm-testing | Warn | Warn | Fail |
| security-webshells | Fail | Fail | Fail |
| security-usernames | Pass | Pass | Warn |

The repository ships no LICENSE file. Offensive-security material requires written authorization before use, and several listings fail or warn on skills.sh's own checks.

## Limitations

- Snapshot data, verified Nov 24, 2026: 4,436 combined installs across 7 indexed listings; 415 GitHub stars; no LICENSE file; last pushed June 8, 2026. Counts drift over time.
- The repository ships no LICENSE file, so reuse terms are unclear even though the README labels the bundled SecLists content MIT-licensed.
- The material is offensive-security tooling (web shells, breach password lists, exploit payloads); use it only against systems you own or have written authorization to test.
- The wordlists are curated subsets of SecLists, not the full 4.5GB collection, so coverage is intentionally limited.
- The suite supplies wordlists and prompts, not an automated scanner: it hands you payloads but does not execute attacks.

## Related

- [CTF Security Skills - Offensive Security Suite Setup](/hermes/skills/catalog/ctf-security-skills-setup)
- [Cybersecurity Skills - 42 Audit and Pentest Skills](/hermes/skills/catalog/briiirussell-cybersecurity-skills-setup)
- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup)
- [Security Skills - Pentest and Compliance Suite](/hermes/skills/catalog/securityskills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the categories you need with --skill <name> rather than the whole set.
- Reach for security-patterns first in code review, it is the most defensive of the seven.
- Keep web-shell and payload skills inside an isolated lab environment, never against production.
- Confirm written authorization and scope before any credential or injection testing.
- Review the raw SKILL.md and wordlist files before installing, since the repo ships no license file.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
