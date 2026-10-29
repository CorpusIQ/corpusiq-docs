---
title: "Refero Design - Research-First UI Design Skill Setup"
description: "Refero Design: 12.2K combined installs. A research-first UI design skill with a read-only MCP over 150,000 real app screens and 6,000 user flows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/refero-design-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "ui design", "design research", "mcp", "frontend"]
---

# Refero Design - Setup Guide

**Source:** [referodesign/refero_skill](https://www.skills.sh/referodesign/refero_skill) via skills.sh - 12.2K combined installs across 1 indexed listing; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [referodesign/refero_skill](https://github.com/referodesign/refero_skill) - 328 stars, MIT, branch master, last pushed 2026-10-15; one skill at `skills/refero-design/SKILL.md` with a bundled `references/` directory beside it, plus plugin manifests for Claude Code, Codex, Cursor and Gemini CLI

**Category:** Research-first UI and product design skill with a read-only design-research MCP

**Quality Tier:** 🟡 Beta - vendor maintained with 328 GitHub stars, a single skill carrying the whole 12.2K combined count, a paid plan behind live research, and a Snyk warning on the sampled listing

Refero is a design research product sold as a skill plus a connection. The repository packages one skill, `refero-design`, and one read-only MCP server, and the skill is written so that research comes before implementation on every visual task. Live research reaches curated visual styles, more than 150,000 real app screens and more than 6,000 user flows from shipped products, so an agent can ground a layout or a checkout sequence in what real interfaces actually do instead of pulling from model memory.

The interesting part is what the skill forbids. It refuses single-reference copying, it refuses averaging several references into a safe middle, and it refuses design decisions that cannot be traced to a reference, a user constraint or a bundled craft rule. Before code is written the agent has to produce a reference lock and a decision ledger, and the bundled references cover typography, color, motion, icons, forms, copywriting and a dedicated anti-AI-slop checklist. The same skill is installable as a Claude Code plugin, a Codex plugin, a Gemini CLI extension, a ChatGPT or Codex plugin directory entry and a plain skills directory copy, and it stays useful with no account at all, working from its bundled craft files.

## Installation

The README's standalone command installs the one skill through a skills CLI, which is the route to use when the client already has the MCP configured or you only want the methodology:

```bash
npx skills add https://github.com/referodesign/refero_skill --skill refero-design
```

Claude Code takes the plugin, which carries the skill and the MCP manifest together:

```text
/plugin marketplace add referodesign/refero_skill
/plugin install refero@refero
```

Codex installs from the marketplace as well, and the README asks for an app restart afterwards:

```bash
codex plugin marketplace add referodesign/refero_skill
codex plugin add refero@refero
```

Gemini CLI takes the repository as an extension:

```bash
gemini extensions install https://github.com/referodesign/refero_skill
```

ChatGPT and Codex can also install from the OpenAI plugin directory, linked in the README, and sign in with a Refero account when prompted; that path needs no manual MCP config. Cursor is listed as available through its plugin marketplace or `/add-plugin` once the listing is approved.

The MCP connection is separate from the skill. The SKILL.md documents the Claude Code spelling for the HTTP endpoint:

```bash
claude mcp add --transport http refero https://api.refero.design/mcp
```

Then run `/mcp` in Claude Code and sign in when prompted; the README states the first connection opens Refero in the browser for OAuth.

Nothing in the repository is written for Hermes, so the manual route is a directory copy. Clone and copy the whole skill directory rather than only `SKILL.md`, because the README is explicit that the `references/` files have to stay beside it:

```bash
git clone https://github.com/referodesign/refero_skill.git
cp -R refero_skill/skills/refero-design ~/.hermes/profiles/corpusiq/skills/
```

The README also warns about older layouts: past clones put `SKILL.md` at the repository root, so remove that installation before reinstalling, or the profile carries two skills with the same trigger surface.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| refero-design | 12163 | Research-first UI and product design across landing pages, dashboards, app screens, redesigns and CSS polish: style, screen and flow research through the Refero MCP when available, bundled typography, color, motion, icon, copy and anti-AI-slop references otherwise, then a reference lock and decision ledger before implementation. |

No indexed listings fall below the threshold; the single indexed listing appears in the table above.

## Why This Matters for Hermes Agents

Design is the place where an agent's lack of taste is most visible. Left alone, a model produces the same hero, the same three feature cards and the same rounded indigo gradient, and it presents that output with full confidence because nothing in the loop compared it to anything real. Refero attacks that directly: the skill makes research a precondition, so an implementation that cannot name its references is treated as unfinished work rather than a finished draft.

The reference lock is the mechanism worth copying into other domains. Before building, the agent writes down one primary direction, three to five traits that must survive, at most two details borrowed from other sources, the roles that tokens are allowed to fill, a media strategy and the defaults it is deliberately rejecting. When the build drifts, the lock is the thing that catches it, and a Hermes run can hand that lock to a human for approval before spending time on code.

Scope discipline is built into the tool routing. Styles are the visual layer, screens are the concrete pattern layer, and flows are the multi-step journey layer, and the SKILL.md says which one to reach for: styles first for anything visual, screens for what a dashboard or empty state should contain, flows when a sequence such as signup, checkout or cancellation is in play. That is a clearer division of labor than most design skills offer, and it keeps an agent from answering a journey question with a color palette.

The quality gate is written as questions with yes or no answers, which makes it checkable by an agent rather than aspirational. Can every major choice be traced to a source? Did the work avoid the current slop signals such as decorative serif word swaps, warm cream canvases and generic section order? Was imagery preserved as imagery instead of faked with CSS boxes? For unattended Hermes work, a checklist an agent can fail is more valuable than a style guide it can only admire.

## Usage

| You say | What happens |
|---|---|
| "Design a landing page for our analytics product" | The skill forms a short brief, searches several visual angles, pulls three or four full styles, locks one primary direction with borrowed details, then builds to that lock instead of a template. |
| "What should the billing settings screen contain" | Screen research rather than style research: it looks for real billing, cancellation and settings screens, then extracts layout, hierarchy, states and copy patterns. |
| "Map out the cancellation journey before we build it" | Flow research returns the steps, decision points, confirmations and exit states of real cancellation flows, which the agent turns into journey logic for the new product. |
| "Give me three directions for this redesign" | Visual exploration mode produces three reference-locked options and asks you to choose, with each option traceable to named references rather than to a mood word. |
| "This page feels like every other AI startup site" | The anti-AI-slop reference runs against the screenshot or capture, naming the specific defaults present and the craft rules being broken. |
| "Tighten the typography and spacing on this dashboard" | Craft references for type scale, density, spacing and radius are applied with tokens defined first, and the primary reference's traits are preserved rather than normalized away. |
| "Audit this screen against our chosen direction" | Audit mode takes captured screenshots or Refero screens as evidence, then reports actionable drift from the locked direction before handoff. |

## Verification

Probe the skill and its references on the master branch before installing. Every URL below returned 200 when this guide was written:

```bash
for p in skills/refero-design/SKILL.md \
         skills/refero-design/references/mcp-tools.md \
         skills/refero-design/references/typography.md \
         skills/refero-design/references/anti-ai-slop.md \
         skills/refero-design/references/visual-workflow.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/referodesign/refero_skill/master/$p"
done
```

Read two files before trusting the install. `SKILL.md` carries the non-negotiables and the tool routing, and `references/mcp-tools.md` carries the MCP tool list:

- https://raw.githubusercontent.com/referodesign/refero_skill/master/skills/refero-design/SKILL.md
- https://raw.githubusercontent.com/referodesign/refero_skill/master/skills/refero-design/references/mcp-tools.md

After the copy, confirm the layout landed correctly. A skill directory with `references/` beside `SKILL.md` is the whole test, and the frontmatter name should read `refero-design`:

```bash
ls ~/.hermes/profiles/corpusiq/skills/refero-design
head -3 ~/.hermes/profiles/corpusiq/skills/refero-design/SKILL.md
grep -c . ~/.hermes/profiles/corpusiq/skills/refero-design/references/*.md | wc -l
```

For the MCP side, ask the agent to run `refero_search_styles` with a simple query. A working connection returns styles; a rejected call means the OAuth sign-in has not completed or the account has no active plan. The README's own release check, `scripts/check-release`, validates manifests, the canonical MCP URL and secret leaks if you want to inspect a clone before installing anything.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| refero-design | Pass | Pass | Warn W011 |

The warning applies to the sampled skill listing rather than to the whole repository, and the repository ships a `SECURITY.md` with a private reporting address at support@refero.design. The MCP connection itself is read-only by design, and the README states that every connection manifest points at the same production endpoint with no access tokens inside. Live research requires a paid Refero account, so treat the connection as a metered external service rather than a free data source. Installation copies text files: the skill directory holds a `SKILL.md` and its references, and nothing in the install path executes beyond the client's own plugin loader.

## Limitations

- Snapshot data, verified 2026-10-28: 12163 combined installs across 1 indexed listing; 328 GitHub stars; MIT license; last pushed 2026-10-15. Counts drift over time.
- The default branch is `master`, not `main`. Every raw URL in this guide and the README commands assume `master`, so do not rewrite them to `main`.
- Live research needs a paid Refero plan. Without one the skill still runs, but it falls back to the bundled craft references and whatever references you supply, so its strongest layer is unavailable.
- Styles cover web marketing and product pages such as landing, pricing and editorial sites. The SKILL.md states that in-app dashboards, auth screens, settings screens and iOS app screens are not yet style systems, so product UI work pairs styles with screen and flow research.
- The 150,000 screen and 6,000 flow figures are the vendor's own counts and cannot be checked from the repository, which contains no data.
- Cursor support is described as pending a marketplace approval, and nothing in the repository is documented for Hermes, so the manual directory copy above is the supported route and single-skill filtering is the only install option offered.
- The sample is one skill, so the security verdict table covers the entire indexed surface but says nothing about the Refero service behind the MCP endpoint.

## Related

- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)
- [Meng To Skills - Frontend & Motion Design Suite Setup](/hermes/skills/catalog/mengto-skills-setup)

## Pro Tips

- Install it even if you never buy a plan. The non-negotiables, the reference lock template, the decision ledger and the anti-AI-slop checklist are plain files, and they change how an agent behaves before it types a single CSS rule.
- Make the reference lock a checkpoint a human approves on high-visibility pages. Three traits and two borrowed details are cheap to review and expensive to discover after a full build.
- Ask for styles before screens on anything visual. The SKILL.md is explicit that screens should support structure and concrete detail, not carry the visual direction.
- Remove an old root-level `SKILL.md` from a previous clone before installing again. Two copies of the same skill compete for the same triggers and the agent picks unpredictably.
- When a build drifts, ask which reference each decision came from. A choice with no source is exactly the case the skill is designed to catch, and naming it in conversation is usually enough to get the drift fixed.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
