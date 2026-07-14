#!/usr/bin/env bash

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root" || return 1 2>/dev/null || exit 1

expected_branch='project/patch-003-project-standardization'

printf '\n=== PATCH 003 BRANCH ===\n'
branch="$(git branch --show-current)"
branch_rc=0
if [ "$branch" = "$expected_branch" ]; then
  printf 'PASS: branch=%s\n' "$branch"
else
  printf 'FAIL: expected branch=%s current=%s\n' "$expected_branch" "$branch"
  branch_rc=1
fi

printf '\n=== PATCH 003 DOCUMENT PRESENCE ===\n'
presence=0
for path in \
  docs/architecture/SYSTEM_ARCHITECTURE.md \
  docs/architecture/DESIGN_DECISIONS.md; do
  if [ -f "$path" ]; then
    printf 'PASS: %s exists\n' "$path"
  else
    printf 'FAIL: %s missing\n' "$path"
    presence=1
  fi
done

printf '\n=== PATCH 003 REQUIRED MARKERS ===\n'
markers=0
check_marker() {
  file="$1"
  marker="$2"
  if grep -Fq -- "$marker" "$file"; then
    printf 'PASS: %s contains %s\n' "$file" "$marker"
  else
    printf 'FAIL: %s missing %s\n' "$file" "$marker"
    markers=1
  fi
}

check_marker docs/architecture/SYSTEM_ARCHITECTURE.md '# System Architecture'
check_marker docs/architecture/SYSTEM_ARCHITECTURE.md '## Dependency direction'
check_marker docs/architecture/DESIGN_DECISIONS.md '# Design Decisions'
check_marker docs/architecture/DESIGN_DECISIONS.md '## Patch traceability requirement'
check_marker docs/architecture/DESIGN_DECISIONS.md '## DD-009 - Technical patches must reference design decisions'

for id in DD-001 DD-002 DD-003 DD-004 DD-005 DD-006 DD-007 DD-008 DD-009; do
  check_marker docs/architecture/DESIGN_DECISIONS.md "$id"
done

printf '\n=== PATCH 003 RUNTIME FILE CHECK ===\n'
runtime=0
changed="$(git diff --name-only project/patch-002-macos-build-baseline...HEAD 2>/dev/null)"
if printf '%s\n' "$changed" | grep -Eq '^(openhantek/|libOpenHantek2xxx/|firmware/|CMakeLists\.txt$)' ; then
  printf 'FAIL: runtime/build-system file changed in Patch 003 comparison\n'
  printf '%s\n' "$changed"
  runtime=1
else
  printf 'PASS: no OpenHantek runtime or firmware files changed\n'
fi

printf '\n=== PATCH 003 WHITESPACE CHECK ===\n'
git diff --check
diff_rc=$?

printf '\n=== PATCH 003 VALIDATION SUMMARY ===\n'
printf 'branch=%d presence=%d markers=%d runtime=%d diff=%d\n' \
  "$branch_rc" "$presence" "$markers" "$runtime" "$diff_rc"

if [ "$branch_rc" -eq 0 ] && \
   [ "$presence" -eq 0 ] && \
   [ "$markers" -eq 0 ] && \
   [ "$runtime" -eq 0 ] && \
   [ "$diff_rc" -eq 0 ]; then
  printf 'PASS: Patch 003 architecture documentation validator complete\n'
  exit 0
fi

printf 'FAIL: Patch 003 architecture documentation validator failed\n'
exit 1
