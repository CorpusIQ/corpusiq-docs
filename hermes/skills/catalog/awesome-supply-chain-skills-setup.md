---
title: "Supply Chain Skills - Operations Research Setup"
description: "kishorkukreja/awesome-supply-chain: 2.1K combined installs; 133 operations research skills for inventory, routing and sourcing"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/awesome-supply-chain-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "supply chain", "operations research", "inventory", "logistics"]
---

# Supply Chain Skills - Setup Guide

**Source:** [kishorkukreja/awesome-supply-chain](https://www.skills.sh/kishorkukreja/awesome-supply-chain) via skills.sh - 2.1K combined installs across 20 indexed listings (2,137 exact); first seen 2026-11-10 (Nov 10, 2026 sweep)
**GitHub:** 96 stars, MIT license, `main` branch, last pushed 2026-10-06, 133 `SKILL.md` files under `skills/<name>/`, with `evals/`, `verticals/` and plugin metadata for Claude Code and Codex alongside
**Category:** Supply chain and operations research: inventory, procurement, forecasting, routing, warehouse and vertical playbooks
**Quality Tier:** 🟡 Solid with caveats - nineteen of twenty sampled listings pass all three scanners and the one exception is a single Snyk warning, but the install base is thin and the skills are advisory rather than tool-backed.

This repository is a curated supply chain library that grew a skill set. The README describes research papers, implementations and libraries organised by industry vertical, and states that 133 agent skills are included in the open Agent Skills format with plugin metadata for Claude Code and Codex. The skill set is the part that matters for an agent, and it is unusually wide for a vertical collection: planning, operations research, inventory, warehouse, transportation, manufacturing and domain expertise.

Where most vertical skill sets are generated from a product's documentation, these read as practitioner playbooks. A skill in this repository does not call an API. It states the decision, the inputs that decision needs, the method that applies, and the trade-offs that make one answer better than another. That makes the set useful for framing and for structured analysis, and it means nothing here computes anything you did not supply.

The 20 indexed listings are the general-purpose core: inventory and replenishment, procurement and sourcing, forecasting, routing and freight, and four industry verticals. The tree carries 113 more, including the operations research topics the README highlights: bin packing, cutting stock, facility location and travelling salesman.

## Installation

The README documents the CLI route with two forms. To browse first:

```bash
npx skills add kishorkukreja/awesome-supply-chain --list
```

To install a named skill to specific agents:

```bash
npx skills add kishorkukreja/awesome-supply-chain \
  --skill supply-chain-decision-to-delegation \
  --agent codex \
  --agent claude-code
```

Claude Code users can take the whole plugin instead:

```text
/plugin marketplace add kishorkukreja/awesome-supply-chain
/plugin install supply-chain-skills@awesome-supply-chain
```

The README also points at `skills/README.md` for the full skill documentation and `docs/agent-installation.md` for agent-specific instructions, which is where a per-client layout would be if your client is not Claude Code or Codex.

The plugin route is the practical choice. The skills are designed to compose, and installing one at a time means the agent has the sourcing skill without the supplier-selection skill it references. Take the bundle unless you have a specific reason not to.

## What It Provides

Eight listings clear the 100-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| pharmacy-supply-chain | 211 | Pharmacy operations: medication distribution, stock policy and the compliance constraints around both. |
| procurement-optimization | 171 | Allocates orders across suppliers and determines optimal purchase quantities under constraints. |
| lean-manufacturing | 159 | Applies lean principles: waste elimination, flow, and continuous improvement programs. |
| supplier-selection | 152 | Evaluates and qualifies suppliers, including scoring and selection frameworks. |
| inventory-optimization | 128 | Sets inventory levels, safety stock and reorder points to minimise holding and stockout cost together. |
| replenishment-strategy | 116 | Designs replenishment policies and the parameters that drive them. |
| retail-replenishment | 102 | Store-level replenishment: reorder points per store and the allocation behind them. |
| food-beverage-supply-chain | 102 | Perishable supply chains: shelf life, food safety constraints and waste. |

The remaining 12 indexed listings range from 75 to 92 installs: `demand-forecasting` (92), `route-optimization` (88), `freight-optimization` (87), `pharmaceutical-supply-chain` (86), `workforce-scheduling` (85), `electronics-supply-chain` (84), `supply-chain-analytics` (82), `warehouse-design` (81), `optimization-modeling` (80), `vehicle-routing-problem` (80), `maintenance-planning` (76) and `strategic-sourcing` (75).

The install counts are tight, between 75 and 211 across the whole table. There is no breakout skill and no clear entry point by adoption, which is consistent with a set that gets installed as a bundle. The verticals lead on adoption, which is a mild signal that practitioners arrive with an industry problem rather than a technique.

## Why This Matters for Hermes Agents

Operations research is exactly the kind of work where an agent produces a confident answer with no method behind it. Ask a general assistant how much safety stock to hold and you get a formula with invented service-level assumptions. Ask what reorder point a store needs and you get a number with no lead-time distribution behind it.

These skills invert that. Each one opens from the decision, names the inputs the decision requires, and states which method applies and when. The agent still needs your numbers, but it can no longer skip the step of establishing what the numbers are.

The second contribution is vocabulary that survives a handover. A purchasing manager and an agent can both use "reorder point" and mean different things. A skill that defines it as lead-time demand plus safety stock, with the service level as an explicit parameter, makes the disagreement visible before it becomes a wrong order.

The honest limitation is that this is knowledge, not tooling. Nothing here reads your ERP, and nothing computes a forecast from your history. The value is in the framing and the structure, and the agent still needs a data path that you supply.

## Usage

| You say | What happens |
|---|---|
| "How much safety stock should we hold on this SKU?" | Inventory optimization frames the decision, asks for demand variability and lead time, and states the service-level trade-off before giving a level |
| "Which supplier should we use for this line?" | Supplier selection runs a scoring framework over the criteria you supply, and names what it could not evaluate |
| "Should we hold stock in three warehouses or one?" | Warehouse design and inventory optimization work the facility and holding-cost trade-off together rather than in isolation |
| "Our food waste is too high" | The food and beverage vertical addresses shelf life and perishability, which change the replenishment policy rather than the forecast |
| "Plan routes for next week's deliveries" | Route optimization frames the problem as a vehicle routing variant and states which constraints it needs before solving |
| "Why does our forecast keep missing?" | Demand forecasting separates method error from data error and asks which regimes the history covers |
| "We need a sourcing strategy for this category" | Strategic sourcing builds the category approach: spend analysis, supply risk and the sourcing event that fits |

## Verification

Each listing resolves to a raw `SKILL.md` one directory below `skills/`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/kishorkukreja/awesome-supply-chain/main/skills/inventory-optimization/SKILL.md | head -5
```

It should open with frontmatter holding `name: inventory-optimization` and a description beginning `When the user wants to optimize inventory levels`, followed by the delimiter and the instruction body. The descriptions in this repository are trigger phrases rather than summaries, which is why they all start with "When the user wants to".

After an install, confirm the skill landed as a directory holding `SKILL.md`:

```bash
ls -d ~/.claude/skills/*/ | head -20
test -f ~/.claude/skills/inventory-optimization/SKILL.md && echo ok
```

The plugin route keeps its bundle in the plugin directory, so use the `/plugin` listing for that install and the directory check for the CLI route.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pharmacy-supply-chain | Pass | Pass | Pass |
| procurement-optimization | Pass | Pass | Pass |
| lean-manufacturing | Pass | Pass | Pass |
| supplier-selection | Pass | Pass | Pass |
| inventory-optimization | Pass | Pass | Pass |
| replenishment-strategy | Pass | Pass | Pass |
| retail-replenishment | Pass | Pass | Pass |
| food-beverage-supply-chain | Pass | Pass | Pass |
| demand-forecasting | Pass | Pass | Pass |
| route-optimization | Pass | Pass | Pass |
| freight-optimization | Pass | Pass | Pass |
| pharmaceutical-supply-chain | Pass | Pass | Pass |
| workforce-scheduling | Pass | Pass | Pass |
| electronics-supply-chain | Pass | Pass | Pass |
| supply-chain-analytics | Pass | Pass | Warn |
| warehouse-design | Pass | Pass | Pass |
| optimization-modeling | Pass | Pass | Pass |
| vehicle-routing-problem | Pass | Pass | Pass |
| maintenance-planning | Pass | Pass | Pass |
| strategic-sourcing | Pass | Pass | Pass |

Agent Trust Hub and Socket pass all 20 listings, and Snyk passes 19 with a single warning on `supply-chain-analytics`. That is the cleanest verdict set in this sweep and the reason the tier note is about the install base rather than the code.

The clean scanning is easy to explain: these skills are prose. They contain no executable payload, no network calls and no credential handling, so there is little for a scanner to object to. The corresponding caution is that a clean scan says nothing about whether the advice is right for your business.

Two skills touch compliance territory. `pharmacy-supply-chain` and `pharmaceutical-supply-chain` describe regulated operations, and regulatory specifics differ by jurisdiction and change over time. Treat their compliance content as a checklist to verify, not as authority.

## Limitations

- Snapshot data, verified 2026-11-10: 2,137 combined installs across 20 indexed listings; 96 GitHub stars; MIT license; last pushed 2026-10-06. Counts drift over time.
- The skills.sh source page renders 20 listings while the README counts 133 skills and the tree carries 133 `SKILL.md` files. The 20 here are the general-purpose core; the operations research topics named in the README, including bin packing, cutting stock and facility location, fall outside the rendered set.
- Install counts are thin across the whole table, between 75 and 211. There is no high-adoption skill to point at as validated.
- Nothing in this set reads data or runs an optimisation. The skills are framing and method; the numbers, the solver and the data pipeline are yours.
- The repository also carries research papers, implementations and libraries. Those are not skills, they are not installed by the CLI, and the README does not always separate the two clearly.
- Compliance content in the pharmacy and pharmaceutical skills is jurisdiction-dependent and should be verified against the current regulation rather than used as written.

## Related

- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)
- [Metabase Skills - BI and Dashboard Agent Suite](/hermes/skills/catalog/metabase-skills-setup)

## Pro Tips

- Install the plugin rather than individual skills. The skills cross-reference each other, and a lone sourcing skill without supplier selection produces a recommendation with no scoring behind it.
- Open with `supply-chain-decision-to-delegation`, the skill the README leads with. It turns a vague operational complaint into a scoped decision and is allowed to conclude that a process problem must be fixed before any AI should touch it.
- Feed it real constraints. These skills will not invent a lead-time distribution for you, and an agent that asks for one is doing the job correctly.
- Use the vertical skills as the entry point if you have an industry problem. The retail, food and beverage, electronics and pharmaceutical skills carry constraints that the general skills do not.
- Pair with a data tool. The framing is only useful next to numbers, and an agent with the analytics skills installed can query them in the same session.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
