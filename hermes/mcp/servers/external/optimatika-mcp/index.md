---
title: "Optimatika MCP - Proven-Optimal Optimisation Solver"
description: "Solves linear, quadratic and mixed-integer models keylessly and returns each variable's value, with the solver's own limits stated."
category: "Business Operations / Optimisation"
stars: "n/a (hosted service; docs at optimatika.se/optimisation-service)"
added: 2026-11-19
source: "the mcp.so submission queue entry #7654 filed 2026-11-19T10:52:09Z, a keyless handshake and full tools/list on 2026-11-19, six tools/call requests across two of the three tools, and the official MCP registry record"
relevance: ★★★
tags: [optimisation, linear-programming, milp, operations-research, solver, production-planning, scheduling, remote, keyless]
last_updated: "2026-11-19"
---

# Optimatika MCP

**Most numbers an assistant produces are estimates. A solver does not estimate: it either proves an answer optimal or says it could not.**

That distinction matters more than it sounds. A production mix, a delivery plan, a shift rota and a capital allocation are all the same shape of question - a quantity to maximise or minimise, limited by constraints the business already knows - and a language model's answer to that question is a guess wearing the clothes of a recommendation. An optimisation solver turns it into arithmetic with a certificate attached: `state: OPTIMAL`, the objective value, and the value of every decision variable by the name the modeller gave it.

This is the first entry in this catalog for that class. There is no operations-research solver here, no linear-programming endpoint, and nothing else that returns a proven optimum rather than a plausible one.

```text
Server type:   remote Streamable HTTP (hosted, stateless, no session id issued)
Endpoint:      https://service-api.optimatika.se/optimisation/mcp
Server:        optimatika-optimisation-service, build a74468c, protocol 2025-06-18
Auth:          none. The public instance needs no account and no key
Tools:         3          solve · translate · environment
Solvers:       LP-JVM · QP-JVM · MILP-JVM · MIQP-JVM   (ojAlgo, JVM)
Limits:        max 1,000 variables/constraints · suffice 30 s · abort 60 s
Registry:      se.optimatika/optimisation-service
Docs:          https://www.optimatika.se/optimisation-service/docs/#mcp
Queue:         mcp.so #7654, filed 2026-11-19T10:52:09Z
```

## What the server says about itself

The `initialize` response carries an instructions string, and it is the cleanest statement of what the product is that a vendor card cannot give you. Quoted as returned:

> Solves linear, quadratic and mixed-integer optimisation models (LP, QP, MILP, MIQP) with deterministic solvers - simplex, interior point, branch and bound - so an optimal result is a proven one. Write the model in LP format and call `solve`; the result gives each variable's value by name. Call `environment` for this server's size and time limits.

The phrase worth keeping is **"so an optimal result is a proven one"**. `solve` does not return a best-effort figure with a confidence interval. It returns a state machine value, and the difference between `OPTIMAL`, `FEASIBLE` and `INFEASIBLE` is the whole point.

## What was driven, and what came back

Eight calls, no account and no key. Six of them carry this guide, and every figure below reproduces by hand.

**The limits, asked rather than assumed.** `environment` with no arguments returned the instance's own contract: a Polar shared instance with **no licence key**, which means **ojAlgo solvers only**, capped at **1,000** variables or constraints (whichever is larger), with a **30-second** point after which a solve returns the best solution found so far as `FEASIBLE` unless it is proven optimal, and a hard **60-second** abort. It also reports `nativeSolvers: false`, which is the honest version of "these are JVM solvers, not commercial Cplex or Gurobi". A planner can size a model against those numbers before writing it.

**A two-variable problem whose answer you can check in your head.** Maximising `3x + 2y` subject to `x + y <= 4`, `x <= 2`, `y <= 3` returned `OPTIMAL`, objective **10.0**, `x = 2.0`, `y = 2.0`. Both constraints bind, and 3·2 + 2·2 = 10.

**A production-mix problem with two shared resources.** Maximising `40A + 30B` under `2A + B <= 100` labour and `A + 2B <= 80` machine hours returned `OPTIMAL`, objective **2,200**, `A = 40`, `B = 20`. Labour reads 80 + 20 = 100 against its ceiling of 100, machine reads 40 + 40 = 80 against 80: both resources are exhausted, which is the expected shape of a two-constraint maximum.

**A minimisation, to prove the direction is not hard-wired.** Minimising `12x + 8y` subject to `4x + 2y >= 12` and `x + y >= 5` returned `OPTIMAL`, objective **44**, `x = 1`, `y = 4`. From the corner set (0, 6) costs 48, (1, 4) costs 44, (5, 0) costs 60 - so 44 is the minimum, and the tool found the one corner that undercuts the naive "satisfy the first constraint only" answer.

**An integer problem, to check the `General` section is honoured.** Maximising `5 desks + 4 chairs` under `3 desks + 2 chairs <= 12` wood and `1 desk + 1 chair <= 5` labour, with both variables declared `General`, returned `OPTIMAL`, **22**, `desks = 2`, `chairs = 3`. Wood reads 6 + 6 = 12 and labour reads 5, both binding; the relaxation's answer and the integer answer happen to coincide here, and the values came back as whole numbers rather than `2.14`.

**A refusal, which is more informative than a success.** Maximising `x + y` subject to `x + y <= 1` *and* `2x + 2y >= 5` describes an empty region. The tool returned `state: INFEASIBLE`, `optimal: false`, `feasible: false`, with the note: *"No solution satisfies all the constraints: the model is infeasible - or, occasionally, unbounded."* The caveat is the vendor being straight about a solver's real limitation: a numerically infeasible reading and an unbounded model are not always separable from the status alone.

**`translate` refused an incomplete call rather than guessing.** Called with a model and `to: "mps"` but no `from`, it returned `isError: true` and the string *"'from' and 'to' are required, each LP, MPS or EBM."* Both ends of a conversion are mandatory, which is the right shape: a tool that inferred the input format from the text would be guessing about the thing you are asking it to be precise about.

## The three tools

| Tool | Arguments | What comes back |
|---|---|---|
| `solve` | `model` in LP format | `state`, `optimal`, `feasible`, the `objective`, and every variable's value by name |
| `translate` | `model`, `from`, `to` (each LP, MPS or EBM) | the same model rewritten in the other file format |
| `environment` | none | the instance's licence, size limit, time suffices and aborts, and the solver list |

## Where this belongs in a business workflow

The cases that pay for it are the ones where a plan has to be defended. A production mix that a planner has to take to a plant manager. A delivery route set that has to survive a fuel-price argument. A roster that has to satisfy a labour agreement. A capital allocation across projects with a budget ceiling and a minimum-return floor on each.

In all four, the assistant's job stops being "here is roughly what I would do" and becomes "here is the model, here is the optimum, and here is what binds". The binding constraint is usually the actual finding: the answer to "why can't we make more" is a named row in the model, not an opinion.

## Questions worth asking before you build on it

### Does it cost anything to call?

Not on the public instance. `environment` reports a Polar shared instance with **no licence key**, which is why the solver list is JVM-only and the ceiling is 1,000 variables or constraints. A licensed deployment is the vendor's commercial product; the endpoint this guide measured is the free shared one.

### Can it handle a real planning model, or only textbook ones?

A thousand variables or constraints is a genuine limit and it is stated rather than discovered. Many operational models - a weekly production plan across a dozen products and four resource types, a rota for one site - fit inside it. A multi-site network design does not, and the honest answer there is that this instance will return a `FEASIBLE` answer at 30 seconds rather than a proof, or refuse beyond 1,000.

### What happens when the model is wrong?

You get `INFEASIBLE` and a note that names the two causes it cannot separate. That is the readable failure mode: an assistant that gets `INFEASIBLE` can tell a user their constraints contradict each other, instead of inventing a solution that quietly violates one of them.

### Is the answer auditable?

Yes, and that is the reason to prefer it over asking a model directly. The model text is itself the record - the objective, the constraints and the bounds - and the response names each variable. A reviewer can re-solve the same text and get the same value, which is not true of a paragraph of prose.

## Gap recorded

`translate` was exercised only through its refusal path: no successful LP-to-MPS conversion was driven, so the fidelity of a round trip is unverified. A trial should convert a model, re-solve the converted file and confirm the objective matches, since a format conversion that silently drops a bound would be the most damaging failure this tool could have. `solve` was driven on LP and MILP only; QP and MIQP are offered by the server and were not exercised.
