# Handoff

## Purpose

This document is the exact continuation point for the next OpenHantek6022
development session.

## Repository state

Repository:

```text
lillknurra/OpenHantek6022
```

Local path:

```text
~/GitHub/OpenHantek6022
```

Active branch:

```text
project/patch-003-project-standardization
```

Base branch:

```text
project/patch-002-macos-build-baseline
```

Accepted technical base commit:

```text
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```

## Current patch

```text
Patch 003 - Project standardization
```

Patch type:

```text
documentation and project infrastructure only
```

No OpenHantek runtime or firmware change is intended.

## Completed and published

### Commit A

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
Patch 003: add architecture documents
```

Result:

- `SYSTEM_ARCHITECTURE.md` present;
- `DESIGN_DECISIONS.md` present;
- `DD-001` through `DD-009` present;
- technical-patch traceability requirement present;
- architecture validator passed;
- no runtime or firmware files changed.

### Commit B

```text
f7fbfdca6635fc0a0990767ae527b82e3adc5842
Patch 003: add patch history
```

Result:

- `PATCH_HISTORY.md` present;
- `PATCH_003.md` present;
- design-decision references present;
- history validator passed;
- no runtime or firmware files changed.

## Current work

Commit C:

```text
Patch 003: synchronize handoff documents
```

Expected files:

```text
docs/handoff/MASTER_INDEX.md
docs/handoff/CURRENT_STATE.md
docs/handoff/AI_MEMORY.md
docs/handoff/HANDOFF.md
scripts/apply_patch_003_handoff_docs.py
scripts/validate_patch_003_handoff_docs.py
```

Design decisions:

```text
Implements:
DD-002
DD-003
DD-007
DD-008
DD-009
```

## Validation requirements for Commit C

- all four handoff documents exist;
- `MASTER_INDEX.md` defines the sole canonical reading order;
- internal paths referenced by `MASTER_INDEX.md` exist;
- `CURRENT_STATE.md` records Patch 002 evidence and Patch 003 status honestly;
- `AI_MEMORY.md` records durable method and design decisions;
- `HANDOFF.md` records exact continuation;
- no runtime or firmware files changed relative to Patch 002;
- `git diff --check` passes;
- only the six intended files are staged.

## Known limitations

The following are not verified:

- visible demo-mode operation;
- Hantek hardware operation;
- USB acquisition;
- firmware behavior;
- simultaneous analog and digital capture;
- synchronization;
- packaging;
- measurement correctness.

## Rollback

Before merge, discard the Patch 003 branch or revert individual commits.

After merge, revert the relevant commits. Do not rewrite published history.

## Next after Commit C

Add the canonical validation workflow and finish the development/Git workflow
documents. Then convert legacy duplicate files to compatibility pointers and
run final Patch 003 structural validation.

Do not begin runtime or hardware work until Patch 003 is accepted.
