---
name: shape-ux-requirements
description: Assess and shape complex enterprise requirements into repository-grounded, user-mental-model-aligned, human-readable Markdown guides, specifications, and progressively user-confirmed ASCII UX. Use when PMs or UX designers need current-state analysis, clarification, public research on comparable products or industry approaches, problem framing, users and scenarios, terminology, ASCII-first IA/task/decision/state/cross-role flows, stories, page/subfeature decomposition, ordered ASCII confirmation, full-state ASCII UI, missing-ASCII supplementation, interaction/system contracts, accessibility, acceptance criteria, or traceability. Inspect repository instructions, code, tests, product copy, schemas, documents, and relevant authoritative public sources before proposing behavior. Default to a reader-first UX/requirements guide with dense control detail in appendices or supporting files. Do not use for visual styling, procurement ranking, or technical architecture alone.
---

# Shape UX Requirements

## Overview

Transform complex enterprise requirements into an evidence-aware product model that PMs, UX designers, engineers, and reviewers can understand and verify. Assess the input before producing solutions; clarify blocking gaps, translate engineering concepts into precise user-facing language, and connect every story, interaction, specification, and acceptance criterion.

Respond in the user's language unless asked otherwise. Use `ASCII`, not `ASII`, when naming text-based interaction drafts.

## Operating rules

1. Treat user-provided statements as inputs, not automatically as verified facts.
2. When a repository is available, inspect relevant code and documentation before evaluating completeness or asking for information the repository may contain.
3. Separate current implementation from intended behavior. Treat code/tests as implementation evidence and product docs/decisions as intent evidence; report drift instead of silently choosing one.
4. Separate completeness, internal consistency, and factual accuracy. Verify factual accuracy only against provided sources, repository evidence, connected authoritative sources, or explicit domain-owner confirmation.
5. Label facts, decisions, inferences, assumptions, unknowns, and conflicts. Never hide uncertainty in polished prose.
6. For a new or materially revised requirement, stop at a user-confirmed requirement/story baseline before detailed IA, specifications, or ASCII UI; stop earlier when a blocking gap could materially change users, scope, permissions, object model, lifecycle, or risk behavior.
7. Ask only 1–3 high-impact clarification questions per round. Prefer a structured choice/input component when available. At every confirmation pause, explicitly offer a modification path with correction guidance and a continuation path naming the next phase and its expected outputs/state.
8. Continue with clearly labeled assumptions only when gaps are non-blocking or the user explicitly requests a provisional draft.
9. Preserve engineering meaning while translating concepts into user-facing product language.
10. Do not expose implementation concepts in the UI unless users need them to make decisions or complete tasks.
11. Keep stable IDs throughout the analysis. Do not silently rename concepts or change rules between sections.
12. Write for UX/PM readers: lead with plain-language meaning and compact ASCII, keep tables narrow, place descriptive/name/outcome columns first and all stable or related ID columns last, and move dense matrices, contracts, and trace detail to appendices.
13. Deliver a completed document request as `.md`. Use chat for clarification and confirmation, but persist the alignment brief, accepted baseline, confirmation record, and final artifacts in Markdown files.
14. Establish the outcome/task/story backbone before committing to pages. Then validate information architecture and task/decision flows before detailed screens.
15. Treat ASCII as a behavioral and structural contract, not visual proof. Anchor every user-visible interaction behavior to at least one ASCII `UI`/`STATE` frame; prose, a flow, or a table alone is insufficient. Record viewport, input, accessibility, density, and responsive constraints that ASCII cannot show.
16. Treat external product and industry research as comparative context. Never let it override repository evidence, project-specific user needs, or explicit owner decisions.
17. Never silently omit an expected artifact in narrow delivery. Show coverage status, impact, and the next step, especially when ASCII UI is omitted, provisional, or blocked.

## Load references progressively

- Read [references/repository-discovery.md](references/repository-discovery.md) first when a project repository or codebase is available.
- Read [references/industry-and-product-research.md](references/industry-and-product-research.md) when internet research could clarify the category, related capabilities, comparable products, current standards, or mainstream approaches.
- Read [references/intake-readiness.md](references/intake-readiness.md) before assessing any new or revised input.
- Read [references/problem-framing.md](references/problem-framing.md) before defining background, objectives, target users, document audiences, target scenarios, scope, or success measures.
- Read [references/concept-language.md](references/concept-language.md) when the input contains engineering terminology, translated terms, unfamiliar domain objects, or naming work.
- Read [references/stories-and-acceptance.md](references/stories-and-acceptance.md) before producing stories or acceptance criteria, then [references/confirmation-gate.md](references/confirmation-gate.md) before any user confirmation pause or baseline approval.
- Read [references/information-architecture-and-task-flows.md](references/information-architecture-and-task-flows.md) after the story backbone and before defining navigation, cross-page journeys, role handoffs, or detailed screen structure.
- Read [references/interaction-logic-principles.md](references/interaction-logic-principles.md), [references/ascii-interactions.md](references/ascii-interactions.md), and [references/progressive-ascii-confirmation.md](references/progressive-ascii-confirmation.md) before organizing, presenting, confirming, or writing detailed ASCII UX.
- Read [references/human-readable-requirements.md](references/human-readable-requirements.md) before composing any UX/PM-facing requirement document.
- Read [references/spec-and-traceability.md](references/spec-and-traceability.md) before producing specifications, matrices, or the final quality audit.
- Read [references/integrated-guide.md](references/integrated-guide.md) before producing a full document, user manual, feature guide, or combined user-guide/specification deliverable.
- Read [references/markdown-delivery.md](references/markdown-delivery.md) before structuring artifacts, then [references/review-and-handoff.md](references/review-and-handoff.md) before final review, repair, completion status, or user handoff.

Use templates from `assets/` only when the user wants a reusable artifact or when a full end-to-end deliverable is requested:

- `assets/repository-context-template.md`
- `assets/requirement-intake-template.md`; `assets/requirement-alignment-template.md`
- `assets/clarification-log-template.md`
- `assets/ascii-ui-supplement-template.md`
- `assets/ux-requirement-guide-template.md`
- `assets/enterprise-requirement-output-template.md`
- `assets/multi-file-index-template.md`

Use `assets/ux-requirement-guide-template.md` as the default human-readable main document. Use `assets/enterprise-requirement-output-template.md` only for a detailed control appendix or when the user explicitly requests one exhaustive specification. Localize headings and labels; keep stable IDs, code identifiers, and repository paths unchanged.

## Select the working mode

Infer the smallest mode that satisfies the request:

| Mode | Use for | Required behavior |
|---|---|---|
| Intake assessment | Reviewing raw input or determining readiness | Assess, identify evidence gaps, and clarify; do not generate a final solution |
| Terminology shaping | Translating engineering or domain concepts | Perform a lightweight assessment, then build the concept language |
| Story shaping | Producing user/job stories and acceptance criteria | Establish a usable baseline and concept vocabulary first |
| Interaction shaping | Producing ASCII UI and flows | Establish IA, task flows, stories, objects, permissions, lifecycle, and state behavior first |
| ASCII UI supplement | Completing or improving missing UI from an existing document | Report delivery coverage, extract the interaction baseline, generate traceable flows/frames when sufficient, or ask focused blocking questions |
| Integrated guide | Human-readable UX/PM guide plus supporting requirements | Lead with context, users, journeys, and ASCII; keep compact local behavior nearby and move dense control detail to appendices |
| Markdown delivery | Creating the final artifact | Use one `.md` for small scope or a planned, linked Markdown document set for large scope |
| Full shaping | End-to-end requirement analysis | First confirm the analysis/story baseline, then run the detailed design phases and integrated guide output contract |
| Existing-spec audit | Reviewing an existing PRD/spec | Preserve source IDs where possible, report gaps and conflicts, and propose revisions separately |
| Repository-grounded shaping | Analyzing requirements inside a project repository | Inspect instructions, code, tests, UI copy, schemas, and docs before clarification; document current behavior and requested delta |
| Industry/product research | Understanding an unfamiliar category, comparable products, or mainstream solutions | Search current public sources, compare documented patterns, and assess project applicability without turning competitor features directly into requirements |

Do not force the complete artifact when the user asks for one narrow output. Still perform the minimum upstream checks required to make that output trustworthy.

For every narrow delivery, state which adjacent artifacts are Included, Provisional, Omitted, Blocked, or Not applicable. When user-visible interaction is in scope and ASCII UI is missing, apply `references/ascii-interactions.md` and use `assets/ascii-ui-supplement-template.md`: generate the targeted supplement from sufficient document evidence, or explain the blocking gaps before drawing final frames. Honor an explicit UI exclusion, but disclose its implementation and review impact.

## End-to-end workflow

### Phase 0: Ground in the repository

When a repository is available, apply `references/repository-discovery.md` before analyzing the request.

1. Locate the repository root and record a read-only snapshot identifier such as branch and commit when available.
2. Read applicable repository instructions, including root and scoped `AGENTS.md`, `CLAUDE.md`, `README`, contribution guidance, and documentation indexes.
3. Inventory relevant files with `rg --files`; avoid generated, vendored, dependency, build, coverage, secret, and credential paths.
4. Search user terms, synonyms, existing UI language, engineering terms, routes, models, permissions, states, APIs, and tests with `rg`.
5. Trace existing behavior across documentation, UI, domain model, service/API, authorization, persistence, and tests as relevant.
6. Build a repository evidence ledger and a current-versus-requested delta table.
7. Identify documentation/code drift, partial implementations, legacy terminology, and constraints.
8. Ask only questions that remain unresolved after repository discovery.

Keep repository discovery read-only. Do not change code, configuration, data, or product documentation unless the user separately requests implementation or edits.

### Phase 0A: Research the public landscape when relevant

Apply `references/industry-and-product-research.md` after the initial repository/request boundary is understood and before asking questions that public evidence could answer.

1. Define research questions, product/capability category, users/tasks, region/industry, date, and exclusions.
2. Search current category terminology, official comparable-product documentation, standards, and credible independent sources.
3. Separate direct, adjacent, and reference products; record `SRC-WEB-###` evidence with URLs, dates, editions/regions, and limitations.
4. Compare user-visible capabilities, workflows, constraints, and failure/recovery behavior; use ASCII for material sequence differences.
5. State the observed sample before calling a pattern common or mainstream.
6. Classify each finding as Adopt, Adapt, Avoid, Investigate, or Not applicable.
7. Do not use external research to decide internal policy, priority, permission, lifecycle, or risk ownership.

### Phase 1: Inventory the input

Extract and identify:

- source documents and source authority;
- repository snapshot, applicable instructions, relevant code/docs/tests, existing UI language, and current behavior when available;
- business and product background, current state, trigger, urgency, and why now;
- current-state statements versus proposed behavior;
- user and system actors;
- problem evidence, current workarounds, impact, business objectives, user objectives, non-goals, and success measures;
- primary target users, secondary users, affected parties, document readers, and target scenarios;
- business objects, operations, relationships, and lifecycle states;
- business rules, permissions, data boundaries, dependencies, and non-functional constraints;
- engineering terms, translated phrases, overloaded words, and undefined acronyms;
- explicit decisions, implicit assumptions, unknowns, and contradictions.

Assign stable IDs:

| Prefix | Entity |
|---|---|
| `SRC` | Source |
| `STMT` | Fact, claim, decision, inference, or assumption |
| `BG` / `OBJ` | Background statement or objective |
| `AUD` / `SCN` | Document audience or target usage scenario |
| `ROLE` | User or system actor |
| `CON` | Concept |
| `UXH` | UX or mental-model hypothesis |
| `IA` / `NAV` | Information-architecture node or navigation rule |
| `REQ` | Requirement |
| `Q` | Open question |
| `US` / `JS` | User story / job story |
| `TASK` / `FLOW` | User task or task/decision flow |
| `PAGE` / `FUNC` / `SUB` / `INT` | Page, feature, subfeature, or interaction scenario |
| `UI` / `STATE` | Interface or state |
| `SPEC` | Specification |
| `SYS` | Interaction-to-system contract |
| `AC` | Acceptance criterion |
| `NFR` | Non-functional requirement |
| `DRIFT` | Code, test, or documentation drift |
| `DEC` / `CHG` / `CFLT` / `CST` | Decision, confirmed-baseline change, conflict, or constraint |

Reuse existing source IDs when they are stable and unambiguous.

### Phase 2: Assess readiness

Apply the readiness model from `references/intake-readiness.md`.

Produce:

1. a concise restatement of the current understanding;
2. an input assessment table;
3. a statement and evidence ledger;
4. a conflict list;
5. prioritized questions.

Choose one readiness status:

- `Ready`
- `Ready with assumptions`
- `Clarification required`
- `Evidence required`
- `Conflicted`

Do not use a numeric score as the sole gate.

### Phase 3: Clarify and baseline

If the status is `Clarification required`, `Evidence required`, or `Conflicted`:

1. Confirm that the relevant repository, provided sources, and applicable public sources were searched before selecting questions.
2. Select the highest-impact 1–3 questions and choose the appropriate interaction type.
3. Use `request_user_input` or the host's equivalent structured choice component for bounded, mutually exclusive decisions when available.
4. Use direct free text for explanations, source material, unknown domain facts, or questions whose answers cannot be safely enumerated.
5. Explain why each answer changes the downstream design.
6. Wait for answers before asking the next batch.
7. Update affected statements, conflicts, and questions after every answer.
8. Record the decision owner or source when known.
9. Summarize the update, then offer `修改当前内容` or a named continuation action with the next phase's expected outputs and state.
10. Repeat the readiness check only after the user chooses to continue.

Do not continue to final stories, UI, or specifications until blockers are resolved, unless the user explicitly asks for a provisional draft. Mark a provisional draft prominently and keep every unresolved decision visible.

Once ready, establish a baseline table containing:

- confirmed background, problem, and why-now context;
- business and user objectives, non-goals, and success measures;
- primary and secondary target users, affected parties, and document audience;
- target scenarios with triggers, context, desired outcomes, and evidence;
- confirmed scope;
- facts and source-backed claims;
- product decisions;
- permitted assumptions;
- unresolved non-blocking questions;
- out-of-scope items.

### Phase 4: Frame the problem, objectives, people, and scenarios

Apply `references/problem-framing.md`.

When a repository is available, precede the problem framing with a repository/current-state evidence summary. Clearly distinguish implemented behavior, documented intent, the user's requested behavior, and the resulting delta.

Produce:

1. a concise background narrative covering current state, trigger, why now, evidence, workaround, and impact;
2. separate business objectives and user objectives;
3. explicit non-goals and boundaries;
4. measurable success indicators without inventing absent targets;
5. primary target users, secondary users, affected parties, and document audiences;
6. target scenario cards covering trigger, context, task, pain, desired result, frequency, risk, and evidence;
7. a trace from each objective and scenario to source statements or labeled assumptions.

For a full requirement document, treat an unknown problem, objective, primary target user, or primary target scenario as blocking unless the user explicitly requests an exploratory draft.

### Phase 5: Build the concept and language model

Apply `references/concept-language.md`.

For each important concept:

1. Inventory the existing product language in repository UI copy, navigation, help text, errors, user documentation, domain/API names, and internal implementation names.
2. Preserve the original engineering term and technical definition.
3. Identify the user role, task, and decision associated with it.
4. Determine whether to preserve, expose, rename, merge, split, or hide the concept.
5. Propose a stable product term.
6. Write a short UI explanation, contextual explanation, full definition, example, and boundary.
7. Record confusing alternatives and forbidden terms.
8. Label the evidence behind the mental-model claim.

Represent important relationships such as containment, ownership, inheritance, dependency, creation, synchronization, and lifecycle transitions. Flag mismatches between the system model and the user's likely mental model.

Identify material unverified claims about terminology, findability, sequence, comprehension, risk perception, or completion signals. Keep concept-specific evidence with `CON`, then consolidate each material claim once in the canonical `UXH` register during Phase 7. Do not present a generated mental model as validated research.

### Phase 6: Shape requirements, scope, and the story backbone

Apply `references/stories-and-acceptance.md`.

Organize work as:

```text
User outcome
  → activity
    → user task
      → user story or job story
        → priority and release slice
          → acceptance criteria
```

Create a canonical requirement register and global story map before assigning stories to pages. Include evidence, priority, release slice, and status without inventing business priority.

When the story backbone contains several activities, tasks, or release slices, precede the canonical table with a compact ASCII story/release overview.

Include unhappy paths, permission differences, bulk operations, long-running work, partial success, auditability, and recovery behavior where relevant. Avoid stories that restate screens or implementation tasks.

Place each story's full definition in its canonical page/subfeature or cross-page task chapter before the related operating steps and ASCII UI. Do not emit story IDs without story text, preconditions, outcome, and trace links.

For a new or materially revised requirement, apply `references/confirmation-gate.md`, deliver the first-pass alignment brief, and stop until the user explicitly chooses either guided modification or the named next phase. Skip or narrow the gate only under the reference's stated exceptions.

### Phase 7: Model information architecture and task flows

Apply `references/information-architecture-and-task-flows.md`.

For multi-page, multi-role, or multi-state work:

1. Consolidate one canonical `UXH` register and validation plan.
2. Derive user-recognizable `FUNC` capabilities from each confirmed `US/JS`; allow many-to-many mappings and do not equate a function with a page or component.
3. Choose each function's starting surface from overview, resource list/collection, work queue, detail-first, direct task, or configuration patterns according to the user's dominant job.
4. Draw an ASCII experience topology showing entry, starting surface, detail/action destinations, cross-page jumps, carried context, return, denied, and not-found paths.
5. Draw an ASCII task/decision flow for every primary scenario and use swimlanes or sequences for material handoffs, waits, notifications, re-entry, and recovery.
6. Validate that functions, pages, and interactions support the confirmed stories without mirroring internal services or turning stories into screen requirements.
7. Map each `SCN/REQ` through `TASK/FLOW`, `US/JS`, `FUNC`, `IA/NAV/PAGE/SUB`, `INT/UI/STATE`, and `SYS/SPEC/AC`.

For a narrow single-screen request, record the entry, return, and one complete task flow without inventing a larger navigation system.

After validating the IA, create the page/feature/subfeature map. Keep each subfeature tied to a distinct user purpose, page region, action set, or state responsibility.

### Phase 8: Model interactions

Apply `references/interaction-logic-principles.md` to derive the interaction, `references/ascii-interactions.md` to express it, and `references/progressive-ascii-confirmation.md` to confirm and persist it in dependency order.

Use ASCII as the default explanatory view for flows, state changes, and interfaces. Create the smallest non-duplicative set needed to explain:

- information hierarchy;
- primary and secondary actions;
- object and status language;
- permission-dependent behavior;
- validation and confirmation;
- loading, empty, success, error, partial-success, disabled, and recovery states;
- navigation and state transitions.

Pair each primary task with a local ASCII flow. Add a separate ASCII decision tree, swimlane, async sequence, or state lifecycle whenever the branches cannot be understood from the main flow. Split a diagram when it becomes too wide or dense; use a table alone only for a rule matrix or when ASCII would reduce comprehension.

For every described user action, input, selection, validation, feedback, permission response, async update, error, or recovery, show the affected control, message, or state in an ASCII UI frame and reference its `UI`/`STATE` ID. Several `INT` behaviors may share one frame only when their visible context and result remain understandable; draw another frame when the visible state changes materially. Label a wholly non-visual automatic step as system-only, and still draw any user-visible progress, notification, or result it produces.

Annotate each interaction with IDs and link it to stories and specifications. Assign an element ID to every field, action, message, status, table, and navigation element that has a requirement. Do not imply visual polish or final layout fidelity.

For each relevant frame, record the assumed viewport/context, keyboard and focus behavior, screen-reader name or announcement needs, non-color status cues, text expansion/overflow behavior, and narrow-screen or dense-table adaptation. Put these constraints beside the frame or in a referenced cross-cutting table.

For a large page or broad feature:

1. Create an ASCII confirmation queue ordered from topology and page overview through dependent function/section slices and recovery paths.
2. Present exactly one candidate unit, with its dependencies, assumptions, modification guidance, target location, and named next unit.
3. Keep candidate ASCII out of canonical requirement sections until the user explicitly confirms it.
4. On confirmation, write its ASCII, adjacent specifications, accessibility/adaptation constraints, acceptance criteria, trace links, and `DEC-ASCII` record as one coherent update.
5. Generate the next unit from the confirmed baseline and relevant confirmed ASCII decisions; reconfirm affected units when an upstream decision changes.

### Phase 9: Specify behavior in tables

Apply `references/spec-and-traceability.md`.

Generate only relevant tables:

- screen-local interface requirements placed immediately after each ASCII UI;
- screen-local interaction and validation requirements whose `INT` rows reference the ASCII `UI`/`STATE` frame that displays the behavior;
- functional specification;
- state-transition table;
- permission matrix;
- validation and error table;
- data and audit table;
- interaction-to-system contract;
- non-functional requirement table;
- traceability matrix.

Write atomic, testable rules. Replace vague terms such as “supports,” “fast,” “normally,” “appropriate,” or “user-friendly” with observable behavior or an explicit open question.

Use an interaction-to-system contract only where implementation boundaries affect user-visible behavior. Map the UI action to the required system capability, authorization, validation, sync/async behavior, data/state changes, idempotency or concurrency behavior, outcome variants, audit/observability, and test surface. Do not turn it into a speculative technical architecture.

### Phase 10: Compose the integrated guide

Apply `references/integrated-guide.md`.

Apply `references/human-readable-requirements.md` and compose the reader-first guide before the detailed control appendix.

Organize the main document by user task rather than by artifact type. For every task:

1. Explain the user goal, applicable role, prerequisites, and expected result.
2. Define the canonical user story or job story.
3. Show the task, decision, handoff, or state sequence as a compact ASCII flow.
4. Describe the shortest complete operating procedure.
5. Show the relevant ASCII UI state.
6. Place the interface requirement table directly after that frame.
7. Place interaction, validation, state, permission, and failure rules directly after the interface table.
8. Add the interaction-to-system contract and accessibility/adaptation constraints when applicable.
9. Attach acceptance criteria and trace IDs.

Keep shared permissions, global state definitions, data rules, audit behavior, non-functional requirements, and the full traceability matrix in appendices to avoid repetition.

Do not collect all ASCII frames in one chapter and all specifications in another unless the user explicitly requests separate documents.

When a large page contains several user tasks, use a page-led chapter:

```text
Page or core feature
  → page overview and page-level ASCII
  → page-level requirements
  → subfeature
    → purpose and canonical story
    → task flow and interaction
    → focused ASCII UI
    → colocated interaction/system specifications, accessibility constraints, and acceptance criteria
```

Use task-led chapters for workflows that cross several pages. Link each task step back to its `PAGE`, `FUNC`, `SUB`, and `UI` IDs.

### Phase 11: Deliver Markdown artifacts

Before the final audit, apply `references/markdown-delivery.md` and deliver the artifact:

1. Choose single-file or multi-file mode from scope and complexity.
2. Use a task plan for multi-file delivery when a planning tool is available; otherwise record the same steps and statuses in `index.md`.
3. Create `index.md` first for multi-file delivery.
4. Ensure the alignment brief and `DEC-BASELINE` confirmation record exist before detailed files; when repository evidence is available, create `00-repository-context.md` from `assets/repository-context-template.md`.
5. When external research was performed, create the landscape artifact before requirement foundation files.
6. Generate foundation files, then confirm and write one dependent ASCII unit at a time before cross-cutting and traceability completion.
7. Update the plan, confirmation queue, and `index.md` after every confirmed unit.
8. Keep each page's canonical stories, ASCII UI, subfeature explanations, local interaction/system requirements, accessibility/adaptation constraints, and acceptance criteria together in the same file.
9. Run `scripts/validate_requirement_docs.py <output-path> --final --profile full` for a completed full-shaping document when Python is available; omit the full profile for narrower modes.
10. Validate relative links, filenames, IDs, document status, and canonical rule ownership manually for anything the script cannot establish.

Use a dedicated output folder for a multi-file deliverable. Follow the current environment's artifact/output convention or a user-specified location.

### Phase 12: Review, repair, revalidate, and hand off

Apply `references/review-and-handoff.md`.

1. Run the deterministic validator, evidence/baseline audit, requirement/trace audit, UX/interaction review, and human-readable document review.
2. Repair findings at their canonical source, update affected dependents, and rerun every affected check.
3. Use `Complete` only when all required artifacts and reviews pass with no blocking issue; otherwise use `Complete with known limitations`, `Provisional`, or `Blocked`.
4. Persist a `Review and delivery summary` in `index.md` for multi-file output or near the end of a single-file document.
5. Give the user a self-contained handoff with the actual file/document tree, artifact links and purposes, content coverage, review results, repairs, remaining risks, omissions, reading order, and next action.

Do not claim completion from validator success alone. Report gaps instead of manufacturing missing coverage.

## Output contract

For a first pass, output the alignment brief through candidate stories and pause for explicit confirmation. After confirmation, preserve that baseline and use this full-shaping order:

1. Document purpose, document audience, repository snapshot, scope, status, and readiness
2. Repository evidence, current implementation, documented intent, code/documentation drift, and requested delta
3. External product/category landscape, comparable patterns, sources, and applicability when researched
4. Requirement background, current state, evidence, impact, and why now
5. Business objectives, user objectives, non-goals, and success measures
6. Primary target users, secondary users, affected parties, and role characteristics
7. Target scenarios and current workarounds
8. Concept model and user-facing terminology
9. Requirement register, global story map, priority, and release slicing
10. Story-derived functional points, starting-surface/page topology, interaction logic and rationale, UX hypotheses, and sequentially confirmed ASCII navigation, task/decision, cross-role, asynchronous, and state flows with supporting rule tables
11. Page, feature, subfeature, and task map
12. Repeated page or core-feature chapters containing:
   - page/feature purpose, scope, and applicable roles;
   - page-level ASCII overview and region legend;
   - page-level navigation, shared state, and requirement specifications;
   - repeated subfeature sections containing purpose, canonical user/job stories, operating steps, focused ASCII UI, colocated interaction and system specifications, accessibility/adaptation constraints, exceptions, and acceptance criteria.
13. Cross-page task chapters with end-to-end ASCII flows when a workflow spans several pages
14. Cross-cutting specifications
15. Glossary
16. Traceability, evidence, assumptions, conflicts, and research needs
17. Review and delivery summary with the actual file/document structure, artifact map, coverage, review results, remaining risks, reading order, and next action

If clarification is still required, output only sections 1–7 and the next question batch. Do not bury the questions after a speculative full solution.

For a small, ready scope, write the reader-first contract using `assets/ux-requirement-guide-template.md`. Add only the detailed appendix sections that are needed for implementation or review.

For a large scope, write a linked Markdown set using `assets/multi-file-index-template.md` as the entry point. Split by page/core feature and cross-page concern, not by artifact type. Do not put all ASCII UI in one file and all specifications in another.

## Quality bar

Reject or revise an output when:

- a repository is available but the analysis relies only on the user's prose;
- current public product, standard, or industry claims rely on model memory when internet research is available and material;
- competitor marketing or search snippets are presented as verified product behavior;
- a comparable feature is converted directly into a requirement without project-specific relevance, fit, and decision ownership;
- clarification asks for facts that a bounded repository search could answer;
- proposed behavior is presented without separating current implementation from documented intent and the requested delta;
- internal code names are treated as user language without checking existing UI copy and product documentation;
- it starts with features or pages without first explaining the background, problem, objectives, target people, and target scenarios;
- the main body reads like a traceability export, schema, or issue tracker rather than a UX requirement guide;
- wide tables, source paths, and stable IDs dominate the reading hierarchy instead of supporting it;
- background claims, user attributes, or scenarios are presented as verified without evidence labels;
- product target users are confused with the audience reading the requirement document;
- objectives are feature descriptions rather than observable business or user outcomes;
- engineering terminology has only been translated literally;
- a product term is friendlier but changes the technical meaning;
- user mental-model claims have no evidence label;
- a material UX hypothesis has neither supporting evidence nor a validation task;
- the story map or functional decomposition starts with pages/components instead of confirmed outcomes, activities, user tasks, and stories;
- a requirement or story has no explicit priority/release status and no owner for that decision;
- detailed IA, specifications, or ASCII UI were produced from a new or materially changed requirement before its analysis/story baseline was explicitly confirmed;
- a primary scenario has no information-architecture entry, task/decision flow, completion, or recovery;
- a primary flow is expressed only as prose or a table when a readable ASCII overview could show its sequence, branching, handoff, or lifecycle;
- a user-visible interaction behavior appears only in prose, a table, or a flow without a corresponding ASCII UI/state frame;
- a narrow interaction delivery omits ASCII UI without a coverage notice, impact statement, and supplement or blocking explanation;
- a story ID appears without a canonical story definition;
- a happy-path-only ASCII screen hides important states;
- an ASCII frame is treated as proof of responsive, accessible, or visual-design quality without explicit constraints;
- a large page is shown as one dense frame without subfeature decomposition;
- a subfeature or interaction lacks its own explanation, focused ASCII, or local specifications when the overview is insufficient;
- a large scope is forced into one unwieldy Markdown file;
- a multi-file deliverable lacks `index.md`, progress status, relative navigation, or a canonical home for each requirement;
- cross-file links are broken or stable IDs conflict;
- a story describes a component instead of a user outcome;
- a specification cannot be observed or tested;
- user-visible service, async, concurrency, persistence, audit, or recovery behavior lacks an interaction-to-system contract when one is needed;
- permissions, inheritance, precedence, lifecycle, or failure behavior remain ambiguous;
- the traceability matrix exposes orphaned stories, screens, specs, or criteria.
- a confirmation pause does not explain how to modify the current material or what the named next phase will produce;
- dependent ASCII units were generated or written ahead of confirmation, or a canonical UI lacks a confirmed `DEC-ASCII` record;
- review findings were not repaired and revalidated, or the user handoff omits the actual file/document structure, contents, coverage, review results, limitations, and reading order.
