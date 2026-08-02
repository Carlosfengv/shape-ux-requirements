# [Feature Name] · User Guide and Requirements Specification

> Detailed control/specification template. Do not use this as the default UX/PM reading experience. Create the reader-first guide with `ux-requirement-guide-template.md`, then use this structure only for required appendices or an explicitly requested exhaustive specification.

## Document information

| Item | Value |
|---|---|
| Purpose | |
| Audience | |
| Applicable roles | |
| Repository snapshot | Branch/commit or N/A |
| Scope | |
| Delivery mode | Single-file Markdown |
| Version/status | Draft / Provisional / Confirmed |
| Readiness | |
| Confirmed baseline | Version and DEC-BASELINE reference |

## 0. Repository context and existing behavior

> Omit this section only when no repository or codebase is available. Record that limitation in the document information.

### 0.1 Snapshot and analyzed scope

| Item | Finding |
|---|---|
| Repository/package | |
| Branch/commit | |
| Working tree status | |
| Applicable instructions | |
| Analyzed paths/modules | |
| Excluded or unavailable areas | |

### 0.2 Repository evidence

| Type | Repository-relative path:line | Evidence summary | Supports | Authority/freshness | Conflicts | SRC ID |
| --- | --- | --- | --- | --- | --- | --- |

### 0.3 Current behavior, documented intent, and requested delta

| Current status | Current implemented behavior | Documented intent | Requested behavior | Delta | Risk/dependency | Evidence | Area or ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

### 0.4 Documentation/code/test drift

| Sources in conflict | Observed difference | User impact | Requirement impact | Resolution owner/status | DRIFT ID |
| --- | --- | --- | --- | --- | --- |

## 0A. External product and industry landscape

> Include when public research was requested or materially improved category, terminology, comparable-product, standard, or solution-pattern understanding. External findings do not override repository evidence or owner decisions.

### 0A.1 Research scope

| Item | Value |
|---|---|
| Research questions | |
| Product/capability category | |
| Users and tasks | |
| Geography/industry | |
| Comparable product set | Direct / adjacent / reference products |
| Search/access date | |
| Exclusions and limitations | |

### 0A.2 Public source ledger

| Source/URL | Source class | Product/version/region | Access date | Supported claim | Confidence/limitation | SRC ID |
| --- | --- | --- | --- | --- | --- | --- |

### 0A.3 Comparable products and solution types

| Product or solution type | Why selected | Target users/jobs | Relevant capability | Documented pattern | Important constraint | Evidence |
|---|---|---|---|---|---|---|

| Capability/task | Product A | Product B | Product C | Recurring pattern | Material difference |
|---|---|---|---|---|---|

### 0A.4 Observed workflow patterns

```text
Observed pattern A
[Select scope] -> [Configure] -> [Pre-check] -> [Review] -> [Execute]
                                      |
                                      +-- issue --> [Correct and retry]

Observed pattern B
[Select object] -> [Execute] -> [Background result/notification]
```

### 0A.5 Applicability to this requirement

| Finding/pattern | Evidence | User/problem relevance | Fit with current product | Tradeoff/risk | Adopt/Adapt/Avoid/Investigate/N/A |
|---|---|---|---|---|---|

## 1. Requirement background and problem

### 1.1 Background and current state

[Explain the operating/business context, current process, and relevant change or trigger.]

### 1.2 Problem, evidence, and current workaround

| Problem/background statement | Evidence | Current workaround | Impact | Source/owner | Confidence | BG ID |
| --- | --- | --- | --- | --- | --- | --- |

### 1.3 Why now

[Explain urgency or timing only when supported by evidence or an explicit decision.]

## 2. Objectives, non-goals, and success

| Type | Objective/outcome | Success indicator/target | Evidence | Related SCN/REQ | OBJ ID |
| --- | --- | --- | --- | --- | --- |

### 2.1 Business objectives

### 2.2 User objectives

### 2.3 Non-goals and boundaries

| Item | Reason | Related IDs |
|---|---|---|

## 3. Target users and document audiences

### 3.1 Product target users

| Segment/type | Primary/secondary/affected | Responsibilities | Goals | Pain/workaround | Expertise/vocabulary | Decision rights | Evidence | ROLE ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### 3.2 Document audiences

| Document audience | What they need from this document | Sections used | AUD ID |
| --- | --- | --- | --- |

## 4. Target scenarios

| Target user | Trigger | Context/preconditions | Current approach and pain | Desired outcome | Frequency/scale | Risk | Evidence | SCN ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### 4.1 Primary scenario narratives

```text
When [trigger and context],
[target user] needs to [task or decision],
but currently [pain/workaround],
so they need to achieve [desired outcome]
without [important risk or constraint].
```

## 5. Concepts and terminology

### 5.1 Concept relationships

```text
[Concept] --relationship--> [Concept]
```

### 5.2 Terminology dictionary

| Source term | Product term | User explanation | Technical boundary | Evidence | CON ID |
| --- | --- | --- | --- | --- | --- |

## 6. Requirement register, story map, and release scope

### 6.1 Requirement register

| Requirement outcome/rule | Source/evidence | Priority | Release slice | Status | Decision owner | Related OBJ/SCN | REQ ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

### 6.2 Global story map

```text
[User outcome]
   |
   +-- [Activity A] --> TASK-01 --> US-01 --> [Release slice]
   |
   +-- [Activity B] --> TASK-02 --> JS-01 --> [Release slice]
```

| Outcome | Activity | User task | Priority | Release slice | Evidence | Status | TASK ID | US/JS reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### 6.3 Story-to-functional-point decomposition

Derive functional points only from the confirmed story baseline. A functional point is a user-recognizable capability, not a component, API, service, or implementation layer.

```text
[Confirmed user outcome]
        |
        v
[US/JS story] --> [FUNC capability] --> [User-visible result]
                         |
                         +-- may support several stories
```

| User outcome | Functional point/capability | User-visible result | Shared with | Evidence | FUNC ID | US/JS ID |
| --- | --- | --- | --- | --- | --- | --- |

### 6.4 Starting surface and experience topology

Choose the starting surface according to the user’s task. Use an overview for cross-object status, a resource list for collection management, a work queue for prioritized work, a detail-first entry for a known object, a direct task surface for a focused operation, or a configuration surface for policy and defaults.

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

| Starting-surface model | Primary content | Entry | Detail/action destination | Return/context behavior | PAGE/IA ID | Related US/JS | FUNC ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

### 6.5 Interaction logic model

Derive interaction logic before detailed ASCII UI:

```text
[User goal]
     |
     v
[Trigger, context, object, and state]
     |
     v
[Information or decision] -> [User action] -> [System response]
                                                  |
                                                  v
                                        [Visible feedback]
                                           /     |      \
                                     complete  cancel  problem
                                        |        |        |
                                     [Next]  [Return]  [Recover]
```

| User goal/task | Current context, object, and state | Information or decision needed | User action | System response | Visible feedback | Next, exit, or recovery | Interaction pattern | Related IDs |
|---|---|---|---|---|---|---|---|---|

| Material decision | User need or risk | Chosen behavior | Why it fits | Rejected alternative | Related IDs |
|---|---|---|---|---|---|

Use inline interaction for a small local change, a dialog for one bounded decision or short form, and a dedicated page or wizard for complex, multi-step, resumable, shareable, or reference-heavy work. Do not use drawers, side sheets, slide-over panels, or off-canvas task surfaces.

## 7. UX hypotheses, information architecture, navigation, and task flows

### 7.1 UX hypotheses and validation

| Hypothesis | Affected user/task | Validation task | Success signal | Failure signal | Current evidence | Status/owner | UXH ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

### 7.2 Information architecture

```text
Product
└── [Primary area]
    ├── [Page/object]
    └── [Page/object]
```

| Level | Page/object | User purpose | Parent/context | Entry points | Return path | Role/visibility rule | Existing/new | IA ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### 7.3 Navigation behavior

```text
[Entry]
   |
   v
[IA/PAGE destination] -- action --> [Next destination]
   |                                   |
   +-- denied/not found --> [Recovery] +-- back/return --> [Prior context]
```

| From | Trigger/link | Destination | Context carried | Back/return behavior | Permission/failure behavior | Related IDs | NAV ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

### 7.4 Primary task and decision flows

```text
[SCN/REQ Trigger]
        |
        v
[FLOW-01 Task step]
        |
        +-- [Decision A] --> [FLOW-02 Next step] --> [Complete]
        |
        +-- [Decision B] --> [FLOW-03 Recovery]  --> [Retry/Exit]
```

| Actor | User intent | Entry/precondition | User or system action | Decision/guard | System response | Next step/state | Interruption/recovery | Related IDs | FLOW/step ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### 7.5 Cross-role or asynchronous flow

> Repeat when the workflow changes owner, waits in the background, notifies another role, or requires re-entry.

```text
ROLE-01 User          Product/System          ROLE-02 Reviewer
     | submit               |                         |
     |--------------------->| create work            |
     |                      |------------------------>|
     | leave/wait           |                         | review
     |< - notification - - -|<------------------------|
     | reopen/result        |                         |
```

## 8. Page, feature, and task map

| Page or core feature | Surface model | Purpose | Applicable roles | Main subfeatures | Related US/JS outcomes | PAGE/FUNC ID |
| --- | --- | --- | --- | --- | --- | --- |

| User outcome | Entry | Result | SUB/TASK reference | Parent PAGE/FUNC | US/JS references |
| --- | --- | --- | --- | --- | --- |

### 8.1 ASCII UX confirmation queue

Confirm one dependency-ordered interaction slice at a time. Do not place candidate ASCII into the canonical chapters below until its confirmation record is complete.

| Order | Section or function | Confirmation scope | Status | Target chapter | Depends on | Included UI/STATE IDs | DEC ID |
|---:|---|---|---|---|---|---|---|

## 9. Page and core-feature chapters

### PAGE-01 · [Page or core feature name]

#### Page/feature purpose

- Purpose:
- Scope:
- Applicable roles:
- Starting-surface model:
- Entry paths:
- Key outcomes:
- Derived from FUNC/US/JS:
- Related requirements:

#### PAGE-01 · Overview

```text
┌────────────────────────────────────────────────────┐
│ [Page title]                          [A: Action]   │
├────────────────────────────────────────────────────┤
│ [B: Shared controls and filters]                   │
├────────────────────────────────────────────────────┤
│ [C: Primary content region]                        │
│                                                    │
├────────────────────────────────────────────────────┤
│ [D: Selection, status, or secondary region]        │
└────────────────────────────────────────────────────┘
```

##### Region and subfeature legend

| Region | Subfeature | User purpose | Main interactions | Focused UI needed? | SUB ID |
| --- | --- | --- | --- | --- | --- |

##### Page-level requirements

| Region/element | Requirement | Permission/state rule | User-visible result | Related IDs | SPEC ID |
| --- | --- | --- | --- | --- | --- |

##### Functional decomposition

| Subfeature | User purpose | Entry/region | Main interactions | Important states | Related IDs | SUB ID |
| --- | --- | --- | --- | --- | --- | --- |

#### SUB-01-01 · [Subfeature name]

##### Subfeature purpose and interaction

- User outcome:
- Applicable roles:
- Entry/region:
- Preconditions:
- Expected result:
- Related stories:

##### User stories and job stories

| User/context | Task or motivation | Expected value/outcome | Preconditions | Canonical priority/release reference | Main/alternate/recovery flow | Related SCN/REQ/FLOW | US/JS ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

##### Task and interaction flow

```text
[TASK/FLOW entry]
       |
       v
[UI-01-01 Default] --> [User action] --> [UI-01-02 Result]
       ^                    |
       +-- correct/retry <--+-- validation or system failure
```

##### Operating steps

1.
2.
3.

##### UI-01-01 · [Focused interaction] · Default

> Canonical only after its confirmation queue row is `Confirmed` and linked to `DEC-ASCII-###`.

```text
┌──────────────────────────────────────────────┐
│                                              │
│                                              │
│                                              │
└──────────────────────────────────────────────┘
```

###### Screen purpose

| User goal | Applicable roles | Entry condition | Success result | Related stories | UI ID |
| --- | --- | --- | --- | --- | --- |

###### Interface requirements

| UI element | Type | Display/data rule | Interaction rule | Permission/state rule | SPEC/AC IDs | Element ID |
| --- | --- | --- | --- | --- | --- | --- |

###### Interaction, validation, and state requirements

> Every user-visible interaction row must reference an ASCII frame shown in this chapter. Add a separate frame when the visible state changes materially.

| Event/input | Condition | User-visible behavior | Next/recovery | ASCII UI/STATE | SPEC/AC IDs | INT ID |
| --- | --- | --- | --- | --- | --- | --- |

###### Interaction-to-system contract

> Use only when the interaction crosses a service, job, integration, persistence, authorization, or concurrency boundary.

| Required system capability | Authorization/scope | Validation | Sync/async | Data/state change | Outcome variants | Idempotency/concurrency | Audit/observability | Test surface | INT/UI action | Source IDs | SYS ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

###### Accessibility, input, and adaptation

| UX constraint | Requirement | Related SPEC/NFR |
|---|---|---|
| Viewport/context | | |
| Keyboard and focus | | |
| Assistive technology | | |
| Non-color status cues | | |
| Text expansion/overflow | | |
| Narrow layout/dense data | | |

##### UI-01-01 · [Focused interaction] · Error or alternate state

```text
┌──────────────────────────────────────────────┐
│                                              │
└──────────────────────────────────────────────┘
```

###### State-specific requirements

| Trigger | User-visible behavior | Available action/recovery | ASCII UI/STATE | SPEC/AC IDs | INT ID |
| --- | --- | --- | --- | --- | --- |

##### Acceptance criteria

| Given | When | Then | SPEC/UI IDs | AC ID |
| --- | --- | --- | --- | --- |

##### Exceptions and recovery

| Scenario | User impact | Product behavior | Recovery | Audit requirement | IDs |
|---|---|---|---|---|---|

## 10. Cross-page task chapters

### TASK-01 · [Cross-page task]

```text
[PAGE-01 Entry]
      |
      v
[UI-01 Action] --> [PAGE-02 Review] --> [UI-02 Complete]
      ^                    |
      +-- return/recover --+
```

| Step | User action | System result | PAGE/SUB/UI ID | Requirement IDs |
| --- | --- | --- | --- | --- |

## 11. Cross-cutting requirements

### 11.1 Role and permission matrix

| Scope | View | Create | Change | Delete | Approve | Exceptional rules | Role |
| --- | --- | --- | --- | --- | --- | --- | --- |

### 11.2 Global lifecycle and states

```text
STATE-01 Draft
  +-- submit valid ------> STATE-02 Processing
  +-- cancel ------------> STATE-05 Cancelled

STATE-02 Processing
  +-- complete ----------> STATE-03 Complete
  +-- partial failure ---> STATE-04 Needs attention
  +-- retry exhausted ---> STATE-06 Failed
```

| User-facing state | Meaning | Entry condition | Available actions | Exit conditions | STATE ID |
| --- | --- | --- | --- | --- | --- |

| Event/action | Guard | Behavior | Feedback | Current STATE ID/name | Next STATE ID/name | IDs |
| --- | --- | --- | --- | --- | --- | --- |

### 11.3 Data, synchronization, and audit

| Data/event | Source | Scope | Freshness | Sensitive? | Retention/audit | User-visible behavior |
|---|---|---|---|---|---|---|

### 11.4 Non-functional requirements

| Quality | Scenario/scale | Target | Measurement | Failure behavior | Source | NFR ID |
| --- | --- | --- | --- | --- | --- | --- |

### 11.5 Shared accessibility and adaptation requirements

| Context | Requirement | Verification | Related UI/FLOW | NFR/SPEC ID |
| --- | --- | --- | --- | --- |

### 11.6 Shared interaction-to-system contracts

| Applicable interactions | Shared system behavior | Authorization/data boundary | Failure/recovery | Audit/observability | Test surface | SYS ID |
| --- | --- | --- | --- | --- | --- | --- |

## 12. Glossary

| Term | User definition | Related terms | Avoid/confuse with |
|---|---|---|---|

## 13. Traceability

| Outcome | Coverage | BG/OBJ/SCN/REQ/STMT | ROLE/CON/UXH | IA/NAV/TASK/FLOW | PAGE/FUNC/SUB/INT | US/JS | UI/STATE | SYS/SPEC/NFR | AC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 14. Internal control appendix

### 14.1 Evidence and decisions

| Statement | Evidence label | Source/owner | Confidence | Affected outputs | STMT ID |
| --- | --- | --- | --- | --- | --- |

### 14.2 Assumptions, conflicts, and research needs

| Item | Type | Impact | Validation/mitigation | Owner/status | ID |
| --- | --- | --- | --- | --- | --- |

## 15. Review and delivery summary

### 15.1 Delivery status and artifact map

| Item | Result |
|---|---|
| Delivery status | Complete / Complete with known limitations / Provisional / Blocked |
| Confirmed baseline | |
| Scope reviewed | |
| Reviewed on | |

| Artifact | What it contains | Status | Location |
|---|---|---|---|

### 15.2 Review results

| Review layer | Result | Findings repaired | Remaining limitation |
|---|---|---|---|
| Structural and deterministic | | | |
| Evidence and baseline | | | |
| Requirement and trace | | | |
| UX and interaction | | | |
| Human-readable document | | | |

### 15.3 Delivered document structure

Replace this example with the headings that actually exist.

```text
[file-name].md
├── Background, objectives, people, and scenarios
├── Confirmed stories and functional decomposition
├── Page/feature and task chapters with ASCII UI
├── Colocated interaction and system specifications
├── Cross-cutting requirements and traceability
└── Review and delivery summary
```

### 15.4 Remaining decisions, risks, and next action

| Decision, risk, or limitation | Impact | Owner/next action | Related IDs |
|---|---|---|---|

### 15.5 Recommended reading order

1. Human-readable UX requirement guide
2. Relevant page or cross-page task chapter
3. Cross-cutting requirements and system contracts
4. Traceability, evidence, decisions, and open questions
