# Release Process

## Purpose

This fork does not create releases from unvalidated experiments. Releases and tags represent accepted, reproducible milestones.

## Preconditions

A release candidate requires:

- an accepted patch baseline;
- documented validation evidence;
- updated `CURRENT_STATE.md`, `AI_MEMORY.md`, `PATCH_HISTORY.md`, and handoff documentation;
- no unrelated working-tree changes;
- an explicit user decision to publish a release or tag.

## Process

1. Confirm the accepted commit and branch.
2. Review the complete diff against the previous accepted baseline.
3. Re-run the validation required by the milestone.
4. Record known limitations and unresolved hypotheses.
5. Merge the accepted patch through the documented GitHub workflow.
6. Create a tag only when explicitly approved.
7. Publish release notes that distinguish verified behavior, inferred architecture, and unknowns.

## Tagging rules

- Do not tag documentation drafts, incomplete experiments, or merely successful builds.
- Do not reuse or move published tags.
- Prefer descriptive milestone tags over speculative product claims.
- A mixed-signal or synchronization tag is forbidden until physical measurements support it.

## Rollback

Rollback means returning to the preceding accepted commit or tag. Published history is not rewritten.