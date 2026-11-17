---
title: "Claude-Red Skills - Offensive Security Library Setup"
description: "snailsploit/claude-red: 11.9K combined installs across 51 indexed listings, an offensive-security skill library for authorized red-team work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-red-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "offensive security", "penetration testing", "red team"]
---

# Claude-Red Skills - Setup Guide

**Source:** [snailsploit/claude-red](https://www.skills.sh/snailsploit/claude-red) via skills.sh - 11.9K combined installs across 51 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 11,165 stars, MIT license, `main` branch, last pushed 2026-11-11, skills under `Skills/<category>/<name>/SKILL.md`
**Category:** Offensive security / red-team and penetration-testing agent skills
**Quality Tier:** 🟠 Orange - an offensive-security library whose sampled verdicts include 5 of 20 Trust Hub fails, 1 Snyk fail and 1 Socket fail.

claude-red is a curated library of offensive-security skills for the Claude skills system: structured SKILL.md files that prime an agent with expert-level methodology for a specific attack surface, from SQL injection and JWT abuse to shellcode, Wi-Fi, OSINT, cloud and mobile. The 78 skills in the tree span 23 categories and load on demand based on conversational triggers. The README positions them for authorized red-team engagements, bug bounty triage, security research and operator training.

The 51 indexed listings carry 11,871 combined installs. Because the skills encode real exploitation procedures and the sampled scanner verdicts include failures on Gen Agent Trust Hub, Socket and Snyk, this guide is marked Orange: load it only on systems you own or are contracted to test.

## Installation

```bash
git clone https://github.com/SnailSploit/claude-red ~/.claude/skills/claude-red
```

To install a single category, use a sparse checkout:

```bash
git clone --filter=blob:none --sparse https://github.com/SnailSploit/claude-red
cd claude-red && git sparse-checkout set Skills/web Skills/active-directory
```

Or run the bundled install script:

```bash
./install.sh                           # interactive
./install.sh --target ~/.claude/skills # explicit target
./install.sh --category web            # single category
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| offensive-sqli | 306 | Test web applications for SQL injection, from error-based to blind and out-of-band. |
| offensive-reporting | 302 | Write penetration-test and red-team reports with CVSS scoring and evidence standards. |
| offensive-jwt | 301 | Test JWT authentication for algorithm confusion, secret cracking and header injection. |
| offensive-business-logic | 300 | Find business-logic flaws like workflow bypass and price or quantity manipulation. |
| offensive-wifi | 267 | Run 802.11 assessments covering WPA2/WPA3, evil twin, WPS and deauthentication. |
| offensive-shellcode | 262 | Write custom x86/x64 shellcode and loaders with AV and EDR evasion. |
| offensive-fuzzing | 261 | Set up fuzzing campaigns with AFL++, libFuzzer and harness writing. |
| offensive-osint | 260 | Run reconnaissance over domain, email, social and breach-data sources. |
| offensive-cloud | 259 | Test AWS, Azure and GCP for privilege escalation and persistence. |
| offensive-wifi-recon | 255 | Map wireless airspace in monitor mode before active attacks. |
| offensive-mobile | 254 | Test Android and iOS apps with Frida, object inspection and pinning bypass. |
| offensive-api-security | 254 | Test REST, gRPC and WebSocket APIs against the OWASP API Security Top 10. |
| offensive-iot | 252 | Test embedded devices across hardware, firmware and radio protocols. |
| offensive-active-directory | 252 | Assess on-prem Active Directory for Kerberoasting, ACL abuse and ADCS. |

The remaining 37 indexed listings range from 159 to 246 installs.

## Why This Matters for Hermes Agents

An agent doing authorized security work needs the same methodology a human operator follows, not a list of tool names. These skills give an agent a structured procedure per attack surface: reconnaissance before exploitation, detection signatures and defensive indicators alongside every technique, and a reporting skill that turns findings into a client-ready deliverable with CVSS scoring and evidence hygiene. The wireless cluster (14 skills) and web cluster (16 skills) are the deepest, covering everything from WPA3 SAE downgrade to request smuggling. Because each skill is a self-contained SKILL.md that loads on trigger phrases, an agent pays context only for the attack surface in scope. The reporting skill matters as much as the exploit skills: it enforces evidence standards, redaction and time-stamping so the output stands up in a retest.

## Usage

| You say | What happens |
|---|---|
| "Test this login form for SQL injection" | Runs offensive-sqli for injection vectors and database-specific payloads. |
| "Check this JWT for weaknesses" | Runs offensive-jwt for algorithm confusion and secret cracking. |
| "Map the wireless around this office" | Runs offensive-wifi-recon for monitor mode and airspace mapping. |
| "Audit this API surface" | Runs offensive-api-security against the OWASP API Top 10. |
| "Write up the engagement" | Runs offensive-reporting for CVSS scoring and a client-ready report. |
| "Enumerate this AD domain" | Runs offensive-active-directory for Kerberoasting and ACL abuse. |

## Verification

Probe skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/snailsploit/claude-red/main/Skills/web/offensive-sqli/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/snailsploit/claude-red/main/Skills/infrastructure/offensive-shellcode/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/snailsploit/claude-red/main/Skills/auth/offensive-jwt/SKILL.md
```

Skills live at `Skills/<category>/<name>/SKILL.md` on `main`. Read each SKILL.md in full before use; they describe real attack techniques, and the tree also ships an install script, a build manifest and CI workflows that sit outside the skill set.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| offensive-sqli | Fail | Warn | Pass |
| offensive-reporting | Pass | Pass | Pass |
| offensive-jwt | Pass | Pass | Pass |
| offensive-business-logic | Pass | Warn | Pass |
| offensive-wifi | Pass | Warn | Warn |
| offensive-shellcode | Fail | Warn | Fail |
| offensive-fuzzing | Pass | Warn | Pass |
| offensive-osint | Fail | Warn | Warn |
| offensive-cloud | Pass | Warn | Pass |
| offensive-wifi-recon | Fail | Warn | Pass |
| offensive-mobile | Pass | Warn | Pass |
| offensive-api-security | Pass | Warn | Pass |
| offensive-iot | Pass | Pass | Warn |
| offensive-active-directory | Pass | Warn | Pass |
| offensive-graphql | Pass | Warn | Pass |
| offensive-bluetooth-ble | Pass | Warn | Warn |
| offensive-evil-twin | Pass | Fail | Pass |
| offensive-deauth-disassoc | Warn | Warn | Pass |
| offensive-lorawan-sub-ghz | Fail | Warn | Warn |
| offensive-bluetooth-classic | Pass | Warn | Pass |

These skills encode real exploitation procedures: credential abuse, shellcode, phishing, persistence and data exfiltration. Use them only on systems you own or are contracted to test, and only within the written scope of an engagement. The sample covers 20 of the 51 indexed listings and includes failures on all three scanners: 5 of 20 Gen Agent Trust Hub fails, 1 Snyk fail and 1 Socket fail, alongside several Warns.

## Limitations

- Snapshot data, verified 2026-11-17: 11,871 combined installs across 51 indexed listings; 11,165 GitHub stars; MIT; last pushed 2026-11-11. Counts drift over time.
- The skills are offensive in nature; loading them into an agent that also has network or shell access is a meaningful risk on any system you do not control.
- Sampled verdicts include failures on three scanners (Gen Agent Trust Hub, Socket and Snyk), so the library does not carry a clean bill of health.
- The tree holds 78 SKILL.md files across 23 categories while the index lists 51 entries; several skill directories (for example AI security and OAuth) are not among the indexed listings.
- MIT covers the code, not the consequences of using it; the author scopes it to authorized engagements, training and research.

## Related

- [Yaklang Hack Skills - Offensive Security Toolkit Setup](/hermes/skills/catalog/hack-skills-setup)
- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup)
- [Supabase Pentest Skills - 24-Skill Audit Suite](/hermes/skills/catalog/supabase-pentest-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the OSINT and reconnaissance skills first; several exploit skills assume you already have an attack-surface map.
- Keep the reporting skill loaded from the start so evidence, timestamps and scope notes are captured as you go.
- Use a sparse checkout (Skills/web or Skills/active-directory) to pull only the surface in scope instead of the whole library.
- Treat every technique as scoped: confirm you own the target or hold a written testing contract before running anything destructive.
- Re-check the skills.sh security pages before production use; the sampled verdicts drift as the library updates.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
