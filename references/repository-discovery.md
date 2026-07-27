# Repository discovery and current-state grounding

Use this reference before readiness assessment whenever the requirement relates to an available project repository.

## Contents

- Purpose
- Discovery boundary
- Establish the repository snapshot
- Read repository instructions
- Build a bounded source inventory
- Search from user language to implementation
- Trace current behavior
- Classify repository evidence
- Maintain the evidence ledger
- Compare current, documented, and requested behavior
- Detect drift and legacy behavior
- Ground product terminology
- Decide what still requires clarification
- Required repository-context output
- Large-document ownership
- Safety and quality checks

## Purpose

Repository discovery prevents requirement shaping from treating an existing product as a blank slate. It answers four separate questions:

1. What does the product implement now?
2. What do product documents say it should do?
3. What change is the user requesting?
4. What remains unknown or requires a product decision?

Do not collapse these questions into one narrative. A polished document must not hide conflicts between them.

## Discovery boundary

Keep discovery:

- read-only unless the user separately requests implementation or documentation edits;
- relevant to the stated product area;
- broad enough to trace behavior across layers;
- bounded enough to avoid indexing the entire repository without purpose;
- explicit about unavailable, excluded, generated, or stale sources.

Do not change code, configuration, dependencies, generated files, test data, or product documentation during requirement analysis.

## Establish the repository snapshot

Record the analyzed baseline before drawing conclusions:

| Field | Record |
|---|---|
| Repository or package | Name or repository-relative location |
| Workspace root | Repository root, not a home-directory assumption |
| Branch | Current branch when available |
| Commit | Current commit when available |
| Working tree | Clean, modified, or unknown |
| Analysis scope | Relevant modules, packages, services, or applications |
| Exclusions | Unavailable systems, generated sources, external services, or intentionally skipped areas |

Treat uncommitted changes as part of the observed workspace, but do not assume they represent an accepted product decision.

## Read repository instructions

Before interpreting source files, locate and read applicable instructions:

1. root and directory-scoped `AGENTS.md`;
2. `CLAUDE.md` or equivalent agent guidance;
3. root and package `README` files;
4. contribution and development guides;
5. documentation indexes and architecture decision indexes;
6. product-specific glossaries, UX guidelines, or design-system guidance.

Apply scoped instructions to files beneath their directory. Record which instructions governed the analyzed area.

## Build a bounded source inventory

Use `rg --files` first to identify likely sources. Prefer focused paths and file types.

Include as relevant:

- product requirements, feature guides, user manuals, release notes, and support content;
- architecture decisions, domain notes, and API contracts;
- routes, pages, components, commands, forms, and navigation definitions;
- UI copy, localization catalogs, help text, validation messages, and error messages;
- models, schemas, migrations, enums, state machines, policies, and permission checks;
- services, APIs, jobs, events, persistence, and external-integration adapters;
- tests, fixtures, examples, stories, and snapshots.

Exclude or de-prioritize:

- dependency trees such as `node_modules`;
- vendored code;
- build, distribution, coverage, cache, and generated-output directories;
- secrets, credentials, `.env` files, private keys, and production data;
- unrelated packages or historical exports.

Do not read sensitive files merely because they match a term.

## Search from user language to implementation

Search iteratively rather than relying on one exact phrase:

1. exact terms in the request;
2. product-facing synonyms and translated alternatives;
3. existing UI labels and navigation terms;
4. engineering/domain terms and acronyms;
5. route, component, API, model, enum, permission, and state names;
6. related validation, error, audit, and test language.

Use `rg` for text search. Start with likely directories, then widen only if necessary.

If a user-facing term cannot be found, search for the underlying action, object, state, and permission rather than concluding that the behavior is absent.

## Trace current behavior

For each important user task, trace the smallest relevant path:

```text
Navigation or entry point
  → visible UI and product copy
  → user action and interaction state
  → validation and authorization
  → API, service, event, or job
  → domain model and persistence
  → integration boundary
  → tests and documentation
```

Not every requirement needs every layer. Follow enough layers to support the claim being made.

For a large feature, trace by subfeature or user task so evidence remains reviewable.

## Classify repository evidence

Repository sources have different authority:

| Source type | What it can support | Important limitation |
|---|---|---|
| Code, configuration, schema | Current implemented behavior and structural constraints | May contain dead, gated, partial, or unreleased behavior |
| Tests and fixtures | Executable expectations and covered edge cases | May be incomplete, stale, or implementation-coupled |
| UI copy and localization | Current product-facing language | May include legacy, hidden, or unused strings |
| User guides and support docs | Documented user workflow and mental model | May lag the implementation |
| Product specs and decision records | Intended behavior and rationale at a point in time | May be superseded or only partly delivered |
| API and domain names | Technical contract and system concepts | Are not automatically suitable user-facing terms |
| Comments and internal names | Implementation clues | Weak evidence for product intent or user language |
| Git history | Change history and prior rationale | Use only when current sources cannot explain a relevant discrepancy |

Code is evidence of implementation, not automatically evidence of desired behavior. Documentation is evidence of intent or communicated behavior, not automatically evidence of the deployed implementation.

## Maintain the evidence ledger

Give every important repository finding a stable source ID.

| Type | Repository-relative path:line | Evidence summary | Supports | Authority/freshness | Conflicts | SRC ID |
| --- | --- | --- | --- | --- | --- | --- |
| UI copy | `app/...:42` | Existing user-facing label | CON-001 | Current workspace | None known | SRC-REP-001 |
| Test | `tests/...:88` | Permission denial is expected | SPEC-014 | Executable expectation | Guide omits restriction | SRC-REP-002 |

Prefer repository-relative paths so the document remains portable. Add a line number where practical. Do not paste large code blocks; summarize the evidence and link or cite its location.

Mark an inference as an inference even when it is strongly suggested by several files.

## Compare current, documented, and requested behavior

Use a delta table before proposing the future state:

| Current status | Current implemented behavior | Documented intent | Requested behavior | Delta | Risk or dependency | Evidence | Area or ID |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use one of these status labels:

- `Existing`
- `Partially implemented`
- `Documented only`
- `Implemented but undocumented`
- `Contradictory`
- `Deprecated or legacy`
- `Absent`
- `Unknown`

Do not describe an existing capability as a new requirement. Do not describe an undocumented implementation as an accepted product rule without confirmation.

## Detect drift and legacy behavior

Create an explicit drift record when:

- code and tests disagree;
- code and user documentation disagree;
- a product spec describes behavior that is absent or partial;
- UI copy uses a legacy name while the domain model uses a newer name;
- several modules implement the same rule differently;
- feature flags, editions, deployments, or permissions create multiple valid behaviors;
- comments or old decisions appear superseded.

Record:

| Sources in conflict | Observed difference | User impact | Requirement impact | Resolution owner/status | DRIFT ID |
| --- | --- | --- | --- | --- | --- |

Do not silently choose the newest file, the code, or the document. Freshness is evidence, not automatic authority.

## Ground product terminology

Before inventing names, inventory the language already used by the product.

Use this preference order when the terms are accurate:

1. active UI labels, navigation, help text, validation, and errors;
2. current user manuals, support content, and training material;
3. product and domain documentation;
4. public or stable API/domain terminology;
5. internal implementation names.

If existing user-facing language is misleading, explain the mismatch and propose a migration instead of silently renaming it.

Distinguish:

- the technical object name;
- the existing product term;
- the user's likely mental model;
- the proposed product term;
- aliases or deprecated terms needed for transition.

## Decide what still requires clarification

Before asking a question:

1. check whether a bounded repository search can answer it;
2. check whether the answer is implemented behavior, documented intent, or a new decision;
3. check whether conflicting evidence makes a domain owner necessary;
4. ask only if the answer materially changes users, scope, permissions, lifecycle, data, terminology, workflow, risk, or success.

Questions that repository discovery should usually answer include:

- current page names and entry points;
- existing fields, states, actions, validations, and error copy;
- present permission checks;
- implemented API or model constraints;
- covered unhappy paths;
- existing user-facing terminology.

Questions that often still require a user or owner include:

- whether current behavior is correct or accidental;
- which conflicting source is authoritative;
- business priority and why now;
- intended target user or scenario;
- future-state policy;
- success thresholds and rollout decisions.

## Required repository-context output

When repository evidence is available, include:

1. repository snapshot and analyzed scope;
2. applicable instructions and source inventory;
3. evidence ledger;
4. current implemented behavior;
5. documented intent;
6. code/documentation/test drift;
7. current-versus-requested delta;
8. discovered constraints, permissions, states, and dependencies;
9. existing and proposed terminology;
10. unresolved questions and required decision owners.

If no relevant evidence is found, say what paths and terms were searched. `No evidence found` is not the same as `the feature does not exist`.

## Large-document ownership

For a multi-file requirement deliverable, use `00-repository-context.md` as the canonical home for:

- snapshot and scope;
- source inventory and evidence ledger;
- current-state behavior;
- documented intent;
- drift records;
- requested delta;
- repository-derived constraints.

Other files should reference these findings by `SRC`, requirement, or drift ID instead of duplicating them.

Omit `00-repository-context.md` only when no repository or codebase is available. Record that limitation in `index.md`.

## Safety and quality checks

Before completing repository discovery, verify:

- applicable repository instructions were read;
- searches covered user language, product language, and implementation language;
- conclusions cite repository-relative locations where practical;
- generated, vendored, unrelated, and sensitive paths were avoided;
- current implementation and intended behavior are not conflated;
- feature flags, permissions, editions, or deployment differences are visible;
- absent search results are not treated as proof of absence;
- documentation/code/test drift is explicit;
- questions are limited to facts or decisions the repository could not resolve;
- discovery remained read-only;
- future-state recommendations are separated from observed current state.
