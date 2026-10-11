---
title: "Mastepanoski Skills - UX & AI Compliance Audits Setup"
description: "Setup guide for mastepanoski/claude-skills - 6.3K combined installs. UX audits, accessibility checks, and AI governance reviews: WCAG, OWASP, and NIST."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mastepanoski-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "ux audit", "accessibility", "ai governance"]
---

# Mastepanoski Skills - Setup Guide

**Source:** [mastepanoski/claude-skills](https://www.skills.sh/mastepanoski/claude-skills) via skills.sh - 6.3K combined installs across 13 indexed listings; first seen Aug 19, 2026 (evening sweep); converted Oct 10, 2026 (zero-catalog audit)
**GitHub:** [mastepanoski/claude-skills](https://github.com/mastepanoski/claude-skills) (54 stars, MIT license; pushed Oct 10, 2026; `skills/<name>/SKILL.md` layout; v1.9.0)
**Category:** UX Audits / Accessibility / AI Compliance
**Quality Tier:** 🟡 Beta - independent UX/AI-governance audit suite (54 stars, MIT); named as an upstream publisher in the podo catalog; mixed sampled verdicts

Publisher mastepanoski ships a 13-skill audit suite (v1.9.0, MIT) for AI coding assistants, split across two concerns. The UX half grounds evaluations in named methodologies: Nielsen's 10 usability heuristics, Don Norman's principles from The Design of Everyday Things, cognitive walkthroughs, WCAG 2.1/2.2 conformance, and information architecture. The AI half covers governance and security against the frameworks reviewers now expect to see cited: ISO 42001, NIST AI RMF, the OWASP Top 10 for LLM Applications, the OWASP AI Testing Guide, and GDPR.

The skills are plain SKILL.md folders that follow the Agent Skills standard, so they run under Claude Code, Codex, ChatGPT, or any compatible agent with no vendor-specific variants. wcag-accessibility-audit (1,514) and ui-design-review (1,097) lead the 6.3K combined installs, and the publisher is also named as an upstream source in the podo design catalog's redistribution disclosure, which speaks to how far these audits travel.

---

## Installation

Prerequisites: Node.js for the skills CLI. Install into your assistant with `npx skills`, or copy the folders into the layout your agent scans (`.claude/skills/` for Claude Code, `.codex/skills/` for Codex).

```bash
# List all available skills
npx skills add mastepanoski/claude-skills --list

# Install one skill (for example the WCAG audit), or the whole set
npx skills add mastepanoski/claude-skills --skill wcag-accessibility-audit
npx skills add mastepanoski/claude-skills
```

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| wcag-accessibility-audit | 1,514 | WCAG 2.1/2.2 audit with POUR principles and A/AA/AAA conformance for ADA and Section 508 work |
| ui-design-review | 1,097 | Visual design review across typography, color, spacing, consistency, and branding |
| ux-audit-rethink | 811 | Holistic UX audit using the Interaction Design Foundation's 7 factors and 5 usability characteristics |
| nielsen-heuristics-audit | 694 | Usability inspection against Nielsen's 10 heuristics with 0-4 severity ratings |
| cognitive-walkthrough | 423 | Novice-user walkthroughs of signup flows and other critical tasks |
| owasp-llm-top10 | 382 | LLM and GenAI security audit against the OWASP Top 10 for LLM Applications |
| don-norman-principles-audit | 356 | Interface evaluation using Don Norman's 7 principles from The Design of Everyday Things |
| iso-42001-ai-governance | 279 | AI system governance audit against ISO 42001:2023 with EU AI Act and GDPR considerations |
| owasp-ai-testing | 226 | Trustworthiness testing from the OWASP AI Testing Guide: 32 test cases across application, model, infrastructure, and data |
| nist-ai-rmf | 226 | AI risk assessment using the NIST AI RMF govern, map, measure, and manage functions |
| ai-assessment-scale | 219 | Measure AI contribution with the 5-level AI Assessment Scale framework and disclosure guidance |

The remaining 2 indexed listings range from 1 to 85 installs: gdpr-audit (85) and information-architecture-audit (1).

## Why This Matters for Hermes Agents

User-facing work ships with defects that generic code review does not catch: contrast failures, inconsistent labeling, flows that only make sense to their authors. This suite packages the standard audit methodologies behind those checks so an agent can run them against a URL, a screenshot, or a component before release. The AI-governance half matters for any team shipping model-backed features into regulated contexts, because ISO 42001, NIST AI RMF, and the OWASP frameworks are the references reviewers and customers now ask about. Because every skill is a plain SKILL.md folder, the same audits run under Claude Code, Codex, or any compatible agent, and each installs independently, so a Hermes agent can add exactly the checks its project needs. The publisher's upstream role in the podo design catalog is also a signal that these audit skills travel beyond their home repo.

## Usage

| You say | What happens |
|---|---|
| "Audit my login page against WCAG AA" | wcag-accessibility-audit runs the POUR analysis and flags conformance gaps |
| "Check this dashboard against Nielsen's heuristics" | nielsen-heuristics-audit reports usability problems with 0-4 severity ratings |
| "Walk through the signup flow as a new user" | cognitive-walkthrough simulates novice cognition step by step |
| "Review the visual design of my landing page" | ui-design-review evaluates typography, color, spacing, consistency, and branding |
| "Assess our chatbot for OWASP LLM risks" | owasp-llm-top10 audits prompt injection, data leakage, and the rest of the 2025 list |
| "Prepare an AI governance review" | iso-42001-ai-governance and nist-ai-rmf check governance and risk against ISO and NIST |
| "Show how much AI is in this project" | ai-assessment-scale maps the contribution onto the 5-level AI Assessment Scale |

## Verification

```bash
# Confirm the install through the skills CLI
npx skills list | grep -i mastepanoski

# Or check the skills directory your agent scans
ls ~/.claude/skills/ | grep -E 'wcag-accessibility-audit|ui-design-review'

# Review the wcag-accessibility-audit skill from GitHub before installing
curl -sL https://raw.githubusercontent.com/mastepanoski/claude-skills/main/skills/wcag-accessibility-audit/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| wcag-accessibility-audit | Pass | Pass | Warn |
| ui-design-review | Pass | Pass | Warn |
| nielsen-heuristics-audit | Pass | Pass | Warn |

## Limitations

- Small repository: 54 GitHub stars, maintained by a single independent author; treat it as a focused audit toolkit rather than an ecosystem.
- Verdict coverage is partial and the sampled skills carry Snyk Warns; re-check each skill's security page before production use.
- Audit skills are only as good as the context you supply; feed them a URL, screenshot, or component code for a useful report.
- gdpr-audit ships an explicit disclaimer that its output is a technical audit, not legal advice or a compliance determination.
- Snapshot data, verified Oct 10, 2026: 6,313 combined installs across 13 indexed listings; 54 GitHub stars; MIT; last pushed Oct 10, 2026. Counts drift over time.

## Related

- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup) - another accessibility-audit skill set for WCAG 2.2 work
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup) - a complementary visual UI review flow
- [Podo Design Agent Skills - 151-Skill Design Catalog Setup](/hermes/skills/catalog/podo-design-agent-skills-setup) - podo catalog; mastepanoski is named as an upstream publisher in its redistribution disclosure
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with ux-audit-rethink for a comprehensive pass, then drill into the specialized audits it points to.
- Share the artifact first: paste the URL, screenshot, or component code before asking for an audit.
- Run wcag-accessibility-audit when compliance is the question; reach for ui-design-review when polish and consistency are.
- For AI features, sequence governance (iso-42001-ai-governance), risk (nist-ai-rmf), and security (owasp-llm-top10).
- Install per-skill with `--skill` so your agent's skill list stays focused on the audits you actually run.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
