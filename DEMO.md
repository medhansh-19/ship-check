# Deliberately faulty target — recording notes

Event: Flip the Switch 2026, https://www.wemakedevs.org/hackathons/switch.
Dates and source quotations are real; no clock or deadline is changed.
The checklist is a saved Scout extraction, not a promise of eligibility.

## Expected initial failures

1. README setup references absent requirements.txt; the app only uses Python's
   standard library. A fresh-clone install command must fail.
2. The task summary counts all tasks as completed; the focused test must fail.
3. No SUBMISSION.md or video URL is provided. Do not invent a video.
4. No root LICENSE is present. This is general project hygiene, not a claimed
   mandatory requirement of this hackathon. Choose a license explicitly.
5. The README does not explain or provide a real Switch workflow for this target.
   Launch Ledger is only the sample being audited. Ship Check is the real entry.

## Audit prompt for Discord

@shipcheck-auditor Audit https://github.com/medhansh-19/ship-check branch
codex/demo-switch-faulty. This is the deliberately faulty Launch Ledger rehearsal
target, not the Ship Check entry. Use Scout's Flip the Switch checklist and its
source quotes. Fresh-clone this exact branch, execute README setup and tests,
capture exit codes and propose numbered fixes. Separate generic hygiene checks
from actual event requirements. Do not fabricate eligibility, Switch integration,
video evidence or a submission. Wait for my approval before changing files.

Expected repairs: correct setup docs and fix task counting. Submission content
stays a labelled draft until the human supplies real evidence. Never approve
personal eligibility or accept legal terms on the owner's behalf.

## Recording

Show the task list versus incorrect summary and the failing test. Ask Scout to
inspect the official Switch event URL. Show source quotes in the dashboard, ask
Auditor for fresh-clone evidence, review proposed changes, approve selected IDs,
then show the resulting PR. Merge only into this demo branch. Fetch the branch
into this demo checkout to trigger the dashboard recheck. Missing video and
human evidence must remain unresolved.
