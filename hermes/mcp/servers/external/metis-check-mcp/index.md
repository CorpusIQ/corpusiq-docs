---
title: "Metis Check MCP - Signed Proof a Citation Resolves"
description: "Checks a DOI, ORCID, LEI, ISBN or SEC CIK at the registry that issues it and files a signed report in one of four states, not a pass or fail."
category: Research / Verification
stars: n/a (commercial, five checks a month free, human verification on paid)
added: 2026-10-27
source: "live probe on https://mcp.metisfoundry.com/mcp returning HTTP 401 with the body Sign in to Metis to connect at 04:05Z on 2026-10-28, the vendor connector documentation read through the r.jina.ai reader proxy covering auto-check default, allowance behaviour and the Verified plan, and the mcpservers.org listing at /servers/mcp-metisfoundry-com-docs"
relevance: ★★★
tags: [citations, verification, registries, doi, lei, orcid, sec-cik, oauth, audit, signed-report]
last_updated: "2026-10-27"
---

# Metis Check MCP

**Every other citation tool in this catalog reports whether a link loads. This one reports whether the identifier resolves to the work the sentence claims it does, and it has a state for cannot tell.**

```
Server type:  Remote (Streamable HTTP), OAuth sign-in
Endpoint:     https://mcp.metisfoundry.com/mcp
Auth:         Metis customer account, OAuth, verification permission
Public surface: initialize without a token returns HTTP 401
Registries:   DOI, PubMed, arXiv, LEI, ORCID, ROR, ISBN, SEC CIK
States:       settled true, settled false, not decidable, unreachable
Free tier:    five checks a month per account
Plans:        monthly allowance, human verification on Verified
Built by:     Metis Foundry
```

## Why This Matters for Operators

An assistant that cites a source has told you where it looked. It has not told you that the source says what the sentence says. Those are different claims and only the second one is worth acting on, which is why a citation check that returns a boolean is worse than useless: it invites a reader to treat a live URL as a verified statement.

The four states are the design. **Settled true** and **settled false** are answers from the registry that issues the identifier. **Not decidable** is the case where the registry cannot settle it, which is most identifiers in practice and the state every other tool silently rounds to true. **Unreachable** is the registry being down, which is a different fact again and should never be reported as a bad citation. A tool that keeps those four apart can be wired into a review process. One that collapses them cannot.

The second half is the receipt. Each report is signed so anyone can recheck it, which turns "I verified this" into an artefact with a name and a date on it rather than a sentence in a chat transcript.

## Verified and Documented

The endpoint answers a bare `initialize` with **HTTP 401 and the body `Sign in to Metis to connect`**, the correct shape for an account-gated connector, so the surface below is the vendor's documentation.

Automatic checking exists and is **off by default**. An operator turns it on per conversation with an explicit instruction, and turning it off stops subsequent checks while allowing a check already running to finish. The vendor states plainly that the dependency is the client calling the tool and that Metis cannot watch a conversation in the background or verify every factual claim, which is the honest boundary of a tool like this.

The allowance is a hard stop rather than a meter that can run over: automatic checks stop at the monthly allowance and no overage payment is ever started, and the account can be asked how many checks remain. The connector receives only the identifiers submitted to it, and the documentation says not to send a whole conversation.

On the paid tier a person is in the loop. A request to verify a specific report has a researcher check the identifiers in real time, and the result is filed on the same report as a signed addendum carrying the reviewer's name and the date. A live verification mode covers every report the account files for the following eight hours. The scope of that human step is stated precisely: the researcher confirms that each identifier resolves to the work or entity the citation names and what the registry and source document say, **not whether the surrounding argument is true**. That sentence is the most useful thing in the documentation, because it is the exact limit of what any citation check can claim.

## Where It Fits Beside CorpusIQ

The failure this tool addresses is the one that makes AI answers untrustworthy in a business setting: a confident sentence with a plausible source. CorpusIQ answers with source citations from the operator's own connected systems, where the source is the record itself. Metis covers the other case, a public identifier offered as proof, and it does so by going to the registry that issues the identifier rather than to the page that cites it.

For an operator reviewing a research memo, a vendor claim or a diligence file, the useful workflow is: extract the identifiers, check them in one pass, and keep the signed reports with the document. Anything reported not decidable is a question for a person, and that is precisely what the tool refuses to hide.

## Limits Worth Recording

- **Five checks a month free.** Enough to evaluate the output, not enough to review a memo. The paid tier is where the volume lives.
- **Identifiers only.** A claim with no identifier cannot be checked, and much of what a business relies on has none.
- **Registries are the authority, not the truth.** A DOI resolving to the named paper says nothing about whether the paper is right, and the vendor says so.
- **No call was executed.** Without an account the connector answers 401, so the four states, the allowance behaviour and the human verification scope are documented behaviour recorded from the vendor pages.
- **Client-dependent.** The automatic mode lives in the client's willingness to call the tool, and the documented path is Claude and the shared ChatGPT and Codex allowance.

## Wiring It Up

Add `https://mcp.metisfoundry.com/mcp` as a connector named Metis Check, sign in with the Metis customer account, and approve the verification permission. Leave auto-check off until a specific review needs it, then turn it on for that conversation and off again.

## FAQ

### Does it tell me whether a source supports the claim?

No, and it says so. It confirms that the identifier resolves to the work or entity the citation names and reports what the registry and the source document say. Whether the surrounding argument is true is outside its scope, on the free tier and on the Verified tier alike.

### What is the difference between not decidable and unreachable?

Not decidable means the registry answered and could not settle the identifier. Unreachable means the registry did not answer. The first is a fact about the identifier and the second is a fact about the network, and a review process has to treat them differently.

### Can it check a whole document automatically?

Not on its own. Auto-check is opt-in per conversation, it depends on the client calling the tool, and it stops at the monthly allowance without ever starting an overage. For a document, extract the identifiers first and check them explicitly.

### What does the human verification add?

A named researcher checks each identifier in a specific report in real time, and the finding is filed on that report as a signed addendum with the reviewer's name and the date, or covers every report the account files for eight hours. It is available on the Verified plan.
