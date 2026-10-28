---
title: "SendNF MCP - Brazilian Tax Invoices From an Agent"
description: "Thirty-six tools that look up a CNPJ, price a service code, preview and issue NFS-e and NFC-e, and hold any draft for a person to approve."
category: Finance / Tax and Invoicing
stars: n/a (commercial, nt_test_ sandbox key and nt_live_ production key)
added: 2026-10-27
source: "live probe on https://api.sendnf.com/mcp returning HTTP 401 with its own refusal body, the published tool table in the sendnf/sendnf-mcp manifest repository read at 03:16Z on 2026-10-28, the vendor page at sendnf.com/mcp and the chatmcp/mcpso submission #6267 filed 2026-10-28T02:31:59Z"
relevance: ★★★
tags: [invoicing, tax, brazil, nfse, nfce, fiscal, cnps, approval, streamable-http, latin-america]
last_updated: "2026-10-27"
---

# SendNF MCP

**A tax invoice is the one document a business cannot let an assistant improvise, and SendNF is the first server in this catalog that puts the whole issuance path behind a draft that a person has to release.**

```
Server type:  Remote (Streamable HTTP, no session)
Endpoint:     https://api.sendnf.com/mcp
Auth:         Bearer key, nt_test_ for homologation, nt_live_ for production
Tools:        36, read and write annotated per tool in the vendor table
Documents:    NFS-e (services) and NFC-e (consumer goods)
Jurisdiction: Brazil, national NFS-e layout plus municipal providers
Built by:     SendNF (sendnf.com)
```

A probe without a key returns HTTP 401 with a Portuguese body that names the header it wants: `Envie uma chave de API valida em Authorization`. That is the correct shape for a fiscal system. The evidence below is the vendor's published tool table, which is unusually complete for a product whose code is private, and the sandbox prefix is the part worth understanding before anything is wired.

## Why This Matters for Operators

In Brazil the invoice is not an accounting artefact produced after the fact. It is the event that creates the tax liability, and it is transmitted to a municipal or state authority that can reject it, block it or accept it with a delay. A business that issues a hundred service notes a month does that in a portal, one form at a time, and the rejections arrive as codes.

What makes this server different from the other document tools in the catalog is the ordering of the steps. The key prefix decides whether anything is real: an `nt_test_` key is homologation and carries no fiscal value, an `nt_live_` key issues into production. Before either, `preview_nfse` validates a note against the official layout or the municipal provider, computes the totals including IBS and CBS, and returns the problems with guidance rather than a generic error. `issue_nfse` then transmits and waits up to about twenty-five seconds for one of four answers: authorized, rejected, blocked or pending.

## The Approval Primitive

The tool that makes this safe to hand to an agent is `create_note_draft`. It builds the note, validates it exactly as the issuance path would, and leaves it in `pending_approval` with an `approval_url` and, on a service note, a preview PDF that carries no fiscal value. The vendor states that the draft waits for a human **even when the lock is switched off**, which is the difference between a policy and a default. A rejected draft returns `rejection_reason` so the agent can rebuild it, and an undecided draft expires after seven days.

Correction has its own path rather than a delete. `get_substitution_draft` reports whether a service note can be corrected by substitution, and returns the original body to edit, which `substitute_document` then reissues pointing at the original. `cancel_document` cancels the whole note at the authority, and `get_document_events` returns the timeline of what happened to it, which is the version an operator can explain to a client.

## The Rest of the Surface

Company setup is handled by tools rather than by a support ticket. `lookup_cnpj` pulls the public Receita record (legal name, address, CNAE, Simples or MEI status), reports whether the municipality uses the national system or its own, and suggests service codes from the CNAE. `search_service_codes` searches the national LC 116 list for the six-digit `cTribNac` and the NBS code, and `get_service_code` returns the official description. `import_invoice` reads the XML of a note the company already issued and completes the setup from it: registrations, regime, service code, NBS, ISS rate, municipal code and the numbering series. `upload_certificate` takes the A1 certificate as base64 plus its password, and `create_onboarding_link` generates a short link so the company owner completes the certificate step themselves rather than sending a `.pfx` through chat.

Operating tools: `account_overview` reports whether the key is test or production, the plan, monthly usage and whether the key is restricted to one company. `usage_by_company` breaks notes down by type, status and environment with a billing estimate. `go_live_status` reports the checklist, whether a test note has passed, and the timestamp the company was enabled for real issuance. `create_export` builds a zip of XML and PDF per company and month plus a `notas.csv` or `notas.xlsx` with number, date, counterparty, CPF or CNPJ, value, ISS, withholdings, status and key, and the download URL is signed for one hour with the archive kept seven days. `create_share_link` issues a read-only link for an accountant with validity and revocation, and `list_share_links` shows last access and access count.

## Limits Worth Recording

- **Brazil only, and the vendor writes in Portuguese.** Every tool description and every rejection the server returns is Portuguese, so the agent reading it needs Portuguese comprehension or a translation step. The national layout does not cover every municipality, which is why `lookup_cnpj` reports which system a city uses.
- **Setup is not self-service.** A1 certificate, municipal registration and the city hall password are real credentials that a company must supply, and `how_to_get` documents where each one comes from rather than fetching them.
- **No call was executed in this pass.** Without a key the server answers 401, so the tool count and the approval semantics are the vendor's published table and not observed behaviour. The 401 body is the only live evidence recorded here.
- **The repository is a manifest.** `sendnf/sendnf-mcp` states plainly that the product code is private and that the repository holds only the manifest, examples and the tool list, so there is nothing to review before trusting it.
- **Fiscal liability does not transfer.** An accepted note creates a real obligation. The approval step protects against an agent issuing one, not against a person approving a wrong one.

## Wiring It Up

```json
{"mcpServers": {"sendnf": {
  "type": "http",
  "url": "https://api.sendnf.com/mcp",
  "headers": {"Authorization": "Bearer nt_test_YOUR_KEY"}
}}}
```

Start on a test key, run `preview_nfse` until it validates clean, then issue one test note and read `go_live_status` before the key is swapped for a production one.

## FAQ

### Can an agent issue a real invoice without a person?

Through `issue_nfse` on a live key, yes, which is why the draft path exists. `create_note_draft` holds the note in `pending_approval` with an approval link and does so even when the account lock is off, and the seven-day expiry means an unattended draft fails closed rather than issuing late.

### What is the difference between the sandbox and production keys?

The prefix on the key. An `nt_test_` key issues into homologation with no fiscal value and an `nt_live_` key issues into production, and `account_overview` reports which mode the key is in so the agent can state it rather than assume it.

### Does it handle corrections?

Yes, by substitution. `get_substitution_draft` returns whether a service note can be corrected and the body to edit, `substitute_document` issues the replacement pointing at the original, and `cancel_document` cancels outright. `get_document_events` returns the timeline of either path.

### Can it be used outside Brazil?

No. The tools are built on the national NFS-e layout, the LC 116 service list, CNPJ and municipal systems, so an operator outside Brazil has nothing to connect it to.
