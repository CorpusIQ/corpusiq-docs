# Security Policy

## Reporting a vulnerability

This repository is public, so please do not open a public issue for a security
problem.

**Private vulnerability reporting is enabled on this repository.** Use the
[Report a vulnerability](https://github.com/CorpusIQ/corpusiq-docs/security/advisories/new)
form under the Security tab. The report stays private between you and the
maintainers until a fix is ready and a disclosure date is agreed.

You can also email **security@corpusiq.io**, which is the contact published on
[the CorpusIQ security page](https://www.corpusiq.io/docs/security).

We aim to acknowledge reports within 24 hours. Please give us a chance to
address the issue before any public disclosure.

## Scope

This repository is the **documentation** site for CorpusIQ and the Hermes
ecosystem. It contains Markdown, build configuration, and deployment scripts.
It does not host the CorpusIQ product.

Reports that belong here:

- A secret or credential committed to this repository
- A security claim on a published page that is inaccurate or overstated
- A vulnerability in this site's build, deployment, or dependency chain
- A way to inject content into a served page

Reports about the CorpusIQ product, the MCP endpoint, connector
authorization, authentication, or customer data belong with the security team
at **security@corpusiq.io**, not in this repository. If you are unsure, use the
private form above and we will route it.

## What to include

- The affected URL, file, or path
- What you expected and what actually happened
- Reproduction steps, with the exact request or input where you have one
- Your assessment of impact, and whether you intend to publish

## Out of scope

- Findings that require a compromised device or an already stolen credential
- Automated scanner output with no reproducible impact
- Best practice suggestions with no demonstrated effect (for example, a missing
  header with no exploit path). These are still welcome as a normal issue.

## Our side of the deal

We will confirm the report, tell you whether we consider it in scope, keep you
informed while we fix it, and credit you in the fix commit or page if you want
credit. We will not pursue legal action against researchers who report in good
faith and follow this policy.
