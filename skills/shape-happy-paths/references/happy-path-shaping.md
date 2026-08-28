# Happy-path shaping

Use this reference after a requirement/story baseline exists and before information architecture or interface design.

## Definition

A happy path is the shortest complete path through normally expected conditions by which the primary actor reaches an observable user outcome. It is not a screen list, demo script, every successful variant, or substitute for alternate, failure, exit, and recovery paths.

## Derive from first principles

Determine:

1. primary actor and the outcome they must achieve;
2. trigger and normally expected context;
3. observable evidence that proves completion;
4. business, permission, data, lifecycle, safety, and role-handoff constraints that cannot be removed;
5. current steps that are essential versus implementation/interface artifacts;
6. shortest safe and comprehensible sequence preserving irreducible constraints.

Use the removal test: if deleting a step still lets the target user safely and correctly reach the same observable result, the step is not inherently part of the happy path.

Keep the first candidate independent of pages and controls:

```text
[Trigger and normal context]
          |
          v
[Understand or provide required information]
          |
          v
[Take the consequential action]
          |
          v
[System completes required work]
          |
          v
[User verifies the intended result]
```

Record:

| Fundamental user outcome | Observable completion evidence | Irreducible constraints | Potentially avoidable steps | Evidence/uncertainty | Related IDs |
| --- | --- | --- | --- | --- | --- |

Do not invent frequency, normality, preference, or completion signals. Mark them Source-confirmed, Repository-confirmed, User-confirmed, Inferred, Assumed, Unknown, or Conflicted.

## Run an adversarial review

Challenge the strongest assumptions:

- Is this the primary user's path rather than the requester, operator, or system's preferred sequence?
- Is the scenario primary by evidence, owner decision, frequency, value, or risk?
- Do preconditions hide setup, permission, data, lifecycle, or integration dependencies?
- Is a required decision, role, wait, notification, handoff, or re-entry missing?
- Does the path end at a user-verifiable result rather than submission, queue acceptance, API success, or a toast?
- Does each step contribute to correctness, safety, comprehension, or the outcome?
- Is exceptional or optional behavior presented as mandatory?
- Would a plausible alternative answer change the actor, outcome, normal preconditions, essential sequence, or completion signal?

Use:

| Challenge | Finding and evidence | Path impact | Resolution/owner | Status | Related IDs |
| --- | --- | --- | --- | --- | --- |

Classify each finding:

- Revise the path when actor, outcome, normal preconditions, irreducible rules, essential sequence, or completion changes.
- Block confirmation when plausible unresolved answers yield materially different paths.
- Link an alternate-success path when another normal success route is material but not primary.
- Link failure, exit, or recovery intent for exceptional conditions.
- Record a downstream `UXH` when the issue concerns discoverability, comprehension, ordering, or interface efficiency.

## Detail without committing to screens

| Step | Actor intent/action | Required system response | User-visible feedback | Next state/completion | Evidence | Related IDs | FLOW/step ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include normally required handoffs, background waits, notifications, and re-entry. Keep exceptional rejection, timeout, and recovery in linked flows.

| Happy-path point | Condition | Path type | User outcome | Linked FLOW/STATE | Status |
| --- | --- | --- | --- | --- | --- |

Use path types Alternate success, Failure, Exit, Recovery, or Out of scope.

## Confirm independently

Story-baseline approval does not confirm detailed happy paths. Present each materially distinct `FLOW-HP` with actor, context, evidence, compact ASCII, detailed steps, first-principles basis, adversarial findings, linked branches, and affected downstream artifacts.

On confirmation, record `DEC-HAPPY-###`, owner/date/conditions, and covered `FLOW-HP/SCN/REQ/TASK/US/JS`. Do not derive canonical pages or detailed UI from an unconfirmed material path.
