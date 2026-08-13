---
title: Creative Ideation — Skill Setup Guide
description: Install and configure ideation, the Hermes Agent skill for generating creative project ideas through constraint-driven brainstorming — 111 installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ideation-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Creative Ideation — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/ideation) (111 installs)
**Category:** Creative / Productivity
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** Hermes Agent

Generate project ideas through creative constraints. The philosophy: constraint + direction = creativity. When you have tools but no direction, this skill picks a constraint from its library, interprets it broadly, and generates three concrete project ideas. If you pick one, it builds it.

---

## What It Does

| Step | Action |
|------|--------|
| **1. Pick constraint** | Selects from a library of creative constraints (random or matched to domain) |
| **2. Interpret broadly** | A coding constraint can become hardware; an art constraint can become a CLI tool |
| **3. Generate 3 ideas** | Concrete, buildable project ideas that satisfy the constraint |
| **4. Build it** | If you pick one, Hermes creates the project, writes the code, ships it |

---

## The Constraint Library (Examples)

| Constraint | Example Ideas It Produces |
|-----------|--------------------------|
| "Only uses the terminal" | TUI game, CLI dashboard, terminal-based art tool |
| "Must work offline" | Local-first note app, offline map viewer, P2P file share |
| "Under 100 lines" | Micro-CLI tool, single-page web toy, one-function library |
| "Opposite of your last project" | If you built a REST API → build a real-time WebSocket app |
| "For a non-technical user" | Grandma-friendly photo organizer, business owner dashboard |
| "Uses AI in an unexpected way" | AI recipe generator from fridge photos, AI plant disease detector |

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill ideation
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/creative/ideation ~/.hermes/skills/
```

---

## Basic Usage

### Get unstuck

```
> I want to build something but don't know what
```

### Domain-specific ideation

```
> Give me project ideas for a CLI tool
```
```
> I have a Raspberry Pi and sensors — what should I build?
```

### Pick and build

```
> I'll take idea #2. Build it.
```

Hermes switches from ideation mode to execution mode, creating the project structure and implementing the idea.

---

## When to Use

| ✅ Use When | ❌ Skip When |
|------------|-------------|
| "I want to build something" | You already have a spec |
| Learning a new tool/framework | Production deadline looming |
| Hackathon/prototype brainstorming | You need a specific solution |
| Creative block / boredom | Task is clearly defined |
| Exploring what's possible with your stack | Working from a ticket |

---

## Tips

- **The constraint is the spark, not the cage:** Interpret loosely
- **Say "more" to get fresh ideas:** The skill generates 3 at a time but can keep going
- **Mix constraints:** "Under 100 lines AND uses AI" produces tighter ideas
- **Save good ideas:** The skill doesn't persist — note the ones you might revisit
- **Domain matters:** Mention your stack/interests for more relevant ideas

---

## How It Differs from `creative-ideation`

The `ideation` skill focuses on buildable project ideas with a constraint-first approach and "pick one and build it" workflow. The `creative-ideation` skill (26 installs) is a lighter brainstorming tool without the build-execution phase. Use `ideation` when you want to actually ship something.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [nousresearch/hermes-agent on skills.sh](https://skills.sh/nousresearch/hermes-agent)*

*Powered by CorpusIQ*
