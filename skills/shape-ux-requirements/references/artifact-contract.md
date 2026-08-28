# Cross-skill artifact contract

Use this contract whenever work moves between two or more Shape UX Requirements skills.

## Canonical stages

| Stage | Required input | Canonical output | Confirmation |
| --- | --- | --- | --- |
| Requirement baseline | User input plus available repository/source evidence | Evidence ledger, current/requested delta, problem, objectives, users, scenarios, concepts, scope, `REQ`, `TASK`, `US/JS` | `DEC-BASELINE` |
| Happy paths | Confirmed or explicitly provisional baseline | One reviewed `FLOW-HP` per material primary scenario, linked branch intents | `DEC-HAPPY` |
| ASCII interactions | Confirmed baseline and material `FLOW-HP` | `FUNC`, `IA`, `NAV`, task/decision `FLOW`, `INT`, `UI`, `STATE`, UX hypotheses | `DEC-ASCII` |
| Delivery | All planned upstream artifacts and confirmation records | `SPEC`, `SYS`, `AC`, `NFR`, traceability, review record, final files | Delivery status |

If an input gate is not satisfied, stop or continue only as an explicitly provisional artifact that lists the missing decision and affected downstream work.

## Stable IDs

Use these prefixes consistently: `SRC`, `STMT`, `BG`, `OBJ`, `AUD`, `SCN`, `ROLE`, `CON`, `UXH`, `REQ`, `Q`, `US`, `JS`, `TASK`, `FLOW`, `FUNC`, `IA`, `NAV`, `PAGE`, `SUB`, `INT`, `UI`, `STATE`, `SPEC`, `SYS`, `AC`, `NFR`, `DRIFT`, `DEC`, `CHG`, `CFLT`, and `CST`.

Specialized decisions use the `DEC` prefix with a semantic segment:

- `DEC-BASELINE-###`: requirement/story baseline confirmation;
- `DEC-HAPPY-###`: detailed happy-path confirmation;
- `DEC-ASCII-###`: ASCII interaction confirmation.

An ID has one canonical definition. Other documents reference it instead of copying an independently editable definition.

## Handoff record

Every stage handoff must state:

1. artifact status: Confirmed, Confirmed with conditions, Provisional, Blocked, Not applicable, or Superseded;
2. source snapshot or evidence boundary;
3. canonical artifact locations and IDs;
4. decisions and owners;
5. unresolved questions and affected downstream IDs;
6. permitted assumptions;
7. the next stage and what it may derive.

## Change control

When a confirmed upstream artifact changes, add `CHG-###`, name the affected IDs, mark dependent confirmations stale when material, and reconfirm only the affected slice. Do not silently preserve a downstream artifact whose actor, outcome, permission, lifecycle, irreducible constraint, or completion signal is no longer valid.
