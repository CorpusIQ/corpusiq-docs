---
title: "n8n Engineering Skills - Repository Workflows for Agents"
description: "n8n-io/n8n on skills.sh: 6.3K combined installs; repo engineering skills for PR titles, bug reproduction, UI copy and endpoint security"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/n8n-engineering-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "n8n", "engineering workflow", "code review", "pull requests"]
---

# n8n Engineering Skills - Setup Guide

**Source:** [n8n-io/n8n](https://www.skills.sh/n8n-io/n8n) via skills.sh - 6.3K combined installs across 20 indexed listings (6,336 exact); first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 209,960 stars, NOASSERTION license field, `master` branch, last pushed 2026-11-10, 40 `SKILL.md` files among 33,401 blobs, with skills at `.agents/skills/<name>/` and one at `.opencode/skills/setup-mcps/`
**Category:** Repository engineering: contribution conventions, PR creation, bug reproduction, content design and review workflows
**Quality Tier:** 🟡 Solid with caveats - the largest star count in this batch, but the repository carries a NOASSERTION licence and the sampled verdicts include Warnings.

These are n8n's own working skills, committed into the main product monorepo rather than published as a separate package. They are the procedures the n8n team uses on its own codebase: how to title a pull request so the `check-pr-title` CI job accepts it, how to turn a Linear ticket into a failing test, how to gate a REST endpoint behind an RBAC scope, how to write UI copy. The publisher page claims 59 skills, the skills.sh list renders 20 of them, the tree carries 40 `SKILL.md` files, and the 20 rendered listings account for 6,336 installs.

The naming is the first thing to understand, because it explains half the table. Each skill directory sits under `.agents/skills/<name>/`, and each `SKILL.md` declares a namespaced frontmatter name such as `n8n:create-pr`. The index therefore carries many skills twice, once under the directory name and once under the frontmatter name, with different install counts for each. `create-pr` at 847 installs and `n8n:create-pr` at 284 are the same 12,653-byte file. Two listings, `n8n-conventions` and `n8n:design-system`, have no matching directory in the tree sample at all, and this guide describes them only from their names.

## Installation

The repository README is the product README, not a skills document: it covers Docker self-hosting, the editor at port 5678 and the licence model, and says nothing about installing skills. The install commands come from the skills.sh listing pages, which name one skill at a time:

```bash
npx skills add https://github.com/n8n-io/n8n --skill create-pr
```

That flag is how every listing installs, so swap the skill name for whichever procedure you want:

```bash
npx skills add https://github.com/n8n-io/n8n --skill reproduce-bug
npx skills add https://github.com/n8n-io/n8n --skill n8n:protect-endpoints
```

The index mixes both naming forms: the observed listing commands include `--skill create-pr` and `--skill n8n:content-design`, so a slug may carry the namespace even though the directory does not. Use the string shown on the listing page you are working from rather than assuming the bare name will resolve.

The `--skill` flag is the reason to use the CLI here rather than a clone: the repository carries 33,401 blobs, and a PR-title template is not worth that checkout. If you already work in the n8n repository, the skills are on disk at `.agents/skills/` and need no install.

## What It Provides

The threshold for this guide is zero installs, so every indexed listing appears below:

| Skill | Installs | Use For |
|---|---|---|
| create-pr | 847 | Creates GitHub pull requests with titles that pass the check-pr-title CI validation, in type(scope): summary form. |
| content-design | 473 | Writes and reviews user-facing copy: button labels, error messages, tooltips, empty states, modal text and i18n strings. |
| n8n-conventions | 433 | Listed under a hyphenated slug with no matching directory in the tree sample, so its content could not be verified; the name points at the repository conventions reference. |
| n8n:conventions | 336 | Quick reference for n8n patterns, pointing at the repository AGENTS.md for the full documentation. |
| reproduce-bug | 306 | Reproduces a bug from a Linear ticket as a failing test, taking the ticket title, description and comments as input. |
| linear-issue | 305 | Fetches a Linear issue with its related context for starting work on a ticket. |
| loom-transcript | 301 | Fetches and displays the full transcript of a Loom video from its URL. |
| n8n:spec-driven-development | 288 | Keeps implementation and specs in sync, checking code against a spec in .agents/specs/ and updating it after changes. |
| n8n:content-design | 287 | Same content design skill as the 473-install listing, indexed a second time under its frontmatter name. |
| n8n:create-pr | 284 | Same pull request skill as the 847-install listing, indexed a second time under its frontmatter name. |
| n8n:create-skill | 271 | Guides authoring a new agent skill: structure, best practices and SKILL.md format. |
| n8n:setup-mcps | 254 | Configures MCP servers for n8n development in OpenCode. |
| n8n:loom-transcript | 253 | Same Loom transcript skill as the 301-install listing, indexed a second time under its frontmatter name. |
| n8n:protect-endpoints | 250 | Applies RBAC scope decorators to REST endpoints so every authenticated route is gated by ProjectScope or GlobalScope. |
| n8n:reproduce-bug | 248 | Same bug reproduction skill as the 306-install listing, indexed a second time under its frontmatter name. |
| n8n:node-add-oauth | 248 | Adds OAuth2 credential support to an n8n node: credential file, node updates, tests and the CLI constant. |
| n8n:create-issue | 247 | Creates Linear tickets or GitHub issues following n8n conventions. |
| n8n:create-community-node-lint-rule | 244 | Creates ESLint rules for the @n8n/eslint-plugin-community-nodes package, with tests, docs and plugin registration. |
| n8n:linear-issue | 244 | Same Linear issue skill as the 305-install listing, indexed a second time under its frontmatter name. |
| n8n:design-system | 217 | Listed with no matching directory in the tree sample, so its content could not be verified; the name points at the repository design system skill. |

All 20 indexed listings clear the zero-install threshold, and none fall outside the table. Five of the rows are byte-identical second entries for a directory listed above them, so the install counts look paired rather than sequential.

The install distribution tells you what people actually want from this repository. `create-pr` at 847 is nearly double the next listing, and the PR title convention is the most mechanical thing in the collection: a `type(scope): summary` line where the type must be one of nine values and the scope must be one of seven, or CI rejects the pull request. Behind it sit the two other workflow skills with real pull, bug reproduction from a Linear ticket and UI copy review, and then a long tail of endpoint security, OAuth credential wiring, lint rules and spec synchronisation.

The two master-style conventions matter more than their install counts suggest. `n8n:conventions` points at `AGENTS.md` for the full documentation, which means the skill is a pointer rather than a body, and `n8n:spec-driven-development` is the piece that keeps an implementation honest against a spec in `.agents/specs/`. Those two are how a large monorepo keeps agent-written code consistent with its own house rules.

## Why This Matters for Hermes Agents

Most agent skills document a third-party API. This set documents one team's internal conventions, which is a different and harder problem: the conventions are unwritten in public, enforced by CI, and invisible to a model that has only seen the repository's code. An agent asked to open a pull request against n8n without these skills will write a reasonable title, watch the `check-pr-title` job fail, and then guess at the scope values.

The specific rules are the valuable part. Types are `feat`, `fix`, `perf`, `test`, `docs`, `refactor`, `build`, `ci` and `chore`; scopes are `API`, `ai-builder`, `benchmark`, `core`, `editor`, `engine`, or a node name; two scopes are comma-separated; a package or folder name is explicitly not a valid scope. That last exclusion is exactly the mistake a model makes when it infers a scope from a directory name.

The engineering skills with review value travel better than the n8n-specific ones. `n8n:protect-endpoints` encodes a real security invariant, that every authenticated endpoint must be gated by `@ProjectScope` or `@GlobalScope`, and its trigger covers any new route rather than only a review. `n8n:node-add-oauth` and `n8n:create-community-node-lint-rule` are similarly complete procedures: files to create, tests to add, registrations to update.

The caveat is portability. These skills assume n8n's toolchain: a Linear workspace, the `gh` CLI, the `check-pr-title` job, `.agents/specs/` and its own node structure. Outside that repository they are a good template and a poor drop-in.

## Usage

| You say | What happens |
|---|---|
| "Open a PR for this branch" | Create PR writes a title in `type(scope): summary` form using an allowed type and scope, then opens the pull request so the title check accepts it |
| "Reproduce this Linear ticket as a test" | Bug reproduction takes the ticket title, description and comments and builds a failing test that captures the reported behavior |
| "What is ENG-1423 about?" | Linear issue fetches the ticket with its comments and related context, so the work starts from the full thread rather than the title |
| "Review this controller for authorization gaps" | Protect endpoints checks every route for a `@ProjectScope` or `@GlobalScope` decorator and flags authenticated endpoints that lack one |
| "Add OAuth2 support to this node" | Node add OAuth creates the credential file, updates the node, adds tests and keeps the CLI constant in sync |
| "Rewrite these error messages and empty states" | Content design reviews or writes the copy for labels, errors, tooltips, empty states, modals and i18n strings |
| "Does this implementation match the spec?" | Spec-driven development compares the code against the spec in `.agents/specs/` and reports or updates the drift |

## Verification

Each listing resolves to a raw `SKILL.md` under `.agents/skills/`, one directory per skill. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/n8n-io/n8n/master/.agents/skills/create-pr/SKILL.md | head -6
```

It should open with frontmatter holding `name: n8n:create-pr`, an `allowed-tools` line granting `Bash(git:*)`, `Bash(gh:*)`, Read, Grep and Glob, and below the delimiter a `# Create Pull Request` heading followed by the title format table. The namespaced `name` is the detail to check: it is why the index carries the same skill under two strings.

After an install, confirm the skill landed as a directory holding `SKILL.md`:

```bash
ls -d ~/.claude/skills/*/ | head -20
test -f ~/.claude/skills/create-pr/SKILL.md && echo ok
```

Then confirm the behavior that matters, which is the title format. Ask for a PR title on a branch that changes one node, and check that it comes back with an allowed type and an allowed scope rather than a package name.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| create-pr | Pass | Pass | Pass |
| content-design | Pass | Pass | Pass |
| n8n-conventions | Pass | Warn | Pass |
| n8n:conventions | None | None | None |
| reproduce-bug | Pass | Pass | Pass |
| linear-issue | Fail | Warn | Warn |
| loom-transcript | Warn | Pass | Warn |
| n8n:spec-driven-development | None | None | None |
| n8n:content-design | None | None | None |
| n8n:create-pr | None | None | None |
| n8n:create-skill | None | None | None |
| n8n:setup-mcps | None | None | None |
| n8n:loom-transcript | None | None | None |
| n8n:protect-endpoints | None | None | None |
| n8n:reproduce-bug | None | None | None |
| n8n:node-add-oauth | None | None | None |
| n8n:create-issue | None | None | None |
| n8n:create-community-node-lint-rule | None | None | None |
| n8n:linear-issue | None | None | None |
| n8n:design-system | None | None | None |

Only 6 of the 20 listings carry scanner verdicts; the other 14 show `None` on all three scanners, which is an absence of data rather than a pass. Of the six that were scanned, `linear-issue` fails Agent Trust Hub and warns on Socket and Snyk, `loom-transcript` warns on Agent Trust Hub and Snyk, and `n8n-conventions` warns on Socket. `create-pr` and `content-design` pass all three.

The verdicts understate the actual surface, because these skills grant shell access. `create-pr` declares `allowed-tools` covering `Bash(git:*)` and `Bash(gh:*)`, and its procedure ends with a real pull request against a real remote. `linear-issue` reads a ticket with whatever credentials the session holds. `reproduce-bug` writes a test into your tree. None of that is malicious and all of it is privileged: an agent following these skills operates with your git identity, your `gh` token and your Linear access.

Treat two properties as load-bearing. First, only run the PR and issue skills against a repository where an agent-authored PR is acceptable, because a title that passes CI is still a merged commit if a human does not look. Second, keep the Linear and gh tokens scoped to one workspace and one repository. None of these skills needs a broad token, and a wider one only extends what a prompt injection in a ticket body can reach.

## Limitations

- Snapshot data, verified 2026-11-09: 6,336 combined installs across 20 indexed listings; 209,960 GitHub stars; NOASSERTION license; last pushed 2026-11-10. Counts drift over time.
- GitHub reports the licence as NOASSERTION while the README names the Sustainable Use License plus the n8n Enterprise License and describes the project as fair-code. Read that as source-available with usage conditions, not as a permissive OSI licence, and check the Sustainable Use terms before redistributing anything built on these files.
- The pack date and the push date disagree by a day: the snapshot is dated 2026-11-09 and the repository's last push is 2026-11-10T04:58:24Z, which is a UTC rollover rather than a real ordering problem.
- The skills.sh source page renders at most 20 listings against the publisher's 59, and the tree carries 40 `SKILL.md` files. Five rows are byte-identical duplicates of a directory listed above them, indexed once by directory name and once by namespaced `name`, so the 20 listings resolve to 15 distinct entries: 13 with a file in the tree and 2 without one.
- `n8n-conventions` and `n8n:design-system` have no matching directory in the tree sample, so their content is unverified here. Their rows are name-level descriptions only.
- These skills encode n8n's own toolchain: Linear tickets, the `gh` CLI, `check-pr-title` CI, `.agents/specs/` and the node package layout. Ported to another repository, the procedures need rewriting rather than configuring.
- 14 of the 20 listings have no scanner verdict at all. The tier note reflects the six listings that were scanned and their majority verdict, not a full audit of the set.

## Related

- [n8n Skills - Workflow Automation for Business](/hermes/skills/catalog/n8n-skills-setup)
- [Alan Skills - Plan, Test and Review PRs](/hermes/skills/catalog/alan-skills-setup)
- [Awesome Copilot - MCP Server Generators & GitHub Automation Setup](/hermes/skills/catalog/awesome-copilot-setup)

## Pro Tips

- Quote any skill name that contains a colon. Both forms appear in the listing pages' own install commands, so copy the exact string from the page you are on, and prefer the directory form (`--skill content-design`) when you are writing a script.
- Read the title table before the first PR. Nine types and seven scopes is small enough to keep in the prompt, and it turns a CI failure into a passing first attempt.
- Use `n8n:protect-endpoints` as a review gate rather than a generator. Asking it to check an existing controller for missing `@ProjectScope` decorators finds real gaps; asking it to add decorators everywhere produces noise.
- Pair bug reproduction with the Linear issue skill in one session. One reads the ticket, the other writes the failing test, and doing both in sequence is what keeps the test aligned with the reported behavior.
- Do not install the whole set into an unrelated repository. Take `create-pr`, `content-design` and the review skills, and leave the n8n node and RBAC skills where they belong.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
