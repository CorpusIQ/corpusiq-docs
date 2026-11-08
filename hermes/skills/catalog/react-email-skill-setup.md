---
title: "React Email Skill - Template Authoring for Agents"
description: "resend/react-email on skills.sh: 9.9K combined installs; one skill for React Email templates, local preview and sending through Resend."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/react-email-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "email templates", "react email", "transactional email"]
---

# React Email Skill - Setup Guide

**Source:** [resend/react-email](https://www.skills.sh/resend/react-email) via skills.sh - 9,922 combined installs across 1 indexed listing; first seen 2026-11-08 (Nov 8, 2026 morning sweep)
**GitHub:** 19,916 stars, MIT via LICENSE.md, `canary` branch, last pushed 2026-11-06, 1 SKILL.md directory at `skills/react-email/` with six reference files beside it
**Category:** Email templates for agents: React Email components, local preview workflow and sending through Resend
**Quality Tier:** 🟢 Recommended - MIT licence, 19,916 stars, Pass on all three scanners, and a single well-scoped skill with a test log in the repository.

The star count is the library, not the skill. React Email is the component set that most new transactional email is written with, and this skill is the instruction file that teaches an agent to use it correctly instead of writing 2010 table markup in JSX. `SKILL.md` is 400 lines, backed by six references, and it exists because the library's failure modes are not obvious from the API: `rem` units, flexbox, media queries and SVG all look reasonable in TypeScript and all break in Outlook.

The skill is opinionated in ways that are easy to check. It requires `Tailwind` with `pixelBasedPreset`, because email clients do not support root-relative units. It bans flexbox and grid in favour of `Row` and `Column`, bans `sm:` and `md:` variants and `dark:` selectors outright, and requires `box-border` on every `Button` and an explicit border style on anything with a border, since email clients do not inherit border type. None of that is discoverable from autocomplete, and the cost of getting it wrong is a template that previews perfectly and collapses in Gmail.

The repository is a pnpm monorepo, and the skill is one directory inside it, next to `packages/`, `examples/` and `apps/`. That shape matters in two ways. The install is the generic skills CLI rather than a bespoke path, and the skill's own frontmatter declares version 2.1.0 while pointing at `react.email` as its homepage, so the skill and the npm package version independently.

## Installation

The README's own instruction for agents is one line, under a heading called "Using with AI":

```bash
npx skills add resend/react-email
```

That installs the skill, not the library. The library is a normal npm dependency, and the skill assumes it is present:

```bash
npm i react-email@latest
```

For a fresh project, the README's scaffold creates a working preview app with an `emails` folder already wired:

```bash
npx create-email@latest
cd react-email-starter
npm install
npm run dev
```

To add previews to an existing application, the skill's own instructions add one script and point it at a folder relative to the project root:

```json
{
  "scripts": {
    "email": "email dev --dir emails --port 3000"
  }
}
```

The dev server runs on port 3000 and previews every template in that folder. Any package manager works, so pnpm and bun need no special handling beyond the equivalent command.

## What It Provides

The threshold for this guide is zero installs, so the single indexed listing appears below:

| Skill | Installs | Use For |
|---|---|---|
| react-email | 9,922 | Writing HTML email as React components, previewing locally, rendering to HTML or plain text, and sending through Resend or another provider |

One row clears the threshold, and since the threshold is zero there is no tail. No rows fall below the threshold.

With one listing, the table is also the whole adoption story: 9,922 installs against 19,916 stars, roughly one install for every two stars. That ratio is high for a package where starring is free, and it suggests the install is being driven by the agent skill's own discovery path rather than by people browsing the library.

The content is genuinely deep for a single file. `SKILL.md` covers the component inventory with structural rules attached (`Container` only once per email, at its built-in 37.5em max width, with `Section` for interior blocks), a mandatory clarification step before writing any template (brand colour as hex, logo format with a warning against SVG and WEBP, tone, and the production URL for static assets), and the static file pattern that most people get wrong: images go in `emails/static/`, and the `src` is built from an environment check so the same file works in preview and in production, with an explicit instruction never to hardcode `localhost:3000`.

The references carry the rest. `COMPONENTS.md` is the full component reference, `STYLING.md` covers typography, layout and dark mode with the required-class table, `SENDING.md` has Resend, Nodemailer and SendGrid examples, `PATTERNS.md` has password reset, order confirmation, notification and team invitation templates, `I18N.md` covers next-intl, react-i18next and react-intl, and `EDITOR.md` documents the embeddable editor built on TipTap and ProseMirror. `TESTS.md` at the skill root is a RED-GREEN compliance log with dated baselines: the mustache-variable test records the unaided agent writing `firstName = "{{firstName}}"` as a default prop, and the skill-loaded run placing `{{firstName}}` only in `PreviewProps`.

The rendering and sending paths are both one-liners, which is the practical reason to keep the skill around. `render()` returns HTML, and `render(..., { plainText: true })` returns the text alternative. The Resend SDK takes the component directly through a `react` prop and handles both renderings, so there is no intermediate HTML string to keep in sync.

## Why This Matters for Hermes Agents

Hermes sends a lot of email, and every template it writes by hand is a small piece of legacy. The recurring failure is an agent producing markup that looks right in a browser and wrong in an inbox: a `div` with `display: flex`, a `rem` font size, a media query, a WEBP logo. The skill converts each of those into a written prohibition with a replacement, which is the only form of instruction that survives a long context. Telling an agent "make it responsive" produces media queries. Telling it "media queries are unsupported, use `Row` and `Column`" produces a layout that works in Outlook.

The second fit is verification. A React Email template can be rendered to HTML and diffed, exported to static files through the CLI, and inspected for size before sending. That gives an agent a real acceptance test instead of a visual claim, and it is why the skill's `email export --outDir <path> --pretty --plainText` command is worth knowing: it turns a template folder into artefacts a test can assert on.

The third is that the skill encodes the accessibility defaults the library already ships. `Html` sets `lang` and `dir`, `Img` defaults to `alt=""` so decorative images are skipped by screen readers, `Markdown` emits layout tables with `role="presentation"`, and `Preview` also emits a `<title>`. An agent that knows those defaults stops adding redundant attributes, and an agent that knows the remaining content rules (linked images are never decorative, headings never skip levels, 4.5:1 contrast) produces email that passes an audit without a separate pass.

The honest counterweight: this skill writes email, it does not govern sending. Deliverability, authentication, retry semantics and suppression live in a sibling skill, and installing this one alone gets you pretty templates that still land in spam.

## Usage

| You say | What happens |
|---|---|
| "Build a welcome email with a verify button" | Asks for brand colour, logo format, tone and production asset URL before writing the component |
| "Make the layout two columns on desktop" | Uses `Row` and `Column`, refuses flexbox and grid, and explains why |
| "Add a dark mode variant" | Declines `dark:` selectors, which most clients ignore, and suggests contrast-safe colours instead |
| "Preview it" | `email dev` on port 3000 against the `emails` folder, with `PreviewProps` supplying the sample data |
| "Render it to HTML for the API" | `render(<Template ... />)` for HTML, or `render(..., { plainText: true })` for the text part |
| "Send it through Resend" | Passes the component as the `react` prop to `resend.emails.send`, which handles HTML and plain text |
| "Add a logo" | Places it in `emails/static/`, builds the URL from an environment check, and warns against SVG or WEBP |
| "Let users edit the template in the app" | Pulls in `@react-email/editor`, documents `EmailEditor`, `StarterKit`, `Inspector` and `composeReactEmail` |

## Verification

The repository's default branch is `canary`, not `main`, so the raw path has to be built against that branch. This one returned 200:

```bash
curl -fsSL https://raw.githubusercontent.com/resend/react-email/canary/skills/react-email/SKILL.md | head -40
```

It should open with YAML frontmatter naming `react-email`, a description that scopes it to building HTML email templates with React components and sending with Resend, and `license: MIT` followed by a `metadata` block reading `author: Resend`, `version: "2.1.0"`, `homepage: https://react.email`. Under that you should see `# React Email` and then `## Installation` with `npm i react-email`.

Confirm the reference files ship with the skill, because the SKILL.md is thin without them:

```bash
curl -fsSL https://raw.githubusercontent.com/resend/react-email/canary/skills/react-email/references/COMPONENTS.md | head -20
```

After install and a package install, the cheapest end-to-end check is a real export rather than a preview:

```bash
npx email export --dir emails --outDir out --pretty --plainText
```

That should write one HTML and one text file per template. If the command is missing, the library is not installed; if the HTML contains `rem` units or a `@media` block, the template violated the styling rules and the skill did not take effect.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react-email | Pass | Pass | Pass |

The skill itself is markdown. All three scanners returning Pass reflects the absence of executable payload, not an audit of what an agent will build with it.

The real surface is npm and the API key. Following this skill installs `react-email`, and optionally `@react-email/editor` with TipTap and ProseMirror behind it, plus `resend` for sending. That is a conventional dependency chain, but it is also three packages deep from a skill file to the code that runs, and the repository pins its own workspace with `pnpm-lock.yaml` while your project will resolve its own versions. Review the lockfile after install rather than trusting the skill's examples.

Sending is the part to scope deliberately. The skill's sending path uses `RESEND_API_KEY` from the environment, and an agent that holds a production key can mail real recipients from your verified domain with a plausible template. That is the intended behaviour and it is also the failure mode: put the key in a scoped environment, keep it out of the working tree, and prefer a test domain or restricted key outside production work. The skill does not include any code that reads or exfiltrates credentials.

## Limitations

- Snapshot data, verified 2026-11-08: 9,922 installs across 1 indexed listing, 19,916 GitHub stars, MIT via `LICENSE.md`, `canary` as the default branch, last pushed 2026-11-06.
- The 19,916 stars belong to the React Email library, not to the skill. Most stargazers have never installed the agent skill, so the star count is a proxy for library trust rather than for skill adoption.
- The default branch is `canary`, so every raw URL and every installed copy tracks unreleased code. A path that resolves today can move without a release, which is why the verification commands above pin the branch explicitly.
- 1 indexed listing and 1 SKILL.md directory match, so there is no directory drift. There is no second listing to cross-check the install count against.
- The repository is a pnpm monorepo whose root `package.json` reads version `0.0.0`, while the skill frontmatter declares 2.1.0. There is no release tag for the skill itself, so a pin means pinning a commit.
- Requires Node and a project with JSX support in `tsconfig.json`. The skill says so directly, and a project without JSX will fail at the first import rather than at install.
- Sending through Resend assumes a Resend account and a verified sending domain. Other providers are supported through the rendered HTML path, but the examples and the `email resend setup` command are Resend-first.
- The cross-agent claim (Claude Code, Codex, Cursor, GitHub Copilot and others) comes from the README and could not be verified beyond the CLI install working.

## Related

- [Resend Agent Skills - Setup Guide](/hermes/skills/catalog/resend-skills-setup)
- [Email Best Practices Skill - Deliverability for Agents](/hermes/skills/catalog/email-best-practices-skill-setup)
- [Agent Email CLI Skill - Setup Guide](/hermes/skills/catalog/agent-email-cli-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the export, not the preview. `email export --pretty --plainText` produces files you can grep for `rem`, `@media` and `display:flex`, which catches the three failures that preview will not show you.
- Keep `PreviewProps` populated for every template. It is the only place a mustache placeholder belongs, and it is what makes the dev server render a realistic email rather than empty fields.
- Treat `box-border` on buttons and an explicit border style as non-negotiable review items. Both are one-word omissions that only show up in Outlook, and both are listed as required classes in the skill's styling reference.
- Add the emailed template folder to your test suite as fixtures. Once `render()` is in the build, a unit test that asserts the HTML contains no `rem` and the expected links is cheaper than a manual client matrix.
- Check the branch before trusting a raw URL. This repository ships from `canary`, and a `main` path can exist and still be stale, so verify against the branch you actually install from.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
