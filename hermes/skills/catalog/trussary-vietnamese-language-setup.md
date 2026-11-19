---
title: "Trussary Vietnamese Language - Professional Copy Setup"
description: "trussary/vietnamese-language-skill: 1.0K combined installs across 5 listings; Vietnamese copywriting, tech, business, finance, and education skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/trussary-vietnamese-language-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "vietnamese", "localization", "copywriting"]
---

# Trussary Vietnamese Language - Professional Copy Setup

**Source:** [trussary/vietnamese-language-skill](https://www.skills.sh/trussary/vietnamese-language-skill) via skills.sh - 1.0K combined installs across 5 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 106 stars, MIT licence, `main` branch, last pushed 2026-09-03. Five skills under skills/, each a self-contained SKILL.md with references, assets, and a validate_copy.py linter, plus a shared/ validator engine copied into each folder.
**Category:** Vietnamese localization and copywriting
**Quality Tier:** 🟡 Yellow - 4 Warns across 5 sampled skills; MIT licence.

Vietnamese is a low-resource language for LLMs. Unguided output is fluent-sounding translationese: English word order, the wrong pronoun for the audience, literal CTAs, advertising superlatives that are illegal under Vietnamese law, and currency formatted the American way. trussary/vietnamese-language-skill fixes that with five skills that write Vietnamese a professional would actually ship.

Each skill covers one register - landing pages, engineering docs, business comms, finance, and education - and ships its own linter (validate_copy.py) plus a shared rule engine. The skills trigger on keywords and are independently installable, so you can take only the ones you need.

## Installation

```bash
npx skills add trussary/vietnamese-language-skill
```

Useful flags: --list to preview what is in the repo, -g for a global install, and -a '*' --all for every agent with no prompts. Then npx skills list to confirm and npx skills update to pull newer versions.

Claude Code plugin: /plugin marketplace add trussary/vietnamese-language-skill. Or copy a folder directly: cp -r skills/vietnamese-landing-copy ~/.claude/skills/. Each folder is self-contained, and npx skills use trussary/vietnamese-language-skill@vietnamese-landing-copy tries one skill in a single session without installing.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| vietnamese-tech-writing | 242 | Write and review native-quality Vietnamese engineering and product docs - commits, PRs, RFCs, design docs, READMEs, API docs, UI microcopy, and i18n files - with code-switching and vi-VN i18n hazard rules. |
| vietnamese-landing-copy | 200 | Write and review Vietnamese landing-page copy, especially real-estate project pages plus SaaS and e-commerce, fixing translationese, wrong pronouns, calqued CTAs, and locale formatting. |
| vietnamese-business-comms | 199 | Write and review Vietnamese marketing and sales copy - email campaigns, Zalo templates, ads, marketplace listings, press releases, and quotes - with pronoun and promotion-law rules. |
| vietnamese-education-copy | 189 | Write and review Vietnamese school, academic, and EdTech copy - report-card remarks, parent notices, syllabi, transcripts, and pronunciation feedback - with MoET grading terms. |
| vietnamese-finance-copy | 183 | Write and review Vietnamese finance copy - e-invoices, financial statements, investor updates, and fintech or insurance product copy - with statement terminology and promotion limits. |

No indexed listings fall below the threshold; all 5 appear above.

## Why This Matters for Hermes Agents

Localization is where generic models fail visibly: a landing page with the wrong pronoun or an illegal superlative reads as machine-translated and can draw regulator attention. These skills encode the native conventions - the right pronoun for the audience, legal promotion limits, Vietnamese number and date formatting - so the output is publication-ready rather than fluent-but-wrong.

The linter is the differentiator for an agent pipeline. Each skill ships validate_copy.py that runs without a model, so a batch of copy can be checked for calques, register mistakes, mixed tone marks, and formatting errors before it ships. Rules that only apply to one document type are gated behind --doctype, so the linter stays switched on instead of firing noise.

All five are plain SKILL.md files with a shared rule engine copied into each folder, so a harness that reads skill files, including Hermes, can load them directly. The linter needs Python 3.9 or later, standard library only.

## Usage

| You say | What happens |
|---|---|
| "Write a landing page for our apartment project in District 7" | vietnamese-landing-copy writes copy with the right pronouns and register, and flags illegal superlatives. |
| "Our Vietnamese README reads like Google Translate" | vietnamese-tech-writing fixes machine-translation tells and decides which English terms stay English. |
| "Draft a sales email with a VAT quote" | vietnamese-business-comms applies B2B pronouns and promotion-law limits to the email and quote. |
| "Can we advertise a guaranteed 12 percent annual return in Vietnam?" | vietnamese-finance-copy flags the guaranteed-return language and routes it to legal review. |
| "Write report-card remarks for a grade 9 math class" | vietnamese-education-copy applies current grading terms and the right teacher-student register. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/trussary/vietnamese-language-skill/main/skills/vietnamese-tech-writing/SKILL.md
```

Then run a skill's linter directly to confirm it works without a model:

```bash
python skills/vietnamese-tech-writing/scripts/validate_copy.py CHANGELOG.md --doctype commit
```

Python 3.9 or later, standard library only, no install step.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| vietnamese-tech-writing | Pass | Warn | Pass |
| vietnamese-landing-copy | Warn | Warn | Pass |
| vietnamese-business-comms | Pass | Pass | Pass |
| vietnamese-education-copy | Pass | Warn | Pass |
| vietnamese-finance-copy | Pass | Pass | Pass |

The sample covers all 5 indexed listings; four cells carry Warns (Socket on four skills, Gen Agent Trust Hub on vietnamese-landing-copy), and every other cell passes.

## Limitations

- Snapshot data, verified Nov 19, 2026: 1,013 combined installs across 5 indexed listings; 106 GitHub stars; MIT licence; last pushed 2026-09-03. Counts drift over time.
- The linter needs Python 3.9 or later; it is standard library only but still a Python requirement.
- Legal references in the skills are copywriting guidance, not legal advice; the finance skill routes regulated phrasing to review rather than editing around it.
- Shared rule files are copied into each skill, not symlinked; edit shared/ and run the sync script, never the per-skill copies.

## Related

- [Korean Skills - Hangul Writing and Style Checks](/hermes/skills/catalog/korean-skills-setup)
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)
- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the linter on a batch before publishing; it catches calques and formatting the model cannot see.
- Pick one skill per document type; the skills point to each other for the wrong register rather than guessing.
- Use npx skills use ...@vietnamese-landing-copy to try one skill in a session before committing to an install.
- Edit shared/ and run tools/sync_shared.py, never the copied references, or CI will flag the drift.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
