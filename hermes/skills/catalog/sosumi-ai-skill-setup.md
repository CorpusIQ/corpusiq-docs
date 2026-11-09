---
title: "Sosumi AI - Apple Docs as Markdown Skill"
description: "nshipster/sosumi.ai on skills.sh: 2.2K combined installs; one skill that fetches Apple docs, HIG pages and WWDC transcripts as Markdown."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sosumi-ai-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "apple", "documentation", "mcp", "markdown"]
---

# Sosumi AI - Setup Guide

**Source:** [nshipster/sosumi.ai](https://www.skills.sh/nshipster/sosumi.ai) via skills.sh - 2.2K combined installs across 1 indexed listing; snapshot 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 483 stars, MIT via LICENSE.md, `main` branch, last pushed 2026-11-07, 2 SKILL.md files in a 108-file tree, at `public/SKILL.md` and `plugin/skills/sosumi/SKILL.md`
**Category:** Apple platform documentation access: a hosted DocC renderer, an MCP server, a CLI and one agent skill that ties them together
**Quality Tier:** 🟡 Yellow - derived from a single Snyk Warn on the one sampled skill; MIT licensed, no Fail verdict, and only one listing to sample.

Sosumi is a service rather than a knowledge base. `developer.apple.com` renders its documentation with JavaScript, so a plain HTTP fetch returns the page shell, not the prose. Sosumi resolves an Apple documentation URL to the underlying DocC JSON, renders it to Markdown, and serves it at the same path on `sosumi.ai`. The skill in this repository is the instruction layer for that service: it tells an agent when to use it, how to build the URL, and what to do when the path is wrong.

The repository is small and the skill inside it is smaller. 108 files, two `SKILL.md` files that are byte-identical copies of each other, and a body of 100 lines. The rest is the service: a Hono application deployed on Cloudflare Workers, an npm CLI package (`@nshipster/sosumi`), an MCP server published to the MCP Registry as `ai.sosumi/sosumi`, and a vitest suite. `public/SKILL.md` is the source of the skill and `plugin/skills/sosumi/SKILL.md` is the copy the Claude Code plugin loads; the README documents the `cp` between them and says a test fails when the two differ.

2,206 installs against 483 stars on a single indexed listing is a low install-to-star ratio, and the shape explains it: the skill is one file that points at a hosted API, so an agent that can already fetch a URL gains little from it, while an agent that cannot gains the whole workflow. The last push, 2026-11-07, is two days before this snapshot.

## Installation

Claude Code installs it as a plugin, which packages the skill and the MCP server together:

```text
/plugin marketplace add NSHipster/sosumi.ai
/plugin install sosumi@sosumi-ai
```

The skills CLI route pulls the skill from the GitHub repository:

```bash
npx skills add https://github.com/nshipster/sosumi.ai --skill sosumi
```

The README also documents a hosted route that reads the skill file from the service itself, which is the one it recommends for spec-compliant clients:

```bash
npx skills add https://sosumi.ai
```

The two routes are not equivalent. The GitHub route pins the repository content, and the hosted route always serves what `https://sosumi.ai/SKILL.md` returns today.

For the MCP server, any client that speaks Streamable HTTP or SSE can connect straight to `https://sosumi.ai/mcp`. Clients without either transport proxy it over stdio:

```json
{
  "mcpServers": {
    "sosumi": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://sosumi.ai/mcp"]
    }
  }
}
```

The CLI is a separate install and is not required by the skill. It is useful when you want to test a path by hand before an agent uses it:

```bash
npx @nshipster/sosumi fetch https://developer.apple.com/documentation/swift/array
```

For regular use, install it once and call `sosumi` directly:

```bash
npm i -g @nshipster/sosumi
sosumi fetch /documentation/swift/array
sosumi search "SwiftData"
```

Every route ends at the same place: a Markdown document. The skill works with nothing installed but a fetch tool, because the primary mechanism is a host swap on a URL.

## What It Provides

The threshold for this guide is zero installs, so the single indexed listing appears:

| Skill | Installs | Use For |
|---|---|---|
| sosumi | 2,206 | Fetches Apple API reference, Human Interface Guidelines, WWDC session transcripts and external Swift-DocC pages as Markdown by swapping developer.apple.com for sosumi.ai, with a search step first when the exact path is unknown |

No indexed listings fall below the threshold; the single listing appears above.

The body is a routing document in the same sense as a coordinator skill. It opens with a list of triggers (Apple platform APIs, availability and parameter behaviour, HIG questions, WWDC transcripts, external Swift-DocC), then gives a three step workflow: swap the host if you already have a URL, search first if you do not, and prefer specific symbol pages over top-level pages when answering an implementation question.

Four content types are documented with path patterns rather than examples alone. API reference is `documentation/{framework}/{symbol}`, HIG is `design/human-interface-guidelines/{topic}`, video transcripts are `videos/play/{collection}/{id}`, and external Swift-DocC pages are fetched by prefixing the full HTTPS URL with `/external/`. The MCP server exposes the same four surfaces as named tools: `searchAppleDocumentation`, `fetchAppleDocumentation`, `fetchAppleVideoTranscript` and `fetchExternalDocumentation`.

Two sections earn their space. The best practices section warns against trusting conformance conditions such as "Conforms when `Element` conforms to `Hashable`", because Apple's documentation data omits some and gets others wrong; when a condition matters, it tells the agent to read the declaration in the module's `.swiftinterface` file in the SDK. The troubleshooting section covers the two failures you will actually hit: a 404 or sparse output, which means the path is wrong or too broad and a search should come first, and an external page that cannot be fetched, which usually means the host blocks the crawler through `robots.txt` or `X-Robots-Tag`.

A live response carries its own provenance. Fetching `https://sosumi.ai/documentation/swift/array` returns Markdown that opens with frontmatter holding `title`, `description`, `source` (the original `developer.apple.com` URL) and a `timestamp`, followed by a `**Navigation:**` line and the symbol text. That timestamp is what makes the citation checkable, since it says when the page was rendered rather than when the model was trained.

## Why This Matters for Hermes Agents

API hallucination is the failure this removes. An agent asked for `Array`'s API, a SwiftUI modifier or a HealthKit initializer will produce something plausible from memory, and the plausible version is often a signature that existed two SDK cycles ago or never existed. Swapping a host in a URL is a small enough instruction that an agent follows it reliably, and the result is the current signature.

The second problem is access, not knowledge. Apple's documentation is JavaScript-rendered, so a generic page fetch returns navigation chrome and no prose. Without a renderer, an agent concludes the page is empty or paraphrases the title. Sosumi turns that fetch into a Markdown document, which means the ordinary tool an agent already has becomes sufficient, and the MCP server is an optimisation rather than a requirement.

The third is HIG and WWDC material, which is the part of Apple guidance that agents handle worst because it is prose rather than code. Transcripts are searchable in the same way as API pages, so "what did Apple say about this at WWDC" becomes a fetch instead of a guess.

The counterweight is that this is one more remote dependency in the answer path. Every call goes to `sosumi.ai`, which is a third-party host run by an independent developer, and the returned Markdown lands in the agent's context as instructions as well as text. The skill is well scoped for that risk, but it does not remove it.

## Usage

| You say | What happens |
|---|---|
| "What is the current signature for SwiftData's @Query" | Fetches the symbol page through `sosumi.ai` and answers from the rendered Markdown, keeping the source URL in the reply |
| "What does the HIG say about colour contrast" | Swaps in the `design/human-interface-guidelines/foundations/color` path and reads the guideline text, rather than recalling a summary of it |
| "Find what the WWDC session said about Liquid Glass adoption" | Searches Apple documentation first if the session id is unknown, then fetches the transcript at `videos/play/{collection}/{id}` |
| "I need the docs for a Swift package that is not Apple's" | Uses the `/external/` prefix with the package's DocC URL, provided the host does not block the crawler |
| "This page came back empty" | Checks whether the path is too broad, runs a search, and retries against a specific symbol page |
| "Is this API available on macOS or iOS only" | Answers from the symbol page's availability section rather than from memory, and flags platform gaps explicitly |

## Verification

The hosted skill file is the canonical copy and returns 200:

```bash
curl -fsSL https://sosumi.ai/SKILL.md | head -6
```

It should open with YAML frontmatter holding `name: sosumi` and a `description` that begins `Fetches Apple documentation as Markdown via Sosumi`. There is no `license`, `version` or `homepage` field, so do not expect one.

The repository copy has to match it, and the raw path carries a `plugin/skills/` prefix rather than the usual `skills/`:

```bash
curl -fsSL https://raw.githubusercontent.com/nshipster/sosumi.ai/main/plugin/skills/sosumi/SKILL.md | head -6
curl -fsSL https://raw.githubusercontent.com/nshipster/sosumi.ai/main/public/SKILL.md | head -6
```

Both must show the same `name` and `description`. The repository's own test suite enforces that equality, so a difference means you are looking at an unreleased edit rather than a supported state. The comparison is a one liner:

```bash
diff <(curl -fsSL https://raw.githubusercontent.com/nshipster/sosumi.ai/main/public/SKILL.md) <(curl -fsSL https://raw.githubusercontent.com/nshipster/sosumi.ai/main/plugin/skills/sosumi/SKILL.md) && echo identical
```

The service itself is the third check, because a skill that points at a dead endpoint is worse than no skill:

```bash
curl -fsSL https://sosumi.ai/documentation/swift/array | head -8
```

That should print frontmatter with `title: Array`, a `source` pointing at `developer.apple.com`, and a `timestamp`, followed by the navigation line. A JSON body, an HTML shell or a 404 means the renderer changed its output contract and the skill's path assumptions need re-reading.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sosumi | Pass | Pass | Warn |

The Snyk Warn is the only flag, and it applies to a 100-line Markdown file that contains no executable code. In plain words: one scanner wants a human to look before this goes into a pipeline, and the file itself has nothing to run. Read the sosumi security page on skills.sh for the specific rule before you decide; do not treat the Warn as evidence of a payload, and do not treat the two Pass verdicts as an audit of the service behind the URL.

What the skill actually does at runtime is fetch. Its whole mechanism is issuing HTTPS requests to `sosumi.ai` and placing the response in the model's context. That makes the content path the risk surface: a documentation page is remote text that the agent will treat as authoritative, and a compromised or spoofed response would be a prompt injection with the credibility of Apple documentation. Two things bound that risk and neither eliminates it. The responses carry a `source` URL and a `timestamp` in frontmatter, so a wrong or stale page is visible if you look, and the skill instructs the agent to keep source links in answers so a reader can check the original. There is no content sanitisation step.

The MCP server moves the same traffic into a tool call against `https://sosumi.ai/mcp`, which means your queries leave the machine and the server sees the symbols and topics you are researching. That is a data-flow decision, not a vulnerability, and it is worth making deliberately if you work on unreleased APIs. The CLI route has the same property. If neither is acceptable, the project is self-hostable: Node 20 or newer, `npm install`, `npm run dev`, then point clients at `http://localhost:8787`.

Self-hosting has its own caveat, documented in the README. External Swift-DocC fetching is restricted by `EXTERNAL_DOC_HOST_ALLOWLIST` and `EXTERNAL_DOC_HOST_BLOCKLIST`, and the README states directly that hostname-based private-network checks cannot fully prevent DNS rebinding, so it asks you to set an explicit allowlist in production. An unconfigured self-hosted instance that fetches arbitrary external URLs on request is a server-side request forgery surface, and the allowlist is the control.

The supply chain is stronger than average for a project this size. The npm package is published from a tagged release workflow using OIDC trusted publishing with `npm publish --provenance`, and the MCP Registry entry is published by the same workflow, so the artifacts carry verifiable build provenance. The repository is MIT licensed and the README states plainly that it is unofficial and not affiliated with or endorsed by Apple, which also means no vendor support and no disclosure channel beyond the repository.

## Limitations

- Snapshot data, verified 2026-11-09: 2,206 combined installs across 1 indexed listing; 483 GitHub stars; MIT license; last pushed 2026-11-07. Counts drift over time.
- One indexed listing covers every route. A plugin install, a skills CLI install, a CLI package and an MCP server all funnel into the same 2,206 figure, so the number cannot tell you how the skill is actually being used.
- The skill is a dependency on a hosted service. If `sosumi.ai` is unavailable or changes its response format, the agent's fallback is a plain fetch of `developer.apple.com`, which returns the JavaScript shell rather than the documentation.
- Two skill files must stay identical. Editing `plugin/skills/sosumi/SKILL.md` in place is the wrong move; the README says to edit `public/SKILL.md` and copy it across, and the test suite fails when they drift.
- Render quality is bounded by Apple's DocC JSON. The skill itself warns that conformance conditions are sometimes missing or wrong, and tells the agent to read the `.swiftinterface` in the SDK when a condition matters. Treat the Markdown as a fast first read, not as the last word on generic constraints.
- Hosts that disallow the `sosumi-ai` user agent through `robots.txt` or `X-Robots-Tag` cannot be fetched, so external Swift-DocC coverage is incomplete by policy rather than by capability.
- The project is unofficial and not affiliated with Apple. There is no SLA, no deprecation notice, and no guarantee that the path patterns in the skill match a future Apple documentation restructure.

## Related

- [Apple Design Skill - HIG Review Across Frameworks](/hermes/skills/catalog/apple-design-skill-setup)
- [Xcode Build Optimization - iOS Build Performance Setup](/hermes/skills/catalog/xcode-build-optimization-setup)
- [SwiftUI Pro - Apple UI Development Skill](/hermes/skills/catalog/twostraws-swiftui-pro-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Teach the host swap rather than the service. The instruction "replace developer.apple.com with sosumi.ai" survives model upgrades and needs no tool configuration, and it is the reason the skill works with any agent that can fetch a URL.
- Search before fetching when the path is uncertain. A top-level framework page returns a summary and an index; a symbol page returns the signature, availability and discussion you actually needed.
- Keep the `source` and `timestamp` values from the response frontmatter in your notes. They are the difference between "an agent told me" and a citation someone can check against the original page.
- Do not let the agent answer a conformance or generic-constraint question from rendered Markdown alone. The skill says Apple's data is incomplete there for a reason, and the `.swiftinterface` file is the authoritative read.
- If you run this at volume, self-host and set `EXTERNAL_DOC_HOST_ALLOWLIST` explicitly. It removes the third-party data flow and closes the request-forgery surface the README warns about at the same time.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
