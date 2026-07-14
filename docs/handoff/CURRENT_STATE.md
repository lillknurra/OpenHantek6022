# Current State

Last updated: 2026-07-14

## Repository

- Fork: `lillknurra/OpenHantek6022`
- Local repository: `~/GitHub/OpenHantek6022`
- Active branch: `project/patch-004-post-merge-state-lock`
- Base branch: `project/patch-002-macos-build-baseline`
- Base commit: `1ce5d559dce0e7d1f4fcd0c69f9fe1744cee10b8`

## Patch 003 status

**Status:** COMPLETE / MERGED.

```text
PR #2
Merge commit: 1ce5d559dce0e7d1f4fcd0c69f9fe1744cee10b8
```

Patch 003 standardized architecture, decisions, history, handoff, validation,
development, release, branching, and GitHub workflow without runtime or
firmware changes.

## Patch 004 status

**Status:** IN PROGRESS / UNMERGED.

```text
project/patch-004-post-merge-state-lock
Patch 004: lock merged state and add GitHub CLI workflow
```

Purpose:

- lock the merged Patch 003 state;
- record PR #2 and its merge commit;
- add the standard GitHub CLI ready/merge/delete-branch workflow;
- identify Patch 005 as the next technical patch.

## Verified

- PR #2 is merged.
- The local base branch was updated to the merge commit.
- GitHub CLI is available locally.
- Patch 003 introduced no intended runtime or firmware changes.

## Unknown or unverified

- visible demo-mode operation;
- physical Hantek operation;
- USB topology and acquisition;
- concurrent analog and digital operation;
- synchronization and measurement correctness.

## Immediate next work

Complete and merge Patch 004. Then begin:

```text
Patch 005 - visible demo-mode runtime baseline
```
