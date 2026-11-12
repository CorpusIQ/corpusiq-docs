---
title: "Code Review Skill - 20+ Language Review Guides"
description: "awesome-skills/code-review-skill: 5.1K combined installs across 2 listings, 21,000 lines of review guidance for 20+ languages loaded on demand"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/code-review-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "security", "react", "python"]
---

# Code Review Skill - Setup Guide

**Source:** [awesome-skills/code-review-skill](https://www.skills.sh/awesome-skills/code-review-skill) via skills.sh - 5.1K combined installs across 2 indexed listings; first seen Jun 5, 2026 (Nov 11, 2026 sweep)
**GitHub:** 2,249 stars, MIT license, `main` branch, last pushed 2026-09-08, 50 tracked files with one `SKILL.md` at the repository root and a `reference/` directory of per-language and cross-cutting guides
**Category:** Engineering quality: structured pull request review, per-language checklists, security review, severity labelling
**Quality Tier:** 🟡 Established - 2,249 stars, MIT, three Pass verdicts on the primary listing and a genuinely large corpus, with a Snyk Warn on the sibling listing keeping it short of the top band.

The problem this skill addresses is consistency. Ask three agents to review the same pull request and you get three different reviews at three different levels of abstraction: one critiques naming, one rewrites the function, one approves without comment. This pack fixes the shape of the review before the content is discussed.

The mechanism is progressive disclosure, and the README states the numbers. The core `SKILL.md` is about 220 lines. Language guides run 200 to 1,100 lines each and load only when the skill decides they apply, which is why the repository can hold more than 21,000 lines of review guidance without costing 21,000 lines of context on every unrelated turn. Frontend coverage includes React 19 with Next.js and TanStack Query v5, Vue 3.5, Angular 17+ with signals, and Svelte 5. Backend and systems coverage includes Rust, TypeScript, NestJS, Java 17 and 21, Java 8 for legacy, PHP, Ruby, Rails and Python. Separate cross-cutting references cover security review, N+1 queries, error handling, async and concurrency, SQL injection and XSS.

The review process itself is four phases: gather context on scope and intent, review architecture, performance and test strategy at a high level, then go line by line, then produce a decision with action items. Every finding carries a severity label from a fixed set, which is the part that makes the output usable in a real review thread.

## Installation

The README's primary route is the skills CLI. It notes one constraint plainly: the CLI looks for `SKILL.md` at the repository root, so do not nest this skill under `skills/`.

```bash
npx skills add awesome-skills/code-review-skill
```

The manual route is a clone into the agent's skills directory, which also works for a Hermes profile:

```bash
git clone https://github.com/awesome-skills/code-review-skill.git \
  ~/.claude/skills/code-review-skill
```

Or add it to an existing plugin's skills folder so it travels with that plugin:

```bash
cp -r code-review-skill ~/.claude/plugins/your-plugin/skills/code-review/
```

A custom slash command is documented for hosts that support them, and the README gives the file to write:

```markdown
<!-- .claude/commands/review.md -->
```

The clone has to preserve the `reference/` directory. A copy that takes only `SKILL.md` installs a skill that will look for language guides and find none, which degrades silently into generic advice.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| code-review-skill | 4,406 | Full four-phase review across 20+ languages and frameworks, with per-language guidelines loaded on demand and severity-labelled findings. |
| code-review-excellence | 687 | The same review corpus published under a second listing name, for hosts that index it separately. |

Both indexed listings clear the threshold and appear above. The install index carries two listings against one `SKILL.md` in the tree, so the second name is a duplicate entry rather than a second skill.

The repository ships 50 tracked files, and almost all of them are reference guides: per-language files such as `reference/react.md` and `reference/java8.md`, security review, and a `reference/cross-cutting/` set covering N+1 queries, error handling, async and concurrency, SQL injection and XSS. The README is bilingual, with an English section and a Chinese section carrying the same tables.

## Why This Matters for Hermes Agents

Review is the highest-leverage place to put a procedure, because it is repetitive, adversarial and expensive to do badly. An agent reviewing without a process produces whatever the diff suggests to it, and diff-suggested review has a known failure mode: it comments on what is visible and misses what is absent, such as the missing test or the unchecked error path.

The four phases force the absent into view. Phase one asks what the pull request is meant to do, which is the question that exposes a change that does the wrong thing competently. Phase two asks about tests before reading the code. Only phase three goes line by line.

The severity vocabulary is the practical part. A reviewer who can label a finding `nit` instead of arguing about it saves the author a round trip, and a `blocking` label ends a discussion that would otherwise continue for a day. The six labels here are a complete set: blocking, important, nit, suggestion, learning and praise. The last two are what most automated review omits, and they are what makes a review something an author reads rather than endures.

Security coverage is separate rather than scattered. The pack has a dedicated security review guide plus per-language security checklists, which matters because security findings in review are the ones most often missed by an agent optimising for style.

## Usage

| You say | What happens |
|---|---|
| "Review this PR" | Runs the four-phase process, gathers scope and intent first, then returns findings with severity labels and an approval decision. |
| "Review this React component" | Loads the React 19 and Next.js reference alongside the core skill and applies the frontend checklist. |
| "Is there anything dangerous in this diff?" | Applies the security review guide and the relevant language security checklist rather than a general scan. |
| "Check this query for performance problems" | Loads the N+1 and SQL references, then points at the access pattern rather than the formatting. |
| "Review my Python service like a senior engineer" | Uses the Python guide with the collaborative tone, asking questions instead of issuing mandates. |
| "Why did this review flag nothing?" | Re-runs phase two, which asks about tests and architecture before line-by-line work, to find what the first pass skipped. |
| "Summarise this review for the author" | Returns the decision, blocking items and action list in the documented output shape. |

## Verification

The skill is a single `SKILL.md` at the repository root, which is short. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/awesome-skills/code-review-skill/main/SKILL.md | head -6
```

The core file should be around 220 lines and reference the per-language guides rather than embedding them. Confirm the references came with the install, because the skill cites them by relative path:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/awesome-skills/code-review-skill/main/reference/security-review-guide.md
```

If you installed by copying a single file, that second check is the one that matters: a skills directory holding `SKILL.md` without `reference/` will run, and will not have the language guidance.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| code-review-skill | Pass | Pass | Pass |
| code-review-excellence | Pass | Pass | Warn |

The primary listing passes all three scanners, and the duplicate name draws a single Snyk Warn. The package is markdown plus reference files: no scripts, no network calls, no credentials, which is why the scanner results are clean.

The thing to keep in view is what a review skill is allowed to do in your workflow. This one reads a diff and writes findings. It does not execute the code under review, and it should not be given credentials to fetch private repositories on your behalf without a reason. A Pass says the instructions are safe to load, not that a review they produce is correct.

## Limitations

- Snapshot data, verified 2026-11-11: 5,093 combined installs across 2 indexed listings; 2,249 GitHub stars; MIT; last pushed 2026-09-08. Counts drift over time.
- The two indexed listings are one skill under two names. The second is not a separate package, and installing both creates a duplicate.
- Coverage is broad but version-pinned. React 19, Angular 17+, Svelte 5 and Java 21 are current at this snapshot; older framework versions may need the Java 8 style legacy guides or fall back to the TypeScript and Python references.
- The `reference/` directory must travel with `SKILL.md`. A single-file install degrades silently.
- Progressive disclosure depends on the model choosing to load a language guide. A vague request such as "review this" may never trigger the load, and the result is the generic review the skill exists to prevent.
- The repository has no runnable test of its own review quality. The guidance is curated opinion, consistently applied, not a benchmarked standard.
- Last push is three months before this snapshot, so framework guidance will drift as the named versions move.

## Related

- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)
- [github-code-review - Setup Guide](/hermes/skills/catalog/github-code-review-setup)
- [Alibaba Open Code Review - AI Code Review CLI Setup](/hermes/skills/catalog/alibaba-open-code-review-setup)

## Pro Tips

- Name the language in the request. The whole value of the pack is the per-language load, and "review this TypeScript service" triggers it where "review this" may not.
- Ask for severity labels explicitly on the first run. Once the output has them, the follow-up conversation is about the blocking items rather than about tone.
- Use phase two as a standalone question. "What is this PR missing?" returns more than a line-by-line pass on the same diff.
- Keep the security guide in the loop for anything touching auth, queries or user input. It is the reference most often skipped by an agent optimising for style.
- Pair it with a static analyser rather than replacing one. The skill documents the split: linters catch mechanics, this catches intent, and a review that duplicates the linter wastes the reader's attention.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
