# Local setup — 6 November 2026

- Docker Desktop opened; Docker Engine responds with version 29.5.3.
- Switch Console 0.40.1 installed in `/Applications/Switch Console.app` from the
  official Apple-silicon release. Download SHA-256 matched the release digest;
  macOS code-signature verification passed.
- Local Switch server 0.31.0 started through Console and shows Running.
- Bundled Mattermost container is healthy; Console shows the linked `@user` account.
- Standalone Codex CLI 0.167.0 installed through the official npm package;
  Console shows Installed / Signed in.
- Private repository created and scaffold pushed:
  https://github.com/medhansh-19/ship-check
- Ship Check template saved privately in the local Switch workspace through its
  template API. Live server validation returned `ok: true`, no errors and no
  warnings. The saved template also appears in Console's Templates list.

## Remaining setup blocker

Console marks GitHub **Unavailable** on this localhost server:

> GitHub needs a server with an https address, so it can't work on this one.

The scoped connector needs an HTTPS server address and GitHub App configuration.
No tunnel, public server exposure, GitHub App credential or agent repository grant
has been created. Local `gh` authentication was used by the setup session to
create/push the repository; it has not been configured as the auditor's fallback.

Scout and auditor have not been provisioned, and no audit or approval/PR rehearsal
has run. The onboarding buddy placeholder exists without a connected AI session.
Keep the repository private until its owner chooses to publish it.

Next: choose an HTTPS hosting/tunnel arrangement, configure the GitHub App with
the owner's participation for credentials and permissions, grant only
`medhansh-19/ship-check`, and instantiate the template with Codex and Mattermost.
