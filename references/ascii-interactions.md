# ASCII interactions and flows

Use this reference to create text-based flows and interaction drafts that explain structure and behavior, not visual styling.

## Contents

- Decide what to draw
- Map every interaction behavior to UI
- Complete missing ASCII UI from an existing document
- Flow conventions
- Frame and dialog conventions
- Decompose large pages
- Cover states
- Annotate behavior
- Pair every frame with requirements
- Enterprise interaction checks
- Accessibility, input, and adaptation
- Language checks

## Decide what to draw

Use ASCII before prose or tables whenever spatial, sequential, branching, ownership, or lifecycle relationships matter. Create:

- one overview flow for every primary user task;
- a decision, cross-role, async, or lifecycle subflow for every materially different branch;
- one ASCII frame per materially different screen or state;
- annotations for conditional behavior;
- supporting tables for exact guards, permissions, state rules, and trace links.

Do not draw decorative flows that merely repeat a two-item sentence. Do not replace a readable flow with a table solely because a table is easier to generate.

## Map every interaction behavior to UI

Treat every user-visible interaction behavior as an `INT` that must point to at least one ASCII `UI` or `STATE` frame. This includes actions, input or editing, selection, filtering, validation, confirmation, disabled or permission feedback, progress, notification, success, empty/error/partial/stale states, and recovery. A task flow, prose description, or interaction table explains sequence or rules but does not replace the UI frame that shows what the user sees and can act on.

Use one frame for several interactions when the controls, context, and visible feedback are all clear in that frame. Draw another frame when the action materially changes content, available actions, status, message, focus context, or recovery options. For non-visual automatic behavior, label the `INT` as `System-only · no user-visible state`; if it produces progress, a notification, or a result the user can see, show that output in ASCII.

Maintain a behavior-to-UI coverage table:

| Interaction behavior | Visible change or feedback | ASCII UI/STATE | Source/SPEC/AC | INT ID |
| --- | --- | --- | --- | --- |

Do not mark an interaction complete until its referenced frame exists and visibly contains the relevant control, message, status, or outcome.

## Complete missing ASCII UI from an existing document

When a narrow-scope request or existing requirement document omits ASCII UI, do not silently treat the delivery as complete.

First decide whether ASCII UI is:

- `Expected`: the scope contains a user interaction, page, form, decision, state change, or user-visible workflow;
- `Optional`: the scope is terminology, background, research, or a system-only rule with no user-visible state;
- `Blocked`: UI behavior is expected but critical task, role, data, permission, lifecycle, or failure information is missing;
- `Explicitly excluded`: the user requested a non-UI artifact only.

Show a delivery coverage notice:

| Artifact | Status | Document basis | Impact of omission | Next action |
|---|---|---|---|---|

Use statuses `Included`, `Provisional`, `Omitted`, `Blocked`, or `Not applicable`. Tell the user whether a targeted ASCII UI supplement can be generated from the available document.

If the document is sufficient:

1. Extract the user goal, role, trigger, entry path, objects, terminology, actions, permissions, states, outcomes, and failure/recovery behavior.
2. Build the smallest complete task and state flow.
3. Generate the corresponding page overview and focused ASCII UI states.
4. Place local interface, interaction, state, permission, accessibility, and acceptance requirements beside the frames.
5. Trace every introduced UI element back to existing requirement evidence. Do not invent unsupported business rules.
6. Review the generated UI against the source document and revise unclear hierarchy, terminology, action labels, state coverage, and recovery.

If gaps are non-blocking, generate a clearly marked provisional ASCII UI and list each assumption beside the affected frame. If gaps could materially change the interaction, stop before final frames and ask 1–3 focused questions using a structured choice component when applicable.

At minimum, test whether the supplement needs default, loading, empty, validation error, system error, partial success, success, disabled/ineligible, permission-denied, stale/conflict, destructive-confirmation, and recovery states.

If the user explicitly excludes UI, honor the boundary. Still state that ASCII UI was not produced and identify the later supplement needed if the document will be used for design, implementation, or acceptance.

## Flow conventions

Put each flow in a fenced `text` block. Label important nodes with `TASK`, `FLOW`, `ROLE`, `PAGE`, `UI`, or `STATE` IDs. Use:

- `->` or `v` for progression;
- `+-- condition -->` for branches;
- `<-` for return or recovery;
- `- - notification - ->` for asynchronous notification;
- aligned columns for roles or systems;
- `[Complete]`, `[Exit]`, `[Blocked]`, or `[Retry]` for explicit terminal outcomes.

Use a compact linear flow for a local task:

```text
[TASK-01 Start]
      |
      v
[UI-01 Enter details] -> [UI-02 Review] -> [UI-03 Result]
                              |
                              +-- validation fails --> [UI-01 Correct and retry]
```

Split diagrams by outcome or subflow when they become too wide, exceed roughly four lanes, or contain deeply nested branches. Preserve links between split diagrams with stable IDs.

## Frame and dialog conventions

Use a stable width within one flow. Label every frame:

```text
UI-01 · Create deployment · Default
┌──────────────────────────────────────────────┐
│ Create deployment                           │
├──────────────────────────────────────────────┤
│ Deployment plan                             │
│ [ Select a plan                         ▾ ]  │
│                                              │
│ Target environment                          │
│ [ Select an environment                  ▾ ] │
│                                              │
│ [Cancel]                      [Start deploy] │
└──────────────────────────────────────────────┘
```

Use:

- `[Action]` for buttons;
- `[ Value ▾ ]` for selects;
- `[________________]` for input;
- `( )` and `(●)` for radio options;
- `[ ]` and `[✓]` for checkboxes;
- `…` for in-progress content;
- `!` with explicit copy for warnings or errors.

Do not rely on color, position alone, or unexplained symbols.

Do not draw drawers, side sheets, slide-over panels, or off-canvas task surfaces. Draw a dialog for one bounded contextual decision or short form. Use a dedicated page or wizard when the task is multi-step, information-dense, long-running, resumable, shareable, or requires navigation.

Show a dialog as its own focused state:

```text
UI-02 · Start deployment · Dialog
┌──────────────────────────────────────────────┐
│ Start deployment                            │
├──────────────────────────────────────────────┤
│ Target: Production                          │
│ 12 resources will be affected.              │
│                                              │
│ [Cancel]                    [Start deployment]│
└──────────────────────────────────────────────┘
```

State the initial focus, cancel and Escape behavior, focus restoration, validation placement, input preservation, and whether the dialog remains open during loading or failure.

## Decompose large pages

For a large page, create two levels:

1. A page-level overview showing information architecture, shared controls, major regions, and navigation.
2. Focused subfeature frames showing detailed interaction and state changes.

Label overview regions:

```text
PAGE-01 · Policy management · Overview
┌────────────────────────────────────────────────────┐
│ Policies                         [A: Create policy] │
├────────────────────────────────────────────────────┤
│ [B: Scope] [C: Status] [D: Search]                 │
├────────────────────────────────────────────────────┤
│ [E: Policy list]                                   │
│ Name       Source       Status       [Row actions] │
├────────────────────────────────────────────────────┤
│ [F: Selection and bulk actions]                    │
└────────────────────────────────────────────────────┘
```

Follow it with a region legend:

| Region | Purpose | Main interactions | Focused UI needed? | SUB ID |
| --- | --- | --- | --- | --- |

Create a focused frame when the region opens a form, dialog, detail view, editable state, confirmation, bulk action, progress state, error, or recovery flow. Do not redraw unchanged page regions; show enough surrounding context to preserve orientation.

## Cover states

Inspect:

| Questions | State |
| --- | --- |
| What can the user see and do? | Default |
| Can the user leave, cancel, or safely retry? | Loading/progress |
| Why is it empty and what action is available? | Empty |
| Which field/rule failed and how is it fixed? | Validation error |
| What happened, what was preserved, and what can happen next? | System error |
| Which items succeeded, failed, or remain pending? | Partial success |
| What changed and what should the user do next? | Success |
| Why is the action unavailable? | Disabled/ineligible |
| Is the object hidden, read-only, or explicitly blocked? | Permission denied |
| How does the user compare, refresh, or resolve changes? | Stale/conflict |
| What scope, consequence, and reversibility are shown? | Destructive confirmation |

Draw only applicable states, but explain why critical states are omitted if uncertainty remains.

## Annotate behavior

After each frame, add:

| User action | Preconditions | Visible behavior or feedback | Next/recovery | ASCII UI/STATE | SPEC/AC IDs | INT ID |
| --- | --- | --- | --- | --- | --- | --- |

Use a flow when several transitions matter:

```text
STATE-01 Draft
  ├─ submit valid input → STATE-02 Deploying
  ├─ submit invalid input → STATE-01 Validation error
  └─ cancel → return to deployment list

STATE-02 Deploying
  ├─ all resources succeed → STATE-03 Running
  ├─ some resources fail → STATE-04 Partially deployed
  └─ all resources fail → STATE-05 Failed
```

Show the ASCII state flow before the canonical state-definition and transition tables. The diagram explains the lifecycle; the tables define exact entry conditions, guards, actions, and feedback.

## Pair every frame with requirements

Place a requirement block immediately after each ASCII frame. Do not defer screen-local behavior to a distant specification chapter.

Start with the screen-purpose summary:

| User goal | Applicable roles | Entry condition | Success result | Related stories | UI ID |
| --- | --- | --- | --- | --- | --- |

Then define each visible or interactive element:

| UI element | Type | Display/data rule | Interaction rule | Permission/state rule | SPEC/AC IDs | Element ID |
| --- | --- | --- | --- | --- | --- | --- |

Add validation and transition rows only when applicable. Every row must identify the ASCII state in which its user-visible behavior appears:

| Event/input | Condition | User-visible behavior | Next/recovery | ASCII UI/STATE | SPEC/AC IDs | INT ID |
| --- | --- | --- | --- | --- | --- | --- |

Keep specifications adjacent to the first frame where the element or behavior appears. Reference—not duplicate—the same rule from later frames.

## Enterprise interaction checks

Show where relevant:

- tenant, project, environment, or other scope context;
- affected object count and selection rules;
- permission or approval requirements;
- inherited versus overridden values;
- source, freshness, and synchronization status;
- job progress and background behavior;
- partial-success details and retry scope;
- audit-relevant confirmation and change summary;
- object identity when names are not unique;
- long labels, IDs, and dense data without depending on truncation.

## Accessibility, input, and adaptation

ASCII communicates hierarchy and behavior, but it cannot prove visual accessibility, responsive behavior, focus handling, or assistive-technology semantics.

For each relevant frame, record:

| UX constraint | Requirement |
|---|---|
| Viewport/context | Primary device, minimum supported viewport, embedded/full-page/modal context |
| Keyboard | Tab order, keyboard actions, escape/cancel behavior, and unavailable keyboard paths |
| Focus | Initial focus, focus after validation, focus restoration after close, and focus during async updates |
| Assistive technology | Accessible name, role, state, relationship, live announcement, and error association |
| Non-color cues | Text, icon label, pattern, or status wording used in addition to color |
| Text adaptation | Long labels, localization expansion, wrapping, truncation disclosure, and zoom behavior |
| Narrow layout | Reflow, stacking, preserved actions, overflow, and hidden-content access |
| Dense data | Horizontal overflow, column priority, sticky context, selection, bulk actions, and row identity |
| Motion/time | Reduced-motion behavior, timeout warning, pause/cancel, and progress announcement |

Add only applicable constraints, but do not leave keyboard, focus, error association, or non-color status cues implicit for interactive workflows.

When several frames share the same constraints, define them once in a cross-cutting table and reference its `SPEC` or `NFR` IDs.

## Language checks

Use approved product terms in titles, fields, actions, statuses, help, errors, and confirmations. Keep source engineering terms only in advanced details when needed.

Name actions by outcomes:

- prefer `Start deployment` over `Submit`;
- prefer `Apply changes to 24 devices` over `Confirm`;
- prefer `Remove access` over `Delete binding`.

Explain consequences near the action. Do not use friendly language to conceal broad or irreversible effects.
