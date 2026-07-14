# GitHub Workflow

## Core rules

- Define the commit message before any GitHub write operation.
- Use one logical purpose per commit.
- Stage exact files and review staged changes.
- Do not rewrite published history.
- A stacked patch targets its actual accepted base branch.

## Start a patch branch

```bash
git fetch --all --prune
git switch BASE_BRANCH
git pull --ff-only origin BASE_BRANCH
git switch -c project/patch-NNN-description
git push -u origin project/patch-NNN-description
```

When the remote branch already exists:

```bash
git fetch origin
git switch --track origin/project/patch-NNN-description
```

## Pull requests with GitHub CLI

Create a draft pull request:

```bash
gh pr create --draft --base BASE_BRANCH --head HEAD_BRANCH   --title "Patch NNN: concise title" --body-file PR_BODY.md
```

Inspect and validate:

```bash
gh pr view PR_NUMBER
gh pr diff PR_NUMBER --name-only
gh pr checks PR_NUMBER
```

Mark ready:

```bash
gh pr ready PR_NUMBER
```

Merge with a merge commit and delete the remote patch branch:

```bash
gh pr merge PR_NUMBER --merge --delete-branch
```

Optional explicit merge metadata:

```bash
gh pr merge PR_NUMBER --merge --delete-branch   --subject "Merge PR #PR_NUMBER: Patch NNN concise title"   --body "Integrate the validated Patch NNN change."
```

## Post-merge synchronization

```bash
git fetch --prune
git switch BASE_BRANCH
git pull --ff-only origin BASE_BRANCH
git status -sb
git log -1 --oneline
```

Record the merge commit in patch history before deleting any remaining local
patch branch.

```bash
git branch -d HEAD_BRANCH
```

## Merge policy

Merge only when acceptance criteria and required checks pass, durable handoff
documents are locked, and no unresolved failure is represented as a pass.

## GitHub write safety

Before a remote write:

1. state the intended operation;
2. define the commit message when a commit is involved;
3. confirm repository and target branch;
4. avoid parallel writes to the same file or ref;
5. verify the result.

Read-only inspection does not create a commit.
