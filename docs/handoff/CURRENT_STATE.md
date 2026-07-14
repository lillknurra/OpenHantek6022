# Current State

Last updated: 2026-07-14

## Repository

- Fork: `lillknurra/OpenHantek6022`
- Local repository: `~/GitHub/OpenHantek6022`
- Active branch: `project/patch-005-demo-runtime-baseline`
- Base branch: `project/patch-002-macos-build-baseline`
- Base commit: `bd6d86b5f21bb07efc6c06b7432dde36d1214b34`

## Patch 004 status

**Status:** COMPLETE / MERGED through PR #3.

## Patch 005 status

**Status:** VALIDATED LOCALLY / UNMERGED.

```text
Runtime result: PASS
Reason: User visually confirmed visible, updating, responsive demo mode
```

## Verified

- Apple Silicon macOS build and application bundle creation from Patch 002.
- Patch 003 and Patch 004 are merged.
- Patch 005 process survived startup and produced durable evidence.
- Visible demo-mode result is exactly `PASS`.

## Unknown or unverified

- physical Hantek enumeration and acquisition;
- exact hardware revision and USB topology;
- concurrent analog and digital acquisition;
- synchronization;
- packaging and measurement correctness.

## Immediate next work

Review and merge Patch 005. Then begin Patch 006 - USB enumeration baseline.
