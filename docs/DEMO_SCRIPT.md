# Demo walkthrough — approximately 3 minutes

## V2 opening — add 45 seconds

Open http://127.0.0.1:8787. Show real blockers, source-labelled deadline and
evidence beside each check. Click Run audit, then show the Discord report and
owner controls. In a disposable broken checkout, review an exact proposed fix,
reject one and approve another. Change a file and show the automatic recheck
resetting approval. Use the existing V1 PR for the live GitHub result; V2's
new PR path has isolated integration-test evidence, not a live rehearsal yet.

## Agent workflow

1. **Problem (20 seconds):** Show Ship Check's README. Explain that teams can
   finish a product while leaving setup broken or missing a submission rule.
2. **Discord room (35 seconds):** Open the Ship Check Demo server and
   `#ship-check-demo`. Show Scout and Auditor posting under their own names.
   Explain that Switch created the channel and coordinates both agents.
3. **Evidence (45 seconds):** Show the saved synthetic audit: literal setup
   failed, a clean-venv diagnostic found missing requirements, and direct app
   execution succeeded. Show numbered fixes and the missing-video deferral.
4. **Human decision (30 seconds):** Show the owner's approval of 1, 2 and 4 with
   MIT in the room. Explain that only auditor has a one-repository GitHub grant.
5. **Reviewable result (35 seconds):** Open PR #1. Show the three approved files,
   corrected command output and merged demo branch. Main project stays intact.
6. **Reuse and limits (15 seconds):** Show Switch Console and the standalone
   room YAML. Mention
   instruction-based approval and temporary local HTTPS. End with the real
   outcome: evidence-backed fixes, reviewed by a human.

This is a replay of a completed rehearsal. The demo branch is now repaired;
for a fresh failing run use a new branch at the original SHA documented in
examples/README.md. Record real UI and results. Do not claim a pending video,
public repository, eligibility decision or submission is already complete.
