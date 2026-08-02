# Stories and acceptance

Use this reference to convert a validated baseline and concept vocabulary into outcome-oriented stories.

## Contents

- Choose the right story form
- Build the requirement register
- Build the story map
- Add story detail
- Confirm stories before design
- Place stories in the final document
- Cover enterprise concerns
- Write acceptance criteria
- Check story quality

## Choose the right story form

Use a user story when role, capability, and value are important:

```text
As a [role],
I want to [perform a meaningful task],
so that [I obtain an outcome].
```

Use a job story when context and motivation are more important than a stable persona:

```text
When [situation],
I want to [motivation/action],
so I can [expected outcome].
```

Use a scenario for concrete interaction behavior:

```text
Given [precondition],
when [event or action],
then [observable outcome].
```

Do not force all three forms for every requirement.

## Build the requirement register

Define each shaped requirement before assigning it to a page:

| Requirement outcome/rule | Source/evidence | Priority | Release slice | Status | Decision owner | Related OBJ/SCN | REQ ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use an explicit `Unprioritized` or `Release undecided` status when the decision is missing. Do not infer roadmap priority from document order, stakeholder seniority, or implementation effort.

## Build the story map

Organize stories without pages or components in the backbone:

| Outcome | Activity | User task | Priority | Release slice | Evidence | Status | TASK ID | US/JS reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Map stories to `IA`, `PAGE`, `SUB`, and `UI` only after the backbone is coherent. Page assignment is a downstream design decision, not the definition of user value.

Check that each story:

- names a user or operational actor;
- describes a complete user-recognizable outcome;
- uses the approved concept vocabulary;
- remains independent enough to discuss and test;
- does not prescribe an implementation unnecessarily;
- links to a source requirement or decision.

## Add story detail

Use this structure:

| Field | Content |
|---|---|
| Story ID | Stable identifier |
| User outcome | Desired result |
| Preconditions | Required state, data, and permission |
| Trigger | Event that begins the story |
| Main flow | Small numbered sequence |
| Alternate flows | Valid variants |
| Failure/recovery | Errors, partial success, retry, rollback |
| Postconditions | Resulting objects and states |
| Dependencies | Required systems, roles, or data |
| Open questions | Unresolved non-blocking details |
| Trace links | REQ, STMT, CON, UI, SPEC, AC IDs |

Use this compact canonical story table in a page, subfeature, or cross-page task chapter:

| User/context | Task or motivation | Expected value/outcome | Preconditions | Canonical priority/release reference | Main/alternate/recovery flow | Related SCN/REQ/FLOW | US/JS ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

Keep the actual priority and release-slice value in the global story-map row. Reference that row here instead of maintaining a second independently editable value.

## Confirm stories before design

For a new or materially revised requirement, treat the story set as a proposed baseline before defining pages or detailed interactions. Apply `confirmation-gate.md` and present complete candidate stories with their evidence, preconditions, main outcome, alternate/failure intent, scope status, and unresolved decisions.

Ask the user to confirm the whole baseline, confirm it with named corrections, or request more analysis. Do not interpret comments on one story as approval of the others. After confirmation, preserve story IDs and record later changes as explicit deltas; reconfirm the affected slice before regenerating dependent IA, specifications, or ASCII UI.

## Place stories in the final document

Place each story definition before its operating steps, ASCII UI, local specifications, and acceptance criteria. Keep it in:

- the corresponding page/subfeature chapter when the story is primarily completed there;
- the cross-page workflow chapter when it spans destinations;
- a cross-cutting chapter only when it represents a genuinely shared operational outcome;
- an independently split module file only when that slice has its own owner, review boundary, or release lifecycle.

Do not create a list containing only story IDs or titles. Do not duplicate the full story in a traceability appendix or file; reference its canonical location.

Every `US` or `JS` ID used by a page, UI, specification, or acceptance criterion must resolve to one canonical story definition.

Keep the requirement register, global story map, and release slicing in `ux-requirements.md`. In Modular delivery, keep full story definitions in independently owned page/subfeature or cross-page workflow files and link them from the main story map; do not create a dedicated story-map file solely because the table exists.

## Cover enterprise concerns

Inspect each applicable concern:

- role and permission differences;
- approval and separation of duties;
- organization, tenant, project, and environment boundaries;
- inheritance and override precedence;
- bulk actions and mixed eligibility;
- long-running operations and progress;
- concurrency, stale data, and conflicting edits;
- partial success and recovery;
- versioning, migration, and backward compatibility;
- audit history and export;
- destructive or irreversible actions;
- integration outage and delayed synchronization;
- security, compliance, privacy, and retention;
- scale, performance, availability, and accessibility.

Do not add generic enterprise requirements without evidence. Add a question or risk when applicability is unclear.

## Write acceptance criteria

Write observable criteria that validate user and system outcomes. Use IDs and link every criterion to a story and specification.

Good criteria define:

- precondition;
- action or event;
- observable result;
- resulting state;
- permission and data boundary when relevant;
- failure or recovery behavior when relevant.

Avoid:

- “works correctly”;
- “is user-friendly”;
- “loads quickly” without a threshold;
- implementation-only assertions invisible to the requested acceptance surface;
- criteria that merely repeat the story.

Use examples to clarify rules, but do not let examples replace the general rule.

## Check story quality

Reject or revise a story when:

- its value clause is circular;
- it describes a screen, component, endpoint, or database change as the goal;
- it combines unrelated outcomes;
- the role cannot perform or benefit from the action;
- terminology conflicts with the concept dictionary;
- acceptance depends on an unresolved blocking rule;
- only the happy path is represented.
