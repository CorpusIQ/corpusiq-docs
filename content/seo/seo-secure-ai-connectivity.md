# Secure AI Data Connectivity — Operation-Level Permissions

The first question when connecting business data to AI is reasonable: "What can each tool change?"

The honest answer belongs in each advertised operation's permissions, not in one product-wide slogan.

## The permission model

CorpusIQ marks external-source retrieval tools read-only. Write-capable connector operations and CorpusIQ control-plane tools are separately named and annotated so clients and reviewers can distinguish retrieval from mutation.

Provider authorization varies by connector. OAuth is used where supported; other connectors use encrypted credentials or restricted roles. The effective permission remains bounded by both the provider grant and the specific advertised tool.

## What else matters for security

**Provider authentication:** CorpusIQ uses provider OAuth where supported and stores required credential-based connector secrets encrypted. Manage provider authorization through the relevant provider controls; provider-side timing follows each provider's lifecycle.

**Scoped retention:** Direct MCP does not retain raw customer files or full connector response payloads; operational logs may persist for up to 30 days.

**Disclosed processors:** CorpusIQ runs on Microsoft Azure and uses the selected AI client to answer the request. Each provider's published data policy applies to its part of the flow.

**CASA Tier 2 certified:** CorpusIQ completed the DEKRA-assessed CASA Tier 2 process. The certification does not replace operation-level permission review.

**SOC 2 aligned:** Security controls are mapped to the framework; formal SOC 2 Type II certification is not claimed.

## The questions to ask any AI data platform

| Question | Why it matters |
|----------|---------------|
| Are retrieval and write operations separately named and annotated? | Prevents a blanket label from hiding mutation capability |
| What data is retained, indexed, or logged? | Distinguishes request payloads from operational records |
| How is authentication handled for each provider? | OAuth, restricted credentials, and roles have different contracts |
| What has been independently assessed? | Certification scope should match the claim being made |
| How do disconnect and provider revocation differ? | CorpusIQ and provider-side lifecycles are separate |
| Which processors receive request context? | The complete flow matters for policy review |

## The bottom line

Secure connectivity needs operation-level permissions, truthful retention disclosures, provider-specific authorization, and independently assessed controls. Shorter slogans are easier to print. They are also where the trouble starts.

---

*CorpusIQ: 40+ connectors, operation-level permissions, scoped retention, and CASA Tier 2 certification. [corpusiq.io](https://www.corpusiq.io)*
