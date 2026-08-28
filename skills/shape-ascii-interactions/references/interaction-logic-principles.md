# Interaction logic principles

Use this reference after the requirement/story baseline is confirmed and before drawing detailed ASCII UI. It explains how to derive, organize, choose, and review interaction logic for complex enterprise products.

## Contents

- Start from the user outcome
- Build the interaction logic chain
- Apply interaction design principles
- Choose the interaction surface
- Use dialogs correctly
- Model decisions, feedback, and recovery
- Explain the rationale
- Validate the interaction logic

## Start from the user outcome

Do not begin with a component, route, form, API, or system event. Begin with the confirmed user story and identify:

1. the result the user needs;
2. the trigger and working context;
3. the user-recognizable object being inspected or changed;
4. the information or decision required at this point;
5. the safest useful action;
6. the completion signal and next task.

Separate business rules from interaction choices. A permission, lifecycle guard, approval rule, or data constraint determines what is possible; the interaction design determines how the user understands and acts within that rule. Do not invent a business rule to justify a preferred interface.

## Build the interaction logic chain

Create one chain for each primary user-recognizable outcome:

```text
[User goal]
     |
     v
[Trigger and current context]
     |
     v
[Object and current state]
     |
     v
[Information or decision needed]
     |
     v
[Available user action]
     |
     v
[System response]
     |
     v
[Visible feedback and changed state]
     |
     +-- complete --> [Next useful destination]
     +-- cancel ----> [Return with context preserved]
     +-- problem ---> [Explain, preserve work, recover]
```

Then record the logic in a compact, reader-first table:

| User goal/task | Current context, object, and state | Information or decision needed | User action | System response | Visible feedback | Next, exit, or recovery | Interaction pattern | Related IDs |
|---|---|---|---|---|---|---|---|---|

Keep each row focused on one meaningful decision or state-changing action. Do not turn every field focus, keystroke, or implementation callback into a top-level interaction.

## Apply interaction design principles

Use these principles to choose and review the logic:

1. **Match the user mental model.** Organize around user-recognizable objects, tasks, states, and outcomes rather than service or database boundaries.
2. **Make the current context explicit.** Show the active scope, selected object, current state, and affected target before the user acts.
3. **Make the next action understandable.** The user should know what can be done, why an action may be unavailable, and what happens after it is selected.
4. **Prefer recognition over recall.** Keep necessary choices, consequences, prior values, and recovery guidance visible instead of requiring memory across steps.
5. **Use progressive disclosure.** Show what is necessary for the current decision first; reveal advanced options and technical detail only when relevant.
6. **Prevent errors before explaining them.** Use valid defaults, constraints, pre-checks, impact previews, and clear scope before relying on error messages.
7. **Give timely, proportional feedback.** Acknowledge the action immediately and distinguish accepted, processing, completed, partially completed, and failed outcomes.
8. **Preserve user work and context.** Retain valid input, filters, selection, pagination, scroll position, and return destination when the task is interrupted or fails.
9. **Provide control and recovery.** Define cancel, back, retry, undo, save/resume, or escalation behavior where applicable.
10. **Avoid dead ends.** Empty, denied, missing, stale, failed, and ineligible states need an explanation and a safe next step.
11. **Keep behavior consistent.** The same object, action, state, and consequence should use the same language and interaction rule across the product.
12. **Design for access and adaptation.** Define keyboard, focus, assistive-technology, non-color, text expansion, and narrow-layout behavior with the interaction.

When principles conflict, prioritize task completion, risk reduction, comprehensibility, and recoverability. Record the tradeoff instead of presenting a subjective preference as a rule.

## Choose the interaction surface

Select the smallest surface that keeps the task understandable and recoverable:

| Task characteristic | Preferred pattern | Use when | Avoid when |
|---|---|---|---|
| Small, local, reversible change | Inline interaction | The object and result remain visible in the current context | The action needs substantial guidance, comparison, or consequence review |
| One bounded decision or short form | Dialog | The user can complete or cancel without navigating inside the surface | Content is dense, multi-step, long-running, or needs a shareable destination |
| High-risk bounded decision | Confirmation dialog | Consequence, affected scope, and reversibility can be explained concisely | The user must investigate details or resolve several issues first |
| Complex, multi-step, or reference-heavy task | Dedicated page or wizard | The task needs navigation, save/resume, deep links, substantial data, or several dependent decisions | The task is a single lightweight decision |
| Repeated object management | Resource list plus detail page | Users find, compare, inspect, and act on persistent objects | The user already has one known object and only needs a focused action |
| Long-running or resumable work | Task/status page with notification and re-entry | Users may leave, monitor progress, inspect results, or recover later | Completion is immediate and needs no durable history |

Do not propose or depict a drawer, side sheet, slide-over, or off-canvas task panel. Use a dialog for a bounded contextual interaction and a dedicated page for complex or persistent work.

## Use dialogs correctly

A dialog is appropriate only when the user can understand and complete one bounded task without navigating away or opening another dialog.

Define:

- a title that names the decision or outcome;
- the object and scope affected;
- only the information needed for the decision;
- a clear primary action and a safe cancel/close action;
- consequence and reversibility for high-risk actions;
- validation next to the affected input;
- loading, success, failure, and retry behavior when the dialog remains open;
- initial focus, focus containment, Escape behavior, and focus restoration;
- preservation of valid input after validation or system failure.

Do not:

- nest dialogs;
- place multi-page navigation or dense resource tables inside a dialog;
- use a dialog for long-form reading, ongoing monitoring, or a task users must bookmark or share;
- close the dialog on failure when doing so would discard useful context or input;
- make the close icon the only cancellation mechanism;
- allow background-page interaction while a modal dialog is active.

When the task outgrows these boundaries, use a dedicated page instead of enlarging the dialog indefinitely.

## Model decisions, feedback, and recovery

For every material action, specify:

| Interaction question | Required answer |
|---|---|
| What enables the action? | Preconditions, role, object state, and required data |
| What prevents it? | Guard, reason, and whether the action is hidden, disabled, or rejected |
| What happens immediately? | Local response, acknowledgement, validation, or optimistic/pessimistic behavior |
| What can the user see? | Changed value, status, progress, message, affected scope, or result |
| What happens next? | Destination, retained context, next task, notification, or completion |
| What can go wrong? | Validation, permission, conflict, timeout, partial success, or system failure |
| How does the user recover? | Correct, retry, undo, cancel, resume, request access, or escalate |

Use the appropriate ASCII form:

- task flow for sequence;
- decision tree for materially different paths;
- state flow for lifecycle and availability;
- swimlane for ownership transfer;
- async sequence for waiting, leaving, notification, and re-entry;
- ASCII UI frame for every user-visible control, message, feedback, and material state.

## Explain the rationale

Before detailed frames, give reviewers a short interaction-logic explanation:

| Decision | User need or risk | Chosen behavior | Why it fits | Rejected alternative | Related IDs |
|---|---|---|---|---|---|

Record only material decisions, such as dialog versus page, explicit submit versus immediate update, single versus bulk action, interruption handling, destructive confirmation, and recovery strategy. Avoid rationalizing ordinary conventions.

Mark an interaction as provisional when the role, object state, data, permission, consequence, or recovery rule is not confirmed. Ask a focused question when the answer would materially change the logic.

## Validate the interaction logic

Check:

- every interaction supports a confirmed story and user outcome;
- every task has a clear trigger, context, completion, exit, and recovery;
- every material branch has an explicit guard and terminal result;
- every state-changing action has visible feedback;
- unavailable actions explain why and what the user can do next;
- navigation, dialog close, cancel, browser back, and return preserve the intended context;
- long-running work supports leaving and re-entry;
- high-risk actions show scope, consequence, and reversibility before commitment;
- user input is preserved across correctable failures;
- the chosen surface follows the pattern rules and no drawer-like pattern appears;
- dialog behavior includes focus, keyboard, cancellation, validation, and failure handling;
- every user-visible interaction appears in an ASCII UI/state frame;
- specifications and acceptance criteria can verify the behavior without relying on visual inference.

Revise the interaction when it is technically complete but forces the user to remember context, guess the next step, repeat work, or reach a state with no safe continuation.
