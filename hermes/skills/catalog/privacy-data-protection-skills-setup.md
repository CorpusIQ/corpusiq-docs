---
title: "Privacy and Data Protection Skills - 282 Procedures"
description: "mukul975/privacy-data-protection-skills: 4.3K combined installs across 96 listings for GDPR, CCPA, EU AI Act and HIPAA procedures"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/privacy-data-protection-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "privacy", "compliance", "gdpr"]
---

# Privacy and Data Protection Skills - Setup Guide

**Source:** [mukul975/privacy-data-protection-skills](https://www.skills.sh/mukul975/privacy-data-protection-skills) via skills.sh - 4.3K combined installs across 96 indexed listings; first seen May 12, 2026 (Nov 12, 2026 sweep)
**GitHub:** 336 stars, Apache-2.0 license, `main` branch, last pushed 2026-03-16, 283 unique skill folders published at the top level and inside 21 Claude Code plugin bundles, 824 `SKILL.md` files in total
**Category:** Privacy and data protection: GDPR, EU AI Act, ePrivacy, CCPA/CPRA, HIPAA, LGPD, PIPL, DPDP and twelve other jurisdictions
**Quality Tier:** 🟡 Established - a systematic, permissively licensed database with clean scanner results, held back by a flat install profile and a repository that has not been pushed since March.

This is a compliance procedure library, not a legal advisor. Every skill takes one obligation and writes out the operational steps: what triggers it, what evidence it needs, what the deliverable looks like, and which article it derives from. The GDPR set alone covers audits, impact assessments, data processing agreements, subject access requests, breach notification, automated decision rights and retention and erasure.

The structure is a top-level `skills/` directory with 283 folders, republished inside 21 Claude Code plugin bundles, which is why the tree carries 824 `SKILL.md` files for a library the README counts at 282 skills. That is duplication rather than drift: the same procedure appears once at the top level and once per bundle that includes it.

Coverage is the reason to look at it. GDPR, the EU AI Act and the ePrivacy Directive are the deepest at 50, 15 and 12 skills. Then CCPA/CPRA, HIPAA and 13 US state privacy laws, followed by LGPD, PIPL, India's DPDP Act, APPI, PIPA, both PDPAs, POPIA and the Australian Privacy Act. For a business that sells into more than one jurisdiction, having the same procedure shape applied to five regimes is more useful than having one regime documented beautifully.

Install counts are the flattest in any pack in this catalog. The top skill draws 65 installs and the floor of the indexed set is 40, so the library is being installed as a set rather than skill by skill.

## Installation

The README's quick start is a clone and a read, which is the honest way to use a compliance library:

```bash
git clone https://github.com/mukul975/Privacy-Data-Protection-Skills.git
cd Privacy-Data-Protection-Skills/skills/privacy/conducting-gdpr-dpia
cat SKILL.md
```

For Claude Code, the repository is a plugin marketplace with 21 installable bundles:

```bash
/plugin marketplace add mukul975/Privacy-Data-Protection-Skills
/plugin install privacy-skills-complete@privacy-data-protection-skills
```

An agent that reads skills from a directory can take the top-level folders directly:

```bash
cp -r Privacy-Data-Protection-Skills/skills/* ~/.claude/skills/
```

Choose the bundle over the full copy if your agent loads skill indexes eagerly: 283 folders of regulatory text is a large context surface, and a GDPR-only bundle is usually the right scope.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| brazil-lgpd | 65 | LGPD compliance: the 10 lawful bases, DPO appointment and Brazilian regulator obligations. |
| analytics-cookie-consent | 61 | Consent for analytics cookies, GA4 privacy configuration and consent mode. |
| gdpr-compliance-audit | 54 | Organisational audit against GDPR Articles 5, 24, 25, 28, 30, 32 and 35. |
| audit-report-writing | 51 | Privacy audit reports: executive summary, findings classification and evidence handling. |
| conducting-gdpr-dpia | 50 | End-to-end Data Protection Impact Assessment under Article 35, including trigger checks. |
| dpa-drafting | 49 | Article 28(3) data processing agreements with all eight mandatory provisions. |
| canada-pipeda | 49 | PIPEDA compliance and the ten fair information principles. |
| backup-retention-erasure | 49 | Retention schedules and erasure obligations, including the backup infeasibility exception. |
| breach-72h-notification | 48 | Article 33 breach notification inside the 72 hour window, with the decision trail. |
| automated-decision-rights | 48 | Article 22 rights over solely automated decisions and profiling. |
| data-localization | 47 | Country-level localisation duties across Russia 242-FZ, China PIPL and similar regimes. |
| dsar-processing | 47 | Article 15 subject access requests from identity verification to response. |
| audit-sampling-methods | 47 | Statistical and non-statistical sampling for a privacy audit. |
| ai-transparency-reqs | 47 | AI transparency duties across EU AI Act Articles 13 and 14 and GDPR Articles 13 and 14. |
| ai-model-privacy-audit | 47 | Model privacy testing: extraction, membership inference and inversion checks. |
| anonymization-alternative | 47 | Anonymisation assessed under Recital 26 with the WP29 technique set. |

The remaining 80 indexed listings range from 40 to 46 installs.

Because the install band is narrow, the ranking says more about which procedures people reach for first than about quality. Consent configuration and the compliance audit lead; the jurisdictional and AI-specific procedures follow.

## Why This Matters for Hermes Agents

Privacy work is procedural, and procedure is where agents fail in a specific and expensive way. Ask for a DPIA and a good model will produce something that looks like a DPIA: a document with sections, risk language and a recommendation. What makes a DPIA defensible is not its shape. It is whether the processing was actually described, whether the necessity and proportionality test was applied to that description, and whether the mitigations map to the risks that were identified.

A skill that walks the article fixes the order and demands the missing inputs. The same holds for a data processing agreement: the eight mandatory Article 28(3) provisions are a checklist, and an agent writing from general knowledge will produce a contract that misses one or two of them in a way that reads fine.

The second value is consistency across jurisdictions. A business that handles EU and Brazilian personal data needs two procedures with one shape. When the same author writes the LGPD skill and the GDPR skill, the deliverable structure stays comparable, which is what makes a compliance program reviewable by someone who is not a specialist in both regimes.

The limit is the one that matters most. These are procedures, not legal advice, and they are eight months old. A supervisor's guidance published after March 2026 is not in them. Use the skill to run the process and to produce a complete first draft, then have someone qualified check the current state of the law.

## Usage

| You say | What happens |
|---|---|
| "Run a GDPR compliance audit for this company" | Applies the audit procedure across the listed articles and produces findings with evidence requests. |
| "Do we need a DPIA for this feature?" | Checks the Article 35 triggers against the described processing before drafting anything. |
| "Draft the DPA for this vendor" | Produces a processing agreement with all eight Article 28(3) provisions and placeholders for the specifics. |
| "We had a breach, what do we do in the next 72 hours?" | Runs the notification procedure: assessment, supervisory authority notice, decision trail. |
| "Someone sent a subject access request" | Walks the Article 15 workflow from identity verification to the response. |
| "Which consent settings do we need for analytics?" | Applies the cookie consent skill to the analytics stack and the consent mode configuration. |
| "We are launching an AI feature in the EU, what has to be documented?" | Uses the AI transparency and model privacy skills to list the duties and the tests. |

## Verification

The top-level skills directory is the clean install path. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/mukul975/Privacy-Data-Protection-Skills/main/skills/privacy/conducting-gdpr-dpia/SKILL.md | head -6
```

The plugin bundles carry the same skill at a different path, which is the duplication that produces 824 files for 283 skills:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/mukul975/Privacy-Data-Protection-Skills/main/plugins/gdpr-compliance-skills/skills/gdpr-compliance-audit/SKILL.md
```

After installing, confirm one folder per procedure and check that the frontmatter carries the regulation and the article. If your agent loads every skill into context, install the bundle rather than the whole tree.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| brazil-lgpd | Pass | Pass | Pass |
| analytics-cookie-consent | Pass | Pass | Pass |
| gdpr-compliance-audit | Pass | Pass | Pass |
| audit-report-writing | Pass | Pass | Pass |

All four sampled skills pass all three scanners, which is what a text-only procedure library should look like. There is no network access, no credential handling and no data exfiltration surface in the skill bodies.

The real risk is misuse rather than compromise: taking a procedure's output as legal advice, or applying a jurisdiction's rules to the wrong jurisdiction. A scanner cannot flag either. The mitigation is procedural: every deliverable from this pack should name the regulation, the article and the date of the source guidance, so a reviewer can check it.

## Limitations

- Snapshot data, verified 2026-11-12: 4,267 combined installs across 96 indexed listings; 336 GitHub stars; Apache-2.0 license; last pushed 2026-03-16. Counts drift over time.
- 96 is the cap of the skills.sh search API. The repository carries 283 unique skill folders, so both the indexed family and the combined install figure are floors.
- The tree has 824 `SKILL.md` files because each of the 283 procedures is republished inside 21 plugin bundles. Counting files overstates the library by roughly three times.
- The repository has not been pushed since March 2026. Regulatory guidance that changed after that date is not reflected, and privacy law moves faster than most domains.
- These are procedures, not legal advice, and no skill in the pack is a substitute for a qualified review of the current rules in your jurisdiction.
- Install counts are flat and low relative to tool packs: the top skill is 65. There is no large user base filing issues, so defects surface when you read the procedure rather than from a crowd.

## Related

- [GRC Skills - Governance, Risk and Compliance Suite](/hermes/skills/catalog/grc-skills-setup)
- [Mastepanoski Skills - UX & AI Compliance Audits Setup](/hermes/skills/catalog/mastepanoski-skills-setup)
- [Cybersecurity Skills - 42 Audit and Pentest Skills](/hermes/skills/catalog/briiirussell-cybersecurity-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the jurisdiction bundle, not the whole tree. A GDPR bundle gives an agent the procedures it can apply; 283 folders give it a reason to pick the wrong regime.
- Ask for the article citations in the output. Every procedure is anchored to one, and an agent that cannot name it has drifted off the method.
- Use the audit procedures to produce findings and the report skill to package them. The two are written as a pair, and the findings format from the audit is what the report skill expects.
- Run the AI-specific skills before an AI feature ships rather than after. Transparency duties and model privacy testing are cheaper to satisfy at design time.
- Check the current law before signing anything generated from this pack. The repository is eight months stale and a procedure's structure survives a regulatory update better than its specifics do.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
