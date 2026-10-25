---
title: "EU AI Act Explorer MCP - Articles, Deadlines, Duties"
description: "A keyless server over the amended EU AI Act: article text, definitions, role obligations and a dated timeline of what is in force and what is not."
category: Compliance / Legal Reference
stars: n/a (free, keyless)
added: 2026-10-24
source: "mcpservers.org /all p1-20 fresh cohort (late sweep, October 24 2026) + live JSON-RPC calls on the endpoint"
relevance: ★★
tags: [eu-ai-act, compliance, regulation, obligations, deadlines, legal-text, keyless, governance]
---

# EU AI Act Explorer MCP

**The amended AI Act, answerable.** A keyless server over Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744, with every answer citing the consolidated text and stating which obligations are already in force and which are not.

```
Server type: Remote (JSON-RPC 2.0 over HTTPS POST)
Endpoint: https://mcp.euaiactlaw.com/mcp
Auth: None. No account, no key
Protocol: 2025-03-26 confirmed at initialize; the vendor also states support for 2026-07-28
Tools: 9 (article, recital, annex, definition, search, obligations, deadlines, assessment, feedback)
Registry: com.euaiactlaw/eu-ai-act-explorer 1.0.0, active
Built by: EU AI Act Explorer (euaiactlaw.com)
```

## Why This Matters for Operators

Any business that puts AI into a product or a hiring process in Europe has obligations with dates attached, and the dates moved. The amended timeline now spreads duties from February 2025 to August 2028, with a new set of prohibitions landing on 2 December 2026. A company that read a summary written in 2024 is working from a map that no longer matches the road.

The practical failure is not ignorance of the Act, it is applying the wrong phase. A deployer of a high-risk system reading Article 26 today would assume duties that are not yet in force, and a company planning next year would miss the December 2026 deadline entirely. This server answers both: the obligation and its application date.

## What It Actually Does

Probed live in this sweep. `initialize` returned `serverInfo` `eu-ai-act-explorer` 1.0.0 with the tools capability and an instruction block stating that it is a read-only reference, every answer cites the Official Journal source, and it is not legal advice. `tools/list` returned nine tools.

| Tool | Argument | What it returns |
|---|---|---|
| `get_article` | `number`, including lettered numbers such as 60a | the full amended text of one article, with citation |
| `get_recital` | `number` | the full text of one recital |
| `get_annex` | roman numeral | the full text of one annex |
| `get_definition` | `term` | the Article 3 definition with its reference |
| `search_text` | `query` | ranked matching passages across articles, recitals and annexes, with article references |
| `get_obligations` | `role`, optional risk tier | the obligation list for a role, each mapped to its article and application date |
| `get_deadlines` | none | the application timeline as of today, with in-force status for each phase |
| `assess_compliance` | the entity's answers | a compliance assessment over the same decision tree as the site's interactive checker |
| `send_feedback` | free text | report a wrong text, a missing amendment or a working answer |

Two real calls, quoted from the run.

**The timeline.** `get_deadlines` returned, as of 2026-10-25: Chapters I and II in force since 2 February 2025; the notified bodies, general-purpose AI, governance and Article 78 provisions in force since 2 August 2025; Articles 102 to 110 in force since 27 July 2026; the new Article 5(1)(ba) to (bb) prohibitions, Article 5(1a) to (1b) and the Article 50(2) compliance deadline for pre-existing systems not yet in force until 2 December 2026; high-risk obligations for Annex III systems on 2 December 2027; and high-risk obligations for Annex I and Article 6(1) systems on 2 August 2028.

**The duties for a role.** `get_obligations` for `deployer` returned a numbered list with an article link on every line: Article 4 AI literacy, in force since 2 February 2025 with the current wording applying from 27 July 2026; Article 5, stop using any system performing a prohibited practice, with points (ba) to (bb) applying from 2 December 2026; and Article 26(1), (2), (4) and (5) on instructions for use, human oversight, input data and monitoring, applying from 2 December 2027 for Annex III systems and 2 August 2028 for Annex I systems.

## Installation

No installation. Add the URL as a remote MCP server:

```
https://mcp.euaiactlaw.com/mcp
```

The transport is plain JSON-RPC over HTTPS POST, which means clients that only speak Streamable HTTP can still reach it. There is no key to obtain and nothing stored on the server side.

## Business Relevance

CorpusIQ's own answering surfaces tell operators which platform supports what; this server tells them what the regulation requires of them while they use it. The pairing matters for a European business adopting AI in hiring, credit, education or safety-relevant operations, where the question is not whether AI is allowed but which duties attach and when.

## Integration with CorpusIQ

The natural use is a compliance check before a workflow goes live: ask which obligations attach to the role the company plays, then ask the deadlines tool whether they apply yet. Because the answers carry article references, the operator can hand the citation to a lawyer instead of a summary.

## Limitations

- Legal information, not legal advice, and the server says so in every response.
- EU law only, with no member-state implementing law, no guidance documents and no case law.
- The tool returns text; it does not judge a specific system's risk tier for you. The `assess_compliance` decision tree takes the operator's own answers as input.
- Two tool calls were driven in this sweep (`get_deadlines` and `get_obligations`); `assess_compliance` and `search_text` were listed but not executed, and a later call in the same sweep was refused with HTTP 403, so repeatability under sustained use is unproven.
- The class is not empty. The official registry also lists `com.eurogpsr/eu-ai-act` 1.1.0, `dk.powerquant/eu-ai-act` and a CSOAI compliance server at 1.8.15, and a prior submission called EU AI Act Compliance was held in September 2026 as thin documentation. This entry is catalogued because it is keyless, its tool surface was enumerated, and it answers with citations rather than a summary.
- An earlier compliance-checker submission that touched Article 50 was held in the AI-visibility class; that disposition still stands and is not reopened here.

## FAQ

### Do I need an account or an API key?

No. The endpoint accepts unauthenticated JSON-RPC POST calls, which is why it could be enumerated and driven in this sweep.

### Which version of the Act does it serve?

Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744, consolidated text of 27 July 2026, with the Official Journal cited in every answer.

### Can it tell me whether my system is high risk?

It can run the same assessment decision tree the vendor's site uses, from answers you supply, and it can list the obligations for a role and a risk tier. It does not classify a system on its own.

### What are the next deadlines I should plan around?

On the current text, 2 December 2026 for the new prohibitions and the Article 50(2) deadline for pre-existing systems, then 2 December 2027 for Annex III high-risk obligations and 2 August 2028 for Annex I systems.

## See Also

- [Double AIgents DSAR MCP - GDPR Deadlines and Breach Clock](/hermes/mcp/servers/external/double-aigents-dsar-mcp/)
- [MCP GLP Audit Proxy - Tamper-Evident Tool-Call Trail](/hermes/mcp/servers/external/mcp-glp-audit-proxy/)
