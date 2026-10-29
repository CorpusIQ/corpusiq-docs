---
title: "Transitions.dev Skills - CSS Motion Suite Setup"
description: "jakubantalik/transitions.dev: 34.0K combined installs, 5 listings. 35 portable CSS transitions, motion polish rules, and agent build reveals."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/transitions-dev-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "css transitions", "motion design", "frontend animation"]
---

# Transitions.dev Skills - Setup Guide

**Source:** [jakubantalik/transitions.dev](https://www.skills.sh/jakubantalik/transitions.dev) via skills.sh - 34.0K combined installs across 5 indexed listings; snapshot 2026-10-29 (Oct 29 morning sweep)
**GitHub:** [jakubantalik/transitions.dev](https://github.com/jakubantalik/transitions.dev) - 5,888 stars, Transitions.dev License (a custom license GitHub reports as NOASSERTION, with the tooling directories under MIT); branch main, last pushed 2026-10-29; layout: the live website at the repo root plus five SKILL.md files at agent/skill/, refine/.agents/skills/refine-live/, skills/transitions-dev/, skills/transitions-polish/ and skills/transitions-ui-generation/
**Category:** Motion & Interaction Design / Frontend CSS
**Quality Tier:** 🟡 Beta - official transitions.dev repository with 5,888 stars and no FAIL verdicts, but a Snyk Warn on the agent listing, a non-OSI license with paid tiers, and a test suite for the agent CLI that no workflow runs

Transitions.dev is Jakub Antalik's interactive collection of reusable CSS transitions, and this repository is both the live site at transitions.dev and the skill payload generated from it. Every card on the index page demonstrates one interaction pattern and ships a copy-ready, portable CSS snippet; `npm run build` re-parses the page templates out of `index.html` and re-renders everything under `skills/transitions-dev/`, so the showcase and the snippets are generated from the same source rather than maintained by hand.

The suite covers three distinct jobs. `skills/transitions-dev` is the library: drop-in transitions namespaced under `t-*` selectors, wired through semantic CSS custom properties, each shipping a `prefers-reduced-motion` guard, plus decision rules for choosing between a dropdown and a modal, a panel reveal and a page slide, or a text morph and a text states swap. `skills/transitions-polish` is the tuning layer, which reads existing motion along five dimensions (duration, distance, scale, blur, easing) and applies higher-order rules for open/close asymmetry, hover in versus hover out, stagger totals and intent delays. `skills/transitions-ui-generation` plays an "agent is generating this" animation measured from the element itself, and the two CLIs (`transitions-dev` for pulling transitions, `transitions-agent` for scanning a repo and fixing its motion) plus the Refine panel round out the tooling.

## Installation

```bash
# Install the skill payload published on skills.sh
# (the README notes this command also installs skills/transitions-ui-generation)
npx skills add Jakubantalik/transitions.dev

# Pull individual transitions into a project from npm
npx transitions-dev list                 # see everything available
npx transitions-dev add card-resize      # free, no account needed
npx transitions-dev add --free           # every free transition at once

# Pro transitions unlock after a passwordless browser sign-in
npx transitions-dev login
npx transitions-dev add confetti-burst
```

Two of the five SKILL.md files sit outside the `skills/` directory, so the skills.sh installer is not guaranteed to deliver them. Copy those two by hand from the raw path in the tree:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/transitions-agent
curl -sL https://raw.githubusercontent.com/jakubantalik/transitions.dev/main/agent/skill/SKILL.md \
  -o ~/.hermes/profiles/corpusiq/skills/transitions-agent/SKILL.md

mkdir -p ~/.hermes/profiles/corpusiq/skills/refine-live
curl -sL https://raw.githubusercontent.com/jakubantalik/transitions.dev/main/refine/.agents/skills/refine-live/SKILL.md \
  -o ~/.hermes/profiles/corpusiq/skills/refine-live/SKILL.md
```

For the library itself, `skills/transitions-dev/_root.css` is the universal install block: copy it into the project once and import it, or paste only the per-snippet `:root` block that a single reference file restates. The skill instructs the agent not to duplicate that block and not to strip the reduced-motion guard.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| transitions-dev | 21518 | Drop-in CSS for the named transitions (modal, dropdown, panel reveal, page slide, badge, toast, accordion, tabs, tooltip, skeleton reveal, success check, thinking states, streaming text and more) with the decision rules, motion tokens and the four `transitions` commands |
| transitions-polish | 11365 | Tuning motion that already exists: map duration, distance, scale, blur and easing onto the shared token scale, then check open/close asymmetry, hover in versus out, stagger totals and intent delays |
| transitions-ui-generation | 1097 | A generation reveal over any element: dotted wireframe drawn from the component's own structure, glyph-traced headlines, halftone image reveal, in skeleton or skeleton-texts mode |

The remaining 2 indexed listings range from 13 to 33 installs.

## Why This Matters for Hermes Agents

Most agent-written animation fails in the same two ways: a hand-rolled `transition` on the wrong properties with an arbitrary duration, or a rewrite that throws out the accessibility guard. This suite attacks both by giving the agent a closed vocabulary it has to match against instead of a blank page. The decision rules are the valuable part, because they resolve the ambiguous request ("make the dropdown nicer") to one named pattern using the visible UI element and the verb, and the skill is explicit that the agent should not invent a new transition when a listed one fits.

The polish skill encodes a rule that is genuinely hard to infer from training data: a value is wrong when it does not fit what the motion does, not when it is numerically far from a token, so a 300ms modal close is corrected to the 150ms close token while a value whose usage matches no token is left alone. That is a judgment procedure suited to an agent that has to justify each diff. The generation skill is a different kind of asset, since it measures its drawing from the rendered element rather than from a placeholder, which means the reveal lands on real geometry in a page the agent has not seen before.

The trust boundary is ordinary for a design skill: the snippets are CSS and small JS orchestration, nothing here phones home at runtime, and the two CLIs are npm packages that talk to api.transitions.dev only for license checks and hosted fixes. The part that needs a human decision is the license, because the free transitions are free for commercial work but the library may not be repackaged as a competing product.

## Usage

| You say | What happens |
|---|---|
| "Make the modal open smoothly" | The decision rules match a trigger plus a centered surface to modal open / close, and the agent pastes the `06-modal.md` snippet, the `.t-modal` hooks and the close-state cleanup. |
| "The timing feels off across the app, polish my transitions" | transitions-polish scans the five token dimensions and returns a per-file list of lines with the current value and the token it should reference, editing nothing until you confirm. |
| "Why does this list feel late at the end?" | The stagger rule does the arithmetic: 8 items at 120ms is 960ms of total delay, so the offset drops to the 40ms stagger token. |
| "Make this headline look like an AI agent is building it" | transitions-ui-generation's text variant traces every glyph along its real outline in dots, then fades the letters in one by one after a 140ms beat. |
| "Scan the repo and tell me what motion is missing" | `npx transitions-agent@latest --json` scores the project 0-100 and lists every recognized component with the recipe it maps to, then offers a polish fix or a revamp fix before touching files. |
| "List every transition this skill has" | transitions reveal prints the numbered catalog with one-line summaries and the matching reference filename, without reading the project. |
| "Add the motion check to our pull requests" | `npx transitions-agent@latest init-ci` writes both workflows, and its fixes arrive as a pull request into the branch, never straight to main. |

## Verification

Check the raw files before installing. All of the paths below returned 200 when checked on 2026-10-29:

```bash
curl -sL -o /dev/null -w "%{http_code}" https://raw.githubusercontent.com/jakubantalik/transitions.dev/main/skills/transitions-dev/SKILL.md
curl -sL -o /dev/null -w "%{http_code}" https://raw.githubusercontent.com/jakubantalik/transitions.dev/main/skills/transitions-polish/SKILL.md
curl -sL -o /dev/null -w "%{http_code}" https://raw.githubusercontent.com/jakubantalik/transitions.dev/main/skills/transitions-ui-generation/SKILL.md
curl -sL -o /dev/null -w "%{http_code}" https://raw.githubusercontent.com/jakubantalik/transitions.dev/main/agent/skill/SKILL.md
```

Confirm the file landed locally and that the frontmatter names the skill:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/transitions-dev/SKILL.md
head -3 ~/.hermes/profiles/corpusiq/skills/transitions-dev/SKILL.md
```

`head -3` should print `name: transitions-dev` inside the frontmatter block. If the file is missing, the installer skipped the skill and the manual copy route in Installation is the fallback.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| transitions-dev | Pass | Pass | Pass |
| transitions-polish | Pass | Pass | Pass |
| transitions-ui-generation | Pass | Pass | Pass |
| refine-live | Pass | Pass | Pass |
| transitions-agent | Pass | Pass | Warn W012 |

Nothing in this set fails an auditor. The single non-Pass is a Snyk Warn under code W012 on transitions-agent, and the finding text was not included in the sample this guide was built from, so read the code on the skills.sh security page rather than inferring it from the label. What can be said from the tree is what that listing asks for: the skill runs `npx transitions-agent@latest` from the repository root, so npm fetches the current package at run time; it authenticates against api.transitions.dev with a license key resolved from `TRANSITIONS_AGENT_LICENSE` or `~/.transitions-agent.json`; and its `fix` step writes to your source files, with `fix --pr` opening a branch and pull request instead. `init-ci` writes GitHub workflow files and, with `--yes`, stores the license as a repository secret. That is a legitimate shape for a code-fixing agent and also the shape a reviewer should check first.

The skill's own guardrails match that reading: never run `fix` without the user choosing a fix mode, never push to main, and stop if a proposed fix would touch component logic rather than motion. No `curl | bash` installer ships in this repository, and the only `curl` calls in the SKILL.md files target a local relay on `localhost:7331`, not a remote script.

## Limitations

- Snapshot data, verified 2026-10-29: 34026 combined installs across 5 indexed listings; 5888 GitHub stars; Transitions.dev License; last pushed 2026-10-29. Counts drift over time.
- This is the transitions.dev website with the skills attached, not a skills-only repository. A clone brings `index.html`, `CNAME`, the auth and account pages, the billing and marketing pages and the build tooling along with the five skill directories, so install the skill payload or single raw files rather than treating the repo root as a skill.
- The license is not OSI-approved. GitHub reports NOASSERTION; the `LICENSE` file is the custom Transitions.dev License, which grants unlimited personal and commercial use, modification and shipping inside your own product, forbids repackaging the library as a competing transitions or motion product, and places `agent/`, `cli/`, `refine/`, `build/` and `scripts/` under MIT. Pro transitions and the paid Agent features require a Pro or Business plan, and Business is required when a company is the user.
- Index names and tree paths do not line up one to one. The five indexed listings are transitions-dev, transitions-polish, transitions-ui-generation, refine-live and transitions-agent, while the tree stores them at `skills/transitions-dev/`, `skills/transitions-polish/`, `skills/transitions-ui-generation/`, `refine/.agents/skills/refine-live/` and `agent/skill/SKILL.md`. Two of the five sit outside `skills/`, and the `refine-live` path is nested under a `.agents` directory, so a top-level installer may not collect them.
- Internal counts drift inside the skill. `skills/transitions-dev/SKILL.md` describes "thirty-two" transitions while its quick reference and the tree carry 35 reference files, and the README still says eighteen. Trust the reference files, not the prose count.
- Single maintainer, high release cadence: the last commit landed on the same day as this snapshot. Pin the copy you install if you need reproducible output.

## Related

- [Meng To Skills - Frontend & Motion Design Suite Setup](/hermes/skills/catalog/mengto-skills-setup)
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup)
- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup)
- [GSAP Skills - GreenSock Animation Platform Setup](/hermes/skills/catalog/greensock-gsap-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `skills/transitions-dev` first and treat `_root.css` as the one place motion values live; pasting per-snippet `:root` blocks alongside it duplicates the tokens and makes the polish pass report phantom mismatches.
- Run `transitions reveal` before asking for anything ambitious. The catalog is the contract, and an agent that knows the 35 named patterns stops inventing a tenth variant of a dropdown.
- Pair the two skills the way the author intends: transitions-dev installs a whole transition, transitions-polish tunes what you already have. Running polish first on a page with no motion produces an empty audit.
- Keep the `prefers-reduced-motion` block in every pasted snippet. It is the single thing most likely to be "cleaned up" by a later agent edit, and removing it breaks the accessibility guarantee the library advertises.
- For the agent CLI, choose the fix mode deliberately: polish is the free-plan treatment and produces small diffs on the existing token scale, revamp installs whole recipes and needs a Business key. Ask for the scan first, since it is read-only and free.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
