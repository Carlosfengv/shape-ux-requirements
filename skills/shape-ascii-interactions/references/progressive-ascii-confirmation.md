# Progressive ASCII UX confirmation

Use this reference after the requirement/story baseline is confirmed and before writing detailed ASCII UX into canonical requirement documents. It defines ordered review units, user confirmation, confirmed-context inheritance, atomic document updates, and change propagation.

## Contents

- Decide whether the loop applies
- Define confirmation units and order
- Maintain the confirmation queue
- Present one candidate at a time
- Process modification or confirmation
- Write confirmed content atomically
- Inherit confirmed context
- Control changes to confirmed ASCII
- Resume and complete the sequence
- Review the confirmation coverage

## Decide whether the loop applies

Use the loop for every material ASCII UX created during full shaping, including:

- experience topology, information architecture, navigation, task, decision, role-handoff, asynchronous, and lifecycle flows;
- page or core-feature overviews;
- section, subfeature, task, dialog, and focused interaction frames;
- materially different permission, validation, loading, empty, error, partial-success, success, stale, conflict, destructive-confirmation, and recovery states;
- cross-page workflows and ASCII UI supplements.

Do not require a new confirmation for a purely editorial ASCII correction that cannot change meaning, behavior, scope, hierarchy, state, control, feedback, navigation, or traceability. Record the correction in the normal revision history.

Confirmation means the ASCII accurately expresses the intended information, behavior, state, and consequence. It does not mean visual design approval, usability validation, accessibility compliance, implementation acceptance, or factual verification unless those activities also occurred.

## Define confirmation units and order

Default to one **interaction slice** per confirmation unit. An interaction slice is one page section, user-recognizable function, subfeature, or cross-page task together with its overview, local flow, and materially different visible states.

Do not force the user to approve every literal frame separately when several frames express one coherent behavior. Use strict per-frame confirmation only when the user explicitly requests it, the interaction is high risk, or separate owners must approve separate states.

Order units by dependency:

```text
[Confirmed requirement and Story baseline]
                    |
                    v
[Experience topology and primary task flow]
                    |
                    v
[Starting page/core-feature overview]
                    |
                    v
[Primary interaction slices in task order]
                    |
                    v
[Alternate, permission, failure, async, and recovery slices]
                    |
                    v
[Downstream detail/dialog/action destinations]
                    |
                    v
[Cross-page and cross-role completion]
```

Move a unit earlier when later units depend on its terminology, layout regions, navigation, controls, state model, or return behavior. Show the proposed queue and allow the user to change the order without requiring a separate gate when the dependency remains safe.

## Maintain the confirmation queue

Persist the queue in `ux-requirements.md` for Compact and Balanced delivery. For Modular delivery, keep the canonical queue in the primary document and mirror only navigation/progress in `index.md`.

Use:

```markdown
## ASCII UX confirmation queue

| Order | Section/function | Confirmation scope | Depends on | Status | Target location | Included UI/STATE IDs | DEC ID |
|---:|---|---|---|---|---|---|---|
```

Use these statuses:

| Status | Meaning |
|---|---|
| Planned | Ordered but not yet generated |
| In review | Candidate is currently presented to the user |
| Changes requested | User requested revision; canonical content remains unchanged |
| Confirmed | User confirmed the current candidate and it was written to the canonical document |
| Blocked | A missing decision prevents a trustworthy candidate |
| Superseded | A later approved change replaced the recorded candidate |

Assign a `DEC-ASCII-###` record when a unit becomes `Confirmed`. One decision may cover several `UI` and `STATE` IDs when they were reviewed together. List every covered ID in the same queue row so confirmation remains traceable.

Only one unit may be `In review` at a time. Do not generate later candidate ASCII while the current unit awaits confirmation unless the user explicitly asks to preview alternatives and accepts that they are provisional.

## Present one candidate at a time

Before presenting a candidate, load:

1. the confirmed baseline and relevant `US/JS`, `FUNC`, `TASK/FLOW`, role, permission, scope, terminology, and state rules;
2. confirmed upstream ASCII units and their `DEC-ASCII` decisions;
3. shared interaction, accessibility, adaptation, and system constraints;
4. unresolved assumptions that affect this unit.

Present:

- queue position, current unit, target file/section, and next planned unit;
- user goal, applicable story/function, entry, expected result, and dependencies;
- the candidate flow and ASCII UI/state frames;
- a concise behavior summary adjacent to the ASCII;
- assumptions, omissions, conflicts, and downstream impact;
- confirmation choices following `confirmation-gate.md`.

Use action-specific choices:

- `修改当前 ASCII UX` — collect changes while keeping canonical content unchanged;
- `确认并写入文档，继续「<next unit>」` — persist this unit and generate the next dependent candidate;
- `暂停 ASCII 确认` — preserve queue state and tell the user how to resume.

When this is the last unit, replace the second label with `确认并写入文档，进入「完整 Review」` and state what the final review will check.

Tell the user how to modify the candidate without requiring IDs. Accept a control, region, step, state, message, quoted text, or plain-language behavior description. Ask for the desired change and its reason/evidence when meaning changes.

## Process modification or confirmation

When the user requests changes:

1. set the unit to `Changes requested`;
2. restate the requested change and identify affected frames, specifications, acceptance criteria, and downstream units;
3. revise only the current candidate and affected provisional material;
4. show a concise before/after/impact summary;
5. set the unit back to `In review` and present it again;
6. do not write the candidate into the canonical page/task document.

When the user confirms:

1. confirm the exact candidate version and covered `UI/STATE` IDs;
2. create or update `DEC-ASCII-###` with confirmer, date, baseline version, dependencies, conditions, and covered IDs;
3. write the ASCII and adjacent local specifications, accessibility/adaptation constraints, acceptance criteria, and trace links to the canonical location;
4. set the queue row to `Confirmed` only after the write succeeds;
5. validate the affected Markdown, links, IDs, trace edges, and local ASCII-to-spec agreement;
6. build the next context packet from all relevant confirmed units;
7. present only the next queue unit.

Do not treat silence, comments on one element, or approval of only the happy path as confirmation of the whole unit.

## Write confirmed content atomically

Keep unconfirmed candidate ASCII out of canonical requirement sections. The confirmation queue may record `In review` or `Changes requested`, but the target page/task section must continue to show `Planned` or `Awaiting ASCII confirmation` until confirmation.

On confirmation, update the following as one coherent slice:

```text
[Confirmed candidate]
        |
        +--> ASCII flow and UI/state frames
        +--> local interface and interaction requirements
        +--> permission, validation, failure, and recovery rules
        +--> accessibility and adaptation constraints
        +--> interaction-to-system contract when applicable
        +--> acceptance criteria
        +--> traceability and confirmation decision
        +--> index/plan status
```

If any required write or validation fails, keep the unit out of `Confirmed`, report the exact failure, repair it, and rerun the affected checks.

## Inherit confirmed context

Treat context in this priority order:

```text
[Confirmed requirement/Story baseline]
                  >
[Confirmed upstream ASCII and DEC-ASCII decisions]
                  >
[Shared confirmed interaction/system rules]
                  >
[Current candidate]
                  >
[Unverified inference or assumption]
```

Carry forward only relevant confirmed context:

- approved product terms, object names, roles, and status language;
- page regions, entry points, navigation, selected scope, and return behavior;
- control names, action hierarchy, dialogs, feedback, focus, and recovery conventions;
- permission, lifecycle, async, concurrency, destructive-action, and audit behavior;
- stable IDs and confirmed trace links.

Do not copy entire earlier documents into the next prompt or section. Summarize the applicable decisions and link their IDs.

## Control changes to confirmed ASCII

Never silently rewrite a confirmed unit. When a new candidate conflicts with confirmed ASCII:

1. stop the affected branch;
2. identify the upstream confirmed unit and `DEC-ASCII` decision;
3. explain the proposed change and downstream impact;
4. create a `CHG-###` record;
5. return the smallest affected confirmed slice to review;
6. mark invalidated downstream units `Changes requested` or `Blocked`;
7. reconfirm and rewrite affected units in dependency order.

Continue unrelated confirmed branches when they do not depend on the changed decision.

## Resume and complete the sequence

When pausing, report:

- the last confirmed unit and decision;
- the current queue statuses;
- the next unit and its dependencies;
- any blocked decisions;
- the exact instruction that resumes work.

When resuming, inspect the canonical documents and queue rather than relying only on conversation memory. Reconstruct the next context packet from confirmed records.

After the final unit is confirmed and written:

1. verify that no required unit remains `Planned`, `In review`, `Changes requested`, or `Blocked` unless the delivery is explicitly provisional or blocked;
2. verify every canonical `UI` definition traces to a confirmed `DEC-ASCII` record;
3. run the full document review and repair loop;
4. include ASCII confirmation coverage and any superseded decisions in the final handoff.

## Review the confirmation coverage

Reject or revise the delivery when:

- several dependent ASCII units were generated together without user confirmation between them;
- unconfirmed candidate ASCII appears as canonical specification;
- the queue order ignores a material dependency;
- a confirmed unit lacks its covered `UI/STATE` IDs or `DEC-ASCII` record;
- the next candidate contradicts confirmed terminology, hierarchy, navigation, state, or behavior;
- a revision changes confirmed upstream behavior without impact analysis and reconfirmation;
- confirmation updates the diagram but leaves adjacent specifications or acceptance criteria stale;
- the user is not told the current unit, how to modify it, what confirmation writes, and what unit comes next.
