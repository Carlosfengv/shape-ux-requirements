# Requirement alignment and confirmation gate

Use this reference to separate requirement understanding from detailed design and prevent silent requirement drift.

## Contents

- Decide when the gate applies
- Produce the first-pass alignment brief
- Ask for confirmation
- Lock the confirmed baseline
- Produce the detailed specification
- Control later changes
- Review the gate

## Decide when the gate applies

Use the confirmation gate by default for a new requirement, a materially revised requirement, or a request that would produce full specifications or ASCII UI from an unconfirmed baseline.

Do not repeat the gate when:

- the user provides an explicitly confirmed baseline and asks for a bounded downstream artifact;
- the task audits an existing specification without changing it;
- the user asks for exploratory options and accepts a provisional output;
- the requested change is editorial and does not alter users, scope, stories, rules, states, permissions, or outcomes.

If a supposedly narrow change alters a story, scope boundary, role, lifecycle, permission, failure behavior, or success outcome, return to the gate for the affected slice.

## Produce the first-pass alignment brief

Complete repository discovery, applicable public research, readiness assessment, problem framing, terminology shaping, and the outcome/task-led story backbone before asking for confirmation.

Use `assets/requirement-alignment-template.md`. Keep the first pass readable and decision-oriented. Include:

1. evidence and current-versus-requested behavior;
2. requirement background, problem, why now, and impact;
3. business and user objectives, non-goals, and success signals;
4. primary users, affected people, and target scenarios;
5. important concepts and user-facing language;
6. in-scope, later, and out-of-scope boundaries;
7. candidate `REQ`, `TASK`, and complete `US/JS` definitions;
8. main, alternate, failure, and recovery intent for each story;
9. assumptions, conflicts, missing decisions, priority/release uncertainty, and risks;
10. a concise statement of what detailed work will follow after confirmation.

Do not produce functional-point decomposition, starting-surface/page topology, detailed interaction logic, the full interface specification, final information architecture, detailed ASCII UI frames, system contracts, or exhaustive acceptance criteria in this pass. A small conceptual ASCII outcome/story flow is allowed only when it helps the user verify sequence or scope; label it as non-binding and do not imply screen structure.

If blocking gaps remain, ask focused questions instead of presenting the brief as confirmable.

## Ask for confirmation

End the alignment brief with one explicit confirmation decision. When the host provides a structured choice component, offer:

- `Confirm baseline and continue` — lock the presented scope and stories, then begin detailed design;
- `Confirm with corrections` — collect the exact corrections, update affected IDs, and present the changed baseline for confirmation;
- `Need more analysis` — keep detailed design paused and investigate the named uncertainty.

Do not treat silence, “looks interesting,” or feedback on only one story as confirmation of the full baseline. Record who confirmed it, when, which version, and any conditions.

## Lock the confirmed baseline

After explicit confirmation:

1. change the baseline status from pending to `Confirmed`;
2. assign a baseline version and record `DEC-BASELINE-###`;
3. freeze the confirmed `BG`, `OBJ`, `ROLE`, `SCN`, `CON`, `REQ`, `TASK`, `US/JS`, scope, assumptions, and open decisions;
4. preserve IDs and wording unless a later approved change requires revision;
5. link every downstream IA, flow, page, interaction, UI, specification, and acceptance criterion to the confirmed baseline.

Confirmation validates shared understanding, not factual truth. Keep evidence labels, assumptions, and unresolved non-blocking questions visible.

## Produce the detailed specification

Only after confirmation, derive functional points from stories, choose the appropriate overview/list/queue/detail/task starting surfaces, map detail and jump destinations, organize and justify the interaction logic, and then proceed with information architecture, task and decision flows, page/subfeature decomposition, complete ASCII UI/state coverage, interaction behavior, system contracts, accessibility/adaptation constraints, atomic specifications, acceptance criteria, and traceability.

If detailed design reveals a material contradiction or missing decision, pause the affected branch, explain why the baseline is insufficient, and return only that slice to confirmation. Continue unaffected confirmed work when separation is safe.

## Control later changes

Never rewrite a confirmed baseline silently. Record each proposed change:

| Requested change | Reason/source | Downstream impact | Decision/status | Affected baseline IDs | CHG ID |
| --- | --- | --- | --- | --- | --- |

Classify the change as:

- `Clarification`: wording improves without changing behavior;
- `Correction`: the baseline was inaccurate;
- `Scope change`: included outcomes or stories change;
- `Behavior change`: rules, states, permissions, or recovery change;
- `Evidence update`: confidence or source changes without automatically changing the decision.

Assign each change a stable `CHG-###` ID. Reconfirm the affected stories and scope before regenerating dependent specifications or ASCII UI. Keep superseded wording and the reason for change in the revision history.

## Review the gate

Before detailed design, verify:

- the baseline status is `Confirmed`;
- confirmation applies to the current version and story set;
- each story is complete enough to discuss without a proposed screen;
- scope, later work, and non-goals are distinguishable;
- assumptions and open decisions are visible;
- no detailed UI or system behavior has been smuggled into an unconfirmed story;
- downstream planning starts from confirmed IDs;
- later changes are handled as deltas, not silent rewrites.
