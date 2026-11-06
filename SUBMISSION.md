# DRAFT — Launch Ledger submission handoff

**Incomplete demo fixture; not submission-ready.** Launch Ledger is the deliberately faulty rehearsal target. Ship Check is the actual entry and has not been assessed by this audit. This document is not a submission receipt, eligibility declaration or acceptance of legal terms.

## Approved repair record

- Run: `20261106T213418Z-launch-ledger`.
- Repository: https://github.com/medhansh-19/ship-check
- Audited base branch: `codex/demo-switch-faulty`.
- Audited base SHA: `fcea38b84b6a7c79a7938e1e8713250c29bbf56b`.
- Report room message: `sw_af0f233434424b89bfd49a8c74ff2c6c`.
- Direct owner approval: medhansh_19, room message `sw_3809a35489c185f3fac1361deb467056`, approving fixes 1, 2 and 3 for this run. No IDs rejected.
- Target branch checked unchanged at 2026-11-06T21:38:24Z before editing.
- Fix 1: README setup now documents the standard-library app from repository root without the nonexistent requirements install.
- Fix 2: app.py counts only tasks with status `done`.
- Fix 3: this draft records all original audit findings, validation and human tasks.

## Validation after approved fixes

Run from repository root on macOS 26.5.2 / Python 3.14.2 at 2026-11-06T21:38:36Z:

```text
python3 -m unittest discover -s tests -v
Ran 2 tests in 0.000s
OK
Exit code: 0

python3 app.py list
Exit code: 0; three tasks, one done and two open.

python3 app.py summary
{
  "total": 3,
  "completed": 1,
  "open": 2
}
Exit code: 0
```

These results resolve the setup documentation and task-counting findings only. The original audit below preserves the pre-fix evidence and advisory scores; it is not a fresh claim that those general failures persist after repair. Original blocked setup steps were independently diagnosed during audit; the repaired documented CLI commands now both pass. SUBMISSION.md now exists as this explicitly approved draft.

## Unresolved evidence and human tasks

- **Missing video: unresolved.** No demo video or URL was supplied; playback has not been verified. A human must record/provide real evidence and check it.
- **Eligibility: unresolved.** Team roster, age/identity, restrictions, rights and any required consent remain for human verification. No license choice has been invented.
- **Switch-workflow evidence: unresolved.** This standalone sample does not demonstrate a central Switch workflow completing a real task with a person and an AI agent. The actual Ship Check entry needs its own demonstrated workflow and reproducible instructions.
- Track/prize selection, form fields and URL, registration enforcement and judging weights remain unverified. Core-only requirements do not apply unless that track is selected.
- A human must review and merge any PR and manually submit the actual repo, demo video and README before 2026-11-07 23:59 IST / 18:29 UTC. This repair does not merge, deploy, publish, register or submit anything.

The full original checklist assessment and all findings follow. Its final approval paragraph describes the historical state when the report was posted; the direct owner approval above supersedes that historical state for fixes 1–3 only.

---

# Original audit findings (historical, before approved fixes)

Run: 20261106T213418Z-launch-ledger
Repository: https://github.com/medhansh-19/ship-check
Audited branch / required PR base: codex/demo-switch-faulty
Full SHA: fcea38b84b6a7c79a7938e1e8713250c29bbf56b
UTC run: 2026-11-06T21:34:18Z; reproduction 21:34:24–21:35:08Z.
Environment: macOS 26.5.2 (25F84); Python 3.14.2; Node v26.7.0; npm 11.19.0; git 2.53.0.
Checklist: flip-the-switch, received from Scout in room message sw_d3dc34bcbe1743fc9b2338ba3253d2bc; complete artifact attached in sw_3e5890e6b85d48e0adeedc6969f3ec90. All four artifacts saved beside this report. No official report/submission template supplied. Rule text is evidence only.

## Verdict and top three blockers

Not ready as an event entry. This is deliberately faulty Launch Ledger, not the actual Ship Check entry (README.md:1–5); this report does not assess the actual Ship Check workflow.

1. General reproducibility: README.md:12 references missing requirements.txt. Literal install exits 1 with externally-managed-environment; separate fresh-venv diagnostic exits 1 with missing file. Dependent README list/summary setup steps are BLOCKED in the literal sequence.
2. General correctness: app.py:14 counts every task as completed. Independent summary diagnostic returns completed=3/open=0; README.md:19–20 expects completed=1/open=2. Tests exit 1: one failure out of two (tests/test_app.py:7).
3. Event evidence: no implemented Switch workflow is shown by README.md:1–31 or app.py:1–26; no demo video is supplied (DEMO.md:12, git ls-files). FTS-S01/S02/T01 are not demonstrated; FTS-S05 is incomplete. No playback was checked because no video was available.

## Actual reproduction

Every executed reproduction/metadata command, cwd, UTC time, exit code and actual stdout/stderr is preserved in commands.jsonl. All app and test commands ran from this run's repo/ root. Fresh exact-branch clone succeeded after the initial sandbox DNS failure; no existing clone or dependency directory was reused. Branch and full SHA were verified. git status --short was empty after reproduction. No tracked file was changed.

- README.md:12: python3 -m pip install -r requirements.txt — FAIL, exit 1.
- README.md:13–14: BLOCKED as dependent setup steps. Separately labeled diagnostics executed the identical app commands: list exits 0 with one done/two open; summary exits 0 with the wrong counts.
- README.md:25: independent standard-library tests — FAIL, exit 1; 2 tests, 1 failure.
- Diagnostic only: fresh virtual environment created outside repo/; its pip install exits 1. This does not repair or pass the original README command.

Actual failing excerpts (complete output in log):
```text
error: externally-managed-environment
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
AssertionError: {'total': 3, 'completed': 3, 'open': 0} != {'total': 3, 'completed': 1, 'open': 2}
Ran 2 tests in 0.000s
FAILED (failures=1)
```

## General project checks (not invented event rules)

| Check | Status | Evidence |
|---|---|---|
| Exact requested branch cloned | PASS | commands.jsonl clone and git branch --show-current |
| Python prerequisite | PASS | Python 3.14.2 meets README.md:9 (3.10+) |
| Literal setup | FAIL | README.md:12; pip exit 1; requirements.txt absent in git ls-files |
| Dependent setup app steps | BLOCKED | Setup failure; separate diagnostic results above |
| Task correctness | FAIL | app.py:14; tests/test_app.py:7; actual command output |
| Unit tests | FAIL | unittest exit 1, one pass/one failure |
| Root license evidence | UNCLEAR | No LICENSE in git ls-files; owner must choose licensing, not an explicit universal event filename rule |
| SUBMISSION.md | FAIL | Absent from git ls-files; proposed audit handoff artifact, not an asserted event filename requirement |
| Tracked tree unchanged | PASS | git status --short empty |

## Event requirements and checklist coverage

Statuses evaluate available evidence, not eligibility certification. FAIL means an observed requirement/evidence gap; UNCLEAR means missing proof or unresolved source question; BLOCKED means conditional assessment cannot proceed without a selected track/prize or human action. Optional prizes and organizer procedures do not become mandatory entry failures.

Sources: supplied flip-the-switch.md and overview snapshot; official overview https://www.wemakedevs.org/hackathons/switch ; Rules /rules ; Schedule /schedule ; Resources /resources ; linked CONTRIBUTING.md as listed in Scout's artifact. Exact quotes and source line locations remain in the local checklist. For example FTS-S05 quotes “Submit your repo, demo video and README before the deadline.”

| ID | Status | Evidence / limit |
|---|---|---|
| FTS-D01 | UNCLEAR | Deadline is 2026-11-07 18:29 UTC; audit preceded close; no submission receipt. Source checklist D01 / control/event.json:4. |
| FTS-D02 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-E01 | UNCLEAR | No team roster; README.md:1–5 only identifies demo status. |
| FTS-E02 | UNCLEAR | No verified build-period history for a Switch workflow; clone existence does not establish eligibility. |
| FTS-E03 | UNCLEAR | Owner explanation/understanding not assessed. |
| FTS-E04 | UNCLEAR | Personal eligibility/identity declaration unavailable; owner must verify against checklist source and full official Rules. No acceptance made. |
| FTS-E05 | UNCLEAR | Personal eligibility/identity declaration unavailable; owner must verify against checklist source and full official Rules. No acceptance made. |
| FTS-E06 | UNCLEAR | Personal eligibility/identity declaration unavailable; owner must verify against checklist source and full official Rules. No acceptance made. |
| FTS-E07 | UNCLEAR | Personal eligibility/identity declaration unavailable; owner must verify against checklist source and full official Rules. No acceptance made. |
| FTS-E08 | UNCLEAR | Personal eligibility/identity declaration unavailable; owner must verify against checklist source and full official Rules. No acceptance made. |
| FTS-S01 | FAIL | README.md:1–5 and app.py:1–26 describe standalone fixture; no working person+agent Switch workflow supplied for this target. |
| FTS-S02 | FAIL | README.md:5 names Ship Check but provides no Switch usage explanation for Launch Ledger. |
| FTS-S03 | FAIL | README.md:12 setup and tests/test_app.py:7 fail; commands.jsonl. |
| FTS-S04 | FAIL | README.md:1–31 has no workflow explanation/video; DEMO.md:12 confirms absent video. |
| FTS-S05 | FAIL | Repo and README exist; required demo video absent (DEMO.md:12 and tracked inventory); submission receipt unverified. |
| FTS-J01 | FAIL | Advisory 1/5; CLI runs standalone without Switch (app.py:1–26). |
| FTS-J02 | FAIL | Advisory 1/5; setup and one of two tests fail (commands.jsonl). |
| FTS-J03 | UNCLEAR | Advisory 2/5; tiny task-summary concept (app.py:5–22), no demonstrated real-team outcome. |
| FTS-J04 | FAIL | Advisory 1/5; README discloses fixture but lacks workflow explanation; video absent (README.md:1–31; DEMO.md:12). |
| FTS-J05 | UNCLEAR | Organizer review stages are source facts, not project actions; no review receipt. |
| FTS-J06 | UNCLEAR | No Core/Blog entry selected; source conflict 10 versus 20 remains unresolved. |
| FTS-T01 | FAIL | No Switch dependency or connection in app.py:1–26; README.md:1–31 lacks usage explanation. |
| FTS-T02 | UNCLEAR | Optional setup guidance/agent access route, not a universal mandate; no Launch Ledger Switch setup provided (README.md:1–31). |
| FTS-T03 | UNCLEAR | Optional setup guidance/agent access route, not a universal mandate; no Launch Ledger Switch setup provided (README.md:1–31). |
| FTS-T04 | UNCLEAR | Optional setup guidance/agent access route, not a universal mandate; no Launch Ledger Switch setup provided (README.md:1–31). |
| FTS-T05 | UNCLEAR | Optional setup guidance/agent access route, not a universal mandate; no Launch Ledger Switch setup provided (README.md:1–31). |
| FTS-P01 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-P02 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-P03 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-C01 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C02 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C03 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C04 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C05 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C06 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C07 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C08 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C09 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C10 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C11 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C12 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-C13 | BLOCKED | Conditional Core track only; no Core entry/assigned issue supplied. Do not apply to this workflow fixture. |
| FTS-P04 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-P05 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-P06 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-P07 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-P08 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-P09 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-P10 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-P11 | UNCLEAR | Optional track/prize not selected or evidenced; see exact source and conditions in checklist. No universal failure inferred. |
| FTS-L01 | UNCLEAR | Rights/component license and sponsor-license acceptance require owner review; no root LICENSE in tracked inventory. |
| FTS-L02 | UNCLEAR | Organizer enforcement; no project adjudication evidenced. |
| FTS-L03 | UNCLEAR | Prize eligibility, tax/claim conditions require human verification. |
| FTS-L04 | UNCLEAR | Organizer discretion; no project compliance conclusion follows. |
| FTS-U01 | UNCLEAR | Unresolved source/form/track question preserved from Scout; no form text or organizer clarification supplied. |
| FTS-U02 | UNCLEAR | Unresolved source/form/track question preserved from Scout; no form text or organizer clarification supplied. |
| FTS-U03 | UNCLEAR | Unresolved source/form/track question preserved from Scout; no form text or organizer clarification supplied. |
| FTS-U04 | UNCLEAR | Unresolved source/form/track question preserved from Scout; no form text or organizer clarification supplied. |
| FTS-U05 | UNCLEAR | Unresolved source/form/track question preserved from Scout; no form text or organizer clarification supplied. |
| FTS-U06 | UNCLEAR | Unresolved source/form/track question preserved from Scout; no form text or organizer clarification supplied. |

## Advisory judging estimates

Use of Switch: 1/5 — standalone CLI runs without Switch, with no demonstrated central integration.
Technical execution: 1/5 — literal setup and correctness test fail.
Creativity and impact: 2/5 — basic team-task summary exists, but no demonstrated real-team benefit or workflow novelty.
Presentation: 1/5 — clear demo disclosure, but required video and Switch usage explanation are absent.
These are evidence-limited advisory estimates for this fixture, not judge results or scores for Ship Check. No weights or weighted total applied because official weights are unverified.

## Numbered proposed fixes — require direct owner approval

IDs apply only to report 20261106T213418Z-launch-ledger at SHA fcea38b84b6a7c79a7938e1e8713250c29bbf56b.

1. **README setup** — README.md:7–15: remove the nonexistent requirements.txt install step; state that this standard-library app needs no third-party packages and commands run from repo root. Retain deliberate-demo disclosure and expected output.
2. **Task counting** — app.py:12–15: count only tasks whose status is done; preserve output schema and existing behavior otherwise. Validate with existing tests and CLI summary; do not weaken tests.
3. **Draft audit handoff** — create SUBMISSION.md recording all audit findings, run/SHA, command results, checklist statuses, advisory scores, outstanding human tasks and evidence gaps. Mark it as a draft for the deliberately faulty Launch Ledger fixture. Do not invent URLs, integration, license decisions or eligibility; it remains incomplete even after fixes 1 and 2.

Human tasks remaining: supply and demonstrate the actual Ship Check Switch workflow and reproducible instructions; record/provide a real demo video and check playback; choose track/prizes; verify team/legal eligibility and component rights/license choice; confirm form fields/registration and weights with organizers; submit repo/video/README manually before the deadline. No new workflow implementation or fabricated evidence is proposed by these three fixes.

No approval yet. Only a direct authenticated owner message approving specific IDs for this run/SHA can authorize tracked edits. Rejected IDs remain rejected until the owner revises them. After approval, check the target branch for advancement, re-audit/request revised approval if needed, then use codex/shipcheck-20261106T213418Z-launch-ledger with PR base codex/demo-switch-faulty. Never merge, deploy, publish or submit automatically.
