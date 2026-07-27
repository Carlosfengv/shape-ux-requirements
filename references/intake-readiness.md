# Intake readiness

Use this reference to assess whether requirement input is trustworthy enough to shape.

## Contents

- Accuracy boundaries
- Evidence labels
- Completeness dimensions
- Blocking test
- Readiness statuses
- Assessment tables
- Clarification strategy
- Baseline after clarification

## Accuracy boundaries

Distinguish four questions:

| Question | What to do |
|---|---|
| Is the language understandable? | Detect ambiguity, undefined terms, vague verbs, and unclear references |
| Is the information complete? | Check whether decisions required for the requested output are present |
| Is the input internally consistent? | Compare roles, rules, terms, states, scope, and examples for conflicts |
| Is the input factually true? | Verify only against authoritative evidence or explicit domain-owner confirmation |

Never claim factual validation from coherence alone.

## Evidence labels

Assign one label to each material statement:

| Label | Meaning |
|---|---|
| Source-confirmed | Supported by an identified authoritative source |
| Repository-code-confirmed | Supported by current code, configuration, or schema as implemented behavior |
| Repository-test-confirmed | Supported by an executable test or fixture as expected behavior |
| Repository-doc-confirmed | Supported by repository product documentation or a decision record as documented intent |
| User-confirmed | Explicitly confirmed by the responsible user or decision owner |
| Provided-unverified | Stated in the input but not independently supported |
| Inferred | Derived from other statements; show the reasoning |
| Assumed | Temporarily adopted to continue; show the impact if wrong |
| Unknown | Not available |
| Conflicted | Incompatible statements or sources exist |

Record source, owner, confidence, and last update when known.

## Completeness dimensions

Check only dimensions relevant to the request, but always inspect the first nine:

1. Background, current state, trigger, evidence, impact, and why now
2. Business objectives, user objectives, non-goals, and success measures
3. Primary users, secondary users, affected parties, document audiences, and system actors
4. Target scenarios, user goals, task context, and current workarounds
5. Current state and target state
6. Scope and system boundary
7. Core objects and relationships
8. Business rules and precedence
9. Permissions and data boundaries
10. Lifecycle, states, and transitions
11. Validation and failure behavior
12. Dependencies and integrations
13. Data source, freshness, retention, and sensitivity
14. Audit, security, compliance, and reversibility
15. Performance, scale, availability, accessibility, and rollout constraints

## Blocking test

Treat a gap as blocking when a plausible answer would materially change one or more of:

- the problem being solved, intended outcome, primary target user, or primary target scenario;
- target users or responsibilities;
- product scope or system boundary;
- core object model or terminology;
- permissions or data visibility;
- business-rule precedence;
- lifecycle or destructive behavior;
- success, failure, rollback, or partial-success behavior;
- security, compliance, financial, or operational risk;
- the primary interaction flow.

Treat cosmetic detail, low-risk copy, secondary sorting, or explicitly deferrable behavior as non-blocking unless the user states otherwise.

For a full requirement document, do not mark the input `Ready` when the background/problem, objectives, primary target users, or primary target scenarios are unknown. Use `Ready with assumptions` only for an explicitly requested exploratory draft and label those sections provisional.

## Readiness statuses

| Status | Condition | Response |
|---|---|---|
| Ready | Required information is present and no material conflicts remain | Proceed |
| Ready with assumptions | Only non-blocking gaps remain and assumptions are explicit | Proceed provisionally |
| Clarification required | A blocking decision or definition is missing | Ask questions before shaping |
| Evidence required | A critical claim needs a source or owner confirmation | Request the evidence |
| Conflicted | Two material statements cannot both be true | Present the conflict and request a decision |

Use a score only as a secondary summary. Never let a high score override one blocking gap.

## Assessment tables

Use an input assessment table:

| Dimension | Current understanding | Status | Impact | Next action | ID |
| --- | --- | --- | --- | --- | --- |

Use a statement ledger:

| Statement | Type/evidence label | Source or owner | Confidence | Affected outputs | STMT ID |
| --- | --- | --- | --- | --- | --- |

Use a conflict table:

| Statement A | Statement B | Why incompatible | Decision owner | Status | CFLT ID |
| --- | --- | --- | --- | --- | --- |

## Clarification strategy

Prioritize questions by:

1. safety and irreversible impact;
2. scope, role, permission, and object-model impact;
3. primary-flow and business-rule impact;
4. exception and operational impact;
5. presentation detail.

Ask 1–3 questions per round. For each question:

- restate the current understanding;
- name the missing decision;
- explain the downstream impact;
- offer concrete, mutually exclusive choices when appropriate;
- allow the user to provide a different answer;
- identify the likely decision owner when the current user may not own it.

Do not ask “Please provide more details.” Ask for a specific decision or artifact.

### Choose the interaction type

Prefer a structured choice component over a prose menu when the host provides one.

| Question type | Interaction |
|---|---|
| One decision with 2–3 mutually exclusive answers | Structured single-select choice |
| Several compatible choices | Structured multi-select only when supported |
| Explanation, evidence, source material, or unbounded domain fact | Free-text input |
| A choice whose valid options are not yet understood | Ask a free-text discovery question first |

When `request_user_input` or an equivalent tool is available:

- use it instead of asking the user to type `1`, `2`, `3`, or `4`;
- keep the question to one sentence;
- keep the header short and specific;
- provide 2–3 mutually exclusive choices;
- put a genuinely recommended choice first and label it recommended only when evidence supports that recommendation;
- explain each option's product impact in one short sentence;
- rely on the component's free-form “Other” path when provided;
- do not use automatic resolution for a blocking question;
- use automatic resolution for a non-blocking question only when continuing with an explicit assumption is safe.

Do not force a bounded choice when the domain owner may need to describe a different rule. Do not simulate multi-select with a single-select component.

If no structured input component is available, ask one concise natural-language question at a time. Follow higher-priority host requirements for fallback formatting, but never imply that a manual numbered menu is an interactive component.

### Process the response

After the user selects or enters an answer:

1. Convert the answer into a `STMT`, decision, constraint, or evidence request.
2. Record the selected option's implications and rejected alternatives when material.
3. Update or close the related `Q` ID.
4. Reassess affected blockers.
5. Ask the next batch only if blocking gaps remain.

## Baseline after clarification

Create a baseline table:

| Baseline item | Category | Evidence | Owner | Status | Item ID |
| --- | --- | --- | --- | --- | --- |

Use these categories:

- In scope
- Out of scope
- Fact
- Decision
- Assumption
- Constraint
- Open non-blocking question

After every answer, update—not duplicate—the affected statement, question, and baseline entries.
