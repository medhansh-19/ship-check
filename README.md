# Launch Ledger — deliberately faulty Ship Check demo

A tiny task-summary app used as a rehearsal target for Ship Check. This is
intentionally incomplete sample software, not our actual hackathon entry.
Ship Check is the real Switch workflow being demonstrated.

## Setup

Requires Python 3.10+. This app uses only the Python standard library; no
third-party packages need to be installed. Run these commands from the
repository root.

```sh
python3 app.py list
python3 app.py summary
```

## Expected behavior

The sample has three tasks: one completed and two open. The summary should
report `total: 3`, `completed: 1`, `open: 2`.

## Tests

```sh
python3 -m unittest discover -s tests -v
```

## Demo disclosure

This fixture began with a broken setup command, a task-summary bug and absent
submission artifacts. The setup and counting issues are repaired; submission
evidence remains incomplete. Do not claim this fixture is eligible or
submission-ready.
