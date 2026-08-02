# [Feature or experience name]

> A human-readable UX requirement guide for product, design, domain, and delivery review.

## At a glance

| Question | Answer |
|---|---|
| What problem are we solving? | |
| Who is most affected? | |
| What outcome should improve? | |
| What is in scope now? | |
| Status | Draft / Provisional / Confirmed |
| Delivery profile | Compact / Balanced / Modular |
| Primary document | ux-requirements.md |
| Split rationale | None for Compact; otherwise state the reader/owner/review/release/readability reason |
| Confirmed baseline | [version and DEC-BASELINE link] |
| Most important open decision | |

### How to read this document

Start with the problem and target scenario, then review the experience overview and relevant task chapters. Detailed evidence, system contracts, matrices, and traceability are linked from the supporting-specification section.

## 1. Why this needs to change

[Explain the current situation, trigger, user impact, workaround, and why the change matters in two to four short paragraphs.]

| Today | Desired outcome | Why it matters |
|---|---|---|
| | | |

### Goals

- User outcome:
- Business outcome:
- Success signal:

### Boundaries

**In scope**

-

**Not in scope**

-

## 2. Who is affected

### Primary user

- Role and context:
- What they are responsible for:
- What they need to accomplish:
- Current pain or workaround:
- Relevant expertise and vocabulary:

### Other affected people

| Person or role | How they are affected | What they need |
|---|---|---|

## 3. The target scenario

> When [trigger and context], [user] needs to [task], so they can [outcome] without [risk or friction].

```text
[Trigger]
    |
    v
[Current task/workaround] -> [Pain, delay, or risk]
    |
    v
[Desired experience] -> [User outcome]
```

### What must be true

- Entry condition:
- Required permission or data:
- Completion signal:
- Important failure or recovery need:

Trace: [SCN / OBJ / REQ references]

## 4. Mental model and product language

[Explain the small set of concepts a user must understand and how they relate.]

```text
[User-recognizable object]
    +-- contains --> [Related object]
    +-- changes through --> [Lifecycle]
    +-- is acted on by --> [User role]
```

| Internal/source term | Product term | Plain-language meaning | Avoid/confuse with |
|---|---|---|---|

## 5. Experience overview

[Summarize the proposed experience and the design principles a reviewer should notice.]

### From stories to the experience

```text
[Confirmed US/JS]
      |
      v
[FUNC user-recognizable capability]
      |
      v
[Overview / resource list / work queue / detail / direct task / configuration]
      |
      +-- inspect or select --> [Detail destination]
      +-- act or create -----> [Task, edit, or wizard destination]
      +-- complete/cancel ---> [Return with prior context preserved]
```

| Story/outcome | Functional point | Starting surface | Detail/action continuation |
|---|---|---|---|
| | | | |

Choose the starting surface from the user’s task; an overview or resource list is not mandatory for every experience.

### Interaction logic

Explain how the user moves from intent to a visible result before presenting detailed screens.

```text
[User goal]
     |
     v
[Trigger, context, object, and current state]
     |
     v
[Information or decision needed]
     |
     v
[User action] -> [System response] -> [Visible feedback]
     |                                      |
     +-- cancel --> [Return with context]   +-- complete --> [Next useful step]
     |
     +-- problem --> [Explain, preserve work, and recover]
```

| User goal/task | Context and decision | Chosen behavior | Visible feedback | Next or recovery | Pattern rationale | Related IDs |
|---|---|---|---|---|---|---|
| | | | | | | |

Use inline interaction for small local changes, a dialog for one bounded decision or short form, and a dedicated page or wizard for complex, multi-step, resumable, or reference-heavy work. Do not use drawers, side sheets, slide-over panels, or off-canvas task surfaces.

```text
[Find or enter the task]
          |
          v
[Understand current state]
          |
          v
[Take action] -> [Review consequence] -> [Complete]
      |                    |
      +-- cannot proceed --+--> [Explain and recover]
```

### Experience principles

- Make the current scope and object clear.
- Make the next action and its consequence understandable.
- Prefer recognition, prevention, and preserved context over recall and rework.
- Use proportional feedback and provide cancel, exit, and recovery paths.
- Explain consequences before commitment.
- Keep recovery close to the failure.
- Use the approved product language.

### Main destinations

| Destination | User purpose | How users arrive | What they leave with |
|---|---|---|---|

### ASCII UX confirmation progress

The detailed experience is confirmed one dependency-ordered section or function at a time. Candidate ASCII remains outside this canonical guide until confirmation.

| Order | Section or function | What was confirmed | Status | Canonical location | Depends on | Included UI/STATE IDs | DEC ID |
|---:|---|---|---|---|---|---|---|

## 6. Task and interface chapters

> Repeat this section for each primary user-recognizable outcome.

### [Task name]

**User goal:**  
**When and where:**  
**Preconditions:**  
**Expected result:**  

Trace: [TASK / US or JS / REQ references]

#### How the task works

```text
[Start]
   |
   v
[Review context] -> [Configure or choose] -> [Confirm] -> [Result]
                           |
                           +-- issue --> [Explain] -> [Correct/retry or exit]
```

#### Steps

1. 
2. 
3. 

#### Interface overview

> What to notice: [Explain the hierarchy, primary decision, or state shown below.]
> Include this frame as canonical content only after its confirmation unit is confirmed.

```text
PAGE · [Page or feature] · Overview
┌────────────────────────────────────────────────────┐
│ [Page title]                         [Main action] │
├────────────────────────────────────────────────────┤
│ [Scope, context, filters, or navigation]           │
├────────────────────────────────────────────────────┤
│ [Primary content and task region]                  │
│                                                    │
├────────────────────────────────────────────────────┤
│ [Status, selection, guidance, or secondary action] │
└────────────────────────────────────────────────────┘
```

| Area | What the user sees | What the user can do | Important behavior |
|---|---|---|---|

#### Focused interaction

```text
UI · [Interaction] · [State]
┌──────────────────────────────────────────────┐
│ [Title and short guidance]                   │
├──────────────────────────────────────────────┤
│ [Fields, choices, summary, or result]        │
│                                              │
├──────────────────────────────────────────────┤
│ [Secondary action]          [Primary action] │
└──────────────────────────────────────────────┘
```

**What the user sees**

-

**What the user can do**

-

**What happens next**

-

| Interaction | Visible change or feedback | Detail link | ASCII UI/state |
| --- | --- | --- | --- |

#### Important states and recovery

| Situation | What the user experiences | Available next step | Design note |
|---|---|---|---|
| Loading or waiting | | | |
| Empty or unavailable | | | |
| Validation problem | | | |
| System failure | | | |
| Partial success | | | |
| Success | | | |

> Add a focused ASCII frame for every row above that changes what the user sees, can do, or use to recover.

#### Decisions and assumptions

> **Decision needed:**  
> **Why it matters:**  

> **Assumption:**  
> **How to validate it:**  

Detailed requirements: [link to local specification and acceptance criteria]

## 7. Cross-task rules readers should know

Summarize only the rules that change the experience across several tasks.

| Topic | What users experience | Important exception | Detail link |
|---|---|---|---|
| Permissions | | | |
| Lifecycle | | | |
| Background work | | | |
| Audit or history | | | |
| Accessibility/adaptation | | | |

## 8. Scope and release view

```text
Now
  +-- [Outcome/task]
  +-- [Outcome/task]

Later
  +-- [Deferred outcome/task]
```

| Outcome or task | Priority/release | Included behavior | Deferred or unresolved |
|---|---|---|---|

## 9. Decisions, risks, and open questions

| Item | Why it matters | Owner/status | Affected experience |
|---|---|---|---|

## 10. Delivery coverage

| Artifact | Status | What is missing or provisional | Next action |
|---|---|---|---|
| User and scenario framing | | | |
| Mental model and terminology | | | |
| Task flows | | | |
| ASCII UI and critical states | | | |
| Detailed requirements | | | |
| Acceptance coverage | | | |

## Supporting specification and evidence

Use links rather than copying dense control material into the main guide.

- Repository/current-state evidence:
- Industry/comparable-product research:
- Requirement register and story map:
- IA, navigation, and detailed flows:
- Page/local specifications:
- Cross-cutting rules and system contracts:
- Acceptance criteria and traceability:
- Full decisions, assumptions, and source ledger:

## 11. Review and delivery summary

### Delivery status

| Item | Result |
|---|---|
| Delivery status | Complete / Complete with known limitations / Provisional / Blocked |
| Delivery profile | Compact / Balanced / Modular |
| Split rationale | |
| Confirmed baseline | |
| Scope reviewed | |
| Reviewed on | |

### Review results

| Review layer | Result | Findings repaired | Remaining limitation |
|---|---|---|---|
| Structural and deterministic | | | |
| Evidence and baseline | | | |
| Requirement and trace | | | |
| UX and interaction | | | |
| Human-readable document | | | |

### Delivered document structure

Replace this example with the headings that actually exist.

```text
ux-requirements.md
├── Background, objectives, people, and scenarios
├── Confirmed stories and functional points
├── Page/task chapters with ASCII UI and local specifications
├── Cross-cutting requirements
├── Traceability, evidence, and decisions
└── Review and delivery summary
```

### Remaining limitations and next action

| Decision, risk, or limitation | Impact | Owner/next action | Related IDs |
|---|---|---|---|

Recommended reading order:

1. This UX requirement guide
2. Relevant page or cross-page task specification
3. Cross-cutting requirements
4. Traceability, evidence, and decisions
