# Command and Terminal Output Guidance

## Immediate-command rule
Whenever the assistant states a next step, include the exact copy/paste command in the same response.

## Command blocks
- Start from the repository root when repository context matters.
- Use one complete shell block per logical action.
- Do not include shell prompt characters.
- Prefer readable multi-line commands.
- Avoid partial heredocs, unmatched quotes, and incomplete pipelines.
- Use only standard ASCII command flags.

## Output headings
Use fixed `printf` headings for long workflows:

```bash
printf '\n=== BUILD ===\n'
cmake --build build

printf '\n=== RESULT ===\n'
git status -sb
```

Headings improve readability but do not prove PASS or FAIL.

## Exit codes and logs
For validation where failure output must remain visible