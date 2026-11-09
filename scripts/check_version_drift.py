"""Fail when the SYP Companion install page shows a different version than the latest release.

The install page (syp/syp-companion/index.html) hard-codes "(version X.Y.Z)" next to each store
link. Releases on this repo are tagged syp-companion-vX.Y.Z. If the two differ, the page is stale
(or the release is) and this exits non-zero.

  python scripts/check_version_drift.py                  # asks `gh` for the latest release tag
  python scripts/check_version_drift.py --tag syp-companion-v0.11.0   # no network, for tests

Exit codes: 0 in step, 1 drift, 2 could not read the page or the tag.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = "yogicapproach/yogic-tools"
DEFAULT_PAGE = Path(__file__).resolve().parent.parent / "syp" / "syp-companion" / "index.html"
TAG_RE = re.compile(r"^syp-companion-v(\d+\.\d+\.\d+)$")
PAGE_RE = re.compile(r"\(version (\d+\.\d+\.\d+)\)")


def page_versions(html):
    return PAGE_RE.findall(html)


def tag_version(tag):
    m = TAG_RE.match(tag.strip())
    return m.group(1) if m else None


def latest_tag():
    out = subprocess.run(
        ["gh", "release", "view", "--repo", REPO, "--json", "tagName", "-q", ".tagName"],
        capture_output=True, text=True, check=True,
    )
    return out.stdout.strip()


def check(html, tag):
    """Return (exit_code, message)."""
    want = tag_version(tag)
    if want is None:
        return 2, f"cannot read a version from release tag {tag!r} (expected syp-companion-vX.Y.Z)"
    found = page_versions(html)
    if not found:
        return 2, "no '(version X.Y.Z)' text found on the install page"
    stale = sorted({v for v in found if v != want})
    if stale:
        return 1, f"DRIFT: install page shows {', '.join(stale)}; latest release is {want} ({tag})"
    return 0, f"ok: install page and latest release are both {want}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--page", type=Path, default=DEFAULT_PAGE)
    ap.add_argument("--tag", help="release tag to compare with; default: ask gh for the latest")
    args = ap.parse_args(argv)
    try:
        html = args.page.read_text(encoding="utf-8")
        tag = args.tag or latest_tag()
    except (OSError, subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    code, msg = check(html, tag)
    print(msg, file=sys.stderr if code else sys.stdout)
    return code


if __name__ == "__main__":
    sys.exit(main())
