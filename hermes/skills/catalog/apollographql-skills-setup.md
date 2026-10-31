---
title: "Apollo GraphQL Skills - GraphQL and Rust Setup"
description: "apollographql/skills: 56.6K combined installs. Fifteen agent skills for Apollo Client, Server, Router, federation, Rover and idiomatic Rust."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/apollographql-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "graphql", "apollo", "rust"]
---

# Apollo GraphQL Skills - Setup Guide

**Source:** [apollographql/skills](https://www.skills.sh/apollographql/skills) via skills.sh - 56.6K combined installs across 15 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [apollographql/skills](https://github.com/apollographql/skills) - 123 stars, MIT, branch main, last pushed 2026-10-30; 15 `SKILL.md` files, one per directory under `skills/`, most with a `references/` folder of deeper documentation beside them and a few carrying `scripts/` or `templates/`

**Category:** GraphQL schema and client work plus Apollo platform tooling for coding agents

**Quality Tier:** 🟢 Green - all five sampled skills Pass on all three auditors, and the repository is MIT-licensed markdown with only a handful of shell scripts

Apollo GraphQL maintains this repository as the first-party skill set for its own stack. The fifteen skills split along the platform: three client libraries (Apollo Client for React, Apollo iOS for Swift, Apollo Kotlin for Android and KMP), the server and router tiers (Apollo Server 5.x, Apollo Router configuration, and native Rust router plugins), the federation and schema layer (subgraph schemas with Federation 2.x directives, SDL design, operation authoring), the tooling that ties them together (Rover CLI, Apollo Connectors and its successor graphos-factory, Apollo MCP Server), and two meta skills for authoring new Apollo skills.

The oddity worth knowing is the top of the install table: rust-best-practices, at 21,981 of the 56,575 combined installs, is a general Rust style guide that happens to live in this Apollo GraphQL repository, which makes the suite GraphQL plus a Rust style guide rather than GraphQL alone. It fits the neighbourhood, since the router plugin skill teaches native Rust plugins, but it is not a GraphQL skill, and a team adopting this suite for schema work gets a Rust handbook in the same install. The rest of the table is coherent: every remaining skill maps to a named Apollo product, and each one ships reference documents that go well past the summary in its description.

## Installation

The README's primary route is the skills CLI, which walks through an interactive picker:

```bash
npx skills add apollographql/skills
```

The picker asks four questions: which skills to install, which agents to target (Claude Code, Codex, Cursor, Gemini CLI, Goose, OpenCode), whether the install is project-scoped and committed with the code or global, and whether to symlink or copy. Any single skill can be pulled on its own:

```bash
npx skills add apollographql/skills@rover
npx skills add apollographql/skills@graphos-factory
```

The same repository is also a Claude Code plugin marketplace, where the skills appear as namespaced slash commands:

```bash
/plugin marketplace add apollographql/skills
/plugin install apollo-skills@apollo-marketplace
```

And the GitHub CLI carries a preview `gh skill` installer with release pinning, which matters because the other routes track `main` HEAD:

```bash
gh skill install apollographql/skills --agent claude-code
gh skill install apollographql/skills --agent claude-code --scope user
gh skill install apollographql/skills --pin v1.0.0 --agent claude-code
gh skill preview apollographql/skills
```

None of those routes knows about Hermes, so the durable install for this profile is a directory copy. The clone holds 15 skill directories, and each one is a complete unit of `SKILL.md` plus whatever `references/`, `scripts/` or `templates/` sit beside it, so copy the directories rather than the files:

```bash
git clone --depth 1 https://github.com/apollographql/skills.git /tmp/apollo-skills
cp -r /tmp/apollo-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

That copies all 15. To take a subset, name the directories explicitly, for example `apollo-client`, `graphql-schema`, `graphql-operations`, `rover` and `apollo-federation`, which is the core loop for schema-first GraphQL work.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| rust-best-practices | 21,981 | Writing or reviewing idiomatic Rust against Apollo's best practices handbook: ownership and borrowing choices, Result-based error handling, performance work, tests and docs. |
| apollo-client | 5,640 | React applications on Apollo Client 4.x: client and provider setup, useQuery and useMutation with optimistic UI, InMemoryCache type policies, reactive variables, error links. |
| graphql-schema | 4,139 | Designing and editing GraphQL SDL: types, nullability, naming, pagination and error patterns, and security in schema design. |
| graphql-operations | 3,660 | Queries, mutations and fragments: organizing operations, type generation and linting setup, and reviewing operations for fetch efficiency. |
| apollo-mcp-server | 3,194 | Standing up Apollo MCP Server so agents can reach a GraphQL API: MCP tools from operations, introspection tools, auth, CORS, health checks, Rhai lifecycle hooks. |
| apollo-server | 2,969 | Apollo Server 5.x: schema definition, resolver patterns, context and authorization, plugins, DataLoader sources, error formatting. |
| rover | 2,311 | Rover CLI: publishing and fetching subgraph or graph schemas, local supergraph development, check and lint, schema describe and schema search for agent discovery. |
| apollo-connectors | 2,194 | Wiring a REST API into a supergraph with the @source and @connect directives. The skill itself is marked deprecated in favor of graphos-factory. |
| skill-creator | 1,968 | Authoring a new Apollo skill or updating an existing one: SKILL.md structure, frontmatter fields and house conventions. |
| apollo-federation | 1,962 | Federation 2.x subgraph schemas: entity keys, @shareable and the other directives, sharing fields across subgraphs, composition errors. |
| apollo-router | 1,853 | Apollo Router configuration with version-aware YAML for v1.x and v2.x: headers, CORS, plugins, telemetry, JWT and persisted-query safelisting. |
| apollo-kotlin | 1,747 | Apollo Kotlin on Android, Kotlin/JVM and Kotlin Multiplatform: Gradle setup, schema download and codegen, interceptors, normalized cache, subscriptions. |
| apollo-router-plugin-creator | 1,653 | Native Rust router plugins: the four service hooks across the request lifecycle, plus the patterns for adding to or modifying an existing plugin. |
| apollo-ios | 1,157 | Apollo iOS in Swift: SPM and codegen configuration, interceptors with token refresh and retry, subscriptions, cache keys, generated test mocks. |
| graphos-factory | 147 | Building a Connectors subgraph from a REST API in a dedicated git workspace that records the API surface, each design decision and the evidence every verification layer produced. |

No indexed listings fall below the threshold.

Every one of the 15 listings has a matching directory in the clone, so there is no index-versus-tree gap to work around here. The two entries worth reading before choosing are `apollo-connectors`, whose own description opens by marking it deprecated, and `graphos-factory`, which the README describes as a read-only copy of a release from a separate `apollographql/graphos-factory` repository.

## Why This Matters for Hermes Agents

GraphQL work fails in a specific way when an agent improvises: the schema compiles, the query validates, and the result is still wrong because the agent invented a naming convention, a pagination shape or a nullability choice that the rest of the graph does not share. Fifteen skills of Apollo house style attack that directly, and the two schema-facing skills, `graphql-schema` and `graphql-operations`, are the ones that stop an agent from freelancing on conventions.

Coverage matters more than depth for a general profile. The same suite answers a React caching question, an Apollo Server authorization question, a subgraph key question, a router YAML question and a Swift codegen question, in Apollo's own vocabulary, so an agent working across a stack does not have to be told which library it is looking at before it gets useful guidance.

The suite is cheap to carry. It is markdown, so installed tokens are spent only when a skill is actually routed to, and every skill keeps its deep material in `references/` files that the agent opens on demand. `apollo-router` alone ships 28 files, including versioned YAML templates, and `graphos-factory` ships 31, including its shell tooling; that structure is what keeps each `SKILL.md` short enough to stay routable.

The two meta skills are the unusual part of the offer. `skill-creator` documents the frontmatter and section conventions Apollo itself uses, and `apollo-router-plugin-creator` documents the plugin request lifecycle, so the suite can be extended in the same shape it was built in rather than around it.

`apollo-mcp-server` is the one that changes what an agent can reach rather than just what it knows. It teaches MCP tool definitions generated from GraphQL operations, which is how an agent moves from describing an API in prose to querying it through a typed tool surface.

## Usage

| You say | What happens |
|---|---|
| "Add a paginated reviews field to the schema" | The agent works from `graphql-schema`: connection-style pagination, nullability and naming conventions, plus the matching error pattern, before it writes any SDL. |
| "Our subgraph will not compose" | The agent switches to `apollo-federation` and walks composition errors against the directive set: `@key`, `@shareable`, `@external`, `@requires`, `@override`. |
| "Why does this query refetch every time the tab regains focus" | `apollo-client` takes over: cache policies, `fetchPolicy` and type policies on the InMemoryCache, then an error link if the request itself is failing. |
| "Point the router at the new supergraph with header propagation" | `apollo-router` produces version-correct YAML for the router generation in use, headers and CORS included, and warns where v1.x and v2.x diverge. |
| "Give our agent read access to the product graph" | `apollo-mcp-server` defines MCP tools from existing GraphQL operations, configures the endpoint and headers, then verifies with the introspection tools. |
| "This Rust plugin needs a new subgraph_service hook" | `apollo-router-plugin-creator` supplies the hook signature, the lifecycle position and an example, and `rust-best-practices` governs the code style around it. |
| "Wrap this REST API as a subgraph" | For a new build the agent should reach for `graphos-factory`, which records decisions and verification evidence in a workspace rather than editing files in place. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} rust-best-practices\n" \
  https://raw.githubusercontent.com/apollographql/skills/main/skills/rust-best-practices/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and the frontmatter:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/apollo-* \
      ~/.hermes/profiles/corpusiq/skills/graphql-* \
      ~/.hermes/profiles/corpusiq/skills/rover \
      ~/.hermes/profiles/corpusiq/skills/rust-best-practices \
      ~/.hermes/profiles/corpusiq/skills/skill-creator \
      ~/.hermes/profiles/corpusiq/skills/graphos-factory | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/graphql-schema/SKILL.md
```

The count should print 15, and the header should show `name: graphql-schema`, a multi-line `description:` written as a numbered trigger list, and `license: MIT`. Check that `references/` came along too, since `apollo-router`, `apollo-mcp-server` and `graphos-factory` lose most of their value without it:

```bash
find ~/.hermes/profiles/corpusiq/skills/apollo-router -type f -name "*.md" | wc -l
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rust-best-practices | Pass | Pass | Pass |
| apollo-client | Pass | Pass | Pass |
| graphql-schema | Pass | Pass | Pass |
| graphql-operations | Pass | Pass | Pass |
| graphos-factory | Pass | Pass | Pass |

All five sampled skills Pass all three auditors, and the sample spans the range of the suite rather than one corner of it: four listings first seen on skills.sh in late January 2026 and `graphos-factory`, the newest, first seen on 2026-10-07. No Fail and no Warn appears in the sample.

The fail surface in a suite like this is small by construction. Each skill is a markdown bundle with YAML frontmatter and reference documents; there is no package to install, no build step and no postinstall script, so the risk is what the instructions tell an agent to run rather than code that executes on install. The exceptions are visible in the tree: `apollo-ios` and `apollo-kotlin` each ship a version-listing script that runs `git ls-remote` against the upstream repository, and `graphos-factory` ships ten shell scripts whose `bootstrap.sh` downloads a prebuilt binary from GitHub Releases into `~/.cache/graphos-factory-core/`, pinning a version and refusing a stale binary with exit 78.

Credential handling is stated in the skills themselves, which is the useful part to check before deployment. The `rover` skill says never to commit `APOLLO_KEY` or `APOLLO_CLIENT_SECRET` and to authenticate with `rover config auth` or an environment variable instead, noting that Rover keeps the key in its own profile rather than in `$APOLLO_KEY`. The `graphos-factory` skill instructs the agent that the key is the user's and must never be asked for, set or printed, and `apollo-mcp-server` expands secrets through `${env.VAR}` references in its server configuration rather than writing literal values into the YAML. Treat those as instructions the agent may ignore, and keep the environment scoped on your side.

## Limitations

- Snapshot data, verified 2026-10-30: 56,575 combined installs across 15 indexed listings; 123 GitHub stars; MIT; last pushed 2026-10-30. Counts drift over time.
- The README's own counts lag the tree. The badge reads 11 skills and the interactive picker sample prints "Found 11 skills", while the checkout holds 15 skill directories and the slash-command table lists 12; `apollo-federation`, `apollo-router` and `apollo-router-plugin-creator` are missing from those lists. Trust the tree, not the summary.
- The install counts are not a ranking of the skills. rust-best-practices alone holds 21,981 of the 56,575 installs, and the bottom entry, graphos-factory, holds 147 while being the actively developed successor to apollo-connectors.
- One skill is deprecated in place. apollo-connectors still carries 2,194 installs and its description opens with the deprecation notice, pointing at graphos-factory for new work, so an install of the whole suite leaves a superseded skill on disk.
- graphos-factory is a copy, not the source. The README describes `skills/graphos-factory/` as a read-only copy of the latest release from `apollographql/graphos-factory`, updated by that repository's release workflow, so local edits there are overwritten on the next sync.
- Success depends on the agent routing correctly. Fifteen skills in one directory compete for attention, and the router and server skills overlap with the client and federation ones on questions like headers and auth; a mis-route produces confident guidance for the wrong tier.

## Related

- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)
- [Anthropic Claude API Skills - Official Claude API](/hermes/skills/catalog/anthropics-claude-api-skills-setup)
- [Composio - SDK Monorepo and Agent Toolkit Setup Guide](/hermes/skills/catalog/composiohq-composio-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the subset that matches the stack in front of you. `graphql-schema`, `graphql-operations`, `rover` and `apollo-federation` cover schema-first work, `apollo-router` and `apollo-router-plugin-creator` cover the gateway, and the three client skills are only worth carrying if you write React, Swift or Kotlin.
- Skip `apollo-connectors` on a fresh install and take `graphos-factory` instead, even though the deprecated skill has fifteen times the install count. The successor records decisions and verification evidence, which is the part that makes a generated subgraph reviewable.
- Read the `references/` files on demand rather than loading them up front. `apollo-router` carries 28 files including versioned YAML templates for v1 and v2, and pulling them all into context buys nothing until you are editing a `router.yaml` for a known version.
- Pin the release if the profile's output has to be reproducible. `gh skill install apollographql/skills --pin v1.0.0` is the only route that does not track `main` HEAD, and pinned skills are skipped by `gh skill upgrade`.
- Keep `APOLLO_KEY` in the environment, never in a prompt or a config file, and prefer the `rover config auth` profile over exporting the variable. The skills say so; the agent's own judgment does not enforce it.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
