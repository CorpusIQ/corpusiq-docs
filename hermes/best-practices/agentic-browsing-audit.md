---
title: "Lighthouse Agentic Browsing: The AI-Readiness Audit Standard"
description: "How to audit a site for Google's Lighthouse Agentic Browsing category: the four signals (llms.txt, WebMCP, accessibility tree, layout stability), fix patterns, and a repeatable checklist."
category: best-practices
tags: [hermes-agent, agentic-browsing, llms-txt, webmcp, lighthouse, accessibility, seo, geo]
last_updated: 2026-10-06
canonical: "https://www.corpusiq.io/docs/hermes/best-practices/agentic-browsing-audit/"
robots: "index,follow"
---

# Lighthouse Agentic Browsing: The AI-Readiness Audit Standard

*Last updated: 2026-10-06*

Google added an **Agentic Browsing** category to Lighthouse in May 2026. Instead of measuring how a page performs for human visitors, it measures how ready a page is for AI agents and agentic browsers: can an agent find a machine-readable summary of the site, call its tools, parse its structure, and render it without layout fighting?

For anyone working on GEO (generative engine optimization) and AEO (answer engine optimization), this is the first standardized, checkable target. You can audit a site in one command and track the score the same way teams track Core Web Vitals.

## The four signals

| Signal | What it checks | Score impact |
|---|---|---|
| llms.txt | A machine-readable site summary at `/llms.txt` | Presence, structure, and links |
| WebMCP | Declared browser tools (`navigator.modelContext.registerTool()`) plus a manifest | Declaration via script, link, or meta tag |
| Accessibility tree | `lang`, landmarks, labels, and alt text coverage | Integrity of the tree agents parse |
| Layout stability | Media with intrinsic dimensions or reserved space | No shifting elements during agent render |

An agent that cannot parse your accessibility tree or that sees your layout jump mid-render has the same experience a human has on a broken mobile page. These four signals are the machine-readable equivalent of usability.

## How to audit

Run Lighthouse with the agentic browsing category enabled:

```bash
npx lighthouse https://example.com --view --only-categories=agentic-browsing
```

Lighthouse reports a 0 to 100 score per signal plus an overall score and letter grade. You can also score a single page with any tool that implements the same four checks, which is useful in CI to fail a build that regresses.

## Fix patterns

### 1. llms.txt

Publish a plain-text summary at your site root. Keep it short, structured, and linked:

```markdown
# Example Product

> One line on what the product does and who it is for.

## Docs
- [Quickstart](https://example.com/docs/quickstart): install and first run
- [API reference](https://example.com/docs/api): endpoints and auth

## Optional
- [Pricing](https://example.com/pricing)
```

### 2. WebMCP

Expose the actions agents may take, directly from the page:

```html
<script>
navigator.modelContext?.registerTool({
  name: "search_docs",
  description: "Search the documentation",
  inputSchema: { type: "object", properties: { query: { type: "string" } } },
  execute: async ({ query }) => search(query)
});
</script>
```

Declare the manifest with a `text/mcp` script or meta tag so scanners can find it without executing the page.

### 3. Accessibility tree

- Set `lang` on the root element.
- Use landmarks: `header`, `nav`, `main`, `footer`.
- Give every image alt text; decorative images get an empty `alt=""`.
- Label every form control.

### 4. Layout stability

Add explicit `width` and `height` attributes to `img`, `iframe`, and `video` elements, or reserve space in CSS with `aspect-ratio`. This is the same fix that improves Core Web Vitals CLS, measured for agents instead of humans.

## Checklist before you ship

- [ ] `/llms.txt` exists and is well formed
- [ ] WebMCP tools are declared and reachable
- [ ] `lang`, landmarks, alt text, and labels are complete
- [ ] All media declare intrinsic dimensions
- [ ] Lighthouse agentic browsing score recorded on the release checklist

## FAQ

### What is Lighthouse Agentic Browsing?

It is a Lighthouse category added in May 2026 that scores how ready a page is for AI agents and agentic browsers. It checks four signals: llms.txt presence, WebMCP integration, accessibility-tree integrity, and layout stability.

### Is this the same as SEO?

It overlaps with technical SEO, but it targets machine consumers instead of search crawlers. A page can rank well and still score poorly here if it lacks llms.txt, declared tools, or stable layout.

### How often should I run the audit?

Run it on every deploy in CI, and review the full site monthly. Score regressions usually come from new pages that ship without llms.txt updates or media without dimensions.

## Related Pages

- [MCP Design](mcp-design): designing the tools agents call
- [Security](security): least privilege and approval gates for agent actions
- [Agent Capability Audit](agent-capability-audit): the four capabilities test
