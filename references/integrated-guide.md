# Human-readable UX guide and requirements specification

Use this reference to present a reader-first UX requirement guide backed by an implementable control appendix or linked specification files.

## Contents

- Core structure
- Confirmation boundary
- Information layers
- Foundation contract
- Story-to-experience derivation contract
- Page and feature chapter contract
- Subfeature and task contract
- Placement rules
- Example block
- Appendix contract
- Review and handoff contract

## Core structure

Organize the reading experience by user need:

```text
At a glance
  → why this matters
  → objectives and non-goals
  → people and target scenarios
  → mental model and product language
  → confirmed stories
  → story-derived functional points
  → starting surface and page topology
  → interaction logic and pattern rationale
  → experience overview
  → task-by-task ASCII flows and UI
  → key states, decisions, risks, and open questions
  → supporting specification and evidence links
```

Use task-led chapters instead when one workflow spans several pages. Do not organize the main body as “all stories → all UI → all specs.” Readers should understand one complete page, subfeature, or task without jumping across the document.

## Confirmation boundary

For a new or materially revised requirement, first write the reader-friendly alignment sections from `assets/requirement-alignment-template.md` into `ux-requirements.md`. They contain evidence, background, objectives, people, scenarios, terminology, scope, and complete candidate stories, but not final IA, detailed specifications, or ASCII UI. After explicit confirmation, extend the same document instead of composing a duplicate guide.

Keep the confirmed baseline version and `DEC-BASELINE` link visible in the integrated guide. If detailed design exposes a material change, return only the affected story/scope slice for reconfirmation before updating dependent UI and specifications.

Baseline confirmation authorizes detailed design but does not pre-approve its ASCII UX. Apply `progressive-ascii-confirmation.md`: confirm the experience topology, page overview, and dependent section/function slices one at a time; write each confirmed slice with its adjacent rules; and use confirmed upstream ASCII decisions as context for later chapters.

## Information layers

Keep content layers visible but place them according to reader need:

| Layer | Reader question | Content | Placement |
|---|---|---|---|
| User guidance | How do I complete this task? | Goal, prerequisites, ASCII task flow, steps, result, recovery | Main guide |
| Interaction explanation | How does the experience move? | ASCII decisions, states, frames, and concise behavior | Main guide |
| Requirement control | What exactly must be implemented and verified? | Atomic rules, matrices, contracts, evidence, traceability | Appendix or supporting files |

Use plain product language in the main guide. Preserve precise engineering and domain constraints in supporting specification tables.

## Foundation contract

Before page or task chapters in the main guide, include:

1. an at-a-glance summary;
2. requirement background, current experience, impact, and why now;
3. business and user outcomes, non-goals, and scope;
4. primary users, affected people, and target scenarios;
5. the small set of concepts and terms needed to understand the experience;
6. experience overview, primary journeys, and release boundary;
7. links to repository evidence, external research, requirement register, and control appendices.

Do not lead with repository metadata, source ledgers, or traceability. Summarize their relevant implications and link to the full detail.

## Story-to-experience derivation contract

After baseline confirmation and before page chapters, make the experience derivation visible:

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
| US/JS reference and intended result | FUNC reference and user-recognizable capability | Chosen pattern and why it fits | Destination, trigger, and return behavior |

Use a many-to-many mapping when one story needs several capabilities or one capability supports several stories. Do not force one story into one page, and do not invent pages independently of confirmed stories. Choose the starting surface from the user’s task: use an overview for cross-object status, a resource list for collection management, a work queue for prioritized work, a detail-first entry for a known object, a direct task surface for a focused operation, or a configuration surface for policy and defaults.

## Page and feature chapter contract

Derive each page or broad feature from the story-to-experience map, then use this structure:

1. Page/feature name, purpose, and scope
2. Applicable roles, derived FUNC/US/JS references, starting-surface model, and entry paths
3. Page-level ASCII overview with labeled regions
4. Region and subfeature legend
5. Shared navigation, filters, selection, refresh, permission, and state rules
6. Functional decomposition table
7. One section per subfeature

Create and follow the ASCII UX confirmation queue before canonicalizing these chapter elements. Confirm the page overview before dependent subfeatures, and confirm each subfeature or task slice before composing later dependent slices.

Use this compact main-guide table:

| Subfeature | User purpose | Main interactions | Important states |
|---|---|---|---|

Give each important region a stable label such as `[A]`, `[B]`, or `[C]` in the overview. Put its `SUB` and trace references in a short line or supporting specification.

## Subfeature and task contract

Repeat this structure for every primary task:

1. Subfeature name, purpose, and user outcome
2. Applicable roles
3. Preconditions and entry path
4. Canonical user story or job story
5. Interaction-logic summary covering context, object/state, decision, action, system response, visible feedback, next step, exit, and recovery
6. Material pattern rationale, including dialog versus dedicated page when applicable
7. ASCII task/decision flow showing main, alternate, and recovery paths
8. ASCII swimlane or async sequence when ownership, waiting, notification, or re-entry matters
9. Numbered operating steps and expected result
10. ASCII UI covering every user-visible interaction, with separate frames for each materially different state
11. Plain-language summary of what the user sees, can do, and what happens next
12. Critical states, exceptions, recovery, decisions, and assumptions
13. Link to local specifications, accessibility detail, acceptance criteria, and trace IDs

Keep one task chapter focused on one user-recognizable result.

Draw or reference an ASCII UI frame for every user-visible interaction behavior. Draw a focused frame when a subfeature has a dialog, expanded region, editable state, bulk action, validation state, long-running state, error, or recovery behavior. Do not use drawer-like surfaces. Reference the page-level overview only when it visibly contains the relevant control, feedback, and result and a separate frame would add no information.

## Placement rules

1. Place a compact plain-language behavior summary immediately after the frame.
2. Define each element or rule once; reference its ID elsewhere.
3. Keep happy, loading, error, partial-success, and recovery frames together within the task.
4. Keep page-level rules after the overview and subfeature rules after focused frames.
5. Put shared permission, state, data, audit, and non-functional rules in appendices.
6. Keep evidence ledgers, assumptions, conflicts, and research needs in an internal-control appendix.
7. Omit unresolved content from a published user manual or mark the entire document as a provisional draft.
8. Keep each story definition with its canonical page/subfeature or cross-page task; reference it elsewhere.
9. Treat ASCII as a structural/behavioral view and state the experience constraints it cannot demonstrate.
10. Place the task flow before operating steps and UI frames; move wide or exhaustive flow, state, permission, and contract tables to supporting specifications.
11. Keep main-body tables to roughly two to five columns; split or relocate wider tables.
12. Put descriptive/name/outcome columns first and stable or related ID columns last; use trace lines or detail links instead of making IDs the visual title.

## Example block

```text
### Deployments

Trace: PAGE-02

Page purpose: View and manage deployments in the current environment.

PAGE-02 · Overview
┌──────────────────────────────────────────────┐
│ Deployments                    [A: Create]   │
├──────────────────────────────────────────────┤
│ [B: Scope] [C: Status filter] [D: Search]   │
├──────────────────────────────────────────────┤
│ [E: Deployment list and row actions]         │
└──────────────────────────────────────────────┘

### Create deployment

Trace: SUB-02-01 · TASK-02

Goal: Create a runnable environment from an approved deployment plan.
Role: Environment administrator
Prerequisites: Create permission; an available target environment.

TASK-02 · Create deployment
[Open deployments]
        |
        v
[UI-02-01 Configure] -> [Review impact] -> [Start deployment]
        ^                       |
        |                       +-- pre-check fails --> [Correct configuration]
        +---------------------------------------------------------+

Steps:
1. Open Deployments and select Create deployment.
2. Select a deployment plan and target environment.
3. Review the affected resources and select Start deployment.

UI-02-01 · Create deployment · Default
┌──────────────────────────────────────────────┐
│ Create deployment                           │
│ Deployment plan [ Select                ▾ ] │
│ Target environment [ Select             ▾ ] │
│ [Cancel]                     [Start deploy] │
└──────────────────────────────────────────────┘
```

Follow the frame with a compact reader summary:

| Area | What the user sees | What the user can do | Important behavior |
|---|---|---|---|
| Deployment plan | Approved plans in the current scope | Select one plan | Required; changing it refreshes the resource summary |

Detailed requirements: SPEC-12 · AC-07

## Appendix contract

Use appendices for:

- repository and public-source evidence ledgers;
- requirement register and full story map;
- confirmed happy paths, first-principles basis, adversarial review, branch inventory, and `DEC-HAPPY` records;
- shared role and permission matrix;
- global lifecycle and state definitions;
- extended terminology dictionary;
- UX hypotheses and validation plan;
- information architecture and cross-page task flows;
- data, synchronization, audit, and retention requirements;
- interaction-to-system contracts that apply across several tasks;
- accessibility, input, responsive/adaptation, and dense-data requirements;
- non-functional requirements;
- traceability matrix;
- evidence, decisions, assumptions, conflicts, and open research.

## Review and handoff contract

After composing the guide and supporting specifications, apply `review-and-handoff.md`: review, repair canonical sources, revalidate affected artifacts, persist the `Review and delivery summary`, and show the actual file/document structure, what each artifact contains, what was reviewed, what remains limited or blocked, what to read first, and what happens next.
