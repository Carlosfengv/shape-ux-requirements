---
name: shape-ux-requirements
description: Orchestrate end-to-end enterprise UX requirement shaping across evidence-grounded baseline confirmation, happy-path review, ASCII interaction design, and final specification delivery. Use when a request spans multiple phases or needs one coordinated artifact. Do not use for a single bounded phase when a specialist skill is sufficient.
---

# Shape UX Requirements

Coordinate the specialist skills without collapsing their confirmation gates. Default to one evolving `ux-requirements.md` and preserve confirmed IDs and decisions across every handoff.

## Read first

Read [references/artifact-contract.md](references/artifact-contract.md) before routing or combining stages.

## Route by smallest sufficient scope

| User need | Specialist |
| --- | --- |
| Repository/current-state discovery, input readiness, problem framing, concepts, stories, baseline | `$shape-requirement-baseline` |
| Candidate or detailed primary successful path, first-principles and adversarial review | `$shape-happy-paths` |
| IA, navigation, task/decision flows, interaction logic, ASCII UI and state confirmation | `$shape-ascii-interactions` |
| Specifications, acceptance, traceability, Markdown packaging, validation, review and handoff | `$deliver-ux-requirements` |

Use only the relevant specialist for a narrow request. For end-to-end shaping, run the stages below in order.

## Orchestration sequence

1. Establish repository/current-state evidence and a requirement/story baseline with `$shape-requirement-baseline`.
2. Stop until the material baseline has `DEC-BASELINE` confirmation, unless the user explicitly requests a provisional continuation.
3. Derive and adversarially review each primary `FLOW-HP` with `$shape-happy-paths`.
4. Stop until material happy paths have `DEC-HAPPY` confirmation or an explicit Blocked/Not applicable rationale.
5. Derive IA, task flows, interaction logic, `UI/STATE` frames, and sequential `DEC-ASCII` confirmations with `$shape-ascii-interactions`.
6. Compose specifications, acceptance criteria, traceability, validation, and handoff with `$deliver-ux-requirements`.

At each pause, offer a correction path and name the exact next stage and its expected output. Do not interpret approval of one stage as approval of the next.

## Cross-stage rules

- Treat user statements as inputs, not verified facts; label facts, decisions, inferences, assumptions, unknowns, and conflicts.
- Inspect an available repository before asking for information that its code, tests, docs, schemas, or UI copy can answer.
- Separate current implementation, documented intent, requested behavior, and resulting delta.
- Preserve stable IDs and canonical definitions. Record changes to confirmed artifacts as `CHG` plus a new decision; never silently rewrite downstream meaning.
- Keep pages and controls downstream of confirmed outcomes, stories, and happy paths.
- Keep user-visible behavior traceable through `REQ → US/JS → FLOW-HP → FUNC/IA/INT → UI/STATE → SPEC/AC` as applicable.
- Default to a reader-first Markdown guide. Split files only for independent ownership, review, release, or material readability needs.

## Completion

An end-to-end request is complete only when planned artifacts are present, confirmation coverage is explicit, the delivery validator passes the appropriate final profile, and unresolved decisions or limitations remain visible in the handoff.
