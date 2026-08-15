---
title: Etincel MCP
description: Deterministic AI-writing-tell detector for operators — 20 tools that audit prose for AI patterns, train brand voices from real writing samples, and run as a local CLI, MCP server, or GitHub Action.
category: Content
stars: n/a (new listing)
added: 2026-08-15
source: mcp.so
relevance: ★★★
tags: [ai-writing-audit, content-quality, brand-voice, style-guide, prose-analysis, ci-cd, content-ops, self-hosted]
---

# Etincel MCP

**Self-hosted MCP server (stdio, no auth) — plus an optional hosted API** — Etincel finds the AI tells in non-fiction prose deterministically, on your own machine: 20 tools that audit text for chatbot fingerprints, train brand voices from real writing samples, and measure drafts against a voice baseline, with a CLI, MCP server, and GitHub Action sharing one codebase (MIT).

```
Server type: Local (stdio) + optional hosted API
Auth: None for stdio; account only for the model-based `second_read` tool
Endpoint: npx etincel serve (local) · https://etincel.ai/api/mcp (hosted)
Tools: 20 (audit, voice training, style management, dictionaries)
Pricing: Free, open source (MIT); hosted second_read is a billed model call
Category: Content / Writing Quality
Built by: AIStoryHub (github.com/AIStoryHub/etincel, etincel.ai)
```

## Why This Matters for Operators

Every operator shipping AI-drafted content faces the same risk: copy that reads synthetic destroys trust before the message lands. Etincel turns that risk into a deterministic check — `audit_text` scans for banned hype vocabulary, chatbot fingerprints, and structural patterns (uniform paragraph length, stacked transitions, em-dash overuse, rule-of-three compulsion) and returns a tiered verdict with each finding located by line. Because it is deterministic, the same text always gets the same verdict, which is what makes it safe to gate commits and CI runs on it.

**The differentiator is the voice-training loop.** `train_style` measures a real writer's habits — sentence length and variance, paragraph rhythm, contraction rate, em-dash and semicolon use, structural entropy — and persists them as a named voice. Drafts can then be checked against that baseline with `check_voice_match`, so brand voice stops being something reviewers eyeball and becomes something an agent can measure before content ships. The `.etincelrc` file makes the banned-words and house-style dictionary reviewable, versioned code, not a hidden vendor config.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `audit_text` | Deterministic scan for AI-writing tells; tiered verdict (green/yellow/orange/red), scored findings with severity and location, plus a strengths counter-signal |
| `train_style` | Train a persistent brand voice from real writing samples (rhythm, contractions, punctuation habits, recurring phrasing) |
| `check_voice_match` | Measure a draft's rhythm against a trained voice baseline — verdict, match score, and per-dial drift notes |
| `check_self_repetition` | Detect a writer's own recurring openings and characteristic phrases across recent pieces |
| `list_styles` / `get_style_guide` | Enumerate presets and trained voices; fetch the full drafting guide for a style |
| `create_style_from_dials` | Build a voice from explicit dials (formality, warmth, directness) plus 8 mechanical dials — no samples needed |
| `update_style` / `fork_style` / `delete_style` / `set_default_style` | Rename or retune voices, fork public community styles, manage defaults |
| `add_banned_word` / `remove_banned_word` | Extend the banned-words list globally or per style |
| `add_custom_word` / `remove_custom_word` / `list_dictionary` | Maintain the allowed-words list (corporate dictionary: acronyms, house terms) |
| `set_style_instructions` / `clear_style_instructions` / `get_style_instructions` | Layer free-text drafting rules (required CTAs, forbidden topics) on top of any voice |
| `second_read` | One model call reading a draft like a careful human editor — hosted only, unscored, never a silent rewrite |

## Installation

```bash
claude mcp add etincel -- npx -y etincel serve
```

The CLI doubles as a linter for files in CI: `npx etincel lint README.md`, and the GitHub Action runs as `AIStoryHub/etincel@main` against pull requests.

## Configuration

```json
{
  "mcpServers": {
    "etincel-nonfiction": {
      "command": "npx",
      "args": ["etincel", "serve"]
    }
  }
}
```

No keys or accounts are needed for the local install — audit, training, and voice checks all run offline. The only hosted dependency is `second_read`, which requires an account at etincel.ai because it bills a model call; a `.etincelrc` at the repo root carries the shared team dictionary and style instructions (dictionary as code, reviewable and versioned).

## Business Relevance

- **Content operators** get a pre-publish gate that flags AI tells with line references before copy reaches customers — tiered verdicts instead of binary detector scores.
- **Brand and marketing teams** can encode a real founder's voice from samples and check every draft against it, including drift warnings per dial.
- **Engineering teams** run the same checks in CI via the GitHub Action or `npx etincel lint`, so style gates survive the human reviewer's absence.
- **Agencies** can fork and reuse public community styles, then retrain them on client samples — voice work becomes a versioned asset, not a per-project retelling.

## Integration with CorpusIQ

Etincel pairs with CorpusIQ as the quality gate on the content pipeline's output side. CorpusIQ connectors (GA4, Search Console, Stripe, Klaviyo) surface the performance data that tells you what to publish; Etincel checks the copy itself before it ships. The workflow composes cleanly: an agent drafts X posts, outreach emails, or docs pages, calls `audit_text` against the CorpusIQ house dictionary in `.etincelrc` (banned hype vocabulary, no em-dash rules, approved product terms), and only content that passes a green or yellow tier proceeds to publishing. Prose Coach (also in this catalog) covers the same problem as a no-auth remote service — Etincel is the self-hosted, CI-friendly complement when copy must stay in-house. For voice work, `train_style` can be fed real Benoit-approved writing samples so future drafts are measured against the actual operator voice, not a generic tone prompt.

## Limitations

- **Brand new** — submitted to mcp.so August 15, 2026; no track record or community adoption yet.
- Local-first: trained voices and self-repetition history live on the installing machine — a hosted/remote connection reports zero history today.
- `second_read` is the only model-based tool and requires a paid etincel.ai account; it fails with a clear explanation on pure stdio installs.
- `check_voice_match` measures rhythm and mechanics — it is explicitly not an authorship or AI-detection proof, and short inputs return low-confidence verdicts.
- Stdio transport means per-machine setup; there is no multi-user OAuth model like CorpusIQ's connectors.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
