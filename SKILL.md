---
name: shape-ux-requirements
description: Compatibility entrypoint for the Shape UX Requirements skill bundle. Use for end-to-end enterprise UX requirement shaping that spans requirement baseline, happy-path review, ASCII interaction design, and final specification delivery. For one bounded phase, prefer the matching specialist skill in this repository.
---

# Shape UX Requirements · Compatibility Entrypoint

This root skill preserves existing standalone installations. The canonical implementation is the plugin bundle under `skills/`.

## Route the request

- For raw input assessment, repository grounding, problem framing, terminology, stories, or baseline confirmation, read `skills/shape-requirement-baseline/SKILL.md` and follow it.
- For first-principles successful-path derivation, adversarial review, or `DEC-HAPPY` confirmation, read `skills/shape-happy-paths/SKILL.md` and follow it.
- For information architecture, task flows, interaction logic, ASCII UI, or `DEC-ASCII` confirmation, read `skills/shape-ascii-interactions/SKILL.md` and follow it.
- For specifications, acceptance criteria, traceability, document composition, validation, review, or handoff, read `skills/deliver-ux-requirements/SKILL.md` and follow it.
- For a request spanning multiple phases, read `skills/shape-ux-requirements/SKILL.md` and use its orchestration contract.

Do not load every specialist skill for a narrow request. Keep stable IDs and confirmed decisions unchanged when handing artifacts between phases.
