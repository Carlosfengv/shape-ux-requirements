# Acceptance criteria

Use this reference after stories and relevant behavior specifications exist.

Write observable criteria that validate user and system outcomes. Link every `AC` to its canonical `US/JS` and applicable `SPEC`, `UI/STATE`, or `FLOW`.

Each criterion should define, when applicable:

- precondition;
- action or event;
- observable result;
- resulting object or lifecycle state;
- permission and data boundary;
- failure, partial-success, or recovery behavior;
- measurable threshold for performance or other non-functional behavior.

Avoid “works correctly,” “is user-friendly,” unbounded “loads quickly,” implementation-only assertions invisible to the requested acceptance surface, and criteria that merely repeat the story.

Use examples to clarify a general rule, never as a substitute for the rule. Do not finalize acceptance when its governing permission, state, precedence, or recovery decision is unresolved; link the blocking question instead.

## Quality checks

Reject or revise an `AC` when:

- it cannot be observed or tested;
- no canonical story or specification owns it;
- it silently assumes an unconfirmed happy path or UI state;
- it checks only successful submission and not the required user-verifiable outcome;
- it duplicates another criterion without a distinct boundary;
- it embeds an arbitrary target that lacks a source or owner.
