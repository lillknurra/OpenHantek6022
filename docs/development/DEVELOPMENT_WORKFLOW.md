# Development Workflow

## Purpose

This document defines the complete patch lifecycle for the OpenHantek6022 MSO
research fork.

The workflow applies to documentation, infrastructure, runtime, USB, firmware,
hardware, and measurement work.

## Official patch phases

```text
IMPLEMENT -> VALIDATE -> PUBLISH -> LOCK -> COMPLETE
```

A patch may move backward when validation reveals a defect. It must not skip a
phase merely because the change appears small.

## Before IMPLEMENT

Read the canonical order in:

```text
docs/handoff/MASTER_INDEX.md
```

Then confirm:

```bash
git status -sb
git branch --show-current
git rev-parse HEAD
git remote -v
```

Record:

- patch title and number;
- narrow objective;
- non-goals;
- base branch and base commit;
- expected changed files;
- applicable design decisions;
- validation plan;
- rollback.

The worktree must be understood before edits begin.

## IMPLEMENT

- Make the smallest coherent change.
- Keep unrelated cleanup out of the patch.
- Preserve upstream-compatible behavior unless the patch explicitly changes it.
- Keep documentation, infrastructure, runtime, and firmware changes
  distinguishable.
- Prefer reproducible applicator scripts for large controlled document changes.
- Make applicators idempotent.
- Refuse to overwrite unexpected existing content without explicit review.
- Do not rewrite published history.
- Keep experiments reversible.

Every technical patch must list design decisions under one or more of:

```text
Implements:
Depends on:
Updates:
Supersedes:
```

When none apply, state that explicitly as required by
`docs/architecture/DESIGN_DECISIONS.md`.

## VALIDATE

Follow:

```text
docs/development/VALIDATION_WORKFLOW.md
```

Minimum repository checks:

```bash
git status -sb
git diff --stat
git diff --check
git diff --name-only
```

Validation must:

- match the claim being made;
- distinguish `PASS`, `FAIL`, `INCONCLUSIVE`, `NOT RUN`, and
  `NOT APPLICABLE`;
- capture relevant evidence;
- verify the intended file set;
- verify that prohibited runtime or firmware paths are unchanged when the patch
  is documentation-only.

A successful build is not runtime, USB, firmware, hardware, synchronization, or
measurement validation.

## PUBLISH

Before a commit:

1. define the commit message;
2. stage exact files explicitly;
3. inspect the staged file list;
4. run `git diff --cached --check`;
5. inspect `git diff --cached --stat`;
6. rerun the applicable validator against the staged work;
7. create one logical commit;
8. push only to the active patch branch.

Example:

```bash
git add -- path/one path/two
git diff --cached --name-status
git diff --cached --check
git diff --cached --stat
git commit -m "Patch NNN: concise action"
git push origin HEAD
```

Do not use blanket staging when exact files are known.

After push, verify the remote commit and confirm the local branch is synchronized
with origin.

## LOCK

Update the documents that own durable knowledge.

Normally review:

- `docs/handoff/CURRENT_STATE.md`;
- `docs/handoff/AI_MEMORY.md`;
- `docs/handoff/HANDOFF.md`;
- `docs/history/PATCH_HISTORY.md`;
- the current detailed patch record;
- `docs/architecture/DESIGN_DECISIONS.md` when policy changed;
- `docs/handoff/MASTER_INDEX.md` when ownership or reading order changed.

`LOCK` must record:

- what is verified;
- what is inferred;
- what remains unknown;
- exact published commit IDs;
- validation limitations;
- the next continuation point.

Chat history is not a substitute for repository-owned memory.

## COMPLETE

A patch is complete only when:

- its objective is met;
- applicable validation criteria passed;
- failures and limitations are recorded;
- rollback remains clear;
- durable documents are synchronized;
- the remote commit is verified;
- the user accepts the patch for review or merge.

Record the final state as one of:

```text
COMPLETE / UNMERGED
COMPLETE / MERGED
ABANDONED
```

A patch marked `COMPLETE / UNMERGED` may be opened as a draft pull request.

## Failure handling

When a check fails:

1. stop before commit or push;
2. preserve the failure output;
3. identify whether implementation or validator logic is wrong;
4. correct the smallest relevant component;
5. rerun the full applicable validation;
6. do not hide the original limitation in the patch record.

When a command ran in the wrong directory or branch, first verify repository
state before attempting cleanup.

## Rollback

Before publication:

```bash
git restore --staged -- path
git restore -- path
```

Use only after reviewing the affected files.

After publication, revert the relevant commit. Do not force-push or rewrite
published project history unless an explicitly approved recovery procedure
requires it.
