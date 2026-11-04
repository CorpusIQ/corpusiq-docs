---
title: "How CorpusIQ Works - Full Overview"
description: "How CorpusIQ works: connectors, MCP architecture, skills, metric specs, and the trust layer that keeps business answers consistent across every AI assistant."
last_updated: "2026-11-04"
---
# How CorpusIQ works

Short reads that explain what's actually happening when you ask CorpusIQ
a question. No deep tech - just enough to know what you're using.

- [what-is-corpusiq.md](what-is-corpusiq.md) - the elevator pitch and the
  problem CorpusIQ solves. Start here.
- [connectors-explained.md](connectors-explained.md) - what a connector is,
  why authentication is required, and what data flows where.
- [mcp-architecture.md](mcp-architecture.md) - the developer deep dive: what
  Model Context Protocol is, how tools are named and scoped, and how to
  connect any MCP-compatible client to the live-data layer.
- [mcp-apps.md](../mcp-apps.md) - interactive app views. How an MCP server
  returns a rendered interface inside the chat, the sandbox that makes it
  safe, and the four checks that separate a live view from a picture.
- [skills-explained.md](skills-explained.md) - the skills engine. Why
  CorpusIQ answers complex questions consistently instead of randomly.
- [rate-limits-and-quotas.md](rate-limits-and-quotas.md) - API rate limits,
  data freshness, and performance expectations. Read this before running
  production queries or dashboards.
- [reading-files-and-pdfs.md](reading-files-and-pdfs.md) - how CorpusIQ
  reads the text inside your PDFs, Word, Excel, and PowerPoint files in
  Google Drive, OneDrive, and Dropbox - and the one limit (scanned
  images) worth knowing.
- [privacy-and-security.md](privacy-and-security.md) - what CorpusIQ does
  and does not do with your data. Read-only, encrypted, disconnect anytime.
- [metric-specs.md](metric-specs.md) - declare a number once (MRR, AOV,
  active customers), then ask any AI client for it and get the same answer
  every time, with a provenance footer and cross-source drift checks.

## Frequently asked questions

### How does CorpusIQ work?

You connect the business tools you already use with read-only authorization,
then ask a question in your AI assistant. CorpusIQ retrieves the live numbers
from those tools, applies the same metric definitions every time, and returns
an answer with the source cited.

### Which AI assistants does CorpusIQ work with?

ChatGPT, Claude and Perplexity are natively supported. Any MCP compatible
client can also connect to the same endpoint, so the answers follow you rather
than staying inside one chat product.

### Does CorpusIQ keep my business data?

Retrieval is read only and happens on demand. CorpusIQ does not retain raw customer files or full connector response payloads for direct MCP requests.
Query text, per user tool call metadata and bounded outcome summaries stay in
operational logs for up to 30 days, and optional indexed search has a separate
embeddings and minimal metadata lifecycle.

### Do I need a credit card to try it?

No. The trial runs for 30 days with no credit card. Every connector is
included in the plan price, with no add-on tier.

### Why not just ask ChatGPT directly?

You can, and the answer will change with the wording, the session and the
model. CorpusIQ fixes the retrieval and the metric definition, so the same
business question returns the same number in every assistant, with a citation
you can check.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How does CorpusIQ work?", "acceptedAnswer": {"@type": "Answer", "text": "You connect the business tools you already use with read-only authorization, then ask a question in your AI assistant. CorpusIQ retrieves the live numbers from those tools, applies the same metric definitions every time, and returns an answer with the source cited."}},
    {"@type": "Question", "name": "Which AI assistants does CorpusIQ work with?", "acceptedAnswer": {"@type": "Answer", "text": "ChatGPT, Claude and Perplexity are natively supported. Any MCP compatible client can also connect to the same endpoint, so the answers follow you rather than staying inside one chat product."}},
    {"@type": "Question", "name": "Does CorpusIQ keep my business data?", "acceptedAnswer": {"@type": "Answer", "text": "Retrieval is read only and happens on demand. CorpusIQ does not retain raw customer files or full connector response payloads for direct MCP requests. Query text, per user tool call metadata and bounded outcome summaries stay in operational logs for up to 30 days, and optional indexed search has a separate embeddings and minimal metadata lifecycle."}},
    {"@type": "Question", "name": "Do I need a credit card to try it?", "acceptedAnswer": {"@type": "Answer", "text": "No. The trial runs for 30 days with no credit card. Every connector is included in the plan price, with no add-on tier."}},
    {"@type": "Question", "name": "Why not just ask ChatGPT directly?", "acceptedAnswer": {"@type": "Answer", "text": "You can, and the answer will change with the wording, the session and the model. CorpusIQ fixes the retrieval and the metric definition, so the same business question returns the same number in every assistant, with a citation you can check."}}
  ]
}
</script>
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
