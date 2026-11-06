# Submission rehearsal record

This is a synthetic rehearsal, not an official hackathon submission or a claim
of submission readiness. No form has been submitted and no demo video is available.

## Audit identity and sources

- Repository: https://github.com/medhansh-19/ship-check
- Report/run: `20261106T143108Z-7c9e85`
- Audited branch and PR target: `codex/demo-broken`
- Audited base SHA: `c06d2e26b50b24d6edbe268c1e53850d55876aad`
- Reproduction: 2026-11-06, 14:31:40–14:32:18 UTC.
- Environment: macOS 26.5.2 (25F84), Darwin arm64, Python 3.14.2,
  Git 2.53.0, Node 26.7.0, npm 11.19.0.
- Checklist: `rehearsal-synthetic`, room document
  `14d04409-d9e4-44f4-88d7-eb5b96ccd7f8`.
- Source: owner-supplied synthetic fixture message
  `sw_8c1f56ec1b1d4b899ac2f18dbcf0ed0e`, handed off by Scout in
  `sw_e4df9ba10fc44383bd374518ea1f2507`.
- Report message: `sw_6a16944ac8534404bb693ed932f7ecd6` in Switch room
  `53c05986-9b8c-4fae-964c-f1143cf7d0c2` (`shipcheck-shipcheck`).
- Full original command logs and report are attached to room message
  `sw_e141c494ffc3494c96290357e036b98a`; each command records cwd,
  UTC time, exit code, stdout and stderr. No secret redactions were needed.

## Checklist and findings

| Quoted synthetic rule | Original audit | After approved fixes |
| --- | --- | --- |
| “The project-root README must provide working setup instructions for a fresh clone.” | FAIL: README.md:10 referenced an absent requirements.txt; the first command exited 1. | PASS on the recorded environment: revised README command exits 0 with the documented output. |
| “The project root must contain a file named LICENSE.” | FAIL: tracked tree contained only README.md and app.py. | PASS: LICENSE copied exactly from the owner-selected master source below. |
| “The README must link to a playable demo video.” | FAIL for missing link; playback BLOCKED because no URL exists. | Unresolved: no URL or placeholder added. Playback remains BLOCKED. |

The checklist also requires: “Run the README commands in order; capture actual
output and exit codes.” The original sequence stopped after its first failure;
the second step was marked BLOCKED and run separately as a diagnostic.

The fixture states: “Deadline: not applicable. Eligibility: demonstration only.
Required technology: none.” These statements apply only to this rehearsal.
No separate report/submission template was supplied.

## Command evidence

The fresh clone requested exactly `codex/demo-broken`, with no reused dependency
directory. The first clone attempt exited 128 with `Could not resolve host:
github.com`; an authorized network retry exited 0. The configured scoped Switch
GitHub helper was used with machine credential fallback disabled. This network
failure is recorded separately from project failures.

Original README step 1, cwd project root, exit 1, stdout empty; stderr included:

```text
python3 -m pip install -r requirements.txt
error: externally-managed-environment
× This environment is externally managed
```

The full stderr also contained a pip cache-permission warning and externally
managed environment guidance. No system-package override was used.

Separate diagnostic: created a fresh virtual environment outside the repository
(exit 0), then ran the following from the project root. It exited 1 with empty
stdout; stderr contained a cache-permission warning and:

```text
../diagnostic-venv/bin/python3 -m pip install -r requirements.txt
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
```

Separate diagnostic `python3 app.py` from the project root exited 0, with empty
stderr and this stdout:

```text
Ready to ship.
```

This diagnostic did not make the original README sequence pass.

Validation after fixes: ran the revised README's sole command, `python3 app.py`,
from the project root. Exit 0; stdout `Ready to ship.` followed by a newline;
stderr empty. The LICENSE bytes match the master source exactly. The reviewed
change scope is README.md, LICENSE and SUBMISSION.md; app.py is unchanged.

## Advisory scores

The source says: “Score reproducibility and presentation from 1 to 5 with
evidence; no weights apply.” These are original-audit estimates, not judge results
or a new score after fixes.

- Reproducibility: **2/5** — the original README installation failed, though the
  one-line app ran independently (README.md:10–11 and app.py:1 at the base SHA).
- Presentation: **1/5** — the minimal original README lacked the required demo
  evidence and the project root lacked LICENSE.

No weighted total is calculated.

## Owner decision and approved scope

Owner approval message `sw_7177bc4400ddf25df513aa04f0995d81`, authenticated as
`user (workspace owner)` in the audit room, explicitly approved IDs **1, 2, 4**
for this report and base SHA. The target branch was verified unchanged before
editing. No fix IDs were rejected; ID 3 was deferred for the reason below.

1. **Approved — README.md Setup:** remove the nonexistent requirements install,
   state no third-party dependencies and the project-root cwd, retain Python
   3.10+ and the app command, and show its observed output.
2. **Approved — LICENSE:** use the MIT license text from this project's master
   branch, exactly as selected by the owner. Source commit:
   `4bab52e89b67ac54ebc6d857f8ae279227fe4ca5`, path `LICENSE`.
3. **Deferred — README.md demo:** no real demo video URL is available yet; the
   owner instructed that no placeholder be added. Do not add a link without
   a real supplied URL and a revised owner decision.
4. **Approved — SUBMISSION.md:** record all audit findings, evidence, decisions,
   advisory scores and remaining human tasks in this file.

## Remaining human tasks

- Record and provide a real demo video URL. Verify access and actual playback;
  the demo criterion remains unmet until that evidence exists.
- Review and, if satisfied, merge the PR targeting `codex/demo-broken`.
- Recheck any actual event's official requirements before a real submission;
  this fixture does not establish eligibility or compliance for an event.
- Perform any eventual publishing, deployment or submission separately. Opening
  this PR does not complete submission.
