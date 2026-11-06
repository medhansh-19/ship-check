# Reuse Ship Check

In the same Discord room, start a new dashboard session and specify the exact
repository, branch and optionally event URL. Public repositories support anonymous
read-only audits. Private reads and all pushes/PRs require the corresponding scoped
GitHub connection. There is no automatic grant to all repositories.

Example for the owner's public Afterglow repository:

```text
@shipcheck-auditor Apply the updated reusable repository policy in this room.
Read-only audit https://github.com/medhansh-19/Afterglow branch main.
Assess general project readiness: fresh-clone setup, tests, documentation and
demo evidence. No event is selected; do not apply Switch hackathon requirements.
Propose numbered fixes. Do not edit or push; report separately if PR access is missing.
```

For event-specific work, include `Event: https://official-event-url` and mention
Scout to extract and hand over that event's source-backed checklist first. Use a
new session for each project/event. The workspace learns repository and branch
from the owner's explicit GitHub URL and `branch NAME` message; results are the
new observed agent messages, not reused demo output.

The optional static repository-check disclosure remains tied to the local runner's
`--repo` checkout. To use it for a different project, start the runner with that
project's local Git checkout. Changing a Discord target alone does not change
the local filesystem being checked. The live agent workspace can observe other
requested public repositories without that checkout change.

To enable PRs for another repository, install the existing GitHub App on that
selected repository and update Auditor's exact-repository Switch grant. Never
grant all repositories just to enable reuse. Agent sessions that began before
the policy update should be restarted or told to reread current room instructions.
