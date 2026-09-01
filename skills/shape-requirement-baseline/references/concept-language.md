# Concept and product language

Use this reference to convert complex engineering vocabulary into precise user-facing concepts.

## Contents

- Maintain three language layers
- Build the user mental-model hypothesis
- Create a concept dictionary
- Identify UX hypotheses
- Explain at four levels
- Naming rules
- Model relationships
- Detect dangerous language
- Validate terminology

## Maintain three language layers

| Layer | Audience | Purpose |
|---|---|---|
| Engineering language | Engineers and architects | Preserve implementation precision |
| Domain language | PMs and domain experts | Describe business objects, rules, and relationships |
| Product language | End users | Support recognition, decisions, and tasks |

Do not assume one-to-one translation. Decide whether to:

- preserve a concept;
- rename it;
- merge several internal concepts;
- split one internal concept by user task;
- hide it from the UI;
- expose it only in advanced, diagnostic, API, or audit contexts.

When a repository is available, first inventory active UI copy, navigation, help text, validation and error messages, localization catalogs, user documentation, domain/API names, and internal implementation names. Prefer accurate existing product-facing language over new terminology; treat internal names as traceability inputs, not automatic UI labels.

## Build the user mental-model hypothesis

For each role, identify:

| Dimension | Question |
|---|---|
| Goal | What result is the user trying to obtain? |
| Trigger | Why does the task begin now? |
| Familiar objects | What does the user believe they are working with? |
| Expected sequence | How does the user expect the task to unfold? |
| Decision information | What must the user know before acting? |
| Risk perception | What mistakes or losses concern the user? |
| Completion signal | How does the user know the task succeeded? |
| Vocabulary | Which words does the user already use? |

Label each claim as research-backed, domain-owner-confirmed, observed in product data, inferred, or assumed.

When a downstream flow-model or interface-model review is planned, treat this role-specific hypothesis as required handoff context. If the primary role or scenario is missing, the review is Blocked. If material dimensions are inferred, assumed, unknown, or conflicted, the downstream review may continue only as Provisional and must not claim user validation.

## Create a concept dictionary

Use one row per stable user-relevant concept:

| Source term | Technical definition | User role/task | Treatment | Product term | UI explanation | Boundary | Evidence | CON ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Use `Treatment` values: Preserve, Rename, Merge, Split, Hide, Advanced-only.

Add these details below the table for important or risky concepts:

- contextual explanation;
- complete definition;
- concrete example;
- non-example;
- lifecycle and ownership;
- related concepts;
- confusing alternatives;
- forbidden or deprecated terms.

## Identify UX hypotheses

Treat claims about user recognition, findability, expected sequence, comprehension, risk perception, and completion signals as hypotheses until supported.

Record concept-specific evidence and confidence in the concept dictionary. Send every material cross-concept or task-level claim to the single canonical `UXH` register owned by `$shape-ascii-interactions`; do not duplicate the hypothesis text here.

Prefer task-based validation over asking whether a label “sounds good.” Define what a representative user must find, explain, predict, or complete.

Do not convert a stakeholder's preferred workflow, the current screen sequence, an API shape, or an implementation model into user-model evidence. Preserve the source and confidence of each expectation so downstream `UXGAP` findings can distinguish a demonstrated mismatch from a hypothesis that still needs testing.

## Explain at four levels

| Level | Typical placement | Rule |
|---|---|---|
| Product term | Navigation, title, field, status | Keep short, stable, and recognizable |
| UI explanation | Tooltip or helper text | Explain purpose in one sentence |
| Contextual explanation | Empty state, confirmation, or error | Explain behavior and consequence in the current task |
| Full definition | Concept guide or help center | Explain meaning, relationships, lifecycle, examples, and boundaries |

Do not force a short label to carry the entire definition.

## Naming rules

1. Name objects by what users recognize, not by storage, API, or orchestration mechanisms.
2. Name actions with verbs that describe the user's intended result.
3. Name states by meaningful outcomes, not internal job states.
4. Keep technically distinct concepts distinct when merging would cause dangerous assumptions.
5. Prefer established domain language over invented simplifications when target users are domain experts.
6. Avoid transliteration and literal engineering translation unless users already use the term.
7. Keep the same concept name across navigation, forms, messages, stories, specs, and help.
8. Qualify role-specific variants explicitly; do not let the same label silently change meaning.
9. Explain inheritance, precedence, synchronization, versioning, and ownership whenever they affect consequences.
10. Preserve original terms in the dictionary so engineers can trace the mapping.

## Model relationships

Represent only relationships needed for understanding or decisions:

```text
[Concept A] --contains--> [Concept B]
[Concept B] --inherits from--> [Concept C]
[Concept D] --created from--> [Concept A]
[Concept D] --deployed to--> [Environment]
```

For each important relationship, specify:

- direction;
- cardinality;
- ownership;
- creation and deletion behavior;
- inheritance or override behavior;
- synchronization behavior;
- effect of later changes.

## Detect dangerous language

Flag:

- one word used for several objects;
- several words used for the same object;
- nouns presented as actions;
- vague verbs such as “process,” “handle,” “support,” or “apply”;
- translated terms that are grammatically correct but unfamiliar to users;
- labels that hide irreversible or broad impact;
- friendly terms that remove essential distinctions;
- status labels that describe system activity but not user consequence.

## Validate terminology

Before accepting a product term, ask:

1. Can the target user predict what object or action it refers to?
2. Does it preserve the technical boundary?
3. Does it distinguish nearby concepts?
4. Does it work in singular, plural, action, status, and error contexts?
5. Can it remain stable as the feature grows?
6. Is the confidence in its user fit explicit?
