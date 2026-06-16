---
title: June 15, 2026 — Nous Research Hermes Agent Expansion (23 skills)
description: Daily sweep found 23 unlisted nousresearch/hermes-agent skills with 131-158 installs each. Creative tools, macOS automation, dev workflows — all from the official repo.
---

# June 15, 2026 — Nous Research Hermes Agent Expansion

Daily sweep surfaced **23 unlisted skills** from the official `nousresearch/hermes-agent` repository — all with **131-158 installs** each. These skills were present in the June 13 massive expansion (72 skills catalogued) but were missed during that sweep. This fills the gap.

The skills span 7 categories: Creative & Media (11), Development & Testing (4), macOS Automation (3), Data & ML (2), Productivity (2), and Smart Home (1).

*Previously catalogued: 350 total (89 native + 261 marketplace). This update adds 23 → 373 total.*

---

## Creative & Media — 11 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `design-md` | 158 | Author/validate/export Google DESIGN.md token spec files |
| `ascii-art` | 157 | ASCII art: pyfiglet, cowsay, boxes, image-to-ascii |
| `sketch` | 157 | Throwaway HTML mockups: 2-3 design variants to compare |
| `ocr-and-documents` | 155 | Extract text from PDFs/scans (pymupdf, marker-pdf) |
| `manim-video` | 151 | Manim CE animations: 3Blue1Brown math/algo videos |
| `ascii-video` | 149 | ASCII video: convert video/audio to colored ASCII MP4/GIF |
| `songwriting-and-ai-music` | 148 | Songwriting craft and Suno AI music prompts |
| `p5js` | 146 | p5.js sketches: gen art, shaders, interactive, 3D |
| `touchdesigner-mcp` | 140 | Control TouchDesigner via twozero MCP — operators, real-time visuals |
| `comfyui` | 137 | Generate images/video/audio with ComfyUI — install, launch, workflows |
| `pretext` | 136 | Creative browser demos with @chenglou/pretext — DOM-free text layout |

**Install all creative skills:**
```bash
npx skills add nousresearch/hermes-agent@design-md -y
npx skills add nousresearch/hermes-agent@ascii-art -y
npx skills add nousresearch/hermes-agent@sketch -y
npx skills add nousresearch/hermes-agent@ocr-and-documents -y
npx skills add nousresearch/hermes-agent@manim-video -y
npx skills add nousresearch/hermes-agent@ascii-video -y
npx skills add nousresearch/hermes-agent@songwriting-and-ai-music -y
npx skills add nousresearch/hermes-agent@p5js -y
npx skills add nousresearch/hermes-agent@touchdesigner-mcp -y
npx skills add nousresearch/hermes-agent@comfyui -y
npx skills add nousresearch/hermes-agent@pretext -y
```

---

## Development & Testing — 4 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `opencode` | 142 | Delegate coding to OpenCode CLI (features, PR review) |
| `spike` | 135 | Throwaway experiments to validate an idea before build |
| `test-driven-development` | 134 | TDD: enforce RED-GREEN-REFACTOR, tests before code |
| `nano-pdf` | 136 | Edit PDF text/typos/titles via nano-pdf CLI (NL prompts) |

**Install all dev skills:**
```bash
npx skills add nousresearch/hermes-agent@opencode -y
npx skills add nousresearch/hermes-agent@spike -y
npx skills add nousresearch/hermes-agent@test-driven-development -y
npx skills add nousresearch/hermes-agent@nano-pdf -y
```

---

## Data & ML — 2 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `polymarket` | 139 | Query Polymarket: markets, prices, orderbooks, history |
| `huggingface-hub` | 136 | HuggingFace hf CLI: search/download/upload models, datasets |

**Install:**
```bash
npx skills add nousresearch/hermes-agent@polymarket -y
npx skills add nousresearch/hermes-agent@huggingface-hub -y
```

---

## macOS Automation — 3 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `apple-notes` | 133 | Manage Apple Notes via memo CLI: create, search, edit |
| `imessage` | 133 | Send and receive iMessages/SMS via the imsg CLI on macOS |
| `findmy` | 131 | Track Apple devices/AirTags via FindMy.app on macOS |

**Install:**
```bash
npx skills add nousresearch/hermes-agent@apple-notes -y
npx skills add nousresearch/hermes-agent@imessage -y
npx skills add nousresearch/hermes-agent@findmy -y
```

---

## Productivity — 2 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `kanban-orchestrator` | 133 | Decomposition playbook + anti-temptation rules for orchestrator profile |
| `gif-search` | 132 | Search/download GIFs from Tenor via curl + jq |

**Install:**
```bash
npx skills add nousresearch/hermes-agent@kanban-orchestrator -y
npx skills add nousresearch/hermes-agent@gif-search -y
```

---

## Smart Home — 1 skill

| Skill | Installs | Description |
|-------|----------|-------------|
| `maps` | 131 | Geocode, POIs, routes, timezones via OpenStreetMap/OSRM |

**Install:**
```bash
npx skills add nousresearch/hermes-agent@maps -y
```

---

## CorpusIQ Use Cases

| Skill | CorpusIQ Agent Use |
|-------|-------------------|
| `spike` | Validate growth hypotheses in throwaway experiments before building |
| `test-driven-development` | Enforce TDD on CorpusIQ product features and MCP connectors |
| `kanban-orchestrator` | Decompose growth ops into parallel workstreams without agent overload |
| `polymarket` | Monitor prediction market sentiment for product positioning |
| `huggingface-hub` | Deploy and manage local AI models for CorpusIQ agent infrastructure |
| `ocr-and-documents` | Extract text from lead research PDFs and competitor reports |
| `maps` | Geocode customer locations for territory analysis |

---

## How These Were Missed

The June 13, 2026 PM sweep documented 72 skills from `nousresearch/hermes-agent` via browser-based repo page sweep. However, the snapshot truncation bug (295-element limit) caused 23 skills below the fold to be missed. This daily sweep used the REST API (`q=nousresearch/hermes-agent&limit=50`) which returned all 50 skills, catching the ones the browser missed.

---

*← [June 12 Update (OpenClaw Security Suite)](/hermes/skills/marketplace/new-june12-2026-update/) | [Skills Marketplace](/hermes/skills/marketplace/) →*

*↑ [Skills Home](/hermes/skills/)*

*Powered by CorpusIQ*
