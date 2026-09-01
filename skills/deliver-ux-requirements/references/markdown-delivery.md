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

Apply `adaptive-delivery-profiles.md`. Start with one human-readable `ux-requirements.md`; put dense evidence, matrices, system contracts, and full traceability in appendices inside that file before considering supporting files. Use chat for clarification and ASCII review, then persist confirmed answers, decisions, and ASCII slices into the same canonical document.

## Use two-stage delivery

For a new or materially revised requirement, Stage 1 creates or updates `ux-requirements.md` using the alignment artifact produced by `$shape-requirement-baseline`. Stop after presenting the evidence-backed analysis, scope, terminology, and complete candidate stories. Keep downstream IA, ASCII UI, detailed specifications, and acceptance sections Planned or omitted until confirmation.

After explicit confirmation, change the baseline status to `Confirmed`, record `DEC-BASELINE-###`, and extend the same main file through Stage 2. Record later changes in its baseline/change section and reconfirm affected stories before updating dependent content. Create a separate alignment file only when governance requires an independently retained approval artifact.

## Choose the delivery mode

Use the three profiles from `adaptive-delivery-profiles.md`:

- `Compact` — default, one `ux-requirements.md`;
- `Balanced` — two or three files when dense control or evidence material disrupts the main reading path;
- `Modular` — four or more files only for independent ownership, review, release, implementation, or acceptance boundaries.

Start Compact and promote only when a stated split condition appears. Complexity, many IDs, cross-page flow, or a validator artifact class does not by itself justify another file. Record the profile, primary document, and split rationale in the main document.

## Report narrow-delivery coverage

A narrow request limits output size, not transparency. Before handoff, show:

| Artifact | Included/Provisional/Omitted/Blocked/N/A | Why | Impact | Next action |
|---|---|---|---|---|

Do this for the requested artifact and the adjacent outputs required to use it safely. For interaction-related work, explicitly cover task flow, ASCII UI, critical states, local specifications, accessibility/adaptation, and acceptance criteria.

When an existing document contains enough interaction evidence but lacks ASCII UI, invoke `$shape-ascii-interactions` to create a targeted supplement from its `assets/ascii-ui-supplement-template.md`. Keep it bounded to the relevant page, subfeature, or task. When evidence is partial, label provisional frames and assumptions. When a missing role, task, permission, state, data, or recovery decision would materially change the interface, mark ASCII UI `Blocked`, explain the impact, and ask focused questions before finalizing it.

If the user explicitly requests only a non-UI artifact, do not expand scope without permission. State that ASCII UI was omitted and whether a later supplement is needed for design, implementation, testing, or acceptance.

## Plan the delivery

When a planning tool is available, create and maintain a plan with exactly one active step. Use this dependency order:

1. Inspect the repository and establish the current-state evidence baseline when a repository is available.
2. Research the current public product/category and industry landscape when requested or materially relevant.
3. Assess readiness and resolve blockers.
4. Select Compact, create `ux-requirements.md`, and record its profile; do not pre-create supporting files.
5. Write background, objectives, users, scenarios, terminology, scope, requirements, and candidate stories into the main document.
6. Request baseline confirmation, then record `DEC-BASELINE` in the same file.
7. Reassess the profile; promote only when a split condition exists and show the proposed tree/rationale.
8. Derive functions, topology, interaction logic, and the ASCII confirmation queue in the main document.
9. Confirm and write one ASCII slice at a time with its local specifications, acceptance criteria, and trace.
10. Add cross-function rules, evidence, decisions, and full trace as main-document appendices or justified Balanced support files.
11. Run deterministic, evidence, semantic, UX, interaction, and readability review; repair and revalidate.
12. Persist the review summary and actual document/file structure, then hand off with reading order and limitations.

If no planning tool is available, track work status in the main document. Use `index.md` only for Modular delivery.

Do not mark a step complete until its file exists, contains no unintended placeholders, passes its local coverage check, and every canonical ASCII UI in scope has a confirmed `DEC-ASCII` record.

## Default structures

Compact:

```text
ux-requirements.md
```

Balanced:

```text
requirement-delivery/
├── ux-requirements.md
├── control-appendix.md
└── evidence-and-research.md   # optional
```

Modular:

```text
requirement-delivery/
├── index.md
├── ux-requirements.md
├── modules/
│   ├── <independently-owned-module>.md
│   └── <independently-owned-module>.md
├── control-appendix.md        # optional
└── evidence-and-research.md   # optional
```

Create `index.md` only for four or more Markdown files. Create no empty categories or placeholder-only files. Use lowercase hyphen-case filenames.

## File ownership

Keep each rule in one canonical file:

| Content | Canonical location |
|---|---|
| Alignment, baseline, background, users, scenarios, terminology, requirements, Stories, experience overview, and page map | `ux-requirements.md` |
| Page/function/task stories, confirmed ASCII, local interaction/system specs, accessibility, and acceptance | Relevant main-document chapter; module file only when independently owned |
| Shared permissions, lifecycle, data, audit, system contracts, NFR, full trace, and detailed decisions | Main-document appendix or `control-appendix.md` when dense |
| Repository evidence, drift, public research, comparable solutions, and source ledger | Concise main summary or `evidence-and-research.md` when substantial |
| Review, actual structure, reading order, and limitations | `ux-requirements.md` |

Reference canonical rules by ID and relative link. Do not copy the same specification into several files.

## Markdown conventions

1. Start the primary document with title, purpose, audience, status, delivery profile, and split rationale; supporting files link to it or to `index.md` in Modular delivery.
2. Use numbered headings only when they help readers navigate; do not renumber stable IDs.
3. Keep tables narrow enough to read. Split unrelated rule types into separate tables.
4. Keep ASCII UI and its local requirement tables in the same file and adjacent sections.
5. Add previous/next links only for independently split module files.
6. Use relative file links. Avoid absolute local paths inside the document set.
7. Update links and index entries when renaming a file.
8. Start each main-guide section with a short plain-language summary.
9. Keep main-guide tables to roughly two to five columns; move wide matrices to an in-file appendix first, then to a supporting file only when independently reviewing it improves readability.
10. In every table, put descriptive/name/outcome/behavior/status columns first and stable or related ID columns last. Use trace lines when identifiers would otherwise dominate the reading path.

## Progress and partial delivery

Create or update `ux-requirements.md` first. Track sections or justified supporting files as Planned, In progress, Blocked, Draft, or Complete. Create `index.md` only after the delivery becomes Modular.

Before baseline confirmation:

- update only the main document's evidence summary, readiness, alignment, and candidate Story sections;
- mark dependent sections as Blocked or Planned, or omit them;
- do not create speculative IA, ASCII UI, specification, acceptance, or placeholder-only files.

After baseline confirmation, persist the ASCII UX confirmation queue in the main document. Keep candidate ASCII in the confirmation conversation, not in canonical requirement sections. Update the plan, queue, canonical page/task slice, adjacent specifications, acceptance criteria, and local trace after each confirmed unit; update `index.md` only in Modular delivery.

For long-running delivery, reconstruct the next unit from the persisted baseline, queue, confirmed `DEC-ASCII` records, and canonical files rather than conversation memory alone.

## Final validation

Check:

- the recorded Compact/Balanced/Modular profile matches the actual file count and has a split rationale when not Compact;
- four-or-more-file Modular delivery has `index.md`, every listed file exists, and supporting files link back to the primary document or index;
- all relative links resolve;
- filenames follow the naming convention;
- `ux-requirements.md` is the primary reading entry rather than an evidence ledger or control table;
- IDs are unique and stable across files;
- repository-backed work includes the analyzed snapshot, source inventory, current behavior, documented intent, drift, and requested delta;
- internet-researched work includes direct source links, access dates, source class, product/version/region context, limitations, and project applicability;
- background, objectives, target users, and target scenarios have canonical sections and evidence labels;
- the alignment brief records a confirmed baseline version, `DEC-BASELINE`, confirmed story/scope coverage, and later change deltas;
- every confirmed story maps to one or more user-recognizable functional points;
- every functional point maps to a justified starting surface plus its detail/action continuation and return behavior;
- each page/subfeature has one canonical chapter or justified independently owned module file;
- ASCII UI remains adjacent to local specifications;
- every user-visible interaction behavior references an ASCII UI/state frame that actually shows its control, feedback, or result;
- every canonical ASCII UI/state is covered by a confirmed `DEC-ASCII` record, and no required queue item remains in review or awaiting changes;
- every primary and cross-page flow has a readable ASCII overview before its detailed rule table;
- every narrow delivery reports expected, omitted, provisional, blocked, and not-applicable artifacts;
- the main guide passes the five-minute, skim, jargon, table-width, ID-hierarchy, and action-findability checks;
- no canonical rule is duplicated with conflicting wording;
- traceability covers all completed pages and requirements;
- no unintended placeholders or stale status labels remain.
- review findings were repaired at their canonical source and affected checks were rerun;
- the primary document contains a populated `Review and delivery summary`;
- the final user handoff shows only the actual delivered files/document sections and accurately reports their locations, purposes, contents, coverage, review results, limitations, omissions, reading order, and next action.

For completed artifacts, run:

```text
python3 <skill-directory>/scripts/validate_requirement_docs.py <output-path> --final --profile full
```

The structural profile checks file/link integrity, table structure, localized ID headers, placeholders, baseline-status fields, final delivery statuses, conditional index usage and backlinks, and unknown ID prefixes. The `model-fit` profile checks explicit target role/scenario scope, flow/representation review coverage, `UXGAP` trace and details, and open Critical gaps without requiring a completed baseline or redesign. The full profile also verifies that the declared Compact/Balanced/Modular profile matches the actual Markdown file count and that Balanced/Modular records a concrete split rationale; requires a canonical `DEC-BASELINE` record linked to confirmed requirement/story coverage, two-stage model-fit coverage, a populated final ASCII UX confirmation queue, confirmed `DEC-ASCII` coverage for every canonical UI, a persisted review/handoff section, and the actual delivered file/document structure; and detects unresolved ASCII confirmation units, duplicate canonical IDs, dangling references, untraced `CHG` records, missing required artifact classes, missing ASCII flow coverage when `FLOW` IDs exist, interaction behaviors without linked ASCII UI/state, stories without functional points or upstream/downstream trace, functional points without stories or user-facing surfaces, `UXGAP` findings without role/scenario/interaction trace, confirmed UI affected by an open Critical gap, UI states without stories or behavioral rules, and orphaned acceptance criteria. It still cannot judge whether a split rationale is genuinely necessary, prove that a person actually approved a candidate, that units were presented sequentially, that review findings were genuinely repaired, that the displayed tree matches the filesystem, that a referenced frame visibly depicts the claimed behavior, that every diagram is comprehensible, or that the product logic, priority, terminology, usability, accessibility, user-model fit, or UX hypothesis is correct; complete those judgments manually and report them honestly in the handoff.
