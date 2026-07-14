# Development Workflow

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