---
version: alpha
name: Ship Check
description: A live workspace for source-backed agent handoffs.
colors:
  primary: '#285fd5'
  background: '#f5f7fb'
  surface: '#ffffff'
  ink: '#192c47'
  muted: '#596a80'
  border: '#dce3ec'
typography:
  sans:
    fontFamily: "Avenir Next, Segoe UI, sans-serif"
  mono:
    fontFamily: "ui-monospace, monospace"
rounded:
  DEFAULT: '6px'
spacing:
  section-gap: '20px'
components:
  button: {}
  dialog: {}
---
# Ship Check workspace design
## Overview
Product register for hackathon builders watching Scout-to-Auditor work. English
UI, en-IN formatting, Asia/Kolkata event timestamps. No Japan-specific scope.
The signature is the four-stage observed handoff strip. Replace the previous
cream-and-serif marketing treatment with a quiet working application.
## Colors
Runtime CSS in control/static/style.css owns tokens (Model B). The frontmatter
mirrors --primary, --background, --surface, --ink, --muted and --border directly.
Semantic success, warning and danger remain text-labelled, never color-only.
## Typography
Sans for application labels and restrained 27px page heading; mono only for
literal message evidence and diffs. No oversized promotional headline.
## Layout
190px desktop navigation; natural document scroll; activity has its own bounded
390px viewport. Below 760px navigation becomes horizontal and panels stack.
## Elevation & Depth
White surfaces and thin borders; no gradients or decorative shadows.
## Shapes
6px shared control and surface radius. Stage dots are circular for status.
## Components
Shared dialog(), button(), message(), empty() own repeated behaviors in app.js.
Global scrollbar variables style all application overflow regions. Buttons reserve
40px height, expose focus and disabled/busy states. Native details own disclosures.
## Do's and Don'ts
- Show only observed messages and source artifacts in the workspace.
- Preserve empty, offline and owner-locked states.
- Do not present static file checks as an agent's executed audit.
- Do not animate or fabricate agent progress percentages.
