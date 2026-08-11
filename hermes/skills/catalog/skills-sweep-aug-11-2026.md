---
title: Skills.sh Sweep — August 11, 2026
description: Automated marketplace sweep discovering 5 new/undocumented Hermes Agent skills. 5 setup guides drafted and pushed.
date: 2026-08-11
sweep_id: aug-11-2026-cron
total_discovered: 20
new_skills: 5
guides_drafted: 5
---

# Skills.sh Sweep — August 11, 2026 (Cron Update)

Automated discovery sweep across the [skills.sh](https://skills.sh) marketplace. Cross-referenced 20+ Hermes-related skills against the existing 366+ entry catalog at `corpusiq-docs/hermes/skills/catalog/`.

**Result:** 5 skills not yet cataloged or lacking setup guides. All 5 setup guides drafted.

---

## 🆕 Genuinely New Skills (3) — First Time Documented

| Skill | Installs | Source | Setup Guide |
|-------|----------|--------|-------------|
| `songwriting-and-ai-music` | 324 | nousresearch/hermes-agent | [songwriting-and-ai-music-setup.md](songwriting-and-ai-music-setup.md) ✍️ |
| `debugging-hermes-tui-commands` | 76 | nousresearch/hermes-agent | [debugging-hermes-tui-commands-setup.md](debugging-hermes-tui-commands-setup.md) ✍️ |
| `hermes-attestation-guardian` | 94 | prompt-security/clawsec | [hermes-attestation-guardian-setup.md](hermes-attestation-guardian-setup.md) ✍️ |

---

## 📝 Previously Identified — Setup Guides Now Complete (2)

| Skill | Installs | Source | Setup Guide |
|-------|----------|--------|-------------|
| `research-paper-writing` | 396 | nousresearch/hermes-agent | [research-paper-writing-setup.md](research-paper-writing-setup.md) ✍️ |
| `plan` | 309 | nousresearch/hermes-agent | [plan-mode-setup.md](plan-mode-setup.md) ✍️ |

---

## 📊 Existing Skills Verified (15+)

All top skills from `npx skills search hermes` and `npx skills search "hermes agent"` were verified as already cataloged: dogfood (5.4K), hermes-imports (4.5K), hermes-history-ingest (2.1K), hermes-tweet (682), hermes-agent (561), popular-web-designs (561), yuanbao (561), powerpoint (472), google-workspace (427), arxiv (422), claude-design (387), llm-wiki (370), jupyter-live-kernel (356), excalidraw (343), ascii-art (341), and more.

---

## 🔍 Methodology

- **4 search queries** across skills.sh CLI:
  - `hermes` (20 results)
  - `hermes agent` (20 results)
  - `hermes skill` (20 results)
  - `nousresearch/hermes-agent` (20 results)
- **Full skills.sh page scrape** of nousresearch/hermes-agent (213 skills) for cross-reference
- **Cross-referenced** against 366+ existing catalog entries
- **5 setup guides** drafted for all uncataloged/new skills
- **Sweep report** published to `marketplace/new-aug11-2026/`

---

## 📈 Ecosystem Growth

| Metric | Aug 10 | Aug 11 | Delta |
|--------|--------|--------|-------|
| Catalog entries | 358+ | 363+ | +5 |
| Official skills tracked | 34 | 36 | +2 |
| Guides drafted this sweep | — | 5 | +5 |
| Genuinely new discoveries | — | 3 | +3 |

---

**Next sweep:** Automated cron — next run.
