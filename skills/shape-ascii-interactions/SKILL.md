---
name: shape-ascii-interactions
description: Shape or audit information architecture, task flows, interaction logic, and ASCII UI/state contracts against explicit target users and scenarios. Use to derive interactions from confirmed requirements or evaluate existing/candidate flows for concept, execution, evaluation, and consequence gaps. Do not use for visual styling or final specification packaging.
---

# Shape ASCII Interactions

Derive navigable product structure and user-visible behavior from confirmed outcomes and paths, or audit supplied interactions against an explicit target-user model. Confirm shaped ASCII interaction units in dependency order.

## Load references progressively

- Read [references/information-architecture-and-task-flows.md](references/information-architecture-and-task-flows.md) before deriving `FUNC`, `IA`, `NAV`, or task flows.
- Read [references/interaction-logic-principles.md](references/interaction-logic-principles.md) before choosing surfaces, dialogs, feedback, or recovery behavior.
- Read [references/model-interface-gap-review.md](references/model-interface-gap-review.md) when shaping material interactions or auditing an existing/candidate flow against target-user expectations.
- Read [references/ascii-interactions.md](references/ascii-interactions.md) before drawing flows or `UI/STATE` frames.
- Read [references/progressive-ascii-confirmation.md](references/progressive-ascii-confirmation.md) before presenting or persisting detailed ASCII UX.

Use `assets/ascii-ui-supplement-template.md` only for a requested standalone supplement or when completing missing ASCII behavior in an existing document.

## Modes and input gate

- **Shape mode:** require a confirmed `DEC-BASELINE` and confirmed material `FLOW-HP/DEC-HAPPY`, or clearly label the affected interaction work provisional. Do not silently turn an unresolved path decision into a page or control choice.
- **Audit mode:** require an explicit `ROLE`, `SCN`, and the `FLOW/INT` under review; require applicable `UI/STATE` only for representation review. A missing target role or scenario blocks the audit. Missing confirmation or user evidence makes the result Provisional rather than silently validated.

## Shape workflow

1. Derive user-recognizable `FUNC` capabilities from confirmed stories and paths.
2. Choose starting surfaces, product topology, `IA`, and `NAV` based on tasks and objects rather than defaulting to dashboards or lists.
3. Model primary, alternate, failure, exit, recovery, cross-role, and asynchronous `FLOW` behavior.
4. Derive each `INT` chain: trigger → context → action → system response → feedback → next state/recovery.
5. Run flow-model fit review against each material target `ROLE/SCN`; revise avoidable concept, execution, evaluation, or consequence gaps before detailed UI.
6. Create compact ASCII hierarchy/flow overviews and focused `UI/STATE` frames for every user-visible interaction behavior.
7. Cover default, loading, empty, success, error, permission, partial-success, stale/concurrent, and recovery states when applicable.
8. Run representation-model fit review; persist coverage and material `UXGAP` findings, keeping severity separate from evidence strength.
9. Record viewport, input, accessibility, density, and responsive constraints that ASCII cannot prove.
10. Order confirmation units by dependency, present one coherent unit at a time, offer modification or confirmation, then persist `DEC-ASCII-###` atomically. Do not confirm an affected slice while a Critical `UXGAP` remains open.

## Audit workflow

1. Inventory the supplied `ROLE`, `SCN`, user-model evidence, `FLOW/INT`, and any `UI/STATE` without assuming they are confirmed or correct.
2. Stop as Blocked when the target role or scenario is missing; otherwise label evidence-bounded limitations and continue Provisionally when needed.
3. Run flow-model fit review on the supplied `FLOW/INT` without deriving unrelated pages, controls, or requirements.
4. Run representation-model fit review only for supplied `UI/STATE`; otherwise record it Not applicable with the concrete scope reason.
5. Record coverage and material `UXGAP` findings, severity, evidence, affected IDs, and recommended resolution. Do not create pass-only gap rows.
6. Report whether the result is expert-reviewed, owner-confirmed, user-validated, or provisional. Do not rewrite or confirm the source artifacts unless the user separately requests shaping or correction.

## Output contract

In Shape mode, produce canonical `FUNC`, `IA`, `NAV`, `FLOW`, `PAGE/SUB` when needed, `INT`, `UI/STATE`, related `UXH`, model-fit coverage, material `UXGAP`, an ASCII confirmation queue, and `DEC-ASCII` records. In Audit mode, produce evidence-bounded coverage and findings without silently rewriting or confirming source artifacts. Maintain traceability to `ROLE/SCN/REQ/TASK/US/JS/FLOW-HP`.

Stop before exhaustive cross-cutting specifications, acceptance criteria, delivery-profile packaging, and final handoff unless the delivery skill is invoked.
