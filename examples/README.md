# Rehearsal fixtures

`broken-project/` deliberately has three submission defects: its README asks for
a nonexistent `requirements.txt`, it has no project-specific LICENSE, and it has
no demo link. Its actual app needs only `python3 app.py`. Do not fix these fixtures
in the main Ship Check repository. The root MIT license still covers the fixture;
the simulated checklist specifically asks for a project-root license file.

The isolated `codex/demo-broken` branch originally contained only this README
and app. Its original commit is `c06d2e26b50b24d6edbe268c1e53850d55876aad`.
[PR #1](https://github.com/medhansh-19/ship-check/pull/1) repaired that branch after
owner approval. For another failing rehearsal, create a new test branch from
the original commit in your own fork, then specify that branch in the audit.
Do not merge the fixture into the main project branch.

A nested fixture folder is not an independently cloneable repository. Use
`checklists/sample-project.md` for the deterministic rehearsal. The other two
checklists link to source-backed scout outputs, with their verification limits.
