# Verified local setup — 6 November 2026

- Docker Engine 29.5.3 and the bundled Mattermost container are healthy.
- Switch Console 0.40.1 and local Switch server 0.31.0 are running.
- Codex CLI 0.167.0 is signed in; both final agents are running.
- The Ship Check template passed live validation with no errors or warnings.
- Room: shipcheck-shipcheck, bridged to Mattermost, with linked owner @user.
- Scout addressing: anyone; auditor addressing: owner-agents.
- Exclusive approver role exists as an agent coordination role, not human authorization.
- The GitHub App ship-check-medhansh-19-2026 is installed on ship-check only.
- Switch's GitHub connection is authenticated as medhansh-19. Only auditor has a
  write grant to this repository; scout has none.
- [PR #1](https://github.com/medhansh-19/ship-check/pull/1) completed the real audit,
  numbered approval and owner-approved merge into the isolated demo branch.
- [Audit evidence](../examples/audit-evidence/README.md) records the observed results.
- Discord bridge `Ship Check Demo` is active. Switch created `#ship-check-demo`
  and attached both final agents; each posted a greeting under its own name.
  See the [Discord setup receipt](../docs/DISCORD_SETUP.md).

## Restart and HTTPS limitation

The local server runs directly on macOS; Mattermost uses Docker. Start Docker,
then start the server in Switch Console. Local agents and room history survive
restarts; a live read-back test verified the two checklist documents after recovery.

The scoped GitHub connector requires HTTPS. This demo uses a temporary Cloudflare
Quick Tunnel to the local API listener. It must remain running during OAuth
callbacks. A new Quick Tunnel gets a new hostname; update both Switch's
GATEWAY_PUBLIC_URL and the GitHub App callback before reconnecting. Console
regenerates local native server settings on startup, so the temporary HTTPS
override must be reapplied after a server restart. It is not persistent hosting.
Use a stable HTTPS deployment for a team installation. Follow the official
[Switch hosting guide](https://docs.switchagents.ai/flintai/switch/deploy/self-host).

All private keys, client secrets and OAuth credentials stay outside this repository.
No credential value is part of the template, README, submission draft or evidence.
The extra manually registered App is not used by this verified workflow.

## Remaining human submission steps

- Review and publish the project repository.
- Record and upload the demo; add its real URL to README and SUBMISSION.md.
- Verify personal eligibility and the submission form, then submit manually.
- Optional prize posts/voice evidence remain human tasks; none are claimed complete.
