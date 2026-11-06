# Live audit evidence

Synthetic rehearsal, run `20261106T143108Z-7c9e85`, against the original
`codex/demo-broken` SHA `c06d2e26b50b24d6edbe268c1e53850d55876aad`.

- [Report](report.md): actual failures, file evidence and numbered fixes.
- [Command evidence](evidence.log): real stdout/stderr, working directories and exit codes.
- [Synthetic checklist](checklist.md): this fixture's rules, separate from official event rules.
- [PR #1](https://github.com/medhansh-19/ship-check/pull/1): authored by the scoped GitHub App.

The owner approved fixes 1 (README), 2 (MIT LICENSE), and 4 (SUBMISSION.md)
in room message `sw_7177bc4400ddf25df513aa04f0995d81`. Fix 3 was deferred because
there is no real video URL. Only those three approved files changed; app.py did not.
The corrected README command exited 0 and printed `Ready to ship.`

The owner then approved merging the reviewed PR. It merged into the isolated
demo branch at `4696b01b4422ec9c60427a19e5c56ced2f756936` on
2026-11-06 at 14:39:31 UTC. The main project branch retains the fixture files
under examples/ so they remain available for another rehearsal.

Switch room: `shipcheck-shipcheck`; scout and auditor run on Codex. The auditor's
GitHub grant names only repository ID `1448179949` (medhansh-19/ship-check), with
write access; scout has no GitHub grant. Provider tool approval is retained.
