---
name: shape-happy-paths
description: Derive and challenge primary successful user paths from a confirmed or explicitly provisional requirement/story baseline. Use for first-principles happy-path analysis, adversarial review, branch inventory, and DEC-HAPPY confirmation. Do not design pages, controls, detailed ASCII UI, or final specifications.
---

# Shape Happy Paths

Turn each material primary scenario into the shortest complete, safe, comprehensible path to an observable user outcome.

## Read first

Read [references/happy-path-shaping.md](references/happy-path-shaping.md) before deriving or reviewing a path.

## Input gate

Require a confirmed requirement/story baseline containing the actor, primary scenario, trigger, intended outcome, relevant rules, permissions, lifecycle, and evidence status. If the baseline is provisional, label every path provisional and do not allow downstream page/UI derivation.

## Workflow

1. Identify one material path per primary scenario or materially different primary role.
2. Derive `FLOW-HP-###` from the user outcome and irreducible constraints, not from current screens.
3. Apply the removal test to every step and separate avoidable interface choices.
4. Run the adversarial review for hidden roles, permissions, data, setup, waits, handoffs, lifecycle conditions, and false completion signals.
5. Revise, block, or create linked alternate/failure/exit/recovery intents based on the findings.
6. Present each path with its evidence, compact ASCII sequence, step table, basis, challenges, and branches.
7. Offer `修改当前 Happy Path` or `确认 Happy Path 并进入「ASCII 交互设计」`.
8. Record `DEC-HAPPY-###` for confirmed paths, including owner/date/conditions and covered `SCN/REQ/TASK/US/JS` IDs.

## Output contract

Every `FLOW-HP` defines actor, trigger, normal context, preconditions, entry, essential steps, required system work, user-visible feedback, resulting state, observable completion evidence, evidence status, adversarial findings, and linked branches.

When no trustworthy path can be produced, record Happy Path coverage as Blocked with the missing decision/evidence and owner. Use Not applicable only when no meaningful primary-user success sequence exists, with rationale.

Stop after the confirmation handoff. Do not derive canonical `FUNC`, `IA`, `PAGE`, detailed `INT`, `UI/STATE`, `SPEC`, or exhaustive `AC` unless the user invokes the downstream skill.
