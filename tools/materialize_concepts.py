#!/usr/bin/env python3
"""Materialize repeated general-zettelkasten concept references.

This tool turns already-authored concept references in `wiki/note/*.md`
into minimal `wiki/concept/*.md` pages. It does not invent concepts, call
an LLM, edit notes, or touch `.agent/graph/*`.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

import yaml

try:
    from lens_loader import LensConfig, LensValidationError, load_lens
except ImportError:  # tools/ also importable as a package
    from tools.lens_loader import LensConfig, LensValidationError, load_lens


REPO = Path(__file__).resolve().parents[1]
DEFAULT_VAULT = Path.cwd()
DEFAULT_LENSES_BASE = REPO / ".agent" / "lenses"
LENS_ID = "general-zettelkasten"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")
CONCEPT_SECTION_RE = re.compile(
    r"^## Concepts \(tier_1_atoms\)\s*$"
    r"(.*?)"
    r"(?=^##\s+|\Z)",
    re.MULTILINE | re.DOTALL,
)
FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESERVED_SLUGS = {"concept-slug"}


@dataclass
class DiscoveryResult:
    lens: str
    notes_scanned: int = 0
    concept_references_found: int = 0
    skipped_invalid: int = 0
    references: dict[str, set[str]] = field(default_factory=dict)

    @property
    def reusable(self) -> list[str]:
        return sorted(slug for slug, notes in self.references.items() if len(notes) >= 2)

    @property
    def singletons(self) -> list[str]:
        return sorted(slug for slug, notes in self.references.items() if len(notes) == 1)


@dataclass
class MaterializeSummary:
    lens: str
    date: str
    notes_scanned: int
    concept_references_found: int
    existing_concepts: int
    created: list[str]
    skipped_existing: int
    reported_singleton: int
    skipped_invalid: int
    singleton_slugs: list[str]

    def to_json_dict(self) -> dict[str, Any]:
        return {
            "lens": self.lens,
            "notes_scanned": self.notes_scanned,
            "concept_references_found": self.concept_references_found,
            "existing_concepts": self.existing_concepts,
            "created": len(self.created),
            "skipped_existing": self.skipped_existing,
            "reported_singleton": self.reported_singleton,
            "skipped_invalid": self.skipped_invalid,
            "created_paths": self.created,
            "singleton_slugs": self.singleton_slugs,
        }


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Return `(frontmatter, body)` for one markdown file."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    raw = match.group(1)
    fm = yaml.safe_load(raw) or {}
    if not isinstance(fm, dict):
        raise ValueError("frontmatter is not a mapping")
    return fm, text[match.end():]


def _normalize_concept_target(raw: Any) -> str | None:
    """Normalize one concept reference to a slug, or return None."""
    if not isinstance(raw, str):
        return None
    value = raw.strip().strip("`").strip()
    if not value:
        return None
    match = WIKILINK_RE.search(value)
    if match:
        value = match.group(1).strip()
    if "/" in value:
        return None
    if value.startswith(("#", "^")) or "#" in value or "^" in value:
        return None
    if "." in value:
        return None
    value = value.strip()
    if value in RESERVED_SLUGS:
        return None
    if not SLUG_RE.fullmatch(value):
        return None
    return value


def _flatten_frontmatter_values(raw: Any) -> list[Any]:
    """Flatten YAML values so unquoted `[[slug]]` still works.

    PyYAML parses an unquoted wikilink like `[[foo]]` as a nested list
    (`[["foo"]]`). Existing notes may mix quoted wikilinks and bare slugs,
    so concept extraction accepts both shapes.
    """
    if isinstance(raw, list):
        out: list[Any] = []
        for item in raw:
            out.extend(_flatten_frontmatter_values(item))
        return out
    return [raw]


def _concepts_from_frontmatter(fm: dict[str, Any]) -> tuple[set[str], int]:
    raw_concepts = fm.get("concepts", [])
    if raw_concepts in (None, ""):
        return set(), 0
    concepts: set[str] = set()
    invalid = 0
    for raw in _flatten_frontmatter_values(raw_concepts):
        slug = _normalize_concept_target(raw)
        if slug is None:
            invalid += 1
            continue
        concepts.add(slug)
    return concepts, invalid


def _concepts_from_body(body: str) -> tuple[set[str], int]:
    match = CONCEPT_SECTION_RE.search(body)
    if not match:
        return set(), 0
    section = HTML_COMMENT_RE.sub("", match.group(1))
    section = FENCED_CODE_RE.sub("", section)
    concepts: set[str] = set()
    invalid = 0
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith(("-", "*")):
            continue
        line_concepts = set()
        for wikilink in WIKILINK_RE.finditer(stripped):
            slug = _normalize_concept_target(wikilink.group(0))
            if slug is None:
                invalid += 1
                continue
            line_concepts.add(slug)
        concepts.update(line_concepts)
    return concepts, invalid


def extract_concepts_from_note(text: str) -> tuple[set[str], int]:
    """Extract canonical concept slugs from one note body."""
    fm, body = parse_frontmatter(text)
    fm_concepts, fm_invalid = _concepts_from_frontmatter(fm)
    body_concepts, body_invalid = _concepts_from_body(body)
    return fm_concepts | body_concepts, fm_invalid + body_invalid


def _validate_lens(lens: LensConfig) -> None:
    if (
        lens.id != LENS_ID
        or lens.entity_model.get("tier_0") != "note"
        or lens.entity_model.get("tier_1_atom") != "concept"
    ):
        raise ValueError(
            "materialize_concepts only supports general-zettelkasten "
            "with tier_0=note and tier_1_atom=concept"
        )


def discover_concepts(vault: Path, lens: LensConfig) -> DiscoveryResult:
    """Scan `wiki/note/*.md` and return concept→note references."""
    _validate_lens(lens)
    vault = Path(vault).resolve()
    note_dir = vault / "wiki" / "note"
    result = DiscoveryResult(lens=lens.id)
    if not note_dir.is_dir():
        return result

    note_paths = sorted(note_dir.glob("*.md"))
    note_slugs = {path.stem for path in note_paths}
    references: dict[str, set[str]] = {}

    for path in note_paths:
        result.notes_scanned += 1
        try:
            concepts, invalid = extract_concepts_from_note(
                path.read_text(encoding="utf-8")
            )
        except Exception:
            result.skipped_invalid += 1
            continue
        result.skipped_invalid += invalid
        for concept in concepts:
            if concept in note_slugs:
                result.skipped_invalid += 1
                continue
            references.setdefault(concept, set()).add(path.stem)

    result.references = references
    result.concept_references_found = sum(len(notes) for notes in references.values())
    return result


def render_concept_page(slug: str, note_slugs: set[str], *, today: str) -> str:
    """Render one minimal concept page."""
    sorted_notes = sorted(note_slugs)
    relation_lines = "\n".join(
        f"  - {{type: exemplifiedBy, target: [[{note_slug}]]}}"
        for note_slug in sorted_notes
    )
    ref_lines = "\n".join(f"- [[{note_slug}]]" for note_slug in sorted_notes)
    return (
        "---\n"
        "type: concept\n"
        f"lens: {LENS_ID}\n"
        f'created: "{today}"\n'
        "status: stub\n"
        "---\n\n"
        f"# {slug}\n\n"
        "<!-- llm:section-start materialize-concepts-relations -->\n"
        "relations:\n"
        f"{relation_lines}\n"
        "<!-- llm:section-end materialize-concepts-relations -->\n\n"
        "<!-- llm:section-start materialize-concepts-stub -->\n\n"
        "## Definition\n\n"
        "待补定义：将这个 concept 从引用它的 notes 中抽象成一句稳定定义。\n\n"
        "## Referenced By\n\n"
        f"{ref_lines}\n"
        "<!-- llm:section-end materialize-concepts-stub -->\n"
    )


def atomic_write_new_file(path: Path, text: str) -> bool:
    """Atomically create `path` if absent. Return False when it exists."""
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    tmp.write_text(text, encoding="utf-8")
    try:
        if path.exists():
            return False
        os.replace(tmp, path)
        return True
    finally:
        if tmp.exists():
            tmp.unlink()


def materialize_concepts(
    vault: Path,
    lens: LensConfig,
    *,
    dry_run: bool = False,
) -> MaterializeSummary:
    """Create missing concept pages for reused concept references."""
    _validate_lens(lens)
    vault = Path(vault).resolve()
    if not vault.exists() or not (vault / "wiki").is_dir():
        raise ValueError(f"{vault} does not look like a Bab-ilu vault")

    discovery = discover_concepts(vault, lens)
    concept_dir = vault / "wiki" / "concept"
    existing_concepts = {
        path.stem for path in concept_dir.glob("*.md")
    } if concept_dir.is_dir() else set()
    today = date.today().isoformat()

    created: list[str] = []
    skipped_existing = 0
    for slug in discovery.reusable:
        target = concept_dir / f"{slug}.md"
        rel_path = target.relative_to(vault).as_posix()
        if slug in existing_concepts or target.exists():
            skipped_existing += 1
            continue
        created.append(rel_path)
        if dry_run:
            continue
        text = render_concept_page(slug, discovery.references[slug], today=today)
        if not atomic_write_new_file(target, text):
            skipped_existing += 1
            created.remove(rel_path)

    return MaterializeSummary(
        lens=lens.id,
        date=today,
        notes_scanned=discovery.notes_scanned,
        concept_references_found=discovery.concept_references_found,
        existing_concepts=len(existing_concepts),
        created=created,
        skipped_existing=skipped_existing,
        reported_singleton=len(discovery.singletons),
        skipped_invalid=discovery.skipped_invalid,
        singleton_slugs=discovery.singletons,
    )


def _validate_vault_or_exit(vault: Path) -> Path:
    vault = vault.resolve()
    if not (vault / ".agent").is_dir() and not (vault / "wiki").is_dir():
        print(
            f"error: {vault} does not look like a Bab-ilu vault "
            "(no .agent/ or wiki/ subdirectory).",
            file=sys.stderr,
        )
        sys.exit(2)
    return vault


def _resolve_lens(args: argparse.Namespace) -> LensConfig:
    vault = Path(args.vault).resolve()
    if args.lenses_base:
        base = Path(args.lenses_base)
    else:
        vault_base = vault / ".agent" / "lenses"
        if args.lens and (vault_base / args.lens / "lens.yaml").exists():
            base = vault_base
        elif not args.lens and (vault_base / "active" / "lens.yaml").exists():
            base = vault_base
        else:
            base = DEFAULT_LENSES_BASE

    lens_id = args.lens
    if not lens_id:
        active_file = base / "active" / "lens.yaml"
        if not active_file.exists():
            print(
                "error: no --lens given and no active lens found. "
                "Pass --lens general-zettelkasten.",
                file=sys.stderr,
            )
            sys.exit(2)
        try:
            active = yaml.safe_load(active_file.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            print(f"error: could not parse {active_file}: {exc}", file=sys.stderr)
            sys.exit(2)
        lens_id = active.get("id")
    if not isinstance(lens_id, str) or not lens_id:
        print("error: lens id is missing", file=sys.stderr)
        sys.exit(2)

    try:
        lens = load_lens(lens_id, base=base)
    except (FileNotFoundError, LensValidationError) as exc:
        print(f"error: lens '{lens_id}' could not be loaded: {exc}", file=sys.stderr)
        sys.exit(2)
    try:
        _validate_lens(lens)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(2)
    return lens


def _print_human(summary: MaterializeSummary, *, vault: Path) -> None:
    print(f"materialize-concepts: lens={summary.lens}")
    print(f"  notes scanned: {summary.notes_scanned}")
    print(f"  concept references found: {summary.concept_references_found}")
    print(f"  existing concepts: {summary.existing_concepts}")
    print(f"  created: {len(summary.created)}")
    print(f"  skipped existing: {summary.skipped_existing}")
    print(f"  reported singleton: {summary.reported_singleton}")
    print(f"  skipped invalid: {summary.skipped_invalid}")
    print(
        "next: python3 -m tools.gap_runner --vault "
        f"{vault.resolve()} --lens {summary.lens}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", default=str(DEFAULT_VAULT))
    parser.add_argument("--lens", default=None)
    parser.add_argument("--lenses-base", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    vault = _validate_vault_or_exit(Path(args.vault))
    args.vault = str(vault)
    lens = _resolve_lens(args)

    try:
        summary = materialize_concepts(vault, lens, dry_run=args.dry_run)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(summary.to_json_dict(), ensure_ascii=False, indent=2))
    else:
        _print_human(summary, vault=vault)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
