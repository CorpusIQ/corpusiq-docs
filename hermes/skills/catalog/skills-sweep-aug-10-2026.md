---
title: Skills.sh Sweep — August 10, 2026
description: Automated marketplace sweep discovering 29 new Hermes Agent skills not yet in the corpusiq-docs catalog. 7 setup guides drafted and pushed.
date: 2026-08-10
sweep_id: aug-10-2026
total_discovered: 50
new_skills: 29
guides_drafted: 7
---

# Skills.sh Sweep — August 10, 2026

Automated discovery sweep across the [skills.sh](https://skills.sh) marketplace. Cross-referenced 50 unique Hermes-related skills against the existing 351-entry catalog at `corpusiq-docs/hermes/skills/catalog/`.

**Result:** 29 skills not yet cataloged. 7 setup guides drafted.

---

## 🆕 New Skills Discovered (29)

### 📦 High-Value Official Skills (nousresearch/hermes-agent)

| Skill | Installs | Setup Guide |
|-------|----------|-------------|
| `claude-design` | 383 | [claude-design-setup.md](claude-design-setup.md) ✍️ |
| `llm-wiki` | 369 | [llm-wiki-setup.md](llm-wiki-setup.md) ✍️ |
| `excalidraw` | 342 | [excalidraw-setup.md](excalidraw-setup.md) ✍️ |
| `ascii-art` | 338 | [ascii-art-setup.md](ascii-art-setup.md) ✍️ |
| `imessage` | 331 | [imessage-setup.md](imessage-setup.md) ✍️ |
| `design-md` | 329 | — |
| `songwriting-and-ai-music` | 324 | — |
| `architecture-diagram` | 320 | — |
| `p5js` | 319 | — |
| `ocr-and-documents` | 316 | — |
| `sketch` | 312 | — |
| `comfyui` | 308 | — |
| `opencode` | 301 | — |
| `ascii-video` | 291 | — |
| `manim-video` | 291 | — |
| `github-code-review` | 281 | [github-code-review-setup.md](github-code-review-setup.md) ✍️ |

### 📦 Third-Party Skills

| Skill | Installs | Source | Setup Guide |
|-------|----------|--------|-------------|
| `printing-press-library` | 679 | mvanhorn/printing-press-library | [printing-press-library-setup.md](printing-press-library-setup.md) ✍️ |
| `p5js-hermes` | 36 | podo/design-agent-skills | — |
| `agentiko-hermes` | 16 | uphiago/recon-skills | (already cataloged) |
| `hermes-learning-loop` | 7 | skills.volces.com | — |
| `hermes-worker-qxun` | 5 | andy304yang/codex | — |
| `hermes-code-bridge` | 3 | xuyang-liu16/hermes-code-bridge | — |
| `hermes-remote-deploy` | 2 | aaaaqwq/agi-super-team | — |
| `hermes-insights` | 2 | alexai-mcp/hermes-ccc | — |
| `hermes-compress` | 1 | theo-one-ai/hermes-ccc | — |
| `hermes-dreaming` | 1 | asimons81/hermes-dreaming | — |
| `hermes-promotion` | 1 | buzzxu/bbg | — |
| `hermes-network` | 1 | schin-300/hermes-skills | — |
| `hermes-delegated-coding` | 1 | denglong450921-oss/hermes-custom-skills | — |

---

## 📊 Existing Skills Verified (21)

The following 21 skills were confirmed as already existing in the catalog (no duplicate guides):

`dogfood` (5,368), `hermes-tweet` (667), `hermes-agent` (561), `yuanbao` (560), `popular-web-designs` (558), `hermes-agent` (525), `powerpoint` (469), `google-workspace` (427), `arxiv` (420), `jupyter-live-kernel` (355), `youtube-content` (336), `hermes-agent-skill-authoring` (276), `claude-code` (287), `codex` (283), `vps-server-management` (61), `hermes` (68), `hermes-agent` (27), `hermes-deploy` (12), plus 4 more. Full details in catalog.

---

## 🔍 Methodology

- **7 search queries** across skills.sh API:
  - `nousresearch/hermes-agent`
  - `hermes+skill+agent`
  - `hermes+automation+OR+hermes+deploy+OR+hermes+tool`
  - `hermes+code+OR+hermes+dev+OR+hermes+workflow`
  - `hermes+deploy+OR+hermes+tool+OR+hermes+plugin`
  - `aradotso/hermes-skills`
- **Cross-referenced** against 351 existing catalog entries
- **7 setup guides** drafted for highest-signal skills (>200 installs or unique capability)
- **22 remaining** new skills documented for future guide drafting

---

## 📈 Ecosystem Growth

| Metric | Jul 30 | Aug 10 | Delta |
|--------|--------|--------|-------|
| Catalog entries | 341 | 351+ | +10+ |
| Official skills tracked | ~15 | 31 | +16 |
| Total discovered unique | ~47 | 50 | +3 |
| Guides drafted this sweep | 5 | 7 | +2 |

The NousResearch Hermes Agent ecosystem continues to ship new skills rapidly. 16 additional official skills were cataloged this sweep that were previously missed — notably the creative suite (ascii-art, excalidraw, sketch), content generation tools (songwriting, manim-video, ascii-video), and developer workflow skills (github-code-review, opencode, architecture-diagram).

---

**Next sweep:** Automated cron — next run. Focus queries on recently added skills and trending.
