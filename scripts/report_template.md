# Audit: <run-id>

Repository: <URL> | branch: <branch> | SHA: <full SHA>
Run time: <UTC timestamp> | environment: <OS, runtime versions>
Checklist: <slug, source URLs, room artifact/message reference>

## Top three blockers

1. <failure, evidence, impact>
2. <failure, evidence, impact>
3. <failure, evidence, impact; omit unused entries>

## Fresh-clone reproduction

For each command record cwd, exact command, exit code, and stdout/stderr.
Store full logs under the run directory; paste real failure output in the room.

```text
<actual output; do not fill with an invented successful run>
```

## Checklist evidence

| Rule ID | Status: PASS/FAIL/UNCLEAR/BLOCKED | Evidence and source quote |
| --- | --- | --- |
| <ID> | <status> | <file:line, command log, URL/section> |

## Advisory judging scores

| Criterion and source | Score 1–5 | Weight if sourced | Evidence and rationale |
| --- | --- | --- | --- |
| <criterion> | <score> | <weight or unspecified> | <evidence> |

## Proposed fixes — awaiting human approval

1. <exact file, specific edit, validation, limitations>
2. <another bounded fix>
3. Write SUBMISSION.md with findings, criteria evidence, demo script and remaining human tasks.

## Decisions

Approver: <verified owner identity> | room message: <ID/link> | report SHA: <SHA>
Approved IDs: <none until explicit approval>
Rejected IDs and reasons: <one line each>
PR: <pending; only replace with a real URL>
