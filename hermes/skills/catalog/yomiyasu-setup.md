---
title: "Yomiyasu - Japanese AI Prose Refinement Setup"
description: "Setup guide for yomiyasu, the agent skill that refines AI-generated Japanese into natural prose - meaning-preserving edits for technical and business docs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/yomiyasu-setup/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skill setup", "yomiyasu", "japanese", "writing", "editing"]
---

# Yomiyasu - Setup Guide

**Source:** [nanaism/yomiyasu](https://www.skills.sh/nanaism/yomiyasu/yomiyasu) via skills.sh - 6,330 installs; first seen Oct 8, 2026 (evening sweep)
**GitHub:** [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu) (1,768 stars, MIT license; very active - pushed Oct 8, 2026; skill at `skills/yomiyasu/SKILL.md`, ~66 KB plus a slop-catalog reference)
**Category:** Writing / Content (Japanese)
**Quality Tier:** 🟡 Beta (strong community traction; MIT; very active; all sampled verdicts Pass; Japanese-language workflows only, verified Oct 8, 2026)

Yomiyasu (読みやすさ, "readability") is an agent skill for refining AI-generated Japanese into natural Japanese. It targets the specific tells of machine-written text: unnatural metaphors, ambiguous subject-predicate relationships, skewed syntax, needless decoration, and copy-style tone. It is built for technical articles, specifications, pull request descriptions, internal reports, and essays or note-style posts.

The skill's governing rule is strict: preserve the original meaning and add no information. Before rewriting a sentence it fixes four properties - the claim being made, the weighting and emphasis, the strength of assertion (definite versus tentative), and the sentence's function (evaluation, explanation, request, plan) - and every other rule applies only within those bounds.

---

## Installation

```bash
# Recommended
npx skills add nanaism/yomiyasu

# Update later
npx skills update yomiyasu
```

Claude Code users can install through the plugin marketplace path described in the repository README. The skill definition lives in a single file (`skills/yomiyasu/SKILL.md`), so manual installation is a one-file copy.

## What It Provides

| Capability | How |
|---|---|
| Meaning preservation | Four checks (claim, weighting, assertive strength, sentence function) run before and after every edit |
| Sentence-ending discipline | Chooses endings by document stance (advice / rules / explanation) so function and politeness level stay correct, without flattening every ending to one style |
| Paragraph and logic structure | Fixes ambiguous connectors, "preview-only" sentences, mixed topics within a paragraph, and broken subject-predicate agreement |
| Subject and object clarity | Restores who-does-what only from stated context; never invents actors or converts system behavior into human action |
| De-personification and metaphor fixes | Replaces AI-typical metaphorical verbs with everyday words while keeping the original metaphor's connotation |
| Self-labeling and negation | Handles "what matters is..." lead-ins and A-not-B contrasts without erasing emphasis or ranking |
| Terminology and punctuation | Keeps technical terms, identifiers, API names, and enum values intact; tunes sentence length (~30-45 characters) and comma placement |
| Structured output | Every pass reports what changed (変えたところ), what AI-ish phrasing remains (残したAIっぽいところ), and points to confirm with the writer (書き手に確かめたい点) |

## Why This Matters for Hermes Agents

Agents generate Japanese constantly - product docs, release notes, replies, marketing copy - and the gap between "grammatically correct" and "reads like a person wrote it" is exactly where output gets rejected. This skill packages a professional-grade refinement pass as a repeatable workflow with explicit guardrails: meaning is preserved, nothing is invented, and the agent flags rather than guesses when context is missing. It gives Japanese output the same anti-slop discipline that English-facing tooling gives English.

## Usage

| You say | What happens |
|---|---|
| 「この文章を読みやすくして」 (make this easier to read) | Full refinement pass under the meaning-preservation rules |
| 「AIっぽさをなくして」 (remove the AI feel) | Targets the slop catalog: metaphors, sameness, stiff compounds, copy-style tone |
| 「自然な日本語にして」 (make it natural Japanese) | Rewrites toward natural phrasing while keeping identifiers and terms |
| 「文章を脱臭して」 (de-odorize the text) | The full anti-AI-smell pass for article drafts |

Note: the skill warns it can conflict with other Japanese proofreading skills; if outputs degrade when several are active, disable the similar ones.

## Verification

```bash
# Confirm installation
npx skills list | grep yomiyasu

# Update to the latest rules
npx skills update yomiyasu
```

The repository publishes versioned releases (see its GitHub releases page) - the rule set is actively evolving.

## Security

skills.sh verdicts for yomiyasu (verified Oct 8, 2026):

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| yomiyasu | Pass | Pass | Pass |

The skill is instruction-only: it edits text and reads a bundled reference, with no network calls or command execution in its workflow.

## Related

- [01coder Agent Skills - Content, Publishing & Security Toolkit Setup](/hermes/skills/catalog/01coder-agent-skills-setup) - Chinese-language content toolkit with a similar language-specific scope
- [Callicrate Skills - AGENTS.md & Documentation Authoring Setup](/hermes/skills/catalog/callicrate-skills-setup) - documentation authoring discipline for agents
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

1. **Give it the destination.** Whether the text is for a blog, a spec, or a report changes the ending style it chooses; state the purpose and reader when you can.
2. **Expect flagged uncertainty, not silent guesses.** Unknown actor or unclear relationship? It asks (maximum two questions) instead of inventing.
3. **Do not mix with similar proofreading skills.** The README explicitly warns of conflicting instructions between competing Japanese refinement skills.
4. **Technical identifiers survive.** API names, keys, types, enum values, and numbers are preserved; the pass will not mangle code-adjacent text.
5. **Use the three-part output.** The changes list, the remaining-slop list, and the confirmation list are designed to be reviewed quickly by a human editor.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
