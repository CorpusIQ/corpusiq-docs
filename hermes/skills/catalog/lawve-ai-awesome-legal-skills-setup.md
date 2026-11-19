---
title: "Lawve AI Legal Skills - Curated Agent Skills for Legal Work"
description: "lawve-ai/awesome-legal-skills: 4.4K combined installs across 96 listings; a curated list of agent skills for automating legal work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/lawve-ai-awesome-legal-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "legal tech", "contract review", "compliance"]
---

# Lawve AI Legal Skills - Setup Guide

**Source:** [lawve-ai/awesome-legal-skills](https://www.skills.sh/lawve-ai/awesome-legal-skills) via skills.sh - 4.4K combined installs across 96 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 964 stars, `main` branch, last pushed 2026-10-19. The GitHub API reports NOASSERTION for the licence while the README licences the list itself under CC BY-NC-ND 4.0; each listed skill carries its own licence terms. Skills live at `skills/<name>/SKILL.md`.
**Category:** Legal technology, contract review, and regulatory compliance
**Quality Tier:** 🟠 Orange - Fail verdicts on docx-processing-superdoc (Gen Agent Trust Hub) and skill-optimizer-lawvable (Snyk); licence field NOASSERTION.

Lawve AI's awesome-legal-skills is a curated list of agent skills for automating legal work, assembled from contributions by practicing lawyers, in-house counsel, academics, and legal technologists. The README states the repo is synced periodically from lawve.ai, which publishes new skills first, and that the collection is built on portable open standards rather than proprietary agent formats.

The repo's README catalogues 276 skills across 28 categories (AI governance, commercial law, compliance, data protection, litigation, legal research, and more), while skills.sh indexes 96 of them. The indexed names are skill slugs that do not always match the directory names in the tree: for example, the indexed `nda-review-jamie-tso` corresponds to the directory `skills/nda-reviewer-jamie-tso/`, and the indexed `docx-processing-superdoc` to `skills/word-editor-superdoc/`.

## Installation

Install the whole curated list:

```bash
npx skills add lawve-ai/awesome-legal-skills
```

Or install a single skill by name (the command skills.sh publishes):

```bash
npx skills add https://github.com/lawve-ai/awesome-legal-skills --skill contract-review-anthropic
```

Skills run under Claude Code, Codex, and other agents that read SKILL.md files.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| mediation-dispute-analysis | 264 | Analyze a dispute for mediation: review case materials, identify issues, and summarize each party's position. |
| contract-review-anthropic | 175 | Review contracts against a negotiation playbook, flag deviations, and generate redline suggestions. |
| privacy-policy-malik-taiar | 147 | Draft GDPR-compliant privacy policies using CNIL recommendations and a reference template. |
| legal-simulation-patrick-munro | 132 | Demonstrate AI capabilities in legal contexts with personas across tenant law, contracts, and disputes. |
| outlook-emails-lawvable | 125 | Read, search, and download Outlook emails and attachments via OAuth2 for legal work. |
| legal-risk-assessment-anthropic | 116 | Classify legal risks with a severity-by-likelihood framework and escalation criteria. |
| vendor-due-diligence-patrick-munro | 116 | Assess IT vendors and third-party partners with risk scoring under DORA, NIS2, and GDPR. |
| tech-contract-negotiation-patrick-munro | 114 | Negotiate technology services agreements with a three-position framework and German/EU law specificity. |
| statute-analysis-rafal-fryc | 97 | Read, interpret, and apply statutes, regulations, and rules in legal and compliance work. |
| tabular-review-lawvable | 94 | Analyze multiple PDF and DOCX documents against user-defined columns and produce cited Excel output. |
| gdpr-privacy-notice-eu-oliver-schmidt-prietz | 92 | Draft GDPR-compliant privacy notices as .docx for any EU/EEA jurisdiction and audience. |
| xlsx-processing-manus | 91 | Create Excel spreadsheets with a focus on aesthetics and data analysis. |
| docx-processing-openai | 88 | Read, edit, and create Word documents with visual quality control. |
| assignation-refere-recouvrement-creance-selim-brihi | 88 | Draft French summary-proceeding writs to recover unpaid commercial debts. |
| docx-processing-superdoc | 86 | Edit, query, and transform Word documents with the SuperDoc CLI. |
| docx-processing-anthropic | 86 | Create, read, edit, and manipulate Word .docx documents. |
| nda-review-jamie-tso | 85 | Review one-way commercial NDAs clause by clause with redlines, fallbacks, and rationales. |
| compliance-anthropic | 85 | Navigate GDPR and CCPA, review DPAs, and handle data subject requests. |

The remaining 78 indexed listings range from 8 to 83 installs.

## Why This Matters for Hermes Agents

For an agent doing legal work, this list is a catalogue of the highest-traffic legal skills rather than a single opinionated suite, which makes it a useful map of what practitioners actually reach for: contract review and playbooks, NDA triage, GDPR notices and DPAs, vendor due diligence, and mediation analysis lead the install counts. The per-skill descriptions are short and trigger-oriented, so an agent can route a legal request to the right skill by reading the frontmatter description.

Two properties matter for builders. First, the list is explicitly a redistribution of third-party work: every listed skill has its own author, licence, and terms, and the list itself is CC BY-NC-ND 4.0, which forbids distributing modified versions or commercial use of the list. Second, several indexed slugs do not match directory names in the tree, so if you install or cite a specific skill, resolve the directory name from the repo before assuming the slug is the path.

The top of the index skews heavily toward document processing and contract review, while the long tail covers niche jurisdictions and frameworks, so treat the install counts as popularity among legal agents, not a quality ranking.

## Usage

| You say | What happens |
|---|---|
| "Review this NDA" | nda-review-jamie-tso produces a clause-by-clause issue log with redlines and fallbacks. |
| "Check this contract against our playbook" | contract-review-anthropic flags deviations and generates redline suggestions. |
| "Do vendor due diligence on this provider" | vendor-due-diligence-patrick-munro runs the DORA, NIS2, and GDPR assessment framework. |
| "Draft a GDPR privacy notice for our EU site" | gdpr-privacy-notice-eu-oliver-schmidt-prietz produces a .docx notice for the target jurisdiction. |
| "Analyze this dispute for mediation" | mediation-dispute-analysis reviews the case materials and summarizes each party's position. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/lawve-ai/awesome-legal-skills/main/skills/vendor-due-diligence-patrick-munro/SKILL.md
```

Then install the list or a single skill and confirm the skill lands in your agent's skills directory.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| mediation-dispute-analysis | Pass | Pass | Pass |
| contract-review-anthropic | Pass | Pass | Pass |
| privacy-policy-malik-taiar | Pass | Pass | Warn |
| legal-simulation-patrick-munro | Pass | Pass | Pass |
| outlook-emails-lawvable | Pass | Pass | Warn |
| legal-risk-assessment-anthropic | Warn | Pass | Pass |
| vendor-due-diligence-patrick-munro | Pass | Pass | Pass |
| tech-contract-negotiation-patrick-munro | Pass | Pass | Pass |
| statute-analysis-rafal-fryc | Pass | Pass | Warn |
| tabular-review-lawvable | Pass | Pass | Pass |
| gdpr-privacy-notice-eu-oliver-schmidt-prietz | Pass | Pass | Pass |
| xlsx-processing-manus | Pass | Pass | Pass |
| docx-processing-openai | Pass | Pass | Warn |
| assignation-refere-recouvrement-creance-selim-brihi | Pass | Pass | Pass |
| docx-processing-superdoc | Fail | Pass | Warn |
| docx-processing-anthropic | Warn | Pass | Pass |
| nda-review-jamie-tso | Pass | Pass | Pass |
| compliance-anthropic | Pass | Pass | Pass |
| skill-optimizer-lawvable | Pass | Pass | Fail |
| red-team-verifier-patrick-munro | Pass | Pass | Warn |

The sample covers 20 of 96 indexed listings; docx-processing-superdoc carries a Gen Agent Trust Hub Fail and skill-optimizer-lawvable a Snyk Fail.

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,399 combined installs across 96 indexed listings; 964 GitHub stars; NOASSERTION licence field; last pushed 2026-10-19. Counts drift over time.
- Licensing is split: the GitHub API reports NOASSERTION while the README licences the list itself under CC BY-NC-ND 4.0 (no modified versions, no commercial use of the list), and every listed skill carries its own licence terms from its own author.
- Indexed skill slugs do not always match tree directories; for example `nda-review-jamie-tso` maps to `skills/nda-reviewer-jamie-tso/` and `docx-processing-superdoc` to `skills/word-editor-superdoc/`, so resolve the directory before fetching a specific SKILL.md.
- The list is a redistribution of third-party skills; the repo takes no responsibility for them and instructs you to check each skill against your firm's confidentiality and professional responsibility obligations before use.
- Several skills are non-English (French and Italian procedure and research skills), so match the skill to the jurisdiction you are actually working in.

## Related

- [Claude for Legal Skills - Anthropic Legal Workflow Suite Setup](/hermes/skills/catalog/claude-for-legal-skills-setup)
- [Privacy and Data Protection Skills - 282 Procedures](/hermes/skills/catalog/privacy-data-protection-skills-setup)
- [GRC Skills - Governance, Risk and Compliance Suite](/hermes/skills/catalog/grc-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install individual skills by their skills.sh slug; the slug is what `npx skills add` accepts even when the directory name differs.
- Read each skill's own licence before redistribution; the list is CC BY-NC-ND 4.0 and forbids distributing modified versions.
- For contract work, start with contract-review-anthropic and nda-review-jamie-tso; they are the highest-traffic review skills in the index.
- Prefer the official upstream for the document-processing skills (the OpenAI, Anthropic, Manus, and SuperDoc entries) if you want the maintained versions.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
