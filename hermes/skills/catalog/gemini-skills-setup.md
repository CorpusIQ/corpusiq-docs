---
title: "Gemini Skills - Official Google AI Development Suite Setup"
description: "Setup guide for google-gemini/gemini-skills: official Google skills for Gemini API, Live API, Omni Flash, and Vertex AI development. 47.8K+ installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gemini-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-30"
tags:
  - hermes skill
  - agent skill
  - skill setup
  - google gemini
  - vertex ai
  - ai development
---

# Gemini Skills - Official Google AI Development Suite Setup

**Source:** [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) (4,231⭐, Apache-2.0, main branch, updated Sep 29, 2026) / **Skill:** `google-gemini/gemini-skills` (5 installable skills, 47.8K combined installs) / **Publisher:** Google (official) / **Category:** AI Development / Google Gemini / Vertex AI / **Quality Tier:** 🟢 Production (official Google org, Apache-2.0, 4.2K stars, verified Sep 30, 2026)

google-gemini/gemini-skills is the official Google repository of agent skills for Gemini development. It covers the Gemini API, the SDK, model and agent interactions, the Live API for realtime sessions, and the Vertex AI platform. With 47.8K combined installs across five skills it is one of the most adopted skill suites in the Hermes ecosystem, and its Apache-2.0 license makes it safe to reuse in production work.

## Installation

```bash
npx skills add google-gemini/gemini-skills
```

After installation, run `npx skills --list` to confirm all five skills are registered under `google-gemini/gemini-skills`. You can also clone the repository with `git clone https://github.com/google-gemini/gemini-skills.git` and copy individual `SKILL.md` folders into your agent's skills directory if you only need a subset.

## Roster

| Skill | Installs | Does |
|---|---|---|
| gemini-api-dev | 22.4K | Gemini API and SDK development patterns for agent code |
| gemini-interactions-api | 12.5K | Model and agent interaction flows, multi-turn orchestration |
| gemini-live-api-dev | 9.1K | Realtime Live API sessions with audio and video streaming |
| gemini-omni-flash-api | 1.5K | Omni Flash model usage for multimodal requests |
| vertex-ai-api-dev | 1.3K | Vertex AI API development and deployment workflows |

## CorpusIQ Use Cases

| Use Case | How It Helps |
|---|---|
| Agent pipelines on Gemini models | gemini-api-dev provides tested SDK patterns for CorpusIQ agent workflows |
| Realtime voice features | gemini-live-api-dev speeds up Live API integration for voice interfaces |
| Model cost evaluation | gemini-omni-flash-api supports flash model experiments before scaling |
| Enterprise deployments | vertex-ai-api-dev guides Vertex AI setups for enterprise customers |

## Limitations / Verification

Verified Sep 30, 2026 against the repository at 4,231 stars and its skills.sh listing. Skill count (5) and install figures were confirmed on that date. Install counts drift over time, and the suite assumes familiarity with Google Cloud credentials and the Gemini SDK. The repository was updated on Sep 29, 2026, so the content is current as of verification.

## Security

License: Apache-2.0 from an official Google GitHub organization, permissive for commercial and internal reuse.

| Scanner | Status |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Assistant UI Skills Setup](/hermes/skills/catalog/assistant-ui-skills-setup)
- [Meta Quest Agentic Tools Setup](/hermes/skills/catalog/meta-quest-agentic-tools-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*

*Powered by CorpusIQ*
