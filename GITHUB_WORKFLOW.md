# GitHub Workflow

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
