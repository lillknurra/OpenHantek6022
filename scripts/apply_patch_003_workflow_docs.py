#!/usr/bin/env python3
"""Patch 003 Commit D - apply validation and development workflow docs."""

from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "project/patch-003-project-standardization"

OLD_BLOB_SHAS = {
    "docs/development/DEVELOPMENT_WORKFLOW.md": "9dc345af78c4eea55e2ceda9dd439432cd814adc",
    "GITHUB_WORKFLOW.md": "70dd82c933a80b3d7709ad40bc2c1d4ab333a1a5",
}

FILES = {
    ROOT / "docs/development/VALIDATION_WORKFLOW.md": (None, r"""# Validation Workflow

## Purpose

This document defines how OpenHantek6022 patches are validated and how evidence
may be described.

Validation must match the type of claim being made. Passing one evidence class
does not imply that another class passed.

## Evidence classes

### Documentation

Examples:

- required files and headings exist;
- internal references resolve;
- stated branch and commit identities are correct;
- `git diff --check` passes.

Documentation validation does not prove build, runtime, USB, firmware, hardware,
synchronization, packaging, or measurement behavior.

### Static and source inspection

Examples:

- source paths and symbols exist;
- call paths and ownership boundaries are understood;
- generated diffs match the patch plan;
- no prohibited files changed.

Static inspection does not prove compilation or runtime behavior.

### Build

Examples:

- configuration succeeds;
- compilation completes;
- expected binaries or bundles are produced;
- warnings are recorded.

A successful build proves only the tested build configuration.

### Runtime

Examples:

- the application launches visibly;
- the intended mode is selected;
- expected UI behavior is observed;
- logs show the expected runtime path.

A command returning without an error is not sufficient evidence of visible
runtime behavior.

### USB and firmware

Examples:

- devices enumerate with recorded identifiers;
- endpoints and interfaces are captured;
- firmware loading is observed;
- transfers are sustained for a defined duration;
- recovery is demonstrated.

Enumeration alone does not prove usable acquisition.

### Physical hardware

Examples:

- PCB revision is identified from the purchased unit;
- measured voltages and signals are recorded;
- analog and digital functions are tested separately;
- concurrent operation is tested.

External schematics and forum material remain references until confirmed on the
physical unit.

### Synchronization and measurement

Examples:

- common stimulus and acquisition conditions are documented;
- offset, jitter, and drift are measured;
- sample counts and timing windows are recorded;
- accuracy is compared with an appropriate reference.

Concurrent streams do not by themselves prove synchronization.

## Required validation plan

Before implementation, every patch records:

1. objective;
2. non-goals;
3. base branch and base commit;
4. expected changed files;
5. applicable design decisions;
6. required evidence classes;
7. commands or procedures;
8. pass criteria;
9. failure and inconclusive criteria;
10. rollback.

Use `Not applicable` rather than silently omitting an evidence class.

## Result vocabulary

- `PASS`: stated criteria passed with recorded evidence.
- `FAIL`: stated criteria failed.
- `INCONCLUSIVE`: evidence is insufficient or ambiguous.
- `NOT RUN`: planned validation was not executed.
- `NOT APPLICABLE`: the class does not apply to the patch.

Never convert `INCONCLUSIVE` or `NOT RUN` into `PASS`.

## Validation order

Run the cheapest relevant checks first:

1. repository and branch sanity;
2. intended-file check;
3. static and structural checks;
4. whitespace and formatting checks;
5. build;
6. runtime;
7. USB and firmware;
8. physical hardware;
9. synchronization and measurement.

Stop when a failed prerequisite makes later claims invalid, but record what was
not run.

## Documentation-only patch minimum

A documentation-only patch must verify:

```bash
git status -sb
git diff --check
git diff --stat
git diff --name-only
```

It must also verify:

- required files and markers;
- internal paths where practical;
- exact staged-file set;
- no runtime or firmware files changed relative to the patch base.

## Technical patch minimum

A technical patch must additionally record:

- build command and result;
- runtime test or explicit reason it was not run;
- design-decision references;
- affected hardware or firmware assumptions;
- rollback or recovery procedure.

Hardware-dependent claims remain `INCONCLUSIVE` or `NOT RUN` until the required
device evidence exists.

## Evidence capture

Store durable evidence in the repository when appropriate:

- commands and concise outputs in patch records;
- long logs in a dedicated evidence directory;
- screenshots only when visual behavior matters;
- measurements with equipment, setup, units, and uncertainty;
- hashes or commit IDs for baselines and generated artifacts.

Do not paste uncontrolled terminal output into canonical state documents.

## Validator requirements

Repository-local validators should:

- be deterministic;
- return non-zero on failure;
- print a short final PASS or FAIL summary;
- distinguish missing files from incorrect content;
- check current worktree changes as well as committed branch changes;
- avoid modifying the repository;
- avoid treating ignored build output as a patch change.

A validator passing proves only the checks implemented by that validator.

## Completion rule

A patch cannot be marked complete until:

- applicable criteria are recorded;
- validation results use the approved vocabulary;
- failures and limitations remain visible;
- durable documents are updated during `LOCK`;
- staged files match the commit plan;
- the published commit is verified after push.
"""),
    ROOT / "docs/development/DEVELOPMENT_WORKFLOW.md": (r"""# Development Workflow

## Official patch phases

```text
IMPLEMENT -> VALIDATE -> PUBLISH -> LOCK -> COMPLETE
```

### IMPLEMENT
- Define one narrow objective.
- List expected changed files.
- Avoid unrelated cleanup.
- Preserve runtime behavior unless the patch explicitly changes it.

### VALIDATE
- Run the checks relevant to the patch.
- Capture commands, logs, screenshots, measurements, or explicit user confirmation.
- A successful build validates only the build, not hardware behavior or mixed-signal operation.

### PUBLISH
- Inspect the working tree.
- Stage intended files explicitly.
- Commit one logical change at a time.
- Push to the active patch branch.

### LOCK
- Update the documents that own the new durable knowledge.
- Normally update `CURRENT_STATE.md`, `AI_MEMORY.md`, `PATCH_HISTORY.md`, and the current handoff.

### COMPLETE
- Record result as
""", r"""# Development Workflow

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
"""),
    ROOT / "GITHUB_WORKFLOW.md": (r"""# GitHub Workflow

## Remotes
- `origin`: `lillknurra/OpenHantek6022`
- `upstream`: `OpenHantek/OpenHantek6022`

## Branch policy
- `main` tracks the fork's accepted baseline and must remain easy to synchronize with upstream.
- Patch branches use `project/patch-NNN-description`.
- Feature branches use `feature/short-description`.
- Hardware experiments use `experiment/short-description` until reproducible.

## Patch sequence
1. Read `AGENTS.md`, `PROJECT_INSTRUCTIONS.md`, `docs/MASTER_INDEX.md`, and `docs/CURRENT_STATE.md`.
2. Define one objective and acceptance criteria.
3. Record the baseline commit before editing.
4. Make the smallest coherent change.
5. Run applicable build, static, demo-mode, and hardware tests.
6. Update state, memory, and handoff documentation.
7. Open a draft pull request to `main`.
8. Merge only after the documented acceptance criteria pass.

## Upstream synchronization
```bash
git remote add upstream https://github.com/OpenHantek/OpenHantek6022.git
git fetch upstream
git checkout main
git merge --ff-only upstream/main
git push origin main
```

Do not mix upstream synchronization with experimental functional changes in the same patch.
""", r"""# GitHub Workflow

## Purpose

This document defines repository, branch, commit, push, pull-request, merge, and
upstream synchronization rules for `lillknurra/OpenHantek6022`.

## Remotes

- `origin`: `lillknurra/OpenHantek6022`
- `upstream`: `OpenHantek/OpenHantek6022`

Verify before work:

```bash
git remote -v
```

## Branch roles

- `main`: accepted fork baseline; keep easy to compare and synchronize with
  upstream.
- `project/patch-NNN-description`: numbered project patch.
- `feature/short-description`: scoped software feature when a numbered patch
  record is not required.
- `experiment/short-description`: reversible investigation that is not yet an
  accepted baseline.
- `hotfix/short-description`: urgent narrow correction to an accepted baseline.

Patch 003 uses:

```text
project/patch-003-project-standardization
```

and targets:

```text
project/patch-002-macos-build-baseline
```

A stacked patch must target its actual accepted base branch, not automatically
`main`.

## Start a patch branch

```bash
git fetch --all --prune
git switch BASE_BRANCH
git pull --ff-only origin BASE_BRANCH
git switch -c project/patch-NNN-description
git push -u origin project/patch-NNN-description
```

Record the exact base commit before editing:

```bash
git rev-parse HEAD
```

## Commit policy

- Define the commit message before any GitHub write operation.
- Use one logical purpose per commit.
- Stage exact paths.
- Review staged changes before committing.
- Do not include build output, secrets, unrelated cleanup, or local machine
  artifacts.
- Do not rewrite published history.
- Use imperative commit messages.

Recommended form:

```text
Patch NNN: concise action
```

Required pre-commit checks:

```bash
git diff --cached --name-status
git diff --cached --check
git diff --cached --stat
```

## Push policy

Push only after local validation passes:

```bash
git push origin HEAD
```

Then confirm:

```bash
git status -sb
git log -1 --oneline
```

The branch should be synchronized with its upstream tracking branch.

## Pull requests

Open a draft pull request when the patch is structurally ready for review but
not yet accepted.

The pull request must state:

- base and head branches;
- objective and non-goals;
- changed-file categories;
- design decisions;
- validation evidence;
- known failures and limitations;
- rollback;
- exact next work.

For stacked patches, choose the immediate patch base. Patch 003 therefore
targets `project/patch-002-macos-build-baseline`.

Mark ready for review only when completion criteria are met.

## Merge policy

Merge only when:

- documented acceptance criteria pass;
- requested review is complete;
- required checks pass;
- branch scope matches the patch record;
- durable handoff documents are locked;
- no unresolved failure is represented as a pass.

Use the repository's approved merge strategy. Record the resulting merge commit
or squash commit in patch history.

Delete a merged patch branch only after the merge identity and rollback path are
recorded.

## Upstream synchronization

Do upstream synchronization in a dedicated patch or maintenance operation.

```bash
git fetch upstream
git switch main
git pull --ff-only origin main
git merge --ff-only upstream/main
git push origin main
```

When fast-forward is impossible, stop and review divergence. Do not substitute
an unreviewed merge or rebase.

Do not mix upstream synchronization with experimental runtime or hardware work.

## GitHub write safety

Before creating or changing a remote branch, commit, pull request, issue, label,
review, or merge:

1. state the intended operation;
2. define the commit message when a commit is involved;
3. confirm repository and target branch;
4. avoid parallel writes to the same file or ref;
5. verify the result after the write.

Read-only GitHub inspection does not create a commit.
"""),
}


def git_output(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=True
    ).stdout.strip()


def apply(path: Path, old: str | None, new: str) -> None:
    desired = new.rstrip() + "\n"
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if existing == desired:
            print(f"PASS: {path.relative_to(ROOT)} already synchronized")
            return
        if old is None:
            raise SystemExit(
                f"ERROR: {path.relative_to(ROOT)} unexpectedly exists with different content"
            )
        expected_old = old.rstrip() + "\n"
        if existing != expected_old:
            relative = str(path.relative_to(ROOT))
            expected_sha = OLD_BLOB_SHAS.get(relative)

            actual_sha = subprocess.run(
                ["git", "hash-object", relative],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=True,
            ).stdout.strip()

            if expected_sha is None or actual_sha != expected_sha:
                raise SystemExit(
                    f"ERROR: {relative} has unexpected content "
                    f"(blob={actual_sha}, expected={expected_sha})"
                )

            print(
                f"PASS: {relative} matches expected GitHub baseline "
                f"blob={actual_sha}"
            )

        path.write_text(desired, encoding="utf-8")
        print(f"PASS: updated {path.relative_to(ROOT)}")
        return

    if old is not None:
        raise SystemExit(f"ERROR: expected existing file missing: {path.relative_to(ROOT)}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(desired, encoding="utf-8")
    print(f"PASS: created {path.relative_to(ROOT)}")


def main() -> None:
    if not (ROOT / ".git").exists():
        raise SystemExit(f"ERROR: not a Git repository: {ROOT}")
    branch = git_output("branch", "--show-current")
    if branch != BRANCH:
        raise SystemExit(f"ERROR: expected branch {BRANCH}, current={branch}")

    for required in (
        "docs/handoff/MASTER_INDEX.md",
        "docs/architecture/DESIGN_DECISIONS.md",
        "docs/history/PATCH_003.md",
    ):
        if not (ROOT / required).is_file():
            raise SystemExit(f"ERROR: required file missing: {required}")

    for path, (old, new) in FILES.items():
        apply(path, old, new)

    print("PASS: Patch 003 Commit D workflow apply complete")


if __name__ == "__main__":
    main()
