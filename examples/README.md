# Rehearsal fixtures

`broken-project/` deliberately has three submission defects: its README asks for
a nonexistent `requirements.txt`, it has no project-specific LICENSE, and it has
no demo link. Its actual app needs only `python3 app.py`. Do not fix these fixtures
in the main Ship Check repository. The root MIT license still covers the fixture;
the simulated checklist specifically asks for a project-root license file.

For an audit rehearsal, copy the contents of `broken-project/` into a **separate**
public test repository you own, then use that owner/name in the Switch template.
Keep write access scoped to that test repository. Do not imply this nested folder
is already an independently cloneable repository.

Use `checklists/sample-project.md` for a deterministic rehearsal. The other two
checklists are pending source verification, not completed rule extraction.
