---
title: "June 29, 2026 — Coding Posture"
description: "New Hermes skills discovered June 29, 2026: task-aware coding modes, anti-AI-slop humanizer, session verification, background delegation, self-fine-tuning, WhatsApp integration, and native Safari automation."
---

# 🆕 June 29, 2026 — 7 New Skills Discovered

**Date:** June 29, 2026
**New Repos:** 7 | **New Skills:** 7+ | **Setup Guides:** 7

Seven new community-contributed skills for Hermes Agent, discovered through GitHub search and skills.sh marketplace scanning. All include full setup guides in the catalog.

---

## New Skills at a Glance

| # | Skill | Stars | Category | Setup Guide |
|---|-------|:-----:|----------|-------------|
| 1 | **coding-posture** | 9★ | Agent Infrastructure | [Setup →](/hermes/skills/catalog/coding-posture-setup/) |
| 2 | **ultimate-humanizer** | 1★ | Content & Social | [Setup →](/hermes/skills/catalog/ultimate-humanizer-setup/) |
| 3 | **clean-slate** | — | Quality Assurance | [Setup →](/hermes/skills/catalog/clean-slate-setup/) |
| 4 | **delegate-skills** | — | Multi-Agent | [Setup →](/hermes/skills/catalog/delegate-skills-setup/) |
| 5 | **autolora** | 1★ | Model Optimization | [Setup →](/hermes/skills/catalog/autolora-setup/) |
| 6 | **hermes-whatsapp-secretary** | — | Communication | [Setup →](/hermes/skills/catalog/hermes-whatsapp-secretary-setup/) |
| 7 | **safari-web-agent** | 1★ | Browser Automation | [Setup →](/hermes/skills/catalog/safari-web-agent-setup/) |

---

## Skill Details

### 1. Coding Posture (9★)
**Repo:** [alexei-led/coding-posture](https://github.com/alexei-led/coding-posture)

A single `SKILL.md` that gives coding agents task-aware working modes — debug, fix, review, migrate, explain, and test. The agent adjusts its reasoning depth, tool selection, and output format based on the active posture. Works across Hermes, Claude Code, Codex, Cursor, and Pi.

**Why it matters:** Eliminates the need to write "be thorough" or "just give me a quick fix" in every prompt. The agent knows what mode it's in.

```bash
npx skills add alexei-led/coding-posture
```

---

### 2. Ultimate Humanizer (1★)
**Repo:** [surdijon/ultimate-humanizer](https://github.com/surdijon/ultimate-humanizer)

Anti-AI-slop detection: 50 patterns, 2-pass self-audit, and 5-dimensional scoring (naturalness, variety, agency, specificity, rhythm). Optimized for French but works across languages. Includes Google spam-protection mode for SEO content.

**Why it matters:** Every AI-generated text carries patterns that readers — and search engines — increasingly detect. Ultimate Humanizer strips them systematically.

```bash
npx skills add surdijon/ultimate-humanizer
```

---

### 3. Clean Slate
**Repo:** [sidhartha1s/clean-slate](https://github.com/sidhartha1s/clean-slate)

Session-end verification that turns "looks done" into proven done. Audits every agent claim — merged PRs, passing tests, fixed bugs — against the real artifact. Produces a structured status report with ✅, ⚠️, and ❌ verdicts.

**Why it matters:** The #1 failure mode of coding agents is claiming completion without verification. Clean Slate makes verification automatic.

```bash
npx skills add sidhartha1s/clean-slate
```

---

### 4. Delegate Skills
**Repo:** [bassemZohdy/delegate-skills](https://github.com/bassemZohdy/delegate-skills)

Spawn background agent workers in isolated git worktrees. The parent agent continues working while background workers handle long-running tasks — with self-healing monitoring that restarts failed workers.

**Why it matters:** True parallel agent work without context pollution. One agent handles the conversation while workers handle the heavy lifting.

```bash
npx skills add bassemZohdy/delegate-skills
```

---

### 5. AutoLoRA (1★)
**Repo:** [DJLougen/autolora](https://github.com/DJLougen/autolora)

Hermes fine-tunes itself. Curates successful agent traces, trains a LoRA adapter on RunPod via Unsloth, and hot-swaps the improved model — all while keeping costs capped via Stripe payment thresholds.

**Why it matters:** This is the self-improving agent loop made real. The agent gets better at your specific workflows over time.

```bash
npx skills add DJLougen/autolora
```

---

### 6. Hermes WhatsApp Secretary
**Repo:** [ricktechmecha/hermes-whatsapp-secretary](https://github.com/ricktechmecha/hermes-whatsapp-secretary)

Read, summarize, draft replies, and schedule WhatsApp messages — all through Hermes. Every reply requires your confirmation before sending. Priority filtering for important contacts.

**Why it matters:** WhatsApp is where business happens for many operators. This brings it into the agent workflow with appropriate safety gates.

```bash
npx skills add ricktechmecha/hermes-whatsapp-secretary
```

---

### 7. Safari Web Agent (1★)
**Repo:** [treyxu23/safari-web-agent](https://github.com/treyxu23/safari-web-agent)

Browser automation using your real Safari browser via native macOS CGEvent. Anti-bot bypass, login session persistence, and real browser fingerprint. Works on sites where Playwright gets detected.

**Why it matters:** Many business tools and dashboards block headless browsers. Safari Web Agent navigates them as a real user.

```bash
npx skills add treyxu23/safari-web-agent
```

---

## Additional Repos Discovered (Curated for Future Review)

These repos were also found in the June 29 sweep. They're tracked for potential future setup guides:

| Repo | Description | Stars |
|------|-------------|:-----:|
| [Carojing/X-KOL-impressions](https://github.com/Carojing/X-KOL-impressions) | X/Twitter KOL outreach data extraction | 1★ |
| [hanxing-AI/feynman-method-skill](https://github.com/hanxing-AI/feynman-method-skill) | Feynman Method interactive learning with hallucination defense | — |
| [shagghiesuperstar/HERMES-Free-SOTA](https://github.com/shagghiesuperstar/HERMES-Free-SOTA) | FreeLLMAPI + Hermes MOA for SOTA at zero cost | — |
| [julianargus01/agent-minds](https://github.com/julianargus01/agent-minds) | Cognitive-function skills for agent thinking styles | 3★ |
| [Jachinx-ai/deep-article-writing-skill](https://github.com/Jachinx-ai/deep-article-writing-skill) | Chinese article writing: raw material to structured Markdown | 6★ |
| [lunkerchen/skill-description-audit-skill](https://github.com/lunkerchen/skill-description-audit-skill) | Audit and improve skill descriptions for trigger accuracy | — |
| [jry21223/final-review-template-kit](https://github.com/jry21223/final-review-template-kit) | LaTeX template + Hermes skill for exam review generation | 2★ |
| [prasadmogulothu/agent-skills](https://github.com/prasadmogulothu/agent-skills) | Reusable agent skills with multi-model orchestration | — |
| [hansai-art/hermes-agent-school](https://github.com/hansai-art/hermes-agent-school) | Failure patterns and diagnostic pack blueprint | — |

---

## Stats

- **Total marketplace skills:** 464+ → **471+**
- **Categories covered this sweep:** Agent Infrastructure, Content & Social, Quality Assurance, Multi-Agent, Model Optimization, Communication, Browser Automation
- **Average stars:** 1.7★ (early-stage community skills — high potential)
- **Setup guides published:** 7

---

*← [Skills Marketplace](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) | [Previous Update →](/hermes/skills/marketplace/new-june28-2026-update3/)*

*Powered by CorpusIQ*
