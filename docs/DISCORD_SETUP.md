# Verified Discord integration — 6 November 2026

Ship Check is connected to the dedicated **Ship Check Demo** Discord server.
Switch reports the Discord bridge as active and channel creation enabled.

## Verified result

- Discord application and bot: `Ship Check`.
- Required gateway intents enabled: Server Members and Message Content.
- Presence intent remains disabled.
- Bot permissions are limited to View Channels, Send Messages, Send Messages
  in Threads, Manage Webhooks, Manage Channels, Manage Roles, Read Message
  History and Attach Files, plus the `applications.commands` scope.
- Switch bridge: `Ship Check Demo`.
- Switch room: `ship-check-demo`.
- Discord channel: `#ship-check-demo`.
- Attached agents: `shipcheck-scout` and `shipcheck-auditor`.
- Discord API read-back confirmed both agents posted their greeting messages.
- The Discord account `medhansh_19` is linked to the Switch admin identity.

The bot token is stored only in Switch's local credential store. It is excluded
from this repository and must never be pasted into documentation, commits, demo
captions or issue text.

## Demo flow

1. Open Discord's **Ship Check Demo** server and `#ship-check-demo`.
2. Mention Scout to extract a quoted rules checklist.
3. Mention Auditor with a repository, branch and completed checklist.
4. Show the evidence-backed numbered fixes in the shared channel.
5. Approve selected fix IDs as the linked owner.
6. Open the scoped GitHub pull request and show that only approved files changed.

Discord is the presentation surface; Switch still owns agent membership,
addressing, room instructions, GitHub scoping and the approval workflow.
