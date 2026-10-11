---
title: "Agentation - Visual Feedback for Agents Setup"
description: "Setup guide for benjitaylor/agentation - 20.2K combined installs. Click-to-annotate visual feedback that points coding agents at exact code."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agentation-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "visual feedback", "frontend", "react"]
---

# Agentation - Setup Guide

**Source:** [benjitaylor/agentation](https://www.skills.sh/benjitaylor/agentation) via skills.sh - 20.2K combined installs across 2 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [benjitaylor/agentation](https://github.com/benjitaylor/agentation) (4,917 stars, NOASSERTION license; pushed Sep 22, 2026; skill layout `skills/agentation/SKILL.md`, plus a second skill at `skills/agentation-self-driving/`)
**Category:** Visual Feedback / Frontend Development
**Quality Tier:** 🟡 Beta - 4,917-star visual feedback tool (Benji Taylor); NOASSERTION license; all sampled verdicts Pass

Agentation is an agent-agnostic visual feedback tool from Benji Taylor (agentation.com). You click elements on a page, add notes, and copy structured output that tells a coding agent exactly which code you mean: instead of describing "the blue button in the sidebar", the agent receives `.sidebar > button.primary` and your note. The toolbar is a React component rendered in the bottom-right corner of a page; click to activate it, then click any element to annotate it. Copied feedback works with Claude Code, Codex, Gemini, Grok, or any AI tool that reads markdown.

The package ships two skills on skills.sh: `agentation` (13,353 installs), the core annotation workflow, and `agentation-self-driving` (6,810 installs), an autonomous critique mode where the agent drives a visible headed browser, scans the page, and adds design annotations itself. For direct sync, an optional MCP server exposes an HTTP endpoint at localhost:4747 that the toolbar connects to.

---

## Installation

Prerequisites: React 18+ on the target page and a desktop browser (mobile is not supported). The toolbar is distributed as an npm dev dependency:

```bash
npm install agentation -D
```

Render it next to your app, as the README shows:

```tsx
import { Agentation } from 'agentation';

function App() {
  return (
    <>
      <YourApp />
      <Agentation />
    </>
  );
}
```

For direct sync with a coding agent, register the MCP server and point the toolbar at its endpoint:

```bash
npx -y agentation-mcp server
```

```tsx
<Agentation endpoint="http://localhost:4747" />
```

The repository also follows the standard skills layout, so skills-compatible agents can install it with the skills CLI:

```bash
npx skills add benjitaylor/agentation
```

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| agentation | 13,353 | Click-to-annotate toolbar: copy structured markdown with selectors, positions, and context so agents grep the exact code |
| agentation-self-driving | 6,810 | Autonomous design critique: the agent drives a headed browser, reviews the page, and adds annotations itself (needs the toolbar plus the agent-browser skill) |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Agents write code well but see user interfaces poorly: feedback like "move the button left" costs extra rounds of guessing because the agent must infer which button and which code. Agentation removes that ambiguity by capturing class names, selectors, and element positions at click time, so the agent can grep for the exact location instead of searching from a description. The structured markdown output is a plain handoff, and the copy path requires no integration - it works with any tool that reads text. The MCP server closes the loop further: with the toolbar pointed at localhost:4747, annotations land where a running agent can read them directly. The self-driving skill flips the direction, critiquing a page on its own in a visible browser. Everything ships as markdown plus a small npm package, so a Hermes agent adopts it the same way it adopts any other skill or dev dependency. For frontend-heavy workflows, this is the missing feedback channel between human eyes and agent edits.

## Usage

| You say | What happens |
|---|---|
| "This card spacing is off, fix it" | Click the card in the toolbar, add the note, and paste the structured markdown into the agent so it gets the exact selector instead of a description |
| "Review the pricing page for me" | agentation-self-driving opens a headed browser, annotates the issues it finds, and you watch the pass in real time |
| "Annotate everything wrong with the nav" | Multi-select (hold Cmd/Ctrl, or drag a region) captures several elements in one structured output block |
| "The hover state looks wrong" | Pause the supported CSS or Web Animations playback, capture the state, and annotate the frozen frame |
| "The widget inside this iframe needs notes too" | Agentation selects elements in open shadow roots and same-origin iframes |
| "Read my latest feedback and fix it" | With the MCP server running, the toolbar endpoint delivers annotations straight to a Claude Code, Codex, Gemini, or Grok session |

## Verification

```bash
# Confirm the npm package landed (install route from the README)
npm ls agentation

# Check which skills a skills-CLI install added
npx skills list | grep -i agentation

# Review the skill file straight from GitHub before installing (this path returned 200)
curl -s https://raw.githubusercontent.com/benjitaylor/agentation/main/skills/agentation/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| agentation | Pass | Pass | Pass |
| agentation-mcp | - | - | - |

## Limitations

- License caveat: GitHub reports NOASSERTION; the README states PolyForm Shield 1.0.0, so treat it as source-available rather than a standard permissive OSI license.
- The MCP server (agentation-mcp) has no sampled security verdicts, and the self-driving skill additionally depends on the separate agent-browser skill being installed.
- React 18+ is required, and the toolbar is desktop-browser only (mobile is not supported).
- Built as a development tool: install with -D and keep the toolbar out of production builds.
- Snapshot data, verified Oct 10, 2026: 20,163 combined installs across 2 indexed listings; 4,917 GitHub stars; NOASSERTION license; last pushed Sep 22, 2026. Counts drift over time.

## Related

- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup) - required by the self-driving skill for its headed-browser critique runs
- [Chrome DevTools MCP Skills - Browser Debugging & Automation Setup](/hermes/skills/catalog/chrome-devtools-mcp-skills-setup) - browser debugging to pair with visual annotations
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup) - structured review pass for the issues the toolbar surfaces
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Render `<Agentation />` next to your app component as the README example does; the toolbar appears in the bottom-right corner.
- Use multi-select for a full review pass: grab several elements with Cmd/Ctrl and send one structured block instead of five separate messages.
- Pause animations before annotating a broken state; the toolbar freezes supported CSS animations, Web Animations, and video so the capture is stable.
- Register `npx -y agentation-mcp server` with your MCP client before asking the agent to read feedback directly.
- Review the raw SKILL.md before installing, and enable the hash-routes option when annotations should be tracked per route rather than per page.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
