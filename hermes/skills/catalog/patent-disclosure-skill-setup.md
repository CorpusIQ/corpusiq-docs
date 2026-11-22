---
title: "Handsomestwei Patent Skills - Chinese Patent Suite Setup"
description: "handsomestwei/patent-disclosure-skill: Chinese patent suite for disclosure drafting, reading and office-action response - 1.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/patent-disclosure-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "patents", "intellectual property", "legal"]
---

# Handsomestwei Patent Skills - Chinese Patent Suite Setup

**Source:** [handsomestwei/patent-disclosure-skill](https://www.skills.sh/handsomestwei/patent-disclosure-skill) via skills.sh - 1.4K combined installs across 10 indexed listings; first catalogued Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [handsomestwei/patent-disclosure-skill](https://github.com/handsomestwei/patent-disclosure-skill) - 13,722 stars, MIT, main branch, last pushed Nov 22, 2026; the repository root is the skill root (a top-level `SKILL.md`), with nine sub-skills under `skills/<name>/SKILL.md` plus `prompts/`, `references/`, `tools/` and `tests/` folders each.
**Category:** Intellectual Property and Legal Document Drafting
**Quality Tier:** 🟠 Orange - 3 Fail and 8 Warn cells across 30 sampled verdicts: Gen Agent Trust Hub Fails on patent-disclosure-skill and patent-oa, and a Snyk Fail on patent-map.

Handsomestwei's patent-disclosure-skill is a Chinese-language suite that walks an agent through the full China patent lifecycle: mining patent points from project materials, drafting invention, utility-model and design disclosures, turning disclosures into application documents, reading patents into plain-language notes, answering office actions, and charting claims. The repository root is itself a skill (the suite entry) that routes to nine sub-skills, and the README frames the disclosure path around engineers who did the core work but never wrote the filing, turning code, design docs and meeting notes into a deliverable disclosure with figures and editable Word output.

Install counts concentrate on the flagship: the patent-disclosure-skill listing holds 1,331 of the 1,387 combined installs, while the nine satellite listings sit at 3 to 8 each. The skills, prompts and documentation are written in Chinese and operate on Chinese patent text, so the English descriptions here are renderings of the shipped Chinese material, not the material itself.

## Installation

Clone the repository as one skill root; the top-level `SKILL.md` is the suite entry and the `skills/` subfolders are the nine sub-skills. For Claude Code:

```bash
mkdir -p .claude/skills
git clone https://github.com/handsomestwei/patent-disclosure-skill .claude/skills/patent-disclosure-skill
```

For Cursor, clone the same tree into the global skills directory:

```bash
mkdir -p ~/.cursor/skills
git clone https://github.com/handsomestwei/patent-disclosure-skill ~/.cursor/skills/patent-disclosure-skill
```

The disclosure path needs Python 3.9+ and, for figure rendering and CNIPA search, a local Chrome or Edge browser. Install dependencies from the repository root:

```bash
pip install -r requirements.txt
```

From the skills.sh marketplace you can also install the suite by name; this pulls the whole repository rather than a single sub-skill:

```bash
npx skills add handsomestwei/patent-disclosure-skill
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| patent-disclosure-skill | 1,331 | Suite entry and agent flow across disclosure, application, docket, search, reading, policy and office-action work |
| patent-disclosure | 8 | Invention, utility and design patent point mining, light prior-art search and disclosure drafting with a protective 1+N layout |
| patent-application | 8 | Turn an existing disclosure into claims, specification, abstract and figures, planning parent and divisional cases |
| patent-reader | 7 | Plain-language reading of Chinese or overseas (US, EU, JP, KR) publication numbers or PDFs into notes, graphs and an Obsidian vault |
| patent-search | 6 | Bibliographic search over CNIPA published announcements, with Google Patents for overseas filings |
| patent-oa | 6 | Office-action question answering and draft responses, with historical case intake |
| patent-map | 6 | Patent maps from read Obsidian cases, five chart types with a terrain view |
| patent-exam-policy | 6 | Policy briefings against recent CNIPA positions, flagging form and disclosure changes |
| patent-docket | 6 | One-pass disclosure plus application drafting from inventor materials, with a three-round revision cap |
| patent-chart | 3 | Claim charts that split the independent claim into features and compare against references, products or standards |

All 10 indexed listings clear the 3-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

For agent builders, this suite is a worked example of a legal-facing pipeline with the guardrails an agent needs: the docket skill role-plays a disclosure engineer against a patent attorney and asks for missing technical facts instead of inventing them, and the application skill parks content disputes in an issue list rather than blocking the whole filing. The patent point mining path turns raw engineering inputs, code, design docs, meeting notes and CAD models, into a structured disclosure with figure plans and editable Word output, which is the part of patent work that stalls most technical teams. The reading and map skills compound: each patent read becomes a plain-language note in a private Obsidian vault, and patent-map and patent-chart then turn that accumulated vault into terrain, citation and claim charts. For anyone filing in China, the exam-policy skill keeps disclosures aligned with recent CNIPA positions and flags form changes, and the search skill reaches CNIPA published announcements plus Google Patents for overseas work. The counterweight is the security sample: three Fail cells and eight Warn cells across thirty verdicts, so read each write-capable skill before wiring it to real filings.

## Usage

| You say | What happens |
|---|---|
| Draft an invention disclosure from my project materials | Mines patent points, runs a light prior-art search and drafts the disclosure with figure plans and Word output |
| Turn this disclosure into application documents | Produces claims, specification, abstract and figures, logging any content dispute in an issue list |
| Read this patent and explain it plainly | Converts a Chinese or overseas publication number or PDF into plain-language notes, graphs and an Obsidian note |
| Build a claim chart against this competitor product | Splits the independent claim into features and compares each against the reference, product or standard |
| Draft a response to this office action | Answers the examination opinion and drafts a response, pulling in historical cases when the vault is thin |
| Search CNIPA for filings by this company | Runs a bibliographic search over published announcements, or Google Patents for overseas filings |
| Do the disclosure and application in one pass from these inventor notes | Runs the docket workflow, role-playing engineer versus attorney and asking for any missing fact |

## Verification

Review the suite entry before installing:

```bash
curl -sL https://raw.githubusercontent.com/handsomestwei/patent-disclosure-skill/main/SKILL.md | head -60
```

Review the flagship sub-skill's routing and disclosure prompts:

```bash
curl -sL https://raw.githubusercontent.com/handsomestwei/patent-disclosure-skill/main/skills/patent-disclosure/SKILL.md | head -60
```

Review the install steps and dependency notes:

```bash
curl -sL https://raw.githubusercontent.com/handsomestwei/patent-disclosure-skill/main/INSTALL.md | head -60
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| patent-disclosure-skill | Fail | Warn | Pass |
| patent-disclosure | Warn | Pass | Pass |
| patent-application | Pass | Pass | Warn |
| patent-reader | Pass | Pass | Warn |
| patent-search | Pass | Pass | Pass |
| patent-oa | Fail | Warn | Warn |
| patent-map | Pass | Pass | Fail |
| patent-exam-policy | Pass | Pass | Pass |
| patent-docket | Pass | Pass | Pass |
| patent-chart | Pass | Warn | Warn |

The 10-skill sample carries 3 Fail cells and 8 Warn cells across the 30 verdicts, so treat anything that drafts or edits filings as review-before-write.

## Limitations

- Snapshot data, verified Nov 21, 2026: 1,387 combined installs across 10 indexed listings; 13,722 GitHub stars; MIT; last pushed Nov 22, 2026. Counts drift over time.
- The skills, prompts and documentation are written in Chinese; the English descriptions here are renderings, and agents that run the skills will emit Chinese patent text.
- Install counts are top-heavy: the flagship listing holds 1,331 of the 1,387 combined installs, so the nine sub-skill listings at 3 to 8 installs are lightly exercised.
- The security sample carries 3 Fail cells (Gen Agent Trust Hub on patent-disclosure-skill and patent-oa, Snyk on patent-map) and 8 Warn cells, so review write-capable skills before use.
- The disclosure path depends on Python 3.9+ and a local Chrome or Edge browser for figure rendering and CNIPA search; PDF and STEP/CAD inputs pull in additional optional dependencies.

## Related

- [Claude for Legal Skills - Anthropic Legal Workflow Suite Setup](/hermes/skills/catalog/claude-for-legal-skills-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Huashu Skills - 22-Skill Content Production Pack](/hermes/skills/catalog/huashu-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Keep the whole repository tree: the top-level SKILL.md is the suite entry and the nine skills/ subfolders are the sub-skills, so copying a single subfolder breaks the routing.
- Run the browser probe before a disclosure run; without a local Chrome or Edge the pipeline falls back to Markdown-only and leaves figure code blocks in Word.
- Follow the per-type builders, since utility-model and design filings fill schemas and figure plans rather than the invention mermaid flow.
- Skip matplotlib unless a formula render falls back to OMML text; the default disclosure path does not need it.
- Translate the shipped Chinese prompts before relying on them if your agent is English-first.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
