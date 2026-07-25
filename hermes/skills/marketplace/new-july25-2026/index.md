---
title: "New Skills — July 25, 2026 Marketplace Sweep"
description: "3 new publishers, 3 setup guides created, 134K+ combined installs. Morning cron sweep of skills.sh marketplace for Hermes-relevant skills."
---

# New Skills — July 25, 2026

## Summary

| Metric | Count |
|---|---|
| New publishers found | 3 |
| Setup guides created | 3 |
| Combined installs | ~134,000+ |
| Combined GitHub stars | 3,434 ⭐ |
| Quality: 🟢 Production | 3 |
| Quality: 🟡 Beta | 0 |
| Quality: 🔵 Community | 0 |

## New Skills

### Agent Infrastructure

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **LangChain Agent Skills** | langchain-ai/langchain-skills | 71K+ | 996⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/langchain-skills-setup/) |

### Growth Operations

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **OPC Skills (Solopreneur)** | resciencelab/opc-skills | 50K+ | 1,174⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/opc-skills-setup/) |

### Career & Job Applications

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **ResumeSkills** | paramchoudhary/resumeskills | 13K+ | 1,264⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/resumeskills-setup/) |

## 🔑 Standout Find: langchain-ai/langchain-skills (71K+ installs)

LangChain's official agent skills — the most authoritative source for agent memory, persistence, RAG, and middleware patterns. Previously only `deep-agents-memory` was documented as a standalone guide. This sweep creates a publisher-level guide covering all 6 skills: deep-agents-memory (13.1K), langgraph-persistence (11.8K), langchain-rag (11.7K), langchain-fundamentals (11.6K), langgraph-human-in-the-loop (11.3K), and langchain-middleware (10.8K). These are the canonical implementation patterns for production AI agents.

## Other Highlights

- **resciencelab/opc-skills** (50K+ installs, 1,174⭐): The solopreneur's AI toolkit. SEO-GEO alone has 37K installs — the most-installed solopreneur skill on skills.sh. Reddit marketing, Product Hunt launches, logo creation, and Twitter growth complete the stack. Previously only seo-geo had a minimal platform entry.
- **paramchoudhary/resumeskills** (13K+ installs, 1,264⭐): Complete job application optimization toolkit — ATS optimization, LinkedIn profile enhancement, bullet writing, resume tailoring, cover letters, and tech formatting. Directly complements CorpusIQ's existing job-application-engine skill.

## Discovery Method

Bulk sweep: 50+ search terms via `npx skills search` → 139 unique repo/publisher entries → cross-referenced against 304 existing catalog entries → publisher-level verification → 3 confirmed new, 47 filtered (Claude-specific, low stars, already documented under different names, or non-agent-relevant).

## Notes

- **langchain-ai/langchain-skills** supersedes the standalone `deep-agents-memory-setup.md` — the publisher-level guide now covers all 6 LangChain agent skills.
- **resciencelab/opc-skills** replaces the minimal `platform/seo-geo.md` entry — full publisher coverage with all 6 skills.
- **paramchoudhary/resumeskills** is entirely new — no prior catalog entry.
- This is the first July 25 sweep. 139 unique repos were scanned; the vast majority were Claude Code-specific or already documented.
- Notable skipped: `composiohq/awesome-claude-skills` (70K⭐, Claude-focused), `lobehub/lobe-chat` (full app, not skills), `greensock/gsap-skills` (12K⭐, already covered by HyperFrames docs), `jeffallan/claude-skills` (10.7K⭐, Claude-only).
- GitHub API rate limited on some OpenClaw repos — deferred to next sweep.
