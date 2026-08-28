---
name: shape-ascii-interactions
description: Turn confirmed requirements and happy paths into information architecture, task and decision flows, interaction logic, and progressively confirmed ASCII UI/state contracts. Use for UX structure and behavior, not visual styling or final specification packaging.
---

# Shape ASCII Interactions

Derive navigable product structure and user-visible behavior from confirmed outcomes and paths, then confirm ASCII interaction units in dependency order.

## Load references progressively

- Read [references/information-architecture-and-task-flows.md](references/information-architecture-and-task-flows.md) before deriving `FUNC`, `IA`, `NAV`, or task flows.
- Read [references/interaction-logic-principles.md](references/interaction-logic-principles.md) before choosing surfaces, dialogs, feedback, or recovery behavior.
- Read [references/ascii-interactions.md](references/ascii-interactions.md) before drawing flows or `UI/STATE` frames.
- Read [references/progressive-ascii-confirmation.md](references/progressive-ascii-confirmation.md) before presenting or persisting detailed ASCII UX.

Use `assets/ascii-ui-supplement-template.md` only for a requested standalone supplement or when completing missing ASCII behavior in an existing document.

## Input gate

Require a confirmed `DEC-BASELINE` and confirmed material `FLOW-HP/DEC-HAPPY`, or clearly label the affected interaction work provisional. Do not silently turn an unresolved path decision into a page or control choice.

## Workflow

1. Derive user-recognizable `FUNC` capabilities from confirmed stories and paths.
2. Choose starting surfaces, product topology, `IA`, and `NAV` based on tasks and objects rather than defaulting to dashboards or lists.
3. Model primary, alternate, failure, exit, recovery, cross-role, and asynchronous `FLOW` behavior.
4. Derive each `INT` chain: trigger → context → action → system response → feedback → next state/recovery.
5. Create compact ASCII hierarchy/flow overviews and focused `UI/STATE` frames for every user-visible interaction behavior.
6. Cover default, loading, empty, success, error, permission, partial-success, stale/concurrent, and recovery states when applicable.
7. Record viewport, input, accessibility, density, and responsive constraints that ASCII cannot prove.
8. Order confirmation units by dependency, present one coherent unit at a time, offer modification or confirmation, then persist `DEC-ASCII-###` atomically.

## Output contract

Produce canonical `FUNC`, `IA`, `NAV`, `FLOW`, `PAGE/SUB` when needed, `INT`, `UI/STATE`, related `UXH`, an ASCII confirmation queue, and `DEC-ASCII` records. Maintain traceability to `SCN/REQ/TASK/US/JS/FLOW-HP`.

Stop before exhaustive cross-cutting specifications, acceptance criteria, delivery-profile packaging, and final handoff unless the delivery skill is invoked.
