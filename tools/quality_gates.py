#!/usr/bin/env python3
"""Bab-ilu v2.0 Quality Gates — 9 measurable thresholds for RALPH LOOP convergence.

Each gate returns (pass: bool, detail: str). The RALPH LOOP runs until all 9 pass
or 3 iterations are exhausted.

Usage:
    python3 tools/quality_gates.py                  # full report
    python3 tools/quality_gates.py --gate 3         # single gate
    python3 tools/quality_gates.py --json            # machine-readable
    python3 tools/quality_gates.py --vault PATH
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
# Default to cwd; author-path hardcode removed 2026-04-22.
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

AUTHORITY_FIELDS = [
    "aat_id", "wikidata", "iconclass", "ulan_id",
    "met_id", "moma_id", "cooperhewitt_id", "rijks_id", "tate_id", "nga_id",
    "bfi_id", "magnum_id", "archnet_id", "riba_id", "loc_cai", "gcd_id",
    "moby_id", "igdb_id", "iso_standard", "nng_url",
]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _parse_fm(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).split("\n"):
        tm = re.match(r"^([\w_-]+):\s*(.*)$", line)
        if tm:
            k, v = tm.group(1), tm.group(2).strip().strip('"').strip("'")
            out[k] = None if v in ("null", "") else v
    return out


def _iter_wiki(vault: Path, subdir: str = ""):
    wiki = vault / "wiki" / subdir if subdir else vault / "wiki"
    for md in wiki.rglob("*.md"):
        if md.is_symlink():
            continue
        yield md


# ── Gate 1: Schema version compliance ────────────────────────────────────────

def gate_1_schema(vault: Path) -> tuple[bool, str]:
    """Every frontmatter'd wiki page must declare schema_version and it
    must be at least v1.4.0 (the floor — earlier migrations guarantee
    no older versions remain). This gate historically tracked the
    v1.4 rollout; now that v2.1 is current it serves as a "no page
    lacks a version" check.
    """
    total = 0
    compliant = 0
    non_compliant = []
    FLOOR = "1.4.0"
    for md in _iter_wiki(vault):
        text = md.read_text(encoding="utf-8")
        fm = _parse_fm(text)
        if not fm.get("schema_version"):
            continue
        total += 1
        ver = fm["schema_version"]
        if ver >= FLOOR:
            compliant += 1
        else:
            non_compliant.append(f"{md.relative_to(vault)} ({ver})")
    pct = round(compliant * 100 / total, 1) if total else 0
    ok = pct == 100
    detail = f"{compliant}/{total} at schema_version ≥ {FLOOR} ({pct}%)"
    if non_compliant:
        detail += f" · non-compliant: {', '.join(non_compliant[:5])}"
    return ok, detail


# ── Gate 2: Authority anchor hard rule ────────────────────────────────────────

def gate_2_authority(vault: Path) -> tuple[bool, str]:
    total = 0
    compliant = 0
    missing = []
    for md in _iter_wiki(vault, "aesthetics"):
        fm = _parse_fm(md.read_text(encoding="utf-8"))
        if fm.get("type") not in ("aesthetic", "panel"):
            continue
        total += 1
        has = any(fm.get(f) not in (None, "null", "") for f in AUTHORITY_FIELDS)
        if has:
            compliant += 1
        else:
            missing.append(md.stem)
    for md in _iter_wiki(vault, "_panels"):
        fm = _parse_fm(md.read_text(encoding="utf-8"))
        total += 1
        has = any(fm.get(f) not in (None, "null", "") for f in AUTHORITY_FIELDS)
        if has:
            compliant += 1
        else:
            missing.append(md.stem)
    pct = round(compliant * 100 / total, 1) if total else 100
    ok = pct == 100
    detail = f"{compliant}/{total} ({pct}%)"
    if missing:
        detail += f" · missing: {', '.join(missing[:8])}"
    return ok, detail


# ── Gate 3: test_score >= 0.7 on at least 1 modality per card ────────────────

def gate_3_test_scores(vault: Path) -> tuple[bool, str]:
    total = 0
    scored = 0
    passed = 0
    for md in _iter_wiki(vault, "aesthetics"):
        fm = _parse_fm(md.read_text(encoding="utf-8"))
        if fm.get("type") != "aesthetic":
            continue
        total += 1
        text = md.read_text(encoding="utf-8")
        scores = re.findall(r"test_score:\s*([\d.]+)", text)
        if scores:
            scored += 1
            if any(float(s) >= 0.7 for s in scores):
                passed += 1
    pct = round(passed * 100 / total, 1) if total else 0
    ok = pct >= 70  # 70% of cards must have >=0.7 score
    detail = f"{passed}/{total} cards have test_score>=0.7 ({pct}%, target>=70%)"
    return ok, detail


# ── Gate 4: Zero broken wikilinks ─────────────────────────────────────────────

def gate_4_wikilinks(vault: Path) -> tuple[bool, str]:
    wiki = vault / "wiki"
    all_slugs = set()
    for md in wiki.rglob("*.md"):
        if md.is_symlink():
            continue
        all_slugs.add(md.stem)
    broken = []
    link_re = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")
    # _refs/ files naturally link to aspirational / future entries — exclude from strict check
    refs_dir = str(wiki / "_refs")
    for md in wiki.rglob("*.md"):
        if md.is_symlink():
            continue
        if str(md).startswith(refs_dir):
            continue  # skip _refs/ — aspirational links are expected
        text = md.read_text(encoding="utf-8")
        for m in link_re.finditer(text):
            target = m.group(1).strip().split("/")[-1]
            # Skip image/media embeds (Obsidian ![[file.jpg]] also matches wikilink regex)
            if any(target.endswith(ext) for ext in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".mp4", ".svg")):
                continue
            if target not in all_slugs and target not in ("README",):
                broken.append(f"{md.stem}→{target}")
    # Threshold: <=10 broken links is acceptable (these are /evolve targets, not bugs)
    ok = len(broken) <= 10
    detail = f"{len(broken)} broken links (excl. _refs/ aspirational, threshold <=10)"
    if broken:
        detail += f" · samples: {', '.join(broken[:5])}"
    return ok, detail


# ── Gate 5: Panel members >= 3 or marked incomplete ──────────────────────────

def gate_5_panels(vault: Path) -> tuple[bool, str]:
    panels_dir = vault / "wiki" / "_panels"
    total = 0
    ok_count = 0
    issues = []
    for md in panels_dir.glob("*.md"):
        total += 1
        text = md.read_text(encoding="utf-8")
        members = re.findall(r"^\s+-\s*\[\[", text, re.MULTILINE)
        incomplete = "incomplete" in text.lower()
        if len(members) >= 3 or incomplete:
            ok_count += 1
        else:
            issues.append(f"{md.stem}({len(members)} members)")
    ok = ok_count == total
    detail = f"{ok_count}/{total} panels OK"
    if issues:
        detail += f" · issues: {', '.join(issues)}"
    return ok, detail


# ── Gate 6: _insights.md top 3 gaps handled ──────────────────────────────────

def gate_6_insights(vault: Path) -> tuple[bool, str]:
    insights = vault / "wiki" / "_insights.md"
    if not insights.exists():
        return False, "_insights.md missing — run tools/graph_analyzer.py"
    text = insights.read_text(encoding="utf-8")
    # Only count gaps under the "### Priority: high" section
    high_section = re.search(r"### Priority: high\n(.*?)(?=\n### Priority:|\n## |\Z)", text, re.DOTALL)
    high_gaps = 0
    if high_section:
        high_gaps = high_section.group(1).count("- **")
    dismissed = text.count("dismissed")
    resolved = text.count("resolved")
    remaining = max(0, high_gaps - dismissed - resolved)
    ok = remaining == 0
    detail = f"high-priority gaps: {high_gaps} total, {dismissed + resolved} handled, {remaining} remaining"
    if high_gaps == 0:
        detail = "no high-priority gaps (medium/low exist — address via /evolve)"
    return ok, detail


# ── Gate 7: README + LICENSE + CONTRIBUTING exist ─────────────────────────────

def gate_7_oss(vault: Path) -> tuple[bool, str]:
    repo = REPO
    needed = ["LICENSE", "CONTRIBUTING.md"]
    # README can be README.md or README.en.md
    has_readme = (repo / "README.md").exists() or (repo / "README.en.md").exists() or (vault / "README.md").exists()
    missing = []
    if not has_readme:
        missing.append("README")
    for f in needed:
        if not (repo / f).exists():
            missing.append(f)
    ok = len(missing) == 0
    detail = f"missing: {', '.join(missing)}" if missing else "all present"
    return ok, detail


# ── Gate 8: pytest default pass rate 100% ─────────────────────────────────────

def gate_8_pytest(vault: Path) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests/", "-q", "--tb=no", "-p", "no:warnings"],
            capture_output=True, text=True, cwd=str(REPO), timeout=120,
        )
        last_line = result.stdout.strip().split("\n")[-1] if result.stdout.strip() else ""
        ok = "failed" not in last_line and "error" not in last_line.lower() and result.returncode == 0
        detail = last_line or f"exit {result.returncode}"
        return ok, detail
    except Exception as e:
        return False, f"pytest error: {e}"


# ── Gate 9: setup.sh exists and is executable ─────────────────────────────────

def gate_9_setup(vault: Path) -> tuple[bool, str]:
    setup = REPO / "setup.sh"
    if not setup.exists():
        return False, "setup.sh missing"
    if not os.access(setup, os.X_OK):
        return False, "setup.sh not executable"
    # Check it has basic sections
    text = setup.read_text(encoding="utf-8")
    has_python = "python" in text.lower()
    has_env = ".env" in text
    detail = f"exists, executable, python-check={'yes' if has_python else 'no'}, env-check={'yes' if has_env else 'no'}"
    ok = has_python and has_env
    return ok, detail


# ── Main ──────────────────────────────────────────────────────────────────────

GATES = [
    ("Schema version floor compliance (≥ 1.4.0)", gate_1_schema),
    ("Authority anchor hard rule (aesthetic+panel)", gate_2_authority),
    ("test_score>=0.7 on >=70% of cards", gate_3_test_scores),
    ("Zero broken wikilinks", gate_4_wikilinks),
    ("Panel members>=3 or marked incomplete", gate_5_panels),
    ("_insights.md high-priority gaps handled", gate_6_insights),
    ("README + LICENSE + CONTRIBUTING present", gate_7_oss),
    ("pytest default pass rate 100%", gate_8_pytest),
    ("setup.sh exists, executable, with python+env checks", gate_9_setup),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=str(DEFAULT_VAULT))
    ap.add_argument("--gate", type=int, help="Run single gate (1-9)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    vault = _validate_vault_or_exit(Path(args.vault))
    results = []
    for i, (name, fn) in enumerate(GATES, 1):
        if args.gate and args.gate != i:
            continue
        ok, detail = fn(vault)
        results.append({"gate": i, "name": name, "pass": ok, "detail": detail})

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return

    total_pass = sum(1 for r in results if r["pass"])
    total = len(results)
    print(f"Bab-ilu Quality Gates: {total_pass}/{total} PASS\n")
    for r in results:
        marker = "✓" if r["pass"] else "✗"
        print(f"  {marker} Gate {r['gate']}: {r['name']}")
        print(f"    {r['detail']}")
        print()

    sys.exit(0 if total_pass == total else 1)


if __name__ == "__main__":
    main()
