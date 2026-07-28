# Repository Agent Context

Keep this file under 150 lines. It is the canonical source for agent behavior in
this repository. (`AGENTS.md` is a symlink to this file — edit only `CLAUDE.md`.)

## Overview

`vitalic-static-assets` is a tiny static-asset repository holding shared Vitalic
brand assets (currently the `vitalic-stacked-colored.svg` logo). It is not an
application: there is no build, no runtime, and no dependencies. Consumers
reference the raw files directly
(`https://raw.githubusercontent.com/vitalic-energy/vitalic-static-assets/main/<file>`),
so **file names and paths are a public contract** — renaming or moving a
published asset breaks external links.

## Build And Test

- Install: none.
- The gating CI `test` job asserts exactly three things — reproduce locally from
  the repo root before opening a PR:

  ```bash
  test -f vitalic-stacked-colored.svg              # required asset, exact name
  find . -type f -not -path './.git/*' -size +2M   # must print nothing
  shopt -s globstar; for s in **/*.svg; do
    python3 -c "import sys,xml.dom.minidom; xml.dom.minidom.parse(sys.argv[1])" "$s"
  done                                             # every SVG = well-formed XML
  ```

- CI also gates on `gitleaks` (secrets scan). It installs the gitleaks **CLI**
  directly — do not swap back to `gitleaks-action@v2` (it crashed calling the PR
  commits API; the CLI install is the fix).
- Lint / Typecheck / Run app: not applicable.
- Local pre-commit hooks use `check-added-large-files` (500 KB default), stricter
  than CI's 2 MB — a legitimate 0.5–2 MB asset passes CI but needs
  `--no-verify` or a hook tweak locally.

## Conventions

- Asset names: lowercase-hyphenated `vitalic-<layout>-<variant>.<ext>`
  (e.g. `vitalic-stacked-colored.svg`).
- Keep assets small and web-appropriate (< 2 MB hard CI limit); optimize SVGs,
  no embedded raster data or external references.
- Adding a new asset: place the file, run the three checks above, and record the
  intended consumer / raw URL in the PR description. Making an asset CI-required
  means editing `.github/workflows/ci.yml` — a red path.
- Never commit secrets, `.env` files, generated dependency folders, or local
  machine artifacts.
- Keep changes scoped to the assigned task; prefer existing local patterns over
  new abstractions.

## Red Paths

Flag for human approval before merge when a change includes:

- deletion, rename, or replacement of a published asset (external raw-URL
  consumers depend on exact paths; `vitalic-stacked-colored.svg` is also
  hard-required by CI);
- `.github/`, `CLAUDE.md`, or `AGENTS.md` changes;
- reviewer-identified anomalies.

## PR Expectations

PRs must include intent, approach, risk, migrations yes/no (always N/A here),
and validation: state that the three local CI checks above pass.
