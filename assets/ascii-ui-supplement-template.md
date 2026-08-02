# [Feature or task] · ASCII UI Supplement

> Purpose: Complete or improve missing ASCII UI from an existing requirement document without expanding into an unrelated full specification.

## 1. Source and supplement status

| Item | Value |
|---|---|
| Source document/path | |
| Source version/date | |
| Target user/task | |
| Supplement scope | |
| Status | Provisional / Ready for review / Confirmed |
| Known limitations | |

## 2. Delivery coverage notice

| Artifact | Included/Provisional/Omitted/Blocked/N/A | Document basis | Impact of omission | Next action |
|---|---|---|---|---|
| Task/decision flow | | | | |
| Page overview | | | | |
| Focused interaction UI | | | | |
| Critical UI states | | | | |
| Local specifications | | | | |
| Accessibility/adaptation | | | | |
| Acceptance coverage | | | | |

## 3. Document-derived interaction baseline

| Topic | Interpreted requirement | Confidence | Gap or assumption | Source ID/section |
| --- | --- | --- | --- | --- |
| User goal and role |  |  |  |  |
| Trigger and entry |  |  |  |  |
| Objects and terminology |  |  |  |  |
| Main actions |  |  |  |  |
| Permissions |  |  |  |  |
| States and lifecycle |  |  |  |  |
| Success outcome |  |  |  |  |
| Failure and recovery |  |  |  |  |

## 4. Questions and assumptions

### Blocking questions

| Question | Why it changes the UI | Owner/status | Q ID |
| --- | --- | --- | --- |

### Provisional assumptions

| Assumption | Validation needed | Affected FLOW/UI/SPEC | STMT ID |
| --- | --- | --- | --- |

## 5. ASCII UX confirmation queue

Confirm one dependency-ordered supplement slice at a time. Keep candidate ASCII out of the canonical supplement sections below until confirmation.

| Order | Section or function | Confirmation scope | Status | Target section | Depends on | Included UI/STATE IDs | DEC ID |
|---:|---|---|---|---|---|---|---|

## 6. ASCII task and state flow

```text
[TASK/FLOW entry]
       |
       v
[UI-01 Default] -> [User action] -> [UI-02 Result]
       ^                  |
       +-- correct/retry <-+-- validation or system failure
```

## 7. Page overview

```text
PAGE-01 · [Page or feature] · Overview
┌────────────────────────────────────────────────────┐
│ [Page title]                          [A: Action]   │
├────────────────────────────────────────────────────┤
│ [B: Context, scope, filters, or navigation]        │
├────────────────────────────────────────────────────┤
│ [C: Primary task/content region]                   │
├────────────────────────────────────────────────────┤
│ [D: Status, selection, help, or secondary region]  │
└────────────────────────────────────────────────────┘
```

| Region | User purpose | Main interactions | Related source | SUB ID |
| --- | --- | --- | --- | --- |

## 8. Focused ASCII UI states

| Interaction behavior | Visible change or feedback | ASCII UI/STATE | Source/SPEC/AC | INT ID |
| --- | --- | --- | --- | --- |

### UI-01 · [Interaction] · Default

> Canonical only after its confirmation queue row is `Confirmed` and linked to `DEC-ASCII-###`.

```text
┌──────────────────────────────────────────────┐
│                                              │
│                                              │
│                                              │
└──────────────────────────────────────────────┘
```

| User goal | Applicable roles | Entry condition | Success result | Related story/source | UI ID |
| --- | --- | --- | --- | --- | --- |

| UI element | Display/data rule | Interaction rule | Permission/state rule | Source/SPEC/AC | Element ID |
| --- | --- | --- | --- | --- | --- |

### UI-02 · [Interaction] · Error, alternate, or recovery

```text
┌──────────────────────────────────────────────┐
│                                              │
└──────────────────────────────────────────────┘
```

| Trigger/condition | User-visible behavior | Available action | Next state | Recovery | Source/SPEC/AC |
|---|---|---|---|---|---|

Repeat focused frames only for materially different states.

## 9. Accessibility and adaptation

| Constraint | Requirement | Related UI/SPEC |
|---|---|---|
| Keyboard and focus | | |
| Assistive technology | | |
| Error association and announcements | | |
| Non-color status cues | | |
| Text expansion and overflow | | |
| Narrow viewport or dense data | | |

## 10. Coverage and optimization review

| Check | Result | Adjustment made or remaining gap |
|---|---|---|
| Uses approved user terminology | | |
| Primary action and hierarchy are clear | | |
| Main, alternate, and recovery paths are visible | | |
| Every user-visible interaction maps to a displayed ASCII UI/state | | |
| Permissions and disabled behavior are explained | | |
| Critical states are represented or explicitly omitted | | |
| Every introduced element traces to source evidence | | |
| Unsupported behavior is labeled as an assumption | | |
| ASCII and adjacent specification agree | | |
| Every canonical UI/STATE is covered by a confirmed DEC-ASCII record | | |

## 11. Revision summary

| Version/date | Source change or review finding | ASCII/spec adjustment | Remaining decision |
|---|---|---|---|
