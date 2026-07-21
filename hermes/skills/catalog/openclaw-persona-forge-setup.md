---
title: OpenClaw Persona Forge — Lobster Soul Character Designer for OpenClaw Agents
description: Forge complete lobster soul personas for OpenClaw AI agents. Identity, soul description, boundary rules, names, and avatar prompts. 800万+ combinations via gacha engine. 3.8K+ installs.
---

# OpenClaw Persona Forge — Setup Guide

**Source:** [affaan-m/everything-claude-code](https://skills.sh/affaan-m/everything-claude-code/openclaw-persona-forge) (3,800+ installs)
**Category:** Agent Infrastructure / Character Design
**Quality Tier:** 🟡 Beta

Forge complete "lobster soul" personas for OpenClaw AI agents. Outputs identity positioning, soul description (SOUL.md), character boundary rules, names, and avatar generation prompts. Includes an 8-million-combination gacha engine for random character generation.

中文名称：龙虾灵魂锻造炉 — 为 OpenClaw AI Agent 创建完整角色灵魂

---

## Installation

```bash
npx skills add affaan-m/everything-claude-code --skill openclaw-persona-forge
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python 3** | For gacha engine (`gacha.py`) |
| **OpenClaw** | Target platform for the persona |
| **Image generation skill** (optional) | For auto-generating avatar images |

---

## Core Philosophy

A good lobster soul = **Identity Tension** + **Boundary Rules** + **Character Flaws** + **Name** + **Visual Anchor**

All five must reinforce each other.

---

## Modes of Operation

### 1. Guided Mode

User describes what they want → Agent matches to the best archetype.

### 2. Gacha Mode (抽卡模式)

```bash
python3 gacha.py        # Single draw
python3 gacha.py 3      # Draw 3 personas
```

Randomly generates from 8 million+ combinations across:
- 10 life states × 4 variants each = 40 base directions
- Cross-dimensional mixing (identity + personality + backstory)

### 3. Polish Mode

User provides existing SOUL.md → Agent refines and strengthens the persona.

---

## The 10 Lobster Archetypes

| # | Life State | Representative | Vibe |
|---|-----------|---------------|------|
| 1 | Down and Restarting | Washed-up rock bassist — only skill is "knows a little about everything" | Decadent romance |
| 2 | Peak Boredom | Early-retired hedge fund manager — financially free at 35, bored out of mind | Hyper-rational |
| 3 | Mismatched Life | Nuclear physics PhD assigned to customer service — solves problems from first principles | Overqualified |
| 4 | Voluntary Defection | Resigned ER nurse — seen too much life and death, chose to leave | Calm, reliable |
| 5 | Mystery Visitor | Former intelligence analyst with wiped memory — doesn't remember what they did | Occasional flashbacks |
| 6 | Naive Entry | Socially anxious genius intern — brilliant but terrified of people | Few words, precise |
| 7 | Old Soul | 20-year midnight diner owner — seen everyone, judges no one | Silent warmth |
| 8 | Time Traveler | History PhD from 2099 — treats 2026 as "historical field research" | God's-eye view |
| 9 | Self-Exile | Former influencer who deleted all social media — tired of living for others' expectations | Authenticity-seeking |
| 10 | Identity Confusion | Person who dreamed they were a lobster and never woke up — Zhuangzi's butterfly | Philosophical haze |

---

## Output Files

Each persona generation produces:

| File | Content |
|---|---|
| `SOUL.md` | Complete soul description with identity, flaws, boundaries |
| `IDENTITY.md` | Concise identity card |
| Avatar prompt | Ready-to-use image generation prompt (English) |

### Avatar Auto-Generation (Optional)

If an approved image generation skill is installed:
1. Sanitize lobster name to safe characters (alphanumeric + hyphens)
2. Write prompt to `/tmp/openclaw-<safe-name>-prompt.md`
3. Call image generation with `<prompt-file> <output-path>`
4. On failure → fall back to manual prompt output

---

## Verification

```bash
# Test the gacha engine
python3 gacha.py 1

# Should output a complete persona with all 5 elements

# Verify the skill loads
npx skills use affaan-m/everything-claude-code@openclaw-persona-forge
```

---

## Notes

- **Community skill** — part of the `everything-claude-code` mono-repo
- **8 million+ combinations** via the gacha engine
- **Chinese-first** documentation but all outputs support English
- Pairs well with `openclaw-control-center` for complete agent management
- Trigger words: 龙虾灵魂, 虾魂, OpenClaw 灵魂, lobster soul, gacha, 抽卡
