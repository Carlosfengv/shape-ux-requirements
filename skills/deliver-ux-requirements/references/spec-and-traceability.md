# Specifications and traceability

Use this reference to convert requirements and interaction behavior into atomic, testable tables.

## Contents

- Screen-local interface specification
- Interaction-to-ASCII coverage
- Functional specification
- State-transition specification
- Permission matrix
- Validation and error specification
- Data and audit specification
- Interaction-to-system contract
- Non-functional specification
- Traceability matrix
- Atomic rule tests
- Final coverage audit

## Screen-local interface specification

Place this table immediately after the related ASCII frame:

| UI element | Type | Display/data rule | Interaction rule | Permission/state rule | SPEC/AC IDs | Element ID |
| --- | --- | --- | --- | --- | --- | --- |

Give every specified element a stable ID such as `UI-01-E01`. Specify labels, values, source, required/default behavior, visibility, editability, and action results only when applicable.

Keep a rule screen-local when it controls one interface element or task step. Move it to a cross-cutting appendix when it applies across several screens, roles, or workflows.

## Interaction-to-ASCII coverage

Define every user-visible interaction behavior with an `INT` ID and place it beside the ASCII frame where the behavior appears:

| Trigger/action | Preconditions | User-visible behavior | Next/recovery | ASCII UI/STATE | SPEC/AC IDs | INT ID |
| --- | --- | --- | --- | --- | --- | --- |

The `ASCII UI/STATE` cell must reference a displayed frame, not a planned screen or flow node alone. Several interactions may reference one frame; create another frame when content, actions, feedback, status, focus context, or recovery materially changes. Mark a truly non-visual automatic behavior `System-only · no user-visible state`; show any visible progress, notification, or result it creates.

## Functional specification

| Object/area | Rule or behavior | Preconditions | User-visible result | Failure/recovery | PAGE/FUNC/SUB/INT | Source IDs | SPEC ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

Write one material rule per row. Use explicit operators, precedence, limits, and time behavior.

## State-transition specification

Precede the tables with an ASCII state flow whenever more than one transition or terminal outcome exists. Use the diagram to explain the lifecycle and the tables to define exact guards and behavior.

Define states once:

| User-facing state | Meaning | Entry condition | Available actions | Exit conditions | STATE ID |
| --- | --- | --- | --- | --- | --- |

Then define transitions:

| Event/action | Guard | System behavior | User feedback | Current STATE ID/name | Next STATE ID/name | SPEC/AC IDs |
| --- | --- | --- | --- | --- | --- | --- |

Cover invalid transitions, retry behavior, cancellation, timeout, and partial success when applicable.

## Permission matrix

| Scope | View | Create | Change | Delete | Approve | Exceptional rules | Role |
| --- | --- | --- | --- | --- | --- | --- | --- |

Distinguish hidden, visible-read-only, disabled, and rejected-on-submit behavior. Do not infer permissions from UI visibility alone.

## Validation and error specification

| Input/event | Validation | Message intent | Preservation | Recovery action | Related IDs | Rule ID |
| --- | --- | --- | --- | --- | --- | --- |

Write messages in user language. Include the cause, consequence, and available recovery without exposing irrelevant internals.

## Data and audit specification

| Data/event | Source | Scope | Freshness | Sensitive? | Retention/audit | User-visible behavior |
|---|---|---|---|---|---|---|

Use only when data provenance, synchronization, security, compliance, or auditability matters.

## Interaction-to-system contract

Use this table when a user-visible interaction crosses a service, job, integration, persistence, or concurrency boundary:

| Required system capability | Authorization/scope | Validation | Sync/async | Data/state change | Outcome variants | Idempotency/concurrency | Audit/observability | Test surface | INT/UI action | Source IDs | SYS ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Specify behavior, not an invented implementation. A capability may be described without choosing an endpoint, queue, database, or framework.

Cover when relevant:

- authoritative authorization enforcement;
- server-side validation and error mapping;
- synchronous response versus accepted background work;
- progress, cancellation, retry, and re-entry;
- duplicate submission and idempotency expectations;
- stale data, optimistic concurrency, and conflict resolution;
- partial success and item-level outcomes;
- persistent state and externally visible side effects;
- audit events and operational observability required to support users;
- frontend, backend, integration, and end-to-end test surfaces.

Keep purely visual or local interactions out of this table.

## Non-functional specification

| Quality | Scenario/scale | Measurable target | Measurement method | Failure behavior | Source | NFR ID |
| --- | --- | --- | --- | --- | --- | --- |

Do not invent thresholds. Mark them as open decisions when absent.

## Traceability matrix

| User outcome | Coverage status | BG/OBJ/SCN/REQ/STMT | ROLE/CON/UXH | TASK/FLOW-HP and branch FLOW | IA/NAV/PAGE/FUNC/SUB/INT | US/JS | UI/STATE | SYS/SPEC/NFR | AC | Baseline/Happy-path/ASCII DEC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Use these coverage statuses:

- Complete
- Partial
- Missing source
- Missing behavior
- Missing UI/state
- Missing acceptance
- Blocked by question
- Out of scope

## Atomic rule tests

Revise a specification when:

- it contains several independent rules joined by “and”;
- it uses vague qualifiers without measurable meaning;
- it does not define the affected role, object, scope, or state;
- it contradicts the concept dictionary or baseline;
- its failure behavior is material but absent;
- no source, decision, or assumption supports it;
- an acceptance criterion cannot observe or verify it.

## Final coverage audit

Find and report:

- requirements without stories;
- confirmed stories without user-recognizable functional points;
- functional points without a confirmed story;
- functional points without a justified starting surface, detail/action destination, or user-visible interaction;
- pages or broad features without subfeature decomposition;
- subfeatures without a user purpose or interaction explanation;
- concepts used but not defined;
- stories without acceptance criteria;
- primary scenarios without an IA entry or complete task/decision flow;
- primary scenarios without an evidence-labeled `FLOW-HP-###`, observable completion evidence, first-principles basis, adversarial review, and confirmed `DEC-HAPPY-###`, unless a Blocked/Not applicable coverage record provides a concrete rationale;
- happy paths that end at submission/system acceptance rather than a verifiable user outcome;
- alternate, failure, exit, or recovery conditions silently mixed into normal success instead of linked as branches;
- user-visible interaction behaviors without an ASCII UI/state frame;
- canonical ASCII UI/state definitions without a confirmed `DEC-ASCII` record;
- unresolved ASCII confirmation queue items or downstream candidates generated before their dependencies were confirmed;
- UI actions without specifications;
- user-visible service/data boundaries without an applicable system contract;
- states without entry or exit behavior;
- specifications without sources;
- permission branches without feedback;
- interactive frames without applicable accessibility, input, or adaptation constraints;
- material UX hypotheses without evidence or a validation task;
- assumptions presented as facts;
- open questions omitted from downstream artifacts;
- terms that drift across artifacts.

Do not “fix” an orphan by inventing a link. Identify the missing decision or artifact.
