"""
One-shot migration: flip `[[A|B]]` → `[[B|A]]` when `B.md` exists and `A.md`
does not.

Background: seed-kit files were written `[[display|slug]]` but Obsidian
treats the pre-pipe segment as the link target. We standardize to
`[[target|display]]` (= Obsidian native) without touching the user-facing
display text.

Decision rules per wikilink `[[A|B]]`:
  - `B.md` exists in vault, `A.md` does NOT → flip to `[[B|A]]`
  - `A.md` exists in vault, `B.md` does NOT → already correct; leave
  - both exist                               → AMBIGUOUS; leave + log
  - neither exists                           → BROKEN; leave + log
  - no pipe present                          → untouched

Usage:
  python tools/flip_wikilinks.py --vault seed-kit --dry-run
  python tools/flip_wikilinks.py --vault seed-kit --apply
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


WIKILINK_RE = re.compile(r"\[\[([^\]|]+)\|([^\]]+)\]\]")


@dataclass
class FlipReport:
    flipped: int = 0
    already_correct: int = 0
    ambiguous: list[tuple[Path, str]] = None
    broken: list[tuple[Path, str]] = None
    files_changed: int = 0

    def __post_init__(self) -> None:
        if self.ambiguous is None:
            self.ambiguous = []
        if self.broken is None:
            self.broken = []


def _index_slugs(vault_root: Path) -> set[str]:
    """Return a set of all markdown stems across the vault."""
    return {p.stem for p in vault_root.rglob("*.md")}


def _rewrite_file(
    path: Path,
    slugs: set[str],
    report: FlipReport,
    apply: bool,
) -> None:
    text = path.read_text(encoding="utf-8")
    changes_here = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal changes_here
        left, right = match.group(1).strip(), match.group(2).strip()
        left_exists = left in slugs
        right_exists = right in slugs

        if right_exists and not left_exists:
            changes_here += 1
            report.flipped += 1
            return f"[[{right}|{left}]]"
        if left_exists and not right_exists:
            report.already_correct += 1
            return match.group(0)
        if left_exists and right_exists:
            report.ambiguous.append((path, match.group(0)))
            return match.group(0)
        report.broken.append((path, match.group(0)))
        return match.group(0)

    new_text = WIKILINK_RE.sub(replace, text)

    if changes_here == 0:
        return

    report.files_changed += 1
    if apply:
        path.write_text(new_text, encoding="utf-8")


def run(vault: Path, apply: bool) -> FlipReport:
    slugs = _index_slugs(vault)
    report = FlipReport()
    for md in vault.rglob("*.md"):
        _rewrite_file(md, slugs, report, apply=apply)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", required=True, type=Path)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if not args.vault.is_dir():
        print(f"error: vault {args.vault} is not a directory", file=sys.stderr)
        return 2

    # Vault validation: ensure --vault points at a Bab-ilu vault root
    # (has .agent/ or wiki/). Without this, flip_wikilinks would iterate
    # any directory and potentially rewrite unrelated markdown files —
    # same "works on my machine" failure mode Wave 5 addressed for
    # tier-0-writing tools.
    if not ((args.vault / ".agent").is_dir() or (args.vault / "wiki").is_dir()):
        print(
            f"error: {args.vault.resolve()} does not look like a Bab-ilu vault "
            f"(no .agent/ or wiki/ subdirectory). Pass --vault <path> "
            f"pointing at a vault root.",
            file=sys.stderr,
        )
        return 2

    report = run(args.vault, apply=args.apply)

    mode_label = "APPLY" if args.apply else "DRY-RUN"
    print(f"[{mode_label}] vault={args.vault}")
    print(f"  flipped:          {report.flipped}")
    print(f"  already correct:  {report.already_correct}")
    print(f"  ambiguous:        {len(report.ambiguous)}")
    print(f"  broken:           {len(report.broken)}")
    print(f"  files modified:   {report.files_changed}")

    if report.ambiguous:
        print("\nAMBIGUOUS (both sides exist — manual review):")
        for path, raw in report.ambiguous[:20]:
            rel = path.relative_to(args.vault)
            print(f"  {rel}: {raw}")
        if len(report.ambiguous) > 20:
            print(f"  ... and {len(report.ambiguous) - 20} more")

    if report.broken:
        print("\nBROKEN (neither side exists — link truly dead):")
        for path, raw in report.broken[:20]:
            rel = path.relative_to(args.vault)
            print(f"  {rel}: {raw}")
        if len(report.broken) > 20:
            print(f"  ... and {len(report.broken) - 20} more")

    return 0


if __name__ == "__main__":
    sys.exit(main())
