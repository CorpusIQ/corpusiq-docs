---
title: "AI Design Skills - Agentic Product Design Suite Setup"
description: "owl-listener/ai-design-skills - 10.9K combined installs: 44 skills, 18 commands and 6 plugins for designing AI products, from prompts to evaluation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/owl-listener-ai-design-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "ai design", "prompt engineering", "evaluation"]
---

# AI Design Skills - Agentic Product Design Suite Setup

**Source:** [owl-listener/ai-design-skills](https://www.skills.sh/owl-listener/ai-design-skills) via skills.sh - 10.9K combined installs across 44 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [owl-listener/ai-design-skills](https://github.com/owl-listener/ai-design-skills) - 212 stars, MIT, main branch, last pushed Jun 9, 2026; skills live under skills/<plugin>/<skill>/SKILL.md with claude-plugin/ and gemini-extension/ mirrors.
**Category:** AI Product Design and Agentic Experience Design
**Quality Tier:** 🟢 Green - every one of the 20 sampled skills passes Gen Agent Trust Hub, Socket and Snyk with no Warn or Fail cells.

The AI Design Skills Collection is 44 skills, 18 commands and 6 plugins for designing AI products, organised around six layers: model interaction, alignment reasoning, system behaviour, evaluation, agent orchestration and prompt architecture. It is part of the Designer Skills suite and installs for both Claude Code and Gemini CLI, with the same skills and shape on each agent.

The skills are translations of academic and industry work, from alignment research and HCI scholarship, into a form coding agents can load. REFERENCES.md lists the source papers and RESEARCH.md maps each paper to the skill it became, so the collection is traceable back to its academic origin.

## Installation

Add the Claude Code marketplace, then install plugins from it:

```bash
claude plugin marketplace add owl-listener/ai-design-skills
claude plugin install model-interaction-design@ai-design-skills
```

Install all six plugins at once:

```bash
for p in model-interaction-design ai-alignment-reasoning system-behavior-shaping evaluation design-agent-orchestration prompt-architecture; do
  claude plugin install "$p@ai-design-skills"
done
```

For Gemini CLI, clone the monorepo and install each extension from its local path:

```bash
git clone https://github.com/owl-listener/ai-design-skills
cd ai-design-skills
gemini extensions install ./gemini-extension/model-interaction-design
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| system-prompt-structure | 505 | the anatomy of effective system prompts: role, context, constraints, format |
| guardrail-design | 431 | defining behavioral boundaries for what the AI should and should not do |
| constraint-specification | 413 | defining output format, length, tone and content boundaries within prompts |
| generative-ui | 374 | designing interfaces where the AI generates UI components dynamically |
| conversation-patterns | 366 | turn-taking, repair sequences, grounding and dialogue structure |
| persona-architecture | 361 | defining AI character, voice and personality traits |
| progressive-disclosure | 360 | revealing AI capability gradually to match user mental models |
| trust-calibration | 353 | helping users form warranted trust, neither overtrust nor undertrust |
| context-window-design | 352 | designing around token limits, memory and conversation persistence |
| feedback-loops | 348 | user correction, thumbs up and down, inline editing, reinforcement signals |
| tone-calibration | 344 | adjusting formality, warmth, confidence and style per context |
| transparency-patterns | 341 | showing users what the AI knows, does not know and how confident it is |
| chain-of-thought-design | 339 | designing reasoning chains that produce better outputs |
| template-design | 333 | reusable, parameterised prompt templates for consistent outputs |
| frustration-detection | 331 | reading user emotion from text signals and adapting before disengagement |
| emotional-design | 331 | how the AI responds to frustration, confusion, delight and distress |
| few-shot-patterns | 326 | crafting examples that steer AI behavior effectively |
| multimodal-orchestration | 324 | coordinating text, image, voice and tool use in one interaction |
| mixed-initiative-flow | 317 | when the AI leads, when the user leads, and how control is handed off |

The remaining 25 indexed listings range from 155 to 194 installs.

## Why This Matters for Hermes Agents

Building an AI product is a design problem as much as an engineering one, and an agent that only knows how to call a model ships interactions that frustrate users: over-confident answers, walls of output, no way to correct a mistake, no signal when the model is guessing. This collection turns the discipline the README calls agentic experience design into six named layers, so an agent can be pointed at trust-calibration, transparency-patterns or feedback-loops instead of improvising. Each skill is a translation of academic work, and RESEARCH.md maps every skill back to its source paper, which matters when a design choice has to be defended.

The collection is agent-agnostic. The same 44 skills ship for Claude Code and Gemini CLI with identical shape, so the design guidance does not fork between agents. For a builder shipping soon, the evaluation and alignment layers are the ones to install first, because they map the failure modes before launch rather than after a user files a complaint.

## Usage

| You say | What happens |
|---|---|
| Design the system prompt for our assistant | Uses system-prompt-structure plus persona and tone skills |
| How do I stop it hallucinating with confidence | Uses trust-calibration and transparency-patterns |
| Make the onboarding reveal features gradually | Uses progressive-disclosure and mixed-initiative-flow |
| Set up a feedback loop so users can correct it | Uses feedback-loops and frustration-detection |
| Add reasoning to improve its answers | Uses chain-of-thought-design and few-shot-patterns |
| We need to evaluate the assistant before launch | Uses the evaluation plugin: rubrics, benchmarks, heuristics |
| Design a multi-agent handoff | Uses handoff-protocols and task-decomposition |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/owl-listener/ai-design-skills/main/README.md | head -40
```

Confirm the generative-ui skill body is present before UI work:

```bash
curl -sL https://raw.githubusercontent.com/owl-listener/ai-design-skills/main/skills/model-interaction-design/generative-ui/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| system-prompt-structure | Pass | Pass | Pass |
| guardrail-design | Pass | Pass | Pass |
| constraint-specification | Pass | Pass | Pass |
| generative-ui | Pass | Pass | Pass |
| conversation-patterns | Pass | Pass | Pass |
| persona-architecture | Pass | Pass | Pass |
| progressive-disclosure | Pass | Pass | Pass |
| trust-calibration | Pass | Pass | Pass |
| context-window-design | Pass | Pass | Pass |
| feedback-loops | Pass | Pass | Pass |
| tone-calibration | Pass | Pass | Pass |
| transparency-patterns | Pass | Pass | Pass |
| chain-of-thought-design | Pass | Pass | Pass |
| template-design | Pass | Pass | Pass |
| frustration-detection | Pass | Pass | Pass |
| emotional-design | Pass | Pass | Pass |
| few-shot-patterns | Pass | Pass | Pass |
| multimodal-orchestration | Pass | Pass | Pass |
| mixed-initiative-flow | Pass | Pass | Pass |
| task-decomposition | Pass | Pass | Pass |

The 24 listings outside the sample carry no verdict cells in this guide, so check their own pages before installing them.

## Limitations

- Snapshot data, verified Nov 23, 2026: 10,890 combined installs across 44 indexed listings; 212 GitHub stars; MIT licence; last pushed Jun 9, 2026. Counts drift over time.
- The 44 listings are not a flat band: the top 19 clear 300 installs and the remaining 25 range from 155 to 194, reflecting which layers designers reach for first.
- The collection is part of the Designer Skills suite; installing the suite adds four more collections in one command, so this repo is one of five doors into the same body of work.
- The same skill exists three times in the tree (skills/, claude-plugin/ and gemini-extension/); install the plugin for your agent, not the raw skill files.
- 24 of the 44 listings sit outside the verdict sample and carry no security cells in this guide.

## Related

- [AI Design Components - Full-Stack Skill Suite Setup](/hermes/skills/catalog/ai-design-components-setup)
- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)
- [Designer Skills - Design Workflow Setup](/hermes/skills/catalog/designer-skills-setup)
- [Impeccable Design Setup](/hermes/skills/catalog/impeccable-design-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install model-interaction-design and prompt-architecture first; the README calls them the foundation for any agentic feature.
- Install all six at once with the marketplace loop; the plugins are small and one command covers them.
- For Gemini CLI, clone and run gemini extensions install per extension directory; the monorepo needs local paths.
- Read RESEARCH.md to trace a skill to its source paper when a design decision needs a citation.
- Use the evaluation plugin before launch: failure modes are cheaper to find in a rubric than in production.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
