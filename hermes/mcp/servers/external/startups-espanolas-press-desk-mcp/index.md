---
title: "Startups Espanolas Press Desk MCP - Spanish Press Releases"
description: "Four tools for sending a press release to three Spanish business publications: the terms, the publications, submission and status, keyless."
category: "Marketing"
stars: n/a (vendor-hosted)
added: 2026-11-21
source: "chatmcp/mcpso submission #7768 filed 2026-11-21T13:03:51Z; the official MCP registry record es.startups-espanolas/notas-de-prensa (domain verified by DNS TXT); keyless initialize and tools/list, then three tools/call requests on 2026-11-21"
relevance: ★★★
tags: [pr, press-release, spain, media, editorial, remote-mcp, keyless]
last_updated: "2026-11-21"
---

# Startups Españolas Press Desk MCP

**Remote MCP server (Streamable HTTP, no authentication to read)** - the press desk of a Spanish-language business media network: three publications, one submission flow, and a confirmation step that a human has to answer before anything is reviewed. An agent can list the publications, read the terms, submit a release and follow its status by ticket.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://app.startups-espanolas.es/mcp
Tools:       4 (ver_medios, ver_condiciones, enviar_nota, estado_nota)
Registry:    es.startups-espanolas/notas-de-prensa
             (domain ownership verified by DNS TXT on the apex)
Network:     startups-espanolas.es, empresas-espanolas.es,
             inmobiliarias-espanolas.es
Repo:        https://github.com/martinschenk/startups-espanolas-mcp
```

## Why This Matters for Operators

A press release is a small transaction with an editorial outcome, and most "PR" tooling hides one of the two halves. This one states both before anything is sent: the free allowance, what a paid note looks like to a reader, and that publication is a decision rather than a purchase.

The three read-only tools return the whole contract in structured form, in Spanish by default and partly translated when asked:

| Call | Returns |
|---|---|
| `ver_medios` | three publications, each with its topics, what it accepts and a criteria URL |
| `ver_condiciones` | the free allowance, the package prices, the labelling rules, the refusals and the process |
| `estado_nota` | the status of a submission by ticket: waiting for confirmation, in review, published with URL, rejected, answered by email, waiting for payment, expired |

And the flow is deliberately not autonomous: `enviar_nota` queues the release and then emails a confirmation request to the sender address, and the review does not start until that email is answered. The instructions say it plainly - *"Call ver_condiciones first. enviar_nota sends a confirmation request…"* - and the terms end with the sentence that matters most for an agent: **"Esta herramienta nunca mueve dinero."**

## Measured Behaviour

Three of the four tools were driven keyless on 2026-11-21. `enviar_nota` was not driven, because it sends a confirmation email to a real sender address and opens a human editorial queue - a mutation with an outbound message, which is documented here rather than fired.

**The three publications** (`ver_medios`):

- **Startups Españolas** - startups, entrepreneurship, self-employment, technology, AI, robotics and the economy.
- **Empresas Españolas** - companies and the economy, studies, people and business events.
- **Inmobiliarias Españolas** - housing, developers, proptech, rentals and offices.

**The terms** (`ver_condiciones`), quoted to the euro:

```text
Free        5 press notes per sender across the whole network
Paid        10 notes   19 EUR net   (+ VAT)
            50 notes   69 EUR
           100 notes   99 EUR
           250 notes  199 EUR
Labelling   paid notes carry "contenido patrocinado" and rel=sponsored
            free notes are marked as a press note and carry rel=nofollow
Editorial   publishing is an editorial decision and is not guaranteed
Refused     gambling, adult content, partisan politics, promises of return,
            unsupported health claims, link-only texts, anything unlawful
Process     send the text here; a confirmation request goes to the sender;
            the reply starts the review; decisions, invoices and the
            published URL arrive by email in the same thread
```

**Status refusal** (`estado_nota`): an unknown ticket returns `{"estado": "unknown", "mensaje": "Ticket desconocido o caducado."}` rather than an error, so an agent can tell a user their ticket is invalid or expired without retrying.

### One detail recorded as measured

`language: "en"` translates the topics, the "what we accept" prose and the criteria language of the publications, but the `accepts` body sent back in the same object stayed in Spanish. The parameter is a partial translation, not a switch, and a guide that called it a localisation would be wrong.

## Where It Stops

- **Three Spanish-language outlets.** The topics and the audience are Spanish business media. An English release can be submitted; it competes in a Spanish-language editorial queue.
- **Editorial, not placement.** Nothing here guarantees publication, and nothing here buys a guarantee. Paid packages buy volume of submissions, and paid coverage is labelled as sponsored content with `rel=sponsored`.
- **A free tier with a ceiling.** Five notes per sender across the whole network, then packages. The counter belongs to the sender address, not to the agent.
- **No analytics.** No impressions, no opens, no referral data - the outcome is a status field and, if it lands, a URL.
- **One submission per call, one ticket per submission.** There is no batch and no scheduling.
- **No money movement.** No purchase tool exists; invoicing is by email.

### What did the agent not do, and why?

`enviar_nota` was left undriven. It writes to a human editorial queue and sends an outbound confirmation email to whatever address it is given, and this catalogue's rule for a human-reviewed intake is to read the contract and stop. The three read tools were enough to establish the terms, the prices, the refusals and the process from the server's own answers.

### How is this different from the press-release distributor already catalogued?

[Comunicate MCP](/hermes/mcp/servers/external/comunicate-mcp) is a distribution marketplace: it searches a catalogue of publications, prices a placement and orders it, with the spend behind a switch. This server is the receiving desk of one network: no catalogue, no per-placement price, a free allowance and an editorial decision. One is a shop, the other is a submission window, and an operator doing PR in Spain needs the second.

### Should an agent write the release itself?

The server does not care how the text was produced, and it does not offer a drafting tool. The value it adds is the contract: allowance, labelling, refusals and status. Everything a model writes still has to survive an editor who publishes nothing for money alone.

## Catalogue Position

Press release distribution had one owner here, and it is a paid placement marketplace. This is the second press entry and the first editorial desk - a free allowance, a sponsored-content label, `rel=sponsored` on paid links, and no tool that can spend. It earns its slot on the receiving half of the job rather than on the category.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Comunicate MCP - Press Release Distribution for Agents](/hermes/mcp/servers/external/comunicate-mcp)
- [MCP Server Discovery - November 21, 2026 (Midday)](/hermes/mcp/sweeps/sweep-november21-2026-midday)
