# [Feature Name] · Modular Requirement Delivery Index

## Document set

| Item | Value |
|---|---|
| Purpose | |
| Audience | |
| Repository snapshot | Branch/commit or N/A |
| Scope | |
| Delivery profile | Modular |
| Primary document | [ux-requirements.md](ux-requirements.md) |
| Split rationale | Independent owner/review/release/readability reason |
| Version/status | Draft / Provisional / Confirmed |
| Readiness | |
| Baseline version/status | Awaiting confirmation |
| Last updated | |

## How to read this document set

1. Start with [ux-requirements.md](ux-requirements.md) for alignment, confirmed Stories, experience, ASCII UX, local specifications, risks, and review status.
2. Open a module file only when you own or review that independently governed module.
3. Open control or evidence files only when you need their dense implementation, trace, or source detail.

## Document map

| File | Purpose | Status | Notes | Main IDs |
| --- | --- | --- | --- | --- |
| [ux-requirements.md](ux-requirements.md) | Canonical reader-first alignment, Stories, experience, confirmed ASCII, local specifications, acceptance, key risks, and Review | In progress | Primary reading entry | All applicable IDs |
| [modules/example-module.md](modules/example-module.md) | Independently owned/reviewed module | Planned / N/A | Replace with a real module or delete this row | PAGE, FUNC, SUB, UI, SPEC, AC |
| [control-appendix.md](control-appendix.md) | Dense shared permissions, lifecycle, data, contracts, NFR, full trace, and detailed decisions | Planned / N/A | Omit when main-document appendices remain readable | SYS, SPEC, STATE, NFR, DEC |
| [evidence-and-research.md](evidence-and-research.md) | Substantial repository evidence, drift, public research, comparisons, and source ledger | Planned / N/A | Omit when a concise main summary is sufficient | SRC, DRIFT, CST |

Delete every unused example/planned row instead of creating an empty file. If fewer than four files remain, remove `index.md` and use `ux-requirements.md` as the entry point.

## Module and ASCII UX progress

Keep the detailed confirmation queue in `ux-requirements.md`. Mirror only enough status here for navigation; do not duplicate frames, specifications, decisions, or acceptance criteria.

| Module or scope | Current outcome | Status | Next action | Location |
|---|---|---|---|---|
| Primary baseline and shared experience | | In progress | Confirm baseline or next ASCII unit | [ux-requirements.md](ux-requirements.md) |
| [Independent module] | | Planned / In review / Confirmed / Blocked | | [module file](modules/example-module.md) |

## Review status

The canonical `Review and delivery summary`, coverage details, limitations, and full delivered tree belong in [ux-requirements.md](ux-requirements.md). This index mirrors only the current result.

| Item | Current result | Location or next action |
|---|---|---|
| Delivery status | Complete / Complete with known limitations / Provisional / Blocked | [Review summary](ux-requirements.md) |
| Baseline | | [Confirmed baseline](ux-requirements.md) |
| ASCII UX confirmation | | [Confirmation queue](ux-requirements.md) |
| Blocking decision | None / summary | Owner and next action |
| Last reviewed | | |
