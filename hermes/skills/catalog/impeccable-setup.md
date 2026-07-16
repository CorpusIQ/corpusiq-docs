---
title: "Impeccable Writing Framework — Setup Guide"
description: Install, configure, and use pbakaus/impeccable — an AI writing quality framework that teaches Hermes style rules, structure templates, and content arrangement. 90K combined installs.
---

# Impeccable Writing Framework — Setup Guide

**Source:** [pbakaus/impeccable](https://skills.sh/pbakaus/impeccable) (90K combined installs)
**Category:** Content / Writing Quality
**Skills:** 2 (teach-impeccable, arrange)

Impeccable is a writing quality framework that loads directly into Hermes — it teaches the agent style rules, structure templates, and content arrangement patterns. The result: every email, social post, docs page, and UGC script follows consistent, high-quality writing standards.

---

## Installation

```bash
# Full framework
npx skills add pbakaus/impeccable

# Or individually
npx skills add pbakaus/impeccable --skill teach-impeccable
npx skills add pbakaus/impeccable --skill arrange
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version with skills.sh support |
| **Content to improve** | Existing text, draft, or writing prompt |

No API keys or external accounts needed. Impeccable is a pure methodology skill — it loads writing rules into the agent's instruction context.

---

## Key Capabilities

### Writing Quality

| Capability | How to Trigger | Notes |
|---|---|---|
| Load writing methodology | "Teach me Impeccable" or "Load impeccable writing rules" | Installs style rules — tone, structure, clarity, anti-buzzword filters |
| Apply style to content | "Apply Impeccable style to this [email/post/article]" | Rewrites content following loaded rules |
| Structure optimization | "Arrange this content" or "Fix the flow" | Logical flow optimization — paragraph ordering, transition quality |

### Content Arrangement

| Capability | How to Trigger | Notes |
|---|---|---|
| Logical flow analysis | "Check the arrangement of [content]" | Identifies flow breaks, missing transitions, structural issues |
| Section reordering | "Rearrange [content] for better flow" | Proposes and applies optimal section ordering |
| Transition generation | "Add transitions between [section A] and [section B]" | Generates smooth bridging content |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Outbound email quality** | Load Impeccable before drafting lead responses — every email follows consistent quality standards |
| **Social media posts** | Apply `arrange` to ensure X threads, LinkedIn posts, and Reddit comments flow logically |
| **Docs quality assurance** | Run every new docs page through `teach-impeccable` before publishing — catches buzzwords, improves clarity |
| **UGC video scripts** | Apply Impeccable style rules to HeyGen video scripts — consistent voice across all content |
| **Community responses** | Load before engaging on Discord, HN, and Reddit — helpful-first tone with professional quality |
| **Internal communications** | Standardize all agent-written internal reports, Telegram messages, and status updates |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| Impeccable rules conflict with CorpusIQ voice rules | The CorpusIQ content voice rules (no emdashes, no buzzwords, pain-point-first) take precedence. Impeccable's structural rules still apply |
| `arrange` over-aggressively reorders | Specify "keep [section] at the beginning/end" in your request — the skill respects explicit placement instructions |
| Rules feel too rigid for creative content | Use `teach-impeccable` for formal content (docs, emails, reports). Skip it for casual community engagement |

---

## Verification

```bash
# Verify skills installed
hermes skills list | grep impeccable

# Quick functional test — have Hermes apply Impeccable to a test sentence
echo 'Test: Apply Impeccable style to this sentence and show the result.' > /tmp/test-impeccable.txt
cat /tmp/test-impeccable.txt
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 27 Discovery](/hermes/skills/marketplace/new-june27-2026/) →*
*Powered by CorpusIQ*
