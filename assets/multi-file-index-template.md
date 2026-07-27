# [Feature Name] · User Guide and Requirements Specification

## Document set

| Item | Value |
|---|---|
| Purpose | |
| Audience | |
| Repository snapshot | Branch/commit or N/A |
| Scope | |
| Delivery mode | Multi-file Markdown |
| Version/status | Draft / Provisional / Confirmed |
| Readiness | |
| Baseline version/status | Awaiting confirmation |
| Last updated | |

## How to read this document set

1. While the baseline is awaiting confirmation, start with [00c-requirement-alignment.md](00c-requirement-alignment.md) and confirm the analysis, scope, and stories.
2. After confirmation, start with [ux-requirement-guide.md](ux-requirement-guide.md) for the intended experience, ASCII UI, decisions, and risks.
3. Open repository or external research only when you need to verify the evidence behind a statement.
4. Use story, IA, page, workflow, cross-cutting, and traceability files for detailed implementation and review.

## Delivery plan

| Step | Deliverable | Status | Dependencies | Notes |
|---|---|---|---|---|
| 1 | Repository context and current-state evidence | Planned / N/A | — | Omit only when no repository is available |
| 2 | External product/category and industry landscape | Planned / N/A | Step 1 or repository N/A | Include when requested or materially relevant |
| 3 | Background, goals, scope, and readiness | Planned | Steps 1–2 or applicable N/A | |
| 4 | Target users and scenarios | Planned | Step 3 | |
| 5 | Concepts and product language | Planned | Steps 1–4 | |
| 6 | Requirement register, story map, priority, and release slicing | Planned | Steps 3–5 | |
| 7 | Requirement alignment brief and explicit story/scope confirmation | In progress | Step 6 | Pause detailed design until confirmed |
| 8 | Story-to-functional-point map and starting-surface/page topology | Blocked by confirmation | Step 7 confirmed | Derive the experience from confirmed stories |
| 9 | Interaction logic, UX hypotheses, and ASCII information architecture, navigation, task, decision, role, async, and state flows | Planned | Step 8 | No drawer-like surfaces |
| 10 | Page and feature map | Planned | Step 9 | |
| 11 | Page/core-feature documents with story details and ASCII UX | Planned | Step 10 | |
| 12 | Cross-page workflows with end-to-end ASCII flows | Planned | Step 11 | |
| 13 | Cross-cutting requirements and system contracts | Planned | Steps 1–12 | |
| 14 | Traceability and decisions | Planned | Steps 1–13 | |
| 15 | Human-readable UX requirement guide | Planned | Steps 1–14 | Summarize and link; do not duplicate dense control tables |
| 16 | Automated, semantic, and readability validation | Planned | Steps 1–15 | |
| 17 | Repair, revalidation, and final handoff summary | Planned | Step 16 | Do not mark complete with blocking findings |

## Document map

| File | Purpose | Status | Notes | Main IDs |
| --- | --- | --- | --- | --- |
| [ux-requirement-guide.md](ux-requirement-guide.md) | Reader-first context, users, scenarios, mental model, journeys, ASCII UI, key decisions, risks, and links to detail | Planned | Primary UX/PM reading experience | Reference IDs only |
| [00-repository-context.md](00-repository-context.md) | Snapshot, instructions, source inventory, current behavior, documented intent, drift, and requested delta | Planned / N/A | Omit only when no repository is available | SRC, DRIFT, CST, Q |
| [00b-industry-and-product-landscape.md](00b-industry-and-product-landscape.md) | Public sources, category taxonomy, comparable products, observed patterns, and project applicability | Planned / N/A | Include when external research was performed | Public SRC IDs |
| [00c-requirement-alignment.md](00c-requirement-alignment.md) | First-pass analysis, candidate stories, baseline confirmation, and change record | In progress | Confirm before detailed design | BG, OBJ, ROLE, SCN, CON, REQ, TASK, US, JS, DEC, CHG |
| [01-background-goals-and-scope.md](01-background-goals-and-scope.md) | Background, problem, objectives, non-goals, success, readiness, and scope | Planned |  | BG, OBJ, STMT, REQ, Q |
| [02-target-users-and-scenarios.md](02-target-users-and-scenarios.md) | Primary/secondary users, affected parties, document audiences, and target scenarios | Planned |  | ROLE, AUD, SCN |
| [03-concepts-and-language.md](03-concepts-and-language.md) | Concept model, terminology, and concept-specific evidence | Planned |  | CON |
| [04-story-map-and-release-scope.md](04-story-map-and-release-scope.md) | Requirement register, outcome/task-led story map, priority, and release slicing | Planned | Full US/JS definitions live in page or cross-page task files | REQ, TASK |
| [05-information-architecture-and-task-flows.md](05-information-architecture-and-task-flows.md) | Story-derived functional points, starting-surface/page topology, interaction logic and rationale, canonical UX hypotheses, and ASCII IA, navigation, task/decision, role, async, lifecycle, handoff, and recovery flows | Planned | US/JS and TASK IDs reference the story-map artifact; no drawer-like surfaces | FUNC, UXH, IA, NAV, FLOW |
| [06-page-and-feature-map.md](06-page-and-feature-map.md) | Page, feature, and subfeature inventory mapped to tasks | Planned | TASK IDs are references to the story-map artifact | PAGE, FUNC, SUB |
| [10-page-example.md](10-page-example.md) | Page operation guide, canonical stories, ASCII UI, local interaction/system specs, accessibility/adaptation, and AC | Planned | PAGE and SUB IDs reference the page-map artifact; replace with real page | US, JS, UI, SYS, SPEC, AC |
| [50-cross-page-workflows.md](50-cross-page-workflows.md) | End-to-end stories and ASCII workflows spanning pages | Planned | Omit if unnecessary | US, JS, TASK, FLOW, INT |
| [80-cross-cutting-requirements.md](80-cross-cutting-requirements.md) | Shared permissions, states, data, system contracts, accessibility/adaptation, audit, and NFR | Planned |  | SYS, SPEC, STATE, NFR |
| [90-traceability.md](90-traceability.md) | Coverage and cross-file ID mapping | Planned |  | All IDs |
| [91-decisions-and-open-questions.md](91-decisions-and-open-questions.md) | Decisions, assumptions, conflicts, and research | Planned |  | STMT, Q |

Delete unused planned rows instead of creating empty files.

## Coverage summary

| Area | Planned | Complete | Blocked | Notes |
|---|---:|---:|---:|---|
| Repository sources and current behavior | | | | |
| Documented intent, drift, and requested delta | | | | |
| External product/category and industry evidence | | | | |
| Comparable patterns and applicability decisions | | | | |
| Background and problem evidence | | | | |
| Objectives and non-goals | | | | |
| Target users and scenarios | | | | |
| Requirement register and release scope | | | | |
| Global story map and prioritization | | | | |
| Requirement/story baseline confirmation | | | | |
| Story-to-functional-point mapping | | | | |
| Starting-surface and page topology | | | | |
| UX hypotheses and validation | | | | |
| Information architecture and task flows | | | | |
| User/job stories | | | | |
| Pages/core features | | | | |
| Subfeatures | | | | |
| ASCII UI states | | | | |
| Requirement specifications | | | | |
| Interaction-to-system contracts | | | | |
| Accessibility and adaptation constraints | | | | |
| Acceptance criteria | | | | |

## Review and delivery summary

### Delivery status

| Item | Result |
|---|---|
| Delivery status | Complete / Complete with known limitations / Provisional / Blocked |
| Confirmed baseline | |
| Scope reviewed | |
| Reviewed on | |

### Artifact map

| Artifact | What it contains | Status | Location |
|---|---|---|---|

### Review results

| Review layer | Result | Findings repaired | Remaining limitation |
|---|---|---|---|
| Structural and deterministic | | | |
| Evidence and baseline | | | |
| Requirement and trace | | | |
| UX and interaction | | | |
| Human-readable document | | | |

### Remaining decisions and recommended reading order

| Item | Impact or purpose | Owner/next action | Location or related IDs |
|---|---|---|---|

## Blocking questions

| Question | Impact | Owner | Status | Q ID |
| --- | --- | --- | --- | --- |

## Change summary

| Version/date | Changed files | Summary | Decision/source | CHG ID |
| --- | --- | --- | --- | --- |
