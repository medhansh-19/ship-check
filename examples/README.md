# Rehearsal fixtures

`broken-project/` deliberately has three submission defects: its README asks for
a nonexistent `requirements.txt`, it has no project-specific LICENSE, and it has
no demo link. Its actual app needs only `python3 app.py`. Do not fix these fixtures
in the main Ship Check repository. The root MIT license still covers the fixture;
the simulated checklist specifically asks for a project-root license file.

The project repository also has an isolated `codex/demo-broken` branch whose
root contains exactly this README and app, with no requirements file, LICENSE,
or demo link. Audit that branch and target demo PRs at that branch. This allows
the rehearsal to use the same single-repository GitHub grant as Ship Check.
Do not merge the deliberately broken fixture into the main project branch.

For a separate installation, copy the fixture into a test repository or create
an isolated demo branch, then name the repository and branch in the audit request.
The nested folder alone is not an independently cloneable repository.

Use `checklists/sample-project.md` for a deterministic rehearsal. The other two
checklists are pending source verification, not completed rule extraction.
