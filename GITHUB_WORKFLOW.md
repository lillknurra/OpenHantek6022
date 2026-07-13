# GitHub Workflow

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
