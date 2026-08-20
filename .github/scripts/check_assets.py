#!/usr/bin/env python3
"""The `test` gate for vitalic-static-assets.

This repository is a public store of brand assets that other Vitalic sites embed
by URL. Four things can actually break here, and each has a consequence:

1. **An SVG that is not well-formed XML** — every site embedding it renders
   nothing.
2. **An asset over 2 MB** — unusable as a logo on a page, and a public repo pays
   for the bandwidth.
3. **Script or external references inside an SVG** — a public SVG embedded by
   other sites is an XSS and tracking vector. `<script>`, `on*` handlers and
   `<foreignObject>` have no business in a logo.
4. **No SVG at all** — the mark everything links to has been deleted. Guards the
   exact shape this repo was in on 2026-08-13.

Deliberately stdlib-only: no lockfile, no dependency to keep current, nothing that
can break this gate for a reason unrelated to the assets.

Run locally with `python3 .github/scripts/check_assets.py`.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAX_BYTES = 2 * 1024 * 1024
SVG_NS = "http://www.w3.org/2000/svg"

# Attribute-level script vectors. `href`/`xlink:href` are allowed (fragment and
# data URIs are normal in SVG) but a remote http(s) reference in a logo is not.
_EVENT_ATTR = re.compile(r"^on[a-z]+$", re.I)
_REMOTE_REF = re.compile(r"^\s*https?://", re.I)


def tracked_files() -> list[Path]:
    """Every file in the checkout, excluding .git and CI's own scripts."""
    return sorted(
        p for p in ROOT.rglob("*")
        if p.is_file() and ".git" not in p.parts and ".github" not in p.parts)


def check_size(path: Path, problems: list[str]) -> None:
    size = path.stat().st_size
    if size > MAX_BYTES:
        problems.append(f"{path.relative_to(ROOT)}: {size} bytes exceeds the "
                        f"{MAX_BYTES}-byte asset limit")


def check_svg(path: Path, problems: list[str]) -> None:
    rel = path.relative_to(ROOT)
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        problems.append(f"{rel}: not well-formed XML — {exc}")
        return
    if root.tag != f"{{{SVG_NS}}}svg":
        problems.append(f"{rel}: root element is {root.tag!r}, expected an SVG "
                        f"root in the {SVG_NS} namespace")
    for element in root.iter():
        local = element.tag.split("}")[-1] if isinstance(element.tag, str) else ""
        if local in ("script", "foreignObject"):
            problems.append(f"{rel}: contains <{local}> — not permitted in a "
                            f"publicly embedded asset")
        for name, value in element.attrib.items():
            local_attr = name.split("}")[-1]
            if _EVENT_ATTR.match(local_attr):
                problems.append(f"{rel}: has event handler attribute {local_attr!r}")
            if local_attr in ("href", "src") and _REMOTE_REF.match(value):
                problems.append(f"{rel}: references a remote URL in {local_attr!r}")


def main() -> int:
    files = tracked_files()
    svgs = [p for p in files if p.suffix.lower() == ".svg"]
    problems: list[str] = []

    if not svgs:
        problems.append("no .svg files found — this repository exists to hold them")

    for path in files:
        check_size(path, problems)
    for path in svgs:
        check_svg(path, problems)

    for path in svgs:
        print(f"checked {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")

    if problems:
        print(f"\nFAILED — {len(problems)} problem(s):", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1
    print(f"\nOK — {len(svgs)} SVG(s), {len(files)} file(s), all within limits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
