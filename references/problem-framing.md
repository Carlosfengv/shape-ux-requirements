# Problem framing, objectives, people, and scenarios

Use this reference to ensure the requirement document explains why the work exists, who it serves, and where it creates value before describing features.

## Contents

- Evidence rules
- Background and problem
- Objectives and non-goals
- Target users and document audiences
- Target scenarios
- Required output tables
- Blocking test
- Quality check

## Evidence rules

Preserve the difference between:

- observed current-state fact;
- repository-confirmed implemented behavior;
- repository-documented intended behavior;
- source-backed problem evidence;
- stakeholder interpretation;
- product decision;
- inferred user need;
- unvalidated mental-model hypothesis;
- open research question.

Never turn a stakeholder request such as “add policy orchestration” into proof that users need that feature. Trace the request back to a user or business problem.

When a repository is available, use code, configuration, schemas, and tests to describe current implementation; use product documents and decision records to describe intended behavior. Report discrepancies explicitly instead of selecting one source silently.

## Background and problem

Write a short narrative that answers:

1. What business or operational environment exists today?
2. What event, change, or recurring pain triggered the request?
3. How do users handle the situation now?
4. What evidence shows the current approach is inadequate?
5. Who or what is affected?
6. What is the cost, risk, delay, or missed opportunity?
7. Why does the organization need to act now?

Use this table:

| Background/problem statement | Current evidence | Impact | Source/owner | Confidence | BG ID |
| --- | --- | --- | --- | --- | --- |

Do not invent urgency, metrics, research, or customer quotes.

## Objectives and non-goals

Separate:

| Type | Meaning |
|---|---|
| Business objective | Organizational result such as reduced operational risk or faster delivery |
| User objective | Result a target user needs to achieve |
| Product outcome | Observable behavior change the product should enable |
| Output | Feature, page, report, API, or other proposed solution |
| Success indicator | Evidence that the objective was achieved |
| Non-goal | Explicitly excluded result or problem |

Use:

| Objective type | Objective | Success indicator/target | Evidence | Related SCN/REQ | OBJ ID |
| --- | --- | --- | --- | --- | --- |

If a target value is unknown, mark it `TBD` and identify the decision owner. Do not convert an output such as “build a dashboard” into an objective.

## Target users and document audiences

Keep these concepts distinct:

- **Primary target user:** directly performs the central task and receives the main value.
- **Secondary target user:** performs supporting, administrative, review, or exception tasks.
- **Affected party:** does not operate the feature but experiences its consequences.
- **System actor:** automated service or integration.
- **Document audience:** person reading the requirement, such as PM, UX, engineering, QA, operations, or customer enablement.

Describe target users with job-relevant attributes, not fictional demographics:

| Segment/type | Responsibilities | Goals | Current pain/workaround | Expertise/vocabulary | Decision rights | Evidence | ROLE ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

Do not create decorative personas. Include only attributes that affect terminology, information needs, permissions, workflow, risk, or interaction design.

Describe document readers separately:

| Document audience | What they need from this document | Sections used | AUD ID |
| --- | --- | --- | --- |

## Target scenarios

A scenario is a concrete context in which a target user attempts to achieve an outcome. It is not a feature list.

Use:

| Target user | Trigger | Context/preconditions | Current approach and pain | Desired outcome | Frequency/scale | Risk | Evidence | SCN ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

For each primary scenario, write a concise narrative:

```text
When [trigger and context],
[target user] needs to [task or decision],
but currently [pain/workaround],
so they need to achieve [desired outcome]
without [important risk or constraint].
```

Mark future or hypothetical scenarios explicitly. Do not present generated examples as observed usage.

## Required output tables

For a full document, include:

1. background and problem narrative;
2. background/evidence table;
3. objective, success, and non-goal table;
4. target-user table;
5. document-audience table;
6. target-scenario table and primary-scenario narratives;
7. trace links from `BG`, `OBJ`, `ROLE`, and `SCN` to downstream requirements.

## Blocking test

Stop and clarify when any of these are unknown and a plausible answer would change the product direction:

- the actual problem;
- primary business or user objective;
- primary target user;
- primary target scenario;
- current workaround or target outcome;
- evidence or owner for a high-risk claim.

Allow a provisional exploratory draft only when the user explicitly accepts assumptions.

## Quality check

Reject or revise framing when:

- it opens with a proposed feature instead of the current problem;
- the background is generic market prose with no connection to the input;
- objectives describe outputs rather than outcomes;
- target users are only job titles with no task context;
- document readers and product users are mixed together;
- scenarios omit trigger, context, current pain, or desired outcome;
- success metrics or user research are invented;
- downstream features cannot trace back to an objective and scenario.
