# Branching Strategy

## Baselines

- `main` is the accepted fork baseline and must remain easy to synchronize with `OpenHantek/OpenHantek6022`.
- Development never starts by modifying `main` directly.

## Branch classes

- `project/patch-NNN-description`: governance, documentation, build baselines, integration, and other planned project work.
- `feature/short-description`: isolated generally useful product changes.
- `experiment/short-description`: hardware, USB, firmware, timing, or MSO experiments whose behavior is not yet proven.
- `hotfix/short-description`: narrowly scoped correction to an accepted baseline when urgency justifies it.

## Rules

1. One patch branch has one clear purpose.
2. Record the starting commit before implementation.
3. Do not mix upstream synchronization with project changes.
4. Do not force-push, rewrite published history, or rebase published branches.
5. Stage intended files explicitly.
6. Open a draft pull request while validation is incomplete.
7. Merge only after the documented acceptance criteria pass or the result is explicitly accepted as inconclusive.
8. Tags represent validated milestones only.

## Patch phases

```text
IMPLEMENT -> VALIDATE -> PUBLISH -> LOCK -> COMPLETE
```

A branch is not complete merely because its files have been committed. Documentation lock and handoff are part of completion.
