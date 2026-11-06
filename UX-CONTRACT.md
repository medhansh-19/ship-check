# Workspace behavior

Business sources: control/README.md, docs/VERCEL.md, scout/AGENT.md, audit/AGENT.md.
Owner writes use the existing Vercel gateway key or local CSRF boundary.

## Canonical UI Map
| Capability | Canonical owner | Source of truth | Allowed variants | Verification |
|---|---|---|---|---|
| Form | dialog() and inline validation in app.js | This contract | owner secret, confirmation | Browser and unit tests |
| Scrollbar | Global style.css tokens | DESIGN.md | standard | Desktop and narrow captures |
| Toast | notice live region | This contract | status and inline dialog errors | Browser |
| CRUD | mutate() and workflow session service | server.py and workflow.py | new session retains history | Unit tests |
| Select/Listbox | None in redesigned workspace | No select UI | not applicable | Static audit |

## Lifecycle and data
New sessions start with no rules, findings or PRs, irrespective of static audit
history. Only new owner or trusted agent messages enter the current session.
Starting a session retains earlier session rows, with a confirmation explaining
the change. Server restarts preserve the session. Discord startup does not import
old channel history. No agent progress percentage is inferred.

## Feedback, navigation and recovery
Mutations are pessimistic, duplicate submits blocked, errors stay in their dialog.
Native modal dialogs provide inert background, Escape and focus restoration.
Owner key is masked with show/hide, kept only in page memory. No persistent secret
storage. Refreshes never replace open form input. Failed reads retain stale content
with a banner; bounded retries stop after five failures and expose Retry.
Result navigation uses hash links; page is a URL query parameter, ten items/page.
Activity is limited to the latest 30 of at most 100 retained session messages.
No search, date picker, bulk selection, deletion or table editing is provided.
Document title: Workspace — Ship Check. Unknown API routes return explicit 404.
Rules are quoted data; owner evidence and existing exact-fix approvals remain
separate from observed agent messages. PR links alone do not imply merge or pass.
