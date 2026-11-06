# Dynamic workspace — 7 November 2026

The primary workspace now starts empty and displays only messages observed after
the current session began. Static repository checks stay in a separate disclosure.
Existing audit history is retained; it does not prefill agent findings.

The Discord listener observes only the configured channel, authenticated owner,
and Scout/Auditor webhook messages owned by the configured bot. It reads Markdown
or text attachments under 200 KB. Scout's stable Markdown checklist items become
source-backed rules. Auditor messages become reports and actual GitHub PR links
become changes. Stage labels are observations, not a certification of completion.
Validation/retest reports mark Verify as report received, never an automatic pass.

The browser polls every three seconds. Server restart preserves the session;
New session retains earlier session records but resets the visible workspace.
No old Discord history is replayed. Keep Switch, the runner and tunnel online.
Discord message-content intent was already enabled in the existing bot setup.

## Verification

- 26 Python tests and four gateway tests pass; production build and JS syntax pass.
- Session tests cover blank startup despite previous audits, deduplication, source
  import, report/PR receipt and new-session isolation without deleting history.
- Safari inspected the empty workspace, confirmation dialog, cancellation and
  keyboard focus. The real Discord-to-dashboard conversation still needs a fresh
  Scout/Auditor message after deployment; no fake messages were injected into it.
- DESIGN.md lint: zero errors, three documentation-only orphan-token warnings.
- Premium's audit_project.py was unavailable at the installed skill path after
  its plugin files disappeared mid-session; no strict-audit pass is claimed.
- Narrow viewport, offline interaction and complete live agent flow remain
  unverified. The generated target informed the layout; exact pixel match is not
  claimed. The empty-state illustration was omitted in favor of functional copy.
