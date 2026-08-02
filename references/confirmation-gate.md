# Requirement alignment and confirmation gate

Use this reference to separate requirement understanding from detailed design and prevent silent requirement drift.

## Contents

- Decide when the gate applies
- Produce the first-pass alignment brief
- Use the confirmation handoff contract
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

## Use the confirmation handoff contract

Apply this contract whenever work pauses for the user to confirm an answer set, requirement slice, story baseline, change, or review decision.

Every confirmation handoff must state:

1. **Current checkpoint** — what has been prepared and its current status.
2. **What to review** — the specific sections, stories, decisions, assumptions, or files that the user is confirming.
3. **Modification path** — what can be changed and how to describe a correction.
4. **Continuation path** — the named next phase, what it will produce, which artifacts or statuses will change, and where the process will pause again.

Use action-specific choices instead of generic `Yes`, `No`, `Confirm`, or `Next` labels. When a structured choice component is available, the two primary choices are:

- `修改当前内容` — keep the next phase paused and collect corrections;
- `确认并进入「<next phase>」` — record the current decision and start the named phase.

Add `需要补充分析` only when a material uncertainty genuinely warrants another path.

For the modification path, tell the user that IDs are optional. Accept corrections by section name, story/function/page name, quoted wording, or a plain-language description. Ask for:

- the item to change;
- the desired wording, rule, scope, or outcome;
- the reason or evidence when it changes behavior or factual confidence.

Offer a compact example such as:

```text
修改“目标用户”：主要用户改为租户管理员，安全审计员作为受影响角色。
修改“批量操作 Story”：本期不支持批量执行，移入后续范围。
```

After receiving corrections:

1. update the canonical item and affected IDs;
2. show a concise change summary with original meaning, revised meaning, and downstream impact;
3. regenerate only affected material;
4. present the affected confirmation slice again with the same modification and continuation paths.

For the continuation path, never say only “进入下一步.” Name the expected state. For example:

```text
确认并进入「详细 UX 设计」
→ baseline 0.2 becomes Confirmed
→ derive functional points and page/task topology
→ generate ASCII task flows and page/subfeature interaction states
→ add colocated specifications and acceptance criteria
→ pause again only if a material contradiction or missing decision appears
```

Do not make the user infer whether choosing continuation locks a baseline, creates files, changes scope status, or starts detailed ASCII UI generation.

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

End the alignment brief with one explicit confirmation decision that follows the confirmation handoff contract. When the host provides a structured choice component, offer:

- `修改需求与 Stories` — keep detailed design paused, collect corrections by section/story name or optional ID, update affected content, and present the changed slice again;
- `确认并进入「详细 UX 设计」` — lock the presented scope and stories, then derive functions, flows, pages, ASCII UI, specifications, and acceptance criteria;
- `补充分析后再确认` — keep detailed design paused and investigate the named uncertainty.

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

Only after confirmation, derive functional points from stories, choose the appropriate overview/list/queue/detail/task starting surfaces, map detail and jump destinations, and organize the interaction logic. Then apply `progressive-ascii-confirmation.md`: order material ASCII UX by dependency, present one candidate unit at a time, write only confirmed units into canonical documents, and derive later candidates from the confirmed baseline plus confirmed upstream ASCII decisions.

Do not interpret baseline confirmation as advance approval of every detailed flow or interface. Each material ASCII interaction slice still requires its own explicit confirmation before canonical write.

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
