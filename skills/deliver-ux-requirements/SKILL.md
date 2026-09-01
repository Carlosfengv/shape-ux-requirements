---
name: deliver-ux-requirements
description: Turn shaped and confirmed UX requirements into atomic specifications, acceptance criteria, traceability, reader-first Markdown artifacts, validation results, and final review/handoff. Use for final document composition or auditing existing deliveries. Do not invent missing upstream product decisions.
---

# Deliver UX Requirements

Package confirmed requirement and interaction artifacts into readable, testable, traceable Markdown without hiding upstream gaps.

## Load references progressively

- Read [references/acceptance-criteria.md](references/acceptance-criteria.md) before writing or auditing `AC`.
- Read [references/spec-and-traceability.md](references/spec-and-traceability.md) before `SPEC/SYS/NFR` tables or trace audits.
- Read [references/human-readable-requirements.md](references/human-readable-requirements.md) before composing the reader-facing body.
- Read [references/integrated-guide.md](references/integrated-guide.md) for a combined guide/specification.
- Read [references/adaptive-delivery-profiles.md](references/adaptive-delivery-profiles.md) and [references/markdown-delivery.md](references/markdown-delivery.md) before creating files.
- Read [references/review-and-handoff.md](references/review-and-handoff.md) before final delivery.

Default to `assets/ux-requirement-guide-template.md`. Use `assets/enterprise-requirement-output-template.md` only for an exhaustive control appendix or explicitly requested single specification. Use `assets/multi-file-index-template.md` only for a justified Modular delivery.

## Input and gap handling

Inspect baseline, `FLOW-HP`, model-fit coverage and `UXGAP`, ASCII confirmation, decisions, sources, and artifact coverage before composing. Do not manufacture missing actors, user-model evidence, permissions, lifecycle rules, error behavior, completion signals, or approvals. Mark the delivery Provisional or Blocked and route the missing decision to the owning upstream stage.

## Workflow

1. Choose Compact, Balanced, or Modular based on reader, owner, review, release, and readability needs; default to Compact.
2. Compose the reader-first guide before dense control tables.
3. Define atomic `SPEC`, state transitions, permissions, validation/error behavior, data/audit behavior, `SYS`, `NFR`, and observable `AC`.
4. Build traceability and coverage without duplicating canonical definitions.
5. Run `scripts/validate_requirement_docs.py <target> --final --profile <stage>` with the narrowest adequate profile; use `full` for completed end-to-end delivery.
6. Review evidence, semantics, target-user model fit, interaction coverage, readability, links, IDs, and delivery structure; repair and revalidate.
7. Persist a review and delivery summary with actual files, coverage, findings, remaining risks, reading order, and next action.

## Stage profiles

- `baseline`: baseline structure and confirmation.
- `happy-path`: baseline plus happy-path basis, adversarial review, and confirmation/waiver coverage.
- `model-fit`: audit-only target role/scenario, reviewed interaction scope, model-fit coverage, and `UXGAP` closure.
- `interaction`: happy-path plus IA, interaction, two-stage model-fit review, ASCII, and `DEC-ASCII` coverage.
- `delivery`: final packaging, specifications, acceptance, traceability, and handoff.
- `full`: all stage contracts together.

The validator checks deterministic structure, model-fit coverage/trace, and Critical-gap closure; it cannot decide whether the interface truly fits a user's model. Manually review evidence quality, product correctness, usability rationale, accessibility constraints, and whether the artifacts express the intended user outcome.
