---
name: shape-requirement-baseline
description: Assess raw or revised enterprise product input against repository and source evidence, then shape problem framing, users, scenarios, concepts, scope, requirements, and stories into a confirmable baseline. Use before happy paths or interface design. Do not produce detailed IA, ASCII UI, or final specifications.
---

# Shape Requirement Baseline

Produce a trustworthy requirement/story baseline and stop before detailed solution design.

## Load references progressively

- When a repository is available, read [references/repository-discovery.md](references/repository-discovery.md) first.
- When current public category or comparable-product evidence matters, read [references/industry-and-product-research.md](references/industry-and-product-research.md).
- Always read [references/intake-readiness.md](references/intake-readiness.md) before judging readiness.
- Read [references/problem-framing.md](references/problem-framing.md) for background, objectives, people, scenarios, scope, and success measures.
- Read [references/concept-language.md](references/concept-language.md) when terminology or mental models matter.
- Read [references/story-shaping.md](references/story-shaping.md) before producing `REQ`, `TASK`, or `US/JS`.
- Read [references/confirmation-gate.md](references/confirmation-gate.md) before asking for baseline approval.

Use assets only for a requested reusable or persisted artifact. Default to the alignment sections in `assets/requirement-alignment-template.md` inside one evolving `ux-requirements.md`.

## Workflow

1. Inventory source authority, repository evidence, current behavior, requested behavior, actors, objects, rules, states, constraints, terminology, decisions, assumptions, unknowns, and conflicts.
2. Label each material statement as fact, decision, inference, assumption, unknown, or conflict and attach its evidence boundary.
3. Assess readiness as Ready, Ready with assumptions, Clarification required, Evidence required, or Conflicted.
4. Ask only 1–3 high-impact questions per round after repository and source discovery. Continue provisionally only when gaps are non-blocking or explicitly authorized.
5. Frame the current problem, why now, business and user objectives, non-goals, target users, affected parties, document audience, primary scenarios, and success signals.
6. Build the concept language, requirement register, outcome/task backbone, complete candidate stories, and conceptual candidate happy paths without binding them to pages or controls.
7. Present the alignment brief and offer a correction path or `确认需求基线并进入「Happy Path 细化与审查」`.
8. On approval, record `DEC-BASELINE-###`, owner/date/conditions, covered IDs, and unresolved non-blocking items.

## Output contract

The canonical baseline contains `SRC/STMT`, current-versus-requested delta, `BG/OBJ`, `ROLE/AUD`, `SCN`, `CON/UXH`, scope/non-goals, `REQ`, `TASK`, canonical `US/JS`, assumptions, conflicts, questions, and baseline status. Preserve existing stable IDs when unambiguous.

Stop after the confirmation handoff. Do not generate detailed `FLOW-HP`, `FUNC`, `IA`, `PAGE`, `INT`, `UI/STATE`, specifications, or exhaustive acceptance criteria in this skill.
