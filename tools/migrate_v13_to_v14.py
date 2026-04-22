#!/usr/bin/env python3
"""Additive migration: schema v1.3.0 → v1.4.0.

Scans wiki/ for MD files with frontmatter `schema_version: "1.3.0"` (or older)
and additively adds null v1.4 fields where missing, then bumps schema_version
to "1.4.0". Body content untouched.

Usage:
    python3 tools/migrate_v13_to_v14.py [--dry-run] [--vault PATH]

    --dry-run  : report diff per file, do not write
    --vault    : vault path (default: current working directory)

v1.4 additive diff per entity type:

    aesthetic:
        + iconclass, iconclass_uncertainty
        + ulan_id, met_id, moma_id, cooperhewitt_id, rijks_id, tate_id,
          nga_id, bfi_id, magnum_id, archnet_id, riba_id, loc_cai,
          gcd_id, moby_id, igdb_id
        + iso_standard, nng_url
        + prompts.ux_flow, prompts.painting, prompts.motion (null-default)

    panel:
        (no additive frontmatter fields; schema_version bump only)

    source / concept / other:
        (no additive frontmatter fields; schema_version bump only)

Non-destructive. Never changes existing field values. Never touches body.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

REPO = Path(__file__).resolve().parents[1]
# Default to cwd; author-path hardcode removed 2026-04-22 to kill
# "works on my machine" bugs (author's private vault paper-over).
DEFAULT_VAULT = Path.cwd()


def _validate_vault_or_exit(vault_path: Path) -> Path:
    """Fail fast if `vault_path` does not look like a Bab-ilu vault.

    A Bab-ilu vault has `.agent/` (lens configs) or `wiki/` (LLM-written
    content) at its root. The prior behaviour silently accepted any
    directory — which masked "works on my machine" bugs. Now we error
    clearly so the user sees the problem immediately.
    """
    vault_path = vault_path.resolve()
    has_agent = (vault_path / ".agent").is_dir()
    has_wiki = (vault_path / "wiki").is_dir()
    if not (has_agent or has_wiki):
        import sys as _sys
        print(
            f"error: {vault_path} does not look like a Bab-ilu vault "
            f"(no .agent/ or wiki/ subdirectory). Pass --vault <path> "
            f"explicitly or run this command from a vault root.",
            file=_sys.stderr,
        )
        _sys.exit(2)
    return vault_path

# v1.4 aesthetic frontmatter additions (all optional, null-default)
AESTHETIC_NEW_FIELDS = [
    ("iconclass", None),
    ("iconclass_uncertainty", None),
    ("ulan_id", None),
    ("met_id", None),
    ("moma_id", None),
    ("cooperhewitt_id", None),
    ("rijks_id", None),
    ("tate_id", None),
    ("nga_id", None),
    ("bfi_id", None),
    ("magnum_id", None),
    ("archnet_id", None),
    ("riba_id", None),
    ("loc_cai", None),
    ("gcd_id", None),
    ("moby_id", None),
    ("igdb_id", None),
    ("iso_standard", None),
    ("nng_url", None),
]

# v1.4 prompts block additive keys
PROMPTS_NEW_KEYS = ["ux_flow", "painting", "motion"]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def split_frontmatter(text: str) -> tuple[str, str, str] | None:
    """Return (pre, frontmatter_body, post) or None if no frontmatter."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    return ("---\n", m.group(1), "\n---\n" + text[m.end() :])


def get_field(fm: str, field: str) -> str | None:
    """Return the raw value line of `field:` or None."""
    m = re.search(rf"^{re.escape(field)}:\s*(.*)$", fm, re.MULTILINE)
    return m.group(1).strip() if m else None


def get_type(fm: str) -> str | None:
    return get_field(fm, "type")


def get_schema_version(fm: str) -> str | None:
    v = get_field(fm, "schema_version")
    if v:
        return v.strip('"').strip("'")
    return None


def add_field_before(
    fm: str, field: str, value: str, anchor: str
) -> str:
    """Insert `field: value` before the first line matching anchor prefix."""
    lines = fm.split("\n")
    new_line = f"{field}: {value}"
    for i, line in enumerate(lines):
        if line.startswith(anchor):
            lines.insert(i, new_line)
            return "\n".join(lines)
    # fallback: append
    lines.append(new_line)
    return "\n".join(lines)


def add_field_at_end(fm: str, field: str, value: str) -> str:
    if fm.endswith("\n"):
        return f"{fm}{field}: {value}\n"
    return f"{fm}\n{field}: {value}"


def has_field(fm: str, field: str) -> bool:
    return get_field(fm, field) is not None


def ensure_aesthetic_fields(fm: str) -> tuple[str, list[str]]:
    """Add v1.4 aesthetic-specific fields if missing. Returns (new_fm, added_fields)."""
    added: list[str] = []
    for field, default in AESTHETIC_NEW_FIELDS:
        if not has_field(fm, field):
            val = "null" if default is None else repr(default)
            fm = add_field_at_end(fm, field, val)
            added.append(field)
    return fm, added


def ensure_prompts_modalities(fm: str) -> tuple[str, list[str]]:
    """Add ux_flow / painting / motion keys to prompts: block if missing.

    Keeps it simple — appends keys with null values under the prompts block.
    Only acts if `prompts:` exists.
    """
    added: list[str] = []
    if not re.search(r"^prompts:\s*$", fm, re.MULTILINE):
        return fm, added

    for key in PROMPTS_NEW_KEYS:
        pattern = rf"^\s+{key}:"
        if re.search(pattern, fm, re.MULTILINE):
            continue
        # Insert after the last indented line under prompts:
        prompts_match = re.search(r"^prompts:\s*$", fm, re.MULTILINE)
        if not prompts_match:
            continue
        start = prompts_match.end()
        # Find end of prompts block (next unindented line or EOF)
        rest = fm[start:]
        end_match = re.search(r"\n(?=\S)", rest)
        if end_match:
            insert_pos = start + end_match.start()
            fm = fm[:insert_pos] + f"\n  {key}: null" + fm[insert_pos:]
        else:
            fm = fm + f"\n  {key}: null"
        added.append(key)

    return fm, added


def bump_schema_version(fm: str, to: str = "1.4.0") -> str:
    return re.sub(
        r'^(schema_version:\s*)["\']?\d+\.\d+\.\d+["\']?',
        rf'\1"{to}"',
        fm,
        count=1,
        flags=re.MULTILINE,
    )


def add_schema_version_if_missing(fm: str, to: str = "1.4.0") -> tuple[str, bool]:
    if has_field(fm, "schema_version"):
        return fm, False
    return add_field_at_end(fm, "schema_version", f'"{to}"'), True


def migrate_file(path: Path, dry_run: bool = False) -> dict:
    text = path.read_text(encoding="utf-8")
    split = split_frontmatter(text)
    if not split:
        return {"path": path, "skipped": "no frontmatter"}

    pre, fm, post = split
    entity_type = get_type(fm)
    old_version = get_schema_version(fm) or "(none)"

    # Skip if already 1.4.0 or newer
    if old_version not in ("(none)", "1.3.0", "1.2.0", "1.1.0", "1.0.0"):
        if old_version.startswith("1.4") or old_version >= "1.4.0":
            return {"path": path, "skipped": f"already {old_version}"}

    new_fm = fm
    added: list[str] = []
    prompts_added: list[str] = []

    if entity_type == "aesthetic":
        new_fm, added = ensure_aesthetic_fields(new_fm)
        new_fm, prompts_added = ensure_prompts_modalities(new_fm)

    # All types get schema_version bump
    if has_field(new_fm, "schema_version"):
        new_fm = bump_schema_version(new_fm, "1.4.0")
    else:
        new_fm, _ = add_schema_version_if_missing(new_fm, "1.4.0")

    if new_fm == fm:
        return {"path": path, "skipped": "no diff"}

    if not dry_run:
        path.write_text(pre + new_fm + post, encoding="utf-8")

    return {
        "path": path,
        "type": entity_type,
        "old_version": old_version,
        "added_fields": added,
        "added_modalities": prompts_added,
    }


def iter_wiki_mds(vault: Path) -> Iterable[Path]:
    wiki = vault / "wiki"
    for p in wiki.rglob("*.md"):
        if p.is_symlink():
            continue
        yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Report only, don't write")
    ap.add_argument(
        "--vault",
        default=str(DEFAULT_VAULT),
        help=f"Vault path (default: {DEFAULT_VAULT})",
    )
    args = ap.parse_args()

    vault = _validate_vault_or_exit(Path(args.vault))
    if not (vault / "wiki").is_dir():
        print(f"error: vault path has no wiki/: {vault}", file=sys.stderr)
        sys.exit(2)

    print(f"Vault: {vault}")
    print(f"Mode:  {'DRY-RUN' if args.dry_run else 'APPLY'}")
    print()

    total = 0
    migrated = 0
    skipped = 0
    details = []

    for path in iter_wiki_mds(vault):
        total += 1
        result = migrate_file(path, dry_run=args.dry_run)
        if "skipped" in result:
            skipped += 1
            continue
        migrated += 1
        details.append(result)

    print(f"Scanned: {total} MDs")
    print(f"Migrated: {migrated}")
    print(f"Skipped (no diff or already 1.4+): {skipped}")
    print()

    # Group by entity type
    by_type: dict[str, list[dict]] = {}
    for d in details:
        by_type.setdefault(d["type"] or "(untyped)", []).append(d)

    for etype, items in sorted(by_type.items()):
        print(f"=== {etype} ({len(items)} migrated) ===")
        for d in items:
            rel = d["path"].relative_to(vault)
            added = d["added_fields"]
            modalities = d["added_modalities"]
            summary_bits = []
            if added:
                summary_bits.append(f"+{len(added)} fields")
            if modalities:
                summary_bits.append(f"+modalities: {','.join(modalities)}")
            summary = " · ".join(summary_bits) or "(version bump only)"
            print(f"  {rel}  [{d['old_version']}→1.4.0] {summary}")
        print()


if __name__ == "__main__":
    main()
