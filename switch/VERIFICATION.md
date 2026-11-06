# Template verification and remaining questions

Checked 2026-11-06 against Switch source revision
`93c132cf6836f2a0200aae3c7a0359764fcbd48a`. The template is a draft, not a deployed
or end-to-end-tested room.

## Sources

- [Template language](https://github.com/sandbox-quantum/switch/blob/93c132cf6836f2a0200aae3c7a0359764fcbd48a/docs/TEMPLATES.md)
  — document structure, params, placeholders, agent block, room block and kickoff.
- [Triage pair](https://github.com/sandbox-quantum/switch/blob/93c132cf6836f2a0200aae3c7a0359764fcbd48a/examples/agent-templates/triage-pair.template.yaml)
  — starting pattern for team-prefixed agents and a shared room.
- [Role lease model](https://github.com/sandbox-quantum/switch/blob/93c132cf6836f2a0200aae3c7a0359764fcbd48a/core/switch_core/db/models.py)
  — RoleLease records an agent holder; see also the official
  [hand-off guide](https://docs.switchagents.ai/flintai/switch/using/hand-off-work).

## Confirmed fields used

| Area | Fields / semantics |
| --- | --- |
| Document | `version: 1`, `params`, `agents`, `room`, `kickoff` |
| Params | `type`, `description`, `pattern`, `default`, `input: advanced` |
| Types | `string`, `provider`, `bridge`, `location`, `directory` |
| Defaults | Provider fallback list; `$first` bridge; `local`; `{$agents_dir}` |
| Agents | `name`, `description`, `instructions`, `addressing`, `provider`, `location`, `directory`, `auto_mode`, `auto_approve`, `connections` |
| GitHub | `service: github`, `access: write`, `repos: [owner/name]` |
| Room | `name`, `description`, `bridge`, `agents`, `users`, `aliases`, `instructions`, `roles` |
| Role | `name`, `exclusive`, `instructions` |
| Aliases | Agent name as the key, alias as the value |
| Creator | `{$creator}` adds the deployer via their linked messaging account |

All instruction text is inline; no unsupported file-include field is used.
Separate directory defaults use explicit team-prefixed names, avoiding reliance
on the single-agent `{agent}` builtin in a multi-agent template. The prompts in
`scout/AGENT.md`, `audit/AGENT.md` and `ROOM.md` are mirrored in the template; keep
them synchronized when editing.

## Uncertainties and deliberate limits

1. **Human approver role:** the requested exclusive role is defined, but upstream
   documents roles as agent-held leases. No confirmed field assigns a human as
   holder. Do not claim exclusive human approval enforcement. The draft instead
   requires direct approval from the auditor's owner. Supporting another human
   approver needs a verified identity and addressing design before use.
2. **Prompt approval gate:** numbered-fix approval is agent policy, not a server
   transaction that blocks Git writes. `auto_approve: false` governs provider tool
   permissions, not the validity of human fix approval. Live-test refusals and
   owner approval before presenting this as a reliable workflow.
3. **GitHub operations:** field syntax and grant scope are confirmed; the user's
   connection, clone credentials, available Git/PR tools and branch permissions
   still need a live test. A grant is not proof that a clone or PR was created.
4. **Working directories:** default workspaces are separate Switch agent folders.
   Use Advanced to point to this checkout's scout/ and audit/ when desired. A
   working directory is not filesystem isolation. No sandbox is claimed.
5. **Rule sources:** event checklists are explicitly pending. Official requirements,
   source deadlines and event-year validity have not been extracted in step one.
6. **Template validation:** static YAML, field/placeholder checks and instruction
   synchronization can run locally. Upstream Python lint could not import in the
   existing environment because `sqlalchemy` is absent. Console import, actual
   provisioning, room commands, alias addressing and clean-room replay remain
   untested. No Switch session or external repository was created in this step.

## Next live checks

- Import the YAML, inspect both machines/directories, provider and connection.
- Create with a fresh team prefix and confirm kickoff plus both aliases.
- Verify a non-owner can ask scout and cannot direct auditor.
- Pass the full checklist in-room; confirm auditor acknowledges it.
- Run the separate broken-project repo; inspect actual command logs and fix IDs.
- Reject a fix, approve a different subset as owner, and inspect the resulting PR.
- Verify no unapproved edits, no fake evidence, no publication or automatic merge.
- Remove only disposable test resources deliberately, then replay the template
  and repeat before recording the demo.
