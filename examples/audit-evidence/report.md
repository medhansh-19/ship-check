Report/run 20261106T143108Z-7c9e85 — READ-ONLY, SYNTHETIC rehearsal

Top three blockers:
1. README setup fails (README.md:10): pip exits 1 in the supplied environment; an isolated diagnostic also exits 1 because requirements.txt is absent.
2. Root LICENSE is absent (12-final-files.stdout:1–2 lists only README.md and app.py).
3. README has no demo video link (README.md:1–12); playback is BLOCKED by the missing URL.

Audited https://github.com/medhansh-19/ship-check, branch codex/demo-broken, full SHA c06d2e26b50b24d6edbe268c1e53850d55876aad. Run UTC 2026-11-06T14:31:08Z; reproduction 14:31:40–14:32:18 UTC. macOS 26.5.2 (25F84), Darwin arm64; Python 3.14.2, git 2.53.0, Node 26.7.0, npm 11.19.0. Clone succeeded through the configured scoped Switch helper with machine fallback removed for the process. Initial sandbox DNS failure (exit 128) is preserved separately in log 01; authorized network retry (02) exited 0. No tracked changes; no push or PR.

Source: rehearsal-synthetic document 14d04409-d9e4-44f4-88d7-eb5b96ccd7f8, Scout handoff sw_e4df9ba10fc44383bd374518ea1f2507, quoting owner fixture message sw_8c1f56ec1b1d4b899ac2f18dbcf0ed0e. Synthetic demonstration rules only; no separate templates supplied.

| Item and quoted fixture rule | Status | Evidence |
| --- | --- | --- |
| “The project-root README must provide working setup instructions for a fresh clone.” | FAIL | README.md:7 requires Python 3.10+, satisfied by 3.14.2; README.md:10 fails in log 07. README.md:11 is BLOCKED in the literal sequence after the failed prerequisite. |
| “Run the README commands in order; capture actual output and exit codes.” | PASS for recording; sequence BLOCKED | Log 07 preserves the first command, cwd, stdout/stderr and exit 1. Diagnostic 11 separately runs the second command and exits 0; this does not turn the literal sequence into a pass. |
| “The project root must contain a file named LICENSE.” / “Check for a project-root LICENSE, even if the fixture's parent has one.” | FAIL | Fresh branch tree contains only README.md and app.py (log 12). Parent files do not satisfy this item. |
| “The README must link to a playable demo video.” / “Check the link and playback; a placeholder is not a pass.” | FAIL link; BLOCKED playback | Entire README.md:1–12 contains no URL. No video was available to test; no playback claim made. |
| “Score reproducibility and presentation from 1 to 5 with evidence; no weights apply.” | PASS, advisory estimates below | Both criteria scored; no weighted total. |
| “Deadline: not applicable. Eligibility: demonstration only. Required technology: none.” | PASS / not applicable | Scope is this synthetic rehearsal; no external event requirements imported. |

Actual failing output (excerpts; complete unchanged stdout/stderr in attached evidence):

README step 1, cwd repo/, command `python3 -m pip install -r requirements.txt`, exit 1 (07):
```text
error: externally-managed-environment

× This environment is externally managed
```
Diagnostic only, fresh venv outside repo/, same requirements install from repo/, exit 1 (10):
```text
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
```
Diagnostic only, `python3 app.py`, cwd repo/, exit 0 (11):
```text
Ready to ship.
```
No secrets were redacted. Full logs include pip's cache-permission warning and externally managed environment guidance.

Advisory estimates, not judge results:
- Reproducibility: 2/5 — README setup fails, although the one-line dependency-free app runs independently (app.py:1; logs 07, 10, 11).
- Presentation: 1/5 — README.md:1–12 describes the CLI and setup, but supplies no demo video; the required root LICENSE is also absent (log 12).

Proposed fixes — IDs belong only to this report/SHA:
1. README.md, Setup section: remove the nonexistent requirements installation step; state that the current app uses no third-party dependencies, explicitly run from the project root, retain Python 3.10+ and `python3 app.py`, and show the observed `Ready to ship.` output. Scope: documentation only; validate the revised sequence.
2. LICENSE at project root: add only owner-selected, owner-supplied license text. BLOCKED on that choice/text; approval of an ID alone does not select a license.
3. README.md, demo section: add only a real owner-supplied video URL, then verify access/playback and record any limitation. BLOCKED on the actual URL; no invented link or placeholder will count.
4. SUBMISSION.md (new): record all audit findings, source identity, run/branch/SHA, command evidence, checklist statuses, advisory scores, approved/rejected fixes and remaining human tasks (license choice, real demo, review/merge and any eventual submission). Mark unresolved evidence honestly. Scope: documentation only, no fabricated artifacts.

No fixes approved or rejected yet. Per owner request and room rule “No tracked repository changes until the auditor's owner ... approves numbered fixes for a specific report in this room,” changes await direct owner approval of specific IDs for this report/SHA. Any later PR must target codex/demo-broken. Owner input is still needed for license text and the real demo URL.
