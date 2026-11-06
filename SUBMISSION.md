# Ship Check — submission draft

Ship Check helps hackathon teams catch broken setup instructions and missed
submission requirements before the deadline. Two agents collaborate in a Switch
room: scout quotes rules and converts deadlines; auditor tests a fresh clone,
reports real failures, and opens a scoped PR for explicitly approved fixes.

- Repository: https://github.com/medhansh-19/ship-check (currently private).
- License: MIT.
- Demo video: pending recording and upload; no playable URL supplied yet.
- Reusable room: [Switch YAML](switch/ship-check.template.yaml).
- Setup: [README](README.md), [verified local environment](switch/LOCAL_SETUP.md).
- Evidence: [live audit receipt](examples/audit-evidence/README.md).
- Discord: [verified bridge and channel](docs/DISCORD_SETUP.md).

## What worked

The room completed checklist handoff, a fresh-clone audit, human approval and a
GitHub App PR limited to one repository. The owner selected fixes 1, 2 and 4,
including MIT licensing, and deferred the missing-video fix. Only README,
LICENSE and SUBMISSION.md changed. Corrected setup printed `Ready to ship.`
[PR #1](https://github.com/medhansh-19/ship-check/pull/1) was separately approved
and merged into the isolated demo branch, preserving the main project.

Switch supplies the shared checklist, evidence and decision history; the helper
scripts alone cannot provide the team handoff or scoped agent connection.
The same workflow now runs in a real Discord server. Switch created the
`#ship-check-demo` channel, attached Scout and Auditor, and delivered both agent
greetings through Discord webhooks under their own names.

## Event evidence

The saved official 2026 source says, “Submissions close at 11:59 PM IST on
November 7.” This converts to **7 November 2026, 18:29 UTC**.
See the [official event page](https://www.wemakedevs.org/hackathons/switch) and
[source-backed checklist](scout/checklists/flip-the-switch.md) for provenance,
eligibility questions and unresolved form requirements. Judging percentages
were not verified; static animation placeholders are not treated as weights.
NEAR is a separate rule-source demonstration, not this entry's requirements.

## Limits and final human actions

The approval gate is agent instruction, not transactional authorization.
Exclusive roles coordinate agents; they do not assign a human approval right.
A clean installation replay and adversarial access tests remain unverified.
Local OAuth uses a temporary HTTPS tunnel; restart instructions are documented.
The fixture's successful audit does not certify this entry's eligibility.

Before submitting: review and publish the repository, record/upload the demo,
replace the pending video entry with its real URL, confirm personal eligibility
and the final form requirements, then submit manually. No optional social,
voice-input or bonus-prize evidence is claimed.

[Demo walkthrough](docs/DEMO_SCRIPT.md)
