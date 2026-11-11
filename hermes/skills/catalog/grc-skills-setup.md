---
title: "GRC Skills - Governance, Risk and Compliance Suite"
description: "GRC compliance suite: 9.4K combined installs across 36 listings, covering ISO 27001, SOC 2, GDPR, HIPAA, EU AI Act and NIST 800-53"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/grc-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "grc", "compliance", "soc 2", "iso 27001", "gdpr"]
---

# GRC Skills - Setup Guide

**Source:** [sushegaad/claude-skills-governance-risk-and-compliance](https://www.skills.sh/sushegaad/claude-skills-governance-risk-and-compliance) via skills.sh - 9.4K combined installs across 36 indexed listings (9,363 exact); first seen 2026-11-11 (Nov 11, 2026 sweep)
**GitHub:** 1,060 stars, MIT license, `main` branch, last pushed 2026-11-07, 36 `SKILL.md` files under `plugins/<regime>/skills/<regime>/`, one per framework
**Category:** Governance, risk and compliance: certification frameworks, privacy law, security baselines, AI regulation and sector rules
**Quality Tier:** 🟢 Strong - MIT licensed, a one-to-one mapping between the 36 indexed listings and 36 skill directories, every sampled security verdict a Pass, and a published evaluation harness behind its accuracy claim.

This is the most complete framework-per-skill compliance library in the skills marketplace, and its organising principle is simple enough to be the reason it works. One regime, one skill. There is no general compliance assistant to misinterpret your question; a question about SOC 2 loads the SOC 2 skill, which carries that framework's control structure and evidence expectations.

The regime list is genuinely broad rather than padded. Certification schemes include ISO 27001, ISO 27701, ISO 42001, SOC 2, FedRAMP, CMMC 2.0, PCI DSS, TISAX, Cyber Essentials and CIS Controls v8. Privacy law covers GDPR, CCPA/CPRA, Brazil's LGPD, India's DPDPA, Vietnam's PDPL, Saudi and UAE data protection. Sector and export rules add HIPAA, SOX ITGC, TSA cybersecurity, SWIFT CSP, ITAR and EAR. The newer surface is AI and resilience regulation: the EU AI Act, the NIST AI Risk Management Framework, DORA, NIS2, the EU Cyber Resilience Act and CSRD.

The README makes an unusual claim for a skill collection and then documents the method. It states a benchmark of 90 percent with skills against 49 percent without, across 180 test cases graded against at least 5 verifiable assertions each by independent agents, 902 assertions in total. Whether you accept the figure or not, publishing the harness and the assertion count is more than most skill repositories do.

## Installation

The recommended path is the Claude Code plugin marketplace, documented as supporting version pinning, automatic updates and team-wide distribution without manual file handling. Add the marketplace, then install the regimes you need, since each one is its own plugin:

```bash
/plugin marketplace add Sushegaad/Claude-Skills-Governance-Risk-and-Compliance
/plugin install iso27001@grc-skills soc2@grc-skills fedramp@grc-skills nist-csf@grc-skills cmmc@grc-skills swift-csp@grc-skills ism@grc-skills cis-controls@grc-skills nist-800-53@grc-skills nzism@grc-skills tisax@grc-skills tprm@grc-skills cyber-essentials@grc-skills sox-itgc@grc-skills gdpr-compliance@grc-skills hipaa-compliance@grc-skills pci-compliance@grc-skills iso27701@grc-skills dpdpa@grc-skills ccpa@grc-skills lgpd@grc-skills vn-pdpl@grc-skills tsa-compliance@grc-skills dora@grc-skills nis2@grc-skills eu-cra@grc-skills iso42001@grc-skills nist-ai-rmf@grc-skills eu-ai-act@grc-skills itar@grc-skills csrd@grc-skills ear@grc-skills section-508@grc-skills wcag@grc-skills saudi-arabia-grc@grc-skills uae-grc@grc-skills
```

That one line installs all 36. For a narrower deployment, install only the regimes that apply, which is also better for skill triggering.

The README documents a second path for Claude's file-based skills: download the `.skill` package for each framework from the repository's per-regime directory and upload it. That route is for Claude rather than for coding agents, and it is the reason each regime directory carries both a `SKILL.md` and a packaged `.skill` file.

For a Hermes profile, copy the skill directories in. Keep the folder names intact:

```bash
git clone https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance
cp -R Claude-Skills-Governance-Risk-and-Compliance/plugins/*/skills/* ~/.hermes/profiles/corpusiq/skills/
```

The repository also publishes a documentation site through GitHub Pages, which the README links, and it ships a monthly update cadence with a version tag, currently v2.2.0.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| lgpd | 423 | Brazil's General Data Protection Law obligations and controls |
| iso27001 | 368 | ISO 27001 information security management, control selection and certification readiness |
| gdpr-compliance | 360 | GDPR lawful basis, data subject rights, DPIA and cross-border transfer questions |
| soc2 | 315 | SOC 2 trust services criteria, control mapping and audit readiness |
| iso42001 | 309 | ISO 42001 AI management system requirements |
| nist-csf | 306 | NIST Cybersecurity Framework functions, categories and maturity |
| eu-ai-act | 298 | EU AI Act risk tiers, obligations and compliance timelines |
| dpdpa | 295 | India's Digital Personal Data Protection Act |
| nis2 | 294 | EU NIS2 directive requirements for essential and important entities |
| pci-compliance | 293 | PCI DSS requirements for cardholder data environments |
| iso27701 | 292 | ISO 27701 privacy information management extensions |
| hipaa-compliance | 291 | HIPAA privacy, security and breach notification rules |
| fedramp | 285 | FedRAMP authorisation, control baselines and continuous monitoring |
| tsa-compliance | 285 | TSA cybersecurity requirements for pipeline and rail operators |
| dora | 283 | EU Digital Operational Resilience Act for financial entities |
| nist-ai-rmf | 282 | NIST AI Risk Management Framework functions and practices |

The remaining 20 indexed listings range from 74 to 274 installs and cover the rest of the library: NIST SP 800-53, CIS Controls v8, CMMC 2.0, TISAX, SWIFT CSP, the Australian ISM, NZISM, Cyber Essentials, SOX ITGC, TPRM, CCPA, Vietnam PDPL, EU CRA, ITAR, EAR, CSRD, Section 508, WCAG, and the two country advisors for Saudi Arabia and the UAE.

Coverage is exactly one to one. Thirty-six indexed listings against thirty-six `SKILL.md` files in the current tree, so there is no index drift to warn about, which is rare in this catalog. Each directory follows the same shape, `plugins/<regime>/skills/<regime>/SKILL.md`, so a manual install script can be generated rather than written.

## Why This Matters for Hermes Agents

Compliance work is a citation discipline, and the failure mode of a general agent is fluent invention of control numbers, article references and evidence requirements. A single-purpose skill is the structural fix: the SOC 2 skill can only answer from SOC 2 material, and the EU AI Act skill can only answer from the Act, so the temptation to blend frameworks disappears.

Framework blending is the specific error this prevents. GDPR and CCPA both govern personal data and their obligations diverge in ways that matter, from the lawful basis structure to the breach timeline to the definition of a sale. An agent holding one skill has one framework to answer from, which mirrors how a compliance professional works: you look up the regime that applies, then map it to the business.

The AI regulation skills are the timely set. ISO 42001, the NIST AI Risk Management Framework, the EU AI Act and the EU Cyber Resilience Act are all recent, all moving, and all areas where model memory is thinnest. Having a skill with a monthly update cadence behind each one is the difference between advice grounded in a specific version and advice grounded in whatever the model saw at training time.

The export control pair is a useful signal of seriousness. ITAR and EAR are not topics a marketplace author adds for install counts; they are the regulations that stop a product from shipping. Their presence suggests the collection was built by someone with a compliance remit rather than a content calendar.

The evaluation harness is the last reason. A published benchmark with an assertion count is the only way a buyer can tell a loaded skill collection from an unloaded one. It does not prove the answers are correct, but it makes the claim falsifiable, which is more than a feature list does.

## Usage

| You say | What happens |
|---|---|
| "What SOC 2 criteria apply to our change management process" | Loads the SOC 2 skill and answers against the trust services criteria rather than a generic control list |
| "Do we need a DPIA for this feature" | Applies the GDPR assessment path, covering the trigger conditions and the documentation the assessment needs |
| "Is our chatbot high risk under the EU AI Act" | Works the risk tiering from the Act's categories and states the obligations that follow |
| "Which ISO 27001 Annex A controls cover supplier access" | Maps the question to the control set and describes the evidence an auditor expects |
| "Draft the information security policy sections ISO 27001 expects" | Produces policy structure grounded in the standard's requirements rather than a template from memory |
| "What does HIPAA require for breach notification" | Answers from the breach notification rule with the timing and content requirements stated |
| "Map our current controls to NIST CSF 2.0" | Works the framework functions and categories and reports gaps between what you have and what the framework expects |

## Verification

Each regime sits at `plugins/<regime>/skills/<regime>/SKILL.md`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/main/plugins/soc2/skills/soc2/SKILL.md | head -6
```

It should open with frontmatter carrying the skill name and description, followed by the framework body. After install, confirm the skill count matches rather than sampling:

```bash
ls ~/.hermes/profiles/corpusiq/skills/ | grep -cE '^(iso27001|soc2|gdpr-compliance|fedramp|hipaa-compliance|pci-compliance)$'
```

That should return 6 if you installed the subset installed above. For the full suite the count is 36, and a lower number means the copy or the plugin install did not complete.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| lgpd | Pass | Pass | Pass |
| iso27001 | Pass | Pass | Pass |
| gdpr-compliance | Pass | Pass | Pass |
| soc2 | Pass | Pass | Pass |
| iso42001 | Pass | Pass | Pass |
| nist-csf | Pass | Pass | Pass |
| eu-ai-act | Pass | Pass | Pass |
| dpdpa | Pass | Pass | Pass |
| nis2 | Pass | Pass | Pass |
| pci-compliance | Pass | Pass | Pass |
| iso27701 | Pass | Pass | Pass |
| hipaa-compliance | Pass | Pass | Pass |

Twelve sampled skills, thirty-six clean verdicts. The pattern fits what these skills are: knowledge packages whose job is to tell an agent what a framework requires. The repository is markdown and archives rather than an executing codebase, which is the shape that scans clean.

The caveat worth stating plainly is that a clean scan says nothing about whether the guidance is right. Nothing in this collection is a substitute for a licensed auditor, a lawyer or a notified body, and the repository's own README carries a disclaimer section. Treat output as a well-organised first draft written by someone who has read the standard, then put it in front of the professional who signs the attestation.

## Limitations

- Snapshot data, verified 2026-11-11: 9,363 combined installs across 36 indexed listings; 1,060 GitHub stars; MIT; last pushed 2026-11-07. Counts drift over time.
- The 90 percent against 49 percent benchmark is the author's own evaluation, on 180 test cases graded by agents. It is evidence of effort and a useful signal, not an independent audit.
- Framework text is summarised, not reproduced. For an audit response you still need the published standard, and several of these frameworks are not freely distributable, which limits how completely a skill can quote them.
- Monthly updates mean the skills can lag a regulation change by weeks. The EU AI Act, NIS2 and the Cyber Resilience Act are all in active implementation, so check the version tag against the current text before relying on a timeline.
- No cross-framework mapping is provided. The one-regime-per-skill design prevents blending by construction, which means mapping SOC 2 to ISO 27001 is a task you still do yourself with two skills loaded.
- Jurisdiction coverage follows the author's list. A regime outside it, or a state or provincial rule, has no skill, and the nearest framework skill will answer a question it was not built for.
- These are knowledge skills, so they do not check your infrastructure. Nothing here reads your cloud configuration and tells you which control is failing.

## Related

- [Security Skills - Pentest and Compliance Suite](/hermes/skills/catalog/securityskills-setup)
- [Mastepanoski Skills - UX & AI Compliance Audits Setup](/hermes/skills/catalog/mastepanoski-skills-setup)
- [OpenClaw Security Hardening Setup](/hermes/skills/catalog/openclaw-security-hardening-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the regimes you answer questions about. Thirty-six loaded skills compete for selection on every prompt, and a narrower set triggers far more reliably.
- Load two skills when the question spans regimes, then ask explicitly for the mapping. The SOC 2 to ISO 27001 crosswalk is a real deliverable and the skills will do it if you name both.
- Ask for the article or control number with every answer. When a response cites a specific clause you can check it in seconds, and when it cannot cite one you have found the boundary of the skill.
- Keep the version tag in your change log. A monthly-cadence library means a policy drafted in one month can be out of step with a regulation update in another.
- Use it for the first draft, not the filing. The output is structured enough to shorten the work and not authoritative enough to replace the reviewer who signs it.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
