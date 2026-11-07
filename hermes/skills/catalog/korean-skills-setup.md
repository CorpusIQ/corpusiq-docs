---
title: "Korean Skills - Hangul Writing and Style Checks"
description: "daleseo/korean-skills on skills.sh: 8.5K combined installs across 3 listings; Korean grammar, style-guide and AI-tell humanizer skills for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/korean-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "korean", "writing", "editing"]
---

# Korean Skills - Setup Guide

**Source:** [daleseo/korean-skills](https://www.skills.sh/daleseo/korean-skills) via skills.sh - 8.5K combined installs across 3 indexed listings; first seen 2026-11-07 (Nov 7 2026 morning sweep)
**GitHub:** 250 stars, MIT, branch `main`, last pushed 2026-05-04, three skill directories under `skills/`, plus `.claude-plugin`, `AGENTS.md` and `CLAUDE.md` at the repository root
**Category:** Korean writing for agents: grammar correction, style-guide enforcement and human-sounding Korean prose
**Quality Tier:** 🟡 Yellow - MIT licensed, 250 stars and three consistent skills, but one sampled skill carries a Snyk Warn and every instruction file is written in Korean.

This is a Korean-language writing suite for agents, and it is the most complete of the three-skill packages in this batch. Each skill is a directory with its own `SKILL.md`, reference material and examples, and the repository also ships a Claude Code plugin manifest under `.claude-plugin`, a CI workflow and release workflow, and both `AGENTS.md` and `CLAUDE.md` at the root for agent and contributor guidance.

The three skills split the work the way a human editing pass does. `humanizer` handles the largest structural change, `grammar-checker` fixes orthography and spacing against the standard rules, and `style-guide` enforces consistency across a document or a whole project. The README documents a recommended order for running them, and it explains why the order matters rather than just listing it.

## Installation

The README's quick start installs everything:

```bash
npx skills add daleseo/korean-skills
```

Single skills can be installed on their own, which is useful when a project only needs one pass:

```bash
npx skills add daleseo/korean-skills@humanizer
npx skills add daleseo/korean-skills@grammar-checker
npx skills add daleseo/korean-skills@style-guide
```

The repository is also a Claude Code plugin marketplace. The README adds the marketplace and then installs the plugin:

```bash
claude /plugin marketplace add daleseo/korean-skills
claude /plugin install korean-skills@korean-skills
```

That route exposes three slash commands: `/korean-skills:humanizer`, `/korean-skills:grammar-checker` and `/korean-skills:style-guide`.

There is a fourth route through the GitHub CLI's `gh skill` preview command, which the README documents with a project-scope install, a user-scope install, a single-skill install and a release pin:

```bash
gh skill install daleseo/korean-skills --agent claude-code
gh skill install daleseo/korean-skills --agent claude-code --scope user
gh skill install daleseo/korean-skills humanizer --agent claude-code
gh skill install daleseo/korean-skills --pin v1.0.0 --agent claude-code
gh skill preview daleseo/korean-skills
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| humanizer | 3,678 | Detect AI-generated Korean patterns and rewrite them into natural prose; 40 patterns scored at three severity levels |
| grammar-checker | 2,420 | Spelling, spacing, grammar and punctuation checks against standard Korean rules, with explanations |
| style-guide | 2,359 | Tone, terminology, number, list, quote and date consistency across a document or a project |

No indexed listings fall below the threshold.

`humanizer` is the heaviest skill in the set. Its description cites the KatFishNet paper (94.88% AUC) as the basis for its pattern set, then lists what it inspects: comma overuse, rigid spacing, part-of-speech diversity, overused AI vocabulary, translationese constructions, pronoun density, plural overuse and structural monotony, across 40 patterns graded S1 to S3 by severity. It carries a `references/` directory of pattern documentation and is an adaptation of an English-language humanizer project, which the README credits.

`grammar-checker` works in four prioritized categories: spelling first, then spacing (dependent nouns, auxiliary verbs, unit nouns), then grammatical structure (particles, endings), then punctuation. The interesting design choice is that it explains each correction and marks confidence, so a firm error reads differently from a suggestion. It ships `references/rules.md`, `references/common-errors.md` and an `examples/` directory.

`style-guide` runs seven consistency categories - tone and formality, terminology, numbers and units, list structure, quotes and emphasis, dates and times, links and references - and resolves conflicts by majority rule across a layered set of authorities: the national language institute's official document guidance, academic thesis guidance, and an industry technical-writing guide.

## Why This Matters for Hermes Agents

Korean is where generic writing skills fail quietly. An English-trained editor skill will pass Korean text that has the wrong particle, the wrong spacing around a dependent noun, or a formal and informal register mixed inside one paragraph, because none of those errors are visible to a token-level model that does not know the rules.

The grammar skill is rule-based rather than stylistic, which is what makes it usable: spelling pairs, spacing rules and particle selection are correctness questions with right answers, and the skill supplies the rule alongside the fix. That matters for any agent producing Korean documentation, product copy or code comments.

The humanizer addresses the second-order problem. Korean has its own AI tells, and they are not translations of the English ones. Overused commas, uniform sentence endings and translationese constructions built from passive auxiliaries are the Korean equivalents of the English tells, and the file enumerates 40 of them rather than telling the agent to "sound natural".

The style guide solves the multi-author problem that shows up in real repositories: one document using formal register in one section and informal in another, or the same concept named two ways across a docs tree. The seven categories are the ones that actually drift.

The README's pipeline order is the useful part operationally. The humanizer changes sentences structurally, so the grammar check belongs after it, and the consistency check belongs last, once the text has stopped moving.

## Usage

| You say | What happens |
|---|---|
| "Clean up this Korean draft without changing the meaning" | The humanizer scans for the 40 patterns, reports them by severity, and rewrites the prose |
| "Check the spelling and spacing in this Korean doc" | The grammar checker reports errors in four prioritized categories, with the rule and a confidence marker per item |
| "Make the terminology consistent across these chapters" | The style guide finds mixed terminology, register and number formats and proposes one form per category |
| "Review the Korean comments in this code file" | The grammar checker runs over comments and docstrings, which the skill description names as a supported use |
| "Is this text AI-generated?" | The humanizer's pattern report gives a per-pattern breakdown by severity rather than a single verdict |
| "Prepare this Korean document for publication" | The three skills run in the documented order: humanizer, then grammar, then style consistency |

## Verification

Read a skill before installing. This path returned HTTP 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/daleseo/korean-skills/main/skills/humanizer/SKILL.md | head -30
```

The same shape applies to the other two, both of which also returned HTTP 200: `skills/grammar-checker/SKILL.md` and `skills/style-guide/SKILL.md`. Expect Korean-language frontmatter and bodies; that is the intended form, not a broken download.

After install, confirm all three directories landed, adjusting the path to the directory your agent scans:

```bash
ls .agents/skills | grep -E 'humanizer|grammar-checker|style-guide'
```

If you installed a single skill, only that name should appear. If you used the plugin route, check the plugin list in Claude Code instead, since the plugin bundle places the skills under its own namespace.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| humanizer | Pass | Pass | Warn |
| grammar-checker | Pass | Pass | Pass |
| style-guide | Pass | Pass | Pass |

The skill surface is markdown and reference files. None of the three skills ships an executable script, and the workflow they describe is "read text, return a report", so there is no install-time or run-time code path to audit.

The Snyk Warn sits on the humanizer. It is a detection-quality or content flag rather than an execution risk, but it is the skill that rewrites text, so it is the one worth reading in full before you let it run over anything you care about. All three skills edit prose, and replacements are suggestions the caller has to apply unless the host agent writes them back.

The repository is MIT licensed with a LICENSE file at the root, so reuse and redistribution are clear.

## Limitations

- Snapshot data, verified 2026-11-07: 8,457 combined installs across 3 indexed listings; 250 GitHub stars; MIT; last pushed 2026-05-04. Counts drift over time.
- The humanizer carries a Snyk Warn while the other two skills pass all three scanners. Do not treat the suite as uniformly cleared.
- Both the README and all three `SKILL.md` files are written in Korean. An English `README_EN.md` exists, but the skill instructions themselves are not translated, so an agent that only loads English context gets less from them.
- The style guide's authority sources are Korean institutions and one company's technical-writing guide. They are appropriate for Korean business and technical documents, and not neutral on house style.
- The humanizer's pattern set is an adaptation of an English-language project with Korean patterns layered on. Pattern coverage will lag whatever produced the text.
- Rule-based grammar checking is strong on orthography and spacing and weaker on semantics. It flags forms, not meaning, so a fluent but wrong sentence can pass.

## Related

- [Humanizer Setup](/hermes/skills/catalog/humanizer-setup)
- [Avoid AI Writing - AI-Pattern Audit & Rewrite Setup](/hermes/skills/catalog/avoid-ai-writing-setup)
- [K-Skill - Korean Agent Skills Setup](/hermes/skills/catalog/k-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the pipeline in the documented order. Humanizer first, grammar second, style guide last, because each pass stabilizes the input for the next.
- Ask for the severity breakdown, not just the corrected text. S1 items are worth acting on; S3 items are often taste.
- Point the style guide at a glossary before a long document. Supplying the preferred term once beats accepting a majority-rule guess across twenty chapters.
- Use the single-skill installs for cost control. A grammar pass on a code comment does not need the humanizer's 40 patterns loaded.
- Keep a copy of the original. These skills rewrite prose, and the grammar checker's explanations are more useful when you can diff against the source.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
