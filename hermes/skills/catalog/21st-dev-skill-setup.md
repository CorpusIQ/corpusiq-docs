---
title: "21st.dev Skills - Registry and UI Build Setup"
description: "21st-dev/skill on skills.sh: 13.3K combined installs across 8 listings; search, install and publish React and shadcn components, themes and templates."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/21st-dev-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "shadcn", "react", "ui"]
---

# 21st.dev Skills - Setup Guide

**Source:** [21st-dev/skill](https://www.skills.sh/21st-dev/skill) via skills.sh - 13.3K combined installs across 8 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 34 stars, Apache-2.0 licence, last pushed 2026-09-09, 7 SKILL.md directories under skills/
**Category:** Frontend component workflow for agents: catalog search, AI generation, registry publishing and UI review
**Quality Tier:** 🟡 Beta - Snyk Fail on 21st-registry and a Snyk Warn on 21st-cli-use; Apache-2.0; 34 stars.

21st.dev is a registry of React and shadcn components, themes and templates. This repository ships seven skills that teach an agent the `21st` CLI (`@21st-dev/cli`): search and install existing components, generate and iterate on new ones with 21st AI, publish your own work to a team library, publish the current project's design tokens as a theme, and run three UI workflow skills for building, exploring and reviewing interfaces.

Each skill file is described in the README as a live mirror of `21st.dev/api/skills/<name>`, so the installed copy is regenerated from the hosted version rather than authored in the repo. Authentication is either an API key from `21st.dev/settings/api-keys` or the CLI's own login command.

## Installation

The README installs cross-agent through skills.sh:

```bash
npx skills add 21st-dev/skill
```

It also documents installing the verified pack globally with the 21st CLI itself:

```bash
npx @21st-dev/cli skills install --global
```

For a single skill, the README shows fetching from the mirror directly:

```bash
curl -fsSL https://21st.dev/api/skills/21st-cli-use -o ~/.claude/skills/21st-cli-use/SKILL.md
```

Claude Code and Codex users can instead install one plugin that bundles these skills with the 21st MCP server, from `21st-dev/claude-code-plugin` or `21st-dev/codex-plugin`. Either way, sign in once with `npx @21st-dev/cli login` or set an API key before running catalog commands.

## What It Provides

Seven listings, all above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| 21st-cli-use | 2,277 | Searching the catalog, printing a component or theme, installing an item into the project and handling auth and teams |
| 21st-ai | 2,252 | Sketching a UI from a prompt, previewing variants in the browser, editing one in place and pulling the final code |
| 21st-registry | 2,003 | Publishing a component to a team library, publishing a theme or template listing, and editing or unpublishing items |
| 21st-design-sync | 1,971 | Reading the project's shadcn and Tailwind tokens and publishing them as a shareable community theme |
| 21st-ui-build | 1,632 | Implementing a page, section or responsive redesign using the project's own design context plus grounded inspiration |
| 21st-ui-explore | 1,599 | Comparing meaningfully different UI directions when the user wants options or has not settled on a direction |
| 21st-ui-review | 1,581 | Auditing existing UI for accessibility, responsive behavior, interaction quality and consistency |

One indexed listing sits below the threshold at 15 installs.

## Why This Matters for Hermes Agents

Left alone, an agent asked for a pricing table will hand-write a component that has already been written a thousand times, badly, with inline styles and a missing focus ring. The `21st-cli-use` skill gives it a search step first: look for an existing component, print its code, install it into the project.

The design-sync skill is the more interesting idea. It reads the shadcn and Tailwind variables already in a project and publishes them as a theme, which turns a design system into a portable artifact an agent can hand to another project instead of re-deriving colors from a screenshot.

The three UI workflow skills are deliberately separated by intent. Explore produces options, build produces an implementation, review produces findings. Naming that distinction in a skill description is what stops an agent from reviewing when the user asked for variants.

Finally, the publishing skills make the registry bidirectional, so agent output can land in a team library where a human reviews it rather than in a local file.

## Usage

| You say | What happens |
|---|---|
| "Find a shadcn pricing table with a toggle" | 21st-cli-use searches the catalog and prints matching components |
| "Install the Button from our team library" | 21st-cli-use resolves the team item and adds it to the project |
| "Generate three hero variants and pull the best one" | 21st-ai sketches from the prompt, previews variants and takes the chosen code |
| "Publish our design tokens as a theme" | 21st-design-sync reads the project variables and publishes them |
| "Publish this component to our team library" | 21st-registry publishes the component and returns the listing handle |
| "Give me two different directions for this settings page" | 21st-ui-explore produces distinct concepts grounded in the existing design system |
| "Audit this page for accessibility and mobile behavior" | 21st-ui-review reports findings against design context and production rules |

## Verification

Confirm the skill mirror serves the file the install pulls:

```bash
curl -fsSL https://21st.dev/api/skills/21st-cli-use | head -6
```

It should open with `name: 21st-cli-use` and a description naming the `21st` CLI. The GitHub copy is the same content:

```bash
curl -fsSL https://raw.githubusercontent.com/21st-dev/skill/main/skills/21st-cli-use/SKILL.md | head -6
```

Then check that the install landed as one directory per skill in the skills directory your installer targets:

```bash
ls ~/.claude/skills | grep 21st
```

Seven directories should appear. Catalog commands need authentication, so run `npx @21st-dev/cli login` before testing a search, or set an API key in the environment.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| 21st-cli-use | Pass | Pass | Warn |
| 21st-ai | Pass | Pass | Pass |
| 21st-registry | Pass | Pass | Fail |
| 21st-ui-build | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified 2026-11-04: 13,330 combined installs across 8 indexed listings; 34 GitHub stars; Apache-2.0; last pushed 2026-09-09. Counts drift over time.
- skills.sh indexes 8 listings against 7 skill directories, so at least one listing is a duplicate or an older name. Check the directory name before scripting an install.
- `21st-registry` carries a Snyk Fail and it is the skill that can publish, edit and delete items in your account. Review the source before giving an agent unattended access to a shared library.
- The skills mirror a hosted API. Local edits to an installed `SKILL.md` are lost the next time the CLI or installer refreshes it.
- The three UI workflow skills depend on project design context, meaning a `components.json` and Tailwind tokens. In an empty directory they fall back to generic output.
- Catalog operations need an API key or an interactive login, so a headless agent needs the key injected as a secret rather than run through the login flow.

## Related

- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup)
- [Patterns.dev Skills - UI and Rendering Patterns Setup](/hermes/skills/catalog/patterns-dev-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Search before generating. `21st-cli-use` leads the install counts, and it is the cheaper path: an existing component ships with the edge cases already handled.
- Publish the design tokens early with `21st-design-sync`. Every later UI task then has a shared vocabulary instead of a hex code in a prompt.
- Keep `21st-registry` out of autonomous loops. Publishing and deleting are the two operations you do not want retried after a timeout.
- Use `21st-ui-explore` when the brief is vague and `21st-ui-build` when it is specific. Running both on the same request produces duplicate work.
- Treat generated variants as drafts and run `21st-ui-review` before merging. The review skill checks the accessibility and responsive gaps that generation usually skips.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
