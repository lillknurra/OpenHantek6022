# Project Rules

1. Preserve the GPL-3.0 license, upstream attribution, and repository history.
2. Keep `main` suitable for upstream synchronization. Development happens on patch or feature branches.
3. Separate verified facts, measurements, inferences, and hypotheses in all technical documents.
4. Do not claim mixed-signal operation until simultaneous analog and digital capture has been reproduced on physical hardware.
5. Establish an unmodified upstream baseline before changing runtime behavior.
6. Every hardware-facing change must include a test plan, expected result, observed result, and rollback path.
7. Experimental FX2 firmware must be RAM-loaded only until recovery has been verified.
8. Never test the instrument directly on mains-referenced circuitry. The USB grounds and BNC grounds are not isolated measurement inputs.
9. Prefer small, reviewable patches with one technical objective.
10. Update `docs/CURRENT_STATE.md`, `docs/AI_MEMORY.md`, and the relevant handoff document before ending a patch.
