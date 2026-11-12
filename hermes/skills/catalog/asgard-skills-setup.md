---
title: "Asgard Skills - 301 Business Methodology Skills"
description: "asgard-ai-platform/skills: 5.0K combined installs across 96 listings, 301 Chinese-language methodology skills over 22 business domains"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/asgard-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "business", "methodology", "research"]
---

# Asgard Skills - Setup Guide

**Source:** [asgard-ai-platform/skills](https://www.skills.sh/asgard-ai-platform/skills) via skills.sh - 5.0K combined installs across 96 indexed listings; first seen Apr 10, 2026 (Nov 12, 2026 sweep)
**GitHub:** 245 stars, MIT license, `main` branch, last pushed 2026-06-06, 314 `SKILL.md` files with one `{category}-{skill-name}/` folder each
**Category:** Business method libraries: graduate-level theory models, algorithms, business frameworks, economics, operations, manufacturing, law fundamentals, Taiwan market practice
**Quality Tier:** 🟡 Established - a large, well-structured methodology library with a permissive license, held back by Chinese-first content, no documented installer and a repository that has not been pushed since June.

This is a teaching library rather than a tool library. Every folder packages a method the way a good analyst would explain it: what the model is, when it applies, how to compute or apply it, and where it goes wrong. The README groups the 301 skills into 22 prefixes, and the two largest are the ones that show the intent. `grad-` covers 87 graduate-level theory models such as the resource-based view, CAPM, structural equation modelling and difference-in-differences. `algo-` covers 62 algorithms including PageRank, BM25, ARIMA and EOQ.

The rest of the prefixes are practice-oriented: `biz-` carries 22 business-school frameworks from SWOT and Porter's five forces to DCF, `ops-` covers OKR, contract review and pitch decks, `mfg-` covers supplier scorecards and predictive maintenance, `ecom-` and `xborder-` cover cross-border and Southeast Asian commerce, and `tw-` carries 38 skills specific to the Taiwan market including stock analysis, e-commerce channels and tax.

Two properties make the pack unusual. The content is primarily Traditional Chinese, with an English README mirror that translates the catalog but not the skill bodies. And every skill folder follows the same shape: `SKILL.md`, plus `examples/`, `references/` and, where a calculation is deterministic, `scripts/` with plain Python.

The install band is narrow by comparison with tool packs. The top skill draws 153 installs and the current floor of the indexed set is 38, so this is a library people select from rather than install wholesale.

## Installation

The repository documents no installer. Both READMEs describe structure and content, not an install command, and there is no published plugin manifest to point a marketplace at. The working path is a clone and a copy:

```bash
git clone https://github.com/asgard-ai-platform/skills.git
cp -r skills/<category>-<skill-name> ~/.claude/skills/
```

For an agent that reads skills from a project directory, copy into `./.claude/skills/` instead. The repository is the raw material for the vendor's own packaged plugins, so a skill is self-contained by design and does not require its siblings. If your agent supports a skills CLI that accepts a repository path, point it at the clone; the layout is one folder per skill, which is the convention those tools expect.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| xborder-logistics | 153 | Cross-border logistics strategy: direct mail, overseas warehousing and bonded warehouse models. |
| tw-stock-analysis | 118 | Taiwan-listed stock analysis with EPS, P/E, dividend yield and financial statements. |
| ux-design-thinking | 112 | Design Thinking's five stages applied to a concrete user problem. |
| law-ip | 107 | Intellectual property fundamentals across patents, trademarks, copyrights and trade secrets. |
| econ-macro-indicators | 105 | Reading GDP, inflation, unemployment, rates and exchange rates as one picture. |
| law-labor | 98 | Taiwan Labor Standards Act: hours, overtime, leave and termination rules. |
| econ-game-theory | 87 | Nash equilibrium, dominant strategies and the Prisoner's Dilemma applied to strategy. |
| cs-sop | 85 | Customer service operations: L1 to L3 tiers, templates, SLAs and escalation. |
| data-dashboard-design | 82 | KPI hierarchy, chart type selection and interaction design for dashboards. |
| mfg-supplier-scorecard | 71 | Weighted supplier evaluation across quality, delivery, price and service. |
| biz-lean-six-sigma | 71 | Waste elimination and process variation reduction in operations. |
| pr-social-copywriting | 68 | Platform-optimised social copy for Instagram, Facebook, LinkedIn and X. |
| ecom-multilingual-listing | 68 | Multilingual product listing optimisation with localisation workflows. |
| ecom-sea-strategy | 66 | Southeast Asia e-commerce strategy: platform choice, payments and logistics. |
| mfg-predictive-maintenance | 61 | Predictive maintenance with remaining-useful-life models and the P-F curve. |

The remaining 81 indexed listings range from 38 to 59 installs.

The tree carries 314 `SKILL.md` files against a README claim of 301 skills and an index cap of 96 listings, so both the index and the count are partial views: the index samples the top of a long tail, and the tree is a few files ahead of the documentation.

## Why This Matters for Hermes Agents

Ask a model for a supplier evaluation and you get a list. Ask it for one with a weighted scorecard across quality, delivery, price and service, and you get a decision you can defend. The difference is not intelligence, it is method, and method is exactly what a general model will not volunteer because a method implies constraints.

That is the gap this library fills. Each skill encodes one method with its inputs, its computation and its known failures. When an agent is asked for a market entry analysis and the skill says to run a five-forces pass before a SWOT, the output arrives in a shape someone can review. Reviewed output gets reused. Unreviewed output gets rewritten, which is the same as not having been produced.

There is a second use that is less obvious. These are teaching documents, so an agent can explain the method it is applying. An operator who asks why a DCF came out a certain way gets an answer in the terms of the model rather than a restatement of the conclusion. That is the difference between a tool that produces numbers and one that helps someone check them.

The trade-off is language. If the task and the reviewer are English-only, the skill bodies need translation before the agent can use them, and the English README does not carry that translation. Treat the pack as bilingual-ready rather than bilingual.

## Usage

| You say | What happens |
|---|---|
| "Score these three suppliers" | Applies the weighted scorecard method and returns a comparison with explicit weights. |
| "Should we enter the Southeast Asian market?" | Runs the regional e-commerce strategy skill: platforms, payments, logistics and local constraints. |
| "Explain this DCF like an analyst" | Walks the model in its own terms, including the assumptions that drive the result. |
| "Design a support escalation process" | Produces tier definitions, SLAs and escalation paths from the customer service operations skill. |
| "What does this contract's IP clause actually cover?" | Uses the IP fundamentals skill to separate patents, trademarks, copyright and trade secrets. |
| "Build me a KPI dashboard layout" | Applies the KPI hierarchy and chart-selection rules before producing a layout. |
| "Plan a predictive maintenance program" | Applies the P-F curve and remaining-useful-life framing to the equipment list. |

## Verification

The skills sit at the repository root as `{category}-{skill-name}` folders. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/asgard-ai-platform/skills/main/xborder-logistics/SKILL.md | head -6
```

Confirm the language of the body before installing a set, since the catalog translation does not apply to the skill text:

```bash
curl -fsSL https://raw.githubusercontent.com/asgard-ai-platform/skills/main/biz-lean-six-sigma/SKILL.md | head -20
```

After copying, list the agent skills directory and confirm the folder names keep their prefix. The prefix is the only grouping signal in the flat layout, and renaming a folder loses the category.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| xborder-logistics | Pass | Pass | Pass |
| tw-stock-analysis | Pass | Pass | Warn |
| ux-design-thinking | Pass | Pass | Pass |
| law-ip | Pass | Pass | Pass |

The one Warn is on the Taiwan stock analysis skill, which asks for market data and produces recommendations. A scanner flags that pattern because a skill that reads prices and suggests positions can be mistaken for advice. The skill is a method, and the market data it uses comes from wherever the operator points it.

The rest of the pack is text and small deterministic scripts. The realistic risks are two: that an agent treats a framework's output as a conclusion rather than an input, and that a market-specific skill (tax, labor law, e-commerce channel rules) is applied in the wrong jurisdiction. Both are usage risks that a scanner cannot see.

## Limitations

- Snapshot data, verified 2026-11-12: 4,981 combined installs across 96 indexed listings; 245 GitHub stars; MIT license; last pushed 2026-06-06. Counts drift over time.
- 96 is the cap of the skills.sh search API and the tree carries 314 `SKILL.md` files, so the index reflects a sample of the library rather than its size.
- Skill bodies are written in Traditional Chinese. The English README translates the catalog and the category table, not the instructions inside each skill.
- No installer is documented in either README, and no published plugin manifest was found. Installation is a manual copy of folders.
- Several skills are jurisdiction-specific: Taiwan labor law, Taiwan e-commerce channels, EU and US-adjacent frameworks. Do not assume a skill applies in your country because its name is generic.
- Last push was June 2026. Policy and market concepts drift, and a five-month-old labor law or tax skill should be checked against the current rules before it is relied on.

## Related

- [Borghei Claude Skills - 385 Business Skill Library](/hermes/skills/catalog/borghei-claude-skills-setup)
- [ClawFu Skills - 175 Marketing Methodologies for AI Agents Setup](/hermes/skills/catalog/clawfu-skills-setup)
- [mbfinotti Business Skills - Sales, RevOps & Advertising](/hermes/skills/catalog/mbfinotti-skills-setup)
- [Dontbesilent dbskill - 35-Skill Business Toolkit Setup](/hermes/skills/catalog/dontbesilent-dbskill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by prefix, not by file. Copying `biz-*` or `ops-*` gives a coherent set, while picking individual skills scatters a method library across unrelated folders.
- Ask the agent to cite the model it applied. These skills name their frameworks, so the trace tells you whether the method was used or a generic answer was dressed up as one.
- Translate before you rely on a skill in an English-language workflow. Reading the body first also tells you whether the skill assumes Taiwan or EU context.
- Treat every market-specific skill as needing a current-source check. Labor law, tax and channel rules move, and the repository has not been pushed since June.
- Use the `grad-` and `algo-` skills as explanation tools, not as computation engines. The scripts that exist are small and deterministic; the value is the method, and the calculation usually belongs in your own code.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
