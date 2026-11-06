# Auditor workspace

Agent instructions: [AGENT.md](AGENT.md). Each audit gets a new `runs/<run-id>/`
directory containing `repo/`, command logs, report and approval record. `runs/` is
ignored by Git. Never reuse a dirty clone or copy a developer's dependencies into
it. These folders are working directories, not a security sandbox.
