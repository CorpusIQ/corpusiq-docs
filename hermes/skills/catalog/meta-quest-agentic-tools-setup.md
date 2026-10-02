---
title: "Meta Quest Agentic Tools - Horizon OS VR Dev Suite Setup"
description: "Setup guide for meta-quest/agentic-tools: 39 official Meta agent skills for Quest and Horizon OS VR development. 5.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/meta-quest-agentic-tools-setup/"
robots: "index,follow"
last_updated: "2026-09-30"
tags:
  - hermes skill
  - agent skill
  - skill setup
  - vr development
  - horizon os
  - meta quest
---

# Meta Quest Agentic Tools - Horizon OS VR Dev Suite Setup

**Source:** [meta-quest/agentic-tools](https://github.com/meta-quest/agentic-tools) (204⭐, Apache-2.0, main branch, updated Sep 30, 2026) / **Skill:** `meta-quest/agentic-tools` (39 installable skills, 5.4K combined installs) / **Publisher:** Meta Quest (official) / **Category:** VR Development / Meta Quest / Horizon OS / **Quality Tier:** 🟡 Beta (official Meta org, Apache-2.0, young repo with community validation pending, verified Sep 30, 2026)

meta-quest/agentic-tools is the official Meta Quest repository of agent skills for Horizon OS and Quest VR development. It bundles 39 skills, most prefixed with hz- for Horizon OS workflows, covering Unity development, WebXR, Perfetto performance tracing, VR debugging, and project scaffolding. Combined installs sit at 5.4K, which reflects a young repository rather than limited usefulness: the Apache-2.0 license and official Meta ownership make it the authoritative VR skill source for Hermes agents.

## Installation

```bash
npx skills add meta-quest/agentic-tools
```

After installation, run `npx skills --list` and expect 39 entries under `meta-quest/agentic-tools`. You can also clone the repository with `git clone https://github.com/meta-quest/agentic-tools.git` and copy individual `SKILL.md` folders into your agent's skills directory if you only need a subset.

## Roster

| Skill | Installs | Does |
|---|---|---|
| portal | 258 | Quest developer portal and publishing workflows |
| hz-immersive-designer | 195 | Immersive scene and app design guidance for Horizon OS |
| hz-vr-debug | 190 | VR debugging workflows and common failure triage |
| hz-perfetto-debug | 185 | Perfetto tracing for Quest performance analysis |
| hz-new-project-creation | 183 | New Horizon OS project scaffolding |
| hz-iwsdk-webxr | 182 | Immersive Web SDK and WebXR development |
| hz-quest-verify-first | 179 | Pre-flight verification checklists for Quest builds |
| hz-unity-code-review | 175 | Unity code review standards for VR projects |
| +31 more hz-* skills | 3.9K combined | Horizon OS and Quest development topics from the full suite |

## CorpusIQ Use Cases

| Use Case | How It Helps |
|---|---|
| XR demos for investor and enterprise pitches | hz-immersive-designer and hz-new-project-creation shorten demo builds |
| Quest store submissions | hz-quest-verify-first enforces pre-submission checklists |
| Performance work on VR prototypes | hz-perfetto-debug covers tracing and frame-time analysis |
| Unity code quality for VR projects | hz-unity-code-review applies Meta review standards |

## Limitations / Verification

Verified Sep 30, 2026. The repository has 204 stars and 39 skills; install figures were confirmed against the skills marketplace on the same day. Individual install counts are modest because the repository is young, and community validation is still accumulating. The repository was updated on Sep 30, 2026, the day of verification.

## Security

License: Apache-2.0 from the official Meta Quest GitHub organization, permissive for commercial and internal reuse.

| Scanner | Status |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Gemini Skills Setup](/hermes/skills/catalog/gemini-skills-setup)
- [Assistant UI Skills Setup](/hermes/skills/catalog/assistant-ui-skills-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*

*Powered by CorpusIQ*
