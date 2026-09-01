# Adaptive delivery profiles

Use this reference before creating requirement files. It keeps the delivery reader-first and compact while preserving the same requirement, ASCII UX, specification, acceptance, evidence, and traceability coverage.

## Contents

- Start compact and promote only when needed
- Choose a delivery profile
- Grow one canonical document through both stages
- Decide when to split
- Apply the default structures
- Consolidate content ownership
- Combine with progressive ASCII confirmation
- Plan and report the delivery
- Review file-count quality

## Start compact and promote only when needed

Begin with one canonical `ux-requirements.md`. Do not pre-create a file merely because the output contract contains a content type such as users, terminology, IA, evidence, traceability, or decisions.

Use headings and appendices inside the main document first. Promote to more files only when an independent reader, owner, review cycle, release boundary, or substantial readability problem justifies the split.

File count is not a quality signal. Coverage, findability, canonical ownership, and reader comprehension are the quality signals.

## Choose a delivery profile

Use one explicit profile:

| Profile | Typical file count | Default use |
|---|---:|---|
| Compact | 1 | Default; one product area and a coherent review path |
| Balanced | 2–3 | Dense evidence or control material would disrupt the main UX reading path |
| Modular | 4+ | Independent modules, teams, releases, owners, or review/acceptance cycles require separate files |

Select `Compact` unless a split condition is already present. Reassess after baseline confirmation and while the document grows. Promotion is allowed; automatic demotion is not required during active work when it would create churn.

Record:

```markdown
| Delivery profile | Compact / Balanced / Modular |
| Primary document | ux-requirements.md |
| Split rationale | None, or the specific reader/ownership/release reason |
```

Do not choose `Modular` only because the requirement is technically complex, contains many IDs, or needs a complete traceability audit.

## Grow one canonical document through both stages

Stage 1 and Stage 2 use the same main file.

During Stage 1, `ux-requirements.md` contains:

```text
ux-requirements.md
├── Document status and delivery profile
├── Repository/current-state summary
├── Background, objectives, users, and scenarios
├── Mental model, terminology, scope, and risks
├── Candidate requirements and User Stories
└── Baseline confirmation
```

Set detailed sections to `Planned` or omit them until the baseline is confirmed. Do not create a separate `requirement-alignment.md` unless the user needs the baseline to be reviewed, approved, or retained as an independent governed artifact.

After confirmation, update the same file:

```text
ux-requirements.md
├── Confirmed baseline and change record
├── Experience overview, target-user model-fit review, and ASCII confirmation queue
├── Page, function, section, and task chapters
│   └── confirmed ASCII + local specifications + acceptance criteria
├── Cross-function rules and necessary appendices
├── Traceability, evidence, decisions, and risks
└── Review and delivery summary
```

Do not restate the confirmed background, users, terminology, stories, or scope in a second guide. Update the canonical section and link to it.

## Decide when to split

Split only when at least one material condition exists:

- a page/module has an independent owner, team, review, release, implementation, or acceptance cycle;
- several readers need different stable entry points and a single table of contents is insufficient;
- a page/task chapter is independently reusable and can be understood with limited parent context;
- repository or public research evidence is substantial enough to obscure the PM/UX reading path;
- cross-cutting permission, lifecycle, data, audit, system-contract, or NFR controls are dense and shared by several chapters;
- the main document cannot remain skimmable after removing duplication and moving dense material into appendices;
- the user explicitly requests separate files.

Before splitting, try:

1. shortening repeated prose;
2. replacing duplicated rules with links or IDs;
3. using an appendix in the same document;
4. grouping tables by reader task;
5. using a table of contents and clear page/task headings.

Do not split solely because:

- a content category exists;
- a template offers a filename;
- a validator checks an artifact class;
- the document contains many stories or IDs;
- a plan has one step per analysis activity.

## Apply the default structures

### Compact

```text
ux-requirements.md
```

Keep evidence summaries, shared rules, decisions, and traceability as concise appendices. Put detailed evidence beside the claim only when readers need it there.

### Balanced

```text
requirement-delivery/
├── ux-requirements.md
├── control-appendix.md
└── evidence-and-research.md   # optional; create only when substantial
```

Use:

- `ux-requirements.md` for the reader-first requirement, confirmed Stories, experience, confirmed ASCII UX, local specifications, acceptance criteria, key decisions, and final review summary;
- `control-appendix.md` for dense shared permissions, lifecycle, data, audit, system contracts, NFR, full traceability, and detailed decision/control tables;
- `evidence-and-research.md` only for substantial repository evidence, drift analysis, public research, comparable products, and source ledgers.

The primary document acts as the entry point. Do not create `index.md` for two or three files.

### Modular

```text
requirement-delivery/
├── index.md
├── ux-requirements.md
├── modules/
│   ├── <independently-owned-module>.md
│   └── <independently-owned-module>.md
├── control-appendix.md        # only when shared controls are substantial
└── evidence-and-research.md   # only when substantial
```

Use `index.md` when four or more Markdown files are delivered. List only real or immediately planned files. Do not populate the index with one file per artifact type.

## Consolidate content ownership

Use this default mapping:

| Content | Compact/Balanced canonical location |
|---|---|
| Alignment brief, baseline confirmation, and change history | Main document |
| Background, goals, scope, users, scenarios, concepts, terminology, requirements, and Story map | Main document |
| Functional decomposition, starting surfaces, IA, navigation, task flows, and page map | Main document experience overview |
| Page/function/section stories, confirmed ASCII, local interaction/system rules, accessibility, and acceptance | Corresponding main-document chapter |
| Cross-page task | Relevant task chapter; split only when independently owned |
| Shared permissions, lifecycle, data, audit, contracts, and NFR | Main appendix or `control-appendix.md` when dense |
| Full traceability and detailed decisions/questions | Main appendix or `control-appendix.md` |
| Repository evidence and public research | Concise main summary; `evidence-and-research.md` only when substantial |
| Review and delivery summary | Main document |

Keep one canonical definition. Do not maintain a detailed page chapter and a second detailed UX-guide copy of the same ASCII or rule.

## Combine with progressive ASCII confirmation

For Compact and Balanced delivery, keep the ASCII UX confirmation queue in `ux-requirements.md`.

After each confirmation:

```text
[Confirmed ASCII unit]
        |
        +--> update its main-document page/function section
        +--> update adjacent specifications and acceptance criteria
        +--> update local trace and DEC-ASCII record
        +--> update the confirmation queue
        +--> generate the next dependent candidate
```

Do not update a separate IA file, page map file, UX-guide copy, page file, and trace file after every confirmation. Keep local trace beside the confirmed slice, then compose or refresh the full traceability appendix during final review.

In Modular delivery, write a confirmed unit to its independently owned module file and update `index.md` only for status/navigation changes.

## Plan and report the delivery

Keep the execution plan about work, not file count. Several analysis steps may update one canonical document.

Before Stage 1, report the expected profile and primary file. After baseline confirmation, reassess and state whether the profile remains appropriate. When promoting:

1. name the split condition;
2. show the proposed file tree;
3. identify content moving from the main document;
4. preserve stable IDs and links;
5. avoid duplicating canonical content;
6. tell the user what to read first.

At final handoff, show the actual tree, each file's purpose, and the split rationale. A one-file delivery still shows its internal document structure.

## Review file-count quality

Reject or revise the delivery when:

- Stage 1 and Stage 2 duplicate the same baseline in separate documents without a governance need;
- background, users, terminology, Stories, IA, page map, traceability, and decisions were split only because they are different artifact types;
- `index.md` exists for a two- or three-file package without a user or environment requirement;
- empty, placeholder-only, or speculative files were created;
- the primary guide repeats detailed ASCII or specifications owned by another file;
- a reader must open several files to understand one page, function, or task;
- a split has no stated reader, owner, release, review, or readability rationale;
- the recorded delivery profile does not match the actual file count;
- consolidation hides material evidence, assumptions, system constraints, or traceability instead of relocating them.

Compact delivery is not narrow delivery. It must still provide every applicable requirement artifact class inside the chosen document structure.
