# Information architecture and task flows

Use this reference after the requirement/story baseline and material happy paths are confirmed to turn validated scenarios, concepts, stories, and paths into a navigable product structure and complete user-task flow before drawing detailed ASCII UI.

## Contents

- Purpose
- Maintain the canonical UX hypothesis register
- Derive functional points from confirmed stories
- Choose the starting surface and page topology
- Define the product structure
- Create the information architecture map
- Specify navigation behavior
- Choose an ASCII flow form
- Model task and decision flows
- Cover cross-role and asynchronous work
- Map flows to stories and interfaces
- Validate the architecture and flows
- Required outputs

## Purpose

Do not begin detailed screen design until users can:

1. find the relevant object or task;
2. understand where they are;
3. predict where an action leads;
4. complete the task across pages, roles, waits, and failure states;
5. return or recover without losing necessary work.

Information architecture describes where product objects and tasks live. Task flows describe how users and systems move through them. Use a fenced `text` ASCII view as the first explanation of every primary hierarchy or flow, then follow it with tables for exact IDs, guards, rules, and trace links.

## Maintain the canonical UX hypothesis register

Keep one canonical register for material claims about terminology, findability, expected sequence, comprehension, risk perception, and completion signals:

| Hypothesis | Affected user/task | Validation task | Success signal | Failure signal | Current evidence | Status/owner | UXH ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use statuses: Evidence-backed, Owner-confirmed, Test planned, Inferred, Assumed, Invalidated, or Blocked.

Concept files may reference a `UXH` ID and retain concept-specific evidence, but must not duplicate the hypothesis definition. Trace material hypotheses to `CON`, `REQ`, `US/JS`, `IA`, `FLOW`, or `UI` IDs.

## Derive functional points from confirmed stories

After baseline confirmation, derive product capabilities before proposing pages:

```text
Confirmed user outcome
  → US/JS
    → FUNC capability
      → starting surface
        → PAGE/SUB destination
          → INT interaction
            → UI/STATE and SPEC/AC
```

Use `FUNC` for a user-recognizable capability or responsibility, not for a screen component, API, service, or implementation module. One story may require several functions; one shared function may support several stories. Preserve that many-to-many relationship instead of forcing one story into one page.

| User outcome | Functional point/capability | User-visible result | Preconditions/rules | Shared with | Evidence | FUNC ID | US/JS ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

For each function, identify the user decision or task it enables, the objects it operates on, its completion signal, applicable exceptions, and the interactions that must eventually be specified. Reject a functional point that cannot be traced to a confirmed story or that only restates a proposed control.

## Choose the starting surface and page topology

Choose the first meaningful product surface from the user's dominant job:

| User need | Preferred starting surface | Typical continuation |
|---|---|---|
| Understand status across objects | Overview or status summary | Filter, inspect exception, open resource detail |
| Find and manage objects | Resource list or collection | Search/filter, select, open detail, create or bulk act |
| Process prioritized work | Work queue or inbox | Claim/review item, complete action, move to next |
| Inspect a known object | Detail-first destination | Review state/history, edit, run contextual action |
| Complete a focused operation | Dialog, direct task, wizard, or dedicated task page | Configure, review consequence, submit, see result |
| Change shared policy or defaults | Configuration or policy surface | Select scope, edit, validate, review impact |

Do not default every feature to a dashboard or resource list. Choose one or more starting surfaces only when they reduce navigation and make the confirmed stories discoverable.

Draw the experience topology before detailed UI:

```text
[Entry or deep link]
        |
        v
[PAGE-01 Overview / Resource list / Work queue]
        |
        +-- select resource ----> [PAGE-02 Resource detail]
        |                              |
        |                              +-- contextual action --> [UI-02-01 Task state]
        |
        +-- create/start task --> [PAGE-03 Task or wizard]
        |
        +-- denied/not found --> [Explanation and recovery]

[Detail/task complete] -- preserve context --> [Return to PAGE-01]
```

Then define the surface map:

| Starting-surface model | User purpose and primary content | Entry | Detail/action destination | Return/context behavior | PAGE/IA ID | Related US/JS | FUNC ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

Show detail pages, dialogs, task pages, external jumps, and cross-product destinations only when they carry a distinct user purpose, decision, or context. Never propose a drawer, side sheet, slide-over, or off-canvas task panel. Record what context travels forward and what is restored on return.

## Define the product structure

Derive structure from user goals, the story backbone, and domain relationships, not from current service boundaries alone.

Identify:

- core user-recognizable objects;
- object containment, ownership, and scope;
- primary activities and recurring tasks;
- global versus contextual destinations;
- detail, list, configuration, history, and diagnostic views;
- role-, edition-, tenant-, project-, or environment-specific visibility;
- existing locations that should be preserved, migrated, or deprecated.

Flag conflicts between:

- current navigation and the proposed user mental model;
- object hierarchy and permission hierarchy;
- product terminology and route/module names;
- one user's entry point and another role's handoff point.

## Create the information architecture map

Use a compact tree:

```text
Product
├── Workspace
│   ├── Policies
│   │   ├── Policy list
│   │   ├── Policy detail
│   │   └── Change history
│   └── Deployments
└── Administration
    └── Access control
```

Then define each node:

| Level | Page/object | User purpose | Parent/context | Entry points | Return path | Role/visibility rule | Existing/new | IA ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Use `IA` IDs for architecture nodes. Reuse `PAGE`, `FUNC`, or `CON` IDs in related-ID columns rather than replacing them.

Do not create a navigation destination for every implementation module. Merge or hide internal boundaries when users experience one task or object.

## Specify navigation behavior

For important destinations, define:

- global, local, contextual, or deep-link entry;
- default destination and landing state;
- breadcrumb or hierarchy context;
- preserved filters, selections, drafts, and scroll position;
- browser back, cancel, close, and return behavior;
- unsaved-change behavior;
- linkability and shareability;
- permission-denied and object-not-found behavior;
- renamed, moved, or deprecated-route behavior;
- cross-scope switching consequences.

Use:

| From | Trigger/link | Destination | Context carried | Back/return behavior | Permission/failure behavior | Related IDs | NAV ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

For multi-step or conditional navigation, precede the table with an ASCII route flow that shows entry, destination, carried context, return, and denied/not-found paths.

## Choose an ASCII flow form

Choose the smallest form that makes the relationship immediately scannable:

| Situation | Preferred ASCII form |
|---|---|
| Linear user task | Vertical or left-to-right arrow flow |
| Decision and alternate paths | Branch tree with labeled guards |
| Several roles or ownership changes | Swimlane or sequence flow |
| Background work, waits, or re-entry | Async sequence with wait/notification/re-entry nodes |
| Lifecycle or status changes | State-transition flow |
| Product/object containment | Tree |
| Requirement-to-UI coverage | Compact trace chain |

Put stable IDs inside or beside important nodes. Keep one diagram focused on one user-recognizable outcome. Split the main path, recovery path, or role handoff into linked subflows when a diagram exceeds roughly four lanes, several nested decisions, or a comfortable Markdown reading width. Use a table without an ASCII companion only when the content is fundamentally a matrix and drawing it would obscure rather than clarify the rule.

## Model task and decision flows

Create one flow for each primary scenario or materially different role path.

Begin with its confirmed `FLOW-HP-###`. Add decision branches only after the happy path is visually understandable, and keep alternate, failure, exit, and recovery paths linked rather than silently merging them into normal success.

Start with a compact ASCII flow before writing the detailed flow table:

```text
[SCN-01 Trigger]
      |
      v
[FLOW-01 Locate target]
      |
      v
[FLOW-02 Run pre-check]
      |
      +-- eligible ----------> [FLOW-03 Review] -> [Complete]
      |
      +-- fixable issue -----> [FLOW-04 Correct] --+
      |                                             |
      +-- no permission -----> [Request access/Exit]|
                                                    |
                         <--------------------------+
```

Then make every step explicit:

| Actor | User intent | Entry/precondition | User or system action | Decision/guard | System response | Next step/state | Interruption/recovery | Related IDs | FLOW/step ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include decisions only when they change the path. Do not turn every field validation into a high-level decision node.

## Cover cross-role and asynchronous work

When applicable, include:

- ownership transfer or review handoff;
- approval, rejection, and requested changes;
- background processing and user departure;
- notification and re-entry;
- timeout, cancellation, retry, and resumption;
- partial success and item-level recovery;
- stale state or concurrent modification;
- external-system wait and delayed synchronization;
- audit checkpoints;
- destructive or irreversible boundaries.

Use swimlane-style ASCII when ownership changes:

```text
Requester           Approver            System
   | submit             |                  |
   |------------------->|                  |
   |                     | review          |
   |                     |----------------->| validate
   |                     |<-----------------| result
   |<--------------------| approve/reject   |
```

Keep the number of lanes small. Split the handoff into linked ASCII subflows before falling back to a supporting table.

Show async departure and re-entry explicitly:

```text
User                  Product                 Worker
 | start job             |                       |
 |---------------------->| enqueue               |
 |<----------------------| job accepted          |
 | leave                 |---------------------->| run
 |                       |<----------------------| result
 |< - - notification - - |                       |
 | reopen job            |                       |
 |---------------------->| show result/recovery  |
```

Do not compress a wait into one arrow when the user may leave, lose context, receive a notification, or need to resume or recover.

## Map flows to stories and interfaces

Trace each primary flow:

```text
SCN/REQ
  → TASK/FLOW-HP
  → US/JS
  → FUNC
  → starting surface and IA/NAV/PAGE/SUB
  → INT/UI/STATE
  → SPEC/AC
```

Every primary story must have:

- one entry or trigger;
- a defined completion outcome;
- a main task flow;
- relevant alternate or recovery branches;
- one or more interface states when a UI is required.

Every primary scenario must have one evidence-labeled candidate happy path, and every full confirmed delivery must promote it to a confirmed `FLOW-HP-###` or explicitly mark it Blocked/Not applicable with a concrete rationale.

Do not create an ASCII UI frame for a flow step that is entirely automatic and has no user-visible state. Keep the step in the ASCII flow, then specify its system behavior and notification instead.

## Validate the architecture and flows

Check:

- every primary scenario has a discoverable entry point;
- every primary scenario has a first-principles-derived happy path with an observable user completion signal;
- every material happy path has an adversarial review and `DEC-HAPPY-###` confirmation before downstream page/UI derivation;
- alternate, failure, exit, and recovery conditions are linked without being mistaken for normal success;
- navigation labels use approved product terminology;
- role visibility matches permission rules;
- the user's scope and current object remain understandable;
- every flow has a completion, exit, or recovery;
- cross-role handoffs identify ownership and notification;
- long-running work defines departure and re-entry;
- destructive paths show consequence and reversibility before commitment;
- alternate paths do not dead-end;
- the number of pages follows user tasks rather than internal services;
- every confirmed story maps to one or more functional points;
- every functional point maps to a justified starting surface and any required detail/action destination;
- overview, list, queue, detail, direct-task, and configuration patterns are chosen from user needs rather than applied uniformly;
- every page and subfeature supports at least one story without changing the story's user outcome;
- IA, task-flow, story, and ASCII IDs trace consistently.

## Required outputs

For a full shaping request, produce:

1. canonical UX hypothesis and validation register;
2. candidate and confirmed `FLOW-HP-###` paths with first-principles basis, adversarial review, linked branch inventory, and `DEC-HAPPY-###` records;
3. confirmed story-to-functional-point map;
4. starting-surface decision table and ASCII page/detail/jump topology;
5. interaction-logic chain, material pattern-rationale table, and flow-model fit coverage for every material target `ROLE/SCN`;
6. information architecture tree and IA node table;
7. ASCII navigation flow plus the applicable navigation behavior table when navigation spans steps or branches;
8. one ASCII task/decision flow plus its detailed table for every primary scenario;
9. ASCII swimlane or async sequence for every material cross-role handoff, wait, notification, or re-entry;
10. ASCII state flow for every material lifecycle;
11. representation-model fit coverage plus material `UXGAP` findings linked to the affected role, scenario, flow, interaction, or UI/state;
12. mapping from stories through happy paths, functions, pages, interactions, UI states, specifications, and acceptance criteria.

For a narrow, single-screen request, a compact ASCII entry/task/return flow plus a short supporting table may be sufficient.
