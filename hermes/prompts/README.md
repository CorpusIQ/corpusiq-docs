# Prompts library

The fastest way to learn CorpusIQ is to fire prompts that exercise the skills
engine. Each file below is a category. Each prompt is copy-pasteable into
Claude or ChatGPT.

Every prompt lists:

- **What this does** — plain English explanation.
- **Connectors used** — which integrations need to be authenticated.
- **Behind the scenes** — the skill runbook id, when one exists. You don't
  need to know this, but if you're curious how CorpusIQ chose its approach,
  the name is here.
- **Sample answer shape** — what you'll get back (a description of structure,
  not invented numbers).

## Categories

| File | What's in it |
|---|---|
| [executive-summary.md](executive-summary.md) | "How healthy is my business?" type prompts |
| [revenue-and-finance.md](revenue-and-finance.md) | Cash, P&L, overdue invoices, MRR, runway |
| [marketing-roas.md](marketing-roas.md) | True CAC, ROAS, channel attribution, ad spend audit |
| [email-and-sms.md](email-and-sms.md) | Klaviyo, Mailchimp, PostScript, list health, campaign perf |
| [customer-and-crm.md](customer-and-crm.md) | Pipeline health, stalled deals, churn risk, customer search |
| [ecommerce-ops.md](ecommerce-ops.md) | Orders, inventory, top SKUs, marketplace sellers |
| [seo-and-content.md](seo-and-content.md) | Search Console, Semrush, YouTube, ranking drift |
| [productivity-and-files.md](productivity-and-files.md) | Inbox triage, calendar, file search, missed emails |
| [multi-source.md](multi-source.md) | The moat — prompts that fire across 3+ connectors |

## Tips

- **Don't over-engineer the prompt.** "How are sales this month?" works.
  "Query my Shopify orders table aggregated by week filtered by status=paid"
  also works but is the long way around.
- **More connectors = better answers.** The executive snapshot is sharper when
  it has 6 sources to triangulate from than when it has 2.
- **If the answer is wrong**, ask CorpusIQ to show its work: "What sources
  did you use? Show me the raw numbers." It will.

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
