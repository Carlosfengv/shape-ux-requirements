# Human-readable UX requirement documents

Use this reference to make the primary requirement document easy for UX designers, PMs, domain experts, and reviewers to read before exposing detailed control and implementation material.

## Contents

- Reader priority
- Use two information layers
- Design the reading path
- Write sections for scanning
- Keep tables readable
- Keep IDs and evidence unobtrusive
- Present ASCII for people
- Structure task chapters
- Handle decisions and uncertainty
- Readability review

## Reader priority

Treat the primary document as a communication artifact, not a database export. A reader should understand within a few minutes:

1. why the change matters;
2. who experiences the problem;
3. which scenario and outcome are in scope;
4. how the proposed experience works;
5. what remains undecided or risky.

Optimize the main body for UX and requirement discussion. Preserve implementation precision in linked appendices or supporting files.

## Use two information layers

Separate:

| Layer | Primary audience | Content |
|---|---|---|
| Human-readable guide | UX, PM, domain owners, reviewers | Context, users, scenarios, mental model, journeys, ASCII UI, key states, decisions, risks |
| Requirement control appendix | Engineering, QA, security, delivery reviewers | Evidence ledger, atomic specs, system contracts, full permission/state matrices, NFRs, traceability |

The main guide may summarize a canonical rule and link its ID. Do not duplicate the full rule. A reader should not need the appendix to understand the intended experience, but should be able to open it to verify exact behavior.

## Design the reading path

Use this order:

```text
At a glance
  -> Why this matters
  -> People and scenarios
  -> Mental model and terminology
  -> Confirmed happy paths
  -> Experience overview
  -> Task-by-task flows and ASCII UI
  -> Key states, decisions, risks, and open questions
  -> Supporting specification and evidence links
```

Start with an “At a glance” block containing the problem, primary user, desired outcome, scope, status, and the most important open decision. Do not make repository metadata or an evidence ledger the first substantive reading experience.

For Modular delivery, make `ux-requirements.md` the first content link in `index.md`. Treat `index.md` as navigation and progress, not the document readers are expected to interpret as the requirement itself. Balanced delivery does not need an index.

## Write sections for scanning

Begin every major section with a short plain-language summary before diagrams or tables. Use headings that answer reader questions, such as:

- Why does this need to change?
- Who is affected?
- What is the user trying to accomplish?
- How does the experience work?
- What can go wrong?
- What is still undecided?

Use:

- short paragraphs;
- one primary message per section;
- bullets for three or more parallel points;
- bold-free or restrained emphasis;
- explicit “Decision,” “Risk,” “Assumption,” and “Open question” callouts;
- links to detail instead of repeating it.

Avoid long introductory prose, generic executive-summary language, repeated definitions, and headings based only on artifact names.

## Keep tables readable

In the main guide:

- prefer two to five columns;
- keep each cell to one idea or a short sentence;
- split a wide table by reader question;
- use a short card or bullets when only one entity is being described;
- use a diagram for sequence, hierarchy, or branching;
- move dense matrices and exhaustive inventories to the control appendix.

Suitable main-body tables include:

- current problem versus desired outcome;
- user/scenario summary;
- concise terminology mapping;
- scope and release summary;
- key UI regions and their purpose;
- critical exception and recovery behavior;
- decisions and open questions.

Permission matrices, detailed state transitions, system contracts, evidence ledgers, and full traceability normally belong in appendices.

## Keep IDs and evidence unobtrusive

Keep stable IDs for traceability, but do not let them dominate the prose.

- Put an ID at the end of a heading, in a small `Trace:` line, or in the last column of a compact table.
- In every table, put the human-readable subject, name, purpose, outcome, behavior, or status columns first. Move stable IDs and related/source/specification ID references to the final columns, preserving their internal order.
- Do not use an ID-only column as the reader's entry point. If the identifier is inseparable from a state or object name, show the readable name first and keep the identifier at the end or in a trace line.
- Use user-facing names in ASCII nodes; add IDs only where cross-reference is useful.
- Do not start every sentence or bullet with an ID.
- Keep source paths, URLs, confidence labels, and conflict details in evidence sections.
- Use a short “Basis” or “Related requirements” line in the main guide.

Prefer:

```text
Create a deployment
Trace: TASK-02 · US-04 · REQ-07
```

Avoid:

```text
TASK-02 / US-04 / REQ-07 / FLOW-08 / UI-09 / SPEC-11
```

as the primary title a reader must decode.

## Present ASCII for people

Introduce each ASCII flow or UI with:

1. what the reader should notice;
2. which state or decision it represents;
3. whether it is confirmed or provisional.

Use user language inside the diagram. Keep technical IDs in labels only when they help navigation. After the diagram, explain the important behavior in three parts:

- what the user sees;
- what the user can do;
- what happens next or when something fails.

Every user-visible interaction described in the guide must appear in at least one ASCII UI/state frame. A flow or prose step alone is not sufficient. Keep the mapping readable with a compact table such as `Interaction | ASCII UI/state | Visible change or feedback | Detail link`; let several interactions share one frame when it remains clear, and add a new frame only for a materially different visible state.

Do not place a ten-column specification table immediately after every frame in the human-readable guide. Use a compact interaction summary and link to the detailed local specification.

## Structure task chapters

For each primary task, use:

1. User goal
2. When and where this happens
3. Preconditions
4. Confirmed `FLOW-HP` with observable completion evidence
5. Linked alternate, failure, exit, and recovery flows
6. Numbered operating steps
7. ASCII UI covering every user-visible interaction, with separate frames for materially different states
8. What the user sees and can do
9. Exceptions and recovery
10. Key decisions or assumptions
11. Links to detailed requirements and acceptance criteria

Keep one chapter focused on one user-recognizable outcome. If a page supports several unrelated goals, split it into subfeature/task sections.

## Handle decisions and uncertainty

Do not bury uncertainty in evidence tables. Show important items close to the affected experience:

> **Decision needed:** Who may retry failed items after a partial bulk operation?
>
> **Why it matters:** The answer changes available actions and audit ownership in the recovery state.

Use a short decision/open-question summary near the end of the main guide, with links to the full control log.

## Readability review

Before delivery, perform:

- **Five-minute test:** Can a UX/PM reader explain the problem, user, scenario, and proposed experience after a quick read?
- **Skim test:** Do headings and diagrams tell a coherent story without reading every table?
- **Jargon test:** Are engineering terms translated or explained where first used?
- **Table test:** Can each main-body table be read without horizontal scrolling in a typical Markdown viewer?
- **ID test:** Do IDs support navigation without becoming the visual hierarchy?
- **Action test:** Are decisions, risks, assumptions, and next steps easy to find?
- **Layer test:** Can detailed evidence and system rules be moved to an appendix without losing the main experience narrative?

Revise the document when the main body feels like a schema, issue tracker, or traceability export rather than a UX requirement guide.
