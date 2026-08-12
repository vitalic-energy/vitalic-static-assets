# vitalic-static-assets

Shared Vitalic Energy brand assets, served straight from this repository over HTTPS.

This is not an application. There is no build step, no runtime, no dependencies and no
package to install — the files in this repository *are* the product.

## Contents

| File | What it is |
|---|---|
| `vitalic-stacked-colored.svg` | The stacked "VITALIC ENERGY" wordmark with the gradient mark. |

## Using an asset

Reference the raw file directly:

```
https://raw.githubusercontent.com/vitalic-energy/vitalic-static-assets/main/vitalic-stacked-colored.svg
```

That URL serves the asset itself, with the file's own content type — so it can be used as
an `<img src="...">`, fetched, or downloaded as-is. The general form is:

```
https://raw.githubusercontent.com/vitalic-energy/vitalic-static-assets/main/<file>
```

## ⚠️ File names and paths are a public contract

**Renaming, moving or deleting a published asset breaks every external link to it.**

Consumers reference these raw URLs directly. There is no redirect layer, no version
negotiation and no way to tell who is depending on a given path — a raw URL that stops
resolving simply starts returning a 404, wherever it was embedded. Treat every published
path as permanent.

- **Adding** a new asset is safe.
- **Replacing** an asset's *contents* at the same path is safe, and is how a refreshed
  version of an existing mark should ship.
- **Renaming, moving or removing** an asset is a breaking change. Publish the new file
  alongside the old one and leave the original path in place.

## Conventions

- Asset names are lowercase-hyphenated: `vitalic-<layout>-<variant>.<ext>`, e.g.
  `vitalic-stacked-colored.svg`.
- Keep assets small and web-appropriate. CI fails on any file larger than 2 MB.
- Optimise SVGs. No embedded raster data and no external references — an asset must render
  standalone.

## Checks

Every pull request and every push to `main` runs two jobs:

- **`gitleaks`** — scans the full history for secrets.
- **`test`** — asserts the expected assets are present, that no file exceeds 2 MB, and that
  every SVG parses as well-formed XML.

Contributors are encouraged to install the `.pre-commit-config.yaml` hooks
(`pre-commit install`), which catch most of the above before a commit is made. Note the
local large-file hook uses a stricter threshold than CI.
