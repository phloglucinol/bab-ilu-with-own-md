"""Discover, validate, and activate Bab-ilu v2.1 lens configurations.

A lens is a discipline-specific ontology scheme plugged into Bab-ilu via
`.agent/lenses/<lens-id>/lens.yaml`. This module is the canonical reader:

    from tools.lens_loader import load_lens, load_all_lenses, activate_for_file

    cfg = load_lens("aesthetic-warburg")           # LensConfig
    all_cfgs = load_all_lenses()                    # dict[str, LensConfig]
    active = activate_for_file(content, fm, all_cfgs)  # list[str] of ids

`LensConfig` is a frozen dataclass so downstream consumers (graph_analyzer,
commands) can treat it as immutable.

Every `lens.yaml` is validated against `.agent/lenses/schema.json` at load
time. Invalid configs raise `LensValidationError` with the lens id and a
short, actionable message — never a silent fallback.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import jsonschema
import yaml

DEFAULT_BASE = Path(".agent/lenses")
SCHEMA_FILENAME = "schema.json"
LENS_FILENAME = "lens.yaml"

_DEFAULT_THRESHOLDS: dict[str, int | float] = {
    "cluster_member_min": 3,
    "cluster_min_size": 3,
    "density_multiplier": 3.0,
    "orphan_min_degree": 1,
    "domain_min": 5,
}

_DEFAULT_COMMUNITY_DETECTION: dict[str, Any] = {
    "algorithm": "louvain",
    "resolution": 1.0,
    "random_state": 42,
}

_SUPPORTED_ALGORITHMS = {"louvain", "leiden"}
# Must stay in sync with schema.json > properties > community_detection >
# properties > algorithm > enum. Kept as a runtime guard for callers that
# bypass schema validation by constructing configs programmatically.

_TRIGGER_RE = re.compile(r"^\|([a-z][a-z0-9-]*)\|\s*>=\s*(\d+)$")


class LensValidationError(Exception):
    """Raised when a lens.yaml cannot be parsed, is schema-invalid, or has
    internal inconsistencies (e.g. unknown community_detection.algorithm)."""

    def __init__(self, lens_id: str, details: str) -> None:
        self.lens_id = lens_id
        self.details = details
        super().__init__(f"[{lens_id}] {details}")


@dataclass(frozen=True)
class LensConfig:
    """Immutable lens configuration.

    All dict-valued fields are wrapped in `types.MappingProxyType` at
    construction time, so both the dataclass slot and the mapping contents
    are read-only. Consumers like graph_analyzer can freely cache and share
    a `LensConfig` across threads/requests without fear of mutation.
    """
    id: str
    version: str
    name: str
    description: str
    deliverable_types: tuple[str, ...]
    entity_model: Mapping[str, str]
    activation: Mapping[str, Any]
    thresholds: Mapping[str, int | float]
    anchors: Mapping[str, Any] | None
    allowed_subdomains: tuple[str, ...]
    community_detection: Mapping[str, Any]
    analysis_contract: Mapping[str, list[str]]
    extensions: Mapping[str, Any]
    source_path: Path = field(compare=False)


def _load_schema(base: Path) -> dict[str, Any]:
    schema_path = base / SCHEMA_FILENAME
    if not schema_path.exists():
        raise LensValidationError(
            "<schema>", f"schema.json not found at {schema_path}"
        )
    try:
        return json.loads(schema_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise LensValidationError(
            "<schema>", f"failed to parse schema.json: {exc}"
        ) from exc


def _read_yaml(path: Path, lens_id: str) -> dict[str, Any]:
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise LensValidationError(
            lens_id, f"YAML parse error in {path}: {exc}"
        ) from exc
    if not isinstance(raw, dict):
        raise LensValidationError(
            lens_id, f"{path} must be a YAML mapping, got {type(raw).__name__}"
        )
    return raw


def _validate_against_schema(
    cfg: dict[str, Any], schema: dict[str, Any], lens_id: str
) -> None:
    try:
        jsonschema.validate(instance=cfg, schema=schema)
    except jsonschema.ValidationError as exc:
        # Surface the missing/bad field in the message.
        loc = "/".join(str(p) for p in exc.absolute_path) or "<root>"
        raise LensValidationError(
            lens_id, f"schema violation at {loc}: {exc.message}"
        ) from exc


def _apply_defaults(cfg: dict[str, Any]) -> dict[str, Any]:
    merged = dict(cfg)
    merged["thresholds"] = {**_DEFAULT_THRESHOLDS, **(cfg.get("thresholds") or {})}
    merged["community_detection"] = {
        **_DEFAULT_COMMUNITY_DETECTION,
        **(cfg.get("community_detection") or {}),
    }
    merged.setdefault("extensions", {})
    merged.setdefault("anchors", None)
    return merged


def _check_trigger_strings(activation: dict[str, Any], lens_id: str) -> None:
    if activation.get("mode") != "triggers":
        return
    triggers = activation.get("triggers", [])
    for trig in triggers:
        if not isinstance(trig, str) or not _TRIGGER_RE.match(trig):
            raise LensValidationError(
                lens_id, f"invalid trigger DSL: {trig!r}"
            )


def _build_lens_config(
    cfg: dict[str, Any], source_path: Path
) -> LensConfig:
    lens_id = cfg["id"]
    if cfg["community_detection"]["algorithm"] not in _SUPPORTED_ALGORITHMS:
        raise LensValidationError(
            lens_id,
            f"unsupported community_detection.algorithm: "
            f"{cfg['community_detection']['algorithm']}",
        )
    _check_trigger_strings(cfg["activation"], lens_id)

    allowed = cfg.get("allowed_subdomains") or ()
    anchors_raw = cfg.get("anchors")
    return LensConfig(
        id=cfg["id"],
        version=cfg["version"],
        name=cfg["name"],
        description=cfg["description"],
        deliverable_types=tuple(cfg["deliverable_types"]),
        entity_model=MappingProxyType(dict(cfg["entity_model"])),
        activation=MappingProxyType(dict(cfg["activation"])),
        thresholds=MappingProxyType(dict(cfg["thresholds"])),
        anchors=MappingProxyType(dict(anchors_raw)) if anchors_raw else None,
        allowed_subdomains=tuple(allowed),
        community_detection=MappingProxyType(dict(cfg["community_detection"])),
        analysis_contract=MappingProxyType(dict(cfg.get("analysis_contract", {}))),
        extensions=MappingProxyType(dict(cfg.get("extensions", {}))),
        source_path=source_path.resolve(),
    )


def load_lens(
    lens_id: str, base: Path = DEFAULT_BASE
) -> LensConfig:
    """Load and validate a single lens by id.

    Raises:
        FileNotFoundError: the lens directory or lens.yaml is missing.
        LensValidationError: the YAML fails schema validation or has an
            internal inconsistency.
    """
    base = Path(base)
    lens_dir = base / lens_id
    lens_path = lens_dir / LENS_FILENAME
    if not lens_path.exists():
        raise FileNotFoundError(
            f"lens '{lens_id}' not found at {lens_path}"
        )
    raw = _read_yaml(lens_path, lens_id)
    schema = _load_schema(base)
    _validate_against_schema(raw, schema, lens_id)
    if raw.get("id") != lens_id:
        raise LensValidationError(
            lens_id,
            f"id in lens.yaml ({raw.get('id')!r}) does not match "
            f"directory name ({lens_id!r})",
        )
    with_defaults = _apply_defaults(raw)
    return _build_lens_config(with_defaults, lens_path)


def load_all_lenses(
    base: Path = DEFAULT_BASE,
) -> dict[str, LensConfig]:
    """Discover every `<base>/<id>/lens.yaml` and return a dict keyed by id.

    Skips directories starting with `_` (reserved for scaffolding) and any
    directory without a `lens.yaml`. Propagates LensValidationError from any
    malformed config — fail-loud on bad data.
    """
    base = Path(base)
    if not base.exists():
        return {}
    out: dict[str, LensConfig] = {}
    for lens_dir in sorted(base.iterdir()):
        if not lens_dir.is_dir():
            continue
        if lens_dir.name.startswith("_"):
            continue
        if not (lens_dir / LENS_FILENAME).exists():
            continue
        cfg = load_lens(lens_dir.name, base)
        out[cfg.id] = cfg
    return out


def _count_occurrences(content: str, frontmatter: dict[str, Any], slug: str) -> int:
    """Count tier-0/tier-1 reference occurrences for a given slug.

    Counts: wikilinks `[[slug]]` (case-sensitive), tags `#slug`, and any
    frontmatter list values (tags, type, lens) matching the slug.
    """
    if not slug:
        return 0
    wikilink = content.count(f"[[{slug}]]")
    tag = len(re.findall(rf"(?<![\w/-])#{re.escape(slug)}(?![\w/-])", content))
    fm_hits = 0
    for key in ("tags", "type", "lens", "domain"):
        val = frontmatter.get(key)
        if isinstance(val, list):
            fm_hits += sum(1 for v in val if v == slug)
        elif isinstance(val, str) and val == slug:
            fm_hits += 1
    return wikilink + tag + fm_hits


def _evaluate_triggers(
    activation: dict[str, Any], content: str, frontmatter: dict[str, Any]
) -> bool:
    mode = activation.get("mode")
    if mode == "always":
        return True
    if mode != "triggers":
        return False
    triggers = activation.get("triggers", [])
    if not triggers:
        return False
    for trig in triggers:
        m = _TRIGGER_RE.match(trig)
        if not m:
            return False
        slug, threshold = m.group(1), int(m.group(2))
        if _count_occurrences(content, frontmatter, slug) < threshold:
            return False
    return True


def activate_for_file(
    content: str,
    frontmatter: dict[str, Any],
    lenses: dict[str, LensConfig],
) -> list[str]:
    """Return lens ids that activate for a given file.

    Activation is determined by `lens.activation`:
      - `mode: always` → always active.
      - `mode: triggers` → every trigger `|<slug>| >= <int>` must match
        against wikilinks/tags/frontmatter references in the file.
    Returns ids in deterministic (sorted) order.
    """
    active: list[str] = []
    for lens_id, cfg in lenses.items():
        if _evaluate_triggers(cfg.activation, content, frontmatter):
            active.append(lens_id)
    return sorted(active)


def _cli_validate(argv: list[str]) -> int:
    """`python -m tools.lens_loader --validate <lens-id>`"""
    if len(argv) < 3 or argv[1] != "--validate":
        print("usage: python -m tools.lens_loader --validate <lens-id>")
        return 2
    target = argv[2]
    try:
        cfg = load_lens(target)
    except (FileNotFoundError, LensValidationError) as exc:
        print(f"INVALID: {exc}")
        return 1
    print(f"OK: {cfg.id} v{cfg.version} @ {cfg.source_path}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    import sys

    sys.exit(_cli_validate(sys.argv))
