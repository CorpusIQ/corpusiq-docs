---
title: "IART Web Animation Skills - GSAP and SVG Suite"
description: "iart-ai/web-animation-skills: 26.2K combined installs. Nine skills for GSAP, SVG, Lottie, micro-interactions, page transitions and 60fps motion."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/iart-web-animation-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "web animation", "gsap", "svg"]
---

# IART Web Animation Skills - Setup Guide

**Source:** [iart-ai/web-animation-skills](https://www.skills.sh/iart-ai/web-animation-skills) via skills.sh - 26.2K combined installs across 9 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 76 stars, license MIT, last pushed 2026-06-22, 9 SKILL.md directories
**Category:** Web animation for agents: GSAP timelines, SVG and Lottie motion, micro-interactions and 60fps performance
**Quality Tier:** 🟡 Yellow - clean layout and MIT licence, but only 76 stars and one of the five sampled listings, gsap-web, carries a Snyk warning

IART publishes this pack as web animation skills for AI coding agents, and the repository description puts the scope in one line: GSAP, SVG, Lottie, micro-interactions, page transitions and 60fps performance, installed straight into your agent. The tree holds nine `SKILL.md` directories under `skills/`, and the README describes each one in its own row.

The pack is unusually well matched to the index: nine listing names on skills.sh and nine skill directories in the tree, one for one. Each skill is a narrow topic rather than a general animation guide, so an agent mounts only the knowledge the current component needs, whether that is a scroll-scrubbed GSAP timeline, an SVG stroke draw-on, a Lottie player, a frosted-glass panel or a reduced-motion fallback.

## Installation

The README documents the skills CLI first, then a Claude Code plugin marketplace route:

```bash
npx skills add iart-ai/web-animation-skills
```

```bash
/plugin marketplace add iart-ai/web-animation-skills
/plugin install web-animation-skills
```

The README states that the skills run in Claude Code, Cursor, Codex and 40 or more agents. Nothing in the install section mentions Hermes, and the skills are Markdown, so a profile skills directory takes the same tree:

```bash
git clone --depth 1 https://github.com/iart-ai/web-animation-skills.git /tmp/iart-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -R /tmp/iart-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

All nine folders can be copied at once, or one at a time when you only want motion knowledge for a specific stack. There is no API key, no CLI binary and no service account in this pack.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| accessible-animation | 3,139 | Tiered `prefers-reduced-motion` handling that degrades gracefully instead of removing all motion. |
| 60fps-animation | 3,059 | Reaching 60 or 120fps by animating only `transform` and `opacity` and removing layout thrash. |
| svg-animation | 3,035 | Stroke draw-on, path morphing, motion along a path, and animated icons, gradients and filters. |
| micro-interaction | 2,982 | Hover and press feedback, toggles, toasts, drawers, and list or layout motion with Framer Motion and CSS. |
| gsap-web | 2,940 | Code-driven motion with GSAP: timelines, ScrollTrigger, SplitText, Flip and Lenis smooth-scroll sync. |
| glassmorphism | 2,885 | Frosted-glass and Liquid Glass panels: backdrop-filter, edge highlights, refraction, specular sweeps and reduced-transparency fallbacks. |
| page-transition-animation | 2,798 | Enter and exit page transitions in the Next.js App Router, including the AnimatePresence exit fix. |
| ascii-animation | 2,687 | Generative ASCII fields and image, video or 3D to ASCII for terminals, canvas and Three.js. |
| lottie-animation | 2,653 | Integrating, controlling, theming and exporting Lottie or dotLottie across web, iOS, Android and React Native. |

All 9 indexed listings appear in the table above.

Every listing in the table has a matching directory in the pack layout, so there is no shadow inventory to reconcile here. The install counts are also the tightest spread of the three packs in this sweep: the top listing holds 3,139 and the bottom holds 2,653, a range of 486, which suggests nine capabilities adopted together rather than one flagship skill carrying the set.

## Why This Matters for Hermes Agents

Motion is where generated frontends usually look generated. A model that has never been told to animate only `transform` and `opacity` will animate `height`, `top` or `margin`, and the result is a janky page that no amount of copy editing fixes. The 60fps skill states the constraint as a rule, which is exactly the kind of instruction an agent follows more reliably than a taste-based request.

The pack also splits knowledge by surface, which fits how an agent actually works. A hero section needs GSAP timelines and ScrollTrigger. A logo needs SVG stroke draw-on. A Next.js route change needs the App Router transition pattern plus the exit-animation fix. Loading that as one skill per task keeps the prompt small and the advice specific, instead of dumping every animation technique into context on the chance that one applies.

Accessibility is handled as a first-class skill rather than a footnote. The tiered `prefers-reduced-motion` approach reduces amplitude and distance instead of deleting the animation outright, which is the difference between a page that respects a user setting and a page that looks broken for anyone who enabled it.

The narrow scope has a cost worth naming. These are technique skills, not a design system: they will make a transition smooth and a path draw correctly, and they will not decide whether the motion belongs. That judgment stays with the builder, which is the right division but not an absent one.

## Usage

| You say | What happens |
|---|---|
| "Build a pinned hero that scrubs a timeline to scroll" | gsap-web supplies the timeline, ScrollTrigger pin and scrub pattern, plus smooth-scroll sync through Lenis. |
| "My CSS animation is janky, make it run at 60fps" | 60fps-animation audits the animated properties, moves the work to `transform` and `opacity`, and removes layout thrash. |
| "Add page transitions in my Next.js App Router app" | page-transition-animation wires enter and exit states and applies the AnimatePresence exit fix. |
| "Make my animations respect prefers-reduced-motion without removing everything" | accessible-animation applies the tiered fallback so motion softens instead of disappearing. |
| "Animate this SVG logo so it draws itself on" | svg-animation sets stroke dash offset and timing for the draw-on, with path morphing as a follow-up option. |
| "Give this card a frosted glass look with a light sweep" | glassmorphism builds the backdrop-filter panel, edge highlight and specular sweep, with a reduced-transparency fallback. |
| "Convert this video into an ASCII field for a terminal" | ascii-animation generates the character field for terminal, canvas or Three.js output. |

## Verification

The raw path below is built from the layout in this pack and returned 200 on branch main when this guide was written on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  "https://raw.githubusercontent.com/iart-ai/web-animation-skills/main/skills/gsap-web/SKILL.md"
```

After a clone, count the directories and check that each folder ships a `SKILL.md` with frontmatter rather than a bare README:

```bash
git clone --depth 1 https://github.com/iart-ai/web-animation-skills.git /tmp/iart-skills
find /tmp/iart-skills/skills -name SKILL.md | wc -l
for d in /tmp/iart-skills/skills/*/; do head -1 "$d/SKILL.md"; done
ls ~/.hermes/profiles/corpusiq/skills | grep -c animation
```

The count should be 9. The second command confirms every directory opens with YAML frontmatter, which is what makes the folder loadable as a skill rather than as documentation. The last command tells you how many of these skills are already in the profile before you copy again, which is the cheapest way to avoid stacking two copies of `gsap-web`.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| accessible-animation | Pass | Pass | Pass |
| svg-animation | Pass | Pass | Pass |
| gsap-web | Pass | Pass | Warn |
| page-transition-animation | Pass | Pass | Pass |
| lottie-animation | Pass | Pass | Pass |

Four of the five sampled listings pass all three auditors, which is the cleanest sample of the three packs in this sweep. The exception is `gsap-web`, the only listing with a Snyk warning, and it is also the listing that ships the most third-party surface: GSAP itself, ScrollTrigger, SplitText, Flip and Lenis are all named in the skill's own description.

That is the audit shape to think about here. The skills are Markdown, so the direct code risk is low, but the instructions tell an agent which packages to install. `gsap-web` is the one to read line by line before you let an agent run its install commands, since a package name in prose becomes a dependency on disk. GSAP's own licence terms for the plugins it names are a separate question from the skill licence, and the skill does not restate them.

There is no API key, no network call and no credential path in this pack. The only external dependency is the package ecosystem the animation skills reference, and the fallbacks in `glassmorphism` and `accessible-animation` mean a page still renders when a browser feature is missing.

## Limitations

- Snapshot data, verified November 3, 2026: 26,178 combined installs across 9 indexed listings; 76 GitHub stars; license MIT; last pushed 2026-06-22. Counts drift over time.
- The repository is small in stars relative to its install count, 76 against 26.2K installs, so community review of the instructions is thinner than the adoption number suggests.
- `gsap-web` is the only sampled listing with a Snyk warning, and it is the skill that names the most third-party packages. Read its install lines before running them.
- The pack is one of a 14-pack collection in the same organisation, so overlapping skills from a sibling pack can collide if you install several at once. Copy only the folders for the stack you are using.
- These are technique skills. They do not choose a motion language for a product, and installing them does not produce a consistent animation system by itself.
- Nothing in the README documents a Hermes install path, and the plugin marketplace route is Claude Code specific. The profile copy above is the closest equivalent.

## Related

- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup)
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup)
- [Motion Graphics Skills - Launch Video Suite](/hermes/skills/catalog/motion-graphics-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `accessible-animation` alongside whatever else you take. It is the skill that keeps every other one usable for people who have reduced motion turned on, and it is the highest-installed listing in the pack for a reason.
- Ask for the property audit before the rewrite. "Which properties are animating here, and which of them trigger layout" gets a specific answer from 60fps-animation, and it is faster than asking for a fix and guessing why it landed.
- Reach for `page-transition-animation` only on the App Router. The skill is written around that router, and its exit-animation fix does not translate to the Pages Router.
- Keep `glassmorphism` behind a feature check. The skill documents reduced-transparency fallbacks, and a frosted panel without one is a readability problem on low-end displays.
- Treat the README's agent list as guidance, not a support matrix. The skills are Markdown, so they load anywhere, but the plugin commands are Claude Code syntax.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
