# Repository Agent Context

Keep this file under 150 lines. It is the canonical source for agent behavior in
this repository.

## Overview

`vitalic-static-assets` is a tiny static-asset repository holding shared Vitalic
brand assets (currently the `vitalic-stacked-colored.svg` logo). It is not an
application: there is no build, no runtime, and no dependencies. Consumers
reference the raw asset files directly.

## Build And Test

- Install: none.
- Test: CI verifies expected assets exist and that SVG files are well-formed XML.
- Lint / Typecheck / Run app: not applicable.

## Conventions

- Never commit secrets, `.env` files, generated dependency folders, or local
  machine artifacts.
- Keep assets small and web-appropriate; avoid oversized binaries.
- Keep changes scoped to the assigned task.
- Prefer existing local patterns over new abstractions.

## Red Paths

Flag for human approval before merge when a change includes:

- deletion or replacement of a published asset that consumers may depend on;
- `.github/`, `CLAUDE.md`, or `AGENTS.md` changes;
- reviewer-identified anomalies.

## PR Expectations

PRs must include intent, approach, risk, migrations yes/no, and tests added.
