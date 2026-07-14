# Patch 004 - Post-Merge State Lock and GitHub CLI Workflow

## Identity

- Branch: `project/patch-004-post-merge-state-lock`
- Base: `project/patch-002-macos-build-baseline`
- Base commit: `1ce5d559dce0e7d1f4fcd0c69f9fe1744cee10b8`
- Status: IN PROGRESS / UNMERGED
- Type: documentation and workflow

## Purpose

Lock the actual post-merge state of Patch 003 and standardize GitHub CLI
commands for readying, merging, deleting the remote branch, and synchronizing
the local base branch.

## Design decisions

**Implements:** `DD-002`, `DD-003`, `DD-007`, `DD-008`, `DD-009`

## Merge evidence

```text
PR #2
Merge commit: 1ce5d559dce0e7d1f4fcd0c69f9fe1744cee10b8
```

## GitHub CLI workflow

```bash
gh pr ready PR_NUMBER
gh pr merge PR_NUMBER --merge --delete-branch
```

## Non-goals

No runtime, USB, firmware, hardware, synchronization, packaging, or measurement
change or validation.

## Next patch

```text
Patch 005 - visible demo-mode runtime baseline
```
