# Template verification and remaining questions

Checked 2026-11-06 against Switch source revision
`93c132cf6836f2a0200aae3c7a0359764fcbd48a`. The template passed live server validation and provisioned both agents and a
Mattermost-backed room. The audit-to-approved-PR workflow completed; see
[the evidence receipt](../examples/audit-evidence/README.md).

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

## Verified live behavior

- Both agents were provisioned from the template with separate directories.
- Scout extracted official Flip the Switch and NEAR checklists. A synthetic
  fixture checklist was handed to auditor through the shared room.
- Auditor fresh-cloned the isolated demo branch and captured actual command failures.
- The owner approved fixes 1, 2 and 4 with MIT, deferring the video fix.
- The scoped GitHub App opened PR #1 with only the approved three files.
- Corrected setup printed `Ready to ship.`; the owner separately approved merging.
- Only auditor has GitHub write access, limited to the selected repository.

## Deliberate limits and unverified checks

- Switch exclusive roles are agent-held leases, not exclusive human authorization.
  Auditor instructions require direct owner approval; another human approver is
  not configured.
- Numbered approval is agent policy, not a server transaction blocking Git writes.
  `auto_approve: false` retains provider permission checks. Adversarial refusal
  and non-owner negative tests have not been completed.
- Agent working directories are not filesystem sandboxes.
- Creating the room worked; deleting and recreating a clean installation has not
  been rehearsed. Do not claim complete clean-room reproducibility.
- Official source checklists preserve unresolved requirements and source limits.
  The successful synthetic audit is not an eligibility certification.
- Local HTTPS uses a temporary tunnel with a restart caveat documented in
  [local setup](LOCAL_SETUP.md).
