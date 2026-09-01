# Model-to-interface gap review

Use this reference to evaluate an existing or candidate interaction flow against an explicit target user and scenario. Apply it while shaping new interactions and when the user requests an audit without redesign.

## Choose the mode

- **Shape mode:** derive `FLOW/INT/UI/STATE`, review model fit at the two checkpoints below, and revise affected candidates before confirmation.
- **Audit mode:** inspect supplied `FLOW/INT/UI/STATE`, report evidence-bounded findings and recommendations, and do not silently redesign or confirm the source artifacts.

Audit mode may begin without a fully confirmed upstream baseline when the minimum input below exists. Mark the result Provisional and identify missing upstream decisions. Do not imply that a provisional audit satisfies the normal downstream confirmation gates.

## Require a target-user context

A trustworthy review needs:

1. a specific primary `ROLE` with responsibilities, goal, relevant expertise/vocabulary, and decision rights;
2. a specific `SCN` with trigger, context, intended outcome, risk, and completion signal;
3. the `FLOW/INT` being reviewed and, for representation review, the applicable `UI/STATE`;
4. an evidence status for claims about familiar objects, expected sequence, decision information, risk perception, vocabulary, and completion.

If `ROLE` or `SCN` is missing, stop as Blocked. When user expectations are inferred or assumed, continue only as Provisional. Keep these evidence states distinct:

- Research-backed or observed with representative users;
- Observed product/behavior data;
- Domain-owner-confirmed;
- Repository/document-supported;
- Inferred;
- Assumed;
- Unknown or conflicted.

Do not average different roles into one mental model. The same flow may fit an expert administrator and fail an occasional requester; review every materially different role/scenario pair separately.

## Compare three models

Review the relationship between:

```text
[What the target user believes they are doing]
                      |
                      v
[What the interface lets the user perceive and do]
                      |
                      v
[What the product and underlying system actually do]
```

Do not treat the stakeholder request, current interface, API shape, service boundary, database schema, or implementation sequence as the user's expected model. Preserve internal distinctions when hiding or merging them would make consequences unsafe or misleading.

## Classify material gaps

Use one primary type per finding and note secondary effects only when useful:

| Type | Question | Common symptom |
| --- | --- | --- |
| Concept | Do objects, relationships, actions, and states mean what the user expects? | Internal entities, job states, or service names appear as product concepts |
| Execution | Can the user discover and perform the action that matches the current goal? | The user must know system order, navigate by module, or translate intent into implementation operations |
| Evaluation | Can the user interpret system state, feedback, completion, and the next useful step? | Submission, queue acceptance, a toast, or an internal status is mistaken for completion |
| Consequence | Can the user predict the affected scope, authority, propagation, reversibility, and delayed effects? | Permission, inheritance, bulk, async, approval, or synchronization effects are hidden or surprising |

Do not create a finding for every reviewed step. Persist `UXGAP-###` only for a material mismatch, unsupported high-risk assumption, or unresolved uncertainty that can change the interaction.

## Review at two checkpoints

### 1. Flow-model fit

Run after candidate `FLOW/INT` exists and before committing to detailed UI. For each meaningful decision or state-changing step, ask:

- What result is the user pursuing now?
- Which familiar object does the user believe they are acting on?
- What sequence and consequence do they predict?
- Does the proposed action correspond to that intent, or expose an implementation operation?
- Are permission, setup, waits, role handoffs, scope changes, or destructive boundaries hidden?
- Does the path end at user-verifiable completion?

Revise the candidate flow when the mismatch comes from avoidable ordering, exposed internal boundaries, missing decisions, false completion, or an incorrect actor. Keep irreducible business and safety constraints, but change how they are explained or staged when possible.

### 2. Representation-model fit

Run after candidate `UI/STATE` exists and before its `DEC-ASCII` confirmation. Ask:

- Do labels and groupings use the target user's product/domain language without erasing essential distinctions?
- Can the user recognize the current object, scope, state, authority, and available action?
- Does the visible action predict the actual result and affected scope?
- Do processing, partial success, failure, completion, stale, and recovery states explain the user's consequence rather than only system activity?
- Can the user determine what happened, whether work is complete, and what to do next?

Do not use helper text to rescue a fundamentally incorrect object model or task order. Repair the canonical `CON/FLOW/INT` source before refining copy or frames.

## Record coverage and findings

Record review coverage even when no material gap is found:

| Model-fit review coverage | Target user/scenario | Reviewed FLOW/INT/UI/STATE | Evidence status | Result | Rationale/limitation |
| --- | --- | --- | --- | --- | --- |
| Flow-model fit | ROLE-### · SCN-### | FLOW-### · INT-### | | Reviewed / Reviewed with findings / Provisional / Blocked / Not applicable | |
| Representation-model fit | ROLE-### · SCN-### | UI-### · STATE-### | | Reviewed / Reviewed with findings / Provisional / Blocked / Not applicable | |

Create findings only when needed:

| Target user/scenario | Flow or interface point | User goal/expectation | Interface expression | Actual system behavior/consequence | Gap type | Severity | Evidence | Resolution/status | Related IDs | UXGAP ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Every `UXGAP` must trace to `ROLE`, `SCN`, and at least one affected `FLOW`, `INT`, `UI`, or `STATE`. Link a material unvalidated expectation to its canonical `UXH`; use `CHG` when repairing a previously confirmed artifact.

## Separate severity from evidence

Use impact and recoverability—not evidence confidence—to assign severity:

- **Critical:** can cause action on the wrong object or scope, unauthorized behavior, irreversible loss, dangerous propagation, or false belief that a consequential task completed.
- **Major:** likely causes task failure, repeated error, lost work, or no viable recovery.
- **Moderate:** creates material comprehension, navigation, decision, or efficiency cost.
- **Minor:** creates localized terminology, guidance, or consistency friction.

Keep evidence strength in its own column. Do not multiply severity and confidence into a pseudo-precise score.

A Critical finding blocks confirmation of affected `UI/STATE` until it is Resolved or Superseded. Do not use Accepted risk to bypass that rule. Open non-critical findings may remain only when the affected output and delivery are explicitly Provisional or carry a named, owned limitation.

## Close the loop without overstating validation

Use these distinct claims:

- **Expert-reviewed:** evaluated by the shaping/review method;
- **Owner-confirmed:** confirmed by the responsible product or domain owner;
- **User-validated:** observed with representative target users performing realistic tasks against the relevant flow or interface;
- **Provisional:** based materially on inference, assumption, incomplete artifacts, or unresolved evidence.

Define a task-based validation plan for material `UXH` or unresolved gaps: what the representative user must find, explain, predict, decide, or complete; the success/failure signal; and the owner. Do not claim usability or user-model validation from `DEC-ASCII` alone.

## Confirmation rule

Before confirming an interaction slice, state its coverage result, evidence status, resolved findings, remaining non-blocking limitations, and user-validation claim. `DEC-ASCII` may confirm the intended behavior only when no affected Critical `UXGAP` remains open. Confirmation does not create missing user evidence.
