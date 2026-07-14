# AI Memory

## Accepted merged baseline

Patch 003 is complete and merged through PR #2.

```text
Merge commit:
1ce5d559dce0e7d1f4fcd0c69f9fe1744cee10b8
```

Accepted base branch:

```text
project/patch-002-macos-build-baseline
```

## GitHub CLI standard

```bash
gh pr ready PR_NUMBER
gh pr merge PR_NUMBER --merge --delete-branch
```

Post-merge:

```bash
git fetch --prune
git switch BASE_BRANCH
git pull --ff-only origin BASE_BRANCH
```

Record the merge commit in patch history.

## Durable method

- Define the commit message before a GitHub write.
- Use one narrow patch purpose.
- Stage exact files.
- Use deterministic applicators and validators.
- Build success is not visible runtime validation.
- Do not rewrite published history.
- Keep experiments reversible.

## Design decisions

Patch 004 implements `DD-002`, `DD-003`, `DD-007`, `DD-008`, and `DD-009`.

## Immediate continuation

Finish Patch 004, then run Patch 005 to establish a visible demo-mode runtime
baseline without physical hardware.
