# Backlog

Curated small chores Hermes may pick up when approved or in fallback chore mode. One item
per line with a size tag. Only real, already-agreed work goes here — anything needing a
decision belongs in an issue or in [`docs/ROADMAP.md`](docs/ROADMAP.md), not in this file.

Every item below is in `.github/workflows/ci.yml`, which is a **red path** — each one needs
human approval before merge, and they could reasonably ship as one PR rather than four.

- [S] Pin both `actions/checkout@v4` uses in `.github/workflows/ci.yml` to full 40-character
  commit SHAs, with the version in a trailing comment. A major-version tag is a mutable
  pointer that the tag owner can repoint at any commit; the rest of the estate pins by SHA
  and one sibling repo hard-fails CI on any unpinned action.
- [S] Verify the gitleaks tarball with `sha256sum -c -` **before** extracting and installing
  it. The download is currently unchecked, and the job then `sudo install`s the result to
  `/usr/local/bin` — so a substituted artefact would be run as root *and* would be the thing
  reporting whether this repo contains secrets. A sibling repo already carries the exact
  pattern to copy, including the checksum for the pinned version.
- [S] Carry the gitleaks version in a single env var (e.g. `GITLEAKS_VERSION`) instead of
  hard-coding `8.24.0` twice inside the download URL, so a version bump is one edit and the
  checksum above stays adjacent to the version it belongs to. Note the version also appears
  as `rev:` in `.pre-commit-config.yaml`; keeping those two in step is the point.
- [S] Add `permissions: contents: read` and a `concurrency` group with
  `cancel-in-progress: true` to `ci.yml`. The workflow currently declares neither, so it
  runs with the default token permissions and superseded pushes keep running to completion.
