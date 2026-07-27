# Markdown delivery

Use this reference to deliver the final requirement artifact as one or more Markdown files.

## Contents

- Required format
- Use two-stage delivery
- Choose the delivery mode
- Report narrow-delivery coverage
- Plan a large delivery
- Multi-file structure
- File ownership
- Markdown conventions
- Progress and partial delivery
- Final validation

## Required format

Deliver completed documents as GitHub-Flavored Markdown (`.md`) unless the user explicitly requests another file format. Use:

- Markdown headings for hierarchy;
- fenced `text` blocks for ASCII UI;
- fenced `text` blocks for hierarchy, task, decision, role-handoff, asynchronous, lifecycle, and trace flows;
- Markdown tables for requirements;
- relative links for navigation;
- stable IDs in visible text, not only in heading anchors.

Make the primary document a human-readable UX requirement guide. Put dense evidence, matrices, system contracts, and full traceability in appendices or supporting files. Use chat for clarification rounds and persist confirmed answers, decisions, and the final baseline into Markdown.

## Use two-stage delivery

For a new or materially revised requirement, Stage 1 produces `requirement-alignment.md` (or `00c-requirement-alignment.md` in a multi-file set) from `assets/requirement-alignment-template.md`. Stop after presenting the evidence-backed analysis, scope, terminology, and complete candidate stories. Keep downstream IA, ASCII UI, detailed specifications, and acceptance artifacts Planned or Blocked by confirmation.

After explicit confirmation, change the baseline status to `Confirmed`, record `DEC-BASELINE-###`, and begin Stage 2. Generate detailed artifacts only from that version. Record later changes in the alignment brief and reconfirm affected stories before updating dependent files.

## Choose the delivery mode

Use a single Markdown file when the requirement has a small, coherent scope that readers can navigate comfortably.

For a small scope, use `assets/ux-requirement-guide-template.md` and add only necessary control appendices. Do not default to the exhaustive enterprise template.

Use multiple Markdown files when any of these signals apply:

- the user requests multiple files;
- several pages, modules, or core features need independent chapters;
- several subfeatures require focused ASCII UI and local specifications;
- workflows cross multiple pages;
- roles have materially different permissions or procedures;
- cross-cutting data, audit, integration, lifecycle, or non-functional rules are substantial;
- producing one file would obscure ownership, progress, or review boundaries.

Do not use file count or word count as the sole decision.

## Report narrow-delivery coverage

A narrow request limits output size, not transparency. Before handoff, show:

| Artifact | Included/Provisional/Omitted/Blocked/N/A | Why | Impact | Next action |
|---|---|---|---|---|

Do this for the requested artifact and the adjacent outputs required to use it safely. For interaction-related work, explicitly cover task flow, ASCII UI, critical states, local specifications, accessibility/adaptation, and acceptance criteria.

When an existing document contains enough interaction evidence but lacks ASCII UI, create a targeted supplement with `assets/ascii-ui-supplement-template.md`. Keep it bounded to the relevant page, subfeature, or task. When evidence is partial, label provisional frames and assumptions. When a missing role, task, permission, state, data, or recovery decision would materially change the interface, mark ASCII UI `Blocked`, explain the impact, and ask focused questions before finalizing it.

If the user explicitly requests only a non-UI artifact, do not expand scope without permission. State that ASCII UI was omitted and whether a later supplement is needed for design, implementation, testing, or acceptance.

## Plan a large delivery

When a planning tool is available, create and maintain a plan with exactly one active step. Use this dependency order:

1. Inspect the repository and establish the current-state evidence baseline when a repository is available.
2. Research the current public product/category and industry landscape when requested or materially relevant.
3. Assess readiness and resolve blockers.
4. Choose the document map and create `index.md` before producing content files.
5. Establish background, objectives, target users, target scenarios, scope, and stable IDs.
6. Establish concepts and product language.
7. Establish the requirement register, outcome/task-led story map, priority, and release slicing.
8. Produce the alignment brief, request explicit confirmation, and pause dependent work.
9. Record the confirmed baseline version and `DEC-BASELINE`.
10. Derive user-recognizable `FUNC` capabilities from confirmed stories, choose the appropriate starting-surface model, and map detail/action destinations and return behavior.
11. Establish interaction logic and material pattern rationale, then the canonical UX hypotheses and ASCII information architecture, navigation, task/decision, role-handoff, asynchronous, and lifecycle flows with supporting rule tables.
12. Produce the page/core-feature map.
13. Produce one page/core-feature file at a time, including canonical story details, subfeatures, ASCII UI, local interaction/system specifications, accessibility/adaptation constraints, and acceptance criteria.
14. Produce cross-page workflows and cross-cutting requirements.
15. Produce traceability, decisions, assumptions, and open questions.
16. Compose or update the human-readable UX requirement guide from the canonical material.
17. Run the deterministic validator plus evidence, semantic coverage, UX/interaction, and readability reviews; repair findings and rerun affected checks.
18. Persist the review and delivery summary, then give the user the actual file/document tree, artifact map, content coverage, review results, limitations, reading order, and next action.

If no planning tool is available, put the same steps and statuses into `index.md`.

Do not mark a step complete until its file exists, contains no unintended placeholders, and passes its local coverage check.

## Multi-file structure

Create only necessary files. Use this default shape:

```text
<feature-slug>/
├── index.md
├── ux-requirement-guide.md
├── 00-repository-context.md
├── 00b-industry-and-product-landscape.md
├── 00c-requirement-alignment.md
├── 01-background-goals-and-scope.md
├── 02-target-users-and-scenarios.md
├── 03-concepts-and-language.md
├── 04-story-map-and-release-scope.md
├── 05-information-architecture-and-task-flows.md
├── 06-page-and-feature-map.md
├── 10-page-<page-slug>.md
├── 11-page-<page-slug>.md
├── 50-cross-page-workflows.md
├── 80-cross-cutting-requirements.md
├── 90-traceability.md
└── 91-decisions-and-open-questions.md
```

Omit empty categories. Add more page files with stable numeric prefixes. Use lowercase hyphen-case filenames.

## File ownership

Keep each rule in one canonical file:

| Content | Canonical location |
|---|---|
| Human-readable context, users, scenarios, journeys, ASCII UI, key decisions, and links to detail | `ux-requirement-guide.md` |
| Repository snapshot, instructions, evidence, current behavior, documented intent, drift, and requested delta | `00-repository-context.md` |
| Public source ledger, product/category taxonomy, comparable solutions, observed patterns, and applicability | `00b-industry-and-product-landscape.md` |
| First-pass analysis, candidate stories, confirmation record, and change history | `requirement-alignment.md` or `00c-requirement-alignment.md` |
| Background, problem, objectives, success, non-goals, overall product scope, readiness | `01-background-goals-and-scope.md` |
| Primary/secondary users, affected parties, document audiences, scenarios | `02-target-users-and-scenarios.md` |
| Concepts, terminology, and concept-specific evidence | `03-concepts-and-language.md` |
| Requirement register, global story map, priority, and release slicing | `04-story-map-and-release-scope.md` |
| Story-derived functional points, starting-surface/page topology, interaction logic and rationale, canonical UX hypotheses, and ASCII IA, navigation, primary task/decision, role-handoff, asynchronous, and lifecycle flows | `05-information-architecture-and-task-flows.md` |
| Page/feature/subfeature inventory | `06-page-and-feature-map.md` |
| Page stories, ASCII, subfeatures, local interaction/system specs, accessibility/adaptation constraints, and AC | Corresponding `10+page-*.md` |
| Cross-page stories, operating tasks, and end-to-end ASCII flows | `50-cross-page-workflows.md` |
| Shared permissions, lifecycle, data, audit, system contracts, accessibility/adaptation, and NFR | `80-cross-cutting-requirements.md` |
| Coverage and ID traceability | `90-traceability.md` |
| Decisions, assumptions, conflicts, research | `91-decisions-and-open-questions.md` |

Reference canonical rules by ID and relative link. Do not copy the same specification into several files.

## Markdown conventions

1. Start each file with title, purpose, audience, status, and parent link to `index.md`.
2. Use numbered headings only when they help readers navigate; do not renumber stable IDs.
3. Keep tables narrow enough to read. Split unrelated rule types into separate tables.
4. Keep ASCII UI and its local requirement tables in the same file and adjacent sections.
5. Add previous/next links when more than three page files exist.
6. Use relative file links. Avoid absolute local paths inside the document set.
7. Update links and index entries when renaming a file.
8. Start each main-guide section with a short plain-language summary.
9. Keep main-guide tables to roughly two to five columns; move wide matrices to supporting files.
10. In every table, put descriptive/name/outcome/behavior/status columns first and stable or related ID columns last. Use trace lines when identifiers would otherwise dominate the reading path.

## Progress and partial delivery

Create `index.md` before content files. Track each file as Planned, In progress, Blocked, Draft, or Complete.

Before baseline confirmation:

- create or update only the evidence, readiness, index, clarification, and alignment material;
- mark dependent files as Blocked or Planned;
- do not fill detailed IA, ASCII UI, specifications, or acceptance files with speculative content.

For long-running delivery, update both the execution plan and the index after each file.

## Final validation

Check:

- every file listed in `index.md` exists;
- every file links back to `index.md`;
- all relative links resolve;
- filenames follow the naming convention;
- the first content link is a human-readable UX requirement guide rather than an evidence ledger or control table;
- IDs are unique and stable across files;
- repository-backed work includes the analyzed snapshot, source inventory, current behavior, documented intent, drift, and requested delta;
- internet-researched work includes direct source links, access dates, source class, product/version/region context, limitations, and project applicability;
- background, objectives, target users, and target scenarios have canonical files and evidence labels;
- the alignment brief records a confirmed baseline version, `DEC-BASELINE`, confirmed story/scope coverage, and later change deltas;
- every confirmed story maps to one or more user-recognizable functional points;
- every functional point maps to a justified starting surface plus its detail/action continuation and return behavior;
- each page/subfeature has a canonical file;
- ASCII UI remains adjacent to local specifications;
- every user-visible interaction behavior references an ASCII UI/state frame that actually shows its control, feedback, or result;
- every primary and cross-page flow has a readable ASCII overview before its detailed rule table;
- every narrow delivery reports expected, omitted, provisional, blocked, and not-applicable artifacts;
- the main guide passes the five-minute, skim, jargon, table-width, ID-hierarchy, and action-findability checks;
- no canonical rule is duplicated with conflicting wording;
- traceability covers all completed pages and requirements;
- no unintended placeholders or stale status labels remain.
- review findings were repaired at their canonical source and affected checks were rerun;
- `index.md` or the single-file document contains a populated `Review and delivery summary`;
- the final user handoff shows only the actual delivered files/document sections and accurately reports their locations, purposes, contents, coverage, review results, limitations, omissions, reading order, and next action.

For completed artifacts, run:

```text
python3 <skill-directory>/scripts/validate_requirement_docs.py <output-path> --final --profile full
```

The structural profile checks file/link integrity, table structure, localized ID headers, placeholders, baseline-status fields, final delivery statuses, index backlinks, and unknown ID prefixes. The full profile also requires a canonical `DEC-BASELINE` record linked to confirmed requirement/story coverage, a persisted review/handoff section, and the actual delivered file/document structure; it detects duplicate canonical IDs, dangling references, untraced `CHG` records, missing required artifact classes, missing ASCII flow coverage when `FLOW` IDs exist, interaction behaviors without linked ASCII UI/state, stories without functional points or upstream/downstream trace, functional points without stories or user-facing surfaces, UI states without stories or behavioral rules, and orphaned acceptance criteria. It still cannot prove that a person actually approved the baseline, that review findings were genuinely repaired, that the displayed tree matches the filesystem, that a referenced frame visibly depicts the claimed behavior, that every diagram is comprehensible, or that the product logic, priority, terminology, usability, accessibility, or UX hypothesis is correct; complete those judgments manually and report them honestly in the handoff.
