# Ship Check V2 — launch control

Run the dashboard with Python 3.10+ and Git:

```sh
python3 -m control.server --repo .
```

Open http://127.0.0.1:8787. The service binds only to the local machine. It stores
audit evidence and decisions under `~/.ship-check/`, separately for each checkout.
Tracked and unignored file changes trigger a recheck every 15 seconds. Use
`--interval 5`, `--port 8788` or `--database /absolute/path/state.sqlite3` as needed.

`control/event.json` holds the event deadline, original quote, source URL and
retrieval timestamp from Scout's saved checklist. The dashboard labels it as
saved rules; refresh the source before relying on it. Other repositories can
provide their own event file or omit it.

## What the checks establish

### Scout event rules

The **Event rules** selector lists Scout's `scout/checklists/*.md` outputs. The
current event defaults to `control/event.json`'s `checklist` path. Selecting another
checklist immediately audits only that event; a previously configured deadline
is hidden rather than carried into the other event. Selection persists locally.
Scout's changes to the selected file trigger automatic rechecks.

Each stable requirement becomes a dashboard check with its category, exact quote,
official source, source location and applicability. MUST items count toward
readiness; OPTIONAL items and guidance remain visible but unscored.
Conditional prize requirements start unscored; recording passed or blocked makes
them applicable and scored, while not-applicable keeps them excluded.
Checked Markdown boxes are never treated as proof. All event requirements initially need
review: in **Source quote and verification**, record a result plus supporting
evidence. The owner can mark verified, blocked or not applicable with a reason.
Reviews persist across rechecks of identical repository bytes and are invalidated
when the project, checklist or selected event changes. Missing quotes cannot be
marked verified. Eligibility and subjective criteria do not auto-pass from files.

New Scout checklists must use the documented `scout/AGENT.md` output format. Empty
checklists, duplicate IDs and paths outside the checklist directory are rejected.

The dashboard inspects README content, setup headings, referenced requirements
files, root license, submission brief and supported video URLs. It shows actual
file evidence and the commit associated with each audit. A video URL is not proof
of playback; file presence is not a successful setup execution or eligibility
certification. Use Switch Scout for event-specific rules and Auditor for execution.

## Review and pull requests

When a requirements file is missing, the engine proposes a reviewable README
change. Missing submission briefs get an explicitly labelled draft. Approve or
reject exact file contents in the dashboard or Discord. Decisions are bound to
the audit and repository fingerprint; changing a file invalidates old approvals.

**Create PR** requires a clean checkout, GitHub CLI (`gh`) signed in, a writable
origin remote, and at least one approved fix. It creates a `codex/ship-check-*`
branch in a temporary Git worktree, commits only approved files, pushes and opens
a pull request against the audited branch. It never merges the PR. If push
succeeds but PR creation fails, the branch remains on GitHub for manual recovery.
The local owner session is the authority; this is not a multi-user hosted service.

## Discord buttons and automatic updates

Install the optional Discord library in a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r control/requirements.txt
```

Provide `DISCORD_BOT_TOKEN`, `DISCORD_CHANNEL_ID` and `DISCORD_OWNER_ID` securely
through your process environment, then start `.venv/bin/python -m control.server`.
Use the existing Ship Check bot and channel; no additional Discord permissions
are needed. The service posts readiness reports and review buttons to that
channel. Only the configured owner can review, approve, reject, rerun an audit or
create the approved PR. Review opens a private exact-diff attachment with decision
buttons. Previous audit buttons reject stale changes. On restart, the latest
audit's public controls are restored; request a fresh audit for older messages.

Switch continues to coordinate Scout and Auditor. V2 supplies the deterministic
check ledger and owner controls alongside their shared Discord room.

On this Mac, reuse the installed Switch Discord connection without copying a token:

```sh
python3 -m control.switch_local --bridge f2fcebe1-afc2-40a0-8ade-070436f2a519 --channel 1568294022110388326 --owner 1417535988829392978 --repo .
```

This optional launcher uses Switch's bundled runtime, reads only the selected
bridge's existing credential into memory and starts the dashboard. It depends on
Switch's local database schema; environment-based startup is the portable option.

## Verification

```sh
python3 -m unittest discover -s tests -v
node --check control/static/app.js
```

Tests cover actual temporary Git repositories, persistent evidence, stale
approval rejection, score changes, unknown fixes, and isolated worktree commits
containing only approved changes. Network push and PR creation are mocked in the
test suite; the existing V1 PR is a separate live GitHub receipt.
