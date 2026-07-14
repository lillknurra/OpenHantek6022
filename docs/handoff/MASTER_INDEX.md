# Master Index

## Authority

This file is the sole canonical reading order for the OpenHantek6022 MSO
research fork.

Legacy top-level documents may remain temporarily for compatibility, but they
must not define a competing reading order. When legacy documents are converted
to pointers, this file remains authoritative.

## Required reading order

1. `../../AGENTS.md`
2. `../../PROJECT_INSTRUCTIONS.md`
3. `../development/DEVELOPMENT_WORKFLOW.md`
4. `CURRENT_STATE.md`
5. `AI_MEMORY.md`
6. `../history/PATCH_003.md`
7. `../architecture/SYSTEM_ARCHITECTURE.md`
8. `../architecture/DESIGN_DECISIONS.md`
9. `../build/MACOS_BUILD_BASELINE.md`
10. `../HARDWARE_BASELINE.md`
11. `../USB_ARCHITECTURE.md`
12. `../MSO_HYPOTHESES.md`
13. `../TEST_PLAN.md`
14. `HANDOFF.md`

## Document ownership

| Document | Ownership |
|---|---|
| `../../AGENTS.md` | Agent behavior, safety rules, and execution discipline |
| `../../PROJECT_INSTRUCTIONS.md` | Project purpose, scope, and patch requirements |
| `../development/DEVELOPMENT_WORKFLOW.md` | Complete patch lifecycle |
| `CURRENT_STATE.md` | Current accepted baseline, active branch, and next work |
| `AI_MEMORY.md` | Durable context and permanent lessons |
| `../history/PATCH_HISTORY.md` | Chronological patch record |
| `../history/PATCH_003.md` | Detailed current patch record |
| `../architecture/SYSTEM_ARCHITECTURE.md` | System boundaries and layer ownership |
| `../architecture/DESIGN_DECISIONS.md` | Accepted design decisions and rationale |
| `HANDOFF.md` | Exact continuation point for the next session |

## Reading rules

- Read in order unless the task is a narrowly scoped inspection.
- Confirm the active branch and baseline before proposing changes.
- Treat `Verified`, `Inferred`, and `Unknown` as distinct evidence classes.
- Do not infer runtime or hardware correctness from documentation or build
  success.
- Every technical patch must reference applicable design decisions.
- Update this index only when document ownership or reading order changes.

## Current patch

Patch 003 standardizes project architecture, history, handoff, validation, and
development workflow without changing OpenHantek runtime or firmware behavior.

Current branch:

```text
project/patch-003-project-standardization
```

Accepted technical base:

```text
project/patch-002-macos-build-baseline
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```
