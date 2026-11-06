---
title: "Claude Code Java - Spring and JVM Review Suite"
description: "decebals/claude-code-java on skills.sh: 6.5K combined installs across 18 listings; Java review, Spring, JPA and Maven skills with routed evals."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-code-java-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "java", "spring boot", "code review"]
---

# Claude Code Java - Setup Guide

**Source:** [decebals/claude-code-java](https://www.skills.sh/decebals/claude-code-java) via skills.sh - 6.5K combined installs across 18 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 770 stars, MIT licence, last pushed 2026-10-30, skills/<name>/SKILL.md layout with 18 skill directories, a plugin.json manifest and setup scripts
**Category:** Java for agents: Spring Boot patterns, JPA, concurrency and Solid reviews, Maven audits and version migration
**Quality Tier:** 🟡 Caution - Snyk Warned on issue-triage, one of five sampled skills; the other four passed all three audits; MIT; 770 stars.

Eighteen skills for Java work, grouped by the task they interrupt: workflow (commit messages, changelogs, issue triage), code quality (review, API contracts, concurrency, performance smells, test quality, Maven dependency audit, security audit), architecture and design (package structure, SOLID, design patterns, clean code), and framework and data (Spring Boot, JPA, logging, version migration). Every skill follows the open Agent Skills specification, and CI validates each one against it.

Two things separate this pack from a folder of prompts. The first is that routing is measured. The README describes `scripts/eval-routing.sh`, which asks a model to pick a skill from nothing but the name, description and path, the same surface an agent sees. On its first run it caught a real defect: "this class does too much, split it" landed on `clean-code` instead of `solid-principles`. Sharpening three descriptions moved the set from 17 of 18 prompts routed correctly to 20 of 20.

The second is that the same skill files drive review. The author runs a reusable GitHub Actions workflow, `skill-review`, that evaluates pull requests against the same skills an agent uses while generating code. One source of truth for both directions removes the usual gap where the generator and the reviewer disagree about what good looks like.

## Installation

The quickest route is the `skills` CLI, which installs into the current project by default:

```bash
npx skills@latest add decebals/claude-code-java
```

Add `--list` to see the skills before installing, `--skill <name>` to take only some, `--global` for a user-level install, or `--copy` to get files instead of symlinks.

For the skills plus a generated `CLAUDE.md`, MCP configuration and project settings, clone the workspace and run its setup script against a project path:

```bash
git clone https://github.com/decebals/claude-code-java.git ~/projects/claude-code-java
cd ~/projects/claude-code-java
chmod +x scripts/*.sh
./scripts/setup-project.sh ~/projects/your-java-project
```

The script creates `.claude/` in the target project with symlinked skills, generates `CLAUDE.md`, and configures settings. The manual equivalent is a symlink of the skills directory:

```bash
mkdir -p your-project/.claude/skills
ln -s ~/projects/claude-code-java/skills/* your-project/.claude/skills/
```

Installing the whole pack at once puts eighteen competing descriptions in front of the router. The requirements are an agent that reads Agent Skills, Java 11 or newer (17 recommended), Git, and Maven or Gradle.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| java-code-review | 1,092 | Systematic review of Java changes: null safety, exception handling, concurrency and performance checks, run before a merge |

One listing clears the 500-install threshold on its own. The remaining 17 indexed listings range from 230 to 407 installs: clean-code (407), concurrency-review (371), solid-principles (369), architecture-review (359), design-patterns (358), spring-boot-patterns and java-migration (345 each), security-audit (330), performance-smell-detection (329), test-quality (314), api-contract-review (301), maven-dependency-audit (295), logging-patterns (288), jpa-patterns (282), changelog-generator (241), git-commit (239) and issue-triage (230).

## Why This Matters for Hermes Agents

An agent reviewing Java without a checklist produces comments about naming and ignores the failure modes that actually ship: a `@Transactional` method calling a sibling method on the same bean so the proxy never applies, a stream collected inside a loop, a `HashMap` shared across threads, an N+1 query hidden behind a lazy association. The pack's skills target exactly those categories, with review checklists that name the pattern to look for instead of leaving the agent to invent criteria.

The JPA and concurrency skills are where this pays best. `jpa-patterns` lists the N+1 problem and `LazyInitializationException` among its triggers; `concurrency-review` covers thread safety, race conditions, virtual threads, `CompletableFuture` and `@Async`. Those are precisely the areas where a model's training distribution favors plausible code over correct code.

The routing work is the part other skill authors should copy. Eighteen descriptions compete for every prompt, and the failure is silent: the wrong skill loads and answers plausibly. Measuring the routing decision, then fixing the descriptions that lost, is a repeatable way to keep a growing skill library from degrading as it grows.

It also gives you a review loop you can automate. The `skill-review` workflow applies the same skill set to pull requests, so the standards an agent generates against are the standards a reviewer enforces, and a disagreement becomes a skill defect rather than a style argument.

## Usage

| You say | What happens |
|---|---|
| "/java-code-review review this diff" | Runs the review checklist over the change and reports null safety, exception, concurrency and performance findings |
| "This class does too much, split it" | Routes to solid-principles after the description fix, and proposes the responsibility split |
| "Check thread safety in this service" | concurrency-review inspects shared state, `@Async` proxying and virtual thread usage |
| "Why am I getting LazyInitializationException?" | jpa-patterns diagnoses the fetch strategy and the transaction boundary that broke it |
| "Audit the Maven dependencies" | maven-dependency-audit reports version conflicts, unused declarations and upgrade candidates |
| "Review this REST endpoint before release" | api-contract-review checks HTTP semantics, versioning and backward compatibility |
| "Write the commit for this change" | git-commit produces a Conventional Commit message from the diff |

## Verification

List the pack before installing, which the README documents as a supported flag:

```bash
npx skills@latest add decebals/claude-code-java --list
```

Then read the skill that will be loaded most. Raw paths are `skills/<name>/SKILL.md` on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/decebals/claude-code-java/main/skills/java-code-review/SKILL.md | head -4
```

It should open with `name: java-code-review` and a description naming null safety, exception handling, concurrency and performance. Finally confirm the count landed:

```bash
ls .claude/skills | wc -l
```

In a project that held no skills before, that should print 18. A lower number means a partial install or a route that took only the files you named.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| java-code-review | Pass | Pass | Pass |
| architecture-review | Pass | Pass | Pass |
| performance-smell-detection | Pass | Pass | Pass |
| logging-patterns | Pass | Pass | Pass |
| issue-triage | Pass | Pass | Warn |

One sampled skill carries a Snyk warning, which is why this guide is tiered Caution. The warning is on `issue-triage`, the skill that reads and categorizes GitHub issues, so treat the network-facing workflow with more care than the review skills that only read local code. Read the finding on the skills.sh security page before giving that skill a token.

The review skills themselves are markdown checklists with accompanying `README.md` files, and nothing in them executes. The repository does ship shell scripts: the setup scripts symlink files into your project and rewrite settings, and the eval script calls a model endpoint. Read `scripts/setup-project.sh` before running it against a repository you care about, since it writes into `.claude/` and generates `CLAUDE.md`.

## Limitations

- Snapshot data, verified 2026-11-05: 6,495 combined installs across 18 indexed listings; 770 GitHub stars; MIT; last pushed 2026-10-30. Counts drift over time.
- One listing clears 500 installs and the other seventeen sit between 230 and 407. A table of the top listing alone understates the pack, so the tail is named in full above.
- The setup scripts are bash and assume a POSIX host with `chmod`. Windows users get the `npx` route or a manual copy.
- Routing was measured against specific model endpoints. The README notes the harness accepts any OpenAI-compatible endpoint, which is exactly why the 20 of 20 result should be re-run against the model you actually deploy.
- The skills assume Java 11 or newer, with 17 recommended, and a Maven or Gradle build. Advice aimed at newer language features will not apply to a legacy codebase.
- `issue-triage` carries the only Snyk warning in the sample and depends on GitHub issue access, which is a wider permission surface than the rest of the pack.

## Related

- [Java Development Plugin - 12-Skill Java Engineering Setup](/hermes/skills/catalog/custom-plugin-java-setup)
- [Kotlin Agent Skills - JetBrains JVM Guidance](/hermes/skills/catalog/kotlin-agent-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)

## Pro Tips

- Run `--list` first, then `--skill java-code-review --skill concurrency-review` for a narrow install. Two strong skills loaded often beat eighteen loaded once.
- Use `--copy` when you want to edit a skill. Symlinks keep the workspace as the source of truth, which is right for tracking upstream and wrong for local tailoring.
- Point the routing harness at your own model. `scripts/eval-routing.sh` reads `EVAL_BASE_URL` and `EVAL_MODEL`, so the 20 of 20 routing result can be verified on your endpoint rather than assumed.
- Start reviews with the diff in the prompt. The review skill inspects what it is given, and a whole-repository request produces broad advice instead of findings.
- Wire `skill-review` into the same repository you generate code in. The value is that generation and review share one skill set, which only holds if both run from the same revision.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
