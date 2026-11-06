# V2 verification — 6 November 2026

- Local dashboard: http://127.0.0.1:8787. Main project has 5/6 static checks;
  the demo video URL remains missing.
- Discord API read-back confirmed readiness embeds and Run audit / Create
  approved PR controls delivered to `#ship-check-demo`.
- Safari exercised manual audit, exact review, rejection and separate approval
  in a disposable fixture. No main-project fixes were approved by these tests.
- Adding the missing fixture requirements file triggered an automatic recheck:
  2/6 → 3/6 checks, with old approvals reset and PR control disabled.
- 14 Python tests pass. JavaScript syntax and Git whitespace checks pass.
- PR tests create real isolated Git worktrees and commits; push and PR creation
  are mocked. V2 Discord clicks through a live PR have not been rehearsed.
  V1's PR #1 remains separate evidence.
- Desktop was visually inspected. Narrow viewport verification is pending.
  See the [visual receipt](v2-evidence/visual-evidence.json).

![Dashboard](v2-evidence/dashboard.png)

![Exact-change review](v2-evidence/review.png)
