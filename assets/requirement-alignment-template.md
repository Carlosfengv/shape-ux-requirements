# [Requirement name] · Requirement Alignment and Story Confirmation

> First-pass review artifact. Confirm the requirement baseline and stories before detailed specifications or ASCII UI are produced.

## Document status

| Item | Value |
|---|---|
| Purpose | Align on the problem, people, scope, and stories |
| Repository/source snapshot | |
| Baseline version | 0.1 |
| Baseline status | Awaiting confirmation |
| Prepared/reviewed on | |
| Confirmation owner | |
| Confirmation record | Not yet confirmed |

## How to review this brief

Confirm whether the background, objectives, users, scenarios, scope, terminology, and stories describe the intended product outcome. Story-to-functional-point decomposition, starting-surface and page topology, interaction-logic design and rationale, detailed ASCII UI, interaction specifications, and acceptance criteria will follow only after this baseline is confirmed.

## 1. Current understanding

[Summarize the requirement in plain language: what is changing, for whom, and why.]

| Today | Requested outcome | Evidence or basis |
|---|---|---|
| | | |

### Current implementation and requested delta

| Area | Current behavior | Requested behavior | Delta/risk | Source |
|---|---|---|---|---|

## 2. Background, problem, and objectives

### Why this matters

[Describe the trigger, current workaround, impact, and why now.]

| Business or user objective | Success signal | Evidence/owner | OBJ ID |
| --- | --- | --- | --- |

### Boundaries

| Boundary | Included, later, or out of scope | Reason/decision |
|---|---|---|

## 3. People and target scenarios

| Person/role | Responsibility and context | Need or pain | ROLE ID |
| --- | --- | --- | --- |

| Trigger and context | User task | Desired result | Important risk | SCN ID |
| --- | --- | --- | --- | --- |

## 4. Mental model and terminology

| Source/internal term | Proposed product term | Plain-language meaning | Evidence or uncertainty | CON ID |
| --- | --- | --- | --- | --- |

## 5. Requirement and story backbone

```text
[User outcome]
      |
      +-- [Activity] --> TASK-001 --> US-001
      |
      +-- [Activity] --> TASK-002 --> US-002

Conceptual scope flow only · not an ASCII UI commitment
```

| Required outcome or rule | Evidence | Priority/release status | Open decision | REQ ID |
| --- | --- | --- | --- | --- |

### US-001 · [Story name]

**Story:** As a [role], I want to [meaningful task], so that [user outcome].

- Preconditions:
- Trigger:
- Scope/release status:
- Evidence:
- Main outcome:
- Alternate or exception intent:
- Failure and recovery intent:
- Related requirement/scenario:
- Assumption or open question:

### US-002 · [Story name]

**Story:** When [situation], I want to [motivation/action], so I can [expected outcome].

- Preconditions:
- Trigger:
- Scope/release status:
- Evidence:
- Main outcome:
- Alternate or exception intent:
- Failure and recovery intent:
- Related requirement/scenario:
- Assumption or open question:

Repeat only for stories in the proposed baseline.

## 6. Assumptions, conflicts, and risks

| Type | Item | Why it matters | Resolution/owner | ID |
| --- | --- | --- | --- | --- |

## 7. What confirmation authorizes

After confirmation, detailed work may begin on:

- deriving user-recognizable functional points from the confirmed stories;
- selecting an overview, resource list, work queue, detail-first, direct-task, or configuration starting surface according to the user task;
- mapping detail/action destinations, jumps, and context-preserving return paths;
- organizing interaction logic from user goal through context, decision, action, system response, feedback, next step, exit, and recovery;
- selecting inline, dialog, or dedicated-page patterns without drawer-like surfaces;
- information architecture and task/decision flows;
- page, feature, and subfeature decomposition;
- ASCII UI for every user-visible interaction and material state;
- interaction, validation, permission, recovery, and system contracts;
- accessibility/adaptation requirements;
- detailed acceptance criteria and end-to-end traceability.

Confirmation does not convert assumptions into facts. Unresolved items remain visible and may pause the affected design branch.

## 8. Confirmation decision

### Current checkpoint and review scope

| Item | Description |
|---|---|
| Current state | Alignment brief complete; detailed UX design paused |
| Review now | Background, users, scenarios, scope, terminology, requirements, and Stories |
| Not generated yet | Functional decomposition, page/task topology, detailed ASCII UI, specifications, and acceptance criteria |

### If changes are needed

Describe the item and desired change by section name, Story name, quoted wording, or optional ID. Include the reason/evidence when behavior or factual confidence changes.

```text
修改“目标用户”：主要用户改为租户管理员，安全审计员作为受影响角色。
修改“批量操作 Story”：本期不支持批量执行，移入后续范围。
```

The affected content will be updated, its downstream impact summarized, and the changed slice presented for confirmation again.

### If the baseline is confirmed

`确认并进入「详细 UX 设计」` will:

```text
baseline becomes Confirmed
  → derive user-recognizable functions
  → establish page/task topology and interaction logic
  → generate ASCII flows and visible UI states
  → colocate specifications and acceptance criteria
  → pause again only for a material contradiction or missing decision
```

| Decision | Baseline version | Story/scope coverage | Owner/date | Conditions or corrections | DEC ID |
| --- | --- | --- | --- | --- | --- |

Use the structured confirmation control when available:

- 修改需求与 Stories
- 确认并进入「详细 UX 设计」
- 补充分析后再确认

## 9. Change record

| Requested change | Downstream impact | Decision/status | Affected IDs | CHG ID |
| --- | --- | --- | --- | --- |
