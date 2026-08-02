# Review, repair, and final handoff

Use this reference after all planned requirement artifacts exist. It defines the mandatory review loop, persisted review record, delivery status, and user-facing handoff for completed requirements.

## Contents

- Review in layers
- Run the repair loop
- Determine the delivery status
- Persist the review and delivery summary
- Show the delivered structure
- Tell the user what was delivered
- Required handoff checks

## Review in layers

Run each applicable layer. A deterministic validator does not replace product, UX, or domain judgment.

### 1. Structural and deterministic review

Run:

```text
python3 <skill-directory>/scripts/validate_requirement_docs.py <output-path> --final --profile full
```

Check file existence, links, filenames, statuses, placeholders, stable IDs, duplicate definitions, dangling references, baseline confirmation, required artifact classes, ASCII flow coverage, and trace-chain integrity.

### 2. Evidence and baseline review

Verify:

- repository-backed claims reflect the inspected snapshot;
- current implementation, documented intent, requested behavior, and delta remain distinct;
- external claims retain URL, access date, product/version/region context, limitations, and applicability;
- facts, decisions, inferences, assumptions, unknowns, and conflicts remain labeled;
- the confirmed baseline version and affected stories match the detailed design;
- later changes are recorded and materially affected slices were reconfirmed.

### 3. Requirement and trace review

Verify:

- background, objectives, users, scenarios, concepts, scope, and release boundary agree;
- every primary scenario maps to a story, user-recognizable function, entry, flow, interface, specification, and acceptance result;
- every story has a canonical definition, preconditions, outcome, priority/release status, and acceptance criteria;
- every function has a story source and a user-facing surface;
- every page, subfeature, interaction, UI state, specification, system contract, and acceptance criterion has an upstream reason;
- assumptions and open questions appear in affected downstream artifacts;
- no rule is duplicated with contradictory wording.

### 4. UX and interaction review

Verify:

- information architecture follows the user mental model rather than service boundaries;
- each task has a clear trigger, context, next action, completion, exit, and recovery;
- main, alternate, permission, failure, asynchronous, partial-success, stale, and recovery paths are covered when applicable;
- every user-visible interaction appears in an ASCII UI/state frame;
- every canonical ASCII UI/state was confirmed in dependency order, traces to a confirmed `DEC-ASCII` record, and was used as context for dependent units;
- no candidate or changes-requested ASCII was silently written as canonical content;
- every visible action, message, status, and consequence has a local behavior specification;
- dialog versus dedicated-page choices follow the interaction-logic rules and no drawer-like surface appears;
- destructive or irreversible actions show scope, consequence, reversibility, and safeguard;
- keyboard, focus, assistive-technology, non-color, text expansion, density, and narrow-layout constraints are defined where applicable.

### 5. Human-readable document review

Run the five-minute, skim, jargon, table-width, ID-hierarchy, action-findability, and information-layer checks.

Verify that:

- the main guide starts with the problem, people, scenario, and intended experience;
- headings, ASCII, and short summaries reveal the reading path;
- engineering terms are translated without changing meaning;
- tables lead with names, outcomes, and behavior while IDs remain trailing;
- dense evidence, system contracts, and exhaustive matrices do not dominate the UX/PM reading experience;
- the reader can find decisions, risks, assumptions, recovery, and next steps quickly.

## Run the repair loop

Use this sequence:

```text
[Generate all planned artifacts]
             |
             v
[Run deterministic checks]
             |
             v
[Run evidence, requirement, UX, and readability review]
             |
             +-- blocking finding --> [Repair affected canonical source]
             |                              |
             |                              v
             |                        [Update dependents]
             |                              |
             +------------------------------+
             |
             v
[Rerun all affected checks]
             |
             +-- unresolved --> [Repeat or mark blocked/provisional]
             |
             v
[Persist review record and hand off]
```

Repair the canonical source of a rule, then update dependent summaries, ASCII, specifications, acceptance criteria, links, index statuses, and trace records. Do not patch only the final summary while leaving the source inconsistency.

Rerun:

- the deterministic validator after any file, ID, link, status, or trace change;
- affected semantic and UX checks after any requirement, story, flow, interaction, state, permission, or recovery change;
- readability checks after restructuring the main guide;
- the complete review when a fix changes scope, users, object model, lifecycle, permission, or risk.

Do not mark the delivery complete merely because the validator exits successfully. Do not leave a known blocking finding hidden in prose.

## Determine the delivery status

Use one status:

| Status | Meaning |
|---|---|
| Complete | All planned artifacts exist; required reviews pass; no blocking issue remains |
| Complete with known limitations | Required artifacts and reviews pass, with explicit non-blocking limitations |
| Provisional | Useful output exists, but assumptions or unconfirmed decisions may change material behavior |
| Blocked | Missing evidence or decisions prevent a trustworthy part of the delivery |

List omitted and not-applicable artifacts separately. Never use `Complete` when a required artifact, baseline confirmation, ASCII interaction state, acceptance criterion, or blocking decision is missing.

## Persist the review and delivery summary

Every completed full-shaping Markdown artifact must contain a section headed `Review and delivery summary` or its localized equivalent, such as `Review 与交付摘要`.

Place it near the end of the primary `ux-requirements.md` for every profile. In Modular delivery, keep `index.md` to navigation and mirror only the summary status/link.

Use:

```markdown
## Review and delivery summary

### Delivery status

| Item | Result |
|---|---|
| Delivery status | Complete / Complete with known limitations / Provisional / Blocked |
| Delivery profile | Compact / Balanced / Modular |
| Split rationale | None for Compact; otherwise the reader/owner/review/release/readability reason |
| Baseline | Version and confirmation record |
| Scope reviewed | Stories, functions, pages, workflows, and release boundary |
| Reviewed on | Date |

### Artifact map

| Artifact | What it contains | Status | Location |
|---|---|---|---|

### Delivered file/document structure

```text
ux-requirements.md
├── Alignment and confirmed baseline
├── Confirmed ASCII UX and local specifications
├── Necessary appendices
└── Review and delivery summary
```

### Coverage

| Area | Included/Provisional/Omitted/Blocked/N/A | Summary | Follow-up |
|---|---|---|---|

### Review results

| Review layer | Result | Findings repaired | Remaining limitation |
|---|---|---|---|
| Structural and deterministic | | | |
| Evidence and baseline | | | |
| Requirement and trace | | | |
| UX and interaction | | | |
| Human-readable document | | | |

### Remaining decisions and risks

| Decision or risk | Impact | Owner/next action | Related IDs |
|---|---|---|---|

### Recommended reading order

1. `ux-requirements.md`
2. Relevant page/function/task chapter
3. Control appendix, when delivered
4. Evidence and research, when delivered
```

Keep the summary concise and link to canonical sections or justified supporting files instead of duplicating their contents.

## Show the delivered structure

After generation is complete, show the actual structure rather than a planned or generic template.

For Balanced or Modular delivery:

- print a compact ASCII directory tree rooted at the output folder;
- include only files that exist;
- identify `ux-requirements.md` as the primary reading entry and show `index.md` only for Modular delivery;
- follow the tree with an artifact table containing each file's purpose and status;
- state the delivery profile and why every supporting/module file was split.

For Compact delivery, show both the file and its internal document hierarchy:

```text
ux-requirements.md
├── Background, objectives, users, and scenarios
├── Confirmed stories and functional decomposition
├── Page/task chapters with ASCII UI and specifications
├── Cross-cutting requirements
├── Traceability and decisions
└── Review and delivery summary
```

Use the headings that actually exist. Do not claim an appendix, page file, ASCII UI supplement, or traceability file was produced when it was omitted, blocked, or not applicable.

## Tell the user what was delivered

After the persisted review record is complete, give the user a self-contained handoff message. Lead with the delivery outcome rather than the work performed.

Include:

1. delivery status, profile, split rationale, location, format, baseline version, and scope;
2. actual file/document tree and a file map with one-sentence descriptions;
3. coverage of users, scenarios, stories, functions, pages, flows, sequential ASCII UX confirmations, UI states, specifications, and acceptance criteria;
4. deterministic and manual review results;
5. important repairs made during review;
6. remaining limitations, assumptions, risks, blocked items, and omitted or not-applicable artifacts;
7. recommended reading order;
8. the next decision or action, if one remains.

For Compact delivery, combine these into a short paragraph and compact list. For Balanced or Modular delivery, use a small artifact table and link each file. Do not paste the entire index or a long traceability matrix into chat.

Do not claim factual correctness, user approval, usability validation, accessibility compliance, or implementation readiness unless the applicable evidence and review support that claim.

## Required handoff checks

Before yielding:

- the persisted `Review and delivery summary` exists;
- the displayed tree contains only delivered files and matches the artifact map;
- the profile matches the actual file count and every split has a material rationale;
- all links in the handoff resolve to real artifacts;
- file descriptions match their current contents and statuses;
- reported coverage matches the document and validator results;
- ASCII confirmation coverage reports confirmed, superseded, omitted, and blocked units accurately;
- repaired findings are no longer present;
- remaining limitations and blocking issues are explicit;
- omitted, provisional, blocked, and not-applicable artifacts are distinguished;
- the user can tell what to read first and what decision or action comes next;
- no internal-only path, scratch file, stale status, or unsupported completion claim is exposed.

If the review cannot complete, report the delivery as provisional or blocked and explain the exact reason. A partial document plus an honest handoff is preferable to a false complete status.
