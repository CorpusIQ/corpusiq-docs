---
title: "tld.expert MCP - Domain and Name Checks With Sources"
description: "Six keyless tools for naming: RDAP availability, dated registrar prices, TLD fit, and whether a name is free on GitHub, npm or the USPTO."
category: "Business Operations"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-25
source: "Submission chatmcp/mcpso #8056 filed 2026-11-25T10:19:51Z; registry record expert.tld/tld-expert 1.0.0 with the remote https://tld.expert/mcp; keyless initialize and a six-tool tools/list on https://tld.expert/mcp read 2026-11-25; check_domain_availability, suggest_tld_alternatives, get_tld_prices, explain_tld and check_brand_name driven the same day"
relevance: "★★★"
tags: [domains, naming, branding, trademark, pricing, registrar, remote-mcp]
last_updated: "2026-11-25"
---

# tld.expert MCP

**Naming a company or a product is four questions in a row, and most assistants answer only the first one.** Is the domain free, what does the ending cost after the first year, what else could I call it, and is the name already taken somewhere that matters, like GitHub, npm or the trademark register. tld.expert answers all four from one keyless endpoint, and it states which registry or list each answer came from and when that source was read.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://tld.expert/mcp
Auth:        none, no key and no account
Registry:    expert.tld/tld-expert 1.0.0
Pricing:     not stated on the server; tld.expert is a reference site, not a registrar
Tools:       6, read from a keyless tools/list
```

The `initialize` response carries an `instructions` string that frames the whole design, and one clause is worth quoting because it is the honest part most naming tools skip: *"check_brand_name for GitHub, npm and US trademark answers on a name (\"none\" there is never \"available\")."* The server also says plainly what it is not: *"an independent (not a registrar) reference for domain extensions."* That distinction matters when you compare its prices against a registrar's own upsell.

## What the six tools do

| Tool | What it needs | What it answers |
| --- | --- | --- |
| `check_domain_availability` | `domain` | taken or available, with the registry record and the RDAP server read |
| `suggest_tld_alternatives` | `domain`, optional `brief` | candidates across endings and name variants, with the taken ones folded out |
| `get_tld_prices` | `tlds` | dated first-year, renewal and five-year cost per registrar |
| `explain_tld` | `tld` | what the ending is, who runs it, who may register, abuse rates and size |
| `check_brand_name` | `name` | GitHub, npm and US trademark verdicts, each with a timestamp |
| `submit_feedback` | `tool`, `what_happened`, `expected`, `proposed_fix` | a written defect report, read by a person |

## A taken domain, with the registrar named

`check_domain_availability` on `corpusiq.io` returned **taken**, and then the record behind the verdict:

- Registered through a privacy service (Domain Protection Services, Inc.), which hides the owner.
- Registrar **Name.com, Inc.**, registered **16 October 2025**, expires **16 October 2027**.
- Source: RDAP at `rdap.identitydigital.services`, checked **2026-11-25**.

`acme.com` returned **taken** with registrar **eNom, LLC**, registered **17 April 1991** and expiring **18 April 2027**, read from `rdap.verisign.com`. Two verdicts, two different registries, both cited. That is the pattern an operator should look for: a naming tool that says "taken" without naming the registry is asking to be believed rather than checked.

## What a name costs after the first year

This is the section to read twice, because the first-year price is the number registrars advertise and the renewal is the number that arrives a year later. `get_tld_prices` for `.com`, `.io` and `.ai` returned, on **2026-11-25**:

| Ending | First year | Renewal | Cheapest direct buy | Five years |
| --- | --- | --- | --- | --- |
| `.com` | $11.62 | $11.62 | Dynadot | $58.10 at Dynadot |
| `.io` | $20.91 | $51.80 | Porkbun | $228.11 at Porkbun |
| `.ai` | $82.70 | $82.70 | Porkbun, two-year minimum | $413.50 at Porkbun |

Every one of those five-year figures reproduces by hand, which is the check to run before you trust a price table: `20.91 + (4 x 51.80) = 228.11` for `.io`, `82.70 x 2 = 165.40` at the two-year minimum, `82.70 x 5 = 413.50` for `.ai`, and `11.62 x 5 = 58.10` for `.com`. The `.io` row is the one to act on. **The renewal is 2.5 times the first year** (51.80 / 20.91 = 2.477), and the tool names it as a *renewal trap 2.5x at Porkbun* rather than leaving you to divide.

The price data is dated at the row level, not just at the top. The `.com` entry carries one more line that a static price list cannot: *renewal changed $10.46 to $11.17 at Cloudflare on 2026-11-24*. A price page that tells you what moved and when is a price page you can put next to an invoice.

## Can an agent prove a name is free to use?

No, and the server says so in the tool itself. `check_brand_name` on `corpusiq` returned:

- **GitHub:** taken by an organization, checked `2026-11-25T17:02:09.857Z`.
- **npm:** no package named `corpusiq`, checked `2026-11-25T17:02:09.858Z`.
- **US trademarks:** no live mark containing the name, checked `2026-11-25T17:02:09.841Z`.
- And the caveat, in the answer: *"None means the source has no record, not that the name is free to use. Not legal advice."*

That last line is the reason this tool is worth a guide. Three negative verdicts in one call is exactly the answer that tempts an assistant to write "the name is available", and the server pre-empts it. A negative trademark search means the register search returned nothing, not that the mark is unencumbered.

### Is a .ai domain worth the price?

`explain_tld` on `.ai` returns an opinion with the numbers behind it: a country-code domain run by the **Government of Anguilla**, ranked **#1 in Best TLDs for AI Products** and **#2 in Best TLDs for Startups: What to Get When the .com Is Taken**, with first-year and renewal both **$82.70** and a two-year minimum. The abuse rates come from Interisle per **10,000 domains**: phishing **5.0** against `.com` at **17.2** (May to July 2026), spam **10.0** against **50.9** (March to May 2026), malware **0.3** against **1.3** (July to September 2026), each linked to the CSV it was read from. Size comes from DomainTools counting **1,485,690** `.ai` domains, read **2026-11-24**. An operator deciding between a $11.62 `.com` and an $82.70 `.ai` now has the renewal cost, the abuse exposure and the installed base in one answer.

### What else could I call it, and which endings still fit?

`suggest_tld_alternatives` on `corpusiq.com` with the brief "business data answers for operators" read the input as **SaaS**, grouped the candidates, and reported **12 of 19 not taken, 7 taken and folded**. It separated *endings that fit* (`corpusiq.tech`), *popular endings* (`.ai`, `.co`, `.dev`, `.net`, `.org`, `.xyz`) and *name variants* (`corpusbiz.ai`, `corpusanswers.com`, `corpusanswers.ai`, `corpusops.ai`, `corpusintel.ai`). The three-group split is the part worth keeping: a flat list of nineteen domains makes the operator do the sorting, and the folded count tells you how much filtering already happened.

## Where it sits next to the rest of this catalog

Domain availability and price checking is already covered here by **Just Domain MCP**, which reads one registrar's first-year and renewal costs. tld.expert takes the other seat: it is registrar-independent, it prices several registrars against each other with the date each was read, and it adds the brand cross-check across GitHub, npm and the trademark register that no existing entry in this catalog performs. If you want portfolio operations instead, **Domain MCP** (Dynadot) and **OSIR Domain MCP** (registrar operations) are the entries for registering and renewing.

**Use it when** an operator is naming a company, a product or a newsletter and wants the domain, the renewal, the alternatives and the name collisions in one pass. **Skip it when** you already own the domain and need to manage DNS or renew a portfolio.

## Limits measured this pass

- The trademark leg reads a search-results page and can only report that no live mark came back. It cannot prove the name is unencumbered, and the server says so in the answer text rather than in documentation.
- `check_domain_availability` and `suggest_tld_alternatives` declare no required fields, so a bare call is accepted by the schema. Send `domain` anyway; the answers are only as specific as the input.
- The `.io` renewal of $51.80 and the `.ai` two-year minimum are the two rows where the cheap first year and the real cost diverge most. Treat any first-year price without a renewal beside it as incomplete.

## See also

- [Just Domain MCP](/hermes/mcp/servers/external/just-domain-mcp/) for single-registrar availability and pricing.
- [Domain MCP](/hermes/mcp/servers/external/domain-mcp/) for Dynadot registration, DNS and transfers.
- [Expired Domains MCP](/hermes/mcp/servers/external/expired-domains-mcp/) for screening expired and auction names.
- [External MCP Server Catalog](/hermes/mcp/servers/external/) for the full index.
