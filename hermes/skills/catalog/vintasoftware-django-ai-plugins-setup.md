---
title: "Vinta Django AI Plugins - Django and Celery Setup"
description: "vintasoftware/django-ai-plugins: 8.4K combined installs. Vinta's portable Django, DRF and Celery agent skills for backend, migration and review work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vintasoftware-django-ai-plugins-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "django", "celery", "python", "backend"]
---

# Vinta Django AI Plugins - Setup Guide

**Source:** [vintasoftware/django-ai-plugins](https://www.skills.sh/vintasoftware/django-ai-plugins) via skills.sh - 8.4K combined installs across 5 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [vintasoftware/django-ai-plugins](https://github.com/vintasoftware/django-ai-plugins) - 166 stars, no LICENSE file in the repository (the README License section states MIT, Vinta Software), branch main, last pushed 2026-07-23 (b8af268); 10 `SKILL.md` files across 5 skill IDs, canonical at `skills/<id>/SKILL.md` with generated package projections at `plugins/<id>/skills/<id>/SKILL.md`, beside `plugins/catalog.json`, `.claude-plugin/`, `.agents/plugins/`, `.cursor-plugin/`, `.opencode/plugins/`, `docs/`, `scripts/` and `tests/`

**Category:** Django, Celery and Python backend engineering guidance

**Quality Tier:** 🟡 Beta - 1 sampled Warn verdict(s); no repository-level license file - five portable skills covering Django backend work, Celery task design, DRF class hierarchies, zero-downtime migrations and report-first review

Vinta Software publishes this repository as a portable Django skills collection for Claude Code, Codex, Cursor, OpenCode and any host that implements the Agent Skills specification. It carries five skills rather than a broad library: `django-expert` for backend, ORM, DRF, security, testing and performance work, `django-celery-expert` for task design, retries and scheduling, `cdrf-expert` for DRF class-based view selection and method resolution order, `django-safe-migration` for PostgreSQL-aware zero-downtime migrations, and `django-reviewer` for report-first review of recent changes. The README describes the five as complementary and points at `docs/installation.md` and `docs/compatibility.md` for host-by-host lifecycle and validation levels.

What makes the repository notable is its packaging discipline. There is one canonical authoring tree under `skills/`, and every host manifest plus every package-local skill copy is generated from `plugins/catalog.json`, so the same behaviour reaches Claude, Codex, Cursor, OpenCode and generic Agent Skills consumers without five hand-maintained copies. The README also positions the skills as a complement to Vinta's `django-ai-boost` MCP server, with the explicit note that neither project requires the other.

## Installation

The README routes installers to `docs/installation.md`, which lists the `skills` CLI as the recommended portable installer for hosts that support Agent Skills. Listing is the only call that touches nothing:

```bash
npx skills add vintasoftware/django-ai-plugins --list
```

Install one skill, or target specific hosts:

```bash
npx skills add vintasoftware/django-ai-plugins --skill django-expert
npx skills add vintasoftware/django-ai-plugins --skill django-expert --agent codex --agent cursor
```

The Claude Code route uses the plugin marketplace declared in `.claude-plugin/marketplace.json`:

```text
/plugin marketplace add vintasoftware/django-ai-plugins
/plugin install django-expert@django-ai-plugins
```

Hermes is not one of the generated adapters, so the durable route for this profile is a directory copy of the canonical skill, which is the same manual path the installation doc documents for `~/.agents/skills/`:

```bash
cp -R skills/django-expert ~/.hermes/profiles/corpusiq/skills/django-expert
```

Copy the whole directory, not the markdown alone. Four of the five skills ship a `references/` folder next to `SKILL.md` with the detail those skills cite while working, and `django-reviewer` is the one that is self-contained. The installation doc is emphatic about one channel per skill ID: installing the same ID through the skills CLI and a native marketplace at once can register the skill twice, and the fix is to remove the shadow copy rather than the working one.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| django-expert | 5,773 | Django backend work: models, views, serializers, ORM query debugging, migrations, authentication, testing and DRF, following Django best practices and modern Python conventions. |
| django-celery-expert | 1,143 | Celery task design: background task structure, worker configuration, retries and error handling, performance tuning, Celery Beat periodic tasks and production monitoring. |
| django-safe-migration | 786 | PostgreSQL zero-downtime migrations: SeparateDatabaseAndState splits, AddIndexConcurrently, FK NOT VALID plus VALIDATE, db_default for NOT NULL columns, lock_timeout and RunPython safety rules. |
| cdrf-expert | 524 | DRF class-based view decisions: APIView versus GenericAPIView versus concrete generics, mixin combinations, ViewSet behaviour, MRO tracing and which method to override, built on the Classy DRF reference. |

The remaining 1 indexed listings range from 164 to 164 installs.

## Why This Matters for Hermes Agents

Most of what goes wrong in agent-written Django is not syntax, it is blast radius: a migration that locks a table in production, a Celery task that retries into a duplicate charge, a DRF override placed on the wrong method so the hook silently never runs. These skills are written against those failure modes rather than against the tutorial path, and `django-safe-migration` is the clearest example, since its whole trigger list is phrased around "will this migration cause locks" and "this migration is blocking production".

The suite also carries a real authorization model. `django-reviewer` states a boundary in its own instructions: it reports findings by default and only applies refinements when the user expresses explicit edit intent or the host has already authorized edits. That is the shape a review skill should have in an agent loop, because it means a scheduled job can review a diff without touching it, and a human can escalate to edits deliberately.

Each skill description is a routing contract with an explicit negative list. `cdrf-expert` says it is not for function-based views, GraphQL, FastAPI or Flask, and `django-celery-expert` says it is not for Django Q, Huey, RQ, Airflow or Prefect. Descriptions that name what they will not handle are what keep a five-skill Django install from shadowing a broader backend skill in the same profile, and they matter more in Hermes, where routing is decided from the description alone.

Finally, the packaging works for a profile that has no plugin manager. Because `skills/<id>/SKILL.md` is canonical and every adapter tree is generated from `plugins/catalog.json`, a plain directory copy into the Hermes skills tree is not a fork of the project, it is the same source the marketplaces ship. That is the cheapest reliable way to test these skills inside an existing Hermes workflow before deciding whether a marketplace install is worth it.

## Usage

| You say | What happens |
|---|---|
| "Review this Django model before I merge" | `django-expert` checks field choices, related names, indexes, null and blank semantics and manager usage, and proposes the change in terms of Django conventions rather than generic Python style. |
| "Why is this queryset doing 400 queries?" | `django-expert` walks the ORM access pattern, identifies the missing `select_related` or `prefetch_related` at the point the loop reads a related object, and warns when the fix would change result ordering. |
| "Is this migration safe to deploy?" | `django-safe-migration` classifies the operation, applies the PostgreSQL lock rules, splits the change with SeparateDatabaseAndState when needed, and rewrites the migration with AddIndexConcurrently or a NOT VALID foreign key where the original would block writes. |
| "This Celery task duplicates charges on retry" | `django-celery-expert` reviews idempotency, `acks_late` and retry policy, task time limits and the boundary between the task and the transaction, then states where the duplicate is created. |
| "Should this be a ModelViewSet or separate APIViews?" | `cdrf-expert` traces the lifecycle for the operations involved, shows the MRO that would apply, and recommends an override point such as `perform_create` instead of `create` so the serializer and permission hooks keep working. |
| "Review the last commit" | `django-reviewer` produces a report-first review of the changed Django and Python code, ordered by severity, and leaves the files untouched unless edit intent was stated. |
| "Add a NOT NULL column to a 40 million row table" | `django-safe-migration` produces the two-step plan: add with `db_default`, backfill outside the migration, then drop the default, with `lock_timeout` set so the deploy fails rather than queues behind the lock. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} expert\n" \
  https://raw.githubusercontent.com/vintasoftware/django-ai-plugins/main/skills/django-expert/SKILL.md
curl -sL -o /dev/null -w "%{http_code} safe-migration\n" \
  https://raw.githubusercontent.com/vintasoftware/django-ai-plugins/main/skills/django-safe-migration/SKILL.md
```

Expect `200` twice. Read one before installing, because the description is the whole routing contract: a good Django skill description names the triggers, the artefacts it works on and the frameworks it refuses.

After a copy lands in the profile, confirm the frontmatter and the shipped references:

```bash
head -4 ~/.hermes/profiles/corpusiq/skills/django-expert/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/django-expert/
```

A good copy shows `name:`, a `description:` line and the closing `---` of the frontmatter, and the directory listing shows `SKILL.md` plus `references/`. `django-reviewer` is the exception and ships `SKILL.md` alone. In the repository itself, `python scripts/generate_adapters.py --check`, `python scripts/validate_plugins.py` and `python -m unittest discover -s tests -p 'test_*.py'` are the maintenance gates the README documents.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| django-expert | Pass | Pass | Pass |
| django-celery-expert | Pass | Warn | Pass |
| django-safe-migration | Pass | Pass | Pass |
| cdrf-expert | Pass | Pass | Pass |
| django-reviewer | Pass | Pass | Pass |

No FAIL verdict appears in the sample. The single Warn is Socket's on `django-celery-expert`, and the pack records the verdict rather than the finding, so read that entry on skills.sh before installing it. The repository also ships no LICENSE file: the GitHub license field is empty and there is no LICENSE or COPYING file in the checkout, so the only license statement is the README's "MIT" line and the `license: MIT` default in `plugins/catalog.json`. Treat redistribution rights as unconfirmed until the maintainers add a license file.

The content risk here is low in kind. These are instruction-only skills: no bundled scripts, no network calls, no credentials, and nothing that executes on install. The thing worth reading before you trust them is what they tell the agent to do to your database, because `django-safe-migration` and `django-reviewer` both produce changes that a human may then apply to a production project.

## Limitations

- Snapshot data, verified 2026-10-30: 8,390 combined installs across 5 indexed listings; 166 GitHub stars; no repository-level license file; last pushed 2026-07-23. Counts drift over time.
- There is no LICENSE file, and the license metadata disagrees with itself: the GitHub API reports none, the checkout carries no LICENSE or COPYING file, while the README License section says MIT and `plugins/catalog.json` sets `"license": "MIT"`. Confirm terms with the maintainers before redistributing the skills inside another product.
- The tree holds twice as many `SKILL.md` files as skills. Five canonical files sit under `skills/<id>/`, and five generated copies sit under `plugins/<id>/`. Edits belong in `skills/` or `plugins/catalog.json`; a package copy is a build artefact, so a fix applied there is lost at the next generation run.
- The generated layout is not uniform. Four plugins expose `plugins/<id>/skills/<id>/SKILL.md`, while `django-reviewer` exposes `plugins/django-reviewer/portable-skills/django-reviewer/SKILL.md` and also carries an `agents/` directory. Scripts that glob for a single pattern across `plugins/` will miss it.
- The installation doc documents a flat 1.0 path (`plugins/<id>/skills/SKILL.md`) that earlier checkouts used. Both the old and the new path can be discovered by a host, which registers the same skill ID twice; remove the stale directory rather than keeping both.
- Everything here is guidance, not a service. No skill calls a live API or needs a credential, and none of them can inspect your running database or Celery cluster, so answers about locks, query plans and queue depth are only as good as the code and exports you hand the agent.

## Related

- [prisma Skills](/hermes/skills/catalog/prisma)
- [OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup)
- [Callstack Agent Skills - React Native Skill Suite Setup](/hermes/skills/catalog/callstackincubator-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `django-expert` first and use it for a week before adding the rest. It is the broad entry point, and a profile that holds all five from day one routes Django questions through four descriptions that all sound plausible.
- Pair `django-safe-migration` with a real migration file, not a description of one. The skill works by classifying each operation and rewriting the risky ones, and it has nothing to classify if you only paste an intention.
- Keep `django-reviewer` read-only in any cron. Its instructions already default to report-only, and leaving the edit path for an interactive session preserves the review trail that makes it useful.
- Read the `references/` folder once per skill. Four of the five ship one, and the framework detail the agent cites at runtime lives there rather than in the top-level markdown.
- Do not mix install channels for the same skill ID. Pick the skills CLI or the marketplace for each host, and delete the shadow copy if both have already run, because duplicate IDs show up as flaky routing rather than as an error.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
