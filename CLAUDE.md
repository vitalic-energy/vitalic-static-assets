# vitalic-static-assets Agent Context

Workspace-wide rules are in the Vitalic workspace `CLAUDE.md`; this file is the
repo-specific layer and wins on conflict only where it is more specific.

## What this repo is

A **public** store of Vitalic brand assets — SVGs that other Vitalic sites embed
by URL. There is no application, no build and no deploy: the files in the root
*are* the product. Keep it that way; anything that needs a build pipeline belongs
in the repo that consumes it.

Public matters. A secret committed here is published the moment it lands, and it
stays published after it is removed — which is why the `gitleaks` job scans the
**full history** (`fetch-depth: 0`), not just the diff.

## Build and test

```bash
python3 .github/scripts/check_assets.py     # exactly what the gating `test` job runs
```

Stdlib only, no dependencies, no lockfile. It asserts that every SVG is
well-formed XML with an SVG root, that no file exceeds 2 MB, that no SVG carries
`<script>`, `<foreignObject>`, an `on*` handler or a remote `href`/`src` (this is
a public asset other sites embed), and that at least one SVG still exists.

## The merge gate — read before touching `.github/`

`main` is protected by the `protect-main` ruleset (id `18455716`), which requires
the status checks **`gitleaks`** and **`test`**, with **no bypass actors** and 0
approving reviews.

Those are literal strings stored in GitHub, not in this repo, and **a required
context is a job's display `name:`**. So:

- **Renaming either job in `.github/workflows/ci.yml` blocks every open pull
  request**, with all checks green, until someone with admin edits the ruleset.
- Deleting the workflow does the same, permanently. That is not hypothetical: on
  2026-08-13 `main` was reset to a commit predating `.github/`, and every PR here
  was unmergeable until CI was restored (`vitalic-hermes-infra#133`).
- No agent can repair either state. The Hermes GitHub App has no
  `administration` permission, so only Luke can change a ruleset.

## Conventions

- **Branch and open a PR; never push to `main`.** Merging is Luke's call.
- Never commit a key, token, connection string or SAS URL — see "Public" above.
- Add assets at the repository root with descriptive, lowercase, hyphenated names
  (`vitalic-stacked-colored.svg`). Optimise before committing; the 2 MB ceiling is
  a backstop, not a target.
- Keep `AGENTS.md` in step with this file if one is added.
