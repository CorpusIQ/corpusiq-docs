---
title: "Skills IL Localization - Hebrew and RTL Skills Setup"
description: "skills-il/localization - 2.6K combined installs: AI agent skills for Hebrew, RTL, translation, and cultural adaptation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/skills-il-localization-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "hebrew", "rtl", "localization", "israel"]
---

# Skills IL Localization - Setup Guide

**Source:** [skills-il/localization](https://www.skills.sh/skills-il/localization) via skills.sh - 2.6K combined installs across 16 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [skills-il/localization](https://github.com/skills-il/localization) - 28 stars, MIT license, last pushed Nov 8, 2026, master branch; 14 skill directories, each holding a SKILL.md plus a SKILL_HE.md Hebrew-language variant alongside scripts, references, and evidence.json files.
**Category:** Hebrew, RTL, Translation and Israeli Market Adaptation
**Quality Tier:** 🟡 Yellow - 16 of 16 listings sampled: thirteen pass all three checks, and three carry a single Snyk Warn each (accessibility compliance, flight finder, travel planner).

skills-il/localization is the Hebrew-language arm of Skills IL, a curated collection of AI agent skills for Israeli developers, published under the MIT license. The suite spans Hebrew content writing, RTL web layout, i18n, NLP, document generation, OCR, and accessibility compliance, alongside consumer and travel helpers such as apartment hunting, wedding planning, and flight finding.

It is a focused, single-market family: 2,631 combined installs across 16 indexed listings, with the top skill (hebrew-rtl-best-practices) at 796 installs. The family mixes engineering skills (RTL best practices, i18n, the Tailwind preset, accessibility compliance, OCR) with consumer and travel helpers, and two indexed listings (israeli-flight-finder and israeli-travel-planner) carry install counts but have no matching directory in the current tree.

## Installation

The README documents a Claude Code install command for a single skill and a full-repo clone:

```bash
# Claude Code - install a specific skill
claude install github:skills-il/localization/hebrew-rtl-best-practices

# Or clone the full repo
git clone https://github.com/skills-il/localization.git
```

Point claude install at any skill path under the repo to install that one skill. Cloning the repo gives every skill directory with its SKILL.md, scripts, and references for manual copy or symlink into the agent skills directory.

## What It Provides

skills.sh publishes per-skill install counts for all 16 indexed listings. The 11 most-installed skills are listed below; the remaining 5 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| hebrew-rtl-best-practices | 796 | implement RTL layouts for Hebrew web apps: CSS logical properties, Tailwind RTL, icon mirroring, and Hebrew typography |
| hebrew-content-writer | 501 | write and edit professional Hebrew copy: grammar, register, gendered language, and Hebrew SEO |
| israeli-accessibility-compliance | 278 | implement Israeli web accessibility per the IS 5568 standard for Hebrew RTL apps |
| hebrew-document-generator | 256 | generate Hebrew PDF, DOCX, and PPTX with correct RTL layout and bidi handling |
| hebrew-tailwind-preset | 240 | configure Tailwind CSS v4 for Hebrew RTL with dir variants and logical property utilities |
| shabbat-aware-scheduler | 186 | schedule meetings and deployments around Shabbat, chagim, and the Hebrew calendar |
| hebrew-i18n | 78 | implement Hebrew i18n: plural forms, date and number formatting, and RTL CSS |
| israeli-ui-design-system | 75 | build RTL-first UI component libraries and design systems with Hebrew typography |
| hebrew-nlp-toolkit | 53 | guide Hebrew NLP work with DictaLM, DictaBERT, AlephBERT, and ivrit.ai |
| hebrew-ocr-forms | 41 | OCR scanned Israeli government forms such as Tabu and tax documents |
| israeli-apartment-hunting | 40 | find and negotiate Israeli rental apartments via Yad2, Madlan, and agents |

The remaining 5 indexed listings range from 4 to 35 installs.

## Why This Matters for Hermes Agents

Hebrew and RTL are domains where generic skills consistently fail: bidi text, mirrored layout, and logical-property handling are easy to get wrong and costly to fix after the fact, and the hebrew-document-generator skill exists precisely because Hebrew Word files that look correct on screen come out scrambled. The suite encodes that hard-won knowledge into skills an agent can run instead of reasoning through from first principles. The accessibility skill targets IS 5568, the Israeli standard built on WCAG with national changes, so an agent can check a Hebrew site against the actual legal requirement rather than a generic WCAG rule. Each skill ships an English SKILL.md plus a SKILL_HE.md Hebrew-language variant, which is a rare bilingual authoring pattern useful for Hebrew-speaking end users. The family is deliberately single-market, which makes it narrow but deep: install counts concentrate at the top, and the engineering skills (RTL, i18n, Tailwind, document generation) all carry clean security verdicts.

## Usage

| You say | What happens |
|---|---|
| Make this site RTL for Hebrew | Uses hebrew-rtl-best-practices for logical properties and Tailwind RTL setup |
| Write Hebrew marketing copy | Uses hebrew-content-writer for grammar, register, and gendered language |
| My Hebrew Word doc comes out reversed | Uses hebrew-document-generator to regenerate it with paragraph-level RTL and bidi |
| Is this app IS 5568 compliant | Uses israeli-accessibility-compliance to audit against the Israeli standard |
| Extract data from this Tabu form | Uses hebrew-ocr-forms to OCR and parse the Israeli land-registry document |
| Schedule around Shabbat and chagim | Uses shabbat-aware-scheduler for halachic times and Israeli holidays |
| Set up Tailwind for Hebrew | Uses hebrew-tailwind-preset for dir variants and logical property utilities |

## Verification

Confirm the README and a representative skill body resolve on the master branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/skills-il/localization/master/README.md | head -60
curl -sL https://raw.githubusercontent.com/skills-il/localization/master/hebrew-rtl-best-practices/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skill's SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| hebrew-rtl-best-practices | Pass | Pass | Pass |
| hebrew-content-writer | Pass | Pass | Pass |
| israeli-accessibility-compliance | Pass | Pass | Warn |
| hebrew-document-generator | Pass | Pass | Pass |
| hebrew-tailwind-preset | Pass | Pass | Pass |
| shabbat-aware-scheduler | Pass | Pass | Pass |
| hebrew-i18n | Pass | Pass | Pass |
| israeli-ui-design-system | Pass | Pass | Pass |
| hebrew-nlp-toolkit | Pass | Pass | Pass |
| hebrew-ocr-forms | Pass | Pass | Pass |
| israeli-apartment-hunting | Pass | Pass | Pass |
| israeli-wedding-planner | Pass | Pass | Pass |
| israeli-flight-finder | Pass | Pass | Warn |
| israeli-travel-planner | Pass | Pass | Warn |
| hebrew-ai-text-humanizer | Pass | Pass | Pass |
| hebrew-book-typesetter | Pass | Pass | Pass |

Across all 16 sampled skills there are 45 Pass, 3 Warn, and 0 Fail cells. Thirteen skills pass all three checks; three carry a single Snyk Warn each (israeli-accessibility-compliance, israeli-flight-finder, israeli-travel-planner).

## Limitations

- Snapshot data, verified Nov 26, 2026: 2,631 combined installs across 16 indexed listings; 28 GitHub stars; MIT license; last pushed Nov 8, 2026. Counts drift over time.
- The install index outruns the tree: israeli-flight-finder and israeli-travel-planner carry install counts but have no matching directory in the current tree.
- The README skills table documents 11 of the 14 in-tree skills; hebrew-book-typesetter, israeli-apartment-hunting, and israeli-wedding-planner ship in the tree and carry skills.sh verdicts but are not listed in the README.
- Several skills embed Israeli legal or halachic guidance (accessibility law, rental and wedding rules, Rabbinate requirements) that is context-specific, and the skill descriptions themselves state they are not legal advice.
- The default branch is master; the raw URLs and install commands above assume it, so future editors should not normalize it to main.

## Related

[Matt Pocock Skills (简体中文) - Localized Engineering Suite Setup](/hermes/skills/catalog/mattpocock-skills-zh-cn-setup) | [Philtz JP Skills - Japanese Business Dev Suite](/hermes/skills/catalog/philtzjp-skills-setup) | [rnskill Content Suite - Chinese AI Skills Setup](/hermes/skills/catalog/rnskill-setup) | [Web AI Agent Skills - Browser AI APIs and WebMCP](/hermes/skills/catalog/web-ai-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with hebrew-rtl-best-practices for any RTL layout, and reach for hebrew-tailwind-preset only when you are already on Tailwind.
- For Hebrew text that renders reversed in Word, use hebrew-document-generator to regenerate the file rather than patching CSS.
- Install a single skill with claude install github:skills-il/localization/<skill> instead of cloning the whole repo when you need just one.
- Read the SKILL_HE.md alongside the English SKILL.md if you want the Hebrew-language prompts.
- Re-check the security pages on skills.sh for israeli-accessibility-compliance, israeli-flight-finder, and israeli-travel-planner, which carry the sample's three Warns.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
